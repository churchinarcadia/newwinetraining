from django.http.response import Http404

from .models import Locality, User, UserType
from django.contrib.auth.models import Group, Permission

from languages.functions import langauge_choice_initial, language_choice_initial

def group_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def group_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def group_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def group_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def group_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def usertype_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def usertype_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def usertype_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def usertype_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def usertype_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def locality_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def locality_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def locality_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def locality_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def locality_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def user_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def user_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    return True

def user_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    return True
    
def user_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    return True

def user_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def user_choices(request):
    
    if request.user.has_role(['Staff', 'Superuser']):
        return User.objects.all()
    elif request.user.has_role(['Training Adminstrator']):
        return User.objects.filter(language_id = language_choice_initial())
    elif request.user.has_role(['Church Responsible']):
        return User.objects.filter(locality = request.user.locality_id)
    elif request.user.has_role(['District Responsible']):
        return User.objects.filter(locality = request.user.locality_id, district = request.user.district)
    elif request.user.has_role(['Trainee']):
        return request.user
    else:
        return ''

def group_choices(request):
    if request.user.has_role(['Staff', 'Superuser', 'Training Adminstrator']):
        return Group.objects.all()
    elif request.user.has_role(['Church Responsible']):
        return Group.objects.filter(name__in = ['Church Responsible', 'District Responsible', 'Trainee'])
    elif request.user.has_role(['District Responsible']):
        return User.objects.filter(name__in = ['District Responsible', 'Trainee'])
    elif request.user.has_role(['Trainee']):
        return User.objects.filter(name__exact = 'Trainee')
    else:
        return ''

#TODO user index table filtering based on role
#TODO user edit perm based on id of user edited and user role
