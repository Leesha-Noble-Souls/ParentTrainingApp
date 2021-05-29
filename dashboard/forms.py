from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Parent

class ParentCreationForm(UserCreationForm):

    class Meta:
        model = Parent
        fields = ('username', 'email')


class ParentChangeForm(UserChangeForm):

    class Meta:
        model = Parent
        fields = ('username', 'email')
