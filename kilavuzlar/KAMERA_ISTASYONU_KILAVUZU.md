# 🎥 KAMERA İSTASYONU KILAVUZU

> Bu depoda kamera bir anlatım aracı değil, bir **sabittir.** `film_md` açı
> çeşitliliğini zorunlu kılar; burada tam tersi geçerlidir: kamera bir kez
> kurulur, bir daha dokunulmaz, ve sahneler arasında değişen tek şey zamandır.
>
> Bu kılavuz istasyonları tanımlar ve kadrajı **hesapla** kurar — göz kararıyla
> değil.

---

# 1. MİMARİ — HİBRİT (8 ana + 2 detay) ⭐ VARSAYILAN

```
S0  ANA      arsa · ilk kazı        ← loop buradan doğar
S1  ÇUKUR    kazı derinleşir
S2  ÇUKUR    iksa + donatı
S3  ANA      radye + bodrum
S4  ANA      çekirdek + vinç kurulur
S5  ANA      ilk katlar
S6  ANA      kış ① kar
S7  ANA      kış ② erime
S8  ANA      cephe
S9  ANA      ⭐ USTA KARE · teslim   ← S0 ile aynı kadraj, aynı saat, aynı ışık
KART         başlıklı kapak · SAHNE DEĞİL · S9'un karesinden türetilir
```

⭐ **DETAY = EK, AŞAMA DEĞİL [P2-e]:** detay istasyonu bir merdiven satırı
almaz; bir ana sahnenin içine ≤2 sn ek olarak girer, kanıt nesnesini
taşımaz. Doruk (kapanış · gömülme · teslim) HER ZAMAN ana istasyondadır ve
ana istasyon toplam sürenin ≥%85'idir. Aşağıdaki 8+2 şeması üst sınırdır.

**Neden 8+2:** 10 sahnede vantaj sayısını ARTIRMAK değil AZALTMAK gerekiyor.
v1'de üç vantaj vardı ve ① merceği filmi "ALTI AYRI GÖRÜNTÜ" saydı; en ağır
gerekçelerden biri, ikincil vantajlarda hiçbir çapanın görünmemesiydi
(① C3 0/10). Ne kadar çok vantaj, o kadar çok "aynı yer" kanıtı borcu.

```
⛔ DETAY İSTASYONUNUN ÜÇ KOŞULU — üçü de zorunlu [DERS 4 · ① C3]
   ① Arka plan çapalarından EN AZ BİRİ kadrajda GÖRÜNÜR ve isimlendirilmiştir.
      Görünmüyorsa istasyon kurulmaz — kadraj değiştirilir ya da sahne
      ana istasyona alınır.
   ② Detay istasyonu da SABİTTİR: kendi içinde kamera hiç hareket etmez.
   ③ Bir filmde EN FAZLA İKİ detay sahnesi olur ve ikisi de AYNI detay
      istasyonundandır. Üçüncü bir vantaj, timelapse kimliğini bozar.

⛔ VE DETAY KARELERİ DE ZİNCİRİN İÇİNDEN ÜRETİLİR [DERS 5]: ana istasyondaki
   aynı aşamanın onaylanmış karesi referans alınır, sıfırdan üretilmez.
```

# 2. İSTASYON TANIM SATIRI — her promptta birebir

```
Camera: MAIN STATION — fixed tripod bolted to the parapet of the building
across the street, lens 24.0 metres above street level, 72 metres from the
south face of the site, bearing 215°, tilt 0°, zero roll. The camera never
moves, never pans, never tilts, never zooms.
```

Altı alan zorunludur: **lens · yükseklik · mesafe · bakış açısı (derece) ·
tilt · roll.** Biri eksikse model onu her sahnede yeniden uydurur.

---

# 3. KADRAJ HESABI — göz kararı değil

Tam kare (full-frame) dikey çekimde kare yüksekliği 36 mm'dir. Bir noktanın
kare içindeki dikey yeri:

```
        kare yüzdesi(y) = %50 + f × (y − h) / (36 × D)

  f = odak uzaklığı (mm)      y = noktanın yerden yüksekliği (m)
  h = kamera yüksekliği (m)   D = kameradan yapıya yatay mesafe (m)
```

### Üç sonuç, doğrudan bu formülden

```
① UFUK ÇİZGİSİ tilt 0°'da HER ZAMAN tam %50'dedir.
   Bu bir kompozisyon tercihi değil, geometrinin sonucudur. Değişmezler
   tablosuna "%50" yazılır ve altı sahnede de aynıdır.

② TACIN YERİ:  taç %82'ye otursun istiyorsan  →  D = f × (H − h) / 11,5
   24 mm için sadeleşir:                          D = (H − h) / 0,48

③ TİLT VERİRSEN dikey çizgiler yakınsar (keystone). Gerçek şantiye
   kameralarının imzası tilt 0°'dır ve dikey çizgilerin dik kalmasıdır.
   ⛔ Tilt vermek yerine KAMERAYI YÜKSELT — aynı kadrajı keystone olmadan verir.
```

### Çalışılmış örnek — referans proje (18 katlı kule)

```
GİRDİLER      H = 58 m (yapı) · f = 24 mm · hedef taç %82
SEÇENEK A     h = 1,60 m (sokak seviyesi)  →  D = 56,4 / 0,48 = 117 m
              ⛔ şehir içinde 117 m'de araya başka bina girer — görüş yok
SEÇENEK B ⭐  h = 24 m (karşı bloğun çatısı) →  D = 34 / 0,48 = 71 m ≈ 72 m
              ✅ görüş açık · keystone yok · aşağıdaki üç bant temiz oturur

SONUÇ KADRAJI (h=24 · D=72 · f=24 · tilt 0°)
   taç        y=58  → %81,5
   ufuk               %50,0
   yapı tabanı y=0   → %27,8
   ────────────────────────────────────
   %82-100   gökyüzü                       ← üst 1/8 boş kalır ✅
   %28-82    YAPI                          ← kadrajın yarısından fazlası
   %25-28    şantiye zemini, makine, çamur
   %0-25     yakın çatı kenarı + sokak     ← platform arayüzü zaten kapatır ✅
```

⭐ **Alt %25'in arayüz tarafından kapatılması bir kayıp değil, bir armağandır:**
o banda yakın plan zemin ve sokak konur; hikâyeye ait hiçbir şey oraya düşmez
ve kadrajın geri kalanı tamamen yapıya kalır.

---

## ⭐ 3.1 GENİŞ SAHADA İKİ MESAFE — kenar ve eksen  [DERS 38]

```
§3'ün formülü doğrudur ve "D = kameradan YAPIYA mesafe" der. Çalışılmış
örnek TEK BİR KULEDİR; orada saha kenarı ile yapı ekseni aynı noktadır.
GENİŞ SAHADA (pad · kampüs · baraj · liman) bu iki mesafe AYRIŞIR.

THE DUST YEAR ölçüldü: "mesafe: pad'in güney kenarından 27,5 m" yazıldı ve
BÜTÜN yüzdeler bu D ile hesaplandı. Direk pad'in MERKEZİNDE duruyor: 42,5 m.
                    planda    D_eksen=42,5   fark
   direk tacı        %82,0       %70,7      11,3 puan
   pad yüzeyi        %30,6       %37,5       6,9
   berm tacı         %37,9       %42,2       4,3
COMPOSITION bloğu modele "the mast head at eighty-two percent" dedi —
beyan edilen istasyonun ÜRETEMEYECEĞİ bir sayı. Model ya istasyonu kaydırır
ya ölçeği bozar; ① STATION IDENTITY 0/10 ve ② SCALE LOCK 4/10 ile ikisi de oldu.

KURAL  Değişmezler tablosu İKİ mesafe beyan eder:
   D_kenar  kameradan sahanın YAKIN kenarına — güvenli alanı bu belirler
   D_eksen  kameradan YAPI EKSENİNE — BÜTÜN yükseklik yüzdeleri yalnız bundan

⭐ ALT ÇEYREK EŞİĞİ de buradan hesaplanır ve Değişmezler'e yazılır:
      D_alt = f × h / (36 × 0,25)      24 mm · h=8,0 m → 21,3 m
   Bundan yakın her şey kadrajın alt %25'indedir. THE DUST YEAR'ın pad
   kenarı 27,5 m — sınırın yalnız 6,2 m ötesinde; ① SAFE AREA 0/10 geldi.
```

# 4. İSTASYON KARTLARI

## 4.1 ANA İSTASYON
```
LENS       24 mm küresel · f/8 · ISO 100 · tilt 0°
YÜKSEKLİK  hesaptan (§3) — tercihen karşı yapının çatısı/parapeti
GÖREV      S0 · S3 · S4 · S5 · kapak · LOOP
KURAL      Bu istasyonun altı alanı bir kez yazılır ve dört sahnede
           TEK KELİMESİ değişmeden tekrarlanır.
```

## 4.2 ÇUKUR İSTASYONU (S1)
```
LENS       35 mm · f/8 · tilt 8° aşağı
KONUM      çukurun kenarında, korkuluğa sabitlenmiş, yerden 1,50 m
GÖREV      kazının DERİNLİĞİNİ göstermek — ana istasyondan görülmeyen tek şey
ÇAPA       arka plan çapalarından ⭐en az biri kadrajın üstünde görünür
KURAL      derinlik bir SAYIYA bağlanır: "the pit floor is four storeys below
           street level, the excavator at the bottom reads as a small shape"
```

## 4.3 VİNÇ İSTASYONU (S2)
```
LENS       50 mm · f/5.6 · tilt 0°
KONUM      vincin dibinden 40 m, mast tabanı kadrajda
GÖREV      ÖLÇEK — vincin ve ilk katların insana göre büyüklüğü
ÇAPA       komşu bina cephesi kadrajın kenarında
KURAL      yük yolu görünür: kanca → halat → araba → bom → mast → beton kaide.
           Model vinci havada asılı bırakmaya yatkındır (§NEGATİF vinç bloğu)
```

---

# 5. LENS KİLİDİ

```
24 mm   ANA istasyon — geniş, yapının tamamı, keystone'suz
35 mm   ÇUKUR — orta, derinlik
50 mm   VİNÇ / detay — sıkıştırılmış ölçek
⛔ 3 lensten fazlası kullanılmaz. Anamorfik YASAK (yatay parlama gündüz
   belgesel görüntüsünde optik bir yalandır).
⛔ Zoom, dolly, gimbal, drone hareketi: hiçbir sahnede yok. Drone KARE olarak
   kullanılabilir (sabit hover) ama HAREKET olarak kullanılamaz.
```

---

# 6. GÜVENLİ ALAN — 1080×1920

```
ÜST   ilk 200-254 px   sekmeler, profil          → yapının TACI buraya girmez
ALT   son 484 px       açıklama, müzik, CTA      → y=1436 altı GÖRÜNMEZ
SAĞ   son 242 px       beğen / paylaş / yorum    → kanıt nesnesi buraya girmez
SOL   ilk 122 px

COMPOSITION satırına yazılacak cümle:
"the crown of the structure sits below the top eighth of the frame and the
working level sits above the bottom quarter of the frame; nothing that proves
progress falls into the right eighth of the frame."
```
