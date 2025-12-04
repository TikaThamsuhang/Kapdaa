from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'phone_number', 'is_active', 'is_admin')
    list_display_links = ('email', 'first_name', 'last_name', 'username', 'phone_number')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = () 
    fieldsets = ()

# Register your models here.
admin.site.register(Account, AccountAdmin)
