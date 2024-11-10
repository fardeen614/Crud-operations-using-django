from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.TextField(max_length=100)
    receipe_description = models.TextField(max_length=200)

class Music(models.Model):
    music_name = models.TextField(max_length=200)
    music_description = models.TextField(max_length=200)
    music_image = models.ImageField(upload_to='receipet')




