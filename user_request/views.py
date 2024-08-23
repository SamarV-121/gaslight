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


@login_required
def view_requests(request):
    user_requests = ServiceRequestModel.objects.filter(username=request.user.username)

    return render(request, "view_requests.html", {"user_requests": user_requests})
