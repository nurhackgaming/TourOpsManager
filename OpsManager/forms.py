from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from .models import *

class WidgetMixin:
    def set_widgets(self):
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
class SetCompanyMixin:
    def set_company_from_request(self, obj):
        if hasattr(self, 'request') and self.request:
            obj.sirket = self.request.user.personel.sirket


class UserCompanyMixin(SetCompanyMixin):
    def create_user_and_set_company(self, cleaned_data, obj):
        user = User.objects.create_user(
            cleaned_data['username'],
            password=cleaned_data['password']
        )
        obj.user = user
        self.set_company_from_request(obj)

class PersonelForm(UserCompanyMixin, WidgetMixin, forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    first_name = forms.CharField(max_length=30, required=True)  # Ad için alan
    last_name = forms.CharField(max_length=30, required=True)   # Soyad için alan
    email = forms.EmailField(required=True)                     # E-posta için alan

    class Meta:
        model = Personel
        fields = ['departman', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PersonelForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        personel = super(PersonelForm, self).save(commit=False)
        self.create_user_and_set_company(self.cleaned_data, personel)
        if commit:
            personel.save()
        return personel

    def create_user_and_set_company(self, cleaned_data, obj):
        user = User.objects.create_user(
            cleaned_data['username'],
            password=cleaned_data['password'],
            first_name=cleaned_data['first_name'],  # Adı ayarlayın
            last_name=cleaned_data['last_name'],   # Soyadı ayarlayın
            email=cleaned_data['email']            # E-posta adresini ayarlayın
        )
        obj.user = user
        self.set_company_from_request(obj)

class DepartmanForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = Departman
        fields = ['adi']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(DepartmanForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        departman = super(DepartmanForm, self).save(commit=False)
        self.set_company_from_request(departman)
        if commit:
            departman.save()
        return departman


class AracTipiForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = AracTipi
        fields = ['adi', 'kapasite']
        labels = {
            'adi': 'Araç Tipi Adı',
            'kapasite': 'Kapasite'
        }
        widgets = {
            'adi': forms.TextInput(attrs={'class': 'form-control'}),
            'kapasite': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AracTipiForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        arac_tipi = super(AracTipiForm, self).save(commit=False)
        self.set_company_from_request(arac_tipi)
        if commit:
            arac_tipi.save()
        return arac_tipi
    
    
class SabitGiderForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = SabitGider
        fields = ['adi', 'fiyati']
        labels = {
            'adi': 'Gider Adı',
            'fiyati': 'Fiyatı'
        }
        widgets = {
            'adi': forms.TextInput(attrs={'class': 'form-control'}),
            'fiyati': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SabitGiderForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        sabit_gider = super(SabitGiderForm, self).save(commit=False)
        self.set_company_from_request(sabit_gider)
        if commit:
            sabit_gider.save()
        return sabit_gider
    
class IlForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = Il
        fields = ['adi']
        labels = {
            'adi': 'İl Adı',
        }
        widgets = {
            'adi': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(IlForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        il = super(IlForm, self).save(commit=False)
        self.set_company_from_request(il)
        if commit:
            il.save()
        return il
    
class LokasyonForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = Lokasyon
        fields = ['il', 'adi']
        labels = {
            'il': 'İl',
            'adi': 'Lokasyon Adı'
        }
        widgets = {
            'il': forms.Select(attrs={'class': 'form-control'}),
            'adi': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LokasyonForm, self).__init__(*args, **kwargs)
        self.fields['il'].queryset = Il.objects.filter(sirket=self.request.user.personel.sirket)
        self.set_widgets()

    def save(self, commit=True):
        lokasyon = super(LokasyonForm, self).save(commit=False)
        self.set_company_from_request(lokasyon)
        if commit:
            lokasyon.save()
        return lokasyon
    
class OtelForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = Otel
        fields = ['lokasyon', 'adi', 'tek_kisilik_oda_ucreti', 'cift_kisilik_oda_ucreti', 'yildiz_sayisi']
        labels = {
            'lokasyon': 'Lokasyon',
            'adi': 'Otel Adı',
            'tek_kisilik_oda_ucreti': 'Tek Kişilik Oda Ücreti',
            'cift_kisilik_oda_ucreti': 'Çift Kişilik Oda Ücreti',
            'yildiz_sayisi': 'Yıldız Sayısı',
        }
        widgets = {
            'lokasyon': forms.Select(attrs={'class': 'form-control'}),
            'adi': forms.TextInput(attrs={'class': 'form-control'}),
            'tek_kisilik_oda_ucreti': forms.NumberInput(attrs={'class': 'form-control'}),
            'cift_kisilik_oda_ucreti': forms.NumberInput(attrs={'class': 'form-control'}),
            'yildiz_sayisi': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(OtelForm, self).__init__(*args, **kwargs)
        self.set_widgets()
        self.fields['lokasyon'].queryset = Lokasyon.objects.filter(sirket=self.request.user.personel.sirket)

    def save(self, commit=True):
        otel = super(OtelForm, self).save(commit=False)
        if self.request:
            otel.sirket = self.request.user.personel.sirket
        if commit:
            otel.save()
        return otel
    
class RehberForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = Rehber
        fields = ['il', 'adi', 'ucreti']
        labels = {
            'il': 'İl',
            'adi': 'Rehber Adı',
            'ucreti': 'Ücreti'
        }
        widgets = {
            'il': forms.Select(attrs={'class': 'form-control'}),
            'adi': forms.TextInput(attrs={'class': 'form-control'}),
            'ucreti': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RehberForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        rehber = super(RehberForm, self).save(commit=False)
        self.set_company_from_request(rehber)
        if commit:
            rehber.save()
        return rehber
    
class TurForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = Tur
        fields = ['lokasyon', 'adi', 'aciklama', 'fiyati']
        labels = {
            'lokasyon': 'Lokasyon',
            'adi': 'Tur Adı',
            'aciklama': 'Açıklama',
            'fiyati': 'Fiyatı'
        }
        widgets = {
            'lokasyon': forms.Select(attrs={'class': 'form-control'}),
            'adi': forms.TextInput(attrs={'class': 'form-control'}),
            'aciklama': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fiyati': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TurForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        tur = super(TurForm, self).save(commit=False)
        self.set_company_from_request(tur)
        if commit:
            tur.save()
        return tur
    
class TransferForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['guzergah', 'fiyat_5_koltuk', 'fiyat_7_koltuk', 'fiyat_9_koltuk', 
                  'fiyat_12_koltuk', 'fiyat_15_koltuk', 'fiyat_16_20_koltuk']
        labels = {
            'guzergah': 'Güzergah',
            'fiyat_5_koltuk': 'Fiyat (5 Koltuk)',
            'fiyat_7_koltuk': 'Fiyat (7 Koltuk)',
            'fiyat_9_koltuk': 'Fiyat (9 Koltuk)',
            'fiyat_12_koltuk': 'Fiyat (12 Koltuk)',
            'fiyat_15_koltuk': 'Fiyat (15 Koltuk)',
            'fiyat_16_20_koltuk': 'Fiyat (16-20 Koltuk)',
        }
        widgets = {
            'guzergah': forms.TextInput(attrs={'class': 'form-control'}),
            'fiyat_5_koltuk': forms.NumberInput(attrs={'class': 'form-control'}),
            'fiyat_7_koltuk': forms.NumberInput(attrs={'class': 'form-control'}),
            'fiyat_9_koltuk': forms.NumberInput(attrs={'class': 'form-control'}),
            'fiyat_12_koltuk': forms.NumberInput(attrs={'class': 'form-control'}),
            'fiyat_15_koltuk': forms.NumberInput(attrs={'class': 'form-control'}),
            'fiyat_16_20_koltuk': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TransferForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        transfer = super(TransferForm, self).save(commit=False)
        self.set_company_from_request(transfer)
        if commit:
            transfer.save()
        return transfer
    
    
class MusteriForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = Musteri
        fields = ['ad', 'soyad', 'tel', 'mail', 'musteri_tipi']
        labels = {
            'ad': 'Ad',
            'soyad': 'Soyad',
            'tel': 'Telefon',
            'mail': 'E-posta',
            'musteri_tipi': 'Müşteri Tipi'
        }
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
            'soyad': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'musteri_tipi': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MusteriForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        musteri = super(MusteriForm, self).save(commit=False)
        self.set_company_from_request(musteri)
        if commit:
            musteri.save()
        return musteri
    
    
class SatisForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = Satis
        fields = ['satici_personel', 'alici_musteri', 'sabit_giderler', 'yolcu', 'digeryolcular', 'baslangic_tarihi', 'bitis_tarihi', 'satildi']
        labels = {
            'satici_personel': 'Satıcı Personel',
            'alici_musteri': 'Alıcı Müşteri',
            'sabit_giderler': 'Sabit Giderler',
            'yolcu': 'Yolcu Bilgisi',
            'digeryolcular': 'Diğer Yolcu Bilgileri',
            'baslangic_tarihi': 'Başlangıç Tarihi',
            'bitis_tarihi': 'Bitiş Tarihi',
            'satildi': 'Satıldı mı?',
        }
        widgets = {
            'satici_personel': forms.Select(attrs={'class': 'form-control'}),
            'alici_musteri': forms.Select(attrs={'class': 'form-control'}),
            'sabit_giderler': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'yolcu': forms.Select(attrs={'class': 'form-control'}),
            'digeryolcular': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'baslangic_tarihi': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'bitis_tarihi': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'satildi': forms.CheckboxInput(attrs={'class': 'form-control' })
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SatisForm, self).__init__(*args, **kwargs)
        self.set_widgets()
        
    def save(self, commit=True):
        satis = super(SatisForm, self).save(commit=False)
        self.set_company_from_request(satis)
        if commit:
            satis.save()
            self.save_m2m()

        return satis


class SatisItemForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = SatisItem
        fields = ['gun', 'saat', 'islem_turu', 'aciklama', 'oteller', 'otel_turu', 'turlar', 'transferler', 'arac_tipi', 'rehber', 'fiyat']
        labels = {
            'gun': 'Gün',
            'saat': 'Saat',
            'islem_turu': 'İşlem Türü',
            'aciklama': 'Açıklama',
            'oteller': 'Otel',
            'otel_turu': 'Otel Türü',
            'turlar': 'Tur',
            'transferler': 'Transfer',
            'arac_tipi': 'Araç Tipi',
            'rehber': 'Rehber',
            'fiyat': 'Fiyat',
        }
        widgets = {
            'gun': forms.TextInput(attrs={'class': 'form-control'}),
            'saat': forms.TimeInput(attrs={'class': 'form-control'}),
            'islem_turu': forms.Select(attrs={'class': 'form-control'}),
            'aciklama': forms.TextInput(attrs={'class': 'form-control'}),
            'oteller': forms.Select(attrs={'class': 'form-control'}),
            'otel_turu': forms.Select(attrs={'class': 'form-control'}),
            'turlar': forms.Select(attrs={'class': 'form-control'}),
            'transferler': forms.Select(attrs={'class': 'form-control'}),
            'arac_tipi': forms.Select(attrs={'class': 'form-control'}),
            'rehber': forms.Select(attrs={'class': 'form-control'}),
            'fiyat': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SatisItemForm, self).__init__(*args, **kwargs)
        self.set_widgets()
    
    def save(self, commit=True):
        satis_item = super(SatisItemForm, self).save(commit=False)
        self.set_company_from_request(satis_item)
        if commit:
            satis_item.save()
        return satis_item



# Satis modeli için SatisItem formseti oluştur
SatisItemFormSet = inlineformset_factory(Satis, SatisItem, form=SatisItemForm, extra=30)


class YolcuBilgileriForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = YolcuBilgileri
        fields = ['musteri', 'pasaport']
        labels = {
            'musteri': 'Müşteri',
            'pasaport': 'Pasaport'
        }
        widgets = {
            'musteri': forms.Select(attrs={'class': 'form-control'}),
            'pasaport': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(YolcuBilgileriForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        yolcu_bilgisi = super(YolcuBilgileriForm, self).save(commit=False)
        self.set_company_from_request(yolcu_bilgisi)
        if commit:
            yolcu_bilgisi.save()
        return yolcu_bilgisi

class DigerYolcuBilgileriForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = DigerYolcuBilgileri
        fields = ['ad', 'soyad', 'tel', 'pasaport']
        labels = {
            'ad': 'Ad',
            'soyad': 'Soyad',
            'tel': 'Telefon',
            'pasaport': 'Pasaport'
        }
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
            'soyad': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'pasaport': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(DigerYolcuBilgileriForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        diger_yolcu_bilgisi = super(DigerYolcuBilgileriForm, self).save(commit=False)
        self.set_company_from_request(diger_yolcu_bilgisi)
        if commit:
            diger_yolcu_bilgisi.save()
        return diger_yolcu_bilgisi
    
    
class FiyatlandirmaForm(SetCompanyMixin, WidgetMixin,forms.ModelForm):
    class Meta:
        model = Fiyatlandırma
        fields = ['genel_toplam', 'arac_toplam', 'transfer_toplam', 'rehber_toplam', 'yemek_toplam', 'double_oda_toplam', 'single_oda_toplam']

    genel_toplam = forms.DecimalField(label='Genel Toplam', widget=forms.TextInput(attrs={'class': 'form-control'}))
    arac_toplam = forms.DecimalField(label='Araç Toplam', widget=forms.TextInput(attrs={'class': 'form-control'}))
    transfer_toplam = forms.DecimalField(label='Transfer Toplam', widget=forms.TextInput(attrs={'class': 'form-control'}))
    rehber_toplam = forms.DecimalField(label='Rehber Toplam', widget=forms.TextInput(attrs={'class': 'form-control'}))
    yemek_toplam = forms.DecimalField(label='Yemek Toplam', widget=forms.TextInput(attrs={'class': 'form-control'}))
    double_oda_toplam = forms.DecimalField(label='Double Oda Toplam', widget=forms.TextInput(attrs={'class': 'form-control'}))
    single_oda_toplam = forms.DecimalField(label='Single Oda Toplam', widget=forms.TextInput(attrs={'class': 'form-control'}))
        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FiyatlandirmaForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        fiyatlandirma = super(FiyatlandirmaForm, self).save(commit=False)
        self.set_company_from_request(fiyatlandirma)
        if commit:
            fiyatlandirma.save()
        return fiyatlandirma
from django import forms
from django.forms.widgets import TextInput

class FiyatlandirmaItemForm(SetCompanyMixin, WidgetMixin, forms.ModelForm):
    class Meta:
        model = FiyatlandirmaItem
        fields = ['tarih', 'aciklama', 'arac_fiyati', 'transfer_fiyati', 'rehber_fiyati', 'yemek_fiyati', 'double_oda_fiyati', 'single_oda_fiyati']
        labels = {
            'tarih': 'Tarih',
            'aciklama': 'Açıklama',
            'arac_fiyati': 'Araç Fiyatı',
            'transfer_fiyati': 'Transfer Fiyatı',
            'rehber_fiyati': 'Rehber Fiyatı',
            'yemek_fiyati': 'Yemek Fiyatı',
            'double_oda_fiyati': 'Double Oda Fiyatı',
            'single_oda_fiyati': 'Single Oda Fiyatı',
        }
        widgets = {
            'tarih': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'gg.aa.yyyy'}),
            'aciklama': forms.TextInput(attrs={'class': 'form-control'}),
            'arac_fiyati': forms.TextInput(attrs={'class': 'form-control'}),
            'transfer_fiyati': forms.TextInput(attrs={'class': 'form-control'}),
            'rehber_fiyati': forms.TextInput(attrs={'class': 'form-control'}),
            'yemek_fiyati': forms.TextInput(attrs={'class': 'form-control'}),
            'double_oda_fiyati': forms.TextInput(attrs={'class': 'form-control'}),
            'single_oda_fiyati': forms.TextInput(attrs={'class': 'form-control'}),
        }

        input_formats = {
            'tarih': ['%d.%m.%Y'],
        }

        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FiyatlandirmaItemForm, self).__init__(*args, **kwargs)
        self.set_widgets()

    def save(self, commit=True):
        fiyatlandirmaitem = super(FiyatlandirmaItemForm, self).save(commit=False)
        self.set_company_from_request(fiyatlandirmaitem)
        if commit:
            fiyatlandirmaitem.save()
        return fiyatlandirmaitem
    
# Satis modeli için SatisItem formseti oluştur
FiyatlandirmaItemFormSet = inlineformset_factory(Fiyatlandırma, FiyatlandirmaItem, form=FiyatlandirmaItemForm, extra=15)