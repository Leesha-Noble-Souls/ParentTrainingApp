from django.forms.widgets import CheckboxSelectMultiple
from lessonPlans.models import LessonFeedback
from django import forms

STATUS_CHOICES = [
    ('Beginning','Beginning'),
    ('Emerged','Emerged'),
    ('Completed','Completed')
]

PROMPTS_CHOICES=[
    ('Verbal','Verbal Prompt'),
    ('Physical','Physical Prompt'),
    ('Other','Other Clues')
]

FREQUENCY_CHOICES=[
    ('Irregular', 'Irregular'),
    ('Sometimes', 'Sometimes'),
    ('Regular', 'Regular'),
    ('Often', 'Often'),
]

class LessonFeedbackForm(forms.ModelForm):
    status = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=STATUS_CHOICES)
    frequency = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=FREQUENCY_CHOICES, label='Regularity')
    prompts= forms.MultipleChoiceField(required=True,choices=PROMPTS_CHOICES,widget=CheckboxSelectMultiple)

    class Meta:
        model = LessonFeedback
        fields = ['status', 'prompts', 'frequency', 'feedback']
        labels={'feedback':'Any Other Feedback'}
        widgets={}