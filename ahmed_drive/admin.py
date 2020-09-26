from django.contrib import admin
from .models import Folder, Fileshare

# Register your models here.
admin.site.register(Folder)
admin.site.register(Fileshare)