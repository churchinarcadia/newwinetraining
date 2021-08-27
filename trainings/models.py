from django.conf import settings
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.

class Term(models.Model):
    term = models.CharField(max_length = 10, choices = [('Fall','Fall'),('Spring','Spring')])
    year = models.IntegerField(
        validators = [
            MinValueValidator(2000, message='Please enter an appropriate year.'),
            MaxValueValidator(2040, message='Please enter an appropriate year.'),
        ],
    )
    language = models.ForeignKey('languages.Language', related_name = 'term_languages', on_delete = models.RESTRICT)
    start_date = models.DateField(auto_now = False, auto_now_add = False, blank = True, null = True)
    end_date = models.DateField(auto_now = False, auto_now_add = False, blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'term_creators', on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'term_modifiers', on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.year + ' ' + self.term + ' (' + self.language + ')'

class ExerciseType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'exercisetype_creators', on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'exercisetype_modifiers', on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.name

class RecordingLocation(models.Model):
    location = models.CharField(max_length = 30)
    code_before_url = models.CharField(max_length = 255, blank = True, null = True)
    code_after_url = models.CharField(max_length = 255, blank = True, null = True)
    url_identifier = models.CharField(max_length = 100)
    notes = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'recordinglocation_creators', on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'recordinglocation_modifiers', on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.location

class Registration(models.Model):
    term = models.ForeignKey(Term, related_name = 'registration_terms', on_delete = models.RESTRICT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'registration_users', on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField(ExerciseType, related_name = 'registration_exercisetypes', blank = True)
    signature = models.CharField(max_length = 100, blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'registration_creators', on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'registration_modifiers', on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.user + ' (' + self.term + ')'

class TrainingMeeting(models.Model):
    date = models.DateField()
    start_time = models.TimeField(blank = True, null = True)
    end_time = models.TimeField(blank = True, null = True)
    language = models.ForeignKey('languages.Language', related_name = 'trainingmeeting_languages', on_delete = models.RESTRICT)
    location = models.CharField(max_length = 255, blank = True)
    recording_url = models.URLField(max_length = 255, blank = True, null = True)
    recording_released_datetime = models.DateTimeField(blank = True, null = True)
    recording_released_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'recordingreleased_user', blank = True, null = True, on_delete = models.RESTRICT)
    notes = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'trainingmeeting_creators', on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'trainingmeeting_modifiers', on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.date + ' (' + self.language + ')'

class UserExercise(models.Model):
    date = models.DateField(default = timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'userexercise_users', on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField(ExerciseType, related_name = 'userexercise_exercisetypes')
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'userexercise_creators', on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'userexercise_modifiers', on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.date + ' | ' + self.user

class Text(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'text_creators', on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'text_modifiers', on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.description