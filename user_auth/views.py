from django.shortcuts import render, redirect
from django.contrib import auth, messages

from user_auth.forms import LoginForm, RegisterForm
from user_auth.models import CustomUserModel


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        form_data = {"form": form}

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            auth_user = auth.authenticate(username=username, password=password)

            if auth_user is not None:
                auth.login(request, auth_user)
                return redirect("home")
            else:
                messages.error(request, "Wrong credentials")
                return redirect("login")
        else:
            return render(request, "login.html", form_data)
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        form_data = {"form": form}

        if form.is_valid():
            full_name = form.cleaned_data.get("full_name")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            contact = form.cleaned_data.get("contact")
            address = form.cleaned_data.get("address")

            data = CustomUserModel(
                full_name=full_name,
                username=username,
                contact=contact,
                address=address,
            )
            data.set_password(password)
            data.save()

            return redirect("login")
        else:
            return render(request, "register.html", form_data)
    return render(request, "register.html")
