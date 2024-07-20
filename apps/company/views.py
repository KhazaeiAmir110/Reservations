import random

from django import forms
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView

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


class FormData(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'baraato/page2.html'

    def get_context_data(self, *args, **kwargs):
        # TODO: change name of dict keys to lower case.
        context = super().get_context_data(**kwargs)
        context.update(
            dict(
                holidays=HolidaysDate.objects.filter(company=context['company']),
                sansConfig=SansConfig.objects.filter(company=context['company']),
                sansHolidayDateTime=SansHolidayDateTime.objects.filter(company=context['company']),
                reservations=Reservation.objects.filter(company=context['company']),
                form=FormData(),
                code=random.randint(1000, 9999)
            )
        )
        return context

    # def post(self, request, *args, **kwargs):
    #     data = request.POST
    #     if (data.get('code') is None) or (int(data.get('code')) != self.rand):
    #         return HttpResponseRedirect(reverse('company:list-company'))
    #
    #     Reservation.objects.create(first_name=data.get('name'), last_name=data.get('family'),
    #                                phone_number=data.get('number'), email=data.get('email'),
    #                                company=Company.objects.get(slug=self.kwargs['slug']), date=data.get('date'),
    #                                time=data.get('time'))
    #
    #     url_name = reverse('company:payment', args=[self.kwargs['slug']])
    #     return HttpResponseRedirect(url_name)


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
        phone_number = request.POST.get('number')

        return JsonResponse({'status': 'success', 'phone_number': phone_number, 'title': 'Code Sent'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
