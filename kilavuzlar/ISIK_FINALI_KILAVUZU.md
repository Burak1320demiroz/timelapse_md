# 🏮 IŞIK FİNALİ KILAVUZU — mavi saat ve yapay ışık

> Bu deponun en çok kullanılan ödül anı yapının ışıklarının yanmasıdır: DEEP END (küçük ışıklar sıra
> sıra) · LAST HARBOR (fener) · BLUE DOOR (lamba → fener → pencere) · FIRST GUEST (kapı ışığı kuma
> yayılır) · EDEN ARK (kemer lambaları) · THE SLOW TAKEOFF (pencereler gruplar hâlinde). Bu kılavuz
> mavi saatin **zamanını**, ışığın **malzeme olarak** önceden takılmasını, sıkıştırma rejiminde **nasıl
> yandığını**, model arızalarını ve kapak karesini yazar. Gece kararı yine sahibindir [ZAMAN_VE_ISIK §5].
>
> Kaynak: A28 · 07.10.2026 (`arastirma/SONUCLAR/A28_GEMINI_HAM.md`) · denetim `A25-A29_DENETIM.md` §4.
> ⭐ Rapordan inen: **alacakaranlık tablosu** (9 satırın 9'u bu makinede tuttu — referansı görünür batış
> −0,833°, rapor "0° geometrik" diye yanlış etiketledi) · **75× ve 900×'te lamba tek karede yanar**
> (1 kare = 2,5 sn / 30 sn; lamba < 1 sn'de yanar — aritmetik ✅) → "yavaşça yanan ışık" yazılmaz, gruplar
> ayrı karelerde yanar · **olumsuzlama nesneyi çağırır**: NegT2IBench (arXiv:2610.03084, Eki 2026 ✅) —
> 11 modelin 9'u olumsuz ifadede kötüleşir, başarısız çıktıların %41,5'i tam yasaklananı çizer [DERS 59'u
> dışarıdan destekler] · **önce ışıklı final, sonra geriye ışıksız** (bizim ters üretimimiz) · küçük resimde
> ışık KÜMESİ ve ≥ 4,5:1 kontrast (WCAG 2.1 ✅).
> ⛔ İnmeyen: "%43,8 ters etki" (o sayı en büyük puan düşüşü; makale lens flare/bloom ÖLÇMEDİ — renk ve
> uzamsal ilişki ölçtü) · gök "10.000–15.000 K" ve EV değerleri (kaynak hesap sitesi) · "kademeli yanma
> profesyonel yapımlarda yalnız kurgu illüzyonudur" (abartı: farklı zamanda açılan gruplar gerçek bir
> sıralı yanmadır) · I2VEdit / Animate Anyone atıfları (arXiv numaraları başka makalelere ait).

---

# 0. 🚪 KURAL

```
Işık bir MALZEMEDİR — kaynağı önceden kadrajdadır, sırası saniyesiyle yazılır.
  · her armatür birkaç klip ÖNCE sönük olarak takılır ve kadrajda görünür [P11-d]
  · A (75×) ve B (900×) rejiminde ışık "yavaşça" YANMAZ: her grup TEK KAREDE yanar; sıra, grupların
    farklı anlarda açılmasıdır ("first … then … last …") [P12-d · A28-b]
  · final mavi saattedir ama zifiri değildir: güneş ufkun −2…−6° altında; yapı, gök ve su okunur [DERS 45]
  · istenmeyen ışık etkisi (hale, huzme, parlama) ADIYLA yazılmaz, negatifte bile — POZİTİF tarif edilir
    [DERS 35 · 59 · NegT2IBench]
  · üretim ters sırada: ışıklı usta kare ÖNCE, ışıksız kareler ondan geriye [DERS 5 · A28-e]
  · mavi saat filmde bir kez; en çok iki A klibi (≈20 dk) [ZAMAN_VE_ISIK §5 · P25-f]
```

Ölçülmüş bedeli (arşiv):

| film | ne oldu | hangi kural yoktu |
|---|---|---|
| POLAR HABITAT | promptta olmayan lazer, bloom, yıldırım arkı | pozitif ışık tarifi |
| THE FIRST GUEST | lamba halesi, havada asılı toz (final yine 2,5 sn kımıldamadı ✅) | pozitif "clear air" |
| THE STAR DOCK | hacimsel huzme pozlamayı patlattı | huzme yazılmaz |
| THE LONG DAY | güneş diski kadraja girdi | güneş yalnız etkisiyle [DERS 39] |
| karanlık finaller | okunmadı | zifiri değil [DERS 45] |

---

# 1. 🌆 MAVİ SAAT NE ZAMAN — dakika tablosu

Güneşin görünür batıştan (üst kenar ufukta, −0,833°) sonra −2°, −4° ve −6°'ye (sivil alacakaranlığın
sonu) indiği dakika — bu makinede hesaplandı, A28 tablosuyla birebir:

| enlem | tarih | −2° | −4° | −6° |
|:-:|---|:-:|:-:|:-:|
| 35° | 21 Mart / 23 Eylül | 5,7 | 15,5 | 25,3 |
| 35° | 21 Haziran | 6,6 | 18,1 | 29,7 |
| 35° | 21 Aralık | 6,5 | 17,4 | 28,2 |
| 45° | 21 Mart / 23 Eylül | 6,6 | 17,9 | 29,3 |
| 45° | 21 Haziran | 8,2 | 22,5 | 37,5 |
| 45° | 21 Aralık | 7,8 | 21,0 | 33,9 |
| 55° | 21 Mart / 23 Eylül | 8,1 | 22,1 | 36,2 |
| 55° | 21 Haziran | 11,9 | 33,8 | 58,3 |
| 55° | 21 Aralık | 10,8 | 28,6 | 45,6 |

```
FORMÜL   cos(HA) = [sin(alt) − sin(enlem)·sin(sapma)] / [cos(enlem)·cos(sapma)]  ·  1° saat açısı = 4 dk
         dakika = (HA(alt) − HA(−0,833°)) × 4
ÖRNEK    THE SLOW TAKEOFF (47° K · sapma +12°): batış (0°) 18:53 güneş saati · −4,4° = 19:20 → G28–G30 ✓
PENCERE  iç/dış ışığın dengelendiği an −4…−6° aralığıdır [A28-a · İDDİA, mimari fotoğraf pratiği];
         −2°'de gök hâlâ baskın, −6°'nin ötesinde gök kararır ve silüet kaybolur
⇒ PLAN   KARE TABLOSU'nda final kareleri (GN ve son iki kare) için güneş yüksekliği −2…−6° yazılır;
         −6°'nin altı GECE'dir ve sahip kararı ister [ZAMAN_VE_ISIK §5]
```

---

# 2. ⏩ SIKIŞTIRMA REJİMİNDE IŞIK — tek kare kuralı

```
1 karenin temsil ettiği süre (30 fps, 8 sn = 240 kare):   A (10 dk) = 2,5 sn · B (2 sa) = 30 sn · G = 1/30 sn
lamba / LED / armatür grubunun yanma süresi:              < 1 sn  → A ve B'de bir grup ya sönüktür ya yanık;
                                                                     arası YOKTUR — "fades in" yazılmaz
mavi saatin (≈30 dk) ekranda kaldığı süre:                 A'da 3 klip ≈ 24 sn · B'de ≈ 2 sn (bir klibin dörtte biri)
```

| rejim | ışıkların yanışı | mavi saat göğü | tutuş |
|---|---|---|---|
| A (≈75×) | "the lights come on in groups: first …, then …, last …" — her grup bir anda | gök klip boyunca soluk alacakaranlıktan maviye koyulaşır | "from about four to eight seconds the lights stay on and nothing else changes" |
| B (≈900×) | gruplar birkaç saniye arayla — ya da hepsi birden | gün ışığından derin maviye birkaç saniyede (agresif) | B finalde KULLANILMAZ (tutuş için gök çok hızlı akar) |
| G (1×) | akkor lamba yumuşak ısınır ("warms up over about a second"); LED anında | gök neredeyse değişmez | doğal: su ve yansıma kıpırdar, ışık sabit |

⭐ **Sıra fiziksel bir saatten türetilir** [P22-d]: içeriden biri lambaları sırayla açar (burundan
kuyruğa), otomatik zamanlayıcı grupları açar, gök karardıkça sensörler açılır. Sıra PLAN'daki IŞIK
DEFTERİ'ne (§4) saniyesiyle yazılır.

---

# 3. 🎨 IŞIK VE GÖK — renk ve okunurluk

```
RENK      yapı ışığı sıcak (2700–3000 K: "warm") · gök mavi saat mavisi ("deep clear blue") — kontrast
          yapı ile gök arasındadır [A28-a · İDDİA: gök Kelvin değerleri hesap sitesi kaynaklı]
EN PARLAK final karesinde en parlak şey yapının ışıklarıdır, gök değil [EDEN ARK G18 cümlesi]
          "the warm windows and their reflections are the brightest things in the frame"
OKUNURLUK uzakta tek lamba birkaç pikseldir — grup/şerit/pencere sırası okunur, tek nokta okunmaz
          (THE SLOW TAKEOFF: kabin penceresi ≈ 8 px → "the whole row of cabin windows")
SU        sakin suda yansıma keskin ters kopya; dalgacıkta dikey ışık sütunu [SU_VE_YANSIMA §2]
İÇ IŞIK   lamba iç mekânda bir kez yanar ve yanık kalır; dış kareyle tutarlı (kokpit lambası S13 ↔ S18–S22)
```

---

# 4. 📒 IŞIK DEFTERİ — final ışıklıysa PLAN'a zorunlu

| armatür / grup | takıldığı klip | sönük göründüğü kareler | grup | yanma sırası · saniye (film) | renk | suda yansıma |
|---|:-:|---|:-:|---|---|:-:|
| ⬜ | S⬜ | G⬜–G⬜ | ⬜ | ⬜ · ⬜ sn | sıcak / nötr | evet / hayır |

Örnek — THE SLOW TAKEOFF (yazılmış prompttan çıkarıldı):

| armatür / grup | takıldığı klip | sönük | grup | yanma | renk | yansıma |
|---|:-:|---|:-:|---|---|:-:|
| kokpit okuma lambası | S13 (kokpit) | — (iç mekân) | iç | S13 sonu (111 sn) · S18'den beri dışarıdan tek ışık | sıcak | — |
| kabin pencereleri (ön) | S12–S15 (iç donanım) | G16–G26 | 1 | S26 ≈ 209 sn | sıcak | evet |
| kabin pencereleri (orta · arka) | aynı | G16–G26 | 2 · 3 | S26 ≈ 211 · 213 sn | sıcak | evet |
| teras korkuluğu + merdiven lamba dizisi | S16 (sönük takılır) | G17–G26 | 4 | S26 ≈ 215 sn | sıcak | evet |

---

# 5. 🤖 YAPAY ZEKÂNIN IŞIKLA BİLİNEN ARIZALARI — ve POZİTİF yazım

| arıza | bizde | genel kanıt | yazım (pozitif — etkinin ADI geçmez) |
|---|---|---|---|
| hale / bloom / flare | FIRST GUEST · POLAR | ölçülmedi (rapor kaynaksız) | "the lights are small warm points and evenly lit windows with crisp edges" |
| huzme / "god rays" | STAR DOCK | — | "the air is clear and dry" |
| armatürsüz ışık | — | difüzyon ışığın "sonucunu" çizer [VARSAYIM] | armatür önceki karelerde SÖNÜK nesne olarak tarif edilir; ışık "from each lamp on the railing" |
| neon / gündüz gibi gece | — | VBench "temporal flickering" = kareler arası ortalama mutlak fark ✅ (yalnız durağan sahnede) | "deep blue hour, the structure, the water and the trees still clearly readable" |
| ışık birden "belirir" | P12-d | aritmetik ✅ (§2) | grupları sırayla yaz; G'de yumuşak ısınma |
| olumsuzlama ters teper | DERS 33 · 35 · 59 | NegT2IBench: 9/11 model kötüleşir · başarısız çıktıların %41,5'i yasaklananı çizer ✅ | ⛔ "no lens flare · no bloom · no lasers · no dust" YAZILMAZ |

⚠️ NegT2IBench görüntü (text-to-image) modellerini ölçtü, video değil; ve renk/uzamsal ilişkileri ölçtü,
ışık etkilerini değil. DERS 59 ile AYNI YÖNDE — kanıt, kural değil [A28-c].

---

# 6. 🖼️ KAPAK KARESİ — ışıklı usta kareden

```
KAYNAK      usta kare GN (ışıklı, mavi saat) — öncesi/sonrası bölme YOK (sahip 19.09.2026)
120 PX      ışıklar KÜME olarak okunmalı: pencere sırası, teras şeridi, sudaki yansıma sütunu —
            tek nokta lamba 120 px'te kaybolur [MUZIK_VE_KAPAK §2.5]
KONTRAST    başlık ≥ 4,5:1 (WCAG 2.1 SC 1.4.3 ✅) · yapı ışığı ile gök arasında belirgin sıcak/soğuk ayrım
KÜÇÜK RESİM sağ alttaki süre damgası köşesine ışık kümesi ve küçük nesne (kano) düşmez [A15-c]
```

---

# 7. ✅ KONTROL LİSTESİ (ihlalde TEK eylem)

| # | madde | ihlal → eylem |
|:-:|---|---|
| 1 | final kareleri güneş −2…−6°'de; −6°'nin altı sahip kararıyla | → SIRAYI YENİDEN YAZ (SAAT sütunu) |
| 2 | Σ ışık günü ≤ 14 sa; mavi saat ≤ 2 A klibi | → SIRAYI YENİDEN YAZ |
| 3 | her armatür birkaç klip önce SÖNÜK takılı ve kadrajda | → SAHNE EKLE (montaj satırı) |
| 4 | IŞIK DEFTERİ dolu: grup · sıra · saniye | → DEFTERİ YAZ |
| 5 | A/B'de "fades in · gradually · slowly lights up" yok; gruplar sırayla | → SIRAYI YENİDEN YAZ |
| 6 | negatifte ışık etkisinin ADI yok (flare · bloom · rays · laser · glow) | → NEGATİFTEN ÇIKAR |
| 7 | pozitif tarif var: "crisp edges · clear dry air · warm windows" | → BLOĞU YENİDEN YAZ |
| 8 | finalde en parlak şey yapının ışıkları; yapı, gök, su okunur | → KAREYİ YENİDEN ÜRET |
| 9 | ışıklı usta kare önce üretildi, ışıksız kareler ondan geriye | → KAREYİ YENİDEN ÜRET |
| 10 | final I2V'sinin son dört saniyesi tutuş ("from about four to eight seconds") | → BLOĞU YENİDEN YAZ |
| 11 | sudaki yansıma §SU_VE_YANSIMA §1 hesabıyla tutarlı | → KAREYİ YENİDEN ÜRET |
| 12 | kapak 120 px'te ışık kümesi + başlık okunuyor, kontrast ≥ 4,5:1 | → KAPAĞI YENİDEN ÇERÇEVELE / SAHNEYİ YENİDEN ÜRET |

---

# 8. 📎 İNMEYENLER

```
⛔ "%43,8 ters etki · no lens flare kadraja çağırır"   rakam karışık; makale ışık etkisi ölçmedi (yön aynı, sayı değil)
⛔ gök 10.000–15.000 K · EV −1 … 12 tablosu            hesap sitesi kaynaklı, film için gerekmez (pozitif dil yeter)
⛔ "kademeli yanma yalnız kurgu illüzyonu"             abartı — farklı anlarda açılan gruplar gerçek sıralı yanmadır
⛔ B rejiminde "all exterior lighting zones simultaneously" bir kural değil, seçenek
⛔ I2VEdit arXiv:2508.14609 · Animate Anyone arXiv:2607.25275   numaralar başka makalelere ait (I2VEdit = 2405.16537)
⚠️ LRTimelapse deflicker / Holy Grail ✅ var — bizde kurgu sonrası titreme ölçümü KURGU_VE_TESLIM §6 ⑥ (YDIF)
```
