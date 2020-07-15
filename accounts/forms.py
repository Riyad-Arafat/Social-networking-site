from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Users





########################### USER SIGNUP FORM #########################

class UserRegistrationForm(UserCreationForm):
    first_name  = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'autocomplete': 'on', 'autofocus' : "on"}))
    last_name   = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'autocomplete': 'on'}))
    email       = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"type" : 'email', 'autocomplete': 'on', }))

    class Meta(UserCreationForm.Meta):
        model = Users
        # I've tried both of these 'fields' declaration, result is the same
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = Users.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email





######################## USER LOGIN FORM #######################################

class UserLoginForm(forms.ModelForm):
    email    = forms.EmailField(max_length=100)
    password    = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'autocomplete':'on'}))
    class Meta:
        model = Users
        fields = ( 'email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")