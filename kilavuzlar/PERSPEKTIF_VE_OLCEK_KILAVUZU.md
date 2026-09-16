# 📐 PERSPEKTİF VE ÖLÇEK KILAVUZU — modelin geometriyi TUTMASINI sağlamak

> **Tek soru:** Ölçek sahneden sahneye ve klip içinde aynı mı?
> **Sahibi olduğu blok:** `COMPOSITION` (görsel prompt) — yüzdeler yazılıyordu,
> ölçeği TUTAN referans nesnesi sistemi yoktu.
>
> ⛔ **Kaynak:** `arastirma/SONUCLAR/A11_GEMINI_HAM.md` · denetim `A9-A12_DENETIM.md`
> · dersler `DERSLER.md` A11-a…l · DERS 5 · 6 · 19 · 23 · 38 · P2-b · A3-b/c/d.
> **KAYNAK ✅** = DOI çekildi ve iddiaya ait; **ÖLÇTÜM** = burada hesaplandı;
> **VARSAYIM** = rapordan, atfı yanlış ya da yok.
>
> **Sınır — ⚠️ en riskli örtüşme:** KAMERA_ISTASYONU = KAMERANIN SAYILARI
> (h · D · f · tilt → kare yüzdesi formülü, istasyon kartları, lens kilidi,
> güvenli alan). Burası = MODELİN o geometriyi TUTMASI: referans nesne defteri,
> kesir cümlesi, sayı testi, zincirde kayma ve kanal. Ufuk %50 kuralı
> KAMERA §3'te kalır; burası ona atıf verir, tekrar etmez.

---

# 0. NEDEN BU KILAVUZ VAR — ölçülmüş arıza

```
① STATION IDENTITY 0/10   "the horizon sits at roughly 58% of the frame, but
                            shifts to 68% at 0:18"
② SCALE LOCK               0 · 4 · 7/10 — beş filmde yapı boyutu değişti
DERS 19 (kontrol grubu)    SAYILI çapa ("exactly three rooftop chimneys") 10/10 ·
                           SAYISIZ bible ("regular structural bays") 2/10 — aynı film
DERS 23                    aynı kamera cümlesi bir araçta 10/10, başkasında 0/10

⭐ Raporun teşhisi (A11 "çelişenler"): prompta "24 mm · 40 m · tilt 0°" yazmak
   kamerayı KİLİTLEMEZ — model bu sayıları metrik vektör değil, semantik
   token olarak işler ("24 mm hissi"). Kilit ya REFERANS NESNEDE ya GEOMETRİ
   KANALINDA yaşar [DERS 23 · A3-d ile aynı]. Kamera satırı yine yazılır
   (kapı arar); ölçeği tutan şey o satır değildir.
```

---

# 1. REFERANS NESNE DEFTERİ — saha başına, pikselle  [A11-a ÖLÇTÜM · A11-b]

```
Kadraj 33,75 × 60,0 m · 1080 × 1920 · 32 px/m  (KAMERA §3 ile aynı geometri)

ÖLÇEK REFERANSI OLABİLEN — film boyunca değişmeyen, yapı dışı, her karede görünür
  saha        nesne                                  boyut      px      kadraj genişliğine oranı
  şehir içi   komşu binanın pencere sövesi           1,5 m      48      1/22
              komşu bina cephesi (tam)               12 m       384     1/2,8
  kırsal      olgun ağaç GÖVDESİ (yaprak hariç)      1,0 m      32      1/34
  kıyı        fener taş kaidesi / mendirek ucu        5,0 m      160     1/6,7
  dağ         buzul taşı (erratic boulder)           3,0 m      96      1/11
  çöl         mesa sırtı (yükseklik farkı)           15 m       480     —  (dikey)
  Ay / Mars   krater kenarı (derinlik)               10 m       320     —  (dikey)
  buzul       ana kaya çıkıntısı (nunatak)           4,0 m      128     1/8,4
  HEPSİ       UFUK ÇİZGİSİ                            —          —      yükseklik %50 (tilt 0°) [KAMERA §3]

⛔ ÖLÇEK REFERANSI OLAMAYAN [A11-b]
  yapının kendisi (büyür) · kule vinç (mast eklenir, döner) · iskele (fraktal
  sınır) · berm ve malzeme yığını (eksilir) · kumul (kayar — SAHA §3.6) ·
  ağaç TACI (mevsimle değişir; gövde olur, taç olmaz)
  ⭐ Mekanizma (VARSAYIM): model büyüyen yapıyı "sabit" sayarsa çevreyi
     küçültür — oturumun bir kareden diğerine DARALMASI budur.

KURAL  Değişmezler tablosunun ARKA PLAN ÇAPALARI satırları [KILAVUZ_REHBERI §3]
       artık üç şey taşır: nesne · gerçek boyut (m) · usta karede ÖLÇÜLEN
       piksel. Piksel yazılmayan çapa, çapa değil tariftir [DERS 19 ile aynı].
```

---

# 2. PERSPEKTİF KURALLARI — model neden kaydırıyor  [A11-c · A11-d · A11-g]

```
GEOMETRİ (formül — kaynak istemez, KAMERA §3)
  tilt 0° → ufuk tam %50 · kaçış noktası sabit · dikeyler dik · paralaks yok
  ⚠️ Plan ±2° tilt beyan ediyorsa ufuk KAMERA §3 formülünden hesaplanır ve o
     sayı yazılır; "%58 ufuk, tilt 0°" iç çelişkidir [A11 çelişenler ①].

MODEL NEDEN KAYDIRIYOR (raporun okuması)
  · kompozisyon önyargısı: eğitim verisinde ufuk çoğunlukla 1/3 ya da 2/3'te;
    "0° tilt" semantik olarak "düzgün mimari foto"dur, y-ekseni sıfırlaması
    değil                                              [VARSAYIM — atıf ❌]
  · GÖRELİ ÖLÇEK tutmuyor: T2I modelleri bir nesneyi diğerine oranla çizerken
    sistematik hata yapıyor (GenScale, 1.643 ölçek ilişkisi) [KAYNAK ✅]
  · UZAMSAL KOMUT darboğaz: 21 model · 1.230 bilgi-yoğun prompt; sağ/sol,
    üst/alt gibi ilişkiler ana hata kaynağı (SpatialGenEval)  [KAYNAK ✅]
  · "at 58% height" / "at pixel x,y" tek başına TUTMAZ (SD 1.5/SDXL/MJ sınıfı);
    piksel kilidi yalnız kutu koordinatı alan mimaride (GLIGEN) [araç · KAYNAK ✅]

⇒ SONUÇ: yüzde/piksel cümlesi YALNIZ bir referans nesneye BAĞLANDIĞINDA işe
   yarar. "the horizon sits at half the frame height" tek başına zayıf;
   "the horizon runs exactly along the roof ridge of the brick block" güçlü —
   çünkü ufku SAYILABİLİR bir nesneye bağlar [DERS 19'un ölçek hâli].
```

---

# 3. SAYI TESTİ — hangi sayı prompta, hangisi SPEC'e  [DERS 19 · P2-b · A11-f]

```
İZLEYİCİ BU SAYIYI KADRAJDA SAYABİLİR Mİ?
  SAYABİLİR   → prompta      3 baca · 5 pencere · 2 pilon · 18 kat · 4 kablo çifti
  SAYAMAZ     → SPEC'e       62 lamba · 14 panel · 620 m · %27,8 · 32 kablo/pilon
                prompta yapısal hâli gider: "one evenly spaced line of lights
                receding with correct perspective"
  MUAF        kamera satırının altı alanı [KAMERA §2] · güneş açıları [DERS 18]

DIŞ DOĞRULAMA [A11-f · KAYNAK ✅]: NumBench (640.000 prompt · 1–100) — küçük
tam sayı tutuyor, sayı büyüdükçe model sayıyı reddediyor ya da nesneleri
birleştiriyor. "10 üstü çöker" eşiği raporun okumasıdır (VARSAYIM); ölçülen
şey eğilimdir.
⭐ Bu, DERS 19'un mekanizmasıdır: "exactly three chimneys" tuttu çünkü model
   üçü sayabiliyor; "62 lamps" tutmaz çünkü sayamıyor — bible'da kalır.
```

---

# 4. KESİR CÜMLESİ — boyut çapası nasıl yazılır  [A11-h · A11-k ÖLÇTÜM]

```
⛔ KESİR TABLODAN DEĞİL, USTA KAREDE ÖLÇÜLEN PİKSELDEN YAZILIR [A11-k].
   Raporun kendi örnekleri kendi tablosuyla tutmuyordu: 1,5 m söve = 48 px =
   kadrajın 1/22'si, "one tenth" değil. Yanlış kesir, yanlış ölçek çağırır.

YORDAM
  1. Usta kare (GN) onaylandı → referans nesnenin genişliği piksel olarak ölçülür
  2. kesir = px / 1080 (genişlik) ya da px / 1920 (yükseklik) → en yakın "one nth"
  3. Cümle ÜÇ parça: nesne · kesir · süreklilik
     "the split-top boulder to frame right spans 96 pixels of frame width —
      one eleventh of the frame — and keeps that width from the first frame
      to the last"
  4. GÖRELİ ORAN ikinci çapa olur [A11-h · İDDİA]:
     "the boulder is one third of the habitat's height"
  5. Ufuk bir NESNEYE bağlanır [§2]: "the horizon runs along the foot of the ridge"

⛔ NEGATİF ÖLÇEK CÜMLESİ YAZILMAZ: "do not move the horizon" ufku ve hareketi
   çağırır [DERS 33 · A11 §3.1]. Pozitif, nesneye bağlı çapa yazılır.
```

---

# 5. ZİNCİRDE KAYMA VE KANAL — cümle yetmediğinde  [A11-i · A11-j · A11-l]

```
HATA BİRİKİMİ [KAYNAK ✅ FreqForcing]: ardışık üretimde küçük hata "yeni
normal" olur; uzun ufukta renk kayması, hareket durması, çöküş. A3-a'nın
dış doğrulaması. ⇒ Zincir kısa tutulur ve her halkada zincir_kontrol.sh
kenarları ölçer [KILAVUZ_REHBERI §8 adım 3b].

İLK KAREYE KİLİT [KAYNAK ✅ Rolling Forcing "attention sink"]: modelin
dikkati bir öncekine değil İLK KAREYE de bağlandığında uzun tutarlılık
artıyor. ⇒ A3-b "merkezi çatı" mantığıyla aynı yön: her kare bir öncekinden
değil USTA KAREDEN türer [P2-a — zincir = edit].

KANAL (VARSAYIM — atıflar ❌, A3-c ile aynı yönde)
  düz çizgi haritası (MLSD)  yapı kenarlarını ve ufku kilitler, bulutu/dokuyu umursamaz → tercih
  derinlik (depth)           metrik uzaklığı tutar; ince boru/kabloda zayıf
  Canny                      bulut ve gölge kenarını da "yapı" sayar → titreme; KULLANILMAZ
  IP-Adapter / referans      stil, renk, atmosfer taşır — GEOMETRİ TAŞIMAZ [A3-c]
  seed                       başlangıç gürültüsünü sabitler — kompozisyonu değil
  poz kanalı (Plücker/pose)  kamera kilidi prompt katmanında değil burada [DERS 23 · A3-d]
KLİP İÇİ KAYMA [A11 §2.4 · İDDİA]: iki sabit kare arasında da ölçek kayar;
ölçüsü optik akış tabanlı warping hatasıdır (sabit kamerada teorik 0).
⇒ zincir_kontrol.sh klibin SON karesi ile G(n+1) arasında koşulur
   [KILAVUZ_REHBERI §8 adım 6]; ⑫ KATILIK "size drift" satırı klip içini ölçer.
```

---

# 6. PROMPTA İNEN CÜMLELER — İngilizce · POZİTİF · kesir ÖLÇÜLDÜKTEN sonra

> A11 Bölüm 5'ten; kesirler §4 yordamıyla YENİDEN yazılır — aşağıdakiler
> örnek kalıptır, piksel usta kareden gelir.

```
Urban      The window surround of the brick block at frame left spans 48 pixels
           of frame width — one twenty-second — and keeps that width in every
           frame; the horizon runs exactly along its second-floor sill line.
Rural      The oak trunk at frame right is a fixed anchor 32 pixels wide — one
           thirty-fourth of the frame — and the field line behind it sits at exactly
           half the frame height throughout.
Coastal    The stone base of the lighthouse holds the left edge at 160 pixels wide —
           one seventh of the frame — and the sea horizon cuts the frame exactly at
           half height in every frame.
Mountain   The glacial boulder in the lower right corner keeps its 96-pixel width —
           one eleventh of the frame — from first frame to last; the ridge line
           fixes the horizon behind it.
Desert     The vertical face of the mesa bounds the background at a constant height;
           the flat desert floor meets the sky exactly at the vertical centre of the frame.
Moon/Mars  The sharp crater rim in the right foreground keeps its width and depth
           unchanged in every frame; the airless horizon splits the frame exactly at
           half height.
Glacier    The bedrock nunatak stands out of the ice at a constant 128-pixel width —
           one eighth of the frame — and the ice horizon runs exactly along the
           frame's centre line.
```

---

# 7. KAPI — bu kılavuz nerede zorlanır

```
prompt_kontrol.py §10d (11.09.2026):
  · COMPOSITION bloğunda hiçbir "spans / keeps … pixels / one nth of the frame /
    percent of frame width" kesir-çapa cümlesi yoksa                    → FIX
  · (mevcut) kamera satırında altı alan · ufuk yüzdesi · Scene N of X

ELLE
  · usta kare onayında referans nesnenin pikseli ÖLÇÜLÜR ve değişmezler
    tablosuna yazılır (§1); kesir cümlesi o sayıdan yazılır (§4)
  · sayı testi: prompta giren her sayı için "izleyici sayabilir mi" (§3)
  · araç kapısı: bu araçta geometri/poz KANALI var mı [KILAVUZ_REHBERI §8 adım 0b · A3-d]

ÖLÇÜLECEK
  · referans nesne + kesir cümlesi ① STATION IDENTITY ve ② SCALE LOCK'u
    2 puanın üstüne taşıyor mu — ilk üretimde
  · kanal seçimi (MLSD vs depth) — hiç koşulmadı, A3-b ile aynı varsayım
```
