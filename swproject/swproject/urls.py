from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from helloapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('service/', views.service, name='service'),
    path('search/',views.search, name='search'),
    path('accountapp/', include('accountapp.urls')),
]
