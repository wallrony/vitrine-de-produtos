from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from vitrine_produtos.accounts.models import Profile


class ClientInline(admin.StackedInline):
    model = Profile
    verbose_name = 'Cliente'


class UserAdminModel(UserAdmin):
    inlines = [ClientInline]


admin.site.unregister(User)
admin.site.register(User, UserAdminModel)
