from django.shortcuts import render

def about(request):
    context = {
        'title': 'About Me',
        'page': 'about',
    }
    return render(request, 'user/about.html', context)

