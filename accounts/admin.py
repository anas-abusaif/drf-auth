from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import UserCreationForm
from accounts.models import User
# Register your models here.


class User_Admin(UserAdmin):
  add_form = UserCreationForm
  model = User
  fieldsets = UserAdmin.fieldsets
  add_fieldsets = ((None,{'fields':('username', 'email', 'first_name', 'last_name', 'password')}),)


admin.site.register(User, User_Admin)
