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

from trainings.models import Term, TrainingMeeting, Text

# Create your views here.

def language_index(request):
    
    class LanguageIndexPage(Page):
        
        page_title = html.h1('Languages')

        instructions = html.p('Click on the language name to view details about that language, as well as any associated data.')
        
        table = Table(
            auto__model = Language,
            title = None,
            columns__language = Column(
                #cell__url = lambda row, **_: row.get_absolute_url(),
                cell__url = lambda row, **_: reverse('languages:language_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('languages:language_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'Language Index | New Wine Training',
            )
            
    return LanguageIndexPage()

def language_view(request, language_id):
    
    language = get_object_or_404(Language, pk = language_id)
    
    class LanguageViewPage(Page):
        
        h1 = html.h1('Language View: ' + language.language)

        language_h2 = html.h2('Details')
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
        language_modifier_dd = html.dd(language.modifier)\

        hr1 = html.hr()

        if language.language != 'English':
        
            translators_h2 = html.h2('Translators')
            translators = language.translator_languages.all()
        
            translators_table = Table(
                auto__model = Translator,
                rows = translators,
                title = None,
                empty_message = 'No translators',
                auto__exclude = ['language'],
                columns__user = Column(
                    display_name = 'Translator',
                    cell__url = lambda row, **_: reverse('languages:translator_view', args = (row.pk,)),
                ),
                columns__edit = Column(
                    attr = '',
                    display_name = '',
                    cell__value = 'Edit',
                    cell__url = lambda row, **_: reverse('languages:translator_edit', args = (row.pk,)),
                ),
            )
        
            hr2 = html.hr()

        translations_h2 = html.h2('Translations')
        translations = language.translation_languages.all()

        translations_table = Table(
            auto__model = Translation,
            rows = translations,
            title = None,
            empty_message = 'No translations',
            auto__exclude = ['language'],
            columns__text = Column(
                display_name = 'Original Text',
                cell__url = lambda row, **_: reverse('languages:translation_view', args = (row.pk,)),
                cell__url_title = lambda row, **_: row.text[0 : 50] + '...' if len(row.text) > 50 else row.text
            ),
            columns__content = Column(
                display_name = 'Translation',
                cell__value = lambda row, **_: row.content[0 : 50] + '...' if len(row.content) > 50 else row.content
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('languages:translation_edit', args = (row.pk,)),
            ),
        )
        
        hr3 = html.hr()

        terms_h2 = html.h2('Terms')
        terms = language.term_languages.all()

        terms_table = Table(
            auto__model = Term,
            rows = terms,
            title = None,
            empty_message = 'No terms',
            auto__exclude = ['language'],
            columns__term = Column(
                after = 'year',
                cell__url = lambda row, **_: reverse('trainings:term_view', args = (row.pk,)),
            ),
            columns__year = Column(
                cell__url = lambda row, **_: reverse('trainings:term_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:term_edit', args = (row.pk,)),
            ),
        )
        
        hr4 = html.hr()

        trainingmeetings_h2 = html.h2('Training Meetings')
        trainingmeetings = language.trainingmeeting_languages.all()

        trainingmeetings_table = Table(
            auto__model = TrainingMeeting,
            rows = trainingmeetings,
            title = None,
            empty_message = 'No training meetings',
            auto__exclude = ['language'],
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_view', args = (row.pk,)),
            ),
            columns__recording_released_datetime = Column(
                display_name = 'Recording Released',
            ),
            columns__recording_released_by = Column(
                display_name = 'Released By',
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_edit', args = (row.pk,)),
            ),
        )

        class Meta:
            context = dict(
                html_title = 'Language View | New Wine Training',
            )

    return LanguageViewPage()

def language_add(request):
    
    return Form.create(
        auto__model = Language,
        auto__include = ['language', 'code'],
        context__html_title = 'Language Create | New Wine Training',
    )

def language_edit(request, language_id):
    
    return Form.edit(
        auto__model = Language,
        auto__instance = Language.objects.get(id = language_id),
        auto__include = ['language', 'code'],
        context__html_title = 'Language Edit | New Wine Training',
    )

def language_delete(request, language_id):
    
    class LangaugeDeleteTemp(Page):
        page_title = html.h1('Delete Language')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'Language Delete | New Wine Training',
            )
    
    return LangaugeDeleteTemp()

def translation_index(request):
    
    class TranslationIndexPage(Page):
        
        page_title = html.h1('Translations')
        
        instructions = html.p('Click on the original text or the translation text to view details about that translation, as well as any associated data.')
    
        table = Table(
            auto__model = Translation,
            title = None,
            columns__text = Column(
                display_name = 'Original Text',
                cell__url = lambda row, **_: reverse('languages:translation_view', args = (row.pk,)),
                cell__url_title = lambda row, **_: row.text[0 : 50] + '...',
            ),
            columns__content = Column(
                display_name = 'Translation',
                cell__value = lambda row, **_: row.content[0 : 50] + '...',
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('languages:translation_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'Translation Index | New Wine Training',
            )
        
    return TranslationIndexPage()

def translation_view(request, translation_id):
    
    translation = get_object_or_404(Translation, pk = translation_id)

    class TranslationViewPage(Page):
        #h1 = html.h1('NewWineTraining')
        h1 = html.h1('View Translation')

        translation_h2 = html.h2('Details')
        dl = html.dl()
        translation_id_dt = html.dt('ID')
        translation_id_dd = html.dd(translation.id)
        translation_langauge_dt = html.dt('Language')
        translation_language_dd = html.dd(translation.language)
        translation_text_dt = html.dt('Text Description')
        translation_text_dd = html.dd(translation.text)
        translation_content_dt = html.dt('Translation')
        translation_content_dd = html.dd(translation.content)
        translation_created_dt = html.dt('Created')
        translation_created_dd = html.dd(translation.created)
        translation_creator_dt = html.dt('Creator')
        translation_creator_dd = html.dd(translation.creator)
        translation_modified_dt = html.dt('Modified')
        translation_modified_dd = html.dd(translation.modified)
        translation_modifier_dt = html.dt('Modifier')
        translation_modifier_dd = html.dd(translation.modifier)
        
        hr1 = html.hr()
        
        text_h2 = html.h2('Text')
        texts = translation.text.all()
        
        text_table = Table(
            auto__model = Text,
            rows = texts,
            title = None,
            empty_message = 'No texts',
            columns__name = Column(
                cell__url = lambda row, **_: reverse('trainings:text_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:text_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        language_h2 = html.h2('Language')
        languages = translation.language.all()
        
        language_table = Table(
            auto__model = Language,
            rows = languages,
            title = None,
            empty_message = 'No languages',
            columns__language = Column(
                cell__url = lambda row, **_: reverse('languages:language_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('languages:language_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'Translation View | New Wine Training',
            )
    
    return TranslationViewPage()

def translation_add(request):
    
    return Form.create(
        auto__model = Translation,
        auto__include = ['language', 'text', 'content'],
        context__html_title = 'Translation Create | New Wine Training',
    )

def translation_edit(request, translation_id):
    
    return Form.edit(
        auto__model = Translation,
        auto__instance = Translation.objects.get(id = translation_id),
        auto__include = ['language', 'text', 'content'],
        context__html_title = 'Translation Edit | New Wine Training',
    )

def translation_delete(request, translation_id):
    
    class TranslationDeleteTemp(Page):
        page_title = html.h1('Delete Translation')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'Translation Delete | New Wine Training',
            )
    
    return TranslationDeleteTemp()

def translator_index(request):
    
    class TranslatorIndexPage(Page):
        
        page_title = html.h1('Translators')
        
        instructions = html.p('Click on the translator\'s name to view details about that translator, as well as any associated data.')
        
        table = Table(
            auto__model = Translator,
            title = None,
            columns__user = Column(
                display_name = 'Translator',
                 cell__url = lambda row, **_: reverse('languages:translator_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('languages:translator_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'Translator Index | New Wine Training',
            )
            
    return TranslatorIndexPage()

def translator_view(request, translator_id):
    
    translator = get_object_or_404(Translator, pk = translator_id)

    class TranslatorViewPage(Page):
        
        h1 = html.h1('Translator View: ' + translator.user)
        
        translator_h2 = html.h2('Details')
        dl = html.dl()
        translator_id_dt = html.dt('ID')
        translator_id_dd = html.dd(translator.id)
        translator_user_dt = html.dt('Translator')
        translator_user_dd = html.dd(translator.user)
        translator_language_dt = html.dt('Language')
        translator_language_dd = html.dd(translator.language)
        translator_created_dt = html.dt('Created')
        translator_created_dd = html.dd(translator.created)
        translator_creator_dt = html.dt('Creator')
        translator_creator_dd = html.dd(translator.creator)
        translator_modified_dt = html.dt('Modified')
        translator_modified_dd = html.dd(translator.modified)
        translator_modifier_dt = html.dt('Modifier')
        translator_modifier_dd = html.dd(translator.modifier)
        
        hr1 = html.hr()
        
        language_h2 = html.h2('Language')
        languages = translator.language.all()
        
        languages_table = Table(
            auto_model = Language,
            rows = languages,
            title = None,
            empty_message = 'No languages',
            columns__language = Column(
                cell__url = lambda row, **_: reverse('languages:language_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('languages:language_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        translation_h2 = html.h2('Translations')
        translations = translator.user.translation_creators.all()
        
        table = Table(
            auto__model = Translation,
            rows = translations,
            title = None,
            empty_message = 'No translations',
            columns__text = Column(
                display_name = 'Original Text',
                cell__url = lambda row, **_: reverse('languages:translation_view', args = (row.pk,)),
                cell__url_title = lambda row, **_: row.text[0 : 50] + '...' if len(row.text) > 50 else row.text
            ),
            columns__content = Column(
                display_name = 'Translation',
                cell__value = lambda row, **_: row.content[0 : 50] + '...' if len(row.content) > 50 else row.content
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('languages:translation_edit', args = (row.pk,)),
            ),
        )

        class Meta:
            context = dict(
                html_title = 'Translator View | New Wine Training',
            )
    
    return TranslatorViewPage()

def translator_add(request):
    
    return Form.create(
        auto__model = Translator,
        auto__include = ['user', 'language'],
        context__html_title = 'Translator Create | New Wine Training',
    )

def translator_edit(request, translator_id):
    
    return Form.edit(
        auto__model = Translator,
        auto__instance = Translator.objects.get(id = translator_id),
        auto__include = ['user', 'language'],
        context__html_title = 'Translator Edit | New Wine Training',
    )

def translator_delete(request, translator_id):
    
    class TranslatorDeleteTemp(Page):
        page_title = html.h1('Delete Translator')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'Translator Delete | New Wine Training',
            )
    
    return TranslatorDeleteTemp()