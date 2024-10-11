from django import forms

from user_request.models import ServiceRequestModel


class RequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequestModel
        fields = ["service_type", "description", "file"]
