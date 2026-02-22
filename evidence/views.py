from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Evidence
from fir.models import FIR
from casefiles.models import CaseFile
import random, string

def generate_evidence_number():
    return 'EVD' + ''.join(random.choices(string.digits, k=6))

@login_required(login_url='login')
def evidence_list(request):
    evidences = Evidence.objects.all().order_by('-created_at')
    return render(request, 'evidence/evidence_list.html', {'evidences': evidences})

@login_required(login_url='login')
def evidence_add(request):
    firs = FIR.objects.all()
    cases = CaseFile.objects.all()
    if request.method == 'POST':
        Evidence.objects.create(
            evidence_number=generate_evidence_number(),
            title=request.POST.get('title'),
            evidence_type=request.POST.get('evidence_type'),
            fir=FIR.objects.get(id=request.POST.get('fir')) if request.POST.get('fir') else None,
            case=CaseFile.objects.get(id=request.POST.get('case')) if request.POST.get('case') else None,
            description=request.POST.get('description'),
            location_found=request.POST.get('location_found'),
            collected_by=request.user,
            status=request.POST.get('status'),
        )
        messages.success(request, 'Evidence added successfully!')
        return redirect('evidence_list')
    return render(request, 'evidence/evidence_add.html', {'firs': firs, 'cases': cases})

@login_required(login_url='login')
def evidence_detail(request, evidence_id):
    evidence = get_object_or_404(Evidence, id=evidence_id)
    return render(request, 'evidence/evidence_detail.html', {'evidence': evidence})
@login_required(login_url='login')
def evidence_delete(request, evidence_id):
    evidence = get_object_or_404(Evidence, id=evidence_id)
    if request.method == 'POST':
        evidence.delete()
        messages.success(request, 'Evidence deleted successfully!')
        return redirect('evidence_list')
    return render(request, 'evidence/evidence_confirm_delete.html', {'object': evidence, 'type': 'Evidence', 'name': evidence.evidence_number})