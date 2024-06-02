from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from datetime import date, timedelta
from django.views.generic import ListView, DetailView

from .models import Company, Category, WorkTime, WorkDate


class HomeView(View):
    def get(self, request, category_slug=None):
        companies = Company.objects.all()
        categories = Category.objects.filter(is_subb=False, status=True)
        golden_companies = Company.objects.filter(golden=True, status=True)
        if category_slug:
            category = Category.objects.get(slug=category_slug, status=True)
            companies = Company.objects.filter(category=category, status=True)
        context_data = {
            'companies': companies,
            'categories': categories,
            'golden_companies': golden_companies
        }
        return render(request, 'company/index.html', context_data)


class CompanyDetailView(View):
    def get(self, request, company_slug, date_time=None):
        WorkDate.delete_past_dates()
        start_time = date.today()
        end_time = start_time + timedelta(days=30)

        company = Company.objects.get(slug=company_slug)
        work_dates = WorkDate.objects.filter(company=company, date__range=[start_time, end_time])

        context_data = {
            'company': company,
            'work_dates': work_dates,
        }

        if date_time:
            work_date = WorkDate.objects.get(company__slug=company_slug, date=date_time)
            work_time = WorkTime.objects.filter(work_date=work_date)
            # work_time = work_time.order_by('start_time')
            context_data = {'work_time': work_time, 'company': company, 'work_dates': work_dates,
                            'work_date': work_date}

        return render(request, 'company/detail-company.html', context=context_data)


# Baraato.com
"""
    work with forms : https://realpython.com/django-social-post-3/
    fix bug redirect : https://stackoverflow.com/questions/34465617/disallowedredirect-unsafe-redirect-to-url-with-protocol-django
    redirect : https://www.scaler.com/topics/django/django-reverse/
"""


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
        # return HttpResponseRedirect(reversed('company:detail-company-baraato/'))
        url_name = reverse('company:detail-company-baraato', args=[action])
        return HttpResponseRedirect(url_name)


class CompanyDetail(DetailView):
    model = Company
    template_name = 'baraato/page2.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.filter(slug=self.kwargs['slug'])
        return context
