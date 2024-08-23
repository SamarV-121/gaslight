from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from user_request.models import ServiceRequestModel


@login_required
def service_request(request):
    if request.method == "POST":
        message = request.POST.get("message")
        service_type = request.POST.get("service_type")

        data = ServiceRequestModel(
            username=request.user.username,
            address=request.user.address,
            description=message,
            service_type=service_type,
        )

        data.save()

    service_type_choices = ServiceRequestModel.SERVICE_TYPE_CHOICES
    return render(
        request, "request.html", {"service_type_choices": service_type_choices}
    )


@login_required
def view_requests(request):
    user_requests = ServiceRequestModel.objects.filter(username=request.user.username)

    return render(request, "view_requests.html", {"user_requests": user_requests})
