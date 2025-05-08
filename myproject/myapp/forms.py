from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Blog

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = ''
        self.fields['username'].label = 'Username '
        self.fields['username'].widget.attrs.update({
            'placeholder': ' username',
            'class': 'input-field'
        })
        self.fields['password1'].help_text = ''
        self.fields['password1'].label = 'Password1 '
        self.fields['password1'].widget.attrs.update({
            'placeholder': ' password',
            'class': 'input-field'
        })
        self.fields['password2'].help_text = ''
        self.fields['password2'].label = 'Password2 '
        self.fields['password2'].widget.attrs.update({
            'placeholder': ' confirm password',
            'class': 'input-field'
        })
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': ' username',
            'class': 'input-field',
            'autocomplete': 'off'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': ' password',
            'class': 'input-field',
            'autocomplete': 'new-password'
        })
    )

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['user_name', 'blog_text'] 