from django.contrib import admin
from main.models import PreviousJob, Company


# Register your models here.
admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to the Admin Dashboard"
admin.site.register(PreviousJob)
admin.site.register(Company)

