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

from .models import Term, ExerciseType, RecordingLocation, Registration, TrainingMeeting, UserExercise, Text
from languages.models import Language, Translation

# Create your views here.

def term_index(request):
    
    class TermIndexPage(Page):
    
        page_title = html.h1('Terms')
    
        instructions = html.p('Click on the year or term to view details about that term, as well as any associated data.')
    
        table = Table(
            auto__model = Term,
            title = None,
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
    
        class Meta:
            context = dict(
                html_title = 'Term Index | New Wine Training',
            )

    return TermIndexPage()

def term_view(request, term_id):
    
    term = get_object_or_404(Term, pk = term_id)

    class TermViewPage(Page):
        
        h1 = html.h1('Term View: ' + term.year + ' ' + term.term)
        
        term_h2 = html.h2('Details')
        dl = html.dl()
        term_id_dt = html.dt('ID')
        term_id_dd = html.dd(term.id)
        term_term_dt = html.dt('Term')
        term_term_dd = html.dd(term.term)
        term_year_dt = html.dt('Year')
        term_year_dt = html.dd(term.year)
        term_language_dt = html.dt('Language')
        term_language_dd = html.dd(term.language)
        term_start_date_dt = html.dt('Start Date')
        term_stert_date_dd = html.dd(term.start_date)
        term_end_date_dt = html.dt('End Date')
        term_end_date_dd = html.dd(term.end_date)
        term_created_dt = html.dt('Created')
        term_created_dd = html.dd(term.created)
        term_creator_dt = html.dt('Creator')
        term_creator_dd = html.dd(term.creator)
        term_modified_dt = html.dt('Modified')
        term_modified_dd = html.dd(term.modified)
        term_modifier_dt = html.dt('Modifier')
        term_modifier_dt = html.dd(term.modifier)
        
        hr1 = html.hr()
        
        language_h2 = html.h2('Language')
        languages = term.language.all()
        
        languages_table = Table(
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
        
        hr2 = html.hr()
        
        trainingmeeting_h2 = html.h2('Training Meetings')
#        trainingmeetings = TrainingMeeting.objects.filter()
        #TODO finish filter
        
        trainingmeetings_table = Table(
            auto__model = TrainingMeeting,
#            rows = trainingmeetings, #TODO
            title = None,
            empty_message = 'No training meetings',
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_edit', args = (row.pk,)),
            ),
        )
        
        hr3 = html.hr()
        
        registrations_h2 = html.h2('Registrations')
        registrations = term.registration_terms.all()
        
        registrations_table = Table(
            auto__model = Registration,
            rows = registrations,
            title = None,
            empty_message = 'No registrations',
            auto__exclude = ['term'],
            columns__user = Column(
                display_name = 'Registrant',
                cell__url = lambda row, **_: reverse('trainings:registration_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:registration_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'Term View | New Wine Training',
            )
    
    return TermViewPage()

def term_add(request):
    
    return Form.create(
        auto__model = Term,
        auto__include = ['year', 'term', 'language', 'start_date', 'end_date'],
        context__html_title = 'Term Create | New Wine Training',
    )

def term_edit(request, term_id):
    
    return Form.edit(
        auto__model = Term,
        auto__instance = Term.objects.get(id = term_id),
        auto__include = ['year', 'term', 'language', 'start_date', 'end_date'],
        context__html_title = 'Term Edit | New Wine Training',
    )

def term_delete(request, term_id):
    
    class TermDeleteTemp(Page):
        page_title = html.h1('Delete Term')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'Term Delete | New Wine Training',
            )

def exercisetype_index(request):
    
    class ExerciseTypeIndexPage(Page):
        
        page_title = html.h1('Exercise Types')
        
        instructions = html.p('Click on the Exercise Type name to view details about that Exercise Type, as well as any associated data.')
        
        table = Table(
            auto__model = ExerciseType,
            title = None,
            columns__name = Column(
                cell__url = lambda row, **_: reverse('trainings:exercisetype_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:exercisetype_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'Exercise Type Index | New Wine Training'
            )
    
    return ExerciseTypeIndexPage()

def exercisetype_view(request,exercisetype_id):
    
    exercisetype = get_object_or_404(ExerciseType, pk = exercisetype_id)

    class ExerciseTypeViewPage(Page):
        
        h1 = html.h1('Exercise Type View: ' + exercisetype.name)
        
        exercisetype_h2 = html.h2('Details')
        dl = html.dl()
        exercisetype_id_dt = html.dt('ID')
        exercisetype_id_dd = html.dd(exercisetype.id)
        exercisetype_name_dt = html.dt('Name')
        exercisetype_name_dd = html.dd(exercisetype.name)
        exercisetype_description_dt = html.dt('description')
        exercisetype_description_dd = html.dd(exercisetype.description)
        exercisetype_created_dt = html.dt('Created')
        exercisetype_created_dd = html.dd(exercisetype.created)
        exercisetype_creator_dt = html.dt('Creator')
        exercisetype_creator_dd = html.dd(exercisetype.creator)
        exercisetype_modified_dt = html.dt('Modified')
        exercisetype_modified_dd = html.dd(exercisetype.modified)
        exercisetype_modifier_dt = html.dt('Modifier')
        exercisetype_modifier_dd = html.dd(exercisetype.modifier)
        
        hr1 = html.hr()
        
        registrations_h2 = html.h2('Registrations')
        registrations = exercisetype.registration_exercisetypes.all()
        
        registrations_table = Table(
            auto__model = Registration,
            rows = registrations,
            title = None,
            empty_message = 'No registrations',
            auto_exclude = ['exercisetypes', 'signature'],
            columns__user = Column(
                display_name = 'Registrant',
                cell__url = lambda row, **_: reverse('trainings:registration_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:registration_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        userexercises_h2 = html.h2('User Exercises')
        userexercises = exercisetype.userexercise_exercisetypes.all()
        
        userexercises_table = Table(
            auto__model = UserExercise,
            rows = userexercises,
            title = None,
            empty_message = 'No user exercises',
            auto__exclude = ['exercisetypes'],
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:userexercise_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:userexercise_edit', args = (row.pk,)),
            ),
        )
        
        

        class Meta:
            title = 'Home | New Wine Training'
    
    return ExerciseTypeViewPage()

def exercisetype_add(request):
    return Form.create(auto__model = ExerciseType)

def exercisetype_edit(request, exercisetype_id):
    return Form.create(auto__model = ExerciseType)

def exercisetype_delete(request, exercisetype_id):
    return Form.create(auto__model = ExerciseType)

def recordinglocation_index(request):
    return Table(auto__model = RecordingLocation)

def recordinglocation_view(request):
    return RecordingLocationView()

class RecordingLocationView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def recordinglocation_add(request):
    return Form.create(auto__model = RecordingLocation)

def recordinglocation_edit(request, recordinglocation_id):
    return Form.create(auto__model = RecordingLocation)

def recordinglocation_delete(request, recordinglocation_id):
    return Form.create(auto__model = RecordingLocation)

def registration_index(request):
    return Table(auto__model = Registration)

def registration_view(request):
    return RegistrationView()

class RegistrationView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def registration_add(request):
    return Form.create(auto__model = Registration)

def registration_edit(request, registration_id):
    return Form.create(auto__model = Registration)

def registration_delete(request, registration_id):
    return Form.create(auto__model = Registration)

def trainingmeeting_index(request):
    return Table(auto__model = TrainingMeeting)

def trainingmeeting_view(request):
    return TrainingMeetingView()

class TrainingMeetingView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def trainingmeeting_add(request):
    return Form.create(auto__model = TrainingMeeting)

def trainingmeeting_edit(request, trainingmeeting_id):
    return Form.create(auto__model = TrainingMeeting)

def trainingmeeting_delete(request, trainingmeeting_id):
    return Form.create(auto__model = TrainingMeeting)

def userexercise_index(request):
    return Table(auto__model = UserExercise)

def userexercise_view(request):
    return UserExerciseView()

class UserExerciseView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def userexercise_add(request):
    return Form.create(auto__model = UserExercise)

def userexercise_edit(request, userexercise_id):
    return Form.create(auto__model = UserExercise)

def userexercise_delete(request, userexercise_id):
    return Form.create(auto__model = UserExercise)

def text_index(request):
    return Table(auto__model = Text)

def text_view(request):
    return TextView()

class TextView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def text_add(request):
    return Form.create(auto__model = Text)

def text_edit(request, text_id):
    return Form.create(auto__model = Text)

def text_delete(request, text_id):
    return Form.create(auto__model = Text)