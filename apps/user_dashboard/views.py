from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, View
from django.urls import reverse_lazy

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


# class CreateCompanyView(View):
#     def get(self, request, **kwargs):
#         form = CreateCompanyForm()
#         context = {'form': form}
#         return render(request, 'backoffice/create-company.html', context)
#
#     def post(self, request):
#         form = CreateCompanyForm(request.POST, request.FILES)
#         try:
#             if form.is_valid():
#                 demand = form.save(commit=False)
#                 demand.user = request.user
#                 demand.save()
#                 return redirect('user_dashboard:profile')
#         except Exception as e:
#             print(e)
#
#         context = {'form': form}
#         return render(request, 'backoffice/create-company.html', context)

class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'backoffice/create-company.html'
    success_url = reverse_lazy('user_dashboard:profile')

    def form_valid(self, form, *args, **kwargs):
        form.instance.user = self.request
        messages.success(self.request, 'The Create Company Successfully')
        return super().form_valid(form)
