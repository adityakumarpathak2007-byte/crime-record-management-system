from django.db import models
from accounts.models import User
from fir.models import FIR
from criminal.models import Criminal

class CaseFile(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('under_investigation', 'Under Investigation'),
        ('closed', 'Closed'),
        ('dismissed', 'Dismissed'),
    ]

    case_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    fir = models.ForeignKey(FIR, on_delete=models.SET_NULL, null=True)
    criminals = models.ManyToManyField(Criminal, blank=True)
    assigned_officer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='open')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.case_number} - {self.title}"