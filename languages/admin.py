from django.contrib import admin

# Register your models here.

from .models import Language, Translation

admin.site.register(Language)
admin.site.register(Translation)