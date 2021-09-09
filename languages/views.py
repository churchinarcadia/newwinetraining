from django.http.response import Http404
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from django.contrib import messages
from django.utils.translation import gettext

from django.db.models import Q

from newwinetraining.iommi import Page, Form, Table, Column

from iommi import ( 
    Fragment,
    html,
    Action,
    Field,
)

#from newwinetraining.views import save_post_handler

from .models import Language, Translation, Translator

from trainings.models import Term, TrainingMeeting, Text

# Create your views here.

def language_index(request):
    
    if request.user.has_staff_perms == False:
        raise Http404
    
    class LanguageIndexPage(Page):
        
        page_title = html.h1(gettext('Languages'))

        instructions = html.p(gettext('Click on the language name to view details about that language, as well as any associated data.'))
        
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
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('languages:language_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Language Index | New Wine Training'),
            )
            
    return LanguageIndexPage()

def language_view(request, language_id):
    
    language = get_object_or_404(Language, pk = language_id)
    
    class LanguageViewPage(Page):
        
        h1 = html.h1(gettext('Language View: ' + language.language))

        language_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__language_id_dt = html.dt('ID'),
            children__language_id_dd = html.dd(language.id),
            children__language_code_dt = html.dt(gettext('Code')),
            children__language_code_dd = html.dd(language.code),
            children__language_language_dt = html.dt(gettext('Language')),
            children__language_language_dd = html.dd(gettext(language.language)),
            children__language_created_dt = html.dt(gettext('Created')),
            children__language_created_dd = html.dd(gettext(language.created)),
            children__language_creator_dt = html.dt(gettext('Creator')),
            children__language_creator_dd = html.dd(language.creator),
            children__language_modified_dt = html.dt(gettext('Modified')),
            children__language_modified_dd = html.dd(language.modified),
            children__language_modifier_dt = html.dt(gettext('Modifier')),
            children__language_modifier_dd = html.dd(language.modifier),
        )

        hr1 = html.hr()

        if language.language != 'English':
        
            translators_h2 = html.h2(gettext('Translators'))
            translators = language.translator_languages.all()
        
            translators_table = Table(
                auto__model = Translator,
                rows = translators,
                title = None,
                empty_message = gettext('No translators'),
                auto__exclude = ['language'],
                columns__user = Column(
                    display_name = gettext('Translator'),
                    cell__url = lambda row, **_: reverse('languages:translator_view', args = (row.pk,)),
                ),
                columns__edit = Column(
                    attr = '',
                    display_name = '',
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('languages:translator_edit', args = (row.pk,)),
                ),
            )
        
            hr2 = html.hr()

        translations_h2 = html.h2(gettext('Translations'))
        translations = language.translation_languages.all()

        translations_table = Table(
            auto__model = Translation,
            rows = translations,
            title = None,
            empty_message = gettext('No translations'),
            auto__exclude = ['language'],
            columns__text = Column(
                display_name = gettext('Text'),
                cell__url = lambda row, **_: reverse('languages:translation_view', args = (row.pk,)),
            ),
            columns__content = Column(
                display_name = gettext('Translation'),
                cell__value = lambda row, **_: row.content[0 : 50] + '...' if len(row.content) > 50 else row.content
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('languages:translation_edit', args = (row.pk,)),
            ),
        )
        
        hr3 = html.hr()

        terms_h2 = html.h2(gettext('Terms'))
        terms = language.term_languages.all()

        terms_table = Table(
            auto__model = Term,
            rows = terms,
            title = None,
            empty_message = gettext('No terms'),
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
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:term_edit', args = (row.pk,)),
            ),
        )
        
        hr4 = html.hr()

        trainingmeetings_h2 = html.h2(gettext('Training Meetings'))
        trainingmeetings = language.trainingmeeting_languages.all()

        trainingmeetings_table = Table(
            auto__model = TrainingMeeting,
            rows = trainingmeetings,
            title = None,
            empty_message = gettext('No training meetings'),
            auto__exclude = ['language'],
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_view', args = (row.pk,)),
            ),
            columns__recording_released_datetime = Column(
                display_name = gettext('Recording Released'),
            ),
            columns__recording_released_by = Column(
                display_name = gettext('Released By'),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_edit', args = (row.pk,)),
            ),
        )

        class Meta:
            context = dict(
                html_title = gettext('Language View | New Wine Training'),
            )

    return LanguageViewPage()

def language_add(request):
    
    return Form.create(
        auto__model = Language,
        auto__include = ['language', 'code'],
        extra__redirect_to = reverse('languages:language_index'),
#        context__html_title = 'Language Create | New Wine Training',
    )

def language_edit(request, language_id):
    
    return Form.edit(
        auto__model = Language,
        auto__instance = Language.objects.get(id = language_id),
        auto__include = ['language', 'code'],
        extra__redirect_to = reverse('languages:language_index'),
#        context__html_title = 'Language Edit | New Wine Training',
    )

def language_delete(request, language_id):
    
    class LangaugeDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Language'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Language Delete | New Wine Training'),
            )
    
    return LangaugeDeleteTemp()

def translation_index(request):
    
    class TranslationIndexPage(Page):
        
        page_title = html.h1(gettext('Translations'))
        
        instructions = html.p(gettext('Click on the text or the translation text to view details about that translation, as well as any associated data.'))
    
        table = Table(
            auto__model = Translation,
            title = None,
            columns__text = Column(
                display_name = gettext('Text'),
                cell__url = lambda row, **_: reverse('languages:translation_view', args = (row.pk,)),
            ),
            columns__content = Column(
                display_name = gettext('Translation'),
                cell__value = lambda row, **_: row.content[0 : 50] + '...' if len(row.content) > 50 else row.content
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('languages:translation_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Translation Index | New Wine Training'),
            )
        
    return TranslationIndexPage()

def translation_view(request, translation_id):
    
    translation = get_object_or_404(Translation, pk = translation_id)

    class TranslationViewPage(Page):
        #h1 = html.h1('NewWineTraining')
        h1 = html.h1(gettext('Translation View'))

        translation_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__translation_id_dt = html.dt('ID'),
            children__translation_id_dd = html.dd(translation.id),
            children__translation_langauge_dt = html.dt(gettext('Language')),
            children__translation_language_dd = html.dd(gettext(str(translation.language))),
            children__translation_text_dt = html.dt(gettext('Text Description')),
            children__translation_text_dd = html.dd(translation.text),
            children__translation_content_dt = html.dt(gettext('Translation')),
            children__translation_content_dd = html.dd(translation.content),
            children__translation_created_dt = html.dt(gettext('Created')),
            children__translation_created_dd = html.dd(translation.created),
            children__translation_creator_dt = html.dt(gettext('Creator')),
            children__translation_creator_dd = html.dd(translation.creator),
            children__translation_modified_dt = html.dt(gettext('Modified')),
            children__translation_modified_dd = html.dd(translation.modified),
            children__translation_modifier_dt = html.dt(gettext('Modifier')),
            children__translation_modifier_dd = html.dd(translation.modifier),
        )
        
        hr1 = html.hr()
        
        text_h2 = html.h2(gettext('Text'))
        texts = Text.objects.filter(pk = translation.text.id)
        
        text_table = Table(
            auto__model = Text,
            rows = texts,
            title = None,
            empty_message = gettext('No texts'),
            columns__name = Column(
                cell__url = lambda row, **_: reverse('trainings:text_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:text_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        language_h2 = html.h2(gettext('Language'))
        languages = Language.objects.filter(pk = translation.language.id)
        
        language_table = Table(
            auto__model = Language,
            rows = languages,
            title = None,
            empty_message = gettext('No languages'),
            columns__language = Column(
                cell__url = lambda row, **_: reverse('languages:language_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('languages:language_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Translation View | New Wine Training'),
            )
    
    return TranslationViewPage()

def translation_add(request):
    
    return Form.create(
        auto__model = Translation,
        auto__include = ['language', 'text', 'content'],
        extra__redirect_to = reverse('languages:translation_index')
#        context__html_title = 'Translation Create | New Wine Training',
    )

def translation_edit(request, translation_id):
    
    return Form.edit(
        auto__model = Translation,
        auto__instance = Translation.objects.get(id = translation_id),
        auto__include = ['language', 'text', 'content'],
        extra__redirect_to = reverse('languages:translation_index')
#        context__html_title = 'Translation Edit | New Wine Training',
    )

def translation_delete(request, translation_id):
    
    class TranslationDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Translation'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Translation Delete | New Wine Training'),
            )
    
    return TranslationDeleteTemp()

def translator_index(request):
    
    class TranslatorIndexPage(Page):
        
        page_title = html.h1(gettext('Translators'))
        
        instructions = html.p(gettext('Click on the translator\'s name to view details about that translator, as well as any associated data.'))
        
        table = Table(
            auto__model = Translator,
            title = None,
            columns__user = Column(
                display_name = gettext('Translator'),
                 cell__url = lambda row, **_: reverse('languages:translator_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('languages:translator_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Translator Index | New Wine Training'),
            )
            
    return TranslatorIndexPage()

def translator_view(request, translator_id):
    
    translator = get_object_or_404(Translator, pk = translator_id)

    class TranslatorViewPage(Page):
        
        h1 = html.h1(gettext('Translator View: ') + translator.user)
        
        translator_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__translator_id_dt = html.dt('ID'),
            children__translator_id_dd = html.dd(translator.id),
            children__translator_user_dt = html.dt(gettext('Translator')),
            children__translator_user_dd = html.dd(translator.user),
            children__translator_language_dt = html.dt(gettext('Language')),
            children__translator_language_dd = html.dd(gettext(str(translator.language))),
            children__translator_created_dt = html.dt(gettext('Created')),
            children__translator_created_dd = html.dd(translator.created),
            children__translator_creator_dt = html.dt(gettext('Creator')),
            children__translator_creator_dd = html.dd(translator.creator),
            children__translator_modified_dt = html.dt(gettext('Modified')),
            children__translator_modified_dd = html.dd(translator.modified),
            children__translator_modifier_dt = html.dt(gettext('Modifier')),
            children__translator_modifier_dd = html.dd(translator.modifier),
        )
        
        hr1 = html.hr()
        
        language_h2 = html.h2(gettext('Language'))
        languages = Language.objects.filter(pk = translator.language.id)
        
        languages_table = Table(
            auto__model = Language,
            rows = languages,
            title = None,
            empty_message = gettext('No languages'),
            columns__language = Column(
                cell__url = lambda row, **_: reverse('languages:language_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('languages:language_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        translation_h2 = html.h2(gettext('Translations'))
        translations = Translation.objects.filter(Q(creator__id = translator.user.id) | Q(modifier__id = translator.user.id))
        
        table = Table(
            auto__model = Translation,
            rows = translations,
            title = None,
            empty_message = gettext('No translations'),
            columns__text = Column(
                display_name = gettext('Text'),
                cell__url = lambda row, **_: reverse('languages:translation_view', args = (row.pk,)),
            ),
            columns__content = Column(
                display_name = gettext('Translation'),
                cell__value = lambda row, **_: row.content[0 : 50] + '...' if len(row.content) > 50 else row.content
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('languages:translation_edit', args = (row.pk,)),
            ),
        )

        class Meta:
            context = dict(
                html_title = gettext('Translator View | New Wine Training'),
            )
    
    return TranslatorViewPage()

def translator_add(request):
    
    return Form.create(
        auto__model = Translator,
        auto__include = ['user', 'language'],
        extra__redirect_to = reverse('languages:translator_index')
#        context__html_title = 'Translator Create | New Wine Training',
    )

def translator_edit(request, translator_id):
    
    return Form.edit(
        auto__model = Translator,
        auto__instance = Translator.objects.get(id = translator_id),
        auto__include = ['user', 'language'],
        extra__redirect_to = reverse('languages:translator_index')
#        context__html_title = 'Translator Edit | New Wine Training',
    )

def translator_delete(request, translator_id):
    
    class TranslatorDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Translator'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Translator Delete | New Wine Training'),
            )
    
    return TranslatorDeleteTemp()