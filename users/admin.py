from django.contrib import admin

from users.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'username', "is_active",)
    search_fields = ('username', 'first_name', 'last_name',)
