from django.contrib import admin
from django.urls import path
from helloapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', views.login, name='login'),
    path('', views.service, name='service'),
    path('',views.search, name='search'),
]
