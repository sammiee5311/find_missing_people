from django import forms
from .models import MissingPeople


class RequestForm(forms.ModelForm):
    class Meta:
        model = MissingPeople
        fields = ('name', 'image_url', 'email')