from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PoliceStation
import random, string

def generate_station_code():
    return 'PS' + ''.join(random.choices(string.digits, k=4))

@login_required(login_url='login')
def station_list(request):
    stations = PoliceStation.objects.all().order_by('name')
    return render(request, 'stations/station_list.html', {'stations': stations})

@login_required(login_url='login')
def station_add(request):
    if request.method == 'POST':
        PoliceStation.objects.create(
            name=request.POST.get('name'),
            station_code=generate_station_code(),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            in_charge=request.POST.get('in_charge'),
        )
        messages.success(request, 'Police station added successfully!')
        return redirect('station_list')
    return render(request, 'stations/station_add.html')

@login_required(login_url='login')
def station_detail(request, station_id):
    station = get_object_or_404(PoliceStation, id=station_id)
    return render(request, 'stations/station_detail.html', {'station': station})

@login_required(login_url='login')
def station_delete(request, station_id):
    station = get_object_or_404(PoliceStation, id=station_id)
    if request.method == 'POST':
        station.delete()
        messages.success(request, 'Police station deleted successfully!')
        return redirect('station_list')
    return render(request, 'stations/station_confirm_delete.html', {'object': station, 'name': station.name})