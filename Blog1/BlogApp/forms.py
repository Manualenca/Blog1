#from .forms import CrearForm
from django.shortcuts import render, redirect
from django import forms 
from.models import Post
class CrearForm(forms.ModelForm):
    def Create_post_New(request):
        if request.method == 'POST':
            form = CrearForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('CrearPostView')
        else:
            form = CrearForm()
        return render(request,'post_create.html',{'form': form})

    