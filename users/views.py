from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import registerUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required as is_logedIn
from .forms import addProfile
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = registerUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account is ready you can login now {username}!')
            return redirect('login')
    else:
        form = registerUser()
    return render(request, 'users/register.html', {'form': form})

@is_logedIn
def profile(request):
    form = Profile
    context = {'form':form}
    return render(request, 'users/profile.html', context)


def addImage(request):
    if request.method == 'POST':
        form = addProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        form = addProfile()
    return render(request, 'users/profile_img.html', {'form':form} )

