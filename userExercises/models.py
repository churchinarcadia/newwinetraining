from django.db import models

# Create your models here.

class UserExercise(models.Model):
    date = models.DateField(default = date.today)
    user = models.ForeignKey(User, on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField(ExerciseType)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(User, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(User, on_delete = models.RESTRICT)