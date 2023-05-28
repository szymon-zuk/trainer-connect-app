from django.contrib import admin
from trainerapp.models import Exercise, Training, TrainingPlan, ExerciseTraining

# Register your models here.
admin.site.register(Exercise)
admin.site.register(Training)
admin.site.register(TrainingPlan)
admin.site.register(ExerciseTraining)
