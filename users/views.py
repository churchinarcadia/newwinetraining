from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from newwinetraining.iommi import Page, Form, Table, Column

from iommi import ( 
    Fragment,
    html,
    Action,
    Field,
)

from django.contrib.auth.models import Group, Permission

from .models import UserType, User, Locality
from languages.models import Language, Translator
from trainings.models import Registration, UserExercise

# Create your views here.

def usertype_index(request):
    
    class UserTypeIndexPage(Page):
        
        page_title = html.h1('User Types')
        
        instructions = html.p('Click on the user type name to view details about that user type, as well as any associated data.')
        
        table = Table(
            auto__model = UserType,
            title = None,
            columns__name = Column(
                cell__url = lambda row, **_: reverse('users:usertype_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('users:usertype_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'User Type Index | New Wine Training',
            )
    
    return UserTypeIndexPage()

def usertype_view(request, usertype_id):
    
    usertype = get_object_or_404(UserType, pk = usertype_id)
    
    class UserTypeViewPage(Page):
        
        h1 = html.h1('User Type View: ' + usertype.name)
        
        usertype_h2 = html.h2('Details')
        dl = html.dl()
        usertype_id_dt = html.dt('ID')
        usertype_id_dd = html.dd(usertype.id)
        usertype_name_dt = html.dt('Name')
        usertype_name_dd = html.dd(usertype.name)
        usertype_description_dt = html.dt('Description')
        usertype_description_dd = html.dd(usertype.description)
        usertype_active_dt = html.dt('Active?')
        usertype_active_dd = html.dd(usertype.active)
        usertype_created_dt = html.dt('Created')
        usertype_created_dd = html.dd(usertype.created)
        usertype_creator_dt = html.dt('Creator')
        usertype_creator_dd = html.dd(usertype.creator)
        usertype_modified_dt = html.dt('Modified')
        usertype_modified_dd = html.dd(usertype.modified)
        usertype_modifier_dt = html.dt('Modifier')
        usertype_modifier_dd = html.dd(usertype.modifier)
        
        hr1 = html.hr()
        
        users_h2 = html.h2('Users')
        users = usertype.user_usertypes.all()
        
        users_table = Table(
            auto__model = User,
            rows = users,
            title = None,
            empty_message = 'No users',
            auto__exclude = ['phone_number', 'email'],
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
        
        class Meta:
            context = dict(
                html_title = 'User Type View | New Wine Training',
            )
    
    return UserTypeViewPage()

def usertype_add(request):
    
    return Form.create(
        auto__model = UserType,
        auto__include = ['name', 'description', 'active'],
        context__html_title = 'User Type Create | New Wine Training',
    )

def usertype_edit(request, usertype_id):
    
    return Form.edit(
        auto__model = UserType,
        auto__instance = UserType.objects.get(id = usertype_id),
        auto__include = ['name', 'description', 'active'],
        context__html_title = 'User Type Edit | New Wine Training',
    )

def usertype_delete(request, usertype_id):
    
    class UserTypeDeleteTemp(Page):
        page_title = html.h1('Delete User Type')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'User Type Delete | New Wine Training',
            )
    
    return UserTypeDeleteTemp()

def locality_index(request):
    
    class LocalityIndexPage(Page):
        
        page_title = html.h1('Localities')
        
        instructions = html.p('Click on the locality name to view details about that locality, as well as any associated data.')
        
        table = Table(
            auto__model = Locality,
            title = None,
            columns__locality = Column(
                cell__url = lambda row, **_: reverse('users:locality_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('users:locality_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'Locality Index | New Wine Training',
            )
        
    return LocalityIndexPage()

def locality_view(request, locality_id):
    
    locality = get_object_or_404(Locality, pk = locality_id)

    class LocalityViewPage(Page):
        
        h1 = html.h1('Locality View: ' + locality.locality)
        
        locality_h2 = html.h2('Details')
        dl = html.dl()
        locality_id_dt = html.dt('ID')
        locality_id_dd = html.dd(locality.id)
        locality_locality_dt = html.dt('Locality')
        locality_locality_dd = html.dd(locality.locality)
        locality_active_dt = html.dt('Active?')
        locality_active_dd = html.dd(locality.active)
        locality_created_dt = html.dt('Created')
        locality_created_dd = html.dd(locality.created)
        locality_creator_dt = html.dt('Creator')
        locality_creator_dd = html.dd(locality.creator)
        locality_modified_dt = html.dt('Modified')
        locality_modified_dd = html.dd(locality.modified)
        locality_modifier_dt = html.dt('Modifier')
        locality_modifier_dd = html.dd(locality.modifier)
        
        hr1 = html.hr()
        
        users_h2 = html.h2('Users')
        users = locality.user_localities.all()
        
        users_table = Table(
            auto__model = User,
            rows = users,
            title = None,
            empty_message = 'No users',
            auto__exclude = ['locality'],
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
        
        class Meta:
            context = dict(
                html_title = 'Locality View | New Wine Training',
            )
            
    return LocalityViewPage()

def locality_add(request):
    
    return Form.create(
        auto__model = Locality,
        auto__include = ['locality', 'active'],
        context__html_title = 'Locality Create | New Wine Training',
    )

def locality_edit(request, locality_id):
    
    return Form.edit(
        auto__model = Locality,
        auto__instance = Locality.objects.get(id = locality_id),
        auto__include = ['locality', 'active'],
        context__html_title = 'Locality Edit | New Wine Training',
    )

def locality_delete(request, locality_id):
    
    class LocalityDeleteTemp(Page):
        page_title = html.h1('Delete Locality')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'Locality Delete | New Wine Training',
            )
    
    return LocalityDeleteTemp()

def user_index(request):
    
    class UserIndexPage(Page):
        
        page_title = html.h1('Users')

        instructions = html.p('Click on the user name to view details about that user, as well as any associated data.')
        
        table = Table(
            auto__model = User,
            title = None,
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
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('users:user_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = 'User Index | New Wine Training',
            )
    
    return UserIndexPage()

def user_view(request, user_id):
    
    user = get_object_or_404(User, pk = user_id)

    class UserViewPage(Page):
        
        h1 = html.h1('User View: ' + user)
        
        user_h2 = html.h2('Details')
        dl = html.dl()
        user_id_dt = html.dt('ID')
        user_id_dd = html.dd(user.id)
        user_first_name_dt = html.dt('First Name')
        user_first_name_dd = html.dd(user.first_name)
        user_last_name_dt = html.dt('Last Name')
        user_last_name_dd = html.dd(user.last_name)
        user_chinese_name_dt = html.dt('Chinese Name')
        user_chinese_name_dd = html.dd(user.chinese_name)
        user_gender_dt = html.dt('Gender')
        user_gender_dd = html.dd(user.gender)
        user_locality_dt = html.dt('Locality')
        user_locality_dd = html.dd(user.locality)
        user_district_dt = html.dt('District')
        user_district_dd = html.dd(user.district)
        user_language_dt = html.dt('Primary Language')
        user_language_dd = html.dd(user.language)
        user_phone_number_dt = html.dt('Phone Number')
        user_phone_number_dd = html.dd(user.phone_number)
        user_email_dt = html.dt('Email')
        user_email_dd = html.dd(user.email)
        user_usertypes_dt = html.dt('User Types')
        user_usertypes_dd = html.dd(user.usertypes)
        user_is_staff_dt = html.dt('Is Staff?')
        user_is_staff_dd = html.dd(user.is_staff)
        user_is_superuser_dt = html.dt('Is Superuser?')
        user_is_superuser_dd = html.dd(user.is_superuser)
        user_last_login_dt = html.dt('Last Login')
        user_last_login_dd = html.dd(user.last_login)
        user_groups_dt = html.dt('Groups')
        user_groups_dd = html.dd(user.groups)
        user_user_permissions_dt = html.dt('User Permissions')
        user_user_permissions_dd = html.dd(user.user_permissions)
        user_created_dt = html.dt('Created')
        user_created_dd = html.dd(user.created)
        user_modified_dt = html.dt('Modified')
        user_modified_dd = html.dd(user.modified)
        user_modifier_dt = html.dt('Modifier')
        user_modifier_dd = html.dd(user.modifier)
        
        hr1 = html.hr()
        
        localities_h2 = html.h2('Locality')
        localities = user.locality.all()
        
        localities_table = Table(
            auto__model = Locality,
            rows = localities,
            title = None,
            empty_message = 'No localities',
            columns__locality = Column(
                cell__url = lambda row, **_: reverse('users:locality_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('users:locality_edit', args = (row.pk,)),
            ),
        )
        
        hr2 = html.hr()
        
        languages_h2 = html.h2('Languages')
        languages = user.language.all()
        
        languages_table = Table(
            auto__model = Language,
            rows = languages,
            title = None,
            empty_message = 'No languages',
            columns__language = Column(
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
        
        usertypes_h2 = html.h2('User Types')
        usertypes = user.usertypes.all()
        
        usertypes_table = Table(
            auto__model = UserType,
            rows = usertypes,
            title = None,
            empty_message = 'No user types',
            columns__name = Column(
                cell__url = lambda row, **_: reverse('users:usertype_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('users:usertype_edit', args = (row.pk,)),
            ),
        )
        
        hr4 = html.hr()
        
        groups_h2 = html.h2('Groups')
        groups = user.groups.all()
        
        groups_table = Table(
            auto__model = Group,
            rows = groups,
            title = None,
            empty_message = 'No groups',
        )
        
        hr5 = html.hr()
        
        permissions_h2 = html.h2('User Permissions')
        permissions = user.user_permissions.all()
        
        permissions_table = Table(
            auto__model = Permission,
            rows = permissions,
            title = None,
            empty_message = 'No user-specific permissions',
        )
        
        hr6 = html.hr()
        
        translators_h2 = html.h2('Translator')
        translators = user.translator_users.all()
        
        translators_table = Table(
            auto__model = Translator,
            rows = translators,
            title = None,
            empty_message = 'No translator roles',
            auto__exclude = ['user'],
            columns__language = Column(
                 cell__url = lambda row, **_: reverse('languages:translator_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('languages:translator_edit', args = (row.pk,)),
            ),
        )
        
        hr7 = html.hr()
        
        registrations_h2 = html.h2('Registrations')
        registrations = user.registration_users.all()
        
        registrations_table = Table(
            auto__model = Registration,
            rows = registrations,
            title = None,
            empty_message = 'No registrations',
            auto__exclude = ['user'],
            columns__term = Column(
                cell__url = lambda row, **_: reverse('trainings:registration_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                cell__value = 'Edit',
                cell__url = lambda row, **_: reverse('trainings:registration_edit', args = (row.pk,)),
            ),
        )
        
        hr8 = html.hr()
        
        userexercises_h2 = html.h2('Exercises')
        userexercises = user.userexercise_users.all()
        
        userexercises_table = Table(
            auto__model = UserExercise,
            rows = userexercises,
            title = None,
            empty_message = 'No user exercises',
            auto__exclude = ['user'],
            columns__date = Column(
                cell__url = lambda row, **_: reverse('trainings:userexercise_view', args = (row.pk,))
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
                html_title = 'User View | New Wine Training',
            )
    
    return UserViewPage()

def user_add(request):
    
    return Form.create(
        auto__model = User,
        auto__exclude = ['usertypes', 'is_staff', 'is_superuser', 'last_login', 'groups', 'user_permissions', 'created', 'modified', 'modifier'],
        context__html_title = 'User Create | New Wine Training',
    )

def user_edit(request, user_id):
    
    return Form.edit(
        auto__model = User,
        auto__instance = User.objects.get(id = user_id),
        auto__exclude = ['created', 'modified', 'modifier'],
        context__html_title = 'User Edit | New Wine Training',
    )

def user_delete(request, user_id):
    
    class UserDeleteTemp(Page):
        page_title = html.h1('Delete User')
        additional_spacing = html.p('')
        temp_disabled = html.h3('This function is disabled for now.')
        
        class Meta:
            context = dict(
                html_title = 'User Delete | New Wine Training',
            )
    
    return UserDeleteTemp()