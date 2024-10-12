from django.contrib import admin
from user_request.models import ServiceRequestModel


class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('username', 'service_type', 'status', 'created_at', 'resolved_at')
    list_filter = ('status', 'service_type')
    search_fields = ('username', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    fields = ('username', 'address', 'description', 'service_type', 'status', 'file', 'created_at', 'resolved_at')
    readonly_fields = ('created_at',)

admin.site.register(ServiceRequestModel, ServiceRequestAdmin)
