from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from user_request.forms import RequestForm
from user_request.models import ServiceRequestModel


@login_required
def service_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                data = form.save(commit=False)
                data.username = request.user.username
                data.address = request.user.address
                data.save()
                messages.success(request, "Submitted the request!")
            except Exception:
                messages.error(request, "Error occured while submitting your data")
                return render(request, "register.html", {'form': form})
    else:
        form = RequestForm()

    return render(
        request, "request.html", {'form': form}
    )


@login_required
def view_requests(request):
    user_requests = ServiceRequestModel.objects.filter(username=request.user.username)

    return render(request, "view_requests.html", {"user_requests": user_requests})
