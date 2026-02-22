from django.db import models
from accounts.models import User

class CrimeType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Victim(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'), ('female', 'Female'), ('other', 'Other')
    ])
    contact = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class FIR(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('under_investigation', 'Under Investigation'),
        ('closed', 'Closed'),
    ]

    fir_number = models.CharField(max_length=20, unique=True)
    crime_type = models.ForeignKey(CrimeType, on_delete=models.SET_NULL, null=True)
    date_of_crime = models.DateField()
    time_of_crime = models.TimeField()
    location = models.TextField()
    description = models.TextField()
    victim = models.ForeignKey(Victim, on_delete=models.SET_NULL, null=True)
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FIR-{self.fir_number}"