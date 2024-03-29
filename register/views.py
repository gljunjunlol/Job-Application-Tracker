from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

from django.contrib.auth import authenticate, login



# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
                                    
            return redirect("/")
    else:
        messages.error(request, "Your error message")
        form = RegisterForm()
    return render(request, "register/register.html", {"form":form})