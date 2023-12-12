from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .signals import send_notification

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            send_notification(sender=None, instance=user) 
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'yourapp/signup.html', {'form': form})
