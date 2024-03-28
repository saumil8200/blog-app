from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
             'first_name': 'Name',
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add classes and placeholders to form fields
        self.fields['first_name'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3 rounded-2xl',
            'placeholder': 'Enter name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3 rounded-2xl',
            'placeholder': 'Enter email'
        })

        self.fields['username'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3 rounded-2xl',
            'placeholder': 'Enter username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3 rounded-2xl',
            'placeholder': 'Enter Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3 rounded-2xl',
            'placeholder': 'Confirm password'
        })