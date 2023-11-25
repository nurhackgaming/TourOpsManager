import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        # Kullanıcı zaten giriş yapmış, ana sayfaya yönlendir
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))  # Giriş başarılı, ana sayfaya yönlendir
        else:
            return render(request, 'auth-login.html', {'error_message': 'Geçersiz kullanıcı adı veya şifre.'})
    else:
        return render(request, 'auth-login.html')

    
    
def logout_view(request):
    logout(request)
    # Çıkış sonrası kullanıcıyı başka bir sayfaya yönlendirebilirsiniz.
    return HttpResponseRedirect(reverse('login'))  # Örnek bir yönlendirme

@login_required
def index(request):
    return render(request, 'index.html', {'title' : 'Anasayfa'})


@login_required
def add_personel(request):
    if request.method == 'POST':
        form = PersonelForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonelForm(request=request)

    return render(request, 'personel_ekle.html', {'form': form, 'title' : 'Personel Ekle'})

@login_required
def add_departman(request):
    if request.method == 'POST':
        form = DepartmanForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DepartmanForm()
    return render(request, 'departman_ekle.html', {'form': form, 'title' : 'Departman Ekle'})

@login_required
def add_personel_departman(request):
    if request.method == 'POST':
        form = DepartmanForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('add_personel')
    else:
        form = DepartmanForm()
    return render(request, 'departman_ekle.html', {'form': form, 'title' : 'Personel için Departman Ekle'})

@login_required
def add_arac_tipi(request):
    if request.method == 'POST':
        form = AracTipiForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AracTipiForm(request=request)
    return render(request, 'arac_ekle.html', {'form': form, 'title' : 'Araç Ekle'})


@login_required
def add_sabit_gider(request):
    if request.method == 'POST':
        form = SabitGiderForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')  # Başarılı kayıttan sonra yönlendirilecek URL
    else:
        form = SabitGiderForm(request=request)

    return render(request, 'sabit_gider_ekle.html', {'form': form, 'title' : 'Sabit Gider Ekle'})

@login_required
def add_il(request):
    if request.method == 'POST':
        form = IlForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')  # Başarılı kayıttan sonra yönlendirilecek view
    else:
        form = IlForm(request=request)

    return render(request, 'il_ekle.html', {'form': form, 'title' : 'İl Ekle'})

@login_required
def add_lokasyon_il(request):
    if request.method == 'POST':
        form = IlForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('add_lokasyon')  # Başarılı kayıttan sonra yönlendirilecek view
    else:
        form = IlForm(request=request)

    return render(request, 'il_ekle.html', {'form': form, 'title' : 'Lokasyon için İl Ekle'})

@login_required
def add_rehber_il(request):
    if request.method == 'POST':
        form = IlForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('add_rehber')  # Başarılı kayıttan sonra yönlendirilecek view
    else:
        form = IlForm(request=request)

    return render(request, 'il_ekle.html', {'form': form, 'title' : 'Rehber için İl Ekle'})

@login_required
def add_lokasyon(request):
    if request.method == 'POST':
        form = LokasyonForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LokasyonForm(request=request)
    return render(request, 'lokasyon_ekle.html', {'form': form, 'title' : 'Lokasyon Ekle'})

@login_required
def add_otel(request):
    if request.method == 'POST':
        form = OtelForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')  # Otel listesi sayfasına yönlendir
    else:
        form = OtelForm(request=request)
    return render(request, 'otel_ekle.html', {'form': form, 'title' : 'Otel Ekle'})

@login_required
def add_otel_lokasyon(request):
    if request.method == 'POST':
        form = LokasyonForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('otel_ekle')
    else:
        form = LokasyonForm(request=request)
    return render(request, 'lokasyon_ekle.html', {'form': form, 'title' : 'Otel için Lokasyon Ekle'})

@login_required
def add_tur_lokasyon(request):
    if request.method == 'POST':
        form = LokasyonForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('tur_ekle')
    else:
        form = LokasyonForm(request=request)
    return render(request, 'lokasyon_ekle.html', {'form': form, 'title' : 'Tur için Lokasyon Ekle'})

@login_required
def add_rehber(request):
    if request.method == 'POST':
        form = RehberForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            # Başarılı kayıttan sonra istediğiniz bir sayfaya yönlendirme yapabilirsiniz.
            return redirect('index')
    else:
        form = RehberForm(request=request)

    return render(request, 'rehber_ekle.html', {'form': form, 'title' : 'Rehber Ekle'})


@login_required
def add_tur(request):
    if request.method == 'POST':
        form = TurForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            # Başarılı bir şekilde tur eklendikten sonra kullanıcıyı turlar listesine yönlendir
            return redirect('index')
    else:
        form = TurForm(request=request)

    return render(request, 'tur_ekle.html', {'form': form, 'title' : 'Tur Ekle'})


@login_required
def add_transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            # Başarılı kayıt sonrası yönlendirme
            return redirect('index')  # 'transfer_liste' URL'sine yönlendir
    else:
        form = TransferForm(request=request)

    return render(request, 'transfer_ekle.html', {'form': form, 'title' : 'Transfer Ekle'})

@login_required
def add_musteri(request):
    if request.method == 'POST':
        form = MusteriForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')  # Başarılı kayıttan sonra yönlendirilecek sayfa
    else:
        form = MusteriForm(request=request)

    return render(request, 'musteri_ekle.html', {'form': form})



@login_required
def personel_list(request):
    user = request.user
    personeller = Personel.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'personel_list.html', {'personeller': personeller, 'title': 'Personel Listesi'})

@login_required
def delete_personel(request, personel_id):
    personel = get_object_or_404(Personel, pk=personel_id)

    if request.method == 'POST':
        personel.delete()  # Personeli sil
        return redirect('personel_list')  # Personel listesine yönlendirme

    return redirect('personel_list')

@login_required
def departman_list(request):
    user = request.user
    departmanlar = Departman.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'departman_list.html', {'departmanlar': departmanlar, 'title': 'Departman Listesi'})

@login_required
def delete_departman(request, departman_id):
    departman = get_object_or_404(Departman, pk=departman_id)

    if request.method == 'POST':
        departman.delete()  # Personeli sil
        return redirect('departman_list')  # Personel listesine yönlendirme

    return redirect('departman_list')


@login_required
def arac_list(request):
    user = request.user
    araclar = AracTipi.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'arac_list.html', {'araclar': araclar, 'title': 'Araç Listesi'})

@login_required
def delete_arac(request, arac_id):
    arac = get_object_or_404(AracTipi, pk=arac_id)

    if request.method == 'POST':
        arac.delete()  # Personeli sil
        return redirect('arac_list')  # Personel listesine yönlendirme

    return redirect('arac_list')

@login_required
def il_list(request):
    user = request.user
    iller = Il.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'il_list.html', {'iller': iller, 'title': 'İl Listesi'})

@login_required
def delete_il(request, il_id):
    il = get_object_or_404(Il, pk=il_id)

    if request.method == 'POST':
        il.delete()  # Personeli sil
        return redirect('il_list')  # Personel listesine yönlendirme

    return redirect('il_list')

@login_required
def lokasyon_list(request):
    user = request.user
    lokasyonlar = Lokasyon.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'lokasyon_list.html', {'lokasyonlar': lokasyonlar, 'title': 'Lokasyon Listesi'})

@login_required
def delete_lokasyon(request, lokasyon_id):
    lokasyon = get_object_or_404(Lokasyon, pk=lokasyon_id)

    if request.method == 'POST':
        lokasyon.delete()  # Personeli sil
        return redirect('lokasyon_list')  # Personel listesine yönlendirme

    return redirect('lokasyon_list')

@login_required
def sabit_gider_list(request):
    user = request.user
    giderler = SabitGider.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'sabit_gider_list.html', {'giderler': giderler, 'title': 'Sabit Giderler Listesi'})

@login_required
def delete_sabit_gider(request, sabit_gider_id):
    sabit_gider = get_object_or_404(SabitGider, pk=sabit_gider_id)

    if request.method == 'POST':
        sabit_gider.delete()  # Personeli sil
        return redirect('sabit_gider_list')  # Personel listesine yönlendirme

    return redirect('sabit_gider_list')

@login_required
def otel_list(request):
    user = request.user
    oteller = Otel.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'otel_list.html', {'oteller': oteller, 'title': 'Otel Listesi'})

@login_required
def delete_otel(request, otel_id):
    otel = get_object_or_404(Otel, pk=otel_id)

    if request.method == 'POST':
        otel.delete()  # Personeli sil
        return redirect('otel_list')  # Personel listesine yönlendirme

    return redirect('otel_list')

@login_required
def rehber_list(request):
    user = request.user
    rehberler = Rehber.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'rehber_list.html', {'rehberler': rehberler, 'title': 'Rehber Listesi'})

@login_required
def delete_rehber(request, rehber_id):
    rehber = get_object_or_404(Rehber, pk=rehber_id)

    if request.method == 'POST':
        rehber.delete()  # Personeli sil
        return redirect('rehber_list')  # Personel listesine yönlendirme

    return redirect('rehber_list')

@login_required
def tur_list(request):
    user = request.user
    turlar = Tur.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'tur_list.html', {'turlar': turlar, 'title': 'Tur Listesi'})

@login_required
def delete_tur(request, tur_id):
    tur = get_object_or_404(Tur, pk=tur_id)

    if request.method == 'POST':
        tur.delete()  # Personeli sil
        return redirect('tur_list')  # Personel listesine yönlendirme

    return redirect('tur_list')

@login_required
def transfer_list(request):
    user = request.user
    transferler = Transfer.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'transfer_list.html', {'transferler': transferler, 'title': 'Transfer Listesi'})

@login_required
def delete_transfer(request, transfer_id):
    transfer = get_object_or_404(Transfer, pk=transfer_id)

    if request.method == 'POST':
        transfer.delete()  # Personeli sil
        return redirect('transfer_list')  # Personel listesine yönlendirme

    return redirect('transfer_list')

@login_required
def musteri_list(request):
    user = request.user
    musteriler = Musteri.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'musteri_list.html', {'musteriler': musteriler, 'title': 'Müşteri Listesi'})

@login_required
def delete_musteri(request, musteri_id):
    musteri = get_object_or_404(Musteri, pk=musteri_id)

    if request.method == 'POST':
        musteri.delete()  # Personeli sil
        return redirect('musteri_list')  # Personel listesine yönlendirme

    return redirect('musteri_list')

@login_required
def satis_list(request):
    # Satışları alın ve ilgili satış itemlerini "prefetch_related" ile alın
    satislar = Satis.objects.prefetch_related('satisitem_set').all()  # Satis modelini kendi projenizdeki modele uygun bir şekilde kullanın

    return render(request, 'satis_list.html', {'satislar': satislar, 'title': 'Satış Listesi'})
@login_required
def satis_detay(request, satis_id):
    # Satışları alın ve ilgili satış itemlerini "prefetch_related" ile alın
    satis = Satis.objects.prefetch_related('satisitem_set').get(id = satis_id)  # Satis modelini kendi projenizdeki modele uygun bir şekilde kullanın
    yolcu_sayisi = 0
    if not satis.yolcu == None:
        yolcu_sayisi += 1
    if not satis.digeryolcular.count() == 0:
        yolcu_sayisi += satis.digeryolcular.count()
            

    return render(request, 'satis_detay.html', {'satis': satis, 'title': 'Satış Listesi', 'yolcu_sayisi': yolcu_sayisi})

from django.contrib import messages
from django.db import transaction

@login_required
def edit_satis(request, satis_id):
    satis = get_object_or_404(Satis, id=satis_id)
    if request.method == 'POST':
        form = SatisForm(request.POST, instance=satis)
        formset = SatisItemFormSet(request.POST, instance=satis, prefix='satis_items')
        
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                satis = form.save()
                formset.save()
                messages.success(request, "Satış ve satış öğeleri başarıyla güncellendi.")
                return redirect('satis_detay', satis_id=satis.id)
        else:
            messages.error(request, "Form veya formset'te hatalar var.")
            print(form.errors)
            print(formset.errors)
            # Konsol çıktıları yerine, hataları template'e gönderin
            context = {'form': form, 'formset': formset, 'satis': satis, 'errors': True}
            return render(request, 'satis_ekle.html', context)
    else:
        form = SatisForm(instance=satis)
        formset = SatisItemFormSet(instance=satis, prefix='satis_items')
    
    context = {'form': form, 'formset': formset, 'satis': satis}
    return render(request, 'satis_ekle.html', context)




@login_required
def create_satis(request):

    if request.method == 'POST':
        form = SatisForm(request.POST, request=request)
        if form.is_valid():
            satis = form.save()
            formset = SatisItemFormSet(request.POST, instance=satis)

            # Formset içindeki her form için request parametresini ayarla
            for form in formset:
                form.request = request

            if formset.is_valid():
                formset.save()
                return redirect('index')
    else:
        form = SatisForm()
        formset = SatisItemFormSet()

    return render(request, 'satis_ekle.html', {'form': form, 'formset': formset, 'title': 'Satış Yap'})

@login_required
def add_yolcu_bilgileri(request):
    if request.method == 'POST':
        form = YolcuBilgileriForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yolcu bilgileri başarıyla kaydedildi.')
            return redirect('yolcu_bilgileri_list')
    else:
        form = YolcuBilgileriForm()

    return render(request, 'yolcu_bilgileri_ekle.html', {'form': form, 'title': 'Yolcu Ekle'})

@login_required
def add_diger_yolcu_bilgileri(request):
    if request.method == 'POST':
        form = DigerYolcuBilgileriForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diğer Yolcu bilgileri başarıyla kaydedildi.')
            return redirect('diger_yolcu_bilgileri_list')
    else:
        form = DigerYolcuBilgileriForm()

    return render(request, 'diger_yolcu_bilgileri_ekle.html', {'form': form, 'title': 'Diğer Yolcu Ekle'})

@login_required
def diger_yolcu_bilgileri_list(request):
    user = request.user
    diger_yolcu_bilgileri = DigerYolcuBilgileri.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'diger_yolcu_bilgileri_list.html', {'diger_yolcu_bilgileri': diger_yolcu_bilgileri, 'title': 'Diğer Yolcu Listesi'})

@login_required
def yolcu_bilgileri_list(request):
    user = request.user
    yolcu_bilgileri = YolcuBilgileri.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'yolcu_bilgileri_list.html', {'yolcu_bilgileri': yolcu_bilgileri, 'title': 'Yolcu Listesi'})

@login_required
def delete_diger_yolcu_bilgileri(request, diger_yolcu_bilgileri_id):
    diger_yolcu_bilgileri = get_object_or_404(DigerYolcuBilgileri, pk=diger_yolcu_bilgileri_id)

    if request.method == 'POST':
        diger_yolcu_bilgileri.delete()  # Personeli sil
        return redirect('diger_yolcu_bilgileri_list')  # Personel listesine yönlendirme

    return redirect('yolcu_bilgileri_list')
@login_required
def delete_yolcu_bilgileri(request, yolcu_bilgileri_id):
    yolcu_bilgileri = get_object_or_404(YolcuBilgileri, pk=yolcu_bilgileri_id)

    if request.method == 'POST':
        yolcu_bilgileri.delete()  # Personeli sil
        return redirect('yolcu_bilgileri_list')  # Personel listesine yönlendirme

    return redirect('yolcu_bilgileri_list')



from django.http import HttpResponse
from io import BytesIO # Modelinizi burada import edin

# def export_to_word(request, satis_id):
#     # Veritabanından satış ve ilgili verileri alın
#     satis = get_object_or_404(Satis, pk=satis_id)
#     satis_items = satis.satisitem_set.all()
#     yolcu_sayisi = 0
#     if not satis.yolcu == None:
#         yolcu_sayisi += 1
#     if not satis.digeryolcular.count() == 0:
#         yolcu_sayisi += satis.digeryolcular.count()
#     # Word dokümanı oluştur
#     doc = Document()
#     doc.add_heading('Satış Raporu', 0)

#     # Ana tabloyu ekle
#     table = doc.add_table(rows=1, cols=8)
#     hdr_cells = table.rows[0].cells
#     hdr_cells[0].text = 'ID'
#     hdr_cells[1].text = 'Satıcı Personel'
#     hdr_cells[2].text = 'Alıcı Müşteri'
#     hdr_cells[3].text = 'Başlangıç Tarihi'
#     hdr_cells[4].text = 'Bitiş Tarihi'
#     hdr_cells[5].text = 'Satış Durumu'
#     hdr_cells[6].text = 'Toplam Fiyat'
#     hdr_cells[7].text = 'Toplam Yolcu Sayısı'
#     # ... diğer başlık hücrelerini doldurun

#     # Satış verilerini tabloya ekle
#     row_cells = table.add_row().cells
#     row_cells[0].text = str(satis.id) if satis.id else "-----"
#     row_cells[1].text = satis.satici_personel.user.get_full_name() if satis.satici_personel.user else "-----"
#     row_cells[2].text = f"{satis.alici_musteri.ad} {satis.alici_musteri.soyad}" if satis.alici_musteri.ad else "-----"
#     row_cells[3].text = str(satis.baslangic_tarihi) if satis.baslangic_tarihi else "-----"
#     row_cells[4].text = str(satis.bitis_tarihi) if satis.bitis_tarihi else "-----"
#     row_cells[5].text = "Satıldı" if satis.satildi else "Beklemede" if satis.satildi else "-----"
#     row_cells[6].text = str(satis.total_price) if satis.total_price else "-----"
#     row_cells[7].text = str(yolcu_sayisi) if yolcu_sayisi else "-----"
#     # Yolcu sayısını nasıl hesapladığınıza bağlı
#     # ... diğer satış verilerini doldurun

#     # Satış öğeleri için alt tablo oluştur
#     doc.add_paragraph('Satış Detayları:')
#     for item in satis_items:
#         item_table = doc.add_table(rows=1, cols=10)
#         item_hdr_cells = item_table.rows[0].cells
#         item_hdr_cells[0].text = 'Gün'
#         item_hdr_cells[1].text = 'İşlem Türü'
#         item_hdr_cells[2].text = 'Açıklama'
#         item_hdr_cells[3].text = 'Otel'
#         item_hdr_cells[4].text = 'Otel Türü'
#         item_hdr_cells[5].text = 'Tur'
#         item_hdr_cells[6].text = 'Transfer'
#         item_hdr_cells[7].text = 'Araç Tipi'
#         item_hdr_cells[8].text = 'Rehber'
#         item_hdr_cells[9].text = 'Fiyat'
#         # ... diğer başlık hücrelerini doldurun

#         item_row_cells = item_table.add_row().cells
#         item_row_cells[0].text = str(item.gun) if item.gun else "-----"
#         item_row_cells[1].text = item.islem_turu if item.islem_turu else "-----"
#         item_row_cells[2].text = item.aciklama if item.aciklama else "-----"
#         item_row_cells[3].text = item.oteller if item.oteller else "-----"
#         item_row_cells[4].text = item.otel_turu if item.otel_turu else "-----"
#         item_row_cells[5].text = item.turlar.adi if item.turlar else "-----"
#         item_row_cells[6].text = item.transferler.guzergah if item.transferler else "-----"
#         item_row_cells[7].text = item.arac_tipi.adi if item.arac_tipi else "-----"
#         item_row_cells[8].text = item.rehber.adi if item.rehber else "-----"
#         item_row_cells[9].text = str(item.fiyat) if item.fiyat else "-----"
#         # ... diğer satış öğesi verilerini doldurun

#     # Word dokümanını bir byte stream olarak kaydet
#     file_stream = BytesIO()
#     doc.save(file_stream)
#     file_stream.seek(0)

#     # Kullanıcıya indirme olarak sun
#     response = HttpResponse(file_stream.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename=satis_raporu.docx'
#     return response

import pandas as pd
import pytz
from django.http import HttpResponse
from .models import Satis  # Modelinizi burada import edin
from io import BytesIO

def export_to_excel(request, satis_id):
    # Veritabanından satış ve ilgili verileri alın
    satis = get_object_or_404(Satis, pk=satis_id)
    satis_items = satis.satisitem_set.all()

    # Zaman dilimi bilgisini kaldırın
    from datetime import datetime, timezone

    def remove_timezone(dt):
        if isinstance(dt, datetime):
            return dt.astimezone(timezone.utc).replace(tzinfo=None)
        return dt  # Eğer datetime değilse, aynı değeri geri döndür

    # Satış bilgilerini bir DataFrame'e aktarın
    satis_data = {
        'ID': [satis.id],
        'Satıcı Personel': [satis.satici_personel.user.get_full_name()],
        'Alıcı Müşteri': [f"{satis.alici_musteri.ad} {satis.alici_musteri.soyad}"],
        'Başlangıç Tarihi': [remove_timezone(satis.baslangic_tarihi)],
        'Bitiş Tarihi': [remove_timezone(satis.bitis_tarihi)],
        'Satış Durumu': ['Satıldı' if satis.satildi else 'Beklemede'],
        'Toplam Fiyat': [satis.total_price]
        # Diğer satış bilgileri eklenebilir
    }
    df_satis = pd.DataFrame(satis_data)

    # Satış öğelerini bir DataFrame'e aktarın
    satis_items_data = [{
        'gun': remove_timezone(item.gun),
        'islem_turu': item.islem_turu,
        'aciklama': item.aciklama,
        'oteller': item.oteller,
        'otel_turu': item.otel_turu,
        'turlar': item.turlar,
        'transferler': item.transferler,
        'arac_tipi': item.arac_tipi,
        'rehber': item.rehber,
        'fiyat': item.fiyat
        # Diğer satış öğe bilgileri eklenebilir
    } for item in satis_items]
    df_satis_items = pd.DataFrame(satis_items_data)

    # Excel dosyasını bir byte stream olarak oluşturun
    with BytesIO() as b:
        # Excel writer oluşturun
        with pd.ExcelWriter(b, engine='openpyxl') as writer:
            # İlk DataFrame'i yazdırın
            df_satis.to_excel(writer, sheet_name='Satış Raporu', index=False)
            
            # İkinci DataFrame'in başlangıç satırını hesaplayın
            startrow = len(df_satis) + 2  # İlk DataFrame'in uzunluğu + boşluk

            # İkinci DataFrame'i yazdırın
            df_satis_items.to_excel(writer, sheet_name='Satış Raporu', startrow=startrow, index=False)

        # Kullanıcıya indirme olarak sunun
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=satis_raporu.xlsx'
        return response

from datetime import datetime

def parse_custom_date(date):
    # Veritabanından gelen datetime.date nesnesini doğrudan kullanın
    return date


def create_fiyatlandirma(request):
    if request.method == 'POST':
        form = FiyatlandirmaForm(request.POST, request=request)
        formset = FiyatlandirmaItemFormSet(request.POST)
        user = request.user
        if form.is_valid() and formset.is_valid():
            personel = Personel.objects.get(user=user)  # User'ı Personel nesnesine dönüştür
            fiyatlandirma = form.save(commit=False)
            fiyatlandirma.olusturan = personel
            fiyatlandirma.save()  # Ana modeli kaydet
            formset.instance = fiyatlandirma  # İlişkiyi kur
            for form in formset:
                tarih_str = form.cleaned_data.get('tarih')
                tarih_obj = parse_custom_date(tarih_str)
                if tarih_obj:
                    form.cleaned_data['tarih'] = tarih_obj
                else:
                    print("Geçersiz tarih formatı:", tarih_str)
            formset.save()  # İlişkili modeli kaydet

            # İşlem başarılıysa, başka bir sayfaya yönlendir
            return redirect('index')
        else:
            print("Form veya FormSet geçerli değil")
            print("Form Hataları:", form.errors)
            print("FormSet Hataları:", formset.errors)
    else:
        form = FiyatlandirmaForm(request=request)
        formset = FiyatlandirmaItemFormSet()

    return render(request, 'fiyatlandirma.html', {'form': form, 'formset': formset, 'title': 'Fiyatlandır'})


@login_required
def fiyatlandırma_list(request):
    user = request.user
    fiyatlandirmalar = Fiyatlandırma.objects.filter(sirket = user.personel.sirket)  # Tüm personelleri alın
    return render(request, 'fiyatlandirma_list.html', {'fiyatlandirmalar': fiyatlandirmalar, 'title': 'Fiyatlandırma Listesi'})

@login_required
def fiyatlandirma_detay(request, fiyatlandirma_id):
    # Satışları alın ve ilgili satış itemlerini "prefetch_related" ile alın
    fiyatlandirma = Fiyatlandırma.objects.prefetch_related('fiyatlandirmaitem_set').get(id = fiyatlandirma_id)  # Satis modelini kendi projenizdeki modele uygun bir şekilde kullanın
    return render(request, 'fiyatlandirma_detay.html', {'fiyatlandirma': fiyatlandirma, 'title': 'Fiyatlandırma Detay'})