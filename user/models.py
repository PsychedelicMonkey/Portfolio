from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def imageUrl(self):
        try:
            img = self.image.url
        except:
            img = ''
        return img
