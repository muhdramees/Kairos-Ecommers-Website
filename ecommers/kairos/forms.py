from django.contrib.auth.forms import AuthenticationForm
from django import forms

class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'


class LoginForm (forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


