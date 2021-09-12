from django.http.response import Http404

from .models import Language, Translator, Translation

def language_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def language_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Translator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def language_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def language_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def language_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def translation_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Translator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def translation_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Translator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def translation_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Translator', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def translation_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Translator', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def translation_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Translator', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def translator_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Translator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def translator_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Translator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def language_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def language_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def language_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def translation_table_rows(request, language_id):
    """
    Returns the arguments to be included in filter() or 404 error if not allowed
    """
    
    base_roles = ['Translator']
    admin_roles = ['Staff', 'Superuser']
    
    if request.user.has_role(admin_roles):
        if language_id is None:
            return ''
        elif language_id in list(Language.objects.values_list('id', flat = True)):
            return 'language_id = ' + language_id
        else :
            #TODO add logging and message
            raise Http404
    elif request.user.has_role(base_roles):
        translator_language = request.user.translator_users.language_id
        if translator_language == language_id or language_id is None:
            return 'language_id = ' + language_id
        else:
            #TODO add logging and message
            raise Http404

