from django.shortcuts import render
from .models import *

# Create your views here.
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})