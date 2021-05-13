from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo

class Gallery(ListView):
    model = Photo
    ordering = ['-created']
    template_name = 'gallery/index.html'
    context_object_name = 'photos'
    extra_context = {
        'title': 'Gallery',
        'page': 'gallery',
    }