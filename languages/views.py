from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from iommi.table import RowConfig

#from newwinetraining.iommi import Table, Form, Page, Column
from iommi import ( 
    Fragment,
    html,
    Action,
    Column,
    Field,
    Page,
    Table,
    Form,
)

from .models import Language, Translation, Translator

# Create your views here.

def language_index(request):
    
    context = {
        'html_title': 'Language Index | New Wine Training',
    }
    
    class LanguageIndexPage(Page):
        
        #context__browser_title = 'Language Index | New Wine Training'
        
        page_title = html.h1('Languages')

        instructions = html.p('Click on the language name to view details about that language entry as well as any associated data.')
        
        class LanguageIndexTable(Table):
            
            id = Column.number(
                attr = 'pk',
                render_column = False,
            )

            language = Column(
                attr = 'language',
                #cell__url = lambda row, **_: row.get_absolute_url(),
                cell__url = lambda row, **_: reverse('languages:language_view', args = (row.pk,))
            )

            code = Column(
                attr = 'code',
            )

            created = Column(
                attr = 'created',
            )

            creator = Column(
                attr = 'creator',
            )

            modified = Column(
                attr = 'modified',
            )

            modifier = Column(
                attr = 'modifier',
            )

            edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('languages:translator_edit', args = (row.pk,)),
            )

        table = LanguageIndexTable(rows = Language.objects.all())
        #table = return Table(auto__model = Language)

    return LanguageIndexPage(context = context)

def language_view(request, language_id):
    
    context = {
        'html_title': 'Language View | New Wine Training',
    }
    
    language = get_object_or_404(Language, pk = language_id)
    
    class LanguageView(Page):
        h1 = html.h1(language.language)

        language_h2 = html.h2(language.language + ' Details')
        dl = html.dl()
        language_id_dt = html.dt('ID')
        language_id_dd = html.dd(language.id)
        language_code_dt = html.dt('Code')
        language_code_dd = html.dd(language.code)
        language_language_dt = html.dt('Language')
        language_language_dd = html.dd(language.language)
        language_created_dt = html.dt('Created')
        language_created_dd = html.dd(language.created)
        language_creator_dt = html.dt('Creator')
        language_creator_dd = html.dd(language.creator)
        language_modified_dt = html.dt('Modified')
        language_modified_dd = html.dd(language.modified)
        language_modifier_dt = html.dt('Modifier')
        language_modifier_dd = html.dd(language.modifier)

        hr1 = html.hr()

        translators_h2 = html.h2(language.language + ' Translators')
        translators = language.translator_languages.all()

        if len(translators) > 0:
            
            class LanguageTranslatorTable(Table):

                id = Column.number(
                    attr = 'pk',
                    render_column = False,
                )

                translator = Column(
                    attr = 'user',
                    cell__url = lambda row, **_: reverse('languages:translator_view', args = (row.pk,))
                )

                created = Column(
                    attr = 'created',
                )

                creator = Column(
                    attr = 'creator',
                )

                modified = Column(
                    attr = 'modified',
                )

                modifier = Column(
                    attr = 'modifier',
                )

                edit = Column(
                    attr = '',
                    display_name = '',
                    cell__value = 'Edit',
                    cell__url = lambda row, **_: reverse('languages:translator_edit', args = (row.pk,)),
                )

            translators_table = LanguageTranslatorTable(rows = translators)
        
        else: 
            no_translators = html.p('No translators.')
        
        hr2 = html.hr()

        translations_h2 = html.h2(language.language + ' Translations')
        translations = language.translation_languages.all()

        if len(translations) > 0:

            class LanguageTranslationTable(Table):

                id = Column.number(
                    attr = 'pk',
                    render_column = False,
                )

                original_text = Column(
                    attr = 'text',
                    cell__url = lambda row, **_: reverse('languages:translation_view', args = (row.pk,)),
                    cell__url_title = lambda row, **_: row.text[0 : 50] + '...',
                )

                translation = Column(
                    attr = 'content',
                    cell__value = lambda row, **_: row.content[0 : 50] + '...',
                )

                created = Column(
                    attr = 'created',
                )

                creator = Column(
                    attr = 'creator',
                )

                modified = Column(
                    attr = 'modified',
                )

                modifier = Column(
                    attr = 'modifier',
                )

                edit = Column(
                    attr = '',
                    display_name = '',
                    cell__value = 'Edit',
                    cell__url = lambda row, **_: reverse('languages:translation_edit', args = (row.pk,)),
                )

            translations_table = LanguageTranslationTable()
        
        else:
            no_translations = html.p('No translations.')
        
        hr3 = html.hr()

        terms_h2 = html.h2(language.language + ' Terms')
        terms = language.term_languages.all()

        if len(terms) > 0:

            class LanguageTermTable(Table):

                id = Column.number(
                    attr = 'pk',
                    render_column = False,
                )

                year = Column(
                    attr = 'year',
                    cell__url = lambda row, **_: reverse('trainings:term_view', args = (row.pk,))
                )

                term = Column(
                    attr = 'term',
                    cell__url = lambda row, **_: reverse('trainings:term_view', args = (row.pk,))
                )

                start_date = Column(
                    attr = 'start_date',
                )

                end_date = Column(
                    attr = 'end_date',
                )

                created = Column(
                    attr = 'created',
                )

                creator = Column(
                    attr = 'creator',
                )

                modified = Column(
                    attr = 'modified',
                )

                modifier = Column(
                    attr = 'modifier',
                )

                edit = Column(
                    attr = '',
                    display_name = '',
                    cell__value = 'Edit',
                    cell__url = lambda row, **_: reverse('trainings:term_edit', args = (row.pk,)),
                )
            
            terms_table = LanguageTermTable()
        
        else:
            no_terms = html.p('No terms.')
        
        hr4 = html.hr()

        trainingmeetings_h2 = html.h2(language.language + ' Training Meetings')
        trainingmeetings = language.trainingmeeting_languages.all()

        if len(trainingmeetings) > 0:

            class LanguageTrainingMeetingTable(Table):

                id = Column.number(
                    attr = 'pk',
                    render_column = False,
                )

                date = Column(
                    attr = 'date',
                    cell__url = lambda row, **_: reverse('trainings:trainingmeeting_view', args = (row.pk,))
                )

                start_time = Column(
                    attr = 'start_time',
                )

                end_time = Column(
                    attr = 'end_time',
                )

                location = Column(
                    attr = 'location',
                )

                recording_url = Column(
                    attr = 'recording_url',
                )

                recording_released_datetime = Column(
                    attr = 'recording_released_datetime',
                    display_name = 'Recording Released',
                )

                recording_released_by = Column(
                    attr = 'recording_released_by',
                    display_name = 'Released By',
                )

                notes = Column(
                    attr = 'notes',
                )

                created = Column(
                    attr = 'created',
                )

                creator = Column(
                    attr = 'creator',
                )

                modified = Column(
                    attr = 'modified',
                )

                modifier = Column(
                    attr = 'modifier',
                )

                edit = Column(
                    attr = '',
                    display_name = '',
                    cell__value = 'Edit',
                    cell__url = lambda row, **_: reverse('trainings:trainingmeeting_edit', args = (row.pk,)),
                )
            
            trainingmeetings_table = LanguageTrainingMeetingTable()
        
        else:
            no_trainingmeetings = html.p('No training meetings.')

    return LanguageView(context = context)

def language_add(request):
    
    class LanguageAddForm(Form):
        
        
    
    
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