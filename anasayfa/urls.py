from django.urls import path
from . import views

urlpatterns = [
    path('anasayfa/', views.anasayfa, name=anasayfa),
    path('', views.anasayfa, name=anasayfa),
    # '' işareti iki tane tek tırnak. Bundan => ' 
]
