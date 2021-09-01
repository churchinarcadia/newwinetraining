#from django.shortcuts import render

from django.urls import reverse

from django.utils.translation import gettext

from newwinetraining.iommi import Page, Form, Table, Column

from iommi import ( 
    Fragment,
    html,
    Action,
    Field,
)

# Create your views here.

def page_index(request):

    class PageIndexPage(Page):
        h1 = html.h1(gettext('NewWineTraining'))
        
        construction_text = html.p(gettext('Under construction...'))
        
        menu_h2 = html.h2(gettext('Temporary Menu'))
        
        menu = [
            {
                'app': 'languages',
                'model': 'language',
                'display': gettext('Languages')
            },
            {
                'app': 'languages',
                'model': 'translator',
                'display': gettext('Translators')
            },
            {
                'app': 'languages',
                'model': 'translation',
                'display': gettext('Translations')
            },
            {
                'app': 'trainings',
                'model': 'term',
                'display': gettext('Terms')
            },
            {
                'app': 'trainings',
                'model': 'exercisetype',
                'display': gettext('Exercise Types')
            },
            {
                'app': 'trainings',
                'model': 'recordinglocation',
                'display': gettext('Recording Locations')
            },
            {
                'app': 'trainings',
                'model': 'registration',
                'display': gettext('Registrations')
            },
            {
                'app': 'trainings',
                'model': 'trainingmeeting',
                'display': gettext('Training Meetings')
            },
            {
                'app': 'trainings',
                'model': 'userexercise',
                'display': gettext('User Exercises')
            },
            {
                'app': 'trainings',
                'model': 'text',
                'display': gettext('Texts')
            },
            {
                'app': 'users',
                'model': 'usertype',
                'display': gettext('User Types')
            },
            {
                'app': 'users',
                'model': 'locality',
                'display': gettext('Localities')
            },
            {
                'app': 'users',
                'model': 'user',
                'display': gettext('Users')
            },
        ]
        
        menu_table = Table(
            rows = menu,
            title = None,
            header__template = None,
            columns__model = Column(
                cell__value = lambda row, **_:  row['display'],
                cell__url = lambda row, **_: reverse(row['app'] + ':' + row['model'] + '_index'),
            ),
            columns__add = Column(
                cell__value = gettext('Add'),
                cell__url = lambda row, **_: reverse(row['app'] + ':' + row['model'] + '_add'),
            ),
        )

        class Meta:
            context = dict(
                html_title = gettext('Home | New Wine Training'),
            )
    
    return PageIndexPage()