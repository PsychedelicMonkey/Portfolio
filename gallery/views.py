from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Photo, Collection

def viewer(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return JsonResponse({'url': photo.imageUrl})

def collection_preview(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    photos = collection.photos.all()[:4]
    return JsonResponse([{'url': photo.imageUrl} for photo in photos], safe=False)

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