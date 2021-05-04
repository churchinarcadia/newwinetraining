from django.db import models

from django.utils import timezone
#import datetime

# Create your models here.

class UserExercise(models.Model):
    date = models.DateField(default = timezone.now)
    user = models.ForeignKey('User', on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField('ExerciseType')
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey('User', on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey('User', on_delete = models.RESTRICT)