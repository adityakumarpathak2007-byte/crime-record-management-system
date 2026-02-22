from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CaseFile
from fir.models import FIR
from criminal.models import Criminal
from accounts.models import User
import random, string

def generate_case_number():
    return 'CASE' + ''.join(random.choices(string.digits, k=6))

@login_required(login_url='login')
def case_list(request):
    cases = CaseFile.objects.all().order_by('-created_at')
    return render(request, 'casefiles/case_list.html', {'cases': cases})

@login_required(login_url='login')
def case_add(request):
    firs = FIR.objects.all()
    criminals = Criminal.objects.all()
    officers = User.objects.all()
    if request.method == 'POST':
        criminal_ids = request.POST.getlist('criminals')
        case = CaseFile.objects.create(
            case_number=generate_case_number(),
            title=request.POST.get('title'),
            fir=FIR.objects.get(id=request.POST.get('fir')) if request.POST.get('fir') else None,
            assigned_officer=User.objects.get(id=request.POST.get('assigned_officer')) if request.POST.get('assigned_officer') else None,
            status=request.POST.get('status'),
            description=request.POST.get('description'),
        )
        if criminal_ids:
            case.criminals.set(criminal_ids)
        messages.success(request, 'Case file created successfully!')
        return redirect('case_list')
    return render(request, 'casefiles/case_add.html', {
        'firs': firs, 'criminals': criminals, 'officers': officers
    })

@login_required(login_url='login')
def case_detail(request, case_id):
    case = get_object_or_404(CaseFile, id=case_id)
    return render(request, 'casefiles/case_detail.html', {'case': case})
@login_required(login_url='login')
def case_update_status(request, case_id):
    case = get_object_or_404(CaseFile, id=case_id)
    if request.method == 'POST':
        case.status = request.POST.get('status')
        case.save()
        messages.success(request, f'Case {case.case_number} status updated successfully!')
    return redirect('case_detail', case_id=case_id)
@login_required(login_url='login')
def case_delete(request, case_id):
    case = get_object_or_404(CaseFile, id=case_id)
    if request.method == 'POST':
        case.delete()
        messages.success(request, 'Case deleted successfully!')
        return redirect('case_list')
    return render(request, 'casefiles/case_confirm_delete.html', {'object': case, 'type': 'Case', 'name': case.case_number})