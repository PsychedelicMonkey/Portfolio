from django.shortcuts import render

def index(request):
    context = {
        'title': 'Gallery',
        'page': 'gallery',
    }
    return render(request, 'gallery/index.html', context)