# book/admin.py
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'public_visibility', 'birth_year', 'address', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('public_visibility', 'birth_year', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('public_visibility', 'birth_year', 'address')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
