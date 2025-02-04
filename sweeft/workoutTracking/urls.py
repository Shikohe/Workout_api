from django.urls import path
from .views import *

urlpatterns = [
    path('workout-plans', WorkoutPlanView.as_view(), name="workout-plans"),
    path('workout-session', WorkoutSessionView.as_view(), name="workout-session"),
    path('fitness-goals', FitnessGoalView.as_view(), name="fitness-goals"),
    path('workout-mode/start', StartWorkoutModeView.as_view(), name='start-workout-mode'),
    path('workout-mode/end/<int:session_id>', EndWorkoutModeView.as_view(), name='end-workout-mode'),
]