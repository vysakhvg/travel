from django.contrib import admin

# Register your models here.
from .models import  data, team

admin.site.register(data)
admin.site.register(team)