from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import User, Profile
from .forms import UserRegisterForm


# class UserRegisterView(LoginRequiredMixin, generic.CreateView):
#     form_class = UserRegisterForm
#     template_name = 'userauths/sing-up.html'
#     success_url = reverse_lazy('userauths:login')

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما قبلا وارد شده اید.')
        return redirect('company:index')

    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name = form.cleaned_data.get('full_name')
        phone = form.cleaned_data.get('phone')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)
        login(request, user)

        messages.success(request,"ثبت نام شما با موفقیت انجام شد.")

        profile = Profile.objects.get(user=request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.email = email
        profile.save()

        return redirect('company:index')

    context = {
        'form': form,
    }
    return render(request, 'userauths/sing-up.html', context)

