from django import forms

class adduser(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=200, required=True)
    last_name = forms.CharField(label="Last Name", max_length=200, required=True)
    username = forms.CharField(label="Username", max_length=100, required=True)
    email = forms.EmailField(label="Email", max_length=100)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Re-type Password", widget=forms.PasswordInput)    




