from django.http.response import Http404

from django.shortcuts import render, get_object_or_404

#from django.http import HttpResponseRedirect
from django.urls import reverse
#from django.utils import timezone

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

from .models import Term, ExerciseType, RecordingLocation, Registration, TrainingMeeting, UserExercise, Text
from languages.models import Language, Translation
from users.models import User

# Create your views here.

def term_index(request):
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class TermIndexPage(Page):
    
        page_title = html.h1(gettext('Terms'))
    
        instructions = html.p(gettext('Click on the year or term to view details about that term, as well as any associated data.'))
    
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
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:term_edit', args = (row.pk,)),
            ),
        )
    
        class Meta:
            context = dict(
                html_title = gettext('Term Index | New Wine Training'),
            )

    return TermIndexPage()

def term_view(request, term_id):
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    term = get_object_or_404(Term, pk = term_id)

    class TermViewPage(Page):
        
        h1 = html.h1(gettext('Term View: ' + str(term.year) + ' ' + term.term))
        
        term_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__term_id_dt = html.dt('ID'),
            children__term_id_dd = html.dd(term.id),
            children__term_term_dt = html.dt(gettext('Term')),
            children__term_term_dd = html.dd(gettext(term.term)),
            children__term_year_dt = html.dt(gettext('Year')),
            children__term_year_dd = html.dd(term.year),
            children__term_language_dt = html.dt(gettext('Language')),
            children__term_language_dd = html.dd(gettext(str(term.language))),
            children__term_start_date_dt = html.dt(gettext('Start Date')),
            children__term_stert_date_dd = html.dd(term.start_date),
            children__term_end_date_dt = html.dt(gettext('End Date')),
            children__term_end_date_dd = html.dd(term.end_date),
            children__term_created_dt = html.dt(gettext('Created')),
            children__term_created_dd = html.dd(term.created),
            children__term_creator_dt = html.dt(gettext('Creator')),
            children__term_creator_dd = html.dd(term.creator),
            children__term_modified_dt = html.dt(gettext('Modified')),
            children__term_modified_dd = html.dd(term.modified),
            children__term_modifier_dt = html.dt(gettext('Modifier')),
            children__term_modifier_dd = html.dd(term.modifier),
        )
        
        hr1 = html.hr()
        
        language_h2 = html.h2(gettext('Language'))
        languages = Language.objects.filter(pk = term.language.id)
        
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
        
        trainingmeeting_h2 = html.h2(gettext('Training Meetings'))
        trainingmeetings = TrainingMeeting.objects.filter(date__gte = term.start_date, date__lte = term.end_date, language = term.language)
        
        trainingmeetings_table = Table(
            auto__model = TrainingMeeting,
            rows = trainingmeetings,
            title = None,
            empty_message = gettext('No training meetings'),
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_edit', args = (row.pk,)),
            ),
        )
        
        hr3 = html.hr()
        
        registrations_h2 = html.h2(gettext('Registrations'))
        registrations = term.registration_terms.all()
        
        registrations_table = Table(
            auto__model = Registration,
            rows = registrations,
            title = None,
            empty_message = gettext('No registrations'),
            auto__exclude = ['term'],
            columns__user = Column(
                display_name = gettext('Registrant'),
                cell__url = lambda row, **_: reverse('trainings:registration_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:registration_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Term View | New Wine Training'),
            )
    
    return TermViewPage()

def term_add(request):
    
    allowed_roles = ['Training Adminstrator', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.create(
        auto__model = Term,
        auto__include = ['year', 'term', 'language', 'start_date', 'end_date'],
        extra__redirect_to = reverse('trainings:term_index'),
#        context__html_title = 'Term Create | New Wine Training',
    )

def term_edit(request, term_id):
    
    allowed_roles = ['Training Adminstrator', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.edit(
        auto__model = Term,
        auto__instance = Term.objects.get(id = term_id),
        auto__include = ['year', 'term', 'language', 'start_date', 'end_date'],
        extra__redirect_to = reverse('trainings:term_index'),
#        context__html_title = 'Term Edit | New Wine Training',
    )

def term_delete(request, term_id):
    
    allowed_roles = ['Training Adminstrator', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class TermDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Term'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Term Delete | New Wine Training'),
            )

def exercisetype_index(request):
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class ExerciseTypeIndexPage(Page):
        
        page_title = html.h1(gettext('Exercise Types'))
        
        instructions = html.p(gettext('Click on the Exercise Type name to view details about that Exercise Type, as well as any associated data.'))
        
        table = Table(
            auto__model = ExerciseType,
            title = None,
            columns__name = Column(
                cell__url = lambda row, **_: reverse('trainings:exercisetype_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:exercisetype_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Exercise Type Index | New Wine Training'),
            )
    
    return ExerciseTypeIndexPage()

def exercisetype_view(request,exercisetype_id):
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    exercisetype = get_object_or_404(ExerciseType, pk = exercisetype_id)

    class ExerciseTypeViewPage(Page):
        
        h1 = html.h1(gettext('Exercise Type View: ' + exercisetype.name))
        
        exercisetype_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__exercisetype_id_dt = html.dt('ID'),
            children__exercisetype_id_dd = html.dd(exercisetype.id),
            children__exercisetype_name_dt = html.dt(gettext('Name')),
            children__exercisetype_name_dd = html.dd(gettext(exercisetype.name)),
            children__exercisetype_active_dt = html.dt(gettext('Active?')),
            children__exercisetype_active_dd = html.dd(gettext(str(exercisetype.active))),
            children__exercisetype_description_dt = html.dt(gettext('Description')),
            children__exercisetype_description_dd = html.dd(gettext(exercisetype.description)),
            children__exercisetype_created_dt = html.dt(gettext('Created')),
            children__exercisetype_created_dd = html.dd(exercisetype.created),
            children__exercisetype_creator_dt = html.dt(gettext('Creator')),
            children__exercisetype_creator_dd = html.dd(exercisetype.creator),
            children__exercisetype_modified_dt = html.dt(gettext('Modified')),
            children__exercisetype_modified_dd = html.dd(exercisetype.modified),
            children__exercisetype_modifier_dt = html.dt(gettext('Modifier')),
            children__exercisetype_modifier_dd = html.dd(exercisetype.modifier),
        )
        
        hr1 = html.hr()
        
        registrations_h2 = html.h2(gettext('Registrations'))
        registrations = exercisetype.registration_exercisetypes.all()
        
        registrations_table = Table(
            auto__model = Registration,
            rows = registrations,
            title = None,
            empty_message = gettext('No registrations'),
            auto__exclude = ['exercisetypes', 'signature'],
            columns__user = Column(
                display_name = gettext('Registrant'),
                cell__url = lambda row, **_: reverse('trainings:registration_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:registration_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        userexercises_h2 = html.h2(gettext('User Exercises'))
        userexercises = exercisetype.userexercise_exercisetypes.all()
        
        userexercises_table = Table(
            auto__model = UserExercise,
            rows = userexercises,
            title = None,
            empty_message = gettext('No user exercises'),
            auto__exclude = ['exercisetypes'],
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:userexercise_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:userexercise_edit', args = (row.pk,)),
            ),
        )

        class Meta:
            context = dict(
                html_title = gettext('Exercise Type View | New Wine Training'),
            )
    
    return ExerciseTypeViewPage()

def exercisetype_add(request):
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.create(
        auto__model = ExerciseType,
        auto__include = ['name', 'description'],
        extra__redirect_to = reverse('trainings:exercisetype_index'),
#        context__html_title = 'Exercise Type Create | New Wine Training',
    )

def exercisetype_edit(request, exercisetype_id):
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.edit(
        auto__model = ExerciseType,
        auto__instance = ExerciseType.objects.get(id = exercisetype_id),
        auto__include = ['name', 'description'],
        extra__redirect_to = reverse('trainings:exercisetype_index'),
#        context__html_title = 'Exercise Type Edit | New Wine Training',
    )

def exercisetype_delete(request, exercisetype_id):
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class ExerciseTypeDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Exercise Type'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Exercise Type Delete | New Wine Training'),
            )
    
    return ExerciseTypeDeleteTemp()

def recordinglocation_index(request):
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class RecordingLocationIndexPage(Page):
        
        page_title = html.h1(gettext('Recording Locations'))
        
        instructions = html.p(gettext('Click on the recording location to view details about that recording location, as well as any associated data.'))
        
        table = Table(
            auto__model = RecordingLocation,
            title = None,
            columns__location = Column(
                cell__url = lambda row, **_: reverse('trainings:recordinglocation_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:recordinglocation_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Recording Location Index | New Wine Training')
            )
        
    return RecordingLocationIndexPage()

def recordinglocation_view(request, recordinglocation_id):
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    recordinglocation = get_object_or_404(RecordingLocation, pk = recordinglocation_id)
    
    class RecordingLocationViewPage(Page):
        
        h1 = html.h1(gettext('Recording Location View: ') + recordinglocation.location)
        
        recordinglocation_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__recordinglocation_id_dt = html.dt('ID'),
            children__recordinglocation_id_dd = html.dd(recordinglocation.id),
            children__recordinglocation_location_dt = html.dt(gettext('Location')),
            children__recordinglocation_location_dd = html.dd(recordinglocation.location),
            children__recordinglocation_code_before_url_dt = html.dt(gettext('Code before URL')),
            children__recordinglocation_code_before_url_dd = html.dd(recordinglocation.code_before_url),
            children__recordinglocation_code_after_url_dt = html.dt(gettext('Code after URL')),
            children__recordinglocation_code_after_url_dd = html.dd(recordinglocation.code_after_url),
            children__recordinglocation_url_identifier_dt = html.dt(gettext('URL Identifier')),
            children__recordinglocation_url_identifier_dd = html.dd(recordinglocation.url_identifier),
            children__recordinglocation_notes_dt = html.dt(gettext('Notes')),
            children__recordinglocation_notes_dd = html.dd(gettext(recordinglocation.notes)),
            children__recordinglocation_created_dt = html.dt(gettext('Created')),
            children__recordinglocation_created_dd = html.dd(recordinglocation.created),
            children__recordinglocation_creator_dt = html.dt(gettext('Creator')),
            children__recordinglocation_creator_dd = html.dd(recordinglocation.creator),
            children__recordinglocation_modified_dt = html.dt(gettext('Modified')),
            children__recordinglocation_modified_dd = html.dd(recordinglocation.modified),
            children__recordinglocation_modifier_dt = html.dt(gettext('Modifier')),
            children__recordinglocation_modifier_dd = html.dd(recordinglocation.modifier),
        )
        
        hr1 = html.hr()
        
        trainingmeetings_h2 = html.h2(gettext('Training Meetings'))
#        trainingmeetings = TrainingMeeting.objects.filter() #TODO

        trainingmeetings_table = Table(
            auto__model = TrainingMeeting,
#            rows = trainingmeetings, #TODO
            title = None,
            empty_message = gettext('No training meetings'),
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_view', args = (row.pk,)),
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
                html_title = gettext('Recording Location View | New Wine Training'),
            )
        
    return RecordingLocationViewPage()

def recordinglocation_add(request):
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.create(
        auto__model = RecordingLocation,
        auto__include = ['location', 'code_before_url', 'code_after_url', 'url_identifier', 'notes'],
        extra__redirect_to = reverse('trainings:recordinglocation_index'),
#        context__html_title = 'Recording Location Create | New Wine Training',
    )

def recordinglocation_edit(request, recordinglocation_id):
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.edit(
        auto__model = RecordingLocation,
        auto__instance = RecordingLocation.objects.get(id = recordinglocation_id),
        auto__include = ['location', 'code_before_url', 'code_after_url', 'url_identifier', 'notes'],
        extra__redirect_to = reverse('trainings:recordinglocation_index'),
#        context__html_title = 'Recording Location Edit | New Wine Training',
    )

def recordinglocation_delete(request, recordinglocation_id):
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class RecordingLocationDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Recording Location'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Recording Location Delete | New Wine Training'),
            )
    
    return RecordingLocationDeleteTemp()

def registration_index(request):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class RegistrationIndexPage(Page):
        
        page_title = html.h1(gettext('Registrations'))
        
        instructions = html.p(gettext('Click on the name to view details about that registration, as well as any associated data.'))
        
        table = Table(
            auto__model = Registration,
            title = None,
            columns__user = Column(
                display_name = gettext('Registrant'),
                cell__url = lambda row, **_: reverse('trainings:registration_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:registration_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Registration Index | New Wine Training'),
            )
            
    return RegistrationIndexPage()

def registration_view(request, registration_id):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    registration = get_object_or_404(Registration, pk = registration_id)

    class RegistrationViewPage(Page):
        
        h1 = html.h1(gettext('Registration View: ') + registration.user.get_full_name() + ' (' + gettext(str(registration.term)) + ')')
        
        registration_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__registration_id_dt = html.dt('ID'),
            children__registration_id_dd = html.dd(registration.id),
            children__registration_user_dt = html.dt(gettext('Registrant')),
            children__registration_user_dd = html.dd(registration.user),
            children__registration_term_dt = html.dt(gettext('Term')),
            children__registration_term_dd = html.dd(gettext(str(registration.term))),
            children__registration_exercisetypes_dt = html.dt(gettext('Exercise Types')),
            children__registration_exercisetypes_dd = html.dd(gettext(', '.join(list(registration.exercisetypes.values_list('name', flat = True))))),
            children__registration_signature_dt = html.dt(gettext('Signature')),
            children__registration_signature_dd = html.dd(registration.signature),
            children__registration_created_dt = html.dt(gettext('Created')),
            children__registration_created_dd = html.dd(registration.created),
            children__registration_creator_dt = html.dt(gettext('Creator')),
            children__registration_creator_dd = html.dd(registration.creator),
            children__registration_modified_dt = html.dt(gettext('Modified')),
            children__registration_modified_dd = html.dd(registration.modified),
            children__registration_modifier_dt = html.dt(gettext('Modifier')),
            children__registration_modifier_dd = html.dd(registration.modifier),
        )
        
        hr1 = html.hr()
        
        users_h2 = html.h2(gettext('Registrant'))
        users = User.objects.filter(pk = registration.user.id)
        
        users_table = Table(
            auto__model = User,
            rows = users,
            title = None,
            empty_message = gettext('No registrants'),
            auto__exclude = ['password'],
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
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('users:user_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        terms_h2 = html.h2(gettext('Term'))
        terms = Term.objects.filter(pk = registration.term.id)
        
        terms_table = Table(
            auto__model = Term,
            rows = terms,
            title = None,
            empty_message = gettext('No terms'),
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
        
        exercisetypes_h2 = html.h2(gettext('Exercise Types'))
        if registration.exercisetypes is not None:
            exercisetypes = registration.exercisetypes.all()
        else:
            exercisetypes = ''
        
        exercisetypes_table = Table(
            auto__model = ExerciseType,
            rows = exercisetypes,
            title = None,
            empty_message = gettext('No exercise types'),
            columns__name = Column(
                cell__url = lambda row, **_: reverse('trainings:exercisetype_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:exercisetype_edit', args = (row.pk,)),
            ),
        )

        class Meta:
            context = dict(
                html_title = gettext('Registration View | New Wine Training'),
            )
    
    return RegistrationViewPage()

def registration_add(request):
    
    return Form.create(
        auto__model = Registration,
        auto__include = ['user', 'term', 'exercisetypes', 'signature'],
        extra__redirect_to = reverse('trainings:registration_index'),
#        context__html_title = 'Registration Create | New Wine Training',
    )

def registration_edit(request, registration_id):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.edit(
        auto__model = Registration,
        auto__instance = Registration.objects.get(id = registration_id),
        auto__include = ['user', 'term', 'exercisetypes', 'signature'],
        extra__redirect_to = reverse('trainings:registration_index'),
#        context__html_title = 'Registration Edit | New Wine Training',
    )

def registration_delete(request, registration_id):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class RegistrationDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Registration'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Registration Delete | New Wine Training'),
            )
    
    return RegistrationDeleteTemp()

def trainingmeeting_index(request):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class TrainingMeetingIndexPage(Page):
        
        page_title = html.h1(gettext('Training Meetings'))
        
        instructions = html.p(gettext('Click on the date to view details about that training meeting, as well as any associated data.'))
        
        table = Table(
            auto__model = TrainingMeeting,
            title = None,
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:trainingmeeting_view', args = (row.pk,)),
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
                html_title = gettext('Training Meeting Index | New Wine Training'),
            )
        
    return TrainingMeetingIndexPage()

def trainingmeeting_view(request, trainingmeeting_id):
    
    allowed_roles = ['Training Adminstrator','Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    trainingmeeting = get_object_or_404(TrainingMeeting, pk = trainingmeeting_id)
    
    class TrainingMeetingViewPage(Page):
        
        h1 = html.h1(gettext('Training Meeting View: ' + trainingmeeting.date))
        
        trainingmeeting_h2 = html.h2('Details')
        dl = html.dl(
            children__trainingmeeting_id_dt = html.dt('ID'),
            children__trainingmeeting_id_dd = html.dd(trainingmeeting.id),
            children__trainingmeeting_date_dt = html.dt(gettext('Date')),
            children__trainingmeeting_date_dd = html.dd(trainingmeeting.date),
            children__trainingmeeting_start_time_dt = html.dt(gettext('Start Time')),
            children__trainingmeeting_start_time_dd = html.dd(trainingmeeting.start_time),
            children__trainingmeeting_end_time_dt = html.dt(gettext('End Time')),
            children__trainingmeeting_end_time_dd = html.dd(trainingmeeting.end_time),
            children__trainingmeeting_language_dt = html.dt(gettext('Language')),
            children__trainingmeeting_language_dd = html.dd(gettext(str(trainingmeeting.language))),
            children__trainingmeeting_location_dt = html.dt(gettext('Location')),
            children__trainingmeeting_location_dd = html.dd(trainingmeeting.location),
            children__trainingmeeting_recording_url_dt = html.dt(gettext('Recording URL')),
            children__trainingmeeting_recording_url_dd = html.dd(trainingmeeting.recording_url),
            children__trainingmeeting_recording_released_datetime_dt = html.dt(gettext('Recording Released')),
            children__trainingmeeting_recording_released_datetime_dd = html.dd(trainingmeeting.recording_released_datetime),
            children__trainingmeeting_recording_released_by_dt = html.dt(gettext('Released By')),
            children__trainingmeeting_recording_released_by_dd = html.dd(trainingmeeting.recording_released_by),
            children__trainingmeeting_notes_dt = html.dt(gettext('Notes')),
            children__trainingmeeting_notes_dd = html.dd(gettext(trainingmeeting.notes)),
            children__trainingmeeting_created_dt = html.dt(gettext('Created')),
            children__trainingmeeting_created_dd = html.dd(trainingmeeting.created),
            children__trainingmeeting_creator_dt = html.dt(gettext('Creator')),
            children__trainingmeeting_creator_dd = html.dd(trainingmeeting.creator),
            children__trainingmeeting_modified_dt = html.dt(gettext('Modified')),
            children__trainingmeeting_modified_dd = html.dd(trainingmeeting.modified),
            children__trainingmeeting_modifier_dt = html.dt(gettext('Modifier')),
            children__trainingmeeting_modifier_dd = html.dd(trainingmeeting.modifier),
        )

        hr1 = html.hr()
        
        terms_h2 = html.h2(gettext('Term'))
        terms = Term.objects.filter(start_date__lte = trainingmeeting.date, end_date__gte = trainingmeeting.date)

        terms_table = Table(
            auto__model = Term,
#            rows = terms,
            title = None,
            empty_message = gettext('No terms'),
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
        
        hr2 = html.hr()
        
        languages_h2 = html.h2(gettext('Language'))
        languages = Language.object.filter(pk = trainingmeeting.language.id)
        
        languages_table = Table(
            auto__model = Language,
            rows = languages,
            title = None,
            empty_message = gettext('No languages'),
            columns__language = Column(
                cell__url = lambda row, **_: reverse('languages:language_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('languages:language_edit', args = (row.pk,)),
            ),
        )
        
        hr3 = html.hr()
        
        recordinglocations_h2 = html.h2(gettext('Recording Location'))
#        recordinglocations = RecordingLocation.objects. #TODO

        recordinglocations_table = Table(
            auto__model = RecordingLocation,
#            rows = recordinglocations, #TODO
            title = None,
            empty_message = gettext('No recording locations'),
            columns__location = Column(
                cell__url = lambda row, **_: reverse('trainings:recordinglocation_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:recordinglocation_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Recording Location View | New Wine Training'),
            )
            
    return TrainingMeetingViewPage()

def trainingmeeting_add(request):
    
    allowed_roles = ['Training Adminstrator','Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.create(
        auto__model = TrainingMeeting,
        auto__include = ['date', 'start_time', 'end_time', 'language', 'location', 'notes'],
        extra__redirect_to = reverse('trainings:trainingmeeting_index'),
#        context__html_title = 'Training Meeting Create | New Wine Training',
    )

def trainingmeeting_edit(request, trainingmeeting_id):
    
    allowed_roles = ['Training Adminstrator','Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.edit(
        auto__model = TrainingMeeting,
        auto__instance = TrainingMeeting.objects.get(id = trainingmeeting_id),
        auto__include = ['date', 'start_time', 'end_time', 'language', 'location', 'recording_url', 'recording_released_datetime', 'recording_released_by', 'notes'],
        extra__redirect_to = reverse('trainings:trainingmeeting_index'),
#        context__html_title = 'Training Meeting Edit | New Wine Training',
    )

def trainingmeeting_delete(request, trainingmeeting_id):
    
    allowed_roles = ['Training Adminstrator','Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class TrainingMeetingDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Training Meeting'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Training Meeting Delete | New Wine Training'),
            )
    
    return TrainingMeetingDeleteTemp()

def userexercise_index(request):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class UserExerciseIndexPage(Page):
        
        page_title = html.h1(gettext('User Exercises'))
        
        instructions = html.p(gettext('Click on the date or user to view details about that user exercise, as well as any associated data.'))
        
        table = Table(
            auto__model = UserExercise,
            title = None,
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:userexercise_view', args = (row.pk,))
            ),
            columns__user = Column(
                cell__url = lambda row, **_: reverse('trainings:userexercise_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:userexercise_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('User Exercise Index | New Wine Training'),
            )
        
    return UserExerciseIndexPage()

def userexercise_view(request, userexercise_id):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    userexercise = get_object_or_404(UserExercise, pk = userexercise_id)

    class UserExerciseViewPage(Page):
        
        h1 = html.h1(gettext('User Exercise View: ') + userexercise.user.get_full_name() + ' (' + str(userexercise.date) + ')')
    
        userexercise_h2 = html.h2('Details')
        dl = html.dl(
            children__userexercise_id_dt = html.dt('ID'),
            children__userexercise_id_dd = html.dd(userexercise.id),
            children__userexercise_date_dt = html.dt(gettext('Date')),
            children__userexercise_date_dd = html.dd(userexercise.date),
            children__userexercise_user_dt = html.dt(gettext('User')),
            children__userexercise_user_dd = html.dd(userexercise.user),
            children__userexercise_exercisetypes_dt = html.dt(gettext('Exercise Types')),
            children__userexercise_exercisetypes_dd = html.dd(gettext(', '.join(list(userexercise.exercisetypes.values_list('name', flat = True))))),
            children__userexercise_created_dt = html.dt(gettext('Created')),
            children__userexercise_created_dd = html.dd(userexercise.created),
            children__userexercise_creator_dt = html.dt(gettext('Creator')),
            children__userexercise_creator_dd = html.dd(userexercise.creator),
            children__userexercise_modified_dt = html.dt(gettext('Modified')),
            children__userexercise_modified_dd = html.dd(userexercise.modified),
            children__userexercise_modifier_dt = html.dt(gettext('Modifier')),
            children__userexercise_modifier_dd = html.dd(userexercise.modifier),
        )
        
        hr1 = html.hr()
        
        users_h2 = html.h2(gettext('User'))
        users = User.objects.filter(pk = userexercise.user.id)
        
        users_table = Table(
            auto__model = User,
            rows = users,
            auto__exclude = ['password'],
            title = None,
            empty_message = gettext('No users'),
            columns__first_name = Column(
                cell__url = lambda row, **_: reverse('users:user_view', args = (row.pk,)),
            ),
            columns__last_name = Column(
                cell__url = lambda row, **_: reverse('users:user_view', args = (row.pk,)),
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('users:user_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        exercisetypes_h2 = html.h2(gettext('Exercise Types'))
        exercisetypes = userexercise.exercisetypes.all()
        
        exercisetypes_table = Table(
            auto__model = ExerciseType,
            rows = exercisetypes,
            title = None,
            empty_message = gettext('No exercise types'),
            columns__name = Column(
                cell__url = lambda row, **_: reverse('trainings:exercisetype_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('trainings:exercisetype_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('User Exercise View | New Wine Training'),
            )
    
    return UserExerciseViewPage()

def userexercise_add(request):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.create(
        auto__model = UserExercise,
        auto__include = ['date', 'user', 'exercisetypes'],
        extra__redirect_to = reverse('trainings:userexercise_index'),
#        context__html_title = 'User Exercise Create | New Wine Training',
    )

def userexercise_edit(request, userexercise_id):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.edit(
        auto__model = UserExercise,
        auto__instance = UserExercise.objects.get(id = userexercise_id),
        auto__include = ['date', 'user', 'exercisetypes'],
        extra__redirect_to = reverse('trainings:userexercise_index'),
#        context__html_title = 'User Exercise Edit | New Wine Training',
    )

def userexercise_delete(request, userexercise_id):
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class UserExerciseDeleteTemp(Page):
        page_title = html.h1(gettext('Delete User Exercise'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('User Exercise Delete | New Wine Training'),
            )
    
    return UserExerciseDeleteTemp()

def text_index(request):
    
    allowed_roles = ['Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class TextIndexPage(Page):
        
        page_title = html.h1(gettext('Texts'))

        instructions = html.p(gettext('Click on the text name to view details about that text, as well as any associated data.'))
        
        table = Table(
            auto__model = Text,
            title = None,
            columns__name = Column(
                cell__url = lambda row, **_: reverse('trainings:text_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:text_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Text Index | New Wine Training'),
            )
        
    return TextIndexPage()

def text_view(request, text_id):
    
    allowed_roles = ['Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    text = get_object_or_404(Text, pk = text_id)

    class TextViewPage(Page):
        
        h1 = html.h1(gettext('Text View: ') + text.name)
        
        text_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__text_id_dt = html.dt('ID'),
            children__text_id_dd = html.dd(text.id),
            children__text_name_dt = html.dt(gettext('Name')),
            children__text_name_dd = html.dd(text.name),
            children__text_description_dt = html.dt(gettext('Description')),
            children__text_description_dd = html.dd(gettext(text.description)),
            children__text_created_dt = html.dt(gettext('Created')),
            children__text_created_dd = html.dd(text.created),
            children__text_creator_dt = html.dt(gettext('Creator')),
            children__text_creator_dd = html.dd(text.creator),
            children__text_modified_dt = html.dt(gettext('Modified')),
            children__text_modified_dd = html.dd(text.modified),
            children__text_modifier_dt = html.dt(gettext('Modifier')),
            children__text_modifier_dd = html.dd(text.modifier),
        )
        
        h1 = html.h1()
        
        translations_h2 = html.h2(gettext('Translations'))
        translations = text.translation_texts.all()
        
        translations_table = Table(
            auto__model = Translation,
            rows = translations,
            title = None,
            empty_message = gettext('No translations'),
            auto__exclude = ['text'],
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
            title = gettext('Text View | New Wine Training'),
    
    return TextViewPage()

def text_add(request):
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.create(
        auto__model = Text,
        auto__include = ['name', 'description'],
        extra__redirect_to = reverse('trainings:text_index'),
#        context__html_title = 'Text Create | New Wine Training',
    )

def text_edit(request, text_id):
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    return Form.edit(
        auto__model = Text,
        auto__instance = Text.objects.get(id = text_id),
        auto__include = ['name', 'description'],
        extra__redirect_to = reverse('trainings:text_index'),
#        context__html_title = 'Text Edit | New Wine Training',
    )

def text_delete(request, text_id):
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == False:
        raise Http404
    
    class TextDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Text'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Text Delete | New Wine Training'),
            )
    
    return TextDeleteTemp()