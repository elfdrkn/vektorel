from django.template import loader
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def ogretmen(request):
    #return HttpResponse("Öğretmen sayfasına hoş geldiniz.")
def ogretmenana(request):
  template = loader.get_template('ogretmenana.html')
  return HttpResponse(template.render())


from django.shortcuts import redirect
from django.shortcuts import render
from django import forms
from .models import Ogretmen
class OgretmenForm(forms.ModelForm):
    class Meta:
        model = Ogretmen
        fields = ['TC', 'AdiSoyadi','Aciklama']  
# Kullanmak istediğiniz alanları buraya ekleyin
def ogretmenekle(request):
    if request.method == 'POST':
        form = OgretmenForm(request.POST)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritabanına kaydetme
            return redirect('ogretmenekle')  #url name
    else:
        form = OgretmenForm()
    return render(request, 'ogretmenekle.html', {'form': form})



def ogretmenliste(request):
    ogretmenliste = Ogretmen.objects.all()
    template = loader.get_template('ogretmenliste.html')
    context ={
        'ogretmenliste' : ogretmenliste,
    }
    return HttpResponse(template.render(context, request))

def ogretmen(request):
    template = loader.get_template('index1.html')
    return HttpResponse(template.render()) 

def detay(request, id):
  item = Ogretmen.objects.get(id=id)
  template = loader.get_template('ogretmendetay.html')
  context = {
    'item': item,
  }
  return HttpResponse(template.render(context, request))

def duzenle(request, id):
    
    ogretmen = Ogretmen.objects.get(id=id)
    if request.method == 'POST':
        form = OgretmenForm(request.POST, instance=ogretmen)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritab. kaydetme
            return redirect('ogretmenliste') #url name
    else:
        form = OgretmenForm(instance=ogretmen)
    return render(request, 'ogretmenduzelt.html', {'form': form})




def ogretmensil(request, id):
  item = Ogretmen.objects.get(id=id)
  
  item.delete()
  return redirect('ogretmenliste')


def ogretmenliste1(request):
    ogretmenliste = Ogretmen.objects.all()
    template = loader.get_template('ogretmenliste1.html')
    context ={
        'ogretmenliste' : ogretmenliste,
    }
    return HttpResponse(template.render(context, request))