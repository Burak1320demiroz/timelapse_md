# THE_RAIN_TOWER — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 8 × 8,0 sn = 64,0 sn (⚠️ sahip istisnası 16.10.2026) · paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn = 37,0 sn
plan: dikey_shorts/THE_RAIN_TOWER/THE_RAIN_TOWER_DIKEY_TIMELAPSE.md (16.10.2026 · 8 sahne · kart beyanlı · kapı BLOCK 0 · FIX 2)
üretim günlüğü: dikey_shorts/THE_RAIN_TOWER/THE_RAIN_TOWER_URETIM_GUNLUGU.md — ⛔ BOŞ → durum "ÜRETİLDİ · GÜNLÜKSÜZ" [DERS 28]
yayın dosyası: ~/Downloads/"the reın tower.mp4" (16.10.2026 23:25) · sha256 9c0530d36572 · 37,01 sn · 2160×3840 · 30 fps · ses var · 2x
              (❶ ❷ dosyayı "teslim_2x.mp4" adıyla gördü — süre ve kurgu aynı; yeniden adlandırılmış kopya varsayıldı)
kaynak klipler: yerelde YOK (Downloads'taki gemini_generated_video_* dosyaları 1280×720 yatay — bu filme ait değil) → klip_eslestir koşulamadı
master: YOK (1x master dışa aktarılmadı; ❸ ❹ da 2x dosyayla koşuldu)
kapak: ~/Downloads/THE_RAIN_TOWER_Cover.jpg (1080×1920, 16.10.2026 23:18) — yayındaki kartla AYNI görsel
koşu tarihleri: beş mercek sahip koşusu, çıktılar 17.10.2026'da yapıştırıldı · ajan ölçümü 17.10.2026

## ⭐ AJAN ÖLÇÜMÜ — merceklerden ÖNCE okunur
ffprobe · kare farkı (54×96 gri) · 1 sn kare panosu · klip başına 4 fps pano · gök bandı (üst %15) mavi−kırmızı · ses
(volumedetect, 1 sn) · `araclar/kapak_prova.py` · kare panoları ajan gözüyle. Dosyalar: scratchpad `rt/` (sheet_1s · k0–k7 ·
cmp · grid · KAPAK_PROVA).

```
YAYIN KURGUSU (2x)        kaynak                         ölçüm
 0,00 –  4,00  S0 İNER         tam                              ✅ (zincir dikişi görünmez — kare farkı tepesi yok)
 4,00 –  8,00  S1 BOŞALIR      tam                              ✅
 8,00 – 12,00  S2 DOLAR        tam                              ✅
12,00 – 16,00  S3 BORULANIR    tam                              ✅
16,00 – 20,00  S4 KAYALANIR    tam                              ✅
20,00 – 24,00  S5 YEŞERİR      tam                              ✅
24,00 – 28,00  S6 TEPEYE ULAŞIR tam                             ✅
28,00 – 32,00  S7 AKAR (rejim G) tam · tutuş 29,75–32,00         ✅ (kaynak ≈ 4,5 sn — plan 4–8 sn)
32,00          SERT KESME → kart (erime yok · plan "≤ 1 sn" — uygun) · parlaklık 117 → 105
32,00 – 37,01  SABİT KART  "THE RAIN TOWER" · 5,0 sn · fark 0,01 (donmuş kare) ✅
SES            sahne bloğu −24…−41 dB (diegetik) · 32,0 −47,6 dB · 33–37 sn −91 dB = DİJİTAL SESSİZLİK
```

```
⛔ PLAN ↔ DOSYA UYUŞMAZLIKLARI
① KART SESİ   plan §SES: "kartta şelale sesi sürer, kartın son saniyesinde söner" · dosya: ses 32,0'da kesiliyor (❺ cat 8 yakaladı).
② BAŞLIK      plan KAPAK: başlık kutusu y 560–770 · dosya: y ≈ 290–465 (üst bant). kapak_prova: 3:4 sınırda · 4:5 "THE RAIN"
              yarıdan kesik · 1:1 başlık YOK. Sebep ölçüldü: G8'de kule plandan 1,5× uzun (aşağıda) → kutu kulenin üst gözüne
              biniyordu [DERS 94 tekrarı → DERS 99].
③ KULE ORANI  SPEC kule %27,2–58,3 (tepe y 800) · ekran kule y ≈ 444–1360 (%29–77) · genişlik ≈ 310 px (SPEC 324 ✅).
              Fabrika saçağı y ≈ 804 — kule saçağın bir göz üstünde (plan: tepe saçağın hemen üstünde).
④ ÇÖZÜNÜRLÜK  teslim 1080×1920 olmalı · dosya 2160×3840 (POOL ROOM E08'in aynısı).
⑤ KAYIT       üretim günlüğü boş · ihrac_kontrol / kesme_kontrol / qa_paket koşulmamış (❸ ❺ boş yer tutucuyla koşuldu) ·
              ❶ ❷ KÖR merceklere QA_SPEC eklendi [DERS 90 tekrarı → DERS 100].
```

```
✅ TUTANLAR (ölçüldü)
· kadraj kilidi — 1 sn panonun 32 karesinde kule, fabrika cephesi, kapı, baca aynı (❶ 10 · ❹ 7 ile uyumlu)
· ⭐ FİNAL (S7, rejim G): işçi kumanda kutusunda (28,0) · su YALNIZ taş ağızdan (28,5) · tek beyaz şerit dibe 29,0'da ·
  tutuş 29,75–32,0 · ikinci şelale yok, kiriş/kolon/borudan fışkırma yok → SKY STATION'ın hayalet suyu (DERS 67) finalde
  TEKRARLANMADI. Hazne finalde ince koyu bant olarak görünür (y ≈ 1310–1340) — plan bedeli (60 px) gerçekleşti.
· ⭐ GEÇ TESLİMAT 5/5 (DERS 92 kilidi): platform S2 10,5 · kaya paleti S3 15,0 · bitki paleti S4 19,25 · sarkan bitki
  paleti S5 ≈ 23,0 · platform park S6 27,5. Ana iş yine ERKEN: ızgara ≈ 0,5 sn · kaya ≈ 0,75 sn · yeşil ≈ 0,5 sn (yayın).
· VİNÇ YALNIZ S0 (onaydan sapma ⑤): sepetli platform + palet zinciri ekranda malzeme kaynağı olarak okundu (❹ cat 7: 7/10).
· KART G8 dünyasından (DERS 85 dersi uygulandı) — kapak = kart, son sahne karesiyle aynı kadraj (alt yarı fark 9,7, renk).
· AÇILIŞ: kabin ilk karede iniyor (❺ HOOK 10) · kabin bedel/kafiye olarak okundu (❺ COST 10 · LOOP 9).
· Güneş tek yay: sabah sağdan, akşam soldan; gölgeler sola → sağa (❷ 1: 7).
```

## ⭐ PROMPT ↔ EKRAN — sahne sahne (yayın 2x · kaynak = 2 × klip içi sn · ajan 4 fps panosu · rapor eşleşmesi)

| S | prompt ne istedi (MOTION FOCUS · saniye) | ekranda ne oldu (yayın sn) | tuttu mu | rapor ne dedi | olay · ders |
|:-:|---|---|:-:|---|---|
| 0 | kabin kuyunun sağında İLK KAREDE iniyor · takozlara oturur (1–5) · zincir sökümü (5–6,5) · vinç bomu toplar, **sağ kenardan** çıkar (6,5–8) | iniş 0,0–1,75 ✅ · toz bulutu 1,5–2,0 · vinç 2,75'e kadar bekler · 3,0–3,5 **SOLA**, kulenin önünden ve kabinin üstünden geçer · kabin 3,25'te bulanıklığın arkasında ≈ 100 px **sağa** sıçrar · G0 kabini kilidin solunda (≈ 600–745 px · SPEC 728–831) | ½ | ❶ cat 7/8 ✓ · ❸ "teleports" ✓ · ❺ HOOK 10 | E01 · DERS 96 |
| 1 | rampa eşiğin üstünden **çukura** · moloz iki arabayla kapıya (0–5) · rampa duvara (6–7) · kısa boru vanadan eşiğe (7–8) | rampa kulenin İLK KİRİŞİNE dayandı · üç araba (plan iki) 4,25–5,25 ✅ · **5,75'te avlunun ortasında dikdörtgen çukur açıldı, rampa içine indi, 6,75'te kapandı** · dört işçi uzun boru 7,0–7,5 ✅ | ❌ | 5/5 mercek gördü · ❶ en kötü eriyen cisim · ❹ ilk beliren parça | E02 · DERS 95 |
| 2 | vana · su boru ucundan **çukurda, yüzeyin altından** kabarır, taş sıra taş sıra (0–5,5) · durur (5,5–6,5) · platform + palet kapıdan (6,5–8) | su 8,25–9,75 boru ucundan **yay çizerek avluya** fışkırdı, avluda göllendi · üst gözde desteksiz sarı sepet 8,25–9,75 · bulutlar hızlı, sonra donuk · platform 10,5 ✅ · palet 11,25 ✅ | ❌ / teslimat ✅ | ❶ ❸ ❹ sepet ✓ · ❷ "su avluya" ✓ · ❺ "direnç: basınçlı su" (hikâye okudu) | E03 · E04 · DERS 95 · 67 |
| 3 | platform yükselir · ızgara raylar arasında **sıra sıra** (0–5) · boru sağ arka köşe + taş ağız (5–6,5) · pompa (6,5–7,5) · kaya paleti (7,5–8) | ızgara 12,5–13,0'te üç katta birden · 12,75 ızgara küpü kule ÇATISININ ÜSTÜNDE · pompa 13,0 ✅ · **13,75 ikinci platform sağda, soldaki kayboldu**, aynı karede gök parlaması · 15,0 kaya paleti ✅ · 15,75 platform yine solda | ❌ / teslimat ✅ | ❶ ❷ ❸ ❹ platform ✓ · ❸ "growth nobody made 0:13" ✓ | E05 · E06 · DERS 92 · 96 |
| 4 | kaya panelleri sepetle, **suyun üstünden tepeye** sıra sıra (0–6) · kanal oluklu, kuru (6–7) · bitki paleti (7–8) | kaya **ÜSTTEN** başladı (iki üst göz 17,0 · alt göz 17,5) · 16,25 fabrika çatısında figür · **17,75–20,0 kule çatısında 2–3 figür** · bitki paleti 19,25 ✅ · kanal ortada ✅ | ½ / teslimat ✅ | ❹ "top-down" + en zararlı davetsiz ✓ · ❶ cat 5 ✓ | E07 · DERS 97 |
| 5 | bitkili modüller **alt iki banda** (0–6) · kanal kuru (6–7) · sarkan modül paleti (7–8) | bitki önce **ÜST gözde** (21,0) · 21,75–22,5 gök kapalı griye döndü · 22,0 alt bantlar tek seferde · üst göz geri gitti · palet sol → sağ → orta · sarkan modül paleti ≈ 23,0 ✅ | ❌ / teslimat ✅ | ❹ regresyon ✓ · ❷ cat 3 ✓ · ❸ idle ½ | E07 · E08 · E09 · DERS 97 · 98 |
| 6 | sarkan modüller üst ceplere (0–5,5) · sepet iner, platform kapı yanına park (5,5–7) · paletler içeri, işçi pompaya (7–8) | yeşil üst gözü doldurdu ✅ · gök 24,75'te **turuncu**, 26,25–27,5 **yeniden mavi**, 27,75 G7 altını · platform geri geri sola, 27,5'te küçük, öne bakan park pozuna sıçradı · palet + torbalar silindi · işçi pompada 27,5 ✅ | ½ | ❷ cat 3/5 ✓ · ❸ "snaps" ✓ · ❺ "mist test" (görülmedi) | E09 · E10 · DERS 98 |
| 7 | el düğmeye (0–1) · su taş ağızdan taşar (1–2,5) · kanaldan iner, köpük halkası (2,5–4) · tutuş (4–8), seviye aynı | düğme 28,0 ✅ · taşma 28,5 · dipte 29,0 ✅ (kaynak 1,0–2,0 — plan 1,0–4,0, hızlı ama yol görünür) · **29,25–29,75 dipte büyük beyaz sis patlaması** · tutuş 29,75–32,0 ✅ | ✅ (sis sınırda) | ❶ C3 ✓ · ❷ 8: 10 · ❺ FINAL BEAT PASS | E11 · DERS 92 2. ölçüm |
| kart | G8 + "THE RAIN TOWER", y 560–770 · 5,0 sn · erime ≤ 1 sn · şelale sesi sürer | sert kesme ✅ · G8 dünyası ✅ · başlık y ≈ 290–465 ❌ · ses kesik ❌ | ½ | ❶ C5 10 · ❹ C1 10 · ❺ C2 10 + ses ✓ | E12 · E13 · DERS 99 · 100 |

```
ÖZET   Prompt'un MEKÂN dili (kamera, cephe, kapı, baca, tek kabin) TUTTU. FİNAL dili (rejim G, tek kaynak, tek şerit) TUTTU —
       bu depoda su finalinin ilk temiz tutuşu. GEÇ TESLİMAT TUTTU (5/5). Kopanlar dört aile:
       ① GÖRÜNMEYEN HEDEF — eşik arkasındaki çukura yazılan rampa ve dolum avluda çukur + fışkırma oldu (DERS 95, S1–S2);
       ② KONUM ÇELİŞKİSİ — uç kare ile klip içi iş noktası ayrışınca kabin sıçradı, platform ikiye çıktı (DERS 96, S0 · S3);
       ③ SIRA — "aşağıdan yukarı" tepeden geldi, "to the top" çatıya insan çıkardı (DERS 97, S4 · S5);
       ④ GÖK — rejim B'de renk ileri geri (DERS 98, S5 · S6).
       Usta kare oranı tutmadı → kapak başlığı yer bulamadı (DERS 99). Teslim kilitleri kurguya inmedi (DERS 100).
```

## MERCEKLER
| mercek | durum | puan | hüküm | ham | en ağır üç bulgu (m:ss.s) · ajan notu |
|---|---|:-:|---|---|---|
| ❶ GÖRÜNTÜ | YANLIŞ GİRDİ + SIZINTI | — (bağlayıcı değil: 6,4) | TIMELAPSE · MELTING | THE_RAIN_TOWER_Q1_GORUNTU_HAM.md | 0:06–0:07 avlu çukuru (E02 ✓) · 0:03 vinç kabinin içinden (E01 ✓) · 0:14 platform ışınlanır (E06 ✓) · ⛔ QA_SPEC ekli; sorular planı biliyor |
| ❷ ZAMAN VE KESME | YANLIŞ GİRDİ | — (bağlayıcı değil: 7,3) | PASSING · TIME | THE_RAIN_TOWER_Q2_ZAMAN_KESME_HAM.md | 0:22 gri gök (E09 ✓ ölçüldü) · 0:24–0:25 renk basamağı (E09 ✓) · 0:14 parlama (E06 ✓) · ⚠️ kesme tablosu "~2 saat" — zincirde zaman klip İÇİNDE akar, kesme dikişsiz |
| ❸ ŞANTİYE | EKSİK (boş blok · D2 · D4) | — (bağlayıcı değil: 2,9) | SAME WORLD · WORKING | THE_RAIN_TOWER_Q3_SANTIYE_HAM.md | 12 klip saydı; "dikişleri" klip içi olaylar ve doğru (çukur · torbalar · palet takası · platform sıçraması) · finalde park/kabin "terk" okundu (plan kasıtlı) |
| ❹ İNŞA | TAM (mod V) | 5,5 | SAME · BUILT · INTRUDERS | THE_RAIN_TOWER_Q4_INSA_HAM.md | 0:06 çukur APPEARED (E02 ✓) · 0:16–0:19 çatı figürleri (E07 ✓) · 0:17 / 0:21 tepeden aşağı (E07 ✓) · D4 evre sınırları 1 sn kaymış |
| ❺ TESLİM | TAM (mod V) | 9,0 | ENDS | THE_RAIN_TOWER_Q5_TESLIM_HAM.md | final PASS (✓ ölçüm) · kart sessizliği (E13 ✓ ölçüldü −91 dB) · ⚠️ ŞİŞİK riski: E03'ü "direnç" diye övdü, 0:25 "mist test" görülmedi |
FİLM PUANI  7,3 · N=2 (❹ 5,5 · ❺ 9,0)          ÖLDÜRÜCÜ  — (❶ SEPARATE IMAGES · ❸ REBUILT · ❹ DIFFERENT yok)
⚠️ PUAN BAĞLAYICI DEĞİL: kör üçlünün hiçbiri TAM değil (❶ ❷ belgeli, ❸ paketsiz). Hüküm satırları NONE değil:
❶ en kötü eriyen cisim (S1) · ❸ büyüme (S3, S1) · ❹ ilk beliren parça (S1) + en zararlı davetsiz (S4) → S1 · S3 · S4 yeniden
üretim adayıdır, ortalama ne olursa olsun [AGENTS kart R 6].

## DOĞRULAMA
- Geri okuma: ❶ ✗ teslim_2x.mp4 / ⛔ QA SPEC / 8+kart · ❷ ✗ teslim_2x.mp4 / ⛔ QA SPEC / 8+kart · ❸ ✗ "video" / NONE / 12 · ❹ ✗ UNSPECIFIED / NONE / 8+kart · ❺ ✗ NOT SHOWN / NONE / 8+kart
- D1: hiçbir raporda dosya dışı damga yok (❸ 0:37.3 — 0,3 sn fazla, kabul) · D2: ❸ 12 klip ✗, diğerleri 8 ✓ · D3: süre itirazı yok ·
  D4: ❸ 11 "kesme"nin 10'u gerçek kesmeden (4,0 · 8,0 … 28,0) > 0,5 sn uzak ✗ · ❹ evre sınırları 0:11 · 0:15 · 0:19 (gerçek 12 · 16 · 20) ✗ ·
  ❶ ❷ ❺ ✓ · D5: kart VAR, beşi de gördü ✓ (POOL ROOM'dan farklı) · D6: ❶ ❷ ❹ ❺ kurgu tablosu 1 sn panoyla tutuyor · ❸ tutmuyor (ŞİŞİK değil, ZAYIF).
- Sızıntı taraması: ❶ — sayı yok ama SORU 1 "kulenin hemen altındaki eşik" ve SORU 2 "sağ kenardan çıkmak yerine" planın S0 ve SPEC
  satırları (ekranda sağdan çıkış hiç görünmedi) → SIZINTI. ❷ — sayı yok, güneş açısını SORUYOR; "kuru kanallı kaya yüzü" tek şüpheli ifade
  (görüntüden de okunur) → kanıt yok. ❸ belgesiz ✓ temiz.

## DOKÜMAN

### ❶ GÖRÜNTÜ
1. **Avludaki çukur:** Planlanmadı. Plan: hazne = kulenin İÇİNDEKİ eski asansör çukuru (taban −1,50), 0,50 m beton eşiğin arkasında; tilt 0'da görünmez. Avludaki çukur model uydurması → E02 · DERS 95.
2. **Vincin sola geçişi:** Beyanlı değil. Plan S0 6,5–8 sn: "vinç bomunu toplar ve sağ kenardan çıkar". → E01.
3. **Üst gözdeki sarı sepet:** Planda yok. Sepetli platform S2'nin son 1,5 sn'sinde (kaynak 6,5–8) kapıdan çıkar; S2'nin başında hiçbir yerde sepet yok. → E04.
4. **Platformun soldan sağa geçişi:** Planlı değil. Plan platformu kulenin solunda tutar; boru sağ arka köşeye sepetten takılır. → E06 · DERS 96.
5. **Çatı figürleri:** Planlanmadı. Yükseklikte yalnız sepetteki iki işçi var. → E07 · DERS 97.

### ❷ ZAMAN VE KESME
1. **Güneş:** G0 78°/+4,2° · G1 79°/+6,0° · G2 99°/+28,6° · G3 126°/+49,5° · G4 175°/+61,0° · G5 228°/+52,4° · G6 257°/+32,3° · G7–G8 278°/+9,8° (41° K, güneş saati). Güneş hiçbir saatte kadraja girmez — 13,75'teki parlama plan dışı (E06).
2. **Mevsim ve tarih:** 20 Ağustos, tek gün ("yaz sonu" okuması doğru).
3. **Süreler:** S0 10 dk (rejim A) · S1–S6 2'şer saat (B) · S7 8 sn (G) · toplam 05:40 → 17:50 + 8 sn. ⚠️ İki keyframe zincirinde KESME zaman sıçraması değildir (S(n) son karesi = S(n+1) ilk karesi); zaman klibin İÇİNDE akar. Raporun "kesmede ~2 saat" okuması klip içi değişimin kesmeye atfı.
4. **Gerçek zamanlı tutuş:** Evet, Klip 8 (S7, rejim G).
5. **24–25 sn basamağı:** Kasıtlı değil. S6 15:50 → 17:50 doğrusal ısınmalıydı; gök 24,75'te turuncuya gidip 26,25'te maviye döndü (gök bandı +120 → +7 → +90) → E09 · DERS 98.

### ❸ ŞANTİYE
1. **12 klip mi:** Hayır — 8 × 4,0 sn (yayın) + kart 5,0 sn; kesmeler 4,0 · 8,0 · 12,0 · 16,0 · 20,0 · 24,0 · 28,0 · kart 32,0. Raporun "dikişleri" klip içi olaylardır.
2. **Kabin:** Kuyudan çıkan eski yük kabini; takozlarda TANIK NESNE olarak kalır, finalde şelaleyle aynı karede geçmişi taşır (plan TASARIM ④ · BEDEL). Kasıtlı.
3. **Avlu çukuru:** Planlanmadı (yukarıda) → E02.
4. **Platform finalde kapı yanında:** Kasıtlı — S6 "platform katlanıp kapı yanına park", G7–G8 kilidi. ⚠️ ❸ ve ❹ bunu "terk edilmiş saha" okudu; ❺ kabini bedel okudu. Karar notu aşağıda.
5. **8,0–9,9 su:** Planlanmadı. Plan: su vanadan sabit boruyla çukura, yüzeyin altından sessiz dolum; pompa S3'te kurulur (ekranda 13,0 ✓) → E03.

### ❹ İNŞA (mod V)
1. **Hazne:** Kazı yok; mevcut asansör çukuru hazne. Finaldeki beyaz "bordür" planın 0,50 m beton eşiği — dokuz karede olmalıydı; 27,0'de ortaya çıkışı plan dışı.
2. **Sıra:** Plan aşağıdan yukarı: kaya tek klipte (S4), bitki iki klipte (S5 alt bantlar · S6 üst bant). Ekranda tepeden aşağı → E07 · DERS 97.
3. **Söküm hattı:** Kabin kalıcı (bedel); platform S6'da kapı yanına park, G7–G8'de katlı. Vinç S0 sonunda çıkar.
4. **Üst gözdeki platform · çatı figürleri:** İkisi de plan dışı; promptlarda yükseklikte yalnız sepetteki iki işçi var.
5. **Kart:** Ayrı kapak kartı (END CARD YES) — G8 + başlık, 5,0 sn.

### ❺ TESLİM
1. **Kimlik sürprizi:** Kasıtlı. Açılış merak sorusu "What will fill this empty shaft?"; ad yalnız sondaki kartta, kaya S4'te, yeşil S5'te gelir.
2. **Tutuş ve hız:** S7 4–8 sn (yayında 30,0–32,0 = 2 sn) · paylaşım 2x. Ölçülen tutuş 29,75–32,0 ✓.
3. **Kabin pompa kutusu mu:** Hayır. Kabin tanık nesne; pompa + kumanda kutusu vana dikmesinin yanında (S3). Yan yana durmaları plan yerleşimi.
4. **Kartta sessizlik:** Kasıtsız — plan: kartta şelale sesi sürer, son saniyede söner → E13.
5. **Kapak ve beyan:** Kapak = G8 + "THE RAIN TOWER" (KAPAK dosyası). Açıklama metni: "Every frame is generated with AI. This is not a record of a real project" + TR satır; yüklemede Altered Content işaretlenir.

## OLAY TABLOSU
| olay | zaman (yayın 2x) | ne oldu (görünen) | mercekler | kanıt | karar |
|---|---|---|---|---|---|
| E01 | 3,0–3,75 (kaynak S0 6,0–7,5) | Vinç SOLA, kulenin önünden geçti (plan: sağ kenardan); kabin vinç bulanıklığının arkasında ≈ 100 px sağa sıçradı. G0'da kabin kilidin solunda asılı, G1'de kilitte | ❶ ❸ ❹ ❺ | k0 2. satır | S0 yeniden adayı (düşük) — G0 kabin x'i G1 oturma yerine hizalı · çıkış yolu yazılı [DERS 96] |
| E02 | 5,75–6,75 (kaynak S1 3,5–5,5) | ⭐ Avlunun ortasında dikdörtgen çukur açıldı, rampa içine indi, 1 sn sonra beton otlarıyla geri geldi. Plan çukuru eşiğin arkasında, görünmez | ❶ ❷ ❸ ❹ ❺ (5/5) | k1 · sheet_1s 6 | ⛔ S1 yeniden — ama prompt düzeltmesi yetmez: hazne görünürlüğü PLAN sorunu [DERS 95] |
| E03 | 8,0–10,0 (kaynak S2 0–4) | Su boru ucundan yay çizerek avluya fışkırdı, avluda göllendi; göl 14,5 civarında iz bırakmadan kurudu | ❷ ❸ ❹ ❺ | k2 | ⛔ S2 yeniden — E02 ile aynı kök (görünmeyen hazne) [DERS 95 · 67] |
| E04 | 8,25–9,75 | Kulenin üst gözünde bomsuz, desteksiz sarı sepet belirip kayboldu | ❶ ❸ ❹ ❺ | k2 1. satır | S2 yeniden olursa "the folded boom lift waits inside the factory until late in the shot" — kök belirsiz |
| E05 | 12,5–13,0 | Izgara üç katta tek seferde (yayın 0,5 sn); 12,75 ızgara küpü kule çatısının üstünde | ❸ ❹ | k3 1. satır | DERS 92 tekrarı (kabul) · küp [DERS 97] |
| E06 | 13,75–15,75 | İkinci platform sağda belirdi, soldaki kayboldu; sağdaki indi; 15,75'te yine solda. Aynı karede sağ üst gökte parlama (plan güneşi kameranın arkasında) | ❶ ❷ ❸ ❹ ❺ | k3 · sky (S3 +117 → +80) | S3 yeniden adayı — tek iş noktası, boru sepetten bom açısıyla [DERS 96] |
| E07 | 16,25–20,0 · 21,0–22,5 | Kaya tepeden aşağı; kule çatısında 2–3, fabrika çatısında 1 figür; S5'te bitki önce üst gözde, sonra alt bantlar, üst göz geri gitti | ❶ ❷ ❸ ❹ | k4 · k5 | S4 yeniden adayı (❹ en zararlı davetsiz) · S5 düşük [DERS 97] |
| E08 | 6,0–10,0 · 18,5 · 22–24 · 27,0 | Beyaz torbalar git-gel; palet malzemesi taş → bitki; bitki paleti sol → sağ → orta → sol; palet ve torbalar silindi | ❶ ❸ ❹ | k1 · k4 · k5 · k6 | kabul (küçük) — dikişte yük takası ailesi [DERS 74 · 96] |
| E09 | 9,0–10,25 · 21,75–22,5 · 24,75–27,75 | Gök ileri geri: S2 hızlı bulut → donma · S5 bir saniye kapalı gri · S6 turuncu → mavi → altın (gök bandı +120 → +7 → +90) | ❷ (3 · 4 · 5) · ❸ (lens 2) | sky ölçümü · k5 · k6 | S6 yeniden adayı (orta) — yönlü gök cümlesi [DERS 98] |
| E10 | 26,5–27,5 | Platform geri geri sola; 27,5'te küçük, öne bakan park pozuna sıçradı (park plan gereği, sıçrama değil) | ❸ | k6 2. satır | kabul — park yeri G7'de kapının hemen yanında, iniş yolu yazılı olsaydı kısalırdı |
| E11 | 29,25–29,75 | Şelalenin dibinde büyük beyaz sis patlaması, 0,5 sn'de dar akışa çekildi | ❶ C3 | k7 1. satır | kabul (sınırda) — plan "sis kuyuyu örterse at": kuyu örtülmedi |
| E12 | kart 32,0–37,0 · kapak | Başlık y ≈ 290–465 (plan 560–770); 4:5 yarım, 1:1 yok. Kök: G8'de kule 1,5× uzun (tepe y ≈ 444) | — (mercekler kartı "güvenli" dedi) | KAPAK_PROVA · grid | kapak yeniden yerleşim: başlık 1:1'de okunacak bantta — kule tepesinin üstünde boşluk yok → küçük punto ya da tek satır; kalıcı çözüm G8 [DERS 99] |
| E13 | 32,0–37,0 | Ses 32,0'da kesildi, 33–37 dijital sessizlik (−91 dB); plan: şelale sesi sürer, son saniyede söner | ❺ | volumedetect | yeniden kurgu — ses kuyruğu (S7 şelale sesi 5 sn uzatılır, son 1 sn söner) |
| E14 | tüm film | Teslim 2160×3840 (plan 1080×1920) | — | ffprobe | yeniden ihraç: 1080×1920 [POOL ROOM E08] |
| E15 | kayıt | Günlük boş · qa_paket koşulmadı · kör ❶ ❷'ye QA_SPEC eklendi · ❸ ❺ boş yer tutucularla koşuldu | ❸ ❺ (kendileri söyledi) | ham künyeler | ❶ ❷ ❸ yeniden koşulmalı (geçici sohbet, belgesiz, paketle) [DERS 100] |

## KARAR

⭐ **SAHİP KARARI BEKLİYOR** — öldürücü hüküm yok, film kendi içinde BİTİYOR (❺ ENDS · final ölçümle tuttu).

- **Önce yeniden kurgu (ucuz, klip üretimi yok):** kartta şelale sesi (E13) · 1080×1920 ihraç (E14) · kapak/kart başlığı 1:1 provasında okunacak yere (E12). Sonra `ihrac_kontrol.sh` + `kapak_prova.py`.
- **Yeniden üretim adayları (öncelik sırasıyla):**
  1. **S1 + S2 (E02 · E03 · E04)** — beş merceğin beşi gördü; filmin en görünür kusuru. ⚠️ Prompt düzeltmesi yetmez: hazne kadrajda görünmüyor (plan TASARIM ⑧). İki yol, sahip seçer: (a) dolum beat'i görünen taşıyıcıya bağlanır — "eşiğin üstünde arka duvar taşlarında yükselen koyu bant", rampa eşiğin arkasında biter (DERS 95 ②③) ve G2/G3'te bant ≥ 40 px çizilir; (b) S2'nin işi değişir (dolum ekran dışı, S2 ızgara + boruyu üstlenir), S3 kaya ve S4–S6 yeniden dağıtılır — zincir değişir.
  2. **S3 (E06)** — ikinci platform. Tek iş noktası, boru sepetten bom açısıyla; G4 korunur.
  3. **S4 (E07)** — çatı figürleri (❹ en zararlı davetsiz). Sepet G4'te en alt sırada çizilir → G4 düzenlenirse S3'ün bitişi de değişir.
  4. **S6 (E09)** — gök ileri geri; yönlü gök cümlesiyle yalnız I2V yeniden (uç kareler kalır).
  5. **S0 (E01)** — düşük; G0 kabin x'i düzenlenirse yalnız S0.
- **Kabul edilen:** E05 (DERS 92 bilinen davranış) · E08 · E10 · E11.
- **Kasıtlı ama okunması tartışmalı:** finalde katlı platform ve kabin. ❺ kabini bedel ve kafiye diye okudu (COST 10 · LOOP 9); ❸ ❹ platformu "terk edilmiş ekipman" okudu. Öneri: kabin kalır (planın bedeli); platform G7'de kapıdan İÇERİ alınır — sonraki filmlerde finalde yalnız yapının kendi parçaları ve tek işçi.
- **QA yeniden koşulur:** kurgu düzeldikten sonra `qa_paket.sh --hiz 2` (günlük §0 doldurulmadan araç durur); ❶ ❷ ❸ geçici sohbette BELGESİZ; ❹ ❺ plan + QA_SPEC (+ kapak) ile mod D.

## DERS
- DERS 92 — 2. ölçüm: geç teslimat 5/5 tuttu, ana iş yine erken (ek satır)
- DERS 95 — Görünmeyen hedefe yazılan eylem: model hedefi görünür yere çizdi, son kare onu geri sildi
- DERS 96 — Uç karelerdeki konum klip içi yolla çelişince nesne ışınlandı ya da ikiye çıktı
- DERS 97 — "Aşağıdan yukarı" yazıldı, montaj tepeden geldi; "to the top" çatıya insan çıkardı
- DERS 98 — Gök ve renk sıcaklığı klip içinde ileri geri gitti; "aynı hız" cümlesi gökte tutmadı
- DERS 99 — Usta karede kule plandan 1,5× uzun çıktı: başlık kutusu yerini kaybetti, kapak kırpmada kesildi
- DERS 100 — POOL ROOM'un teslim dersleri ikinci filmde kurguya ve QA koşusuna inmedi
