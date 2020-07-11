from django.shortcuts import render
from .models import Destination
#from .models import travello
from .forms import travelloForm

# Create your views here.
def index(request):
	
	dests = Destination.objects.all()
	return render(request,"index.html", {'dests' : dests})

def travelloTestView(request):
	obj = travello.objects.get(id = 1)
	context = {
		'objecto' : obj,
	}
	return render(request,'descripcion.html',context)

def destinoCreate(request):
	form = travelloForm(request.POST or None)
	context ={}
	if form.is_valid():
		form.save()
		my_form = travelloForm()

		context = {
		'forms' : my_form
	} 
	return render(request,'destinoCreate.html',context)
