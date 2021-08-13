from django.conf import settings
from django.db import models

# Create your models here.

class Registration(models.Model):
    term = models.ForeignKey('terms.Term', on_delete = models.RESTRICT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField('exerciseTypes.ExerciseType')
    signature = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)