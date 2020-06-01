from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.mail import send_mail
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # send_mail(
            #     'Welcome',
            #     'Welcome to black gram',
            #     settings.EMAIL_HOST_USER,
            #     ['mwaaruth@gmail.com'],
            #     fail_silently=False,
            # )
            form.save()
            username = form.cleaned_data.get('username')
            email =form.cleaned_data.get(email)
            messages.success(request, f'Account created for {username}!')
            
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'find/register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'find/profile.html',context)

def send(request):
    send_mail(
    'Welcome',
    'Welcome to black gram',
    'ruthwanjiramugo@gmail.com',
    ['mwaaruth@gmail.com'],
    fail_silently=False,
)


    return render(request,'find/send.html')