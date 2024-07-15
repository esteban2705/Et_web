from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']

class JournalistForm(forms.ModelForm):
    class Meta:
        model = Journalist
        fields = ['first_name', 'last_name', 'email', 'bio']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


