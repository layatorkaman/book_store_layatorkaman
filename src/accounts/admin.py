from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Customer, CustomUser, Owner_site, Staff, Address


class StaffAdmin(UserAdmin):
    fieldsets = (
                    ('اطلاعات اوليه'), {'fields': ('username', 'first_name', 'last_name',)}),
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'is_staff')}),
    )
    list_display = ['id', 'email', 'username', 'is_staff']


def get_queryset(self, request):
    return get_user_model().objects.filter(is_staff=True, is_superuser=False)


admin.site.register(Staff, StaffAdmin)




admin.site.register(CustomUser)

admin.site.register(Owner_site)
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
                    ('اطلاعات اوليه'), {'fields': ('username', 'first_name', 'last_name',)}),
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email',)}),
    )
    list_display = ['id', 'email', 'username', ]
    # list_display = ['email', 'username','first_name']
admin.site.register(Customer , CustomerAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['city','street','postal_code','address_line1','address_line2','status']
    list_filter = ['city','customer']
    search_fields = ['city', 'customer']


admin.site.register(Address, AddressAdmin)
