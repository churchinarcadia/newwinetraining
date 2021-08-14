from django.conf import settings
from django.db import models

# Create your models here.

class Language(models.Model):
    language = models.CharField(max_length = 100)
    code = models.CharField(max_length = 5)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)

class Translation(models.Model):
    text = models.ForeignKey('trainings.Text', on_delete = models.CASCADE)
    language = models.ForeignKey(Language, on_delete = models.RESTRICT)
    content = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)