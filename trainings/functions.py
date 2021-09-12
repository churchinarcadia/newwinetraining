from django.utils import timezone
from dateutil.relativedelta import relativedelta

from .models import Term, ExerciseType, RecordingLocation, Registration, TrainingMeeting, UserExercise, Text

def current_terms(self, language_id = None):
    conditions = 'start_date < ' + timezone.now() + ', end_date > ' + timezone.now()
    if language_id != None:
        conditions += ', language_id = ' + language_id
            
    return Term.objects.filter(conditions).values_list('id', flat = True)

def current_or_future_terms(self, language_id = None):
    conditions = timezone.now() + ' < start_date < ' + timezone.now() + relativedelta(months = +6)
    if language_id != None:
        conditions += ', language_id = ' + language_id
    
    if len(current_terms(language_id)) > 0:
        return current_terms(language_id)
    else:
        return Term.objects.filter(conditions).values_list('id', flat = True)
    
def last_terms(self, language_id = None):
    conditions = timezone.now() + relativedelta(months = -6) + ' < start-date < ' + timezone.now()
    if language_id != None:
        conditions += ', language_id = ' + language_id
    
    return Term.objects.filter(conditions).values_list('id', flat = True)

