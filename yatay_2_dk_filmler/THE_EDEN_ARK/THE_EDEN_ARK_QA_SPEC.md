# 🔍 THE_EDEN_ARK — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM · ⑥ GEÇİŞ · ⑧ YÖNTEM · ⑩ SEBEP · ⑪ ENVANTER).
> ⛔ ① KARE · ③ ZAMAN · ⑤ DEVAMLILIK · ⑦ İŞ · ⑨ FAALİYET · ⑫ KATILIK merceklerine **VERİLMEZ** — o altısı
> dokümansız koşar [AGENTS değişmez ⑦ · QA/00_README mod sistemi]. Yorum yok, yalnız ölçülebilir kilitler.
>
> ⛔ Dosya adı `*_QA_SPEC.md` KALIR — `araclar/sayac.sh` ve `araclar/qa_paket.sh` bu deseni arar.
> ⛔ Koşu paketi: `bash araclar/qa_paket.sh yatay_2_dk_filmler/THE_EDEN_ARK <teslim.mp4> [kapak.png]` — günlüksüz durur [DERS 28].

---

## 0. KÜNYE

```
FİLM          THE_EDEN_ARK — terk edilmiş 130 m'lik bir yük gemisi kuru havuzda soyulur, ambarları bahçeyle dolar,
              üstü cam kubbeyle örtülür, havuz dolar ve gemi mavi saatte denize çıkar · tek yüksek çapraz istasyon
FORMAT        16:9 yatay · 1920×1080 · 30 fps · yatay_2_dk_filmler · ⚠️ BANDIN DIŞI (18 × 8,0 — sahip izni 05.10.2026)

TESLİM YAPISI ⭐ SAHNE BLOĞU  18 sahne × 8,0 sn = 144,0 sn              ← merceklerin konusu
              ⭐ KAPAK KARTI  1 × 5,0 sn          =   5,0 sn              ← SAHNE DEĞİL
                 TOPLAM                          149,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR. Ayrı denetlenir: "kart, S17'nin sonundaki gemiyi mi gösteriyor?"

SAHNE SAATLERİ  sahne n = n × 8,0 → (n+1) × 8,0   ·   S0 0,0–8,0 · … · S17 136,0–144,0 · KART 144,0–149,0
                (120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · her kesme ölçü başında)
PART GRID       — (yalnız 6/8 dk hattı; bu formatta QA birimi FİLM)
⛔ DÜZ IZGARA   sahip ızgarası. ⑥ METRONOM hükmü BEKLENEN ve KABUL EDİLMİŞ risktir (PLAN §AŞAMA MERDİVENİ).
⛔ ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — en büyük kutu ≥ 9,0 gerekir; {4,6,8} çıkarsa iki-klip hükmü (PLAN).

YAPI          130 m genel kargo gemisi · üç ambar · cam kubbe 20 kemer × 4 m, 18 m en, güverteden 13 m · incir 13 m
SAHA          eski Adriyatik tersanesi, kuru havuz 170 × 26 m (kenar +1,5 · taban −7,0) · çapalar: tuğla baca · yakın
              havuz kenarı · mendirek feneri + ufuk
ZAMAN YAYI    gerçekte aylar · film mertebe anlatır: "tek bir uzun haziran günü, sabahtan mavi saate" [P1-c]
IŞIK          TEK GÜN 06:00 → 20:00 · Σ rejim 14,0 saat (12 A + 6 B) · bilinçli sıkıştırma
KAMERA        MAIN STATION — tek istasyon · h +24,00 m · d_orta 135,0 m · bakış 10° · tilt 0° · detay istasyonu YOK
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G18 usta kare → G17 → … → G0 · her kare zincir_kontrol.sh + tuğla baca ELLE
GÜNLÜK        THE_EDEN_ARK_URETIM_GUNLUGU.md — ⛔ boş (üretim başlamadı; boşken bu SPEC'in hükmü yoktur)
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S17
SANİYE      143,0 (S17'nin 7,0. saniyesi — son 2,0 sn'lik TUTUŞUN içi [P2-i]; mavi saat, okunur [DERS 45])
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① cam kubbe ışıyor, içinde yeşil taçlar ve büyük incir; kemerler boyunca sıcak lamba dizileri yanık
   ② gemi KAPININ DIŞINDA: baş x ≈ 1328 · kıç x ≈ 1657 · baca üstten ≈ 552; römorkör kıçın sağında (x 1685–1728),
      halat gergin; havuz BOŞ ve su dolu; iskele, rampa, vinç, konveyör YOK
   ③ AYNI tuğla baca: x ≈ 100 · üstten 418 → 671 · 253 px — G0 ile aynı konum ve boy
   + BEDEL görünür: üç ambarın yerinde cam altında orman; gövde lacivert, pas yok

KOMUT
   ffmpeg -ss 143.0 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede ①②③'ten biri yoksa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP
   ffmpeg -ss 0.3   -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 143.9 -i teslim.mp4 -frames:v 1 kanit_g18.jpg
   İki karede tuğla baca, yakın havuz kenarı, mendirek feneri ve ufuk tam aynı yerde. Işık BİLİNÇLİ FARKLI
   (06:00 sabah ↔ 20:00 mavi saat — PLAN LOOP satırı).
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=+24,00 · d_orta 135,0 · tilt 0 · yüzde ALT kenardan)

| nesne | y (m) | yüzde | x (soldan, px) | px boy | her karede |
|---|:-:|:-:|:-:|:-:|---|
| ufuk (tilt 0) | — | 50,0 (üstten 540) | — | — | ✓ |
| ⭐ tuğla baca (KANIT) | +1,5 → +45 | 37,9 → 61,3 | 100 | 253 | ✓ BİREBİR (boy dâhil) |
| yakın havuz kenarı (baş hizası → kıç hizası) | +1,5 | 17,4 → 34,2 | 215 → 1332 | — | ✓ |
| mendirek feneri | +2 → +14 | 42,6 → 46,6 | ≈ 1850 | 43 | ✓ (G15+'da kırmızı ışığı yanabilir) |
| gemi baş bodoslama (G0–G16 başı) | +8,0 | 29,3 | 172 | — | S16'ya kadar ✓ |
| gemi baca tepesi (G0–G16 başı) | +21,5 | 48,2 | 1182 | — | S16'ya kadar ✓ |
| yakın borda güverte (baş → kıç) | +5,5 | 26,7 → 36,9 | 437 → 1290 | — | ✓ (G15+'da +1,0 m yukarıda) |
| ambar 1 · 2 · 3 mezarnası | +7,0 | 31,9 · 34,3 · 36,1 | 570 · 806 · 988 | ≈ 150 en | ✓ |
| cam kubbe tepe (baş ucu → kıç ucu) | +18,5 | 43,7 → 45,8 | 416 → 1067 | — | G12+ |
| büyük incir tepesi (dikili) | +16,0 | 42,6 | 806 | — | G7+ |
| vinç bom başı / kanca (yalnız G5–G7) | +32 / +22,5 | 57,8 / 48,6 | 838 / 806 | — | bom GÖĞE karşı ⚠️ · kanca KARAYA karşı ✓ [DERS 22] |
| final gemi (G18) | +8 → +21,5 | 40,1 → 48,9 | 1328 → 1657 | 329 en | yalnız G18 |
| römorkör (G18) | +6 | 42,7 → 43,1 | 1685 → 1728 | — | yalnız G18 |

```
KAMERA SABİTLİK  ilk/son kare kayması ≤ 2 px [sahip kararı 19.09.2026] · 3 nirengi: baca · havuz kenarı · fener
```

---

## 3. YAPI BIBLE — sayılar (promptta kısmen, burada tam) [P2-b · DERS 36]

```
gemi LOA 130 · en 20 · derinlik 11 · keel −5,5 · güverte +5,5 · baş kasara +8,0 · köprüüstü +17,5 · baca +21,5
havuz 170 × 26 · kenar +1,5 · taban −7,0 · takoz 1,5 m · liman 0 · gemi suda −1,0'de kalkar, 0'da +1,0 m yukarıda
kubbe 20 kemer · 4 m ara · 18 m en · güverteden 13 m (+18,5) · incir 13 m (+3,0 basamakta · tepe +16,0)
geçici: kamyonlu mobil vinç (bom ≈ 35 m) · 6 tekerlekli iskele kulesi · rampa · 4 hurda konteyneri · konveyör ·
        teleskopik yükleyici · montaj portalı (KALICI)
```

### Yapı ve saha durumu — sahne sahne (② İNŞA · ④ TESLİM · ⑩ SEBEP için)

| S | saat | yapı: eleman + ara hâl | ölçülen kenar (kadraj) | geçici ekipman kadrajda | saha / ışık |
|:-:|:-:|---|:-:|---|---|
| S00 | 06:00→06:10 | kapaklar → yana · 3 ambar açık | açık ambar 0 → 3 | iskele · rampa · fidanlık · toprak | soluk sabah |
| S01 | 06:10→08:10 | kapak + 2 direk → hurda | direk 2 → 0 · konteyner 0 → 4 | + konteyner · telehandler | gölge −115° → −95° |
| S02 | 08:10→08:20 | delik → yeni levha | yama x 908 | kaynak perdesi | açık |
| S03 | 08:20→10:20 | pas → lacivert/gri/beyaz | renk sınırı x 172 → 1249 | raspa düzeneği | gölge −93° → −61° |
| S04 | 10:20→10:30 | çerçeve içeride · vinç gelir | demet 6 → 0 | + vinç · treyler | — |
| S05 | 10:30→12:30 | toprak %100 · incir askıya | yığın → 0 · incir asılı (705) | konveyör · vinç | gölge −57° → +8° |
| S06 | 12:30→12:40 | incir oturur | incir tepesi 620 | vinç (sapan) | öğle |
| S07 | 12:40→14:40 | yeşil ambar 1 → 3 | fidanlık 5 → 0 | vinç ve konveyör GİDER | gölge +14° → +60° |
| S08 | 14:40→14:50 | ilk sulama | ıslaklık | — | ikindi |
| S09 | 14:50→15:00 | portal + kemer 1 | kemer 1 (x ≈ 1067) | portal | — |
| S10 | 15:00→17:00 | kemer 1 → 18 · cam | ⭐ baş kenar x 1067 → 470 | portal · telehandler | gölge +64° → +87° |
| S11 | 17:00→17:10 | kemer 20 · cam tam | son panel x 416 | portal (park) | altın |
| S12 | 17:10→17:20 | teras korkuluğu · lamba hatları | — | — | altın |
| S13 | 17:20→17:30 | iskele ve rampa çekilir | iskele 6 → 0 | iskele GİDER | altın |
| S14 | 17:30→19:30 | havuz dolar · gemi kalkar | ⭐ borda bandı 38 → 48 px · uzak duvarda su | — | gölge +92° → +112° |
| S15 | 19:30→19:40 | kapılar açılır · römorkör bağlanır | kapı kanatları | römorkör | turuncu |
| S16 | 19:40→19:50 | gemi 0 → +60 m · ışık yanar (≈ 5 sn) | baş x 172 → 846 | römorkör | batış |
| S17 | 19:50→20:00 | gemi +60 → +150 m | ⭐ baş x 846 → 1328 | römorkör | mavi saat |

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
KANIT NESNESİ   tuğla baca — G0…G18 hepsinde x ≈ 100 px · üstten 418 → 671 · 253 px boy; zincirde her karede ELLE ✓/✗
İKİNCİ ÇAPA     yakın havuz kenarı (granit + babalar) — sol alttan (215, 892) kapılara (1332, 711)
⑤ İÇİN          dikiş = KARE (G1…G17): dikişin iki yakası aynı görsel; ⑤ REBUILT hükmü zincir koşulmadı demektir
⭐ GÖRÜNMEYEN SU — ölçülerek beyan: yakın havuz duvarı, havuzun içini +1,5'in altından örter. Suyun kanıtları:
   ① uzak duvarın iç yüzünde yükselen ıslak bant (x ≈ 813, üstten ≈ 752) ② kıç–kapı arasındaki 20 m'lik açık boşluk
   (x ≈ 1217–1328) ③ yakın borda bandının 38 → 48 px'e çıkışı (gemi 1,0 m kalkar). ⛔ Üçü de yoksa S14 düşer.
```

---

## 5. ⑧ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| eleman | kaynak (kadrajda nerede birikir) | geçici destek | ilk EKSİK kare | tamam kare | söküm karesi |
|---|---|---|:-:|:-:|:-:|
| açık ambar | kapaklar (zincir + vinç) | ray | G0 | G1 | — |
| hurda | kapak + direk → 4 konteyner | torç · telehandler | G1 | G2 | konteyner G3'te yok |
| yeni levha | telehandler çatalı | iskele kulesi · kaynak perdesi | G2 | G3 | — |
| boya | raspa düzeneği + hortum | iskele kuleleri · toz örtüsü | G3 | G4 | — |
| çerçeve | rıhtımdaki demetler | telehandler | G4 | G5 | — |
| toprak | yakın rıhtım yığını (x 461) | konveyör | G5 | G6 | konveyör G8'de yok |
| incir | yassı treyler | vinç + kısa sapan | G5 | G7 | vinç G8'de yok |
| ağaç, palmiye, eğrelti | fidanlık 5 sıra (x 972) | telehandler · rampa | G7 | G8 | fidanlık G8'de boş |
| kemer + cam | kıç ucu istif (G8) | portal (raylar) | G9 | G12 | portal KALICI |
| teras + lamba | güverte | — | G12 | G13 | — |
| su | liman → kapı savakları | — | G14 | G15 | — |
| çıkış | römorkör (havza) | çekme halatı | G15 | G18 | halatlı — G18'de hâlâ bağlı |

```
⑪ DAVETLİ LİSTESİ: tek gemi · tersane işçileri (iz) · telehandler · 4 hurda konteyneri · raspa düzeneği · kamyonlu vinç ve
                  treyleri · konveyör · iskele kuleleri · rampa · portal · tek römorkör (G15+) · uzak sac ambarlar · baca · fener.
                  ⛔ İkinci gemi, ikinci vinç, kule vinci, yük direği (G2'den sonra), tekne kalabalığı = INTRUDER [DERS 55].
⑩ SEBEP           her büyümenin sebebi bir önceki klipte GÖRÜNÜR: incir G6'da ASILI başlar (kaldırma G5→G6'da biter —
                  DERS 57); kemerler portalın deck'inden yükselir, havadan gelmez; su kapı savaklarından gelir.
```

---

## 6. ⑥ GEÇİŞ — kesme listesi ve ses

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · … · 136,0  (17 kesme, her 8,0 sn — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 yatay_2_dk_filmler/THE_EDEN_ARK/THE_EDEN_ARK_PLAN.md
                     tolerans kesme başına ±0,25 sn · betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE; kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                120 BPM · müziksiz pencereler 0,0–8,0 ve 112,0–120,0 · katmanlar 8 · 24 · 48 · 72 · (104 çekilir) · 120 ·
                     vuruşlar ≈ 53 ve ≈ 133 · final tutulan akor 142,0–144,0 → kartta söner
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. BÖLÜM SINIRI — G9 (S8 ↔ S9) [DERS 52]

```
İKİ DOSYA, BİR KARE  BOLUM_1'in son I2V'si G9 karesinde biter; G9 BOLUM_2'nin ilk görselidir.
ELLE KARE            ffmpeg -ss 72.0 -i teslim.mp4 -frames:v 1 sinir.jpg → üç ambar yeşil ve ISLAK · gölge +62° · ikindi
                     küme bulutu · kıç ucunda kemer ve portal istifi · iskele kuleleri yerinde
```

---

## 8. ⭐ PİLOT KAPILARI — üretim başlamadan

```
① YÜZEN GEMİ (G18 + G17 + S17): gemi tek gövde, uzaklaşırken boyu perspektifle KÜÇÜLÜR ama oranı değişmez;
   römorkör halatla bağlı; ışıklar yanık; baca ve fener yerinde.
② TEK KALDIRMA (G5 → G6 → G7 · S5 · S6) [DERS 57 · 22]: G5'te incir treylerde, kancada · S5 6,5–8,0 sn kaldırır ·
   G6'da ambar 2'nin 0,5 m üstünde asılı (treyler BOŞ) · S6 düz aşağı iner. ⛔ İki incir (treyler + ambar), boş kanca,
   saydamlıktan beliren ağaç = klip düşer.
③ YÜRÜYEN CAM (G10 → G11 · S10) [DERS 49 · P15-g]: kubbe kıçtan başa monoton büyür; her bölme beyaz kemerle ve gök
   yansımasıyla gelir. ⛔ Bir anda beliren kubbe, geri çekilen cam = klip düşer.
⛔ Üçü geçmeden kalan klipler üretilmez.
```

---

## 9. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç THE_EDEN_ARK_URETIM_GUNLUGU.md §0'a
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse araç değişir ya da karar sahibe (PLAN)
⛔ USTA KARE      G18 önce; kapı: final hiyerarşisi bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + tuğla baca ELLE (boy dâhil)
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4 (TAM master'a)
⛔ KAPAK KANITI   ffmpeg -ss 143.9 -i teslim.mp4 -frames:v 1 g18_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g18_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
⭐ KELİME KAPISI (yalnız prompt kod blokları — P23-f):
   cat THE_EDEN_ARK_BOLUM_1.md THE_EDEN_ARK_BOLUM_2.md | awk '/^### (📸|🎥)/{lab=$0} /^```$/{f=!f;next} f && tolower($0) ~ /(^|[^a-z])(ark|cruise|greenhouse|rainforest|eden)([^a-z]|$)/ {print lab}' | sort -u   → boş
   aynı komut "cranes?" ile → yalnız G5 · G6 · G7 görselleri + S4–S7 I2V'leri (7 blok)
   aynı komut "floats?|floating|afloat" ile → yalnız S14 · S15 I2V'leri + G15 · G16 · G17 · G18 (6 blok)
   aynı komut "tugs?" ile → yalnız G15 · G16 · G17 · G18 + S15 · S16 · S17 I2V'leri (7 blok)
   ⭐ 05.10.2026'da koşuldu, hepsi tuttu (ilk koşuda "floating" BIBLE'da 19 bloktaydı — DERS 56 kaçağı, düzeltildi).
```
