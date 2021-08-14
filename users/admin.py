from django.contrib import admin

from django import forms
#from django import django.utils.translation
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

# Register your models here.

from users.models import User, UserType, Locality

class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Password Again', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_password2(self):
        #Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
        
    def save(self, commit = True):
        #Save the provided password in hashed format
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):

    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled pasword hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'chinese_name',
            'gender',
            'language',
            'locality',
            'district',
            'phone_number',
            'email',
            'usertypes',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    ordering = ('last_name', 'first_name',)

    list_display = (
        'first_name',
        'last_name',
        'locality',
        'district',
        'is_staff',
        'is_superuser',
    )
    list_filter = ('is_staff', 'is_superuser',)
    fieldsets = (
        ('Personal Info', {
            'fields': (
                'first_name',
                'last_name',
                'chinese_name',
                'gender',
                'language',
                'locality',
                'district',
                'phone_number',
                'email',
        )}),
        (None, {
            'fields': (
                'usertypes',
                'groups',
                'user_permissions',
                'is_staff',
                'is_superuser',
        )}),
    )

admin.site.register(User,UserAdmin)
#admin.site.register(Group)
admin.site.register(Permission)
admin.site.register(UserType)
admin.site.register(Locality)