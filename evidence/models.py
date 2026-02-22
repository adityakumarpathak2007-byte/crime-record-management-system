from django.db import models
from accounts.models import User
from fir.models import FIR
from casefiles.models import CaseFile

class Evidence(models.Model):
    TYPE_CHOICES = [
        ('physical', 'Physical'),
        ('digital', 'Digital'),
        ('documentary', 'Documentary'),
        ('forensic', 'Forensic'),
        ('witness', 'Witness Statement'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('collected', 'Collected'),
        ('in_lab', 'In Lab'),
        ('verified', 'Verified'),
        ('submitted', 'Submitted to Court'),
    ]

    evidence_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    evidence_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    fir = models.ForeignKey(FIR, on_delete=models.SET_NULL, null=True, blank=True)
    case = models.ForeignKey(CaseFile, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    location_found = models.CharField(max_length=200, blank=True)
    collected_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='collected')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.evidence_number} - {self.title}"
