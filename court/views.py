from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CourtCase
from casefiles.models import CaseFile
from criminal.models import Criminal
import random, string

def generate_court_number():
    return 'CRT' + ''.join(random.choices(string.digits, k=6))

@login_required(login_url='login')
def court_list(request):
    court_cases = CourtCase.objects.all().order_by('-created_at')
    return render(request, 'court/court_list.html', {'court_cases': court_cases})

@login_required(login_url='login')
def court_add(request):
    case_files = CaseFile.objects.all()
    criminals = Criminal.objects.all()
    if request.method == 'POST':
        CourtCase.objects.create(
            court_case_number=generate_court_number(),
            case_file=CaseFile.objects.get(id=request.POST.get('case_file')) if request.POST.get('case_file') else None,
            criminal=Criminal.objects.get(id=request.POST.get('criminal')) if request.POST.get('criminal') else None,
            court_name=request.POST.get('court_name'),
            judge_name=request.POST.get('judge_name'),
            hearing_date=request.POST.get('hearing_date'),
            status=request.POST.get('status'),
            verdict=request.POST.get('verdict'),
            notes=request.POST.get('notes'),
        )
        messages.success(request, 'Court case added successfully!')
        return redirect('court_list')
    return render(request, 'court/court_add.html', {
        'case_files': case_files, 'criminals': criminals
    })

@login_required(login_url='login')
def court_detail(request, court_id):
    court_case = get_object_or_404(CourtCase, id=court_id)
    return render(request, 'court/court_detail.html', {'court_case': court_case})
@login_required(login_url='login')
def court_delete(request, court_id):
    court_case = get_object_or_404(CourtCase, id=court_id)
    if request.method == 'POST':
        court_case.delete()
        messages.success(request, 'Court case deleted successfully!')
        return redirect('court_list')
    return render(request, 'court/court_confirm_delete.html', {'object': court_case, 'type': 'Court Case', 'name': court_case.court_case_number})
