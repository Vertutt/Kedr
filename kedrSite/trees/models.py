from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser
import datetime

# Create your models here.
class Trees(models.Model):
    title = models.CharField(max_length=100, default='Дерево')
    content = models.TextField(null=True)
    picture = models.ImageField(upload_to='tree_photos/', null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    plant_date = models.DateField(default=datetime.date(2000,9,9))
    creation_date = models.DateField(auto_now_add=True, null = True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="trees_owned", null=True )
    dedicated_to = models.CharField(max_length=100, default='')

class TreesImages(models.Model):
    tree = models.ForeignKey(Trees, on_delete=models.CASCADE, related_name='images', verbose_name=u'Дерево')
    image = models.ImageField(upload_to='tree_photos/', null=True, blank=True)