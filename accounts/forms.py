from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Users, Profile





########################### USER SIGNUP FORM #########################

class UserRegistrationForm(UserCreationForm):
    first_name  = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'on', 'autofocus' : "on"}))
    last_name   = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'on'}))
    email       = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'placeholder' : "name@example.com", "type" : 'email', 'autocomplete': 'on', }))
    birthday    = forms.CharField(max_length=12, widget=forms.DateTimeInput(attrs={"type": "hidden"}))


    class Meta(UserCreationForm.Meta):
        model = Users
        # I've tried both of these 'fields' declaration, result is the same
        fields = ('first_name', 'last_name', 'email', 'birthday', 'gender', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = Users.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'





######################## USER LOGIN FORM #######################################

class UserLoginForm(forms.ModelForm):
    email    = forms.EmailField(max_length=100)
    password    = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'autocomplete':'on'}))
    class Meta:
        model = Users
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'





########################### Edit profile form ###############3333


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'pattern' : "[a-zA-Z0-9-._%+-]+", 'title': 'remove all spaces'}))
    birthday = forms.CharField(max_length=12, widget=forms.DateInput(attrs={"type": "hidden"}))
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'email', 'birthday', 'gender',)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture', 'bio')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'