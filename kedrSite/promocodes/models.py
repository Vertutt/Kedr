from django.db import models

# Create your models here.
class Promocode(models.Model):
    code = models.CharField(max_length=16, unique=True)
    is_activated = models.BooleanField(default=False)