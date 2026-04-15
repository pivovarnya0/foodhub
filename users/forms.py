from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.help_text = None
            field.label = ''

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-control auth-input'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'class': 'form-control auth-input'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-control auth-input'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repeat password',
            'class': 'form-control auth-input'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        if email and '@' not in email:
            raise forms.ValidationError('Email must contain @')
        return email


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.label = ''

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-control auth-input'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-control auth-input'
        })
