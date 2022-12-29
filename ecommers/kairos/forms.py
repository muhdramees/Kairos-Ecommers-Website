from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import Form



class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'email'


class LoginForm (forms.Form):
    email = forms.EmailField(label="email", max_length=100)
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class SignupForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=200, required=True)
    last_name = forms.CharField(label="Last Name", max_length=200, required=True)
    username = forms.CharField(label="Username", max_length=100, required=True)
    email = forms.EmailField(label="Email", max_length=100)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Re-type Password", widget=forms.PasswordInput)



