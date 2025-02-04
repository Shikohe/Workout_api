from rest_framework import serializers
from .models import *


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    muscles = MuscleSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = ["id", "name", "description", "muscles", "instruction"]
