from django.contrib import admin
from .models import Face, Picture
# Register your models here.
admin.site.register((Face, Picture))