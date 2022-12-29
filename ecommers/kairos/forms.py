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
    

