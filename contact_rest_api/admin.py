from django.contrib import admin
from contact_rest_api import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Contact)