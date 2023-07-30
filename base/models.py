from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Study(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    formal_study_hours = models.DurationField()
    informal_study_hours = models.DurationField()

    def __str__(self):
        return str(self.date)
    
    class Meta:
        ordering = ['date']
