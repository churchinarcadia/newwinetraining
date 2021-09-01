from django.conf import settings
from django.db import models
from newwinetraining.models import BaseModel

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

from django.utils.translation import gettext

# Create your models here.

class Term(models.Model):
    term = models.CharField(max_length = 10, choices = [('Fall',gettext('Fall')),('Spring',gettext('Spring'))], verbose_name = gettext('Term'))
    year = models.IntegerField(
        validators = [
            MinValueValidator(2000, message = gettext('Please enter an appropriate year.')),
            MaxValueValidator(2040, message = gettext('Please enter an appropriate year.')),
        ],
        verbose_name = gettext('Year')
    )
    language = models.ForeignKey('languages.Language', related_name = 'term_languages', verbose_name = gettext('Language'), on_delete = models.RESTRICT)
    start_date = models.DateField(auto_now = False, auto_now_add = False, verbose_name = gettext('Start Date'), blank = True, null = True)
    end_date = models.DateField(auto_now = False, auto_now_add = False, verbose_name = gettext('End Date'), blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'term_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'term_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return str(self.year) + ' ' + self.term + ' (' + str(self.language) + ')'

class ExerciseType(models.Model):
    name = models.CharField(max_length=100, verbose_name = gettext('Name'))
    description = models.TextField(blank = True, verbose_name = gettext('Description'))
    active = models.BooleanField(default = True, verbose_name = gettext('Active'))
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'exercisetype_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'exercisetype_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.name

class RecordingLocation(models.Model):
    location = models.CharField(max_length = 30, verbose_name = gettext('Location'))
    code_before_url = models.CharField(max_length = 255, verbose_name = gettext('Embed Code Before URL'), blank = True, null = True)
    code_after_url = models.CharField(max_length = 255, verbose_name = gettext('Embed Code After URL'), blank = True, null = True)
    url_identifier = models.CharField(max_length = 100, verbose_name = gettext('URL Identifier'))
    notes = models.TextField(blank = True, verbose_name = gettext('Notes'))
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'recordinglocation_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'recordinglocation_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.location

class Registration(models.Model):
    term = models.ForeignKey(Term, related_name = 'registration_terms', verbose_name = gettext('Term'), on_delete = models.RESTRICT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'registration_users', verbose_name = gettext('User'), on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField(ExerciseType, related_name = 'registration_exercisetypes', verbose_name = gettext('Exercise Types'), blank = True)
    signature = models.CharField(max_length = 100, verbose_name = gettext('Signature'), blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'registration_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'registration_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.user.get_full_name() + ' (' + str(self.term) + ')'

class TrainingMeeting(models.Model):
    date = models.DateField(verbose_name = gettext('Date'))
    start_time = models.TimeField(verbose_name = gettext('Start Time'), blank = True, null = True)
    end_time = models.TimeField(verbose_name = gettext('End Time'), blank = True, null = True)
    language = models.ForeignKey('languages.Language', related_name = 'trainingmeeting_languages', verbose_name = gettext('Language'), on_delete = models.RESTRICT)
    location = models.CharField(max_length = 255, verbose_name = gettext('Location'), blank = True)
    recording_url = models.URLField(max_length = 255, verbose_name = gettext('Recording URL'), blank = True, null = True)
    recording_released_datetime = models.DateTimeField(verbose_name = gettext('Recording Released'), blank = True, null = True)
    recording_released_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'recordingreleased_user', verbose_name = gettext('Recording Released By'), blank = True, null = True, on_delete = models.RESTRICT)
    notes = models.TextField(verbose_name = gettext('Notes'), blank = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'trainingmeeting_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'trainingmeeting_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return str(self.date) + ' (' + str(self.language) + ')'

class UserExercise(models.Model):
    date = models.DateField(default = timezone.now, verbose_name = gettext('Date'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'userexercise_users', verbose_name = gettext('User'), on_delete = models.RESTRICT)
    exercisetypes = models.ManyToManyField(ExerciseType, related_name = 'userexercise_exercisetypes', verbose_name = gettext('Exercise Types'))
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'userexercise_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'userexercise_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return str(self.date) + ' | ' + self.user.get_full_name()

class Text(models.Model):
    name = models.CharField(max_length = 255, verbose_name = gettext('Name'))
    description = models.TextField(blank = True, verbose_name = gettext('Description'))
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'text_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'text_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.description