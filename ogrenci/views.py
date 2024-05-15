from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def ogrenci(request):
    return HttpResponse("Öğrenci sayfasına hoş geldiniz.")
def ogrenciana(request):
  template = loader.get_template('ogrenciana.html')
  return HttpResponse(template.render())




from django.shortcuts import redirect
from django.shortcuts import render
from django import forms
from .models import Ogrenci
class OgrenciForm(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = ['TC', 'AdiSoyadi','Aciklama']  
# Kullanmak istediğiniz alanları buraya ekleyin
def ogrenciekle(request):
    if request.method == 'POST':
        form = OgrenciForm(request.POST)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritabanına kaydetme
            return redirect('ogrenciekle')  #url name
    else:
        form = OgrenciForm()
    return render(request, 'ogrenciekle.html', {'form': form})



def ogrenciliste(request):
    ogrenciliste = Ogrenci.objects.all()
    template = loader.get_template('ogrenciliste.html')
    context ={
        'ogrenciliste' : ogrenciliste,
    }
    return HttpResponse(template.render(context, request))

def ogrenci(request):
    template = loader.get_template('index1.html')
    return HttpResponse(template.render()) 

def detay(request, id):
  item = Ogrenci.objects.get(id=id)
  template = loader.get_template('ogrencidetay.html')
  context = {
    'item': item,
  }
  return HttpResponse(template.render(context, request))

# def duzenle(request, id):
#     template = loader.get_template('ogrenciduzelt.html')
#     ogrenci = Ogrenci.objects.get(id=id)
#     context = {
#         'ogrenci': ogrenci,
#     }
#     return HttpResponse(template.render(context, request))
def duzenle(request, id):
    # ogrenci = get_object_or_404(Ogrenci, id=id)
    ogrenci = Ogrenci.objects.get(id=id)
    if request.method == 'POST':
        form = OgrenciForm(request.POST, instance=ogrenci)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritab. kaydetme
            return redirect('ogrenciliste') #url name
    else:
        form = OgrenciForm(instance=ogrenci)
    return render(request, 'ogrenciduzelt.html', {'form': form})




def ogrencisil(request, id):
  item = Ogrenci.objects.get(id=id)
  # item = Ogrenci.objects.all()[4]
  item.delete()
  return redirect('ogrenciliste')
    

def ogrenciliste1(request):
    ogrenciliste = Ogrenci.objects.all()
    template = loader.get_template('ogrenciliste1.html')
    context ={
        'ogrenciliste' : ogrenciliste,
    }
    return HttpResponse(template.render(context, request))