from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request, *args,**kwargs):
	dest1 = Destination()
	dest1.nombreCiudad='Munbai'
	dest1.descripcionCiudad= 'The city that never sleeps'
	dest1.imagenCiudad = 'destination_1.jpg'
	dest1.precioTour = 701
	dest1.ofertaTour = False

	dest2 = Destination()
	dest2.nombreCiudad='Hiderabad'
	dest2.descripcionCiudad= 'The city '
	dest2.imagenCiudad = 'destination_2.jpg'
	dest2.precioTour = 700
	dest2.ofertaTour = True

	dest3 = Destination()
	dest3.nombreCiudad='Bengalarub'
	dest3.descripcionCiudad= 'Beatiful city '
	dest3.imagenCiudad = 'destination_3.jpg'
	dest3.precioTour = 702
	dest3.ofertaTour = False

	dests =[dest1,dest2,dest3]
	return render(request,"index.html", {'dests' : dests})
