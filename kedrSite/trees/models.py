from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser


# Create your models here.
class Trees(models.Model):
    title = models.CharField(max_length=100, default='Дерево')
    content = models.TextField(blank=True)
    picture = models.ImageField(null='true')
    latitude = models.FloatField()
    longitude = models.FloatField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="trees_owned", null=True )