from django.contrib import admin

from .models import Version, User, ToDo

admin.site.register(Version)
admin.site.register(User)
admin.site.register(ToDo)
