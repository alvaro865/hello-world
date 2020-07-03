from django.contrib import admin
from django.urls import path , include
from inicio.views import myHomeView, otherView	
from django.conf import settings
from django.conf.urls.static import static 
from accounts.views import register
from accounts.views import login
from accounts.views import logout


urlpatterns = [
	path('',include('travello.urls')),
    path('admin/', admin.site.urls),
    path('',myHomeView, name="pagina de inicio"),
    path('otro/',otherView, name="otra pagina"),
    #path('accounts/',include('accounts.urls')),
    path('accounts/register',register,name="register"),
    path('accounts/login',login,name="login"),
    path('accounts/logout',logout,name="logout")
    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	
