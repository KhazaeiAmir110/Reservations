from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, View
from django.urls import reverse_lazy

from apps.company.models import Company
from apps.userauths.models import User, Profile
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


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'backoffice/create-company.html'
    success_url = reverse_lazy('user_dashboard:profile')

    def form_valid(self, form, *args, **kwargs):
        form.instance.user = self.request
        messages.success(self.request, 'The Create Company Successfully')
        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'backoffice/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        pass
