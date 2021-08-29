from django.contrib import admin

# Register your models here.

from .models import Language, Translation, Translator

admin.site.register(Language)
admin.site.register(Translation)
admin.site.register(Translator)