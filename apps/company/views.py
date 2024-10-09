import json
import requests

from django.views import View
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse

from reservations.secret import mediana
from reservations.secret import zarinpal
from .models import Company, HolidaysDate, SansConfig, SansHolidayDateTime, Reservation


class CompanyListView(ListView):
    model = Company
    template_name = 'baraato/page1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(companies=Company.objects.all())
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        action = data.get('company_slug')
        request.session['company_slug'] = data.get('company_slug')
        url_name = reverse('company:detail-company-baraato', args=[action])
        return HttpResponseRedirect(url_name)


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
        if (data.get('code') is None) or (int(data.get('code')) != mediana.code):
            return HttpResponseRedirect(reverse('company:detail-company-baraato',
                                                args=[kwargs['slug']]))

        url_name = reverse('company:payment_view', args=[self.kwargs['slug']])
        return HttpResponseRedirect(url_name)


class PaymentView(ListView):
    model = Company
    template_name = 'baraato/page4.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(company=Company.objects.get(slug=self.kwargs['slug']))

        return context

    def post(self, request, *args, **kwargs):
        datas = request.POST
        if datas.get('zarin'):
            data = {
                "MerchantID": zarinpal.MERCHANT,
                "Amount": zarinpal.amount,
                "Description": zarinpal.description,
                "Phone": zarinpal.phone,
                "CallbackURL": zarinpal.CallbackURL,
            }

            data = json.dumps(data)
            # set content length by data
            headers = {
                'content-type': 'application/json',
                'content-length': str(len(data))
            }
            try:
                response = requests.post(zarinpal.ZP_API_REQUEST, data=data, headers=headers)

                if response.status_code == 200:
                    response = response.json()
                    if response['Status'] == 100:
                        return redirect(f'{zarinpal.ZP_API_STARTPAY}{response["Authority"]}')
                    else:
                        return {'status': False, 'code': str(response['Status'])}
                return response

            except requests.exceptions.Timeout:
                return {'status': False, 'code': 'timeout'}
            except requests.exceptions.ConnectionError:
                return {'status': False, 'code': 'connection error'}
        else:
            url = reverse('company:payment_view', args=[self.kwargs['slug']]) + '?error=ERROR : IS NOT FOUND'
            return HttpResponseRedirect(url)


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
        mediana.api.send(
            sender=mediana.sender,
            recipients=[request.POST.get('number'), ],
            message=f'کد تأیید : {mediana.code}\n سیستم رزرواسیون و نوبت دهی براتو',
            summary=mediana.summary
        )

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


# zarinpal

class VerifyPaymentView(View):
    def get(self, request):
        data = {
            "MerchantID": zarinpal.MERCHANT,
            "Amount": zarinpal.amount,
            "Authority": request.GET.get('Authority')
        }
        data = json.dumps(data)
        headers = {
            'content-type': 'application/json',
            'content-length': str(len(data))
        }

        response = requests.post(zarinpal.ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                # send sms Success reserve
                Reservation.objects.create(
                    first_name=request.session['name'][0],
                    last_name=request.session['family'][0],
                    phone_number=request.session['number'][0],
                    email=request.session['email'][0],
                    time=request.session['time'][0],
                    date=request.session['date'][0],
                    company=Company.objects.get(slug=request.session['company_slug'])
                )
                mediana.api.send(
                    sender=mediana.sender,
                    recipients=[request.session['number'], ],
                    message="ثبت نام شما با موفقیت انجام شد.",
                    summary=mediana.summary
                )
                return render(request, 'baraato/page5.html')
            elif response['Status'] == 101:
                return HttpResponse("transaction already")

        return HttpResponse('Invalid Not Payment')
