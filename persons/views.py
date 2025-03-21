from django.shortcuts import render, get_object_or_404
from .models import Person

def person_list(request):
    persons = Person.objects.filter(user=request.user)
    return render(request, 'persons/person_list.html', {'persons': persons})

def person_detail(request, id):
    person = get_object_or_404(Person, id=id)
    return render(request, 'persons/person_detail.html', {'person': person})