from django.contrib import admin

from user.models import User




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "password", "first_name", "last_name", "created_at", "updated_at", "is_staff", "is_active", "is_superuser")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['email'].disabled = True
            form.base_fields['password'].disabled = True
            form.base_fields['first_name'].disabled = True
            form.base_fields['last_name'].disabled = True
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['user_permissions'].disabled = True
            form.base_fields['groups'].disabled = True
        return form



# class ReadOnlyAdminMixin:

#     def has_add_permission(self, request):
#         return True

#     def has_change_permission(self, request, obj=None):
#         return False

#         # if request.user.has_perm('inventory.change_product'):
#         #     return True
#         # else:
#         #     return False

#     def has_delete_permission(self, request, obj=None):
#         return False

#     def has_view_permission(self, request, obj=None):
#         return True