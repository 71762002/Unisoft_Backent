from django.contrib import admin

from user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "password", "first_name", "last_name", "created_at", "updated_at", "is_staff", "is_active", "is_superuser")

