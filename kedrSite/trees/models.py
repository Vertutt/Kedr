from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from users.models import CustomUser
import datetime

class Trees(models.Model):
    title = models.CharField(max_length=100, default='Дерево')
    content = models.TextField(null=True)
    picture = ProcessedImageField(upload_to='tree_photos/', null=True, blank=True,
                                processors=[ResizeToFit(800,600)],
                                format='JPEG',
                                options={'quality':60})
    latitude = models.FloatField()
    longitude = models.FloatField()
    plant_date = models.DateField(default=datetime.date(2000,9,9))
    creation_date = models.DateField(auto_now_add=True, null = True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="trees_owned", null=True )
    owner_name = models.CharField(max_length=256, default='')
    dedicated_to = models.CharField(max_length=100, default='')

class TreesImages(models.Model):
    tree = models.ForeignKey(Trees, on_delete=models.CASCADE, related_name='images', verbose_name=u'Дерево')
    image = ProcessedImageField(upload_to='tree_photos/', null=True, blank=True,
                                processors=[ResizeToFill(800,600)],
                                format='JPEG',
                                options={'quality':60})
