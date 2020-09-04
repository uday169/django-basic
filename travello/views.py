from django.shortcuts import render
from .models import Destination

def index(request):
   
   dest1 = Destination()
   dest1.name = "Mumbai"
   dest1.desc = "City That never sleep"
   dest1.img = "destination_1.jpg"
   dest1.price = 700
   
   dest2 = Destination()
   dest2.name = "Hydrabed"
   dest2.desc = "Hydrabedi Biryani"
   dest2.img = "destination_2.jpg"
   dest2.price = 650
   
   dest3 = Destination()
   dest3.name = "Banglore"
   dest3.desc = "Silcon City"
   dest3.img = "destination_3.jpg"
   dest3.price = 750
   
   dests = [dest1, dest2, dest3]
   
   return render(request, 'index.html' , {'dests': dests})