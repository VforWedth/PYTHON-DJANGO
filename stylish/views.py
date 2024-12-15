from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    
    card1 = Destination()
    card1.name = 'Running Shoes'
    card1.img = 'card-image2.jpg'
    card1.price = 99
    
    return render(request, "index.html", {'card': card1})
