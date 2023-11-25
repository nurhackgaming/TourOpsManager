from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Departman, Fiyatlandırma, FiyatlandirmaItem, Personel, DigerYolcuBilgileri, Musteri, AracTipi, SabitGider, Il, Rehber, Lokasyon, Otel, Tur, Satis, SatisItem, Sirket, Transfer, YolcuBilgileri


class SatisItemInline(admin.TabularInline):  # veya admin.StackedInline
    model = SatisItem
    extra = 1  # Varsayılan olarak kaç tane boş 'SatisItem' formu gösterileceği

class SatisAdmin(admin.ModelAdmin):
    inlines = [SatisItemInline]
    # Diğer admin ayarları, örneğin list_display, search_fields vb.


    
admin.site.register(Satis, SatisAdmin)
admin.site.register(Departman)
admin.site.register(Personel)
admin.site.register(Musteri)
admin.site.register(AracTipi)
admin.site.register(SabitGider)
admin.site.register(Il)
admin.site.register(Rehber)
admin.site.register(Lokasyon)
admin.site.register(Otel)
admin.site.register(Tur)
admin.site.register(SatisItem)
admin.site.register(Transfer)
admin.site.register(YolcuBilgileri)
admin.site.register(Sirket)
admin.site.register(DigerYolcuBilgileri)
admin.site.register(Fiyatlandırma)
admin.site.register(FiyatlandirmaItem)
