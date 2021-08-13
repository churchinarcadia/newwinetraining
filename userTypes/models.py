from django.conf import settings
from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)