from django.shortcuts import render, redirect
from django import forms 
from .models import Post


class CrearForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'image','categories']
        exclude = ['reporter']
        forms.ModelChoiceField(queryset=model.objects.all())
    ''' widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'reporter': forms.Select(attrs={'class': 'form-control'})
        }
    '''