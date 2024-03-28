from django.forms import ModelForm, Textarea
from django import forms
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['category', 'title', 'description',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add classes and placeholders to form fields
        self.fields['category'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3 rounded-2xl font-light',
        })
        self.fields['title'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3 rounded-2xl',
            'placeholder': 'Enter title'
        })
        # Set the Textarea widget for the description field and adjust its attributes
        self.fields['description'].widget = Textarea(attrs={
            'class': 'w-full bg-[#F5F5F5] p-3 rounded-2xl',
            'placeholder': 'Enter description',
            'rows': 15  # Number of visible rows
        })

        # Set a default placeholder or initial value for the category field
        self.fields['category'].empty_label = 'Select category'