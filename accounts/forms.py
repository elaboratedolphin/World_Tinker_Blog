
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserCreationForm
# from accounts.models import UserProfileInfo



# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password')

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 widget= forms.TextInput
                                (attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=100,
                                widget= forms.TextInput
                               (attrs={'placeholder':'Last Name'}))
    username = forms.CharField(max_length=100,
                               widget= forms.TextInput
                              (attrs={'placeholder':'Username'}))
    email = forms.CharField(max_length=100,
                            widget= forms.EmailInput
                           (attrs={'placeholder':'Email'}))
    password1 = forms.CharField(max_length=100,
                                widget= forms.PasswordInput
                               (attrs={'placeholder':'Password'}))
    password2 = forms.CharField(max_length=100,
                                widget= forms.PasswordInput
                               (attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
