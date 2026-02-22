from django.db import models
from stations.models import PoliceStation

class Officer(models.Model):
    RANK_CHOICES = [
        ('constable', 'Constable'),
        ('head_constable', 'Head Constable'),
        ('si', 'Sub Inspector'),
        ('inspector', 'Inspector'),
        ('dsp', 'Deputy Superintendent'),
        ('sp', 'Superintendent'),
        ('dcp', 'Deputy Commissioner'),
        ('cp', 'Commissioner'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('retired', 'Retired'),
    ]

    name = models.CharField(max_length=100)
    badge_number = models.CharField(max_length=20, unique=True)
    rank = models.CharField(max_length=20, choices=RANK_CHOICES)
    station = models.ForeignKey(PoliceStation, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active')
    joined_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.badge_number} - {self.name}"
