from django.conf import settings
from django.db import models

# Create your models here.

class Language(models.Model):
    language = models.CharField(max_length = 100)
    code = models.CharField(max_length = 5)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'language_creators', on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'language_modifiers', on_delete = models.RESTRICT)

    def __str__(self):
        return self.language

class Translation(models.Model):
    text = models.ForeignKey('trainings.Text', related_name = 'translation_texts', on_delete = models.CASCADE)
    language = models.ForeignKey(Language, related_name = 'translation_languages', on_delete = models.RESTRICT)
    content = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translation_creators', on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translation_modifiers', on_delete = models.RESTRICT)

    def __str__(self):
        return self.text + ', ' + self.language

class Translator(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translator_users', on_delete = models.RESTRICT)
    language = models.ForeignKey(Language, related_name = 'translator_languages', on_delete = models.RESTRICT)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translator_creators', on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'translat0r_modifiers', on_delete = models.RESTRICT)

    def __str__(self):
        return self.user + ' (' + self.language + ')'