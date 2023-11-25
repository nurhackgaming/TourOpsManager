from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User

class Sirket(models.Model):
    adi = models.CharField(max_length=100, verbose_name="Şirket")
    is_active = models.BooleanField(default=False)
    baslangic_tarihi = models.DateTimeField(verbose_name="Başlangıç Tarihi", blank=True, null=True)
    bitis_tarihi = models.DateTimeField(verbose_name="Bitiş Tarihi", blank=True, null=True)
    
    def __str__(self):
        return self.adi
    
    class Meta:
        verbose_name = "Şirket"
        verbose_name_plural = "Şirketler"

class Departman(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    adi = models.CharField(max_length=100, verbose_name="Departman")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Departman"
        verbose_name_plural = "Departmanlar"

class Personel(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departman = models.ForeignKey(Departman, on_delete=models.SET_NULL, null=True, verbose_name="Departman")
    is_ceo = models.BooleanField(verbose_name="Yetkili mi?", default=False)
    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username

    class Meta:
        verbose_name = "Personel"
        verbose_name_plural = "Personeller"

class Musteri(models.Model):
    MUSTERI_TIPLERI = [
        ('Xiaohongshu', 'Xiaohongshu'),
        ('Ctrip', 'Ctrip'),
        ('Bireysel', 'Bireysel'),
        ('Acenta', 'Acenta'),
        ('Surekli Acenta', 'Sürekli Acenta'),
    ]
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    ad = models.CharField(max_length=100, verbose_name="Ad")
    soyad = models.CharField(max_length=100, verbose_name="Soyad")
    tel = models.CharField(max_length=15, verbose_name="Telefon")
    mail = models.EmailField(verbose_name="E-posta")
    musteri_tipi = models.CharField(max_length=20, choices=MUSTERI_TIPLERI, verbose_name="Müşteri Tipi", default="Acenta")

    def __str__(self):
        return f"{self.ad} {self.soyad}"

    class Meta:
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"

class YolcuBilgileri(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    musteri = models.ForeignKey(Musteri, verbose_name="Müşteriler", on_delete=models.CASCADE)
    pasaport = models.CharField(verbose_name="Pasaport", max_length=75)

    def __str__(self):
        return f"{self.musteri.ad} {self.musteri.soyad} - {self.pasaport}"

    class Meta:
        verbose_name = "Yolcu Bilgisi"
        verbose_name_plural = "Yolcu Bilgileri"
        
class DigerYolcuBilgileri(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    ad = models.CharField(max_length=100, verbose_name="Ad")
    soyad = models.CharField(max_length=100, verbose_name="Soyad")
    tel = models.CharField(max_length=15, verbose_name="Telefon")
    pasaport = models.CharField(verbose_name="Pasaport", max_length=75)
    
    def __str__(self):
        return f"{self.ad} {self.soyad} - {self.pasaport}"
    
    class Meta:
        verbose_name = "Diğer Yolcu Bilgisi"
        verbose_name_plural = "Diğer Yolcu Bilgileri"

class AracTipi(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    adi = models.CharField(max_length=100, verbose_name="Adı")
    kapasite = models.IntegerField(verbose_name="Kapasite")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Araç Tipi"
        verbose_name_plural = "Araç Tipleri"

class SabitGider(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    adi = models.CharField(max_length=100, verbose_name="Adı")
    fiyati = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyatı")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Sabit Gider"
        verbose_name_plural = "Sabit Giderler"

class Il(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    adi = models.CharField(max_length=100, verbose_name="Adı")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "İl"
        verbose_name_plural = "İller"

class Rehber(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    il = models.ForeignKey(Il, on_delete=models.CASCADE, verbose_name="İl")
    adi = models.CharField(max_length=100, verbose_name="Adı")
    ucreti = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ücreti")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Rehber"
        verbose_name_plural = "Rehberler"

class Lokasyon(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    il = models.ForeignKey(Il, on_delete=models.CASCADE, verbose_name="İl")
    adi = models.CharField(max_length=100, verbose_name="Adı")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Lokasyon"
        verbose_name_plural = "Lokasyonlar"

class Otel(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    lokasyon = models.ForeignKey(Lokasyon, on_delete=models.CASCADE, verbose_name="Lokasyon")
    adi = models.CharField(max_length=100, verbose_name="Adı")
    tek_kisilik_oda_ucreti = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Tek Kişilik Oda Ücreti")
    cift_kisilik_oda_ucreti = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Çift Kişilik Oda Ücreti")
    yildiz_sayisi = models.IntegerField(verbose_name="Yıldız Sayısı")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Otel"
        verbose_name_plural = "Oteller"

class Tur(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    lokasyon = models.ForeignKey(Lokasyon, on_delete=models.CASCADE, verbose_name="Lokasyon")
    adi = models.CharField(max_length=100, verbose_name="Adı")
    aciklama = models.TextField(verbose_name="Açıklama")
    fiyati = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyatı")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Tur"
        verbose_name_plural = "Turlar"

class Transfer(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    guzergah = models.CharField(max_length=100, verbose_name="Güzergah")
    fiyat_5_koltuk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Fiyat (5 Koltuk)")
    fiyat_7_koltuk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Fiyat (7 Koltuk)")
    fiyat_9_koltuk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Fiyat (9 Koltuk)")
    fiyat_12_koltuk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Fiyat (12 Koltuk)")
    fiyat_15_koltuk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Fiyat (15 Koltuk)")
    fiyat_16_20_koltuk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Fiyat (16-20 Koltuk)")

    def __str__(self):
        return f"{self.guzergah}"

    class Meta:
        verbose_name = "Transfer"
        verbose_name_plural = "Transferler"

class Satis(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    satici_personel = models.ForeignKey(Personel, on_delete=models.CASCADE, verbose_name="Satıcı Personel")
    alici_musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, verbose_name="Alıcı Müşteri")
    sabit_giderler = models.ManyToManyField(SabitGider, blank=True, verbose_name="Sabit Giderler")
    yolcu = models.ForeignKey(YolcuBilgileri, on_delete=models.CASCADE, verbose_name="Yolcu Bilgisi", blank=True, null=True)
    digeryolcular = models.ManyToManyField(DigerYolcuBilgileri, verbose_name="Diğer Yolcu Bilgileri", blank=True, null=True)
    baslangic_tarihi = models.DateTimeField(verbose_name="Başlangıç Tarihi", blank=True, null=True)
    bitis_tarihi = models.DateTimeField(verbose_name="Bitiş Tarihi", blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Toplam Fiyat")
    satildi = models.BooleanField(verbose_name="Satıldı mı?", default=False)
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs)
        self.calculate_total_price()
        super().save(*args, **kwargs)  # Toplam fiyatı güncelleyerek tekrar kaydet

    def calculate_total_price(self):
        total = 0
        for item in self.satisitem_set.all():
            total += item.fiyat

        for gider in self.sabit_giderler.all():
            total += gider.fiyati
            
        self.total_price = total

        
        


    def __str__(self):
        return f"{self.satici_personel} - {self.alici_musteri}"

    class Meta:
        verbose_name = "Satış"
        verbose_name_plural = "Satışlar"

class SatisItem(models.Model):
    ISLEM_TURLERI = [
        ('Karşılama', 'Karşılama'),
        ('Araç', 'Araç'),
        ('Tur', 'Tur'),
        ('Uğurlama', 'Uğurlama'),
        ('Serbest Zaman', 'Serbest Zaman'),
        ('Aktivite', 'Aktivite'),
        ('Çince Şoför', 'Çince Şoför'),
        ('Tercüman', 'Tercüman'),
    ]
    ODA_TURLERI = [
        ('Tek', 'Tek'),
        ('Çift', 'Çift'),
    ]
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE)
    satis = models.ForeignKey(Satis, on_delete=models.CASCADE, verbose_name="Satış")
    gun = models.CharField(max_length=3, verbose_name="Gün", blank=True, null=True)
    saat = models.TimeField(null=True, blank=True, verbose_name="Saat")
    islem_turu = models.CharField(max_length=50, choices=ISLEM_TURLERI, verbose_name="İşlem Türü")
    aciklama = models.CharField(max_length=250, blank=True, null=True, verbose_name="Açıklama")
    oteller = models.ForeignKey(Otel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Otel")
    otel_turu = models.CharField(max_length=50, choices=ODA_TURLERI, default="Tek", verbose_name="Otel Türü")
    turlar = models.ForeignKey(Tur, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tur")
    transferler = models.ForeignKey(Transfer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Transfer")
    arac_tipi = models.ForeignKey(AracTipi, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Araç Tipi")
    rehber = models.ForeignKey(Rehber, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Rehber", default=None)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Fiyat")

    def save(self, *args, **kwargs):
        self.calculate_price()  # Fiyatı hesapla
        super().save(*args, **kwargs)  # SatisItem nesnesini kaydet

        if self.satis_id:  # Satis modelinin kaydedilmiş olduğundan emin ol
            self.satis.calculate_total_price()  # İlişkili Satis nesnesinin total_price'ını hesapla
            self.satis.save()  # İlişkili Satis nesnesini güncelle

    def calculate_price(self):
        self.fiyat = 0  # Başlangıçta fiyatı sıfırla

        # Otel fiyatını ekle
        if self.oteller:
            if self.otel_turu == 'Tek':
                self.fiyat += self.oteller.tek_kisilik_oda_ucreti
            elif self.otel_turu == 'Çift':
                self.fiyat += self.oteller.cift_kisilik_oda_ucreti

        # Tur fiyatını ekle
        if self.turlar:
            self.fiyat += self.turlar.fiyati

        # Rehber ücretini ekle
        if self.rehber:
            self.fiyat += self.rehber.ucreti

        # Transfer fiyatını ekle
        if self.transferler and self.arac_tipi:
            # Arac tipine göre transfer fiyatını hesapla
            if self.arac_tipi.kapasite == 5:
                self.fiyat += self.transferler.fiyat_5_koltuk
            elif self.arac_tipi.kapasite == 7:
                self.fiyat += self.transferler.fiyat_7_koltuk
            elif self.arac_tipi.kapasite == 9:
                self.fiyat += self.transferler.fiyat_9_koltuk
            elif self.arac_tipi.kapasite == 12:
                self.fiyat += self.transferler.fiyat_12_koltuk
            elif self.arac_tipi.kapasite == 15:
                self.fiyat += self.transferler.fiyat_15_koltuk
            elif self.arac_tipi.kapasite == 20:
                self.fiyat += self.transferler.fiyat_16_20_koltuk
            # ... [diğer araç kapasiteleri için benzer ifadeler] ...
            else:
                print("Uygun araç tipi fiyatı bulunamadı.")
                
        if self.satis.alici_musteri and self.satis.alici_musteri.musteri_tipi:
            # Müşteri tipine göre çarpan
            multiplier_dict = {
                "Bireysel": Decimal('1.3'),
                "Xiaohongshu": Decimal('1.3'),
                "Ctrip": Decimal('1.3'),
                "Acenta": Decimal('1.2'),
                "Surekli Acenta": Decimal('1.1'),
            }
            multiplier = multiplier_dict.get(self.satis.alici_musteri.musteri_tipi, Decimal('1'))
            self.fiyat = self.fiyat * multiplier

    def __str__(self):
        return f"{self.satis} - {self.islem_turu}"

    class Meta:
        verbose_name = "Satış İtem"
        verbose_name_plural = "Satış İtemler"
        
class Fiyatlandırma(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE, blank=True, null=True)
    olusturan = models.ForeignKey(Personel, verbose_name="Personel", on_delete=models.CASCADE, blank=True, null=True)
    genel_toplam = models.DecimalField(verbose_name="Genel Toplam Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    arac_toplam = models.DecimalField(verbose_name="Araç Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    transfer_toplam = models.DecimalField(verbose_name="Transfer Toplam Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    rehber_toplam = models.DecimalField(verbose_name="Rehber Toplam Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    yemek_toplam = models.DecimalField(verbose_name="Yemek Toplam Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    double_oda_toplam = models.DecimalField(verbose_name="Double Oda Toplam Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    single_oda_toplam = models.DecimalField(verbose_name="Single Oda Toplam Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return f"{self.olusturan.user.get_full_name()} - {self.genel_toplam}"

    class Meta:
        verbose_name = "Fiyatlandırma"
        verbose_name_plural = "Fiyatlandırmalar"
        
class FiyatlandirmaItem(models.Model):
    sirket = models.ForeignKey(Sirket, verbose_name="Şirket", on_delete=models.CASCADE, blank=True, null=True)
    fiyat = models.ForeignKey(Fiyatlandırma, verbose_name="Fiyatlandırma", on_delete=models.CASCADE)
    tarih = models.DateField(verbose_name="Tarih", blank=True, null=True)
    aciklama = models.CharField(verbose_name="Açıklama", max_length=50, blank=True, null=True)
    arac_fiyati = models.DecimalField(verbose_name="Araç Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    transfer_fiyati = models.DecimalField(verbose_name="Transfer Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    rehber_fiyati = models.DecimalField(verbose_name="Rehber Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    yemek_fiyati = models.DecimalField(verbose_name="Yemek Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    double_oda_fiyati = models.DecimalField(verbose_name="Double Oda Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    single_oda_fiyati = models.DecimalField(verbose_name="Single Oda Fiyatı", max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f"{self.fiyat.olusturan.user.get_full_name()} - {self.tarih}"

    class Meta:
        verbose_name = "Fiyatlandırma Item"
        verbose_name_plural = "Fiyatlandırma Itemleri"