from django import forms

class LoginForm(forms.Form):
   username = forms.CharField(max_length=150)
   password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
   username = forms.CharField(max_length=150)
   password = forms.CharField(widget=forms.PasswordInput)
   confirm_password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.Form):
   username = forms.CharField(max_length=150)
   img = forms.ImageField()
   bio = forms.CharField(max_length=100)
