from django.shortcuts import render
from django.contrib.auth.models import User

def about(request):
    user = User.objects.get(pk=1)
    context = {
        'title': 'About Me',
        'page': 'about',
        'user': user,
    }
    return render(request, 'user/about.html', context)

