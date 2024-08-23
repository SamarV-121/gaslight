from django.shortcuts import render, redirect
from django.contrib import auth, messages

from user_auth.models import CustomUserModel


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = CustomUserModel.objects.filter(username=username)

        if not user.exists():
            messages.error(
                request,
                "User not found. Please check your username and try again, if you care.",
            )
            return redirect("login")

        auth_user = auth.authenticate(username=username, password=password)

        if auth_user is not None:
            auth.login(request, auth_user)
            return redirect("home")
        else:
            messages.error(request, "Wrong credentials")
            return redirect("login")

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
            messages.error(
                request, "Username already taken, Try being a bit more original"
            )
            return redirect("register")

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
