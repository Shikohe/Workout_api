from rest_framework import serializers
from .models import *


class WorkoutPlanSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())

    class Meta:
        model = WorkoutPlan
        fields = "__all__"


class WorkoutSessionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    workout_plan = serializers.PrimaryKeyRelatedField(queryset=WorkoutPlan.objects.all())

    class Meta:
        model = WorkoutSession
        fields = "__all__"


class FitnessGoalSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = WorkoutSession
        fields = "__all__"


class WorkoutModeSessionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    workout_plan = serializers.PrimaryKeyRelatedField(queryset=WorkoutPlan.objects.all())

    class Meta:
        model = WorkoutModeSession
        fields = '__all__'
