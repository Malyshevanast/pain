from django import forms
from django.core.exceptions import ValidationError
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['doctor', 'text']
    providers = forms.ModelMultipleChoiceField(queryset=Record.objects.all(), widget=forms.CheckboxSelectMultiple)

