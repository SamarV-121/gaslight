from django.db import models


class ServiceRequestModel(models.Model):
    STATUS_CHOICES = [("pending", "Pending"), ("addressed", "Addressed")]
    SERVICE_TYPE_CHOICES = [
        ("maintainance", "Maintainance"),
        ("refill", "Refill"),
        ("leakage", "Leakage"),
        ("exchange", "Exchange"),
        ("payment", "Payment"),
        ("other", "Other"),
    ]

    username = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )
    file = models.FileField(upload_to="requests/", null=True, blank=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Service Request"
