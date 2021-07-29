from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Password',
            'id': 'password',
        }
    ))


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=50, help_text='Required')
    last_name = forms.CharField(label='Last Name', max_length=50, help_text='Required')
    username = forms.CharField(label='Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required',
                             error_messages={'required': 'Please, type a valid email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password Confirm', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_username(self):
        cleaned_name = self.cleaned_data['username'].lower()
        duplication = User.objects.filter(username=cleaned_name)

        if duplication.count():
            raise forms.ValidationError('Username already exists')

        return cleaned_name

    def clean_password_confirm(self):
        cleaned_data = self.cleaned_data

        if cleaned_data['password'] != cleaned_data['password_confirm']:
            raise forms.ValidationError('Passwords do not macth')

        return cleaned_data['password_confirm']

    def clean_email(self):
        cleaned_email = self.cleaned_data['email']
        duplication = User.objects.filter(email=cleaned_email)

        if duplication.exists():
            raise forms.ValidationError('Email already exists')

        return cleaned_email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Last Name'})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password_confirm'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password Confirmation'})
