"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import anasayfa.views
import ogrenci.views
import ogretmen.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anasayfa/', anasayfa.views.anasayfa),
    path('home/', anasayfa.views.xxxen, name='homeen'),
    path('anasayfa/', anasayfa.views.anasayfa, name='home'),
    path('', anasayfa.views.anasayfa),
    path('', anasayfa.views.anasayfa, name='home'),
    #path('ogrenci/', ogrenci.views.ogrenci),
    #path('ogretmen/', ogretmen.views.ogretmen),
    path('ogretmen/', ogretmen.views.ogretmenana, name='ogretmenana'),
    path('ogrenci/', ogrenci.views.ogrenciana, name='ogrenciana'),
    path('ogrenciekle/', ogrenci.views.ogrenciekle, name='ogrenciekle'),
    path('ogretmenekle/', ogretmen.views.ogretmenekle, name='ogretmenekle'),
    path('ogrenciliste/', ogrenci.views.ogrenciliste, name='ogrenciliste'),
    path('ogrenciler/detay/<int:id>', ogrenci.views.detay, name='detay'),
    path('ogrenci/duzelt/<int:id>', ogrenci.views.duzenle, name='duzenle'),
    path('sil/<int:id>', ogrenci.views.ogrencisil, name='sil') ,  
    path('ogretmenliste/', ogretmen.views.ogretmenliste, name='ogretmenliste'),
    path('ogretmenler/detay/<int:id>', ogretmen.views.detay, name='detay'),
    path('ogretmen/duzelt/<int:id>', ogretmen.views.duzenle, name='duzenle'),
    path('ogretmen/sil/<int:id>', ogretmen.views.ogretmensil, name='sil') ,
    path('ogrenciliste1/', ogrenci.views.ogrenciliste1, name='ogrenciliste'),
    path('ogretmenliste1/', ogretmen.views.ogretmenliste1, name='ogretmenliste'),
]

