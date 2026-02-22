from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Officer
from stations.models import PoliceStation
import random, string

def generate_badge():
    return 'B' + ''.join(random.choices(string.digits, k=5))

@login_required(login_url='login')
def officer_list(request):
    officers = Officer.objects.all().order_by('name')
    return render(request, 'officers/officer_list.html', {'officers': officers})

@login_required(login_url='login')
def officer_add(request):
    stations = PoliceStation.objects.all()
    if request.method == 'POST':
        Officer.objects.create(
            name=request.POST.get('name'),
            badge_number=generate_badge(),
            rank=request.POST.get('rank'),
            station=PoliceStation.objects.get(id=request.POST.get('station')) if request.POST.get('station') else None,
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            status=request.POST.get('status'),
            joined_date=request.POST.get('joined_date'),
        )
        messages.success(request, 'Officer added successfully!')
        return redirect('officer_list')
    return render(request, 'officers/officer_add.html', {'stations': stations})

@login_required(login_url='login')
def officer_detail(request, officer_id):
    officer = get_object_or_404(Officer, id=officer_id)
    return render(request, 'officers/officer_detail.html', {'officer': officer})

@login_required(login_url='login')
def officer_delete(request, officer_id):
    officer = get_object_or_404(Officer, id=officer_id)
    if request.method == 'POST':
        officer.delete()
        messages.success(request, 'Officer deleted successfully!')
        return redirect('officer_list')
    return render(request, 'officers/officer_confirm_delete.html', {'name': officer.name})