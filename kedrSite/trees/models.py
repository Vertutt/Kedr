from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser


# Create your models here.
class Trees(models.Model):
    title = models.CharField(max_length=100, default='Дерево')
    content = models.TextField(null=True)
    picture = models.ImageField(upload_to='tree_photos/', null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    owner = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="trees_owned", null=True )