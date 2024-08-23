from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from user_request.models import ServiceRequestModel


@login_required
def service_request(request):
    if request.method == "POST":
        message = request.POST.get("message")

        data = ServiceRequestModel(
            username=request.user.username,
            address=request.user.address,
            description=message,
        )

        data.save()
    return render(request, "request.html")
