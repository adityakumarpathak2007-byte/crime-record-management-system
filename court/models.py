from django.db import models
from casefiles.models import CaseFile
from criminal.models import Criminal

class CourtCase(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('ongoing', 'Ongoing'),
        ('adjourned', 'Adjourned'),
        ('verdict_given', 'Verdict Given'),
        ('closed', 'Closed'),
    ]
    VERDICT_CHOICES = [
        ('pending', 'Pending'),
        ('guilty', 'Guilty'),
        ('not_guilty', 'Not Guilty'),
        ('dismissed', 'Dismissed'),
    ]

    court_case_number = models.CharField(max_length=20, unique=True)
    case_file = models.ForeignKey(CaseFile, on_delete=models.SET_NULL, null=True)
    criminal = models.ForeignKey(Criminal, on_delete=models.SET_NULL, null=True, blank=True)
    court_name = models.CharField(max_length=200)
    judge_name = models.CharField(max_length=100, blank=True)
    hearing_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    verdict = models.CharField(max_length=20, choices=VERDICT_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.court_case_number} - {self.court_name}"