from django.contrib import admin
from .models import CustomUser, AuthorPoint
from django.contrib.auth.models import Permission

admin.site.register(CustomUser)
admin.site.register(AuthorPoint)
admin.site.register(Permission)
