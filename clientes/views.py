from django.shortcuts import render, redirect
from .models import *
from .forms import PersonForm

# Create your views here.
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

def persons_new(request):
    form = PersonForm(request.POST, request.FILES, None)

    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'form': form})