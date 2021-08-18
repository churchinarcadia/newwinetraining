#from django.shortcuts import render

from newwinetraining.iommi import Page

from iommi import Fragment, html

# Create your views here.

def page_index(request):
    return PageIndex()

class PageIndex(Page):
    h1 = html.h1('NewWineTraining')
    #h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'
