from django.contrib import admin
from .models import Aircraft, Gram, Report

# Register your models here.

admin.site.register(Aircraft)
admin.site.register(Gram)
admin.site.register(Report)