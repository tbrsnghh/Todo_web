from django import forms
from django.forms import ModelForm
from .models import Task
# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()