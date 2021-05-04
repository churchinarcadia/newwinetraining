from django.db import models

# Create your models here.

class Registration(models.Model):
    term = models.ForeignKey('Term', on_delete = models.RESTRICT)
    user = models.ForeignKey('User', on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField('ExerciseType')
    signature = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey('User', on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey('User', on_delete = models.RESTRICT)