from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images')
    display_image_left = models.BooleanField(default=True)


# Create your models here.
