from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from OAuth.models import newuser
# Register your models here.

class newuserAdmin(UserAdmin):
    filedsets = (
        (None, {'fileds': ('username', 'password')}),
        (_('Personal_info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser','user_permissions','roles')}),
    )

    list_display = ('id','username','roles','email','is_active')
    list_display_links = ('id','username','roles','is_active')
    search_fields = ('username', 'email')

admin.site.register(newuser, newuserAdmin)
