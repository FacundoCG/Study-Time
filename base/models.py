from django.db import models

# Create your models here.

class Study(models.Model):
    date = models.DateField()
    formal_study_hours = models.DurationField()
    informal_study_hours = models.DurationField()

    def __str__(self):
        return str(self.date)