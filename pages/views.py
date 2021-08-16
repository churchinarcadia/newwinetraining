from django.shortcuts import render

from newwinetraining.iommi import Page

# Create your views here.

class Index(Page):
    h1 = html.h1('NewWineTraining')

    body_text = 'Under construction...'
