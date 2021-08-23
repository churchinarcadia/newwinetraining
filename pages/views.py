#from django.shortcuts import render

from django.urls import reverse

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
        h1 = html.h1('NewWineTraining')
        
        construction_text = html.p('Under construction...')
        
        menu_h2 = html.h2('Temporary Menu')
        
        menu = [
            {
                'app': 'languages',
                'model': 'language',
                'display': 'Languages'
            },
            {
                'app': 'languages',
                'model': 'translator',
                'display': 'Translators'
            },
            {
                'app': 'languages',
                'model': 'translation',
                'display': 'Translations'
            },
            {
                'app': 'trainings',
                'model': 'term',
                'display': 'Terms'
            },
            {
                'app': 'trainings',
                'model': 'exercisetype',
                'display': 'Exercise Types'
            },
            {
                'app': 'trainings',
                'model': 'recordinglocation',
                'display': 'Recording Locations'
            },
            {
                'app': 'trainings',
                'model': 'registration',
                'display': 'Registrations'
            },
            {
                'app': 'trainings',
                'model': 'trainingmeeting',
                'display': 'Training Meetings'
            },
            {
                'app': 'trainings',
                'model': 'userexercise',
                'display': 'User Exercises'
            },
            {
                'app': 'trainings',
                'model': 'text',
                'display': 'Texts'
            },
            {
                'app': 'users',
                'model': 'usertype',
                'display': 'User Types'
            },
            {
                'app': 'users',
                'model': 'locality',
                'display': 'Localities'
            },
            {
                'app': 'users',
                'model': 'user',
                'display': 'Users'
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
                cell__value = 'Add',
                cell__url = lambda row, **_: reverse(row['app'] + ':' + row['model'] + '_add'),
            ),
        )

        class Meta:
            context = dict(
                html_title = 'Home | New Wine Training',
            )
    
    return PageIndexPage()