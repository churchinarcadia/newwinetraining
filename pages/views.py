from django.shortcuts import render

from iommi import Page

from .models import Page

# Create your views here.

class Index(Page):
    h1 = htmo.h1('NewWineTraining')

    body_text = 'Under construction...'
