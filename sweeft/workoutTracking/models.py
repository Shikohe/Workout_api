from django.db import models
from workoutUser.models import User
from workoutExercise.models import Exercise


class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    goal = models.CharField(max_length=100, choices=[('Muscle Gain', 'Muscle Gain'), ('Fat Loss', 'Fat Loss'),
                                                     ('Endurance', 'Endurance')])
    frequency = models.PositiveIntegerField(help_text="Number of days per week", default=3)
    sets = models.PositiveIntegerField(default=3)
    reps = models.PositiveIntegerField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    rest_period = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.exercise.name} - {self.user.username}"


class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name="workout_plan")
    completed_at = models.DateTimeField(auto_now_add=True)
    duration_completed = models.PositiveIntegerField(help_text="Total workout duration in minutes", null=True,
                                                     blank=True)
    sets_completed = models.PositiveIntegerField(default=0)
    reps_completed = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Session {self.id} - {self.user.username}"


class FitnessGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=50,
                                 choices=[('Weight Loss', 'Weight Loss'), ('Strength Gain', 'Strength Gain'),
                                          ('Endurance', 'Endurance')])
    target_value = models.DecimalField(max_digits=5, decimal_places=2)
    current_value = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=20, choices=[('kg', 'kg'), ('lbs', 'lbs'), ('reps', 'reps')])
    deadline = models.DateField(null=True, blank=True)
    achieved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.goal_type} - {self.user.username}"


class WorkoutModeSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('in_progress', 'In Progress'), ('completed', 'Completed'),
                                                      ('paused', 'Paused')])

    def __str__(self):
        return f"Live Workout - {self.user.username}"
