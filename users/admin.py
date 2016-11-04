from django.contrib import admin
from .models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'created', 'updated')

admin.site.register(UserInfo, UserInfoAdmin)
