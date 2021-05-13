from django.db import models

class Photo(models.Model):
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def imageUrl(self):
        try:
            img = self.image.url
        except:
            img = ''
        return img
