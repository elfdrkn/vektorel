from django.contrib import admin
from .models import Ogrenci

# admin.site.register(Ogrenci)

class OgrenciAdmin(admin.ModelAdmin):
  list_display = ("AdiSoyadi", "Aciklama")

admin.site.register(Ogrenci, OgrenciAdmin)
# Register your models here.
