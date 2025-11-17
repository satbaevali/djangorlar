from django.contrib import admin

from user.models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'department','city', 'role', 'is_staff', 'is_active','salary','birth_date' ,'date_joined','country')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('department', 'role', 'is_staff', 'is_active')
    ordering = ('username',)
