from django.db import models

# Create your models here.

class RecordingLocation(models.Model):
    location = models.CharField(max_length = 30)
    code_before_url = models.CharField(max_length = 255)
    code_after_url = models.CharField(max_length = 255)
    url_identifier = models.CharField(max_length = 100)
    notes = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey('User', on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey('User', on_delete = models.RESTRICT)