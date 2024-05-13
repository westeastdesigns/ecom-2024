from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.shortcuts import redirect, render

from .forms import SignUpForm
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def about(request):
    return render(request, "about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # if the login is successful
            login(request, user)
            messages.success(request, ("You are now logged in. Welcome back!"))
            return redirect("home")

        else:
            # if the login is not successful
            messages.success(request, ("There was an error. Please try again."))
            return redirect("login")

    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out... Thanks for visiting!"))
    return redirect("home")


def register_user(request):
    form = SignUpForm()
    # if they fill out the form
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # log the user in
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been registered... Welcome!"))
            return redirect("home")
        else:
            # if the form is not valid
            messages.success(
                request,
                (
                    "Uh oh, there was an error. Please check all of your entries and try to register again."
                ),
            )
            return redirect("register")
    else:
        return render(request, "register.html", {"form": form})
