from django.shortcuts import render
from .models import Destination

def index(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/index.html', {'destinations': destinations})

def destination_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    return render(request, 'destinations/destination_detail.html', {'destination': destination})
