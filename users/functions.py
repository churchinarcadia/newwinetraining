from django.http.response import Http404

from .models import Locality, User, UserType
from django.contrib.auth.models import Group, Permission

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






#TODO function to generate list of possible users as choice based on role
#TODO function to generate list of group choices based on role