from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

import random

from .models import Company, HolidaysDate, SansConfig, SansHolidayDateTime, Reservation


class CompanyListView(ListView):
    model = Company
    template_name = 'baraato/page1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        action = data.get('company_slug')
        url_name = reverse('company:detail-company-baraato', args=[action])
        return HttpResponseRedirect(url_name)


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'baraato/page2.html'

    rand = random.randint(1000, 9999)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.get(slug=self.kwargs['slug'])
        context['holidays'] = HolidaysDate.objects.filter(company=context['company'])
        context['sansConfig'] = SansConfig.objects.filter(company=context['company'])
        context['sansHolidayDateTime'] = SansHolidayDateTime.objects.filter(company=context['company'])
        context['reservations'] = Reservation.objects.filter(company=context['company'])
        context['code-rand'] = self.rand
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        if (data.get('code-rand') is None) or (data.get('code-rand') != self.rand):
            return HttpResponseRedirect(reverse('company:list-company'))

        Reservation.objects.create(first_name=data.get('name'), last_name=data.get('family'),
                                   phone_number=data.get('number'), email=data.get('email'),
                                   company=Company.objects.get(slug=self.kwargs['slug']), date=data.get('date'), time=data.get('time'))
        # url_name = reverse('company:detail-company-baraato', args=[action])
        # return HttpResponseRedirect(url_name)
