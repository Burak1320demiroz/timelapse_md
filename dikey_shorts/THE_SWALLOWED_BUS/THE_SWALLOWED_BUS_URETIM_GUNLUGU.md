# 🗒️ THE SWALLOWED BUS — ÜRETİM GÜNLÜĞÜ

```
DURUM   ⛔ BOŞ — araç kapısı KOŞULMADI · ön görselleştirme ÇİZİLMEDİ · (19.09.2026 plan yazıldı)
KURAL   her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil [DERS 28]
        bu dosya yoksa ya da §0 boşsa araclar/qa_paket.sh durur
```

> Şablon: `dikey_shorts/URETIM_GUNLUGU_SABLONU.md` · Plan: `THE_SWALLOWED_BUS_DIKEY_TIMELAPSE.md`
> Format: 7 sahne = 8 kare (G0…G7) + 7 I2V · her sahne tek 8,0 sn klip.
> Izgara: ⛔ DÜZ 7 × 8,0 = 56,0 sn — proje sahibinin kesin kuralı; ⑥ METRONOM beyanlı risk.
> ⭐ S0 REJİM A · S6 REJİM G (gerçek zaman 1×, depoda ikinci koşu) · ⭐ AŞAĞI BAKIŞ istasyonu (ikinci koşu).

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32]

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki her sahne 8,0
   ⛔ tavan < 8,0 ise bu araçta üretilmez; karar sahibine döner:   KARAR ____
② KAMERA        ilk/son kare kayması: ____ px    (KAMERA_ISTASYONU §7 eşiğini aşıyorsa ÜRETİLMEZ;
                eşik zincir_kontrol.sh çıktısının "3 nirengi" satırında)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
   ⭐ üç nirengi bu filmde: kemerli giriş (%60,4) · trafik lambası direği (%73,7) · çınar gövdesi (%24,5)
③ GÖLGE         ilk/son kare açı farkı: ____°    (rejim B test klibinde 0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5
⑤ PROMPT TAVANI ____ karakter · son nesne göründü mü: __/5  (plan promptları 5.745–5.979 krk)
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
⑧ İKİ KARE      araç ilk+son kare alıyor mu: evet/hayır  ⭐ FORMAT KAPISI
   SON KARE     klibin son karesi ↔ hedef görsel · zincir_kontrol: ____

⭐ ⑨ SAYIM TESTİ [DERS 55]
   Test promptuna plandaki sayım cümlesi birebir konur. Beş klipte:
   kaç çukur / kaç otobüs çıktı: __/__/__/__/__      hedef: hepsinde 1 / 1 (G0 promptu)
   G1 test karesinde BOŞ çukura hayalet otobüs ya da boru kondu mu: __
   ⛔ Herhangi bir klipte 2+ çukur ya da caddede ikinci çöküntü çıkarsa ARAÇ DEĞİŞİR, plan düşürülmez.
   KARAR         ____

⑩ ÇÖZÜNÜRLÜK    bu filmde UYGULANMAZ — kurgu hareketi yok, kırpma yok [plan §KURGU]

⑪ AŞAĞI BAKIŞ TESTİ (bu filme özel · KAMERA_ISTASYONU "AVLU / AŞAĞI BAKIŞ" ikinci koşu)
   G2 test karesinde çukur TABANI ve uzak duvar görünüyor mu (yakın perde örtmüyor): __
   gök göründü mü (üst kenar cepheyi kesmeli): __ · keystone sekiz karede aynı mı: __
   — taban görünmüyorsa h/D/tilt yeniden hesaplanır, plan §DEĞİŞMEZLER güncellenir
⑫ SAPAN TESTİ (bu filme özel · SPEC §4)
   S0 test klibinde otobüs SAPANLA mı kalktı, süzüldü mü: __ · boyunu korudu mu: __
   S2 test klibinde boru sapanla mı indi, bileziğe oturdu mu: __
   — sapansız yükseliyorsa DERS 8 / F08 tetiklenmiştir; araç sorgulanır
⑬ KATMAN TESTİ (bu filme özel · SPEC §5)
   S3 test klibinde dolgu ÜÇ basamakta mı yükseldi, tek hamlede mi doldu (F05): __
   G4 test karesinde çelik bant görünüyor mu (~42 px): __
⑭ BAĞLI SÖKÜM TESTİ (bu filme özel · SPEC §5 ③)
   S4 test klibinde perdeler teker teker mi çekildi, bir anda mı kayboldu: __
   her perdenin arkasına katman döküldü mü: __

⭐ ⑮ GERÇEK HIZ GEÇİŞ TESTİ — rejim G'nin bu filmdeki kapısı (SPEC §7)
   "moves at natural speed ... the bus rolls in from the right edge ... at walking pace" test klibinde:
   otobüs NET mi (iz yok): __ · gölge sabit mi: __ · 0/4/8 sn'de boy ve kapı sayısı: __/__/__
   ön teker doğu dikişi ____ sn · arka teker batı dikişi ____ sn (plan ≈ 1,0 / 4,5)
   yama otobüsün arkasında yeniden göründü mü: __
   — biri düşerse rejim G bu araçta yok; S6 için karar sahibine döner

KARAR           bu araçla üretilir / üretilmez — sebep
```

## 0b. ÖN GÖRSELLEŞTİRME — usta kareden ÖNCE [plan §DEĞİŞMEZLER · dış değerlendirme ④]

```
PLAN + YAN KESİT  istasyon (+18,0 m · güney parapet) · yakın kaldırım (d 3) · çukur (d 15–21 ·
                  x −6…+2 · −3,5 m) · boru (d 19,5) · uzak kaldırım (d 25) · cephe (d 29 · 17,5 m) ·
                  çınar (x −7 · d 27) · trafik lambası (x +6 · d 25) · ızgara (x −8 · d 25) ·
                  vinç (yakın şerit · x −8…−2 · d 5–10) · lowbed (uzak şerit · d 23,5) ·
                  G0 otobüs (x −5,5…+6,5 · d 17,5) · S6 giriş-çıkış yolu (d 17,5 · sağdan sola)
ÇİZİLDİ Mİ        evet/hayır · dosya: ____
⭐ KANIT KUTUSU    çukur %22–59 × %36–49 kutunun (x %11–78 · y %25–87) içinde mi: __
⭐ TABAN           uzak yarı tabanı (d > 17,9) ve boru bandı %38–42 okunuyor mu: __
⭐ OTOBÜS + VİNÇ + LOWBED + TABAN + S6 YOLU  aynı kadrajda okunuyor mu: __
GÖK               üst kenar cepheyi %100'de kesiyor mu (parapet 17,5 m > 16,4 m): ✓/✗
GÜNEŞ             bakış 0° — güneş gün boyu kameranın arkasında; cephe güneye bakıyor: ✓/✗
```

## 1. USTA KARE

```
KARE    G7 (S6'nın HEDEF karesi · sahne değil) [§2.7]
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne, neden]
SEED    [varsa]
KAPI    çukur/yama 1 · otobüs 1 (arkası sol kenarda, arka teker dikişin solunda) · yama BÜTÜN ·
        beyaz çizgi 1, düz · makine 0 · koni 0 (istif) · figür 1 sırtı dönük · gök YOK ·
        kemerli giriş %60,4 · trafik lambası %73,7 · çınar %24,5 → geçti/düştü
FİNAL HİYERARŞİ  ① yama bütün → ② otobüs solda, arka teker yolda → ③ figür + bariyer yerde [SPEC §1]
PİKSEL  yama kenarları y ____ / ____ · x ____ / ____ · giriş x ____ · direk x ____ · çınar x ____
        → plana ve SPEC §2'ye yazıldı mı: __
DOSYA   [kare dosya adı]
```

## 1b. ⛔ PİLOT ÜÇLÜ — FİNAL ÜRETİLEBİLİRLİK TESTİ [KILAVUZ_REHBERI §8 adım 2b · C1-b]

> Zincirin İLK halkası. Üçü onaylanmadan §2'nin kalanı üretilmez; (c) üretilemiyorsa
> kapsam daralır (sahne çıkar), prompt "düzeltilmez". Nirengi eşiği: KAMERA_ISTASYONU §7.
> ⭐ Bu filmde (c′) = S2 boru oturma; öncelik sırası (dış değerlendirme): S0 kaldırış · S2 boru · S6 tam geçiş.

| parça | dosya | zincir_kontrol (önceki ↔ yeni · ana referans ↔ yeni) | 3 nirengi (px) | beş soru ✓ | sahip onayı (tarih) |
|---|---|---|---|:---:|---|
| (a) referans karesi G7 + 3 nirengi işaretli (giriş · direk · çınar) | | — | | — | |
| (b) ilk halka G7 → G6 (otobüs önü sağa, bariyer ele, teker izi kalkar) | | geçti/düştü · geçti/düştü | | — | |
| (c) final I2V (G6 → G7) — otobüs geçer, yama arkasında bütün | | geçti/düştü | | ✓/✗ | |
| (c′) en zor montaj: S2 boru oturma I2V (G2 → G3) | | geçti/düştü | | ✓/✗ | |
| (c″) S0 kaldırış I2V (G0 → G1) — sapanla, boy korunarak | | geçti/düştü | | ✓/✗ | |

## 2. GERİYE ZİNCİR — KARE başına TEK satır · G6 → G5 → G4 → G3 → G2 → G1 → G0

> Her kare bir öncekinin üstünde EDİT [P2-a]. Kanıt nesnesi = çukur/yama kenarları + üç nirengi, elle ✓/✗ [DERS 25].

| G | araç + ayar | kaynak kare | master'dan ne KALDIRILDI / EKLENDİ | prompt birebir mi | zincir_kontrol (önceki · ana) | kenar + nirengi elle | çukur/otobüs sayımı | ⭐ çelik / boru / dolgu elle | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|:---:|---|
| 6 | | G7 | otobüs soldan kalkar → ÖNÜ sağ kenara · teker izi kalkar · figüre bariyer · ışık AYNI | | geçti/düştü · geçti/düştü | ✓/✗ | 1 / 1 | — / — / yama | |
| 5 | | G6 | asfalt + çizgi kalkar → gri TABAN (−0,15) · koni-bariyer yakın şeride · tandem silindir yamaya · tır (istif) + ekskavatör (son perde kıskaçta) uzak şeride · mat · figür kalkar · otobüs kalkar · ışık 15:30 | | | | 1 / 0 | istif / gömülü / taban | |
| 4 | | G5 | taban −0,7'ye iner · ÇELİK BANT dört kenara (1 m) · hendek silindiri dolguya · damper 2 (kasa kalkık) yakın kenara · tandem silindir kalkar · ışık 13:30 | | | | 1 / 0 | bant / gömülü / ¾ | |
| 3 | | G4 | dolgu kalkar → çakıl taban + SÜREKLİ BORU (iki bilezik) · çelik tam yükseklik · vinç (silindir zincirde) yakın şeride · damper 1 kasa inik · boş tır · ışık 11:30 | | | | 1 / 0 | tam / sürekli / yok | |
| 2 | | G3 | ikinci boru tıra, birinci SAPANA (tırın üstünde) · bilezikler BOŞ · pompa + hortum ızgaraya · ekskavatör vibro çekiçle · ışık 09:30 | | | | 1 / 0 | tam / sapanda / yok | |
| 1 | | G2 | çelik kalkar → YIRTIK kenar · taban moloz + su · uçlar bileziksiz · tır ve ekskavatör kalkar · lowbed'de OTOBÜS (sapan bağlı) · ışık 07:30 | | | | 1 / 1 (lowbed) | yok / uçlar / yok | |
| 0 | | G1 | otobüs lowbed'den ÇUKURA (burnu −3,5, arka teker yolda, 30°) · lowbed boş · sapan otobüsün altında gergin · pompa kalkar · ışık 07:20 | | | | 1 / 1 (çukurda) | yok / uçlar (otobüs örter) / yok | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTI boş kalır — kare atılır, yeniden türetilir.
⭐ Her kare hem ÖNCEKİ onaylıyla hem ANA REFERANSLA (G7) karşılaştırılır: zincir_kontrol.sh <önceki> <yeni> G7 [C1-f].
⭐ G2 → G1 filmin en riskli editidir: çukur BOŞ ve YIRTIK kalmalı; model çeliği bırakıyorsa
   "ragged asphalt edges" öne alınarak tekrar denenir.
⭐ G1 → G0 "otobüsü çukura koyma" editidir; otobüs boyu 12 m (~600 px) korunur, burnu içeride.
⛔ Her karede TEK ÇUKUR sayılır [SPEC §6].
```

## 3. VİDEO — I2V, klip başına TEK satır

> ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn. Kırpma BAŞTAN [§2.7 ③].
> ⭐ baş/orta/son [C1-a]: başta malzeme kartın ① yerinde mi · ortada taşıyıcıyla birlikte mi
> (süzülmüyor, boyu değişmiyor) · sonda ④ farkı görünüyor mu. Üç ✓ olmayan klip yeniden üretilir.

| S | araç + ayar | rejim | ilk kare | son kare | son kare ↔ hedef | prompt birebir mi | ffprobe süre | kırpma | teslim | yüzey kanıtı | beş soru ✓/✗ | baş/orta/son | dosya |
|:-:|---|:-:|---|---|:---:|---|---:|---|---:|:---:|:---:|:---:|---|
| 0 | | **A** | G0 | G1 — ⛔ otobüs İLK SANİYEDE kımıldadı mı ✓/✗ · SAPANLA kalktı mı (süzülmedi) ✓/✗ · lowbed'e oturdu mu ✓/✗ | geçti/düştü | | | | 8,0 | | ✓/✗ | ✓✗✗ | |
| 1 | | B | G1 | G2 — ⭐ lowbed SOLDAN ÇIKTI mı ✓/✗ · perdeler tırdan zemine teker teker mi ✓/✗ · hortum çalıştı mı ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 2 | | B | G2 | G3 — ⭐ boru sapanla İNDİ mi ✓/✗ · bileziğe oturdu mu ✓/✗ · hortum SONRA gitti mi ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 3 | | B | G3 | G4 — ⭐ ÜÇ katman mı ✓/✗ · çelik bant göründü mü ✓/✗ · vinç sol alttan ÇIKTI mı ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 4 | | B | G4 | G5 — ⭐ perdeler teker teker mi ✓/✗ · arkasına katman ✓/✗ · taban düz ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 5 | | B | G5 | G6 — ⭐ finişer sağdan sola ✓/✗ · çizgi çizildi mi ✓/✗ · koni-makine ÇIKTI mı ✓/✗ · otobüs önü sağda ✓/✗ | | | | | 8,0 | | ✓/✗ | | |
| 6 | | **G** | G6 | G7 (usta kare) — ⭐ arka teker dikişi geçti mi ✓/✗ · yama arkasında bütün ✓/✗ · net, iz yok ✓/✗ · çıkarken bitti mi ✓/✗ | | | | | 8,0 | | ✓/✗ | | |

## 4. ⭐ REJİM G ÖLÇÜMÜ — S6, depoda ikinci koşu

```
GÖLGE            G6/G7 balkon gölgesi açı farkı: ____° (hedef 0°)
İZ               motion streak ya da hayalet nesne: var/yok
FİGÜR            sırtı dönük kaldı mı: ✓/✗ · yüz okundu mu: ✓/✗
ÖN TEKER         doğu dikişini kaç saniyede geçti: ____ (plan ≈ 1,0)
ARKA TEKER       batı dikişini kaç saniyede geçti: ____ (plan ≈ 4,5)
BOY              otobüs 0/4/8 sn: ____ / ____ / ____ px (kesilen kısım hariç, KISALMAMALI)
YAMA             otobüsün arkasında yeniden göründü mü: ✓/✗ · dikişler sağlam mı: ✓/✗
48,0 DİKİŞİ      iz → net geçişi izlenebilir mi: ✓/✗ · rahatsız edici mi: ✓/✗
8,0 DİKİŞİ       rejim A'nın okunur figürleri → rejim B izleri: rahatsız edici mi: ✓/✗
⭐ ONE MORE TURN'den sonra ikinci gerçek zaman ölçümü. Sonuç DERSLER.md'ye (kart D) yazılır.
```

## 5. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM §6]

```
① BİÇİM         ffprobe → ____   (1080,1920,30/1,h264)
② SÜRE          ffprobe format=duration → ____ sn   (56,0 · kart YOK · logo YOK)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 <plan> → __
                beklenen kesmeler 8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0
                ("PLANIN KENDİSİ DÜZ" uyarısı BEKLENİR — sahip kuralı)
④ SES           ebur128 → I: ____ LUFS · Peak: ____ dBFS · BPM 120
⑤ AÇILIŞ        0,0–0,8 müziksiz pencere (kablo + kımıltı): __
                46,0–48,0 müziksiz pencere (dikiş): __ · 50,0'da müzik girdi mi: __
⑥ FLICKER       signalstats YDIF → kesme dışında sıçrama: evet/hayır
⑦ FİNAL + KAPAK ffmpeg -ss 54.0 → SPEC §1 üçlüsü görünüyor mu: __
                54,0 ↔ 55,0 arka teker x farkı: ____ px (≈ 170)
                KAPAK KANITI zincir_kontrol.sh g7_kaynak.jpg kapak.png → __
```

## 6. PLANDAN SAPMALAR

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
19.09.2026 — plan, ajan önerisinin dış değerlendirmeyle düzeltilmiş hâlidir; yedi düzeltme
             plana §KONSEPT KAPISI altına yazıldı. Sapma değil, ilk sürümün kendisi budur.
```
