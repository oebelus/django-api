from django.shortcuts import render, get_object_or_404
from .models import Prescription

def prescription_detail(request, id):
    prescription = get_object_or_404(Prescription, id=id)
    return render(request, 'prescription_detail.html', {'prescription': prescription})