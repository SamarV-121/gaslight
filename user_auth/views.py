from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from user_auth.models import CustomUserModel


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not CustomUserModel.objects.filter(username=username).exists():
            return HttpResponse("Username not found, Bitch")

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return HttpResponse(f"WTF - {user}")

    return render(request, "login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home")


def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        contact = request.POST.get("contact")
        address = request.POST.get("address")

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
