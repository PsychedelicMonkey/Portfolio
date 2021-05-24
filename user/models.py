from PIL import Image
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

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            if img.height > 400 or img.height > 400:
                output_size = (400, 400)
                img.thumbnail(output_size, Image.ANTIALIAS)
                img.save(self.image.path)

class SocialMediaUrl(models.Model):
    CHOICES = (
        ('YOUTUBE', 'YouTube'),
        ('FACEBOOK', 'Facebook'),
        ('TWITTER', 'Twitter'),
        ('PINTEREST', 'Pinterest'),
        ('INSTAGRAM', 'Instagram'),
        ('LINKEDIN', 'LinkedIn'),
        ('GITHUB', 'GitHub'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    site = models.CharField(max_length=20, choices=CHOICES, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.site}'