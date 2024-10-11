from django.contrib.auth.password_validation import validate_password
from django import forms
from user_auth.models import CustomUserModel


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput, validators=[validate_password]
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not CustomUserModel.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "User not found. Please check your username and try again, if you care."
            )
        return username


class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput, validators=[validate_password]
    )
    contact = forms.CharField(max_length=12)
    address = forms.CharField(widget=forms.Textarea)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUserModel.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username already taken, Try being a bit more original."
            )
        return username
