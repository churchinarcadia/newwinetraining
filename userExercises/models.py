from django.conf import settings
from django.db import models

from django.utils import timezone
#import datetime

# Create your models here.

class UserExercise(models.Model):
    date = models.DateField(default = timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField('exerciseTypes.ExerciseType')
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)