from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from hello.models import C

class MakeForm(ModelForm):
    class Meta:
        model = C
        fields = '__all__'

class BasicForm(forms.Form):
    title = forms.CharField(validators=[
        validators.MinLengthValidator(2, "Please enter 2 or more characters")
    ])
    description = forms.CharField()
