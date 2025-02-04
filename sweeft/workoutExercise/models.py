from django.db import models


class Exercise(models.Model):
    name = models.CharField("Name", max_length=50, unique=True)
    description = models.TextField()
    instruction = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"


class Muscle(models.Model):
    muscle = models.CharField("Name", max_length=50)
    exercise = models.ForeignKey(Exercise, related_name="muscles", on_delete=models.CASCADE)

    def __str__(self):
        return self.muscle

    class Meta:
        verbose_name = "Muscle"
        verbose_name_plural = "Muscles"
