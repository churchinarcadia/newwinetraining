from django.conf import settings
from django.db import models

# Create your models here.

class TrainingMeeting(models.Model):
    date = models.DateField()
    start_time = models.TimeField(blank = True)
    end_time = models.TimeField(blank = True)
    language = models.ForeignKey('languages.Language', on_delete = models.RESTRICT)
    location = models.CharField(max_length = 255, blank = True)
    recording_url = models.URLField(max_length = 255, blank = True)
    notes = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)