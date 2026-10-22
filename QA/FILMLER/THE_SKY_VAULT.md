# THE_SKY_VAULT — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 8 × 8,0 sn = 64,0 sn (⚠️ sahip istisnası 20.10.2026) · paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn = 37,0 sn
plan: dikey_shorts/THE_SKY_VAULT/THE_SKY_VAULT_DIKEY_TIMELAPSE.md (20.10.2026 · 8 sahne · kart beyanlı · kapı BLOCK 0 · FIX 1)
üretim günlüğü: dikey_shorts/THE_SKY_VAULT/THE_SKY_VAULT_URETIM_GUNLUGU.md — ⛔ BOŞ ("DURUM ⛔ BOŞ — araç kapısı KOŞULMADI") → durum "ÜRETİLDİ · GÜNLÜKSÜZ" [DERS 28]
yayın dosyası: raporlarda "the sky vault.mp4" (❹) · 0:37.0 · 9:16 — ⚠️ AJAN OKUYAMADI (yol ~/Downloads · macOS izni "Operation not permitted") → sha256 · ffprobe · çözünürlük · fps · ses YOK
master: bilinmiyor (❸ ❹ 2x dosyayla koşuldu — "GRABS NOT SUPPLIED")
kapak: bilinmiyor (❺ "cover: NOT SUPPLIED")
koşu tarihleri: beş mercek sahip koşusu, çıktılar 20.10.2026'da yapıştırıldı · ajan ölçümü YAPILAMADI

## ⭐ AJAN ÖLÇÜMÜ — merceklerden önce okunur
⛔ **YAPILAMADI.** Yayın dosyası ajan makinesinde okunamadı (`ls ~/Downloads` → Operation not permitted); `klip_eslestir.py`, `kapak_prova.py`,
1 sn kare panosu, 4 fps klip panosu, ses kuyruğu ve gök bandı ölçümü KOŞULMADI. Bu kayıttaki her "ekranda ne oldu" satırı **mercek raporundan**
gelir; kare kanıtı yoktur. Ölçüm yapılana kadar D6 ve olayların "kanıt karesi" sütunu açık kalır.

```
YAYIN KURGUSU (2x · PLAN beklentisi — dosyayla DOĞRULANMADI)
 0,00 –  4,00  S0 KABUK AÇILIR      panel iner · vinç çıkar · yan paneller        ⏳ klip_eslestir koşulmadı
 4,00 –  8,00  S1 İÇİ BOŞALIR       borular · tortu · alet seti
 8,00 – 12,00  S2 KABUK KÖMÜRE DÖNER tel fırça → rulo
12,00 – 16,00  S3 MEŞE DÖŞENİR      iç zemin · deck · sargılı berjer
16,00 – 20,00  S4 ODA KURULUR       berjerler · sehpa · ışık · cam arabası
20,00 – 24,00  S5 CAMLAR TAKILIR    üç filmli cam · cam arabası çıkar · korkuluk + saksı arabası
24,00 – 28,00  S6 TERAS TAMAMLANIR  korkuluk · saksılar · gün batımı
28,00 – 31,87  S7 FİLM SOYULUR (rejim A) · tutuş 30,0–32,0
32,00 – 37,00  KART G8 + "THE SKY / VAULT" (plan §SES: çatı rüzgârı sürer, son saniyede söner)
```

```
⛔ PLAN ↔ RAPOR UYUŞMAZLIKLARI (dosya ölçülemediği için "iddia")
① KLİP SAYISI   plan 8 × 4,0 · ❶ ❷ "6 klip × 5,0 sn" · ❸ ❹ "31 klip × 1,0 sn" · ❺ "8 klip" (sınırlar 4·8·12·16·20 → 23 · 27 · 31,5)
② MÜZİK         plan müziksiz · ❷ "MUSIC = YES · her kesme bite denk" · ❶ "sound effects" · ❺ "rooftop ambiance … C1 MUSIC NOT TRIGGERED"
                → müzik iddiası yalnız ❷'de; ❷'nin kesme ızgarası uydurma → iddia güvenilmez (kulakla DOĞRULANMADI)
③ KART SESİ     plan "çatı rüzgârı sürer, kartın son saniyesinde söner" · ❺ "end card is silent from 0:32.0 to 0:37.0" (⚠️ ölçülmedi —
                RAIN TOWER E13 · HIDDEN LOFT E13'ün aynısı olabilir)
④ BAŞLIK YERİ   plan kutusu y 560–770 (üstten) · ❶ "19–81 % W, 68–83 % H" (alttan) ≈ y 326–614 (üstten) — ⚠️ ❶'in ufku %56 (plan %50) → ±6 puan
                sapma; yön DERS 99'un yine (5. film) aynısı gibi okunuyor (≈ 100–230 px yukarı) · kapak_prova KOŞULMADI
⑤ ÇÖZÜNÜRLÜK    plan 1080×1920 · dosya ölçülemedi (son üç film 2160×3840 çıktı)
⑥ NİRENGİ       ❶ üç bina % W aralıkları (8–14,5 · 28–43,5 · 83,5–96,5) plan px konumlarıyla (1–10 · 19–24 · 80–87 %) örtüşmüyor →
                ya ❶ yüzdesi ± ya kadraj; zincir_kontrol / nirengi ölçümü gerekir
⑦ KAYIT         günlük boş · qa_paket / ihrac_kontrol koşulmadı · beş mercek ölçülmüş olgular bloğu BOŞ (yer tutucu) koşuldu — DÖRDÜNCÜ film
```

```
✅ TUTANLAR (raporlarda — ajan doğrulaması bekliyor)
· kamera kilidi: ❶ CAMERA LOCK 7 (kare çifti yok → tavan 7) · FRAME AND ANCHOR 10 — üç bina dokuz karede aynı · ❸ "A çerçeveli raf 0:00 ↔ 0:30 aynı"
  (plan tanığı) · ❹ SCALE TABLE 0 % kayma — DERS 11 / HOME kilidi tuttu (rapor)
· kart = son sahne: ❶ SAME · ❹ C1 10 · ❺ C2 10 — DERS 85 (kart = G8 dünyası) 3/3 mercekte tuttu
· final tutuşu: ❶ ❷ ❸ ❹ "2,0 sn · 30,0–32,0" (plan tutuşu 2,0) · ❺ 30,0–31,5 — DERS 92 ikinci yarı geç teslimat bu filmde tutuşu bozmadı
· SAME WORLD (❸) · SAME (❹) · TIMELAPSE (❶) · ENDS (❺) — beş olumlu hükmün hepsi gerçek
· paslı paneller rafta kalır (plan "kafiye") ❸ ❹ okudu — plan kararı (beyanlı)
```

## ⭐ PROMPT ↔ EKRAN — sahne sahne (yayın 2x · RAPORDAN · kare kanıtı YOK)

| S | prompt ne istedi | ekranda ne oldu (rapor · yayın sn) | tuttu mu | hangi mercek | olay |
|:-:|---|---|:-:|---|---|
| 0 | panel askıda → 1,0'a dek rafa iner · vinç 1,0–1,5'te sol kenardan çıkar · yan paneller TEK TEK elle rafa · ipucu: el arabası | 0,0–1,0 vinç + katlı merdiven + panel YERİNDE silindi, raf üç panelle belirdi · 1,0–2,0 sol panel yerinde silindi · 3,0 sağ panel gerilip geniş bulanık levha oldu, 4,0'te rafa eklenmeden yok · 3,9–4,0 işçi yeleği sarı → lacivert (yalnız ❸) | ❌ | ❶ ❸ ❹ ❺ (E01) · ❶ ❸ ❹ (E02 · E03) | E01 · E02 · E03 |
| 1 | boru TEK TEK elle → açık yüz → el arabası · tortu kürek → çuval · alet seti | 4,0 boru yığını kürekle toprak gibi küçüldü (❶ ❷) · 5,9–6,0 yığının tamamı bir anda yok, çuvallar kendiliğinden 3×3 istif (❸ ❹) · 6,0–7,0 sabit el arabasında çuvallar kovalara döndü (❶ ❷ ❸ ❹) · 7,0–8,0 gümüş merdiven sağdan sola sıçradı (8,0 dikişi) | ❌ | ❶ ❷ ❸ ❹ | E04 · E05 · E06 |
| 2 | tel fırça → gri → kömür (rulo, dikey şerit) · boya takımı → merdiven evi | 9,0 iç duvar gri, 10,0–11,0 dış kabuk mat siyah "step-frame fade" (❶ ❸ ❹: boyacısız) · ❺ "ladders prime the interior … paint black" okudu · 8,9–9,0 el arabası + iki işçi yok, kovalar çakıl üstünde · 10,0 kovalar platform kenarına · 11,0 çakıldaki pas yok · 10,0–11,0 işçi önden geçer, iş yok (❸) | ½ | ❶ ❸ ❹ ↔ ❺ | E07 |
| 3 | meşe iç zemin (arkadan öne) · deck · basamak yüzleri · sargılı berjer el arabasında | 12,0 zeminin 1/3'ü, 13,0 tamamı (❹) · tahta yığınlı araba sağdan sola 13,0'da ışınlandı, yığın hiç azalmadı, dolu itilip gitti (❸ ❹) · 14,0 deck + basamaklar "pop" (❶ ❸ ❹) · 16,0'da ikinci mobilya arabası yerinde yok (❸) | ❌ | ❶ ❸ ❹ (❺ "lay planks" okudu) | E08 |
| 4 | berjer A / B tek tek, doğrudan yerine · sehpa aralarına · ışık şeridi el → halka → yanar · cam arabası basamak sağına | 16–17 sargılı berjer yerinde kalkıp indi (❸) · 17,0 sehpa sağ kenarda kendiliğinden (❸ ❹) · 18,0 berjerler + sehpa + bitki + tavan LED hepsi "pop" (❶ ❷ ❸ ❹; ❺ "switch on" okudu) · 19,0 cam arabası gözetimsiz belirdi, 19–20 çerçevesi ve sapı yeniden çizildi (❶ ❸ ❹) | ❌ | ❶ ❷ ❸ ❹ | E09 |
| 5 | cam ① 20,0–21,25 · cam ② 21,25–22,25 · cam ③ 22,25–23,0 TEK TEK vantuzla · boş araba → merdiven evi · korkuluk + saksı arabası (tohum) | 20,0–21,0 arabadaki filmli paneller bir anda yok, işçiler tek şeffaf panel tutar (❸ ❹) · 21,0 üç bay aynı anda buzlu film (❶ ❸ ❹) · ⭐ 22,0–23,0 YABANCI SEGMENT: gök gün batımı turuncusu + sağ binada siyah dış merdiven/iskele + saksılar güvertede; 23,0'te hepsi geri, saksılar el arabasında, gök gündüz (❶ ❷ ❸ ❹ ❺) · 23,0–24,0 korkuluk + saksı arabası sağdan girer (plan ✅) | ❌ | ❶ ❸ ❹ (E10) · ❶ ❷ ❸ ❹ ❺ (E11) | E10 · E11 |
| 6 | korkuluk + saksı TEK TEK · gün batar · film köşesi | 24,0–25,0 korkuluklar yerinde "pop", arabadaki saksılarda çalılar yerinde yok (❶ ❸ ❹) · 26,0 saksılar dış köşelerde, el arabası ahşaptan gri metal düz arabaya yerinde döndü (❸ ❹) · 25,9–26,0 gök turuncudan maviye sıçradı (❶ ❸ ❺) · 26,0–27,0 işçisiz (❸ — 1 sn örneklemesi) | ❌ | ❶ ❸ ❹ (❺ gök) | E12 |
| 7 | orta film 0–1,0 (28–29) tek geniş tabaka yukarıdan aşağı · yan filmler 1,0–1,5 · çıkış 1,5–2,0 · tutuş 2,0–4,0 | ❶ film soyulurken kahverengi şeffaf PERDEYE döndü, camın içine asıldı, 30,0'da yok · ❸ ❹ sol cam filmi 29,0'da dokunulmadan yok, orta/sağ film işçisiz erir, boş el arabası + sağ işçi 29,0'da kayboldu · ❺ "peel … PASS" · tutuş 30,0–32,0 ✅ (❶ ❷ ❸ ❹) | ❌ (3/4) | ❶ ❸ ❹ ↔ ❺ | E13 · E14 |
| kart | G8 + başlık y 560–770 · erime ≤ 1 sn · çatı rüzgârı sürer | G8 ✅ (❶ ❹ ❺) · başlık yeri ⚠️ (E15) · ses: "sessiz" ❺ (E16) | ½ | ❶ ❹ ❺ | E15 · E16 |

```
ÖZET   MEKÂN ve KAMERA TUTTU (HOME kilidi · tanık raf · kart = G8). KOPAN: nesnelerin yerinde belirip yok olması — S0'dan S7'ye HER klipte.
       Kopanlar üç aile:
       ① YERİNDE SİLİNME / BELİRME — vinç (S0) · yan paneller (S0) · borular, çuvallar→kovalar, merdivenler (S1) · boya (S2) · plank + deck (S3) ·
          mobilya + tavan ışığı (S4) · cam + film (S5, S7) — DERS 48 · 49 · 61'in tekrarı; planın "⛔ … atılır" listesi dokuz yerde tetiklenmiş görünüyor;
       ② YABANCI SEGMENT — S5'in ortasında 1 sn'lik, planda olmayan merdiven + gün batımı + erken saksı (beş mercekte aynı saniye);
       ③ KAYIT — blok boş dördüncü film (DERS 100 · 105 · 106): puanlar 2,8 ile 9,75 arasında dağıldı → hiçbiri bağlayıcı değil.
       ⛔ Kare olmadan hüküm kesinleşmez: ❸ ❹ 1 sn örneklemesiyle yazıldı (yalıtım şüphesi) — bağımsız tanık ❶ ❷ ❺.
```

## MERCEKLER
| mercek | durum | puan | hüküm | ham | en ağır üç bulgu (m:ss.s) · ajan notu |
|---|---|:-:|---|---|---|
| ❶ GÖRÜNTÜ | EKSİK (blok boş · D2 ✗ · D4 ✗) | — (bağlayıcı değil: 6,3) | TIMELAPSE · MELTING | THE_SKY_VAULT_Q1_GORUNTU_HAM.md | 0:00–0:01 vinç + merdiven yerinde silindi (E01 ✓ 4 mercek) · 0:22–0:23 siyah merdiven (E11 ✓ 5 mercek) · 0:28–0:30 film → perde (E13) · ⚠️ kesme ızgarası uydurma |
| ❷ ZAMAN VE KESME | EKSİK + ŞİŞİK (blok boş · D2 ✗ · D4 ✗ · 11/12 10/10) | — (bağlayıcı değil: 9,75) | PASSING · TIME · RHYTHM | THE_SKY_VAULT_Q2_ZAMAN_KESME_HAM.md | RHYTHM = eşit 5,0 sn ızgara (gerçek 4,0; metronom plan ⑥ beyanlı) · MÜZİK YES (❶ ❺ yok diyor) · gölge/mevsim tablosu tahmin (summer → autumn uydurma; plan tek gün 05:45–19:55) |
| ❸ ŞANTİYE | EKSİK + ÇÖKÜK (D2 · D4 · D6 · 9/11 ≤ 3) | — (bağlayıcı değil: 2,8) | SAME WORLD · WORKING | THE_SKY_VAULT_Q3_SANTIYE_HAM.md | 31 × 1 sn klip uydurdu · "18/30 dikiş kusurlu", "6 boş klip" 1 sn örneklemesinin ürünü · ama 4,0 · 8,0 · 16,0 · 20,0 gerçek dikişlerinde sıçrama bildirdi (E03 · E06 · E10) |
| ❹ İNŞA | EKSİK (mod V · D2 · D4 · D6) | — (bağlayıcı değil: 4,0) | SAME · APPEARING · INTRUDERS | THE_SKY_VAULT_Q4_INSA_HAM.md | 0:01 sağ yüz kapandı / sol açıldı (E02) · 0:22 siyah merdiven = en zararlı davetsiz (E11) · boya/deck/LED/korkuluk "doğmuş tam" (E07–E09 · E12) |
| ❺ TESLİM | YANLIŞ GİRDİ (mod D lensi belgesiz · D4 ✗) | — (bağlayıcı değil: 8,6) | ENDS | THE_SKY_VAULT_Q5_TESLIM_HAM.md | final PASS (❶ ❸ ❹ ile çelişir — E13) · kart sessiz iddiası (E16) · RESISTANCE ekranda yok (plansız okuma) |
FİLM PUANI  — · N=0          ÖLDÜRÜCÜ  — (❶ TIMELAPSE · ❸ SAME WORLD · ❹ SAME; hiçbiri SEPARATE IMAGES / REBUILT / DIFFERENT değil)
⚠️ PUAN BAĞLAYICI DEĞİL: beş merceğin beşi de EKSİK ya da YANLIŞ GİRDİ. Hüküm satırları NONE değil [AGENTS kart R 6]:
❶ en kötü eriyen cisim (araba+yük S1 · film→perde S7) → S1 · S7 · ❸ GROWTH NOBODY MADE (film 29–30) → S7 · ❹ FIRST PIECE (sol panel 1,0) → S0 ·
❹ MOST DAMAGING INTRUDER (siyah merdiven 22,0) → S5 · ❺ "never reached": RESISTANCE — plansız okuma, yeniden üretim adayı DEĞİL.

## DOĞRULAMA
- Geri okuma: ❶ ✗ görülmüyor / NONE / 6+kart · ❷ ✗ görülmüyor / NONE / 6+kart · ❸ ✗ yer tutucu / NONE / 31+kart · ❹ ✓ "the sky vault.mp4" / NONE / 31+kart ✗ ·
  ❺ ✗ "video_file" / NONE (kapak NOT SUPPLIED) / 8+kart ✓
- D1: dosya dışı damga yok (en büyük 0:37.0) ✓ · D2: ❶ ✗ 6 · ❷ ✗ 6 · ❸ ✗ 31 · ❹ ✗ 31 · ❺ ✓ 8 + kart (⚠️ ızgara plandan; dosya ölçülemedi) ·
  D3: planlanan-süre itirazı yok ✓ · D4: ❶ ❷ ✗ (5 · 10 · 15 · 20 · 25 ↔ 4 · 8 · 12 · 16 · 20 · 24 · 28; sapma 1–8 sn) · ❸ ❹ ✗ (her tam saniye) ·
  ❺ ✗ (23 · 27 · 31,5 ↔ 24 · 28 · 32) · D5: kart VAR (plan 32,0–37,0), beşi de gördü ✓ · D6: ⏳ pano yok; plan ızgarasına göre ❶ ❷ ❸ ❹ tutmuyor, ❺ klip sayısı ✓ sınırlar ✗
- İki ya da daha çok D-kaldısı: ❶ ❷ ❸ ❹ → TEKRAR [QA_KOSU §4] · ❺ belgesiz mod D → YANLIŞ GİRDİ [QA_KAYIT §4]
- Sızıntı taraması (❶ ❷ ❸): temiz — plan sayısı (px, %, saat), "G0…G8", "spec", "landing", "sapan", "viewing room" yok; "tank"/"lounge"/"pavilion"
  mercek kendi okuması ("water", "tower" planın yasak korpusu — geçmiyor). Başlık "THE SKY VAULT" karttan okunur — sızıntı sayılmaz.
  ⚠️ ❸ ❹ aynı 31 × 1 sn bölütleme + aynı olay listesi (merdiven 0:22, saksı 0:22→0:23) → yalıtım şüphesi (aynı sohbet / oturum); kanıt yok.
- Şişik/çökük sayımı [DERS 105 ③ · DERS 106]: ❷ 11/12 kategori 10 → ŞİŞİK · ❸ 9/11 kategori ≤ 3 → ÇÖKÜK

## DOKÜMAN
(kör ❶ ❷ ❸ soruları plandan cevaplanır; ❹ ❺ mod V sorusu da)

### ❶ GÖRÜNTÜ
1. **Blok değerleri:** hız 2x · 8 klip · yayında 4,0 sn · kesmeler 4,0 · 8,0 · 12,0 · 16,0 · 20,0 · 24,0 · 28,0 · END CARD = YES (32,0–37,0; erime ≤ 1 sn) · MÜZİK = YOK ·
   9:16 · 37,0 sn · final tutuşu planda 2,0 sn (30,0–32,0).
2. **Adım kareler:** Hayır — 9 görsel (G0…G8) + 8 I2V zinciri; her klip iki onaylı kareye kilitli, klip içi sürekli. Klip içinde nesnelerin 1 sn adımlarla belirmesi
   ❶'in "step-frame" okuması = erime (E01–E13).
3. **Vinç (G0):** Plan: panel G0'da vincin kancasında; S0'da panel rafa iner (2x 0–1,0), vinç paletleri üstünde parapet boyunca sol kenardan ÇIKAR (1,0–1,5) —
   hareketle ayrılmalıydı, yerinde silinmemeli [plan S0 ⛔ "vinç havada erirse klip atılır"] → E01.
4. **Merdiven/iskele kulesi 0:22:** Planlı değil. Sağ kenardaki sabit "merdiven evi" (x 884–1080, kapı 900–927) nirengidir; üstündeki siyah dış merdiven plan dışı → E11.
5. **Film:** Plan: süt beyazı film camın DIŞINDA; S7'de tek geniş esnek tabaka hâlinde yukarıdan aşağı soyulur; iç perde YOK [plan S7 ⛔ "yeni nesne belirirse atılır"] → E13.

### ❷ ZAMAN VE KESME
1. **Blok:** yukarıdaki ❶-1.
2. **Güneş:** 41° K, 21 Haziran, güneş saati — G0 69,6°/+12,5° · G1 87,6°/+34,6° · G2 111,4°/+56,8° · G3 168,7°/+72,2° · G4 239,4°/+61,9° · G5 267,4°/+40,2° · G6 285,9°/+17,8° ·
   G7 304,5°/−2,6° · G8 306,2°/−4,1°. ⚠️ Rapor "öğleden sonra → akşam, 40° → 22°" okudu; plan sabah 05:45 → öğle 11:45 (+72°) → mavi saat 19:55 — sabah yarısı okunmadı.
3. **Mevsim:** Tek gün (21 Haziran); takvim yok. Raporun "summer → autumn → night" sırası uydurma.
4. **Süre:** S0–S6 2'şer saat (rejim B · 900×), S7 10 dk (rejim A · 75×). 05:45 → 19:45 + 10 dk; kesmeler zaman sıçraması değil — zaman klibin içinde akar.
5. **Müzik:** Hayır — plan müziksiz, diegetik yatak. ❷'nin "kesmeler müzik barına denk" iddiası dayanaksız (kesme ızgarası da uydurma).

### ❸ ŞANTİYE
1. **"Boş klipler" (S1 · S6 · S9 · S19 · S22 · S26):** Klip değil — 1 sn örneklemesi. Plan: boş zaman tek yerde, S5 + S6'da oda film arkasında (2x ≈ 8 sn bekleyiş — beyanlı) ve S7 tutuşu.
2. **Vinç:** G0 + S0'ın ilk 2 sn'si (2x 1 sn), sonra kadrajdan çıkar, HİÇBİR karede yok [DERS 8 · 46]; "6,0'a kadar kalması" planda yok.
3. **A çerçeveli raf:** Kalıcı — paslı paneller rafta KALIR (kafiye, tanık). Rafın yanındaki "küçük merdiven" planda tanımlı değil (G2'de "katlı merdiven platformda") → kare doğrulaması.
4. **0:22–0:23 "yanlış sıra klip":** Sıra hatası değil; S5'in (20,0–24,0) ortasında 1 sn'lik yabancı segment → E11.
5. **El arabası:** Plan TEK el arabası; ahşap → gri metal dönüşümü yerinde kimlik değişimi → E12.

### ❹ İNŞA (mod V)
1. **Kabuk:** G0'da sağ geniş yüz AÇIK (karanlık delik, içeride borular); sol geniş ve sağ dar yüz paslı panelli; panel rafın tam üstünde askıda. Rapor 0:01'de sağ yüzün kapanıp sol yüzün açıldığını yazdı → E02.
2. **Ara adımlar:** S2 tel fırça → kömür rulo (dikey şerit, soldan sağa) · S3 meşe + deck (arkadan öne) · S5 camlar tek tek vantuzla · S6 korkuluk cıvatalanır; her biri planda iş sırasıyla yazılı — ekran yerinde belirmeyi seçmiş (E07–E09 · E12).
3. **Vinç:** Plan paletli (crawler) vinç, rafın ötesinde; rapor "yer tipi teleskopik bom" okudu; sol-kenardan çıkış planlı, silinme değil → E01.
4. **0:22 klip:** Reddedilmiş üretim ya da sıra hatası değil; S5 içi segment → E11.
5. **Sol cam filmi:** Plan: orta film ilk, sonra "biri sol geniş yüzün, diğeri sağ dar yüzün" yan filmi soyar — ekranda soyulması beklenirdi; rapor 29,0'da yerinde kaybolduğunu yazdı → E13.

### ❺ TESLİM (rapor belgesiz — sorular yine cevaplanır)
1. **Vaat:** "Paslı depo → ışıklı seyir odası" (plan VAAT) · oda tanınması ≈ S4 sonu (2x 18,0–20,0); tam kanıt S7 (2x 28–30).
2. **Final beat:** Evet — film soyulur, oda görünür, tutuş 2,0 sn (30,0–32,0); hız 2x.
3. **Merak sorusu:** "Bu depoya ne yapıyorlar?" — G0'da panel havada, delikten borular; gün → mavi saat planlı yay (05:45 → 19:55), "aynı ışık çifti" değil.
4. **Kart sesi:** Planlı değil — plan: çatı rüzgârı sürer, kartın son saniyesinde söner (döngüde S0 vinç uğultusuna bağlanır) → E16 (ölçüm bekliyor).
5. **Kapak / AI beyanı:** Kapak THE_SKY_VAULT_KAPAK.md (G8 + "THE SKY / VAULT"); beyan YAYIN paketinde (ayrı) — ❺'a verilmedi.

## OLAY TABLOSU
| olay | zaman (yayın 2x) | ne oldu (rapordan) | mercekler | kanıt karesi | karar |
|---|---|---|---|---|---|
| E01 | 0,0–1,0 (S0) | ⭐ Vinç + katlı merdiven yerinde silindi; askıdaki panel rafa inmeden raf üç panelle belirdi; plan: panel iner, vinç hareketle çıkar | ❶ (cat 7 · C1 5) ❸ ❹ (C4 5) ❺ | ⏳ yok (video okunamadı) | ⛔ S0 yeniden adayı #1 — plan kill-line "vinç havada erirse" [DERS 8 · 46 · 49] · kare doğrulaması önce |
| E02 | 1,0–2,0 (S0) | Sol paslı panel yerinde silindi; ❹: sağ açık yüz paslı panelle kapandı, sol kapalı yüz açıldı (yüz yer değiştirdi) | ❶ ❸ ❹ | ⏳ | S0 ile birlikte — yan paneller TEK TEK elle [DERS 49] |
| E03 | 3,0–4,0 (S0|S1) | Sağ panel gerilip geniş bulanık levha oldu, rafa eklenmeden yok (4,0); ❸: işçi yeleği sarı → lacivert 3,9–4,0 | ❶ ❸ ❹ | ⏳ | S0 ile · dikiş 4,0 (G1) kontrol — iki onaylı kare kilidi kaçmış olabilir |
| E04 | 4,0 · 5,9–6,0 (S1) | Boru yığını kürekle toprak gibi küçüldü (4,0); tamamı bir anda yok (6,0) | ❶ ❷ ❸ ❹ | ⏳ | S1 yeniden adayı — "pipes one at a time by hand" [DERS 61 · 48] |
| E05 | 6,0–7,0 (S1) | Sabit el arabasında çuval yığını boya kovalarına döndü | ❶ ❷ ❸ ❹ | ⏳ | S1 ile birlikte (kova → platform ayrı cümle) |
| E06 | 7,0–8,0 (S1|S2) | Gümüş merdiven sağdan sola sıçradı (8,0 dikişi), küçük merdiven ikinci kez | ❶ ❸ ❹ | ⏳ | dikiş 8,0 · merdiven tavanı 1 [DERS 69 akrabası] |
| E07 | 8,9–11,0 (S2) | İç gri astar 9,0, dış kabuk mat siyah 10,0–11,0 "step-frame fade", boyacısız; ❺ boyacı okudu; kovalar sekme sekme çakıl → platform | ❶ ❸ ❹ ↔ ❺ | ⏳ | kare doğrulaması — plan: rulo + şerit şerit soldan sağa [DERS 49] |
| E08 | 13,0–14,0 (S3) | Dolu tahta arabası 13,0'da sağdan sola ışınlandı, yığın azalmadan döşeme + deck "pop" | ❶ ❸ ❹ | ⏳ | S3 yeniden adayı [DERS 48 — kaynağı azalmayan yük] |
| E09 | 17,0–19,0 (S4) | Sehpa kendiliğinden (17,0); berjerler + sehpa + bitki + tavan LED 18,0'de tam; cam arabası gözetimsiz belirir (19,0) | ❶ ❷ ❸ ❹ | ⏳ | S4 yeniden adayı — işçi kapıdan getirir, ışık yanışı kare senkron [DERS 48 · 61] |
| E10 | 20,0–21,0 (S5) | Arabadaki paneller bir anda yok; üç bay aynı anda buzlu film | ❶ ❸ ❹ | ⏳ | ⛔ S5 yeniden adayı #2 — plan kill-line "cam ① ② ③ tek tek / aynı anda iki cam" [DERS 88] |
| E11 | 22,0–23,0 (S5 ortası) | ⭐ YABANCI SEGMENT: gök gün batımı + sağ binada siyah dış merdiven + saksılar güvertede (erken); 23,0'te hepsi geri, saksılar arabada, gök gündüz | ❶ ❷ ❸ ❹ ❺ (5/5) | ⏳ | ⛔ S5 yeniden adayı #1 — en çok mercekli olay · hipotez: G7 dünyası klip ortasında 1 sn sızdı (DERS 96 · 98 akrabası) — ölçülmedi |
| E12 | 24,0–26,0 (S6) | Korkuluklar yerinde "pop"; arabadaki saksı çalıları yok; el arabası ahşap → gri metal (26,0); gök turuncu → mavi sıçradı | ❶ ❸ ❹ (❺ gök) | ⏳ | S6 yeniden adayı #4 — el arabası tek [DERS 69] |
| E13 | 28,0–30,0 (S7) | Film soyulurken kahverengi perdeye döndü ya da yerinde eridi; sol cam filmi dokunulmadan yok; araba + sağ işçi 29,0'da yok; ❺ "PASS" | ❶ ❸ ❹ ↔ ❺ | ⏳ | ⛔ S7 yeniden adayı #3 — plan kill-line "film solarak kaybolursa" [DERS 49 · 91] · final klip |
| E14 | 30,0–32,0 | Raf + küçük merdiven solda kalır | ❸ ❹ | ⏳ | raf: kabul (plan kafiyesi) · merdiven: kare doğrulaması |
| E15 | kart | Başlık ❶ ölçümüyle plan kutusunun ≈ 100–230 px üstünde (⚠️ ❶ ufku %56) | ❶ | ⏳ kapak_prova koşulmadı | kapak_prova + 1080×1920 yeniden dışa aktarım [DERS 99 · 5. film] |
| E16 | 32,0–37,0 | Kartta ses kesilmiş ("silent"); plan: çatı rüzgârı sürer | ❺ | ⏳ ses ölçümü yok | ölç; doğruysa S7 oda tonu 5 sn uzatılır [DERS 100 · 4. film] |
| E17 | 0,0 · 2,0 · 27,0 · 28,0 | İşçiler keskin ve pozlu (❶ cat 5 = 3) ↔ ❸ ❹ "3,0–11,0 motion-blur ghosting, uzuv kayması" | ❶ ↔ ❸ ❹ | ⏳ | kabul/ölçüm — rejim B izli, S7 tanınır figür (plan beyanlı) · çelişki çözülmedi |
| E18 | tüm film | ❷ "MUSIC = YES · bite denk kesme" — ❶ ❺ müzik yok der | ❷ ↔ ❶ ❺ | ⏳ kulak yok | kulakla dinle (Veo müzik — DERS 100 2. ölçüm) |
| E19 | kayıt | Günlük boş · qa_paket koşulmadı · beş mercek blok boş · D2 4/5 ✗ | ❶ ❷ ❸ ❹ (kendileri söyledi) | ham künyeler | ❶ ❷ ❸ ❹ ❺ yeniden koşulur, blok ajan tarafından dolu [DERS 105 · 106] |

## KARAR

⭐ **SAHİP KARARI BEKLİYOR** — öldürücü hüküm yok (TIMELAPSE · SAME WORLD · SAME), ama PUAN YOK ve hükümler bağlayıcı değil.

- **Önce ölçüm (klip üretimi YOK):** yayın dosyasını ajanın okuyabileceği yere koy (workspace içine kopya ya da Terminal'e Downloads izni) →
  `ffprobe` · `klip_eslestir.py` · 1 sn + 4 fps pano · `kapak_prova.py` · kart ses kuyruğu · `ihrac_kontrol.sh --hiz 2 --kart 5`. Bu pano E01–E19'un
  kanıt karesi sütununu doldurur ve D6'yı kapatır.
- **Sonra QA yeniden koşu:** `bash araclar/qa_paket.sh --hiz 2 <film_klasoru> <yayin.mp4>` (günlük boşsa ajan bloğu elle doldurur) ·
  ❶ ❷ ❸ geçici sohbette belgesiz, AYRI sohbetlerde (❸ ❹ aynı oturumda koşmayın) · ❹ ❺ plan + QA_SPEC (+ kapak) ile mod D.
- **Yeniden üretim adayları (kare doğrulaması geçerse, öncelik sırasıyla):**
  1. **S5 (E10 · E11)** — beş mercekli yabancı segment + üç camın aynı anda belirmesi; I2V yeniden, G5/G6 uçları kalır.
  2. **S0 (E01 · E02 · E03)** — vinç yerinde erir, paneller silinir; planın kill-line'ı üç kere tetikli. Açılış klibi — kanca etkisi ağır.
  3. **S7 (E13)** — final klip; film → perde / yerinde erime. ⛔ S7'den önce ❺'in PASS'i ile ❶ ❸ ❹'ün çelişkisi karelerle çözülür.
  4. **S1 · S3 · S4 (E04–E06 · E08 · E09)** — kaynağı azalmayan yük, kendiliğinden beliren mobilya/ışık; DERS 48 · 49 · 61 kilitleri tekrar okunur.
  5. **S2 · S6 (E07 · E12)** — renk ve korkuluk; yalnız kare doğrulaması bu çelişkiyi çözerse (❺ boyacı okudu).
- **Kabul edilen (şimdilik):** E14 raf (plan kafiyesi) · E17 işçi pozu (rejim B/A beyanlı) — küçük merdiven (E14) ayrı.
- **Gerekçe:** ❸ ❹ 1 sn örneklemesiyle yazdı ve aynı oturum şüphesi taşıyor; ama aynı olayların çoğunu bağımsız ❶ de zaman damgasıyla saydı (20 bulgu, S0'dan S7'ye)
  ve E11'i beş mercek gördü. Dört+ mercekte örtüşen olaylar: E01 · E04 · E05 · E09 · E11. Önce bu beşi ve E13 (❺ ile çelişen final) karelenir; geri kalan
  olaylar tek-iki mercekli — karelenmeden klip atılmaz.
- **Günlüksüz paket bayrağı** (qa_paket.sh `--gunluksuz`) sahip kararı beklemeye devam ediyor — dört filmdir blok boş koşuluyor; kilidin kâğıtta kalması
  ölçülmüş bir arıza [DERS 100 · 105 · 106].

## DERS
- DERS 100 — 3. ölçüm: günlük boş ✅ doğrulandı · qa_paket koşulmadı · kart sesi iddiası (❺) · ajan ölçümü bu kez izin yüzünden yapılamadı (ek satır)
- DERS 105 — 2. ölçüm: boş blok → ❸ ❹ 31 × 1 sn, ❶ ❷ 6 × 5 sn; yalnız ❺ 8 klip saydı (ek satır)
- DERS 106 — Blok boş koşulduğunda yanlış bölütleme puanı iki yönde bozar: ❷ tavana (9,75), ❸ tabana (2,8); eşit uydurma ızgara METRONOM'u "RHYTHM" yazdırdı
- ⚠️ DERS ADAYLARI (video ölçümü gelince): ① S5 ortasında 1 sn'lik yabancı segment (beş mercek aynı saniye) · ② S0 vinç yerinde silindi / planın kill-line'ı tuttu mu
  · ③ S7 film → perde (iç perde yeni nesne) — üçü de DERSLER'e yalnız kare kanıtıyla girer
