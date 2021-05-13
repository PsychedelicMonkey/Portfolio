from django.shortcuts import render

def index(request):
    context = {
        'title': 'Gallery',
        'page': 'gallery',
    }
    return render(request, 'gallery/index.html', context)

def about(request):
    context = {
        'title': 'About Me',
        'page': 'about',
    }
    return render(request, 'gallery/about.html', context)
