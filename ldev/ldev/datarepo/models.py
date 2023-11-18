from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.
class Home(models.Model):
    image = models.ImageField(upload_to='images/')
    title = RichTextField()
    slug = models.CharField(max_length=255,blank=True,null=True)
    description = RichTextField()
    button_text = models.CharField(max_length=50,null=True,blank=True)
    button_link = models.CharField(max_length=255,null=True,blank=True)
    