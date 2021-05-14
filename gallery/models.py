from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

    @property
    def imageUrl(self):
        try:
            img = self.image.url
        except:
            img = ''
        return img

class Collection(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    photos = models.ManyToManyField(Photo, related_name='collections')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_photos(self):
        return self.photos.all()