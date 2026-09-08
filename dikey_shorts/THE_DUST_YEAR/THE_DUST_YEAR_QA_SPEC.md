# 🔍 THE DUST YEAR — QA SPEC

> ⛔ **BU SPEC ÜRETİMDEN ÖNCE YAZILDI.** Buradaki her kilit, plandaki on
> görsel ve on I2V promptunun içinde İngilizce olarak YAZILIDIR. Ölçülmemiş
> olanlar §7'de açıkça AÇIK durur.
>
> ⭐ VE BELGE YETMEZ [DERS 27 · 29]: her mercek koşusundan ÖNCE tek satır
> yazılır ve raporun başına yapıştırılır: `verilen girdiler: <dosya adları>`.
> Koşu `araclar/qa_paket.sh` ile PAKETLENİR [DERS 29].

---

## 0. KÜNYE

```
FİLM          THE DUST YEAR
FORMAT        9:16 dikey · 10 sahne = 60,0 sn
              (6,0 · 4,0 · 8,0 · 4,0 · 6,0 · 4,0 · 10,0 · 4,0 · 6,0 · 8,0 — hedef)
KAPAK KARTI   5,0 sn · SAHNE DEĞİL · SON 5 sn · S9'un 0:59,0 karesinden türer
TOPLAM        65,0 sn
YAPI          Mars robotik yüzey üssü · habitat Ø8,0×6,4 m + 3,0 m regolit berm
              + Ø30,0 m sinter pad + 21,2 m direk (6×3,2 m) + Ø1,6 m çanak
              + fisyon ünitesi Ø2,2 m + 4 radyatör 2,4×4,0 m + 2×6 güneş paneli
SAHA          🔴 Mars · düz toz ovası · 40°K · SAHA KARTI YOK (§7)
ZAMAN YAYI    667 sol ≈ 685 Dünya günü ≈ 1,00 Mars yılı · Ls 20 → Ls 19
              ⭐ MEVSİM VAR: Mars eksen eğikliği 25,19°, Dünya'nınkine yakın
KAMERA        tek istasyon — ANA (10 sahnenin 10'u) · detay istasyonu YOK
              h 8,0 m · D 27,5 m · bearing 348° · tilt 0° · roll 0°
              ⛔ D hesaptan çıktı: (21,2 − 8,0) / 0,48 = 27,5 m
ÜRETİM SIRASI ⛔ TERS: S9 usta kare → S8 → … → S0
              her kareden sonra zincir_kontrol.sh + KAYA elle doğrulanır
KAPI          python3 araclar/prompt_kontrol.py → ⚠️ FIX (tek madde: kutu seti)
⛔ ARAÇ KAPISI KOŞULMADI [DERS 23 · ARAC_KARTLARI §4]. Kutu seti bilinmiyor;
   S6 (10,0 sn) ve S2/S9 (8,0 sn) tek klipte üretilebilir mi BİLİNMİYOR.
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S9
SANİYE      0:59,6   (S9 klibinin son 0,4 saniyesi · sahne bloğu 0:52,0–1:00,0)
GÖRÜLMESİ GEREKEN ŞEY — ALTISININ ALTISI birden:
   ① KAPALI BERM: habitatın çevresinde kesintisiz regolit torba halkası,
      tacı yarık tepeli kayanın tepesinden 0,6 m YUKARIDA. Halkada açık
      çeyrek YOK.
   ② TAM DİREK: ALTI bölüm sayılabiliyor, taç kadrajın %82'sinde, ÜÇ gergi
      teli DÜMDÜZ ve gergin, çanak BEŞİNCİ bölümde. İskele YOK.
   ③ DÖRT RADYATÖR tek sırada ayakta, fisyon ünitesinde SAPAN YOK.
   ④ ⭐ BEDEL ①: İKİ güneş dizisi hâlâ habitatın 9,0 m batısında, altışar
      panel, hepsi GRİ — bir yıllık toz altında, açıldıkları yerde, ölü.
      ⛔ Sökülmüş, temizlenmiş ya da kadraj dışına alınmış OLMAMALI.
   ⑤ ⭐ BEDEL ②: 17,0 m'lik ödünç çukuru hâlâ açık, basamakları tozla
      dolmuş; pad ile çukur arasında BİR YILLIK tek geniş cilalı iz yolu.
      S0'da izsiz olan ovada temiz alan kalmamış.
   ⑥ IŞIK S0 İLE AYNI: azimut 125° · yükselti 44° (S0: 124° · 45°).
      Kayanın gölgesi sola, güneş diski kadrajda YOK.

KOMUT
   ffmpeg -y -sseof -5.4 -i teslim.mp4 -frames:v 1 kanit.jpg
   ⭐ Kare TESLİM dosyasından alınır, üretilen klipten DEĞİL — kırpma
     kareleri kaydırır [KURGU_VE_TESLIM §2].
⛔ Altısından biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
```

---

## 2. KADRAJ KİLİTLERİ — ANA istasyon (10 sahnenin 10'u)

```
ufuk           kare yüksekliğinin tam %50'sinde, ON karede de
pad zemini     %30,6
berm tacı      %37,9 (tamamlandığında)
habitat tepesi %46,1
3. direk flanşı %58,7   ·  5. flanş %74,2  ·  direk tacı %82,0
kadraj         23,2 m genişlik × 41,2 m yükseklik · 46,5 px/m
güvenli alan   ilerlemeyi kanıtlayan hiçbir şey sağ 1/8'e ve alt 1/4'e düşmez

⭐ OKUNABİLİRLİK EŞİĞİ 0,5 m = 23 px [INSAAT_YONTEMI §1]
   Kontrol: promptlarda 0,5 m'den küçük hiçbir nesne adı GEÇMEMELİ.
   (prompt_kontrol.py bunu FIX olarak arar)

KAMERA KİLİDİ ÖLÇÜLEBİLİR YAZILDI [DERS 6]:
   "The split-top boulder occupies exactly the same width of the frame at
    both ends of the shot ... the horizon stays at exactly half the frame
    height throughout."
   ⛔ Ölçüm: ilk ve son karede kayanın piksel genişliği. Fark > 2 px ise
      kamera kilidi DÜŞTÜ ve klip atılır [ARAC_KARTLARI §4 ölçüm 2].
```

---

## 3. DEĞİŞMEZLİK KİLİTLERİ — sahneler arası

```
ARKA PLAN ÇAPALARI — üçü de ON karede aynı yerde, aynı boyutta:
   ① yarık tepeli kaya · 2,4 m · pad kenarından 6,0 m doğuda · 112 px
   ② sığ krater · Ø40 m · kenarı ovadan 1,8 m yüksek · iç kuzey yüzü gölgede
   ③ ufuk sırtı · profilinde TEK kare basamak · soldan 1/3 içeride

⭐ ⑤ "AYNI YER" NESNESİ: yarık tepeli kaya.
   ⛔ ÜRETİM KAPISI [DERS 25]: her zincir_kontrol koşusunda iki karede de
      AYNI YERDE olduğu ELLE doğrulanır. Kaybolduysa kare ATILIR — betik
      geçse bile. MOUNTAIN DOOR'da nesne beş prompta da yazılmıştı ve İLK
      dikişte kayboldu.

YAPI BIBLE — on promptta BİREBİR aynı kelimeler (prompt_kontrol denetler)
SITE / BACKGROUND — on promptta BİREBİR aynı kelimeler

MONOTON BÜYÜME — geri alınan tek şey GEÇİCİ EKİPMANDIR ve §6'da takvimlidir:
   ⛔ pad küçülemez · berm alçalamaz · direk bölüm kaybedemez ·
      panel sayısı azalamaz · çukur kapanamaz
```

---

## 4. GÜNEŞ SAATİ KİLİDİ — Mars 40°K

```
Mars sol 24 sa 39 dk 35 sn · saat açısı 14,599°/sa · eğiklik 25,19°
⛔ DÜNYA SAYISI KULLANILMADI.

S0 az 124° yük 45° | S1 123/56 | S2 125/65 | S3 137/70 | S4 134/61
S5 136/46 | S6 162/36 | S7 158/23 | S8 151/21 | S9 125/44

KİLİTLER
 · Azimut bandı 123°-162°, kamera bakışı 348° → GÜNEŞ HER SAHNEDE KAMERANIN
   ARKASINDA. Disk hiçbir karede kadrajda GÖRÜNMEZ [DERS 32].
   ⛔ Ölçüm: on klibin hiçbirinde parlak disk aranır; bulunursa klip atılır.
 · Mevsim TEK YÖNDE: Ls 20 → 45 → 70 → 100 → 135 → 170 → 210 → 250 → 290 → 19
 · Yükselti yayı: 45 → 70 (yaz doruğu) → 21 (kış dibi) → 44 (döngü kapanır)
 · S8 yılın en uzun gölgesi: 1 m çubuk → 2,63 m gölge
 · S3 yılın en kısası: 1 m → 0,35 m
 · ⛔ S6'DA GÖLGE YOK: toz fırtınası ışığı düzleştirir. O sahnede gölge
   ARANMAZ; zamanın taşıyıcısı BİRİKEN TOZDUR. Bu bir kusur değil, fiziktir.
```

---

## 5. SIKIŞTIRMA REJİMİ KİLİDİ ⭐ yeni [SANTIYE_HAREKETI §1-2]

```
S0 B · S1 B · S2 B · S3 A · S4 B · S5 B · S6 C · S7 B · S8 B · S9 B

REJİM A (10 dk · 100×)   S3 — makineler MAKİNE olarak tanınır, gölge ~5° döner
REJİM B (2 saat · 1200×) sekiz sahne — gölge 25°-50° süpürür, makineler bulanık
REJİM C (iş günü · 5400×) S6 — hiçbir araç görünecek kadar durmaz, iş YÜZEYLE
                          kanıtlanır: biriken toz, dolan izler, yükselen halka

⛔ KİLİT: bir klipte gök, gölge, toz ve makine AYNI SAATE tabidir.
   Ölçüm: gökyüzü hızlı akarken makine gerçek zamanda yürüyorsa ③ TIME RATE
   düşer ve klip atılır [DERS 15 · A6-a].
⛔ REJİM C'DE İNSAN İSTENMEZ — zaten insansız film. prompt_kontrol bunu
   BLOCK olarak arar.
```

---

## 6. ARA HÂL VE SÖKÜM TAKVİMİ ⭐ [INSAAT_YONTEMI §2]

```
⑧ YÖNTEM MERCEĞİ DOKUZ ELEMANI TEK TEK İZLER. Her biri EN AZ BİR ara hâlde
görünmelidir; hiçbiri tamamlanmış doğmamalıdır.

eleman              ara hâl sahneleri          geçici ekipman kanıtı
──────────────────────────────────────────────────────────────────────
① çalışma pad'i     S0 %25 · S1 %50 · S2 %75   bıçak izi · spoil ridge · akkor kenar
② güneş dizisi      S1 %50 · S2 %75            yarı açık paneller
③ ödünç çukuru      S2 %25 · S5 %50 · S6 %75   basamaklı duvar · spoil yığını
④ habitat           S3 %50 · S4 %75            KIZAK + derin gevşek kırışıklıklar
⑤ regolit berm      S4 %25 · S5 %50 · S6 %75   istiflenmemiş torba yığını
⑥ fisyon ünitesi    S7 %50 · S8 %75            KALDIRMA SAPANI takılı
⑦ radyatör          S7 %25 · S8 %75            paletten kalkan panel
⑧ direk             S8 %50 · S9 %75            İSKELE + gevşek gergi telleri
⑨ çanak             S9 %50→%75                 boş kelepçe → asılı → bağlı

SÖKÜM TAKVİMİ — hiçbiri kendiliğinden kaybolmaz, her biri I2V'de FİİL alır
   habitat kızağı  S3 kurulur → S4 SÖKÜLÜR, pad'e düz istiflenir
   kaldırma sapanı S7 takılır → S8 SÖKÜLÜR
   direk iskelesi  S8 kurulur → S9 SÖKÜLÜR
   ⛔ SÖKÜLMEYENLER (bunlar BEDEL'dir, kaybolurlarsa film yalan söyler):
      ödünç çukuru  S2 açılır → S9'da hâlâ 17,0 m, tozla dolu
      güneş dizisi  S1 açılır → S6 gömülür → S9'da hâlâ orada, gri, ölü
```

---

## 7. ⛔ BU SPEC'İN KENDİ AÇIKLARI — üretimden önce bilinen

```
① ARAÇ KUTU SETİ ÖLÇÜLMEDİ. En uzun sahne 10,0 sn. Kutu {4,6,8} çıkarsa
   tavan 7,00 sn olur ve S6 · S2 · S9 tek klipte üretilemez [A7-b].
   → Üretim günlüğü §0 doldurulmadan tek kare üretilmez.

② MARS SAHA KARTI YOK. SAHA_VE_IKLIM_KARTLARI'nda Mars kartı bulunmuyor;
   bu filmin saha bilgisi doğrudan planın §2 ve §4'ünde duruyor. İlk
   üretimden sonra kart yazılır ya da yazılmaz — ölçüm karar verir.

③ MARS FOTOĞRAFİK KORPUSU İDDİA EDİLDİ, ÖLÇÜLMEDİ [DERS 34].
   "hard-mounted engineering camera" cümlesi kondu ama bu deponun hiçbir
   filminde ölçülmedi. ① SURFACE TRUTH'tan okunacak ilk şey budur.

④ TOZ FIRTINASI SAHNESİNDE ⑦ İŞ RİSKİ. S6 rejim C'dir ve hiçbir makine
   görünmez. ⑦ merceği bunu "işsiz aralık" sayarsa hüküm PARKED'a yaklaşır.
   ⭐ Karşı kanıt promptta yazılı: yükselen halka + dolan izler + kalınlaşan
      toz katmanı. Bu üçü YETMEZSE bulgu DERS olur.

⑤ REJİM KAVRAMI HİÇ ÖLÇÜLMEDİ. SANITYE_HAREKETI_KILAVUZU 08.09.2026'da
   yazıldı ve bu ONU KULLANAN İLK FİLM. A · B · C ayrımının modelde bir
   karşılığı olup olmadığı bilinmiyor.

⑥ MARS GÖLGE HESABI BU DEPODA YAPILDI, DOĞRULANMADI. 25,19° eğiklik ve
   14,599°/sa saat açısıyla hesaplandı; bağımsız bir efemerise karşı
   denetlenmedi.
```

---

## 8. KOŞULACAK MERCEKLER

```
⛔ HEPSİ qa_paket.sh ile koşar; üretim günlüğü yoksa paket AÇILMAZ [DERS 28].
⛔ Her koşunun başına: "verilen girdiler: <dosya adları>" [DERS 27].

① KARE        mod V   ⭐ SURFACE TRUTH ve PEOPLE burada okunur (film insansız
                      beyanlıdır; PEOPLE 0 bir KUSUR DEĞİL, beyanın teyididir)
② İNŞA        mod D   SPEC §3 · §6 verilir
③ ZAMAN       mod V   TAM KURGU · ⭐ rejim tutarlılığı burada ölçülür
④ TESLİM      mod D   plan §0 (VAAT/DİRENÇ/BEDEL) verilir
⑤ DEVAMLILIK  mod V   ⭐ "aynı yer" nesnesi: yarık tepeli kaya
⑥ GEÇİŞ       mod D   plan §3 SÜRE sütunu verilir + kesme_kontrol.sh çıktısı
⑦ İŞ          mod V   ⭐ S6 burada sınanır (§7 madde ④)
⑧ YÖNTEM      mod D   SPEC §6 ara hâl tablosu verilir — dokuz eleman tek tek
```
