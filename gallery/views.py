from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Photo, Collection

class Gallery(ListView):
    model = Photo
    ordering = ['-created']
    template_name = 'gallery/index.html'
    context_object_name = 'photos'
    extra_context = {
        'title': 'Gallery',
        'page': 'gallery',
    }

class CollectionListView(ListView):
    model = Collection
    ordering = ['-created']
    template_name = 'gallery/collections.html'
    context_object_name = 'collections'
    extra_context = {
        'title': 'Collections',
        'page': 'collections',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'gallery/collection_detail.html'