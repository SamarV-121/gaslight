from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth

from user_auth.models import CustomUserModel


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = CustomUserModel.objects.filter(username=username)

        if not user.exists():
            return HttpResponse("Username not found, Bitch")

        auth_user = auth.authenticate(username=username, password=password)

        if auth_user is not None:
            auth.login(request, auth_user)
            return redirect("home")
        else:
            return HttpResponse("Wrong credentials, Bitch")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        contact = request.POST.get("contact")
        address = request.POST.get("address")

        user = CustomUserModel.objects.filter(username=username)

        if user.exists():
            return HttpResponse("Username already taken, Bitch")

        data = CustomUserModel(
            full_name=full_name,
            username=username,
            contact=contact,
            address=address,
        )
        data.set_password(password)

        data.save()
        return redirect("login")

    return render(request, "register.html")
