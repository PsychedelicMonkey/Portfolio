from django.conf import settings
from django.core import paginator
from django.core.paginator import Paginator
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
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
    paginate_by = settings.ITEMS_PER_PAGE
    extra_context = {
        'title': 'Gallery',
        'page': 'gallery',
    }

class CollectionListView(ListView):
    model = Collection
    ordering = ['-created']
    template_name = 'gallery/collections.html'
    context_object_name = 'collections'
    paginate_by = settings.ITEMS_PER_PAGE
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

    def get_context_data(self, **kwargs):
        photos = self.get_object().get_photos()
        paginator = Paginator(photos, settings.ITEMS_PER_PAGE)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)
        context = super().get_context_data(**kwargs)
        context['page_obj'] = page_obj
        return context

class ArchiveYear(YearArchiveView):
    queryset = Photo.objects.all()
    paginate_by = settings.ITEMS_PER_PAGE
    date_field = 'created'
    make_object_list = True
    allow_future = True
    extra_context = {
        'page': 'archives'
    }

class ArchiveMonth(MonthArchiveView):
    queryset = Photo.objects.all()
    paginate_by = settings.ITEMS_PER_PAGE
    date_field = 'created'
    make_object_list = True
    allow_future = True
    extra_context = {
        'page': 'archives'
    }