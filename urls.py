"""primerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio.views import myHomeView, otherView	
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from accounts.views import register
from accounts.views import login
from accounts.views import logout
from travello.views import travelloTestView, destinoCreate

urlpatterns = [
    path("",views.index,name="index"),
    path('',include('travello.urls')),
    path('admin/', admin.site.urls),
    path('',myHomeView, name="pagina de inicio"),
    path('otro/',otherView, name="otra pagina"),
    #path('accounts/',include('accounts.urls')),
    path('accounts/register',register,name="register"),
    path('accounts/login',login,name="login"),
    path('accounts/logout',logout,name="logout"),
    path('crearDestino',travelloTestView,name="crear destino"),
    path('accounts/agregar',destinoCreate,name="agregar destino"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	
