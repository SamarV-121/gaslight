from django.db import models


class ServiceRequestModel(models.Model):
    username = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("addressed", "Addressed")],
        default="pending",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
