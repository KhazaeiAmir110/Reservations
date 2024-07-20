from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView
from kavenegar import KavenegarAPI

from reservations.secret import kavenegar
from .models import Company, HolidaysDate, SansConfig, SansHolidayDateTime, Reservation


class CompanyListView(ListView):
    model = Company
    template_name = 'baraato/page1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(companies=Company.objects.all())
        return context

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(
            reverse(
                'company:detail-company-baraato', args=[request.POST.get('company_slug')]
            )
        )


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'baraato/page2.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            dict(
                holidays=HolidaysDate.objects.filter(company=context['company']),
                sansconfig=SansConfig.objects.filter(company=context['company']),
                sansholidaydatetime=SansHolidayDateTime.objects.filter(company=context['company']),
                reservations=Reservation.objects.filter(company=context['company']),
            )
        )
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        if (data.get('code') is None) or (int(data.get('code')) != kavenegar.code):
            return HttpResponseRedirect(reverse('company:detail-company-baraato',
                                                args=[kwargs['slug']]))

        url_name = reverse('company:payment', args=[self.kwargs['slug']])
        return HttpResponseRedirect(url_name)


class PaymentView(ListView):
    model = Company
    template_name = 'baraato/page4.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.get(slug=self.kwargs['slug'])
        return context


# send code
def send_code(request):
    if request.method == 'POST':
        # save information user in session
        request.session['name'] = request.POST.get('name'),
        request.session['family'] = request.POST.get('family'),
        request.session['number'] = request.POST.get('number'),
        request.session['email'] = request.POST.get('email'),
        request.session['time'] = request.POST.get('time'),
        request.session['date'] = request.POST.get('date'),

        # send code to number
        api = KavenegarAPI(kavenegar.API_KEY)
        params = {
            'receptor': request.POST.get('number'),
            'message': f'کد تأیید : {kavenegar.code}\n سیستم رزرواسیون و نوبت دهی براتو'
        }

        api.sms_send(params)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
