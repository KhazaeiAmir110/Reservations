# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
#
# from .models import User, Profile
# from .forms import UserRegisterForm
#
#
# # class UserRegisterView(LoginRequiredMixin, generic.CreateView):
# #     form_class = UserRegisterForm
# #     template_name = 'userauths/sing-up.html'
# #     success_url = reverse_lazy('userauths:login')
#
# def RegisterView(request):
#     if request.user.is_authenticated:
#         messages.warning(request, 'شما قبلا وارد شده اید.')
#         return redirect('company:index')
#
#     form = UserRegisterForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         full_name = form.cleaned_data.get('full_name')
#         phone = form.cleaned_data.get('phone')
#         username = form.cleaned_data.get('username')
#         email = form.cleaned_data.get('email')
#         password = form.cleaned_data.get('password1')
#
#         user = authenticate(username=username, password=password)
#         login(request, user)
#
#         messages.success(request, "ثبت نام شما با موفقیت انجام شد.")
#
#         profile = Profile.objects.get(user=request.user)
#         profile.full_name = full_name
#         profile.phone = phone
#         profile.email = email
#         profile.save()
#
#         return redirect('company:index')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'userauths/sing-up.html', context)
#
#
# def LoginView(request):
#     if request.user.is_authenticated:
#         messages.warning(request, 'شما قبلا وارد شده اید.')
#         return redirect('company:index')
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         try:
#             user_query = User.objects.get(username=username)
#             user_auth = authenticate(request, username=user_query, password=password)
#
#             if user_auth is not None:
#                 login(request, user_auth)
#                 messages.success(request, 'شما وارد شدید!!')
#                 next_url = request.GET.get('next', 'company:index')
#                 return redirect(next_url)
#             else:
#                 messages.error(request, 'اشتباه است!!!!')
#                 return redirect('userauths:login')
#         except:
#             messages.error(request, 'ورود صورت نگرفت!!!!')
#             return redirect('userauths:login')
#     return render(request, 'userauths/login.html')
#
#
# def LogoutView(request):
#     logout(request)
#     messages.success(request, 'شما خارج شدید!!')
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import User, Profile
from .forms import UserRegisterForm


class UserRegisterView(LoginRequiredMixin, generic.CreateView):
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

        profile = Profile.objects.get(user=self.request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.email = email
        profile.save()

        return response


class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.warning(request, 'شما قبلا وارد شده اید.')
            return redirect('company:index')

        return render(request, 'userauths/login.html')

    def post(self, request):
        if request.user.is_authenticated:
            messages.warning(request, 'شما قبلا وارد شده اید.')
            return redirect('company:index')

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user_query = User.objects.get(username=username)
            user_auth = authenticate(request, username=user_query, password=password)

            if user_auth is not None:
                login(request, user_auth)
                messages.success(request, 'شما وارد شدید!!')
                next_url = request.GET.get('next', 'company:index')
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
