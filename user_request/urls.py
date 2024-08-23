from django.urls import path
from . import views

urlpatterns = [path("", views.service_request, name="user_request")]
