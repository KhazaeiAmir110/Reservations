from django.shortcuts import render
from django.views import View
from datetime import date, timedelta

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
            context_data = {'work_time': work_time, 'company': company, 'work_dates': work_dates,'work_date':work_date}

        return render(request, 'company/detail-company.html', context=context_data)


# Page 3
# class WorkTimeView(View):
#     def get(self, request, company_slug, date):
#         work_date = WorkDate.objects.get(company__slug=company_slug, date=date)
#         work_time = WorkTime.objects.filter(work_date=work_date)
#         return render(request, 'company/work_hours.html', {'work_time': work_time})
