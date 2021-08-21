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
    return Table(auto__model = Term)

def term_view(request):
    return TermView()

class TermView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def term_add(request):
    return Form.create(auto__model = Term)

def term_edit(request, term_id):
    return Form.create(auto__model = Term)

def term_delete(request, term_id):
    return Form.create(auto__model = Term)

def exercisetype_index(request):
    return Table(auto__model = ExerciseType)

def exercisetype_view(request):
    return ExerciseTypeView()

class ExerciseTypeView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

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