from django.db import models

# Create your models here.
class Destination:
	idCiudad : int
	nombreCiudad : str
	imagenCiudad :str
	descripcionCiudad :str
	precioTour :int
	ofertaTour : bool
