from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fir.models import FIR
from criminal.models import Criminal
from casefiles.models import CaseFile
from evidence.models import Evidence
from court.models import CourtCase

@login_required(login_url='login')
def reports_view(request):
    context = {
        # FIR stats
        'total_firs': FIR.objects.count(),
        'fir_open': FIR.objects.filter(status='open').count(),
        'fir_under_investigation': FIR.objects.filter(status='under_investigation').count(),
        'fir_closed': FIR.objects.filter(status='closed').count(),

        # Case stats
        'total_cases': CaseFile.objects.count(),
        'cases_open': CaseFile.objects.filter(status='open').count(),
        'cases_under_investigation': CaseFile.objects.filter(status='under_investigation').count(),
        'cases_closed': CaseFile.objects.filter(status='closed').count(),
        'cases_dismissed': CaseFile.objects.filter(status='dismissed').count(),

        # Criminal stats
        'total_criminals': Criminal.objects.count(),
        'criminals_wanted': Criminal.objects.filter(status='wanted').count(),
        'criminals_arrested': Criminal.objects.filter(status='arrested').count(),
        'criminals_convicted': Criminal.objects.filter(status='convicted').count(),
        'criminals_released': Criminal.objects.filter(status='released').count(),

        # Evidence stats
        'total_evidence': Evidence.objects.count(),
        'evidence_collected': Evidence.objects.filter(status='collected').count(),
        'evidence_in_lab': Evidence.objects.filter(status='in_lab').count(),
        'evidence_verified': Evidence.objects.filter(status='verified').count(),
        'evidence_submitted': Evidence.objects.filter(status='submitted').count(),

        # Court stats
        'total_court': CourtCase.objects.count(),
        'verdict_guilty': CourtCase.objects.filter(verdict='guilty').count(),
        'verdict_not_guilty': CourtCase.objects.filter(verdict='not_guilty').count(),
        'verdict_pending': CourtCase.objects.filter(verdict='pending').count(),

        # Recent data
        'recent_firs': FIR.objects.order_by('-created_at')[:5],
        'recent_criminals': Criminal.objects.order_by('-created_at')[:5],
    }
    return render(request, 'reports/reports.html', context)