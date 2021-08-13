from django.conf import settings
from django.db import models

# Create your models here.

class Translation(models.Model):
    text = models.ForeignKey('texts.Text', on_delete = models.CASCADE)
    language = models.ForeignKey('languages.Language', on_delete = models.RESTRICT)
    content = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)