from django.contrib.auth.models import User
from .models import SocialMediaUrl

def social_media_urls(request):
    profiles = SocialMediaUrl.objects.all()
    dict = {}
    for profile in profiles:
        dict[profile.site] = profile.url
    return dict