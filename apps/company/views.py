from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .models import Company


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
