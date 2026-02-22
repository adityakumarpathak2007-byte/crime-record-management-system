from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FIR, CrimeType, Victim
import random, string

def generate_fir_number():
    chars = string.digits
    return 'FIR' + ''.join(random.choices(chars, k=6))

@login_required(login_url='login')
def fir_list(request):
    firs = FIR.objects.all().order_by('-created_at')
    return render(request, 'fir/fir_list.html', {'firs': firs})

@login_required(login_url='login')
def fir_register(request):
    crime_types = CrimeType.objects.all()
    if request.method == 'POST':
        # Create victim first
        victim = Victim.objects.create(
            name=request.POST.get('victim_name'),
            age=request.POST.get('victim_age'),
            gender=request.POST.get('victim_gender'),
            contact=request.POST.get('victim_contact'),
            address=request.POST.get('victim_address'),
        )
        # Create FIR
        FIR.objects.create(
            fir_number=generate_fir_number(),
            crime_type=CrimeType.objects.get(id=request.POST.get('crime_type')),
            date_of_crime=request.POST.get('date_of_crime'),
            time_of_crime=request.POST.get('time_of_crime'),
            location=request.POST.get('location'),
            description=request.POST.get('description'),
            victim=victim,
            registered_by=request.user,
            status='open',
        )
        messages.success(request, 'FIR registered successfully!')
        return redirect('fir_list')
    return render(request, 'fir/fir_register.html', {'crime_types': crime_types})

@login_required(login_url='login')
def fir_detail(request, fir_id):
    fir = get_object_or_404(FIR, id=fir_id)
    return render(request, 'fir/fir_detail.html', {'fir': fir})
@login_required(login_url='login')
def fir_update_status(request, fir_id):
    fir = get_object_or_404(FIR, id=fir_id)
    if request.method == 'POST':
        fir.status = request.POST.get('status')
        fir.save()
        messages.success(request, f'FIR {fir.fir_number} status updated successfully!')
    return redirect('fir_detail', fir_id=fir_id)
@login_required(login_url='login')
def fir_delete(request, fir_id):
    fir = get_object_or_404(FIR, id=fir_id)
    if request.method == 'POST':
        fir.delete()
        messages.success(request, 'FIR deleted successfully!')
        return redirect('fir_list')
    return render(request, 'fir/fir_confirm_delete.html', {'object': fir, 'type': 'FIR', 'name': fir.fir_number})