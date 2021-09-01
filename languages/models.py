from django.conf import settings
from django.db import models
from newwinetraining.models import BaseModel

from django.utils.translation import gettext

# Create your models here.

class Language(models.Model):
    language = models.CharField(max_length = 100, verbose_name = gettext('Language'))
    code = models.CharField(max_length = 5, verbose_name = gettext('Code'), blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'language_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'language_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.language

class Translation(models.Model):
    text = models.ForeignKey('trainings.Text', related_name = 'translation_texts', verbose_name = gettext('Text'), on_delete = models.CASCADE)
    language = models.ForeignKey(Language, related_name = 'translation_languages', verbose_name = gettext('Language'), on_delete = models.RESTRICT)
    content = models.TextField(blank = True, verbose_name = gettext('Translation Content'))
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Creaed'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translation_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translation_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.text + ', ' + self.language

class Translator(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translator_users', verbose_name = gettext('User'), on_delete = models.RESTRICT)
    language = models.ForeignKey(Language, related_name = 'translator_languages', verbose_name = gettext('Language'), on_delete = models.RESTRICT)
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translator_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translat0r_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.user + ' (' + self.language + ')'