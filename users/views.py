from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

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
        dl = html.dl(
            children__usertype_id_dt = html.dt('ID'),
            children__usertype_id_dd = html.dd(usertype.id),
            children__usertype_name_dt = html.dt('Name'),
            children__usertype_name_dd = html.dd(usertype.name),
            children__usertype_description_dt = html.dt('Description'),
            children__usertype_description_dd = html.dd(usertype.description),
            children__usertype_active_dt = html.dt('Active?'),
            children__usertype_active_dd = html.dd(usertype.active),
            children__usertype_created_dt = html.dt('Created'),
            children__usertype_created_dd = html.dd(usertype.created),
            children__usertype_creator_dt = html.dt('Creator'),
            children__usertype_creator_dd = html.dd(usertype.creator),
            children__usertype_modified_dt = html.dt('Modified'),
            children__usertype_modified_dd = html.dd(usertype.modified),
            children__usertype_modifier_dt = html.dt('Modifier'),
            children__usertype_modifier_dd = html.dd(usertype.modifier),
        )
        
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
    
    def add_usertype_save_post_handler(form, **_):
        if not form.is_valid():
            messages.warning(request, 'Adding user type failed. Please check and fix any error messages below, and try again.')
            return

        form.apply(form.instance)
        form.instance.save()
        messages.success(request, 'Successfully saved new user type.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return Form.create(
        auto__model = UserType,
        auto__include = ['name', 'description', 'active'],
        actions__submit__post_handler=add_usertype_save_post_handler,
#        context__html_title = 'User Type Create | New Wine Training',
    )

def usertype_edit(request, usertype_id):
    
    def edit_usertype_save_post_handler(form, **_):
        if not form.is_valid():
            messages.warning(request, 'Editing user type failed. Please check and fix any error messages below, and try again.')
            return

        form.apply(form.instance)
        form.instance.save()
        messages.success(request, 'Successfully saved user type.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return Form.edit(
        auto__model = UserType,
        auto__instance = UserType.objects.get(id = usertype_id),
        auto__include = ['name', 'description', 'active'],
        actions__submit__post_handler=edit_usertype_save_post_handler,
#        context__html_title = 'User Type Edit | New Wine Training',
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
        dl = html.dl(
            children__locality_id_dt = html.dt('ID'),
            children__locality_id_dd = html.dd(locality.id),
            children__locality_locality_dt = html.dt('Locality'),
            children__locality_locality_dd = html.dd(locality.locality),
            children__locality_active_dt = html.dt('Active?'),
            children__locality_active_dd = html.dd(locality.active),
            children__locality_created_dt = html.dt('Created'),
            children__locality_created_dd = html.dd(locality.created),
            children__locality_creator_dt = html.dt('Creator'),
            children__locality_creator_dd = html.dd(locality.creator),
            children__locality_modified_dt = html.dt('Modified'),
            children__locality_modified_dd = html.dd(locality.modified),
            children__locality_modifier_dt = html.dt('Modifier'),
            children__locality_modifier_dd = html.dd(locality.modifier),
        )
        
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
    
    def add_locality_save_post_handler(form, **_):
        if not form.is_valid():
            messages.warning(request, 'Adding locality failed. Please check and fix any error messages below, and try again.')
            return

        form.apply(form.instance)
        form.instance.save()
        messages.success(request, 'Successfully saved new locality.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return Form.create(
        auto__model = Locality,
        auto__include = ['locality', 'active'],
        actions__submit__post_handler=add_locality_save_post_handler,
#        context__html_title = 'Locality Create | New Wine Training',
    )

def locality_edit(request, locality_id):
    
    def edit_locality_save_post_handler(form, **_):
        if not form.is_valid():
            messages.warning(request, 'Editing locality failed. Please check and fix any error messages below, and try again.')
            return

        form.apply(form.instance)
        form.instance.save()
        messages.success(request, 'Successfully saved locality.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return Form.edit(
        auto__model = Locality,
        auto__instance = Locality.objects.get(id = locality_id),
        auto__include = ['locality', 'active'],
        actions__submit__post_handler=edit_locality_save_post_handler,
#        context__html_title = 'Locality Edit | New Wine Training',
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
        
        h1 = html.h1('User View: ' + user.__str__())
        
        user_h2 = html.h2('Details')
        dl = html.dl(
            children__user_id_dt = html.dt('ID'),
            children__user_id_dd = html.dd(user.id),
            children__user_first_name_dt = html.dt('First Name'),
            children__user_first_name_dd = html.dd(user.first_name),
            children__user_last_name_dt = html.dt('Last Name'),
            children__user_last_name_dd = html.dd(user.last_name),
            children__user_chinese_name_dt = html.dt('Chinese Name'),
            children__user_chinese_name_dd = html.dd(user.chinese_name),
            children__user_gender_dt = html.dt('Gender'),
            children__user_gender_dd = html.dd(user.gender),
            children__user_locality_dt = html.dt('Locality'),
            children__user_locality_dd = html.dd(user.locality),
            children__user_district_dt = html.dt('District'),
            children__user_district_dd = html.dd(user.district),
            children__user_language_dt = html.dt('Primary Language'),
            children__user_language_dd = html.dd(user.language),
            children__user_phone_number_dt = html.dt('Phone Number'),
            children__user_phone_number_dd = html.dd(user.phone_number),
            children__user_email_dt = html.dt('Email'),
            children__user_email_dd = html.dd(user.email),
            children__user_usertypes_dt = html.dt('User Types'),
            children__user_usertypes_dd = html.dd(', '.join(list(user.usertypes.values_list('name', flat = True)))),
            children__user_is_staff_dt = html.dt('Is Staff?'),
            children__user_is_staff_dd = html.dd(user.is_staff),
            children__user_is_superuser_dt = html.dt('Is Superuser?'),
            children__user_is_superuser_dd = html.dd(user.is_superuser),
            children__user_last_login_dt = html.dt('Last Login'),
            children__user_last_login_dd = html.dd(user.last_login),
            children__user_groups_dt = html.dt('Groups'),
            children__user_groups_dd = html.dd(', '.join(list(user.groups.values_list('name', flat = True)))),
            children__user_user_permissions_dt = html.dt('User Permissions'),
            children__user_user_permissions_dd = html.dd(', '.join(list(user.user_permissions.values_list('name')))), #TODO
            children__user_created_dt = html.dt('Created'),
            children__user_created_dd = html.dd(user.created),
            children__user_modified_dt = html.dt('Modified'),
            children__user_modified_dd = html.dd(user.modified),
            children__user_modifier_dt = html.dt('Modifier'),
            children__user_modifier_dd = html.dd(user.modifier),
        )
        
        hr1 = html.hr()
        
        localities_h2 = html.h2('Locality')
        localities = Locality.objects.filter(pk = user.locality.id)
        
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
        languages = Language.objects.filter(pk = user.language.id)
        
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
    
    def add_user_save_post_handler(form, **_):
        if not form.is_valid():
            messages.warning(request, 'Adding user failed. Please check and fix any error messages below, and try again.')
            return

        form.apply(form.instance)
        form.instance.save()
        messages.success(request, 'Successfully saved new user.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return Form.create(
        auto__model = User,
        auto__exclude = ['usertypes', 'is_staff', 'is_superuser', 'last_login', 'groups', 'user_permissions', 'created', 'modified', 'modifier'],
        actions__submit__post_handler=add_user_save_post_handler,
#        context__html_title = 'User Create | New Wine Training',

    )

def user_edit(request, user_id):
    
    def edit_user_save_post_handler(form, **_):
        if not form.is_valid():
            messages.warning(request, 'Editing user failed. Please check and fix any error messages below, and try again.')
            return

        form.apply(form.instance)
        form.instance.save()
        messages.success(request, 'Successfully saved user.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return Form.edit(
        auto__model = User,
        auto__instance = User.objects.get(id = user_id),
        auto__exclude = ['password', 'last_login', 'created', 'modified', 'modifier'],
        actions__submit__post_handler=edit_user_save_post_handler,
#        context__html_title = 'User Edit | New Wine Training',
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

def user_register(request):
    
    def register_user_save_post_handler(form, **_):
        if not form.is_valid():
            messages.warning(request, 'Failed to create your account. Please check and fix any error messages below, and try again.')
            return

        form.apply(form.instance)
        form.instance.save()
        messages.sucess(request, 'Successfully created your account. Please log in with your email and password to proceed to training registration.')
        return HttpResponseRedirect(reverse('trainings:registration_add'))
    
    class UserRegisterPage(Page):
        
        page_title = html.h1('Register')
        
        registration_form = Form(
            fields = dict(
                login_box = html.div(
                    attrs__class__box=True,
                    children__title = html.h2('Login information'),
                    children__instructions = html.p('Please enter your email and choose a password, then type the password twice. Please double-check your email; we will send you regular announcements and reminders via email, and you will use your email to log in.'),
                    children__email = Field.email(),
                    children__password = Field.password(),
                    children__password_confirmation = Field.password(),
                ),
                name_box = html.div(
                    attrs__class__box = True,
                    children__title = html.h2('Name'),
                    children__name_box_instructions = html.p('Fill in either your first and last name in English, or your Chinese name.'),
                    children__first_name = Field.text(),
                    children__last_name = Field.text(),
                    children__chinese_name = Field(),
                ),
                personal_box = html.div(
                    attrs__class__box = True,
                    children__title = html.h2('Personal Information'),
                    children__instructions = html.p('Please fill in the following information completely. All fields are required.'),
                    children__gender = Field(),
                    children__locality = Field(),
                    children__district = Field(),
                    children__language = Field(),
                    children__phone_number = Field(
                        help_text = 'Please fill in your cell phone number. We will send you text message announcements and reminders.'
                    ),
                ),
            ),
            actions__submit__post_handler=register_user_save_post_handler,
        )
                
        class Meta:
            context = dict(
                html_title = 'Register | New Wine Training',
            )
            
    
    return UserRegisterPage()

def user_login(request):
    
    class LoginForm(Form):
        
        title = 'Log in'
        
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
                html_title = 'Login | New Wine Training',
            )
    
    return Form(
        title = "Log in",
        context__html_title = 'User Edit | New Wine Training',
        
    )

def user_logout(request):
    
    logout(request)
    
    class UserLogoutPage(Page):
        
        confirmation = html.p('You have been successfully logged out.' +  html.url(reverse('users:user_login'), 'Click here to log in.'))
        
        class Meta:
            context = dict(
                html_title = 'Logout | New Wine Training',
            )
    
    return UserLogoutPage()