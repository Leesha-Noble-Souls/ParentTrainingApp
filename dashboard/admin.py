from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ParentCreationForm, ParentChangeForm
from .models import Parent

class ParentAdmin(UserAdmin):
    add_form = ParentCreationForm
    form = ParentChangeForm
    model = Parent
    list_display = ['email', 'username', ]


admin.site.register(Parent, ParentAdmin)
