from django.contrib import admin

# Register your models here.

from .models import Term, ExerciseType, RecordingLocation, Registration, Text, TrainingMeeting, UserExercise

admin.site.register(Term)
admin.site.register(ExerciseType)
admin.site.register(RecordingLocation)
admin.site.register(Registration)
admin.site.register(Text)
admin.site.register(TrainingMeeting)
admin.site.register(UserExercise)