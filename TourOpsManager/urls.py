"""
URL configuration for TourOpsManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from OpsManager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('anasayfa', views.index, name='index'),
    
    path('personel-ekle/', views.add_personel, name='add_personel'),
    path('personel-list/', views.personel_list, name='personel_list'),  # Personel listesi için yo
    path('personel/delete/<int:personel_id>/', views.delete_personel, name='delete_personel'),
    
    path('departman-ekle/', views.add_departman, name='add_departman'),
    path('departman-list/', views.departman_list, name='departman_list'),
    path('departman/delete/<int:departman_id>/', views.delete_departman, name='delete_departman'),
    path('personel/departman-ekle/', views.add_personel_departman, name='add_personel_departman'),

    path('arac-ekle/', views.add_arac_tipi, name='add_arac'),
    path('arac-list/', views.arac_list, name='arac_list'),
    path('arac/delete/<int:arac_id>/', views.delete_arac, name='delete_arac'),
    
    path('il-ekle/', views.add_il, name='add_il'),
    path('il-list/', views.il_list, name='il_list'),
    path('il/delete/<int:il_id>/', views.delete_il, name='delete_il'),
    path('rehber/il-ekle/', views.add_rehber_il, name='add_rehber_il'),
    
    path('lokasyon-ekle/', views.add_lokasyon, name='add_lokasyon'),
    path('lokasyon-list/', views.lokasyon_list, name='lokasyon_list'),
    path('lokasyon/delete/<int:lokasyon_id>/', views.delete_lokasyon, name='delete_lokasyon'),
    path('lokasyon/il-ekle/', views.add_lokasyon_il, name='add_lokasyon_il'),
    path('otel/lokasyon-ekle/', views.add_otel_lokasyon, name='add_otel_lokasyon'),
    path('tur/lokasyon-ekle/', views.add_tur_lokasyon, name='add_tur_lokasyon'),
    
    path('sabit-gider-ekle/', views.add_sabit_gider, name='add_sabit_gider'),
    path('sabit-gider-list/', views.sabit_gider_list, name='sabit_gider_list'),
    path('sabit-gider/delete/<int:sabit_gider_id>/', views.delete_sabit_gider, name='delete_sabit_gider'),
    
    path('otel-ekle/', views.add_otel, name='otel_ekle'),
    path('otel-list/', views.otel_list, name='otel_list'),
    path('otel/delete/<int:otel_id>/', views.delete_otel, name='delete_otel'),
    
    path('rehber-ekle/', views.add_rehber, name='add_rehber'),
    path('rehber-list/', views.rehber_list, name='rehber_list'),
    path('rehber/delete/<int:rehber_id>/', views.delete_rehber, name='delete_rehber'),
    
    path('tur-ekle/', views.add_tur, name='tur_ekle'),
    path('tur-list/', views.tur_list, name='tur_list'),
    path('tur/delete/<int:tur_id>/', views.delete_tur, name='delete_tur'),
    
    path('transfer-ekle/', views.add_transfer, name='add_transfer'),
    path('transfer-list/', views.transfer_list, name='transfer_list'),
    path('transfer/delete/<int:transfer_id>/', views.delete_transfer, name='delete_transfer'),
    
    path('diger-yolcu-bilgileri-ekle/', views.add_diger_yolcu_bilgileri, name='add_diger_yolcu_bilgileri'),
    path('diger-yolcu_bilgileri-list/', views.diger_yolcu_bilgileri_list, name='diger_yolcu_bilgileri_list'),
    path('diger-yolcu-bilgileri/delete/<int:diger_yolcu_bilgileri_id>/', views.delete_diger_yolcu_bilgileri, name='delete_diger_yolcu_bilgileri'),
    
    path('yolcu-bilgileri-ekle/', views.add_yolcu_bilgileri, name='add_yolcu_bilgileri'),
    path('yolcu_bilgileri-list/', views.yolcu_bilgileri_list, name='yolcu_bilgileri_list'),
    path('yolcu-bilgileri/delete/<int:yolcu_bilgileri_id>/', views.delete_yolcu_bilgileri, name='delete_yolcu_bilgileri'),
    
    path('musteri-ekle/', views.add_musteri, name='add_musteri'),
    path('musteri-list/', views.musteri_list, name='musteri_list'),
    path('musteri/delete/<int:musteri_id>/', views.delete_musteri, name='delete_musteri'),
    
    path('satis-ekle/', views.create_satis, name='add_satis'),
    path('satis-list/', views.satis_list, name='satis_list'),
    path('satis/detay/<int:satis_id>', views.satis_detay, name='satis_detay'),
    path('satis/duzenle/<int:satis_id>/', views.edit_satis, name='edit_satis'),


    path('satis-raporu-indir/<int:satis_id>/', views.export_to_excel, name='satis_raporu_indir'),
    path('fiyatlandirma/', views.create_fiyatlandirma, name='create_fiyatlandirma'),
    path('fiyatlandirma-list/', views.fiyatlandırma_list, name='fiyatlandırma_list'),
    path('fiyatlandirma/detay/<int:fiyatlandirma_id>', views.fiyatlandirma_detay, name='fiyatlandirma_detay'),
]
