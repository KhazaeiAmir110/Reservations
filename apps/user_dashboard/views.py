from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.company.models import Company
from .forms import CompanyForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'backoffice/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['companies'] = Company.objects.filter(user=self.request.user)
        context['form'] = CompanyForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
        return self.get(request, *args, **kwargs)