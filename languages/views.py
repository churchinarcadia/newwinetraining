from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from newwinetraining.iommi import Table, Form, Page
from iommi import Fragment

from .models import Language, Translation, Translator

# Create your views here.

def language_index(request):
    return Table(auto__model = Language)

def language_view(request):
    return LanguageView()

class LanguageView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def language_add(request):
    return Form.create(auto__model = Language)

def language_edit(request, language_id):
    return Form.create(auto__model = Language)

def language_delete(request, language_id):
    return Form.create(auto__model = Language)

def translation_index(request):
    return Table(auto__model = Translation)

def translation_view(request):
    return TranslationView()

class TranslationView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def translation_add(request):
    return Form.create(auto__model = Translation)

def translation_edit(request, translation_id):
    return Form.create(auto__model = Translation)

def translation_delete(request, translation_id):
    return Form.create(auto__model = Translation)

def translator_index(request):
    return Table(auto__model = Translator)

def translator_view(request):
    return TranslatorView()

class TranslatorView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def translator_add(request):
    return Form.create(auto__model = Translator)

def translator_edit(request, translator_id):
    return Form.create(auto__model = Translator)

def translator_delete(request, translator_id):
    return Form.create(auto__model = Translator)