from django.utils import timezone
import datetime
from dateutil.relativedelta import relativedelta

from .models import Term, ExerciseType, RecordingLocation, Registration, TrainingMeeting, UserExercise, Text

def term_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def term_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def term_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def term_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def term_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def exercisetype_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def exercisetype_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def exercisetype_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def exercisetype_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def exercisetype_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def recordinglocation_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def recordinglocation_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def recordinglocation_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def recordinglocation_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def recordinglocation_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def registration_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def registration_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def registration_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    return True
    
def registration_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    #TODO account for entry being edited compared to role
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def registration_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def trainingmeeting_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def trainingmeeting_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator','Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def trainingmeeting_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator','Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def trainingmeeting_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator','Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def trainingmeeting_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Training Adminstrator','Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def userexercise_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def userexercise_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Trainer', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def userexercise_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def userexercise_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def userexercise_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Trainee', 'District Responsible', 'Church Responsible', 'Training Adminstrator', 'Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def text_index_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def text_view_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Staff', 'Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def text_add_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False
    
def text_edit_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def text_delete_perm(request):
    """
    Analyzes if the user has one of the required roles to see this view. Returns boolean.
    """
    
    allowed_roles = ['Superuser']
    if request.user.has_role(allowed_roles) == True:
        return True
    else:
        #TODO add logging
        return False

def current_terms(language_id = None):
    conditions = 'start_date < ' + timezone.now() + ', end_date > ' + timezone.now()
    if language_id != None:
        conditions += ', language_id = ' + language_id
            
    return Term.objects.filter(conditions).values_list('id', flat = True)

def current_or_future_terms(language_id = None):
    conditions = timezone.now() + ' < start_date < ' + timezone.now() + relativedelta(months = +6)
    if language_id != None:
        conditions += ', language_id = ' + language_id
    
    if len(current_terms(language_id)) > 0:
        return current_terms(language_id)
    else:
        return Term.objects.filter(conditions).values_list('id', flat = True)
    
def last_terms(language_id = None):
    conditions = timezone.now() + relativedelta(months = -6) + ' < start-date < ' + timezone.now()
    if language_id != None:
        conditions += ', language_id = ' + language_id
    
    return Term.objects.filter(conditions).values_list('id', flat = True)

def userexercise_today():
    if timezone.now().time() < datetime.time(2,0):
        return timezone.now().date() + relativedelta(days = -1)
    else:
        return timezone.now().date()

def trainingmeeting_term(trainingmeeting_id):
    trainingmeeting = TrainingMeeting.objects.get(pk = trainingmeeting_id)
    return Term.objects.get(language_id = trainingmeeting.language_id, start_date__lte = trainingmeeting.date, end_date__gte = trainingmeeting.date)

def term_trainingmeetings(term_id):
    term = Term.objects.get(pk = term_id)
    return TrainingMeeting.objects.filter(language_id = term.language_id, date__gte = term.start_date, date__lte = term.end_date)