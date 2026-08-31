# 🔍 THE NARROW LOT — QA SPEC

> ⛔ **BU SPEC ÜRETİMDEN SONRA YAZILDI ve promptlardan GERİ OKUNDU.**
> Uydurulmadı: buradaki her kilit, teslim edilen beş görsel promptun
> içinde İngilizce olarak yazılıdır. Uydurulan tek şey yoktur; **eksik
> olanlar §6'da açıkça EKSİK diye durur.**
>
> Sebebi süreçtir: v1 koşusunda SPEC hiç üretilmedi ve `② İNŞA`, `④ TESLİM`,
> `⑥ GEÇİŞ` belgesiz (mod V) koştu — skorları bu yüzden T tablolarına skor
> olarak yazılmadı [DERS 17]. Bu dosya, o üç merceğin **belgeyle
> TEKRARLANMASI** için vardır.
>
> ⭐ Ve §6, bu filmin en öğretici parçasıdır: `② STRUCTURE IDENTITY 2/10`,
> SPEC'te olmayan iki sayının doğrudan sonucudur.

---

## 0. KÜNYE

```
FİLM          THE NARROW LOT — Dar Parsel
FORMAT        9:16 dikey · 5 sahne · ölçülen toplam 0:29,9
              klip süreleri (① raporundan): 5,7 · 6,1 · 6,2 · 6,0 · 5,9
              ⛔ hedef 6,0 × 5 = 30,0 · ffprobe ölçümü yapılmadı [D-d]
KAPAK KARTI   ⛔ ÜRETİLMEDİ — altı merceğin altısı da "NO CARD" yazdı
YAPI          18 katlı betonarme konut kulesi · yaklaşık 58,7 m
SAHA          şehir içi dar parsel (yıkım artığı) + kış eki
ZAMAN YAYI    ~12 ay (③ okuması: "about one year" ✅ TUTTU)
KAMERA        tek istasyon — ANA (5 sahnenin 5'i) · detay istasyonu YOK
ÜRETİM SIRASI ⛔ BEYAN EDİLMEDİ. Zincir fiilen tuttu (① 10/10 · ⑤ SAME WORLD)
              ama ters inşa sırası belgeye hiç yazılmadı.
KAYNAK        harici GPT (Restoration Timelapse) · brief: BES_SAHNE_GPT_BRIEFI
```

---

## 1. ⛔ FİNAL VURUŞ KANITI — teslimin tek kapısı

```
SAHNE       S4
SANİYE      0:29,0
GÖRÜLMESİ GEREKEN ŞEY:
   Tamamlanmış on sekiz katlı kule, antrasit metal cephe bantları ve açık
   taş düşey panelleriyle taban kotundan taç parapetine kadar KAPALI;
   parselde HİÇBİR VİNÇ, iskele veya geçici ekipman YOK; ve kulenin gölgesi
   kadrajın sağındaki ALTI KATLI KIRMIZI TUĞLA BLOĞUN cephesinde duruyor.

KOMUT
   ffmpeg -ss 29.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⚠️ v1 SONUCU: ④ mod V'de PASS verdi — ama mod V'de bu kategori "bir sonu
   var mı"ya dönüşür. Yukarıdaki cümle HİÇ DENETLENMEDİ [DERS 17].
⛔ Ve bu filmin BEDELİ (gölgenin komşuya düşmesi) promptta hiç yazılmamıştı;
   §6'ya bakınız. ④ "THE ONE THING THIS FILM DOES: NONE FOUND" dedi.
```

---

## 2. KADRAJ KİLİTLERİ — ANA istasyon (5 sahnenin 5'i)

Formül (`KAMERA_ISTASYONU §3`): `kare yüzdesi = %50 + f × (y − h) / (36 × D)`
Bu filmde `f = 24`, `h = 24,0`, `D = 72` → **kare yüzdesi = %50 + (y − 24) / 108**
Tolerans **± %2**.

| Ne | y (m) | Beklenen | Hangi sahnelerde | v1 ölçümü |
|---|---:|---:|---|---|
| ufuk çizgisi | 24,0 | **%50,0** | 5 sahnede de | ✅ sapma %0 (① tablo) |
| yapı tabanı | 0 | %27,8 | 5 sahnede de | NOT VISIBLE |
| taç (parapet) | 58,7 | %82,1 | S3 · S4 | NOT VISIBLE |
| kat yüksekliği | 3,15 | — | bible | NOT VISIBLE |

```
⛔ ÜST SINIR: hiçbir yapı parçası %87,5'in üstünde olamaz (üst 1/8 = arayüz).
⛔ ALT SINIR: ilerlemeyi kanıtlayan hiçbir şey %25'in altında olamaz.
⛔ SAĞ ŞERİT: kanıt nesnesi kare genişliğinin sağ %13'ünde duramaz.

⚠️ v1 SONUCU: ① SAFE AREA 4/10. İki bulgunun ikisi de alt %25'te:
   0:00,0-0:05,7 işçiler ve kazı hendeği · 0:24,0-0:29,9 işçiler ve kaldırım.
   SEBEP: COMPOSITION bloğu promptlarda hiç yoktu (0/5) [DERS 20].
```

---

## 3. DEĞİŞMEZLİK KİLİTLERİ — sahneler arası

```
① KAMERA        5 sahnenin 5'inde de kamera hareketi = 0 kare.
                Pan/tilt/zoom/kayma/sarsıntı: hiçbiri 1 karede bile yok.
                v1: ✅ ① CAMERA LOCK 10/10 · VANTAGE GROUPS = 1

② ANA İSTASYON  5 sahnede de: lens 24 mm · yükseklik 24,0 m · mesafe 72 m ·
                bakış 035° · tilt 0° · roll 0°. Beşi BİREBİR aynı.
                v1: ✅ ① STATION IDENTITY 10/10

③ ÇAPA ① SAĞDA  ALTI katlı koyu kırmızı tuğla apartman, çatısında TAM ÜÇ baca.
                ⛔ Kat sayısı ya da baca sayısı değişirse BLOCK.
                ⛔ EK KİLİT [v1'de eksikti]: bloğun sokak kotundaki TEK KATLI
                   EKİ de her karede vardır ve sayılır.
                   v1 bulgusu ⑤ 0:23,2 → 0:24,0: "single-story annex …
                   completely missing". Sayılmayan parça korunmayan parçadır.

④ ÇAPA ② SOLDA  DÖRT katlı açık taş bina, üst katında TAM BEŞ eşit aralıklı
                pencere. Sayı değişirse BLOCK.

⑤ ÇAPA ③ ARKADA sürekli ağaçlıklı sırt, profili değişmez.
                ⚠️ Mevsim rengi DEĞİŞİR (taşıyıcıdır), profil DEĞİŞMEZ.

⑥ UFUK          %50,0 · sapma ± %2 · 5 sahnede de     v1: ✅ %0 sapma

⑦ YAPI GEOMETRİSİ  kat sayısı 18 · kat yüksekliği 3,15 m sabit ·
                çekirdek merkezde tek betonarme · cephe: antrasit metal bant
                + sıcak açık taş düşey panel + tam boy cam · taç düz
                ⛔ OTURUM VE AKS SAYISI EKSİK — §6'ya bak. ② BURADA DÜŞTÜ.

⑧ VİNÇ TİPİ     gri flat-top, yatay bom, zemin kotunda beton kaide.
                Tip, renk ve konum S2 ve S3'te BİREBİR aynı.
                v1: ✅ ⑤ MACHINE IDENTITY 10/10
```

---

## 4. GÜNEŞ SAATİ KİLİDİ — promptlarda dereceyle yazılıydı

| S | Mevsim | Azimut | Yükseklik | Gölge yönü | v1 ölçümü |
|:-:|---|---:|---:|---|---|
| 0 | yaz ikindi | 236° | 61° | doğu-kuzeydoğu | ⛔ ~45° ölçüldü |
| 1 | sonbahar ikindi | 225° | 42° | doğu-kuzeydoğu | ⛔ ~45° ölçüldü |
| 2 | kış ① ikindi | 202° | 18° | kuzeydoğu | ⛔ ~45° ölçüldü |
| 3 | kış ② geç ikindi | 214° | 22° | kuzeydoğu | ⛔ ~45° ölçüldü |
| 4 | yaz ikindi (S0 ile AYNI) | 236° | 61° | doğu-kuzeydoğu | ⛔ ~45° ölçüldü |

```
⛔ v1 SONUCU: ③ SUN DIRECTION 0/10 · SHADOW VS SUN HEIGHT 2/10.
   "In the winter scenes the shadows are identical in length and direction
    to the summer scenes, implying a high summer sun elevation."
   ⭐ SAYILAR PROMPTTA VARDI. Yalnız GÖRSEL promptta vardı; I2V'ye hiç
      girmediler ve videoyu üreten prompt I2V'dir [DERS 18].

⛔ KLİP İÇİ: her klipte BİR GÜN geçer ve gölge kadrajı SÜPÜRÜR.
   v1: ③ beş klibin beşinde de açı değişimini 0 derece ölçtü.
   v2'de I2V'ye başlangıç VE bitiş azimut/yüksekliği yazılır.

⛔ MEVSİM YAYI tek yönlü: yaz → sonbahar → kış① → kış② → yaz.
   v1: ✅ ③ SEASON ORDER 10/10 · SEASON CARRIER 10/10
```

---

## 5. MONOTON BÜYÜME VE SÖKÜM TAKVİMİ

```
S0  arsa · ilk kazı kesiği                 EKLENEN: kazı kesiği
S1  + radye + bodrum + zemin podyumu       EKLENEN: podyum üst kotu
S2  + çekirdek + 6 kat                     EKLENEN: vinç KURULUR
S3  + 18 kat + taç + cephenin bir kısmı    EKLENEN: cephe başlar
S4  + cephe tamam + peyzaj                 SÖKÜLEN: vinç · iskele · çit

SÖKÜM TAKVİMİ
  vinç        kurulum S2  →  söküm S4'ten ÖNCE (S4'te yok)
  şantiye çiti kurulum S0  →  söküm S4'ten ÖNCE
  kalıp       S1-S3       →  söküm S4'ten ÖNCE

⛔ KURULUM TAKVİMİ EKSİKTİ — v1'in gerçek devamlılık hatası:
   ⑤ 0:11,2 → 0:12,0 "a fully erected tower crane clipping through the
   structure" — vinç kaidesi hiçbir sahnede hazırlanmadı.
   v2 KİLİDİ: vinç kaidesi S1'de dökülür ve S1 karesinde GÖRÜNÜR.

⛔ ZEMİN DURUMU BİRİKİR (v1'de birikmedi — ⑤ WEAR 2/10):
   S0 kuru toprak, az iz → S1 derin çamur → S2 kar altında kirli çamur →
   S3 erime suyu, en dağınık → S4 yeni kaldırım + kenarda kuru çamur artığı.
   ⛔ Çamur ve birikinti DEĞİŞMEZ DEĞİLDİR; sahne sahne farklı yazılır.
```

---

## 6. ⛔ BU SPEC'İN KENDİ AÇIKLARI — ②'nin düştüğü yer tam olarak burasıdır

Aşağıdakiler teslim edilen promptlarda **hiç yazılmadı**, dolayısıyla bu
SPEC de onları içeremez. Uydurmak yerine EKSİK olarak duruyorlar.

```
⛔ OTURUM ÖLÇÜSÜ         yok. Promptta yalnız "narrow rectangular".
⛔ AKS DÜZENİ            yok. Promptta yalnız "regular structural bays".
⛔ AKS ARALIĞI           yok.
⛔ ÇAPA YÜKSEKLİKLERİ    yok — tuğla bloğun çatı sırtı kaç metrede?
                         Bu yüzden §2 tablosunda kanıt kotu YAZILAMADI.
⛔ KANIT NESNESİ         sahne başına yazılmadı; "the sixth completed
                         structural level" gibi ölçüsüz ifadeler kaldı.
⛔ VAAT / DİRENÇ / BEDEL yok. Konsept kapısı hiç koşulmadı.
⛔ KAPAK KARTI           yok.
⛔ MÜZİK / BPM           yok.

⭐ VE SONUCU ÖLÇÜLDÜ:
   ② STRUCTURE IDENTITY 2/10 · VERDICT DIFFERENT
   "Clip 3 occupies almost the entire width of the site … by Clip 5 the
    finished building has a drastically narrower footprint"
   ⛔ Bina genişliği hiçbir yerde bir SAYIYA bağlanmamıştı.

   ④ "THE ONE THING THIS FILM DOES THAT NOTHING ELSE DOES: NONE FOUND"
   ⛔ Çünkü BEDEL hiç yazılmamıştı. Bir film yazılmamış bir bedeli teslim edemez.

   Buna karşılık ÇAPALAR sayıyla yazılmıştı (6 kat · 3 baca · 5 pencere) ve
   ① ANCHOR IDENTITY 10/10 · ⑤ SAME WORLD aldı.
   ⭐ Aynı film, aynı model: SAYILAN tuttu, TARİF EDİLEN dağıldı [DERS 19].
```

---

## 7. BU SPEC'LE TEKRARLANACAK KOŞULAR

```
② İNŞA    bu dosya + tam kurgu           → skoru T2'ye SKOR olarak yazılır
④ TESLİM  plan + kapak + tam kurgu       → ⛔ kapak ÜRETİLMEDİ, koşulamaz
⑥ GEÇİŞ   plan + SESLİ tam kurgu         → ⛔ ses YOK, koşulamaz

⭐ Yani v1'de yalnız ② belgeyle tekrarlanabilir. ④ ve ⑥ için önce eksik
   TESLİM parçaları (kapak kartı ve müzik) üretilmelidir — ve o noktada
   film zaten v2'dir.
```
