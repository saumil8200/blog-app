from django.forms import ModelForm
from django import forms
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['featured_image', 'title', 'description', 'category', 'tags',]