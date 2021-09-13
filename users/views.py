from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
#from django.utils import timezone

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.utils.translation import gettext

from django.db.models import Q

from newwinetraining.iommi import Page, Form, Table, Column, Menu, MenuItem

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

from .functions import group_index_perm, group_view_perm, group_add_perm, group_edit_perm, group_delete_perm
from .functions import usertype_index_perm, usertype_view_perm, usertype_add_perm, usertype_edit_perm, usertype_delete_perm
from .functions import locality_index_perm, locality_view_perm, locality_add_perm, locality_edit_perm, locality_delete_perm
from .functions import user_index_perm, user_view_perm, user_add_perm, user_edit_perm, user_delete_perm
#from .functions import 

from languages.functions import language_index_perm, language_edit_perm, translator_index_perm, translator_edit_perm
from trainings.functions import registration_index_perm, registration_edit_perm, userexercise_index_perm, userexercise_edit_perm

# Create your views here.

def group_index(request):
    
    if not group_index_perm():
        raise Http404
    
    class GroupIndexPage(Page):
        
        page_title = html.h1(gettext('Groups'))
        
        instructions = html.p(gettext('Click on the group name to view details about that user type, as well as any associated data.'))
        
        table = Table(
            auto__model = Group,
            title = None,
            columns__name = Column(
                cell__url = lambda row, **_: reverse('users:group_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                include = group_edit_perm,
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('users:group_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Group Index | New Wine Training'),
            )
    
    return GroupIndexPage()

def group_view(request, group_id):
    
    if not group_view_perm():
        raise Http404
    
    group = get_object_or_404(Group, pk = group_id)
    
    class GroupViewPage(Page):
        
        h1 = html.h1(gettext('Group View: ' + group.name))
        
        group_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__group_id_dt = html.dt('ID'),
            children__group_id_dd = html.dd(group.id),
            children__group_name_dt = html.dt(gettext('Name')),
            children__group_name_dd = html.dd(gettext(group.name)),
            children__group_permissions_dt = html.dt(gettext('Permissions')),
            children__group_permissions_dd = html.dd(gettext(', '.join(list(group.permissions.values_list('name', flat = True))))),
        )
        
        if user_index_perm():
        
            hr1 = html.hr()
            
            users_h2 = html.h2(gettext('Users'))
            users = group.user_set.all()
            
            users_table = Table(
                auto__model = User,
                rows = users,
                title = None,
                empty_message = gettext('No users'),
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
                    include = user_edit_perm,
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('users:user_edit', args = (row.pk,)),
                ),
            )
        
        class Meta:
            context = dict(
                html_title = gettext('Group View | New Wine Training'),
            )
    
    return GroupViewPage()

def group_add(request):
    
    if not group_add_perm():
        raise Http404
    
    if request.method != 'POST':
        referer = request.META.get('HTTP_REFERER')
    
    return Form.create(
        auto__model = Group,
        auto__include = ['name', 'description', 'active'],
        extra__redirect_to = referer,
#        context__html_title = 'Group Create | New Wine Training',
    )

def group_edit(request, group_id):
    
    if not group_edit_perm():
        raise Http404
    
    if request.method != 'POST':
        referer = request.META.get('HTTP_REFERER')
    
    return Form.edit(
        auto__model = Group,
        auto__instance = Group.objects.get(id = group_id),
        auto__include = ['name', 'description', 'active'],
        extra__redirect_to = referer,
#        context__html_title = 'Group Edit | New Wine Training',
    )

def group_delete(request, group_id):
    
    if not group_delete_perm():
        raise Http404
    
    class GroupDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Group'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Group Delete | New Wine Training'),
            )
    
    return GroupDeleteTemp()

def usertype_index(request):
    
    if not usertype_index_perm():
        raise Http404
    
    class UserTypeIndexPage(Page):
        
        page_title = html.h1(gettext('User Types'))
        
        instructions = html.p(gettext('Click on the user type name to view details about that user type, as well as any associated data.'))
        
        table = Table(
            auto__model = UserType,
            title = None,
            columns__name = Column(
                cell__url = lambda row, **_: reverse('users:usertype_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                include = usertype_edit_perm,
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('users:usertype_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('User Type Index | New Wine Training'),
            )
    
    return UserTypeIndexPage()

def usertype_view(request, usertype_id):
    
    if not usertype_view_perm():
        raise Http404
    
    usertype = get_object_or_404(UserType, pk = usertype_id)
    
    class UserTypeViewPage(Page):
        
        h1 = html.h1(gettext('User Type View: ' + usertype.name))
        
        usertype_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__usertype_id_dt = html.dt('ID'),
            children__usertype_id_dd = html.dd(usertype.id),
            children__usertype_name_dt = html.dt(gettext('Name')),
            children__usertype_name_dd = html.dd(gettext(usertype.name)),
            children__usertype_description_dt = html.dt(gettext('Description')),
            children__usertype_description_dd = html.dd(gettext(usertype.description)),
            children__usertype_active_dt = html.dt(gettext('Active?')),
            children__usertype_active_dd = html.dd(gettext(str(usertype.active))),
            children__usertype_created_dt = html.dt(gettext('Created')),
            children__usertype_created_dd = html.dd(usertype.created),
            children__usertype_creator_dt = html.dt(gettext('Creator')),
            children__usertype_creator_dd = html.dd(usertype.creator),
            children__usertype_modified_dt = html.dt(gettext('Modified')),
            children__usertype_modified_dd = html.dd(usertype.modified),
            children__usertype_modifier_dt = html.dt(gettext('Modifier')),
            children__usertype_modifier_dd = html.dd(usertype.modifier),
        )
        
        if user_index_perm():
        
            hr1 = html.hr()
            
            users_h2 = html.h2(gettext('Users'))
            users = usertype.user_usertypes.all()
            
            users_table = Table(
                auto__model = User,
                rows = users,
                title = None,
                empty_message = gettext('No users'),
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
                    include = usertype_edit_perm,
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('users:user_edit', args = (row.pk,)),
                ),
            )
        
        class Meta:
            context = dict(
                html_title = gettext('User Type View | New Wine Training'),
            )
    
    return UserTypeViewPage()

def usertype_add(request):
    
    if not usertype_add_perm():
        raise Http404
    
    if request.method != 'POST':
        referer = request.META.get('HTTP_REFERER')
    
    return Form.create(
        auto__model = UserType,
        auto__include = ['name', 'description', 'active'],
        extra__redirect_to = referer,
#        context__html_title = 'User Type Create | New Wine Training',
    )

def usertype_edit(request, usertype_id):
    
    if not usertype_edit_perm():
        raise Http404
    
    if request.method != 'POST':
        referer = request.META.get('HTTP_REFERER')
    
    return Form.edit(
        auto__model = UserType,
        auto__instance = UserType.objects.get(id = usertype_id),
        auto__include = ['name', 'description', 'active'],
        extra__redirect_to = referer,
#        context__html_title = 'User Type Edit | New Wine Training',
    )

def usertype_delete(request, usertype_id):
    
    if not usertype_delete_perm():
        raise Http404
    
    class UserTypeDeleteTemp(Page):
        page_title = html.h1(gettext('Delete User Type'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('User Type Delete | New Wine Training'),
            )
    
    return UserTypeDeleteTemp()

def locality_index(request):
    
    if not locality_index_perm():
        raise Http404
    
    class LocalityIndexPage(Page):
        
        page_title = html.h1(gettext('Localities'))
        
        instructions = html.p(gettext('Click on the locality name to view details about that locality, as well as any associated data.'))
        
        table = Table(
            auto__model = Locality,
            title = None,
            columns__locality = Column(
                cell__url = lambda row, **_: reverse('users:locality_view', args = (row.pk,))
            ),
            columns__edit = Column(
                attr = '',
                display_name = '',
                include = locality_edit_perm,
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('users:locality_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('Locality Index | New Wine Training'),
            )
        
    return LocalityIndexPage()

def locality_view(request, locality_id):
    
    if not locality_view_perm():
        raise Http404
    
    locality = get_object_or_404(Locality, pk = locality_id)

    class LocalityViewPage(Page):
        
        h1 = html.h1(gettext('Locality View: ' + locality.locality))
        
        locality_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__locality_id_dt = html.dt('ID'),
            children__locality_id_dd = html.dd(locality.id),
            children__locality_locality_dt = html.dt(gettext('Locality')),
            children__locality_locality_dd = html.dd(gettext(locality.locality)),
            children__locality_active_dt = html.dt(gettext('Active?')),
            children__locality_active_dd = html.dd(gettext(str(locality.active))),
            children__locality_created_dt = html.dt(gettext('Created')),
            children__locality_created_dd = html.dd(locality.created),
            children__locality_creator_dt = html.dt(gettext('Creator')),
            children__locality_creator_dd = html.dd(locality.creator),
            children__locality_modified_dt = html.dt(gettext('Modified')),
            children__locality_modified_dd = html.dd(locality.modified),
            children__locality_modifier_dt = html.dt(gettext('Modifier')),
            children__locality_modifier_dd = html.dd(locality.modifier),
        )
        
        if user_edit_perm():
        
            hr1 = html.hr()
            
            users_h2 = html.h2(gettext('Users'))
            users = locality.user_localities.all()
            
            users_table = Table(
                auto__model = User,
                rows = users,
                title = None,
                empty_message = gettext('No users'),
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
                    include = user_edit_perm,
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('users:user_edit', args = (row.pk,)),
                ),
            )
        
        class Meta:
            context = dict(
                html_title = gettext('Locality View | New Wine Training'),
            )
            
    return LocalityViewPage()

def locality_add(request):
    
    if not locality_add_perm():
        raise Http404
    
    if request.method != 'POST':
        referer = request.META.get('HTTP_REFERER')
    
    return Form.create(
        auto__model = Locality,
        auto__include = ['locality', 'active'],
        extra__redirect_to = referer,
#        context__html_title = 'Locality Create | New Wine Training',
    )

def locality_edit(request, locality_id):
    
    if not locality_edit_perm():
        raise Http404
    
    if request.method != 'POST':
        referer = request.META.get('HTTP_REFERER')
    
    return Form.edit(
        auto__model = Locality,
        auto__instance = Locality.objects.get(id = locality_id),
        auto__include = ['locality', 'active'],
        extra__redirect_to = referer,
#        context__html_title = 'Locality Edit | New Wine Training',
    )

def locality_delete(request, locality_id):
    
    if not locality_delete_perm():
        raise Http404
    
    class LocalityDeleteTemp(Page):
        page_title = html.h1(gettext('Delete Locality'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('Locality Delete | New Wine Training'),
            )
    
    return LocalityDeleteTemp()

def user_index(request):
    
    if not user_index_perm():
        raise Http404
    
    class UserIndexPage(Page):
        
        page_title = html.h1(gettext('Users'))

        instructions = html.p(gettext('Click on the user name to view details about that user, as well as any associated data.'))
        #TODO auto-filter users based on role
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
                include = user_edit_perm,
                cell__value = gettext('Edit'),
                cell__url = lambda row, **_: reverse('users:user_edit', args = (row.pk,)),
            ),
        )
        
        class Meta:
            context = dict(
                html_title = gettext('User Index | New Wine Training'),
            )
    
    return UserIndexPage()

def user_view(request, user_id):
    
    if not user_view_perm():
        raise Http404
    
    user = get_object_or_404(User, pk = user_id)

    class UserViewPage(Page):
        
        h1 = html.h1(gettext('User View: ') + user.__str__())
        
        user_h2 = html.h2(gettext('Details'))
        dl = html.dl(
            children__user_id_dt = html.dt('ID'),
            children__user_id_dd = html.dd(user.id),
            children__user_first_name_dt = html.dt(gettext('First Name')),
            children__user_first_name_dd = html.dd(user.first_name),
            children__user_last_name_dt = html.dt(gettext('Last Name')),
            children__user_last_name_dd = html.dd(user.last_name),
            children__user_chinese_name_dt = html.dt(gettext('Chinese Name')),
            children__user_chinese_name_dd = html.dd(user.chinese_name),
            children__user_gender_dt = html.dt(gettext('Gender')),
            children__user_gender_dd = html.dd(gettext(user.gender)),
            children__user_locality_dt = html.dt(gettext('Locality')),
            children__user_locality_dd = html.dd(gettext(str(user.locality))),
            children__user_district_dt = html.dt(gettext('District')),
            children__user_district_dd = html.dd(gettext(user.district)),
            children__user_language_dt = html.dt(gettext('Primary Language')),
            children__user_language_dd = html.dd(gettext(str(user.language))),
            children__user_phone_number_dt = html.dt(gettext('Phone Number')),
            children__user_phone_number_dd = html.dd(user.phone_number),
            children__user_email_dt = html.dt(gettext('Email')),
            children__user_email_dd = html.dd(user.email),
            children__user_usertypes_dt = html.dt(gettext('User Types')),
            children__user_usertypes_dd = html.dd(gettext(', '.join(list(user.usertypes.values_list('name', flat = True))))),
            children__user_is_staff_dt = html.dt(gettext('Is Staff?')),
            children__user_is_staff_dd = html.dd(gettext(str(user.is_staff))),
            children__user_is_superuser_dt = html.dt(gettext('Is Superuser?')),
            children__user_is_superuser_dd = html.dd(gettext(str(user.is_superuser))),
            children__user_last_login_dt = html.dt(gettext('Last Login')),
            children__user_last_login_dd = html.dd(user.last_login),
            children__user_groups_dt = html.dt(gettext('Groups')),
            children__user_groups_dd = html.dd(gettext(', '.join(list(user.groups.values_list('name', flat = True))))),
            children__user_user_permissions_dt = html.dt(gettext('User Permissions')),
            children__user_user_permissions_dd = html.dd(gettext(', '.join(list(user.user_permissions.values_list('name'))))),
            children__user_created_dt = html.dt(gettext('Created')),
            children__user_created_dd = html.dd(user.created),
            children__user_modified_dt = html.dt(gettext('Modified')),
            children__user_modified_dd = html.dd(user.modified),
            children__user_modifier_dt = html.dt(gettext('Modifier')),
            children__user_modifier_dd = html.dd(user.modifier),
        )
        
        if locality_index_perm():
        
            hr1 = html.hr()
            
            localities_h2 = html.h2(gettext('Locality'))
            localities = Locality.objects.filter(pk = user.locality.id)
            
            localities_table = Table(
                auto__model = Locality,
                rows = localities,
                title = None,
                empty_message = gettext('No localities'),
                columns__locality = Column(
                    cell__url = lambda row, **_: reverse('users:locality_view', args = (row.pk,))
                ),
                columns__edit = Column(
                    attr = '',
                    display_name = '',
                    include = locality_edit_perm,
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('users:locality_edit', args = (row.pk,)),
                ),
            )
        
        if language_index_perm():
        
            hr2 = html.hr()
            
            languages_h2 = html.h2(gettext('Languages'))
            languages = Language.objects.filter(pk = user.language.id)
            
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
                    include = language_edit_perm,
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('languages:language_edit', args = (row.pk,)),
                ),
            )
        
        if usertype_index_perm():
        
            hr3 = html.hr()
            
            usertypes_h2 = html.h2(gettext('User Types'))
            usertypes = user.usertypes.all()
            
            usertypes_table = Table(
                auto__model = UserType,
                rows = usertypes,
                title = None,
                empty_message = gettext('No user types'),
                columns__name = Column(
                    cell__url = lambda row, **_: reverse('users:usertype_view', args = (row.pk,))
                ),
                columns__edit = Column(
                    attr = '',
                    display_name = '',
                    include = usertype_edit_perm,
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('users:usertype_edit', args = (row.pk,)),
                ),
            )
        
        if group_index_perm():
        
            hr4 = html.hr()
            
            groups_h2 = html.h2(gettext('Groups'))
            groups = user.groups.all()
            
            groups_table = Table(
                auto__model = Group,
                rows = groups,
                title = None,
                empty_message = gettext('No groups'),
            )
        
        hr5 = html.hr()
        
        permissions_h2 = html.h2(gettext('User Permissions'))
        permissions = user.user_permissions.all()
        
        permissions_table = Table(
            auto__model = Permission,
            rows = permissions,
            title = None,
            empty_message = gettext('No user-specific permissions'),
        )
        
        if translator_index_perm():
        
            hr6 = html.hr()
            
            translators_h2 = html.h2(gettext('Translator'))
            translators = user.translator_users.all()
            
            translators_table = Table(
                auto__model = Translator,
                rows = translators,
                title = None,
                empty_message = gettext('No translator roles'),
                auto__exclude = ['user'],
                columns__language = Column(
                    cell__url = lambda row, **_: reverse('languages:translator_view', args = (row.pk,))
                ),
                columns__edit = Column(
                    attr = '',
                    display_name = '',
                    include = translator_edit_perm,
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('languages:translator_edit', args = (row.pk,)),
                ),
            )
        
        if registration_index_perm():
        
            hr7 = html.hr()
            
            registrations_h2 = html.h2(gettext('Registrations'))
            registrations = user.registration_users.all()
            
            registrations_table = Table(
                auto__model = Registration,
                rows = registrations,
                title = None,
                empty_message = gettext('No registrations'),
                auto__exclude = ['user'],
                columns__term = Column(
                    cell__url = lambda row, **_: reverse('trainings:registration_view', args = (row.pk,))
                ),
                columns__edit = Column(
                    attr = '',
                    display_name = '',
                    include = registration_edit_perm,
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('trainings:registration_edit', args = (row.pk,)),
                ),
            )
        
        if userexercise_index_perm():
        
            hr8 = html.hr()
            
            userexercises_h2 = html.h2(gettext('Exercises'))
            userexercises = user.userexercise_users.all()
            
            userexercises_table = Table(
                auto__model = UserExercise,
                rows = userexercises,
                title = None,
                empty_message = gettext('No user exercises'),
                auto__exclude = ['user'],
                columns__date = Column(
                    cell__url = lambda row, **_: reverse('trainings:userexercise_view', args = (row.pk,))
                ),
                columns__edit = Column(
                    attr = '',
                    display_name = '',
                    include = userexercise_edit_perm,
                    cell__value = gettext('Edit'),
                    cell__url = lambda row, **_: reverse('trainings:userexercise_edit', args = (row.pk,)),
                ),
            )
        
        class Meta:
            context = dict(
                html_title = gettext('User View | New Wine Training'),
            )
    
    return UserViewPage()

def user_add(request):
    
    if not user_add_perm():
        raise Http404
    
    if request.method != 'POST':
        referer = request.META.get('HTTP_REFERER')
    
    return Form.create(
        auto__model = User,
        auto__exclude = ['usertypes', 'is_staff', 'is_superuser', 'last_login', 'groups', 'user_permissions', 'created', 'modified', 'modifier'],
        extra__redirect_to = referer,
#        context__html_title = 'User Create | New Wine Training',

    )

def user_edit(request, user_id):
    
    if not user_edit_perm():
        raise Http404
    
    if request.method != 'POST':
        referer = request.META.get('HTTP_REFERER')
    
    return Form.edit(
        auto__model = User,
        auto__instance = User.objects.get(id = user_id),
        auto__exclude = ['password', 'last_login', 'created', 'modified', 'modifier'],
        extra__redirect_to = referer,
#        context__html_title = 'User Edit | New Wine Training',
    )

def user_delete(request, user_id):
    
    if not user_delete_perm():
        raise Http404
    
    class UserDeleteTemp(Page):
        page_title = html.h1(gettext('Delete User'))
        additional_spacing = html.p('')
        temp_disabled = html.h3(gettext('This function is disabled for now.'))
        
        class Meta:
            context = dict(
                html_title = gettext('User Delete | New Wine Training'),
            )
    
    return UserDeleteTemp()

def user_register(request):
    
    def register_user_save_post_handler(form, **_):
        if not form.is_valid():
            messages.warning(request, gettext('Failed to create your account. Please check and fix any error messages below, and try again.'))
            return

        form.apply(form.instance)
        form.instance.save()
        messages.sucess(request, gettext('Successfully created your account. Please log in with your email and password to proceed to training registration.'))
        return HttpResponseRedirect(reverse('trainings:registration_add'))
    
    class UserRegisterPage(Page):
        
        page_title = html.h1(gettext('Register'))
        
        registration_form = Form(
            fields = dict(
                login_box = html.div(
                    attrs__class__box=True,
                    children__title = html.h2(gettext('Login information')),
                    children__instructions = html.p(gettext('Please enter your email and choose a password, then type the password twice. Please double-check your email; we will send you regular announcements and reminders via email, and you will use your email to log in.')),
                    children__email = Field.email(),
                    children__password = Field.password(),
                    children__password_confirmation = Field.password(),
                ),
                name_box = html.div(
                    attrs__class__box = True,
                    children__title = html.h2(gettext('Name')),
                    children__name_box_instructions = html.p(gettext('Fill in either your first and last name in English, or your Chinese name.')),
                    children__first_name = Field.text(),
                    children__last_name = Field.text(),
                    children__chinese_name = Field(),
                ),
                personal_box = html.div(
                    attrs__class__box = True,
                    children__title = html.h2(gettext('Personal Information')),
                    children__instructions = html.p(gettext('Please fill in the following information completely. All fields are required.')),
                    children__gender = Field(),
                    children__locality = Field(),
                    children__district = Field(),
                    children__language = Field(),
                    children__phone_number = Field(
                        help_text = gettext('Please fill in your cell phone number. We will send you text message announcements and reminders.')
                    ),
                ),
            ),
            actions__submit__post_handler=register_user_save_post_handler,
        )
                
        class Meta:
            context = dict(
                html_title = gettext('Register | New Wine Training'),
            )
            
    
    return UserRegisterPage()

def user_login(request):
    
    class LoginForm(Form):
        
        title = gettext('Log in')
        
        email = Field.email()
        password = Field.password()
        
        def post_handler(form, **_):
            if not form.is_valid():
                return
            
            user = authenticate(request, form.email, form.password)
            
            if user is not None:
                login(request, user)
            
#            else:
#                ThrowError()
                    
        class Meta:
            context = dict(
                html_title = gettext('Login | New Wine Training'),
            )
    
    return Form(
        title = gettext('Log in'),
        context__html_title = gettext('User Edit | New Wine Training'),
        
    )

def user_logout(request):
    
    logout(request)
    
    class UserLogoutPage(Page):
        
        confirmation = html.p(gettext('You have been successfully logged out.' +  html.url(reverse('users:user_login'), 'Click here to log in.')))
        
        class Meta:
            context = dict(
                html_title = gettext('Logout | New Wine Training'),
            )
    
    return UserLogoutPage()