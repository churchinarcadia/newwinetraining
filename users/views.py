from django.shortcuts import render

from newwinetraining.iommi import Page, Form, Table
from iommi import Fragment

# Create your views here.

def usertype_index(request):
    return Table(auto__model = UserType)

def usertype_view(request):
    return UserTypeView()

class UserTypeView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def usertype_add(request):
    return Form.create(auto__model = UserType)

def usertype_edit(request, usertype_id):
    return Form.create(auto__model = UserType)

def usertype_delete(request, usertype_id):
    return Form.create(auto__model = UserType)

def locality_index(request):
    return Table(auto__model = Locality)

def locality_view(request):
    return LocalityView()

class LocalityView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def locality_add(request):
    return Form.create(auto__model = Locality)

def locality_edit(request, locality_id):
    return Form.create(auto__model = Locality)

def locality_delete(request, locality_id):
    return Form.create(auto__model = Locality)

def user_index(request):
    return Table(auto__model = User)

def user_view(request):
    return UserView()

class UserView(Page):
    #h1 = html.h1('NewWineTraining')
    h1 = Fragment('New Wine Training', tag='h1')

    body_text = 'Under construction...'

    class Meta:
        title = 'Home | New Wine Training'

def user_add(request):
    return Form.create(auto__model = User)

def user_edit(request, user_id):
    return Form.create(auto__model = User)

def user_delete(request, user_id):
    return Form.create(auto__model = User)