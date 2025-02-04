from django.urls import path
from .views import *

urlpatterns = [
    path('exercises', ExerciseView.as_view(), name="exercises"),
    path('muscles', MuscleView.as_view(), name="muscles"),
]