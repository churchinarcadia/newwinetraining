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
from users.models import User

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
            context = dict(
                html_title = 'Exercise Type View | New Wine Training',
            )
    
    return ExerciseTypeViewPage()

def exercisetype_add(request):
    
    return Form.create(
        auto__model = ExerciseType,
        auto__include = ['name', 'description'],
        context__html_title = 'Exercise Type Create | New Wine Training',
    )

def exercisetype_edit(request, exercisetype_id):
    
    return Form.edit(
        auto__model = ExerciseType,
        auto__instance = ExerciseType.objects.get(id = exercisetype_id),
        auto__include = ['name', 'description'],
        context__html_title = 'Exercise Type Edit | New Wine Training',
    )

def exercisetype_delete(request, exercisetype_id):
    
    class ExerciseTypeDeleteTemp(Page):
        page_title = html.h1('Delete Exercise Type')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'Exercise Type Delete | New Wine Training',
            )
    
    return ExerciseTypeDeleteTemp()

def recordinglocation_index(request):
    
    class RecordingLocationIndexPage(Page):
        
        page_title = html.h1('Recording Locations')
        
        instructions = html.p('Click on the recording location to view details about that recording location, as well as any associated data.')
        
        table = Table(
            auto__model = RecordingLocation,
            title = None,
            columns__location = Column(
                cell__url = lambda row, **_: reverse('trainings:recordinglocation_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:recordinglocation_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'Recording Location Index | New Wine Training'
            )
        
    return RecordingLocationIndexPage()

def recordinglocation_view(request, recordinglocation_id):
    
    recordinglocation = get_object_or_404(RecordingLocation, pk = recordinglocation_id)
    
    class RecordingLocationViewPage(Page):
        
        h1 = html.h1('Recording Location View: ' + recordinglocation.location)
        
        recordinglocation_h2 = html.h2('Details')
        dl = html.dl()
        recordinglocation_id_dt = html.dt('ID')
        recordinglocation_id_dd = html.dd(recordinglocation.id)
        recordinglocation_location_dt = html.dt('Location')
        recordinglocation_location_dd = html.dd(recordinglocation.location)
        recordinglocation_code_before_url_dt = html.dt('Code before URL')
        recordinglocation_code_before_url_dd = html.dd(recordinglocation.code_before_url)
        recordinglocation_code_after_url_dt = html.dt('Code after URL')
        recordinglocation_code_after_url_dd = html.dd(recordinglocation.code_after_url)
        recordinglocation_url_identifier_dt = html.dt('URL Identifier')
        recordinglocation_url_identifier_dd = html.dd(recordinglocation.url_identifier)
        recordinglocation_notes_dt = html.dt('Notes')
        recordinglocation_notes_dd = html.dd(recordinglocation.notes)
        recordinglocation_created_dt = html.dt('Created')
        recordinglocation_created_dd = html.dd(recordinglocation.created)
        recordinglocation_creator_dt = html.dt('Creator')
        recordinglocation_creator_dd = html.dd(recordinglocation.creator)
        recordinglocation_modified_dt = html.dt('Modified')
        recordinglocation_modified_dd = html.dd(recordinglocation.modified)
        recordinglocation_modifier_dt = html.dt('Modifier')
        recordinglocation_modifier_dd = html.dd(recordinglocation.modifier)
        
        hr1 = html.hr()
        
        trainingmeetings_h2 = html.h2('Training Meetings')
#        trainingmeetings = TrainingMeeting.objects.filter #TODO

        trainingmeetings_table = Table(
            auto__model = TrainingMeeting,
#            rows = trainingmeetings, #TODO
            title = None,
            empty_message = 'No training meetings'
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
        
        class Meta:
            context = dict(
                html_title = 'Recording Location View | New Wine Training',
            )
        
    return RecordingLocationViewPage()

def recordinglocation_add(request):
    
    return Form.create(
        auto__model = RecordingLocation,
        auto__include = ['location', 'code_before_url', 'code_after_url', 'url_identifier', 'notes'],
        context__html_title = 'Recording Location Create | New Wine Training',
    )

def recordinglocation_edit(request, recordinglocation_id):
    
    return Form.edit(
        auto__model = RecordingLocation,
        auto__instance = RecordingLocation.objects.get(id = recordinglocation_id),
        auto__include = ['location', 'code_before_url', 'code_after_url', 'url_identifier', 'notes'],
        context__html_title = 'Recording Location Create | New Wine Training',
    )

def recordinglocation_delete(request, recordinglocation_id):
    
    class RecordingLocationDeleteTemp(Page):
        page_title = html.h1('Delete Recording Location')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'Recording Location Delete | New Wine Training',
            )
    
    return RecordingLocationDeleteTemp()

def registration_index(request):
    
    class RegistrationIndexPage(Page):
        
        page_title = html.h1('Registrations')
        
        instructions = html.p('Click on the name to view details about that registration, as well as any associated data.')
        
        table = Table(
            auto__model = Registration,
            title = None,
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
                html_title = 'Registration Index | New Wine Training'
            )
            
    return RegistrationIndexPage()

def registration_view(request, registration_id):
    
    registration = get_object_or_404(Registration, pk = registration_id)

    class RegistrationViewPage(Page):
        
        h1 = html.h1('Registration View: ' + registration.user + ' (' + registration.term + ')')
        
        registration_h2 = html.h2('Details')
        dl = html.dl()
        registration_id_dt = html.dt('ID')
        registration_id_dd = html.dd(registration.id)
        registration_user_dt = html.dt('Registrant')
        registration_user_dd = html.dd(registration.user)
        registration_term_dt = html.dt('Term')
        registration_term_dd = html.dd(registration.term)
        registration_exercisetypes_dt = html.dt('Exercise Types')
        registration_exercisetypes_dd = html.dd(registration.exercisetypes)
        registration_signature_dt = html.dt('Signature')
        registration_signature_dd = html.dd(registration.signature)
        registration_created_dt = html.dt('Created')
        registration_created_dd = html.dd(registration.created)
        registration_creator_dt = html.dt('Creator')
        registration_creator_dd = html.dd(registration.creator)
        registration_modified_dt = html.dt('Modified')
        registration_modified_dd = html.dd(registration.modified)
        registration_modifier_dt = html.dt('Modifier')
        registration_modifier_dd = html.dd(registration.modifier)
        
        hr1 = html.hr()
        
        users_h2 = html.h2('Registrant')
        users = registration.user.all()
        
        users_table = Table(
            auto__model = User,
            rows = users,
            title = None,
            empty_message = 'No registrants',
            auto_exclude = ['password'],
            columns__first_name = Column(
                cell__url = lambda row, **_: reverse('users:user_view', args = (row.pk,)),
            ),
            columns__last_name = Column(
                cell__url = lambda row, **_: reverse('users:user_view', args = (row.pk,)),
            ),
            columns__chinese_name = Column(
                cell__url = lambda row, **_: reverse('users:user_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('users:user_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        terms_h2 = html.h2('Term')
        terms = registration.term.all()
        
        terms_table = Table(
            auto__model = Table,
            rows = terms,
            title = None,
            empty_message = 'No terms',
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
        
        exercisetypes_h2 = html.h2('Exercise Types')
        exercisetypes = registration.exercisetypes.all()
        
        exercisetypes_table = Table(
            auto__model = ExerciseType,
            rows = exercisetypes,
            title = None,
            empty_message = 'No exercise types',
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
                html_title = 'Registration View | New Wine Training',
            )
    
    return RegistrationViewPage()

def registration_add(request):
    
    return Form.create(
        auto__model = Registration,
        auto__include = ['user', 'term', 'exercisetypes', 'signature'],
        context__html_title = 'Registration Create | New Wine Training',
    )

def registration_edit(request, registration_id):
    
    return Form.edit(
        auto__model = Registration,
        auto__instance = Registration.objects.get(id = registration_id),
        auto__include = ['user', 'term', 'exercisetypes', 'signature'],
        context__html_title = 'Registration Edit | New Wine Training',
    )

def registration_delete(request, registration_id):
    
    class RegistrationDeleteTemp(Page):
        page_title = html.h1('Delete Registration')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'Registration Delete | New Wine Training',
            )
    
    return RegistrationDeleteTemp()

def trainingmeeting_index(request):
    
    class TrainingMeetingIndexPage(Page):
        
        page_title = html.h1('Training Meetings')
        
        instructions = html.p('Click on the date to view details about that training meeting, as well as any associated data.')
        
        table = Table(
            auto__model = TrainingMeeting,
            title = None,
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
        
        class Meta:
                context = dict(
                html_title = 'Training Meeting Index | New Wine Training',
            )
        
    return TrainingMeetingIndexPage()

def trainingmeeting_view(request, trainingmeeting_id):
    
    trainingmeeting = get_object_or_404(TrainingMeeting, pk = trainingmeeting_id)
    
    class TrainingMeetingViewPage(Page):
        
        h1 = html.h1('Training Meeting View: ' + trainingmeeting.date)
        
        trainingmeeting_h2 = html.h2('Details')
        dl = html.dl()
        trainingmeeting_id_dt = html.dt('ID')
        trainingmeeting_id_dd = html.dd(trainingmeeting.id)
        trainingmeeting_date_dt = html.dt('Date')
        trainingmeeting_date_dd = html.dd(trainingmeeting.date)
        trainingmeeting_start_time_dt = html.dt('Start Time')
        trainingmeeting_start_time_dd = html.dd(trainingmeeting.start_time)
        trainingmeeting_end_time_dt = html.dt('End Time')
        trainingmeeting_end_time_dd = html.dd(trainingmeeting.end_time)
        trainingmeeting_language_dt = html.dt('Language')
        trainingmeeting_language_dd = html.dd(trainingmeeting.language)
        trainingmeeting_location_dt = html.dt('Location')
        trainingmeeting_location_dd = html.dd(trainingmeeting.location)
        trainingmeeting_recording_url_dt = html.dt('Recording URL')
        trainingmeeting_recording_url_dd = html.dd(trainingmeeting.recording_url)
        trainingmeeting_recording_released_datetime_dt = html.dt('Recording Released')
        trainingmeeting_recording_released_datetime_dd = html.dd(trainingmeeting.recording_released_datetime)
        trainingmeeting_recording_released_by_dt = html.dt('Released By')
        trainingmeeting_recording_released_by_dd = html.dd(trainingmeeting.recording_released_by)
        trainingmeeting_notes_dt = html.dt('Notes')
        trainingmeeting_notes_dd = html.dd(trainingmeeting.notes)
        trainingmeeting_created_dt = html.dt('Created')
        trainingmeeting_created_dd = html.dd(trainingmeeting.created)
        trainingmeeting_creator_dt = html.dt('Creator')
        trainingmeeting_creator_dd = html.dd(trainingmeeting.creator)
        trainingmeeting_modified_dt = html.dt('Modified')
        trainingmeeting_modified_dd = html.dd(trainingmeeting.modified)
        trainingmeeting_modifier_dt = html.dt('Modifier')
        trainingmeeting_modifier_dd = html.dd(trainingmeeting.modifier)

        hr1 = html.hr()
        
        terms_h2 = html.h2('Term')
#        terms = Term.objects

        terms_table = Table(
            auto__model = Term,
#            rows = terms,
            title = None,
            empty_message = 'No terms',
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
        
        hr2 = html.hr()
        
        languages_h2 = html.h2('Language')
        languages = trainingmeeting.language.all()
        
        languages_table = Table(
            auto__model = Language,
            rows = languages,
            title = None,
            empty_message = 'No languages',
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
        
        hr3 = html.hr()
        
        recordinglocations_h2 = html.h2('Recording Location')
#        recordinglocations = RecordingLocation.objects.

        recordinglocations_table = Table(
            auto__model = RecordingLocation,
#            rows = recordinglocations,
            title = None,
            empty_message = 'No recording locations',
            columns__location = Column(
                cell__url = lambda row, **_: reverse('trainings:recordinglocation_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:recordinglocation_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'Recording Location View | New Wine Training',
            )
            
    return TrainingMeetingViewPage()

def trainingmeeting_add(request):
    
    return Form.create(
        auto__model = TrainingMeeting,
        auto__include = ['language', 'code'],
        context__html_title = 'Language Create | New Wine Training',
    )

def trainingmeeting_edit(request, trainingmeeting_id):
    
    return Form.edit(
        auto__model = Language,
        auto__instance = Language.objects.get(id = language_id),
        auto__include = ['language', 'code'],
        context__html_title = 'Language Edit | New Wine Training',
    )

def trainingmeeting_delete(request, trainingmeeting_id):
    
    class LangaugeDeleteTemp(Page):
        page_title = html.h1('Delete Language')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'Language Delete | New Wine Training',
            )
    
    return LangaugeDeleteTemp()

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