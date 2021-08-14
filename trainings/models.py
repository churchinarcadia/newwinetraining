from django.conf import settings
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.

class Term(models.Model):
    term = models.CharField(max_length = 10, choices = [('Fall'),('Spring')])
    year = models.IntegerField(
        validators = [
            MinValueValidator(2000, message='Please enter an appropriate year.'),
            MaxValueValidator(2040, message='Please enter an appropriate year.'),
        ],
    )
    language = models.ForeignKey('languages.Language', on_delete = models.RESTRICT)
    start_date = models.DateField(auto_now = False, auto_now_add = False)
    end_date = models.DateField(auto_now = False, auto_now_add = False, )
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)

class ExerciseType(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)

class RecordingLocation(models.Model):
    location = models.CharField(max_length = 30)
    code_before_url = models.CharField(max_length = 255)
    code_after_url = models.CharField(max_length = 255)
    url_identifier = models.CharField(max_length = 100)
    notes = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)

class Registration(models.Model):
    term = models.ForeignKey(Term, on_delete = models.RESTRICT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField(ExerciseType)
    signature = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)

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

class UserExercise(models.Model):
    date = models.DateField(default = timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField(ExerciseType)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)

class Text(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)