from django.shortcuts import render
from django.views import View

from .models import Company, Category


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
