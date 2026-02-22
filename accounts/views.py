from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from fir.models import FIR
from criminal.models import Criminal
from casefiles.models import CaseFile
from evidence.models import Evidence
from court.models import CourtCase

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role', 'police')
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/login.html', {'signup_error': 'Username already exists'})
        user = User.objects.create_user(username=username, password=password, role=role)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def dashboard_view(request):
    context = {
        'user': request.user,
        'total_firs': FIR.objects.count(),
        'active_cases': CaseFile.objects.exclude(status='closed').count(),
        'total_criminals': Criminal.objects.count(),
        'closed_cases': CaseFile.objects.filter(status='closed').count(),
        'total_evidence': Evidence.objects.count(),
        'total_court': CourtCase.objects.count(),
        'recent_firs': FIR.objects.order_by('-created_at')[:5],
        'recent_cases': CaseFile.objects.order_by('-created_at')[:5],
    }
    return render(request, 'accounts/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
from .models import User
from stations.models import PoliceStation
import random, string

def generate_badge():
    return 'B' + ''.join(random.choices(string.digits, k=5))

