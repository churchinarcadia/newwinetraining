from django.db import models

# Create your models here.

class Translation(models.Model):
    text = models.ForeignKey('Text', on_delete = models.CASCADE)
    language = models.ForeignKey('Language', on_delete = models.RESTRICT)
    content = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey('User', on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey('User', on_delete = models.RESTRICT)