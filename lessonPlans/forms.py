from django import forms
  
# import GeeksModel from models.py
from .models import FeedBack
  
# create a ModelForm
class FeedBackForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = FeedBack
        fields = "__all__"