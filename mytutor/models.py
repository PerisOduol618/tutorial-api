from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.


class Tutorial(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    content = models.TextField(max_length=400)
    link = models.URLField(max_length= 100)
    published = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_created=True)


