from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Criminal

@login_required(login_url='login')
def criminal_list(request):
    criminals = Criminal.objects.all().order_by('-created_at')
    return render(request, 'criminal/criminal_list.html', {'criminals': criminals})

@login_required(login_url='login')
def criminal_add(request):
    if request.method == 'POST':
        Criminal.objects.create(
            name=request.POST.get('name'),
            alias=request.POST.get('alias'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            nationality=request.POST.get('nationality', 'Indian'),
            address=request.POST.get('address'),
            status=request.POST.get('status'),
            description=request.POST.get('description'),
            photo=request.FILES.get('photo'),
        )
        messages.success(request, 'Criminal profile added successfully!')
        return redirect('criminal_list')
    return render(request, 'criminal/criminal_add.html')

@login_required(login_url='login')
def criminal_detail(request, criminal_id):
    criminal = get_object_or_404(Criminal, id=criminal_id)
    return render(request, 'criminal/criminal_detail.html', {'criminal': criminal})
@login_required(login_url='login')
def criminal_delete(request, criminal_id):
    criminal = get_object_or_404(Criminal, id=criminal_id)
    if request.method == 'POST':
        criminal.delete()
        messages.success(request, 'Criminal record deleted successfully!')
        return redirect('criminal_list')
    return render(request, 'criminal/criminal_confirm_delete.html', {'object': criminal, 'type': 'Criminal', 'name': criminal.name})