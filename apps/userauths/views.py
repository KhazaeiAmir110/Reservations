from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views import generic

from .forms import UserRegisterForm
from .models import User


class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'userauths/sing-up.html'
    success_url = reverse_lazy('userauths:login')

    def form_valid(self, form):
        response = super().form_valid(form)

        full_name = form.cleaned_data.get('full_name')
        phone = form.cleaned_data.get('phone')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)
        login(self.request, user)

        messages.success(self.request, "ثبت نام شما با موفقیت انجام شد.")

        return response


class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.warning(request, 'شما قبلا وارد شده اید.')
            return redirect('user_dashboard:profile')

        return render(request, 'userauths/login.html')

    def post(self, request):
        if request.user.is_authenticated:
            messages.warning(request, 'شما قبلا وارد شده اید.')
            return redirect('user_dashboard:profile')

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user_query = User.objects.get()
            user_auth = authenticate(request, username=user_query, password=password)

            if user_auth is not None:
                login(request, user_auth)
                messages.success(request, 'شما وارد شدید!!')
                next_url = request.GET.get('next')
                return redirect(next_url)
            else:
                messages.error(request, 'اشتباه است!!!!')
                return redirect('userauths:login')
        except User.DoesNotExist:
            messages.error(request, 'ورود صورت نگرفت!!!!')
            return redirect('userauths:login')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'شما خارج شدید!!')
        return redirect('company:index')
