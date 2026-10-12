# 🔭 THE_FIRST_LIGHT — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **20 × 8,0 sn = 160,0 sn** | Kapak kartı: **⛔ YOK** | Toplam: **160,0 sn**
Prompt yapısı: ⭐ **20 sahne → 21 ana görsel (G0…G20; G17 kubbe içi) + kubbe son karesi G17′ + 20 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G10**
Yapı: **dağ zirvesinde onarılan gözlemevi — Ø 24 m alçak granit davul (4 m), Ø 24 m bakır kubbe (tek gözlem yarığı, tek kapak), çatallı büyük teleskop, giriş basamakları, uçurum terası** (kart yok: `YAPI_TIPI_KARTLARI` §10 şablonuyla 00_ANALIZ/02 §2a'da yazıldı; en yakın emsal THE HIDDEN FALLS vinçli söküm + THE BURIED KHAN taş onarımı) · Saha: **dağ zirvesi, bulut denizinin üstü, 30° K** (`SAHA_VE_IKLIM_KARTLARI` — dağ/yüksek saha satırı ⚠️ okunmadı; 02 §2b'de bu film için yazıldı)
Zaman yayı: **gerçekte ≈1 yıl (kış → ertesi sonbahar) → 160 saniye** · film mertebe anlatır: *"bir kış söküm, bir bahar bakım, bir yaz kubbe, bir sonbahar ilk ışık"* [P1-c] · ÜSLUP BEYANI: takvim tek bir günün ışığına sıkıştırıldı (THE HIDDEN FALLS · THE BURIED KHAN emsali)
Işık günü: **07:35 → 18:05 (koyu mavi saat) · Σ rejim penceresi 10 sa 30 dk ≤ 14** — kesmede ışık atlamaz [§2.7 ①]
Kamera mimarisi: **MAIN STATION** (19 klip + usta kare) + **KUBBE İSTASYONU** (1 klip · S17 · S16'nın son 8 sn'si ∥ — İKİNCİ İSTASYON BEYANI aşağıda)
Izgara: ⛔ **DÜZ — 20 × 8,0** · ⚠️ BANDIN DIŞI (format 12 × 10,0 · 2:00) — sahip senaryosunun biçimi, toplam 2:40 (hikâye SAPMA ②) · §DÜZ IZGARA BEYANI
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 10.10.2026 (TUR 3 · "hazırla" · 20 satır · SAPMA ①–⑰)
Havuz kaydı: `apexait/YAYIN_PLANI.md` — ⬜ satır açılmadı (sahip kararı) · siluet ailesi: **kubbeli tek yapı + gök finali** (THE BURIED KHAN taş onarımıyla akraba; THE HIDDEN FALLS'tan farklı — su ve cam YOK)

_"İlk karede bulutların üstünde, vinçte asılı yeşil bir bakır kubbe ve altında açığa çıkan eski teleskop; son karede aynı yerde onarılmış gözlemevi, kameraya dönmüş açık yarığında kırmızı ışık ve göğe bakan teleskop."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     20 sahne × 8,0 sn                       = 160,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     ⛔ YOK — tam 160,0 sn (sahip senaryosu: "afişe veya siyaha kesilmeden 02:40'ta biter"); film adı yalnız
               küçük resme eklenir · ihrac_kontrol.sh --kart YOK
──────────────────────────────────────────────────────────────
TOPLAM                                                     160,0 sn
HIZ             1x (yatay hat 2x'e çevrilmez — 2x yalnız dikey paylaşım kuralıdır [DERS 58])
MÜZİK           ✅ VAR — düşük seviyeli, sözsüz, 120 BPM (8,0 sn = 4 ölçü) · diegetik yatak ÖNDE (vinç · metal · motor · dağ
               rüzgârı) · sahip senaryosu TUR 3 (hikâye SAPMA ⑮) · THE_FIRST_LIGHT_MUZIK.md
EKRAN BİNDİRMESİ ⭐ S17 (136,0–144,0) masadaki büyük ekrana gözlem görüntüsü KURGUDA yerleşir (139,0 sn'den sonra) · üretimde
               ekran KARANLIK ve BOŞ · kaynak görüntü ⬜ seçilmedi (kurmaca, halkaları açık bir gezegen görüntüsü — tek
               tutarlı referans, telifsiz ya da üretilmiş; kaynak ve lisans günlük §5'e) · ⛔ dış göğe gezegen girmez
               (hikâye SAPMA ⑦) · ekranda okunur arayüz yazısı YOK
YASAK KELİME    ruins · ruin · ruined · abandoned · saturn · planet · moon · galaxy · nebula · milky · spaceship · ufo · laser · searchlight · spotlight · mosque · church · chapel · cathedral · temple · tomb · mausoleum · shrine · planetarium · castle · fortress · hotel · rundetaarn · copenhagen
               ⭐ [DERS 59 · 55 · 42] hiçbir promptta, negatifte bile — "ruins · abandoned" harabe ALANI çağırır;
                  "saturn · planet · moon · galaxy · nebula · milky" dış göğe dev cisim koyar (gözlem görüntüsü
                  KURGUDA bindirilir, prompta adı girmez); "spaceship · ufo · laser · searchlight · spotlight" göğe ışık
                  sütunu ve bilimkurgu çağırır; kubbeli yuvarlak taş yapı "mosque · church · chapel · cathedral ·
                  temple · tomb · mausoleum · shrine" diye okunabilir; "planetarium" iç kubbe projeksiyonu; "castle ·
                  fortress" zirvedeki taş yapı korpusu; "hotel" zirve oteli; "rundetaarn · copenhagen" GERÇEK YER
KELİME KİLİDİ   "crane" yalnız G0–G15 + S0–S15 I2V [P7-e] · "glow"/"lit" (yol lambaları) yalnız S15 I2V ve G16'dan sonra ·
               "red light" yalnız S16 I2V ve G17'den sonra · "stars" yalnız S18 I2V ve G19'dan sonra · yarık için "open"
               yalnız S16 I2V'den sonra (öncesinde "closed by a … shutter") · STRUCTURE'da ışık, yıldız, kırmızı yok
               (yalnız yapı) [DERS 36]
BÖLÜM DOSYASI   BOLUM_1 = S0–S9 (0–80,0)  ·  BOLUM_2 = S10–S19 + KUBBE G17/G17′ + USTA KARE (80,0–160,0) · ceil(20/2)=10
QA BİRİMİ       FİLM (tek master × 5 mercek · ❶ ❷ ❸ kör · ❹ ❺ belgeli) — QA/HAM/THE_FIRST_LIGHT/
```

⛔ Kart olmadığı için platform son ekranı **son 5 saniyeye konmaz** ya da yalnız gök bandına (üstten 0–240 px) konur — açık yarık, teleskop ve korkuluktaki iki kişinin üstüne yerleştirilmez.
⚠️ Son sahnenin (S19) ikinci yarısı TUTUŞTUR (final kanıtı 156,0–160,0, `QA_SPEC` §1): kubbe durur, yarık açık, iki kişi korkulukta, kırmızı ışık sabit; yalnız bulut denizi akar.
⭐ Platform küçük resmi (kapak) G20'den gelir (sahip kararı 19.09.2026 — öncesi/sonrası bölme yok).

### 🔭 İKİNCİ İSTASYON BEYANI [ISTASYON_VE_IC_MEKAN §0 · DERS 52]

```
KLİP          tek: S17 (136,0–144,0) · KUBBE İSTASYONU · gerçek hız (G) · süre payı 8,0 / 160,0 = %5,0 (ana %95,0 ≥ %85 ✓)
① SABİT       clamp mount, tilt 0, roll 0 — kendi içinde kıpırdamaz
② ORTAK ÇAPA  TAŞ ÖRGÜSÜ cümlesi iki SITE bloğunda BİREBİR ("The granite of the drum is laid in long low courses of squared
              blocks with thin dark joints.") · dışarıda davulun ön yüzü, içeride iç duvar (bakış 160°)
              ⚠️ çam yarıktan GÖRÜNMEZ (yarık 159°, çam 125° — hikâye SAPMA ⑧); iç kadrajın ölçülebilir çapası YARIK
              (≈180 px, "keeps that width")
③ DIŞ BÜYÜME  taşımaz: S16'nın SON sekiz saniyesi ∥ · S16 I2V'si ana G18'e biter · S17 G17 → G17′ · S18 yine G18'den · dış
              kare iki yakada AYNI
④ BEYANLI     bu satır + QA_SPEC künyesi + günlük §3 İSTASYON sütunu
⚠️ KONUM      kural "gelişme bölümü %20–%80" der; S17 %85–%90'da, finale yakın — sahip onaylı düzen (TUR 3), hikâye SAPMA ⑥.
              Gerekçe: iç klip dışarıdan okunmayan TEK işi gösterir (teleskobun yarığa hizalanması + ekrandaki ilk görüntü)
```

### ⭐ İZLEYİCİ KAPISI [C2-a…d · KILAVUZ_REHBERI §6]

```
İŞLEV ANI         S8 tüp ilk kez hareket eder (test) → S16 kapak AÇILIR, kırmızı ışık → S17 içeride teleskop hizalanır, ekranda
                  ilk görüntü → S18 kubbe halkasında DÖNER, açık yarık kameraya gelir. S19 sakin tutuş.
AÇILIŞ NESNESİ    G0: vinçte asılı yeşil bakır kubbe (x 716–1204, tepe üstten 451) ve altında açık davulda tozlu teleskop ·
                  ona ne oluyor: söküm ilk karede SÜRÜYOR (kubbe sola kayıyor). 120 px'te okunan: beyaz bulut denizi
                  önünde koyu yeşil yarım küre + sarı vinç.
DİRENÇ EKRANDA    ① ağırlık — S0 kubbe · S1 tüp · S7 tüp geri · S10–S11 kubbe (16 sn, iki klip) — hepsi vinçte, dört sapan ·
                  ② yıpranma — S0–S2 sarmaşıklı, kirli taş + yeşil bakır + paslı ray · S2 şerit şerit temizlik · S4 paslı
                  ray yığını · S5 aşınmış zemin · S3 sökülen yeşil paneller · ③ hassas makine — S6 panel panel tüp bakımı,
                  S7 çatala inen tüp, S8 tek eğim hareketi
DÖNGÜ KAFİYESİ    G20 ↔ G0 aynı kadraj, aynı çam (x 1652–1805), aynı iki uzak tepe: G0'da kubbe davulun ÜSTÜNDE havada ve
                  yeşil, G20'de AYNI kubbe davulun üstünde, kahverengi bakır, yarığı kameraya açık; G0'da teleskop dik ve
                  tozlu, G20'de yarığın içinde göğe dönük. Işık FARKLI, bilinçli: sabah ↔ koyu mavi saat.
MERAK SORUSU      Bu terk edilmiş gözlemevi yeniden çalışacak mı?
AÇILIŞ DÜZENİ     ① NESNE havadaki yeşil kubbe · ② DOKUNUŞ "From the first frame the dome is already moving" · ③ İPUCU
                  açık davulda dik duran tozlu teleskop — ne olduğu hemen okunur, ama çalışıp çalışmayacağı okunmaz ·
                  ④ ÖLÇEK paletli vinç + iskele kuleleri + ekip (iz) · AÇILIŞ GERİ ÇEKİLMESİ ⛔ YOK (sabit geniş)
BEŞ AN (sahip)    00:00 kubbe havada · 00:24 bakır dönüşümü (S3 sonu) · 00:56 tüp geri (S7) + 01:04 test (S8) · 01:20–01:36
                  kubbe kalkar ve oturur (S10–S11) · 02:08–02:40 kullanım (S16–S19) — sahibin kurgu tercihi, ölçülmüş
                  bir formül değil
```

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Bulutların üstündeki eski bir gözlemeviyi söküp onarmak ve yeniden göğe baktırmak.
DİRENÇ   ① ağırlık ve ölçek (24 m kubbe ve 9 m teleskop tüpü tek parça kaldırılır)  ② yıpranma (kir, sarmaşık, yeşil bakır,
         paslı ray, aşınmış zemin, çatlak yol)  ③ hassas makine (tüp bakımı · geri dönüş · ilk hareket)
         EKRANDA NASIL [P1-b]:  S0–S1 · havadaki kubbe ve tüp  ·  S2 · şerit şerit temizlenen taş  ·  S3 · sökülen yeşil
                                paneller  ·  S4 · paslı ray yığını  ·  S8 · dikilen tüp  ·  S10–S11 · inen kubbe
BEDEL    ⭐ eski yüz — yeşil bakır ve kirli, sarmaşıklı taş: G0'da kubbe yeşil (x 716–1204), davul kirli (920–1400); S2'de taş
         temizlenir, S3'te yeşil kaplama sökülür, S9'da eski yeşil kapak gider (istif S14'te kamyonla). G20'de aynı kubbe
         kahverengi bakır. Okuma bilinçli: "eski bina yenilendi" değil, "gözlemevi yeniden göğe bakıyor".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            yeşil kubbe yüzü + kirli taş + paslı ray + eski kapak                       ✅
  □ kadrajda görünüyor mu?    kubbe 382–877 (sehpada) / 920–1400 (davulda) · davul ön yüzü 807–890       ✅
  □ cevap "zaman geçiyor" mu? hayır — "teleskop hareket etti, kubbe açıldı ve döndü"                       ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: kubbe nerede (havada · sehpada · davulun üstünde asılı · davulda) · ne renk (yeşil ·
                           pembe bakır + yeşil kapak · pembe · kahve) · tüp nerede (çatalda dik · beşikte kirli/temiz · çatalda
                           yatay · dik park) · ray paslı mı parlak mı · iç zemin koyu mu açık mı · yol eski mi yeni mi ·
                           korkuluk var mı · yarık kapalı mı açık mı, nereye bakıyor
② KİNETİK BAĞIMSIZLIK   ✅ her klipte vinç, ekip, kamyon, kubbe, kapak, tüp ya da servis aracı hareket eder
③ BAŞLIK ŞEMASI         ✅ kapak "FIRST LIGHT" (2 kelime) · yayın başlığı YAYIN_PAKETI (45 karakter — ⚠️ 40 sınırının üstünde,
                           sahip seçimi)
④ OMURGA CÜMLESİ [P1-k] ✅ kubbe kalkar → tüp çıkar → taş temizlenir → bakır kaplanır → ray yenilenir → zemin döşenir → tüp
                           bakımı → tüp geri → test → kapak değişir → kubbe kalkar → oturur → yol → korkuluk → şantiye gider →
                           vinç gider → yarık açılır → teleskop hizalanır → kubbe döner → göğe bakar
```

⚠️ **Aile benzerliği [P16-a]:** THE BURIED KHAN ile taş onarım + akşam ışığı finali akrabalığı; AYIRICI FARK: orada kum
kazılır ve kapı açılır, burada vinçle söküm-montaj ve final bir MAKİNENİN çalışmasıdır (yarık + dönüş + iç ekran).
THE HIDDEN FALLS ile vinç ağırlıklı söküm ortak; su ve cam yok. Üçü ardışık yayınlanmamalı (YAYIN_PLANI §3 — sahip kararı).

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera (ana istasyon %95,0) · tek iç klip (S17)
                          ② kanıt nesnesi: dağ ÇAMI (x 1652–1805 · üstten 551–870 · 153 px · 21 ana karede birebir)
                          ③ çapa: iki uzak tepe (ikiz doruk solda · uzun düz sırt sağda) · ④ ufuk %77,4 (244)
                          ⑤ davul tek parça: x 920–1400 · ön dip 890 · ön duvar tepesi 807 — G0 → G20 ±2 px; yalnız KAZANIR
                             (temiz taş · yeni ray · yeni zemin · yol · korkuluk)
                          ⑥ kubbe defteri: havada (G0) → sehpada 382–877 (G1–G10) → asılı 920–1400 (G11) → davulda (G12+) ·
                             renk yeşil (G0–G3) → pembe bakır + yeşil kapak (G4–G9) → pembe (G10–G11) → kahveye döner
                             (G12–G13) → kahve (G14+) · yarık kapalı SAĞ ÖNDE (G0–G16) → açık sağ önde (G18) → açık ÖNDE
                             (G19–G20)
                          ⑦ teleskop defteri: çatalda dik + tozlu (G0–G1) → tüp beşikte (G2–G7, G7 yenilenmiş) → çatalda
                             yatay (G8) → dik park (G9–G11) → kubbenin altında (G12–G16) → yarıkta (G18+)
                          ⑧ insan: A/B'de iz ("soft motion streaks") · S17'de sırtı dönük iki kişi · S16–G20 iki kişi
                             (≈30–35 px, yüz okunmaz)
                          ⑨ vinç kancası: ya YÜKLÜ ya bom ucu kadraj dışında (G2 · G15) — boş kanca hiç yok
P1.5 · fırsat buldukça   gök (kış berrak → bahar küçük bulut → yaz uzak kümülüs → sonbahar berrak) · bakırın matlaşması
                          (pembe → kahve) · gölge süpürmesi (B: S2 · S3 · S5 · S14) · bulut denizinin dokusu
SPEC · yalnız belge      azimut/yükseklik dereceleri (kapı şartı) · px tabloları
```

**Malzeme kimliği (her promptta):** *açık gri granit (uzun alçak sıralar, ince koyu derz) · bakır (yeşil → pembe → kahve) · koyu gri çatal · soluk beyaz tüp · sarı paletli vinç · gri çakıl · beyaz bulut denizi* — korpus: "documentary site photograph on colour negative film" [DERS 34 · 42].
**İnsan kararı:** ekip var — A/B'de iz; S16–S18 iki kişi (küçük sandık taşır, iz); S17 iç klipte masada iki kişi sırtı dönük; S19–G20 korkulukta iki kişi (≈30 px, yüz okunmaz).
**Vinç kararı [DERS 8 · 22 · 46 · 57]:** büyük sarı paletli vinç, uzun gri kafes bom, davulun arkasında (x ≈914 · D 84) · G0–G15. Kanca: G0 kubbe · G1 tüp (sapanlı) · G3 bakır paleti · G4 ray parçası · G5 zemin paneli paleti · G6 tüp paneli paleti · G7 tüp çerçevede (sapanlı) · G8 boş taşıma çerçevesi · G9 yeni kapak · G10 kubbe (sapanlı) · G11 kubbe asılı · G12 taş plaka paleti · G13 korkuluk demeti · G14 iskele tahtası demeti — YÜKLÜ ("carries a visible load" / "with a … on the hook"); G2 ve G15 bom ucu kadrajın üstünde ("its tip above the top edge of the frame"). S15'te bomunu servis yolu boyunca yatırır ve çıkar; G16'dan sonra "crane" kelimesi yok [P7-e].
**Uzun rijit yük [DERS 57]:** ⚠️ VAR — kubbe (Ø 24 m) ve teleskop tüpü (9 m). Gerekçe: senaryonun kancası budur ("dev kubbe havada") ve kubbenin dönüşü 16 sn'lik iki klip. Önlem: her biri dört sapanla, yavaş, tek parça; ikinci kopya yazılmaz ("exactly one dome"); PİLOT ② + S10–S11 pilot sonrası ilk klipler.
**Korpus kararı [DERS 55]:** zirve + yuvarlak taş + kubbe korpusu çoğuldur (ikinci kubbe, zirve oteli, şapel) → NEGATIVE'de her karede: "The summit holds exactly one building site, this one, and exactly one dome." — kubbe sehpadayken davul AÇIK, ikinci kubbe çizilmez.
**Yapı adı kararı [DERS 42]:** "observatory" yazılır (tek yapı tipi); "abandoned" (harabe) → "old · grimed · green with verdigris · half covered in dark ivy"; kubbe "copper dome" — dini yapı kelimeleri YASAK; gözlem görüntüsünün adı hiçbir promptta yok.

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
KARAR CÜMLESİ [KAMERA_DILI §0]: İzleyici kubbenin, teleskobun, taşın ve iç zeminin değişimini görecek. Çam, iki uzak tepe ve
                 bulut denizinin düzeyi aynı kalacak. Kamera ÜÇ ÇEYREK ÇAPRAZ / yüksek aileden (h 28 · tilt 13° aşağı)
                 bakacak — kubbesiz davulun içi ve zemini ancak böyle görünür. Hareket YOK.

ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0,
                 yani en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp [A7-b]; kutu tam 8,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 20 sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.

┌─ KAMERA İSTASYONU (ANA) ─────────────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 (G16, G18–G20 ISO 800) · YATAY     │
│ yükseklik     h = +28,0 m (zirve zemininden) — güneydeki yüksek kaya tepeciği  │
│ mesafe        D_eksen = 64,0 m (davul ekseni — BÜTÜN yüzdeler buradan) ·       │
│               D_kenar = 52,0 m (davulun ön yüzü) · D_çam = 50 · D_sehpa = 62 · │
│               D_beşik = 50 · D_istif = 50 · D_vinç = 84 · D_teras 56–72 [DERS 38]│
│ bakış açısı   bearing 0° (kuzey) · tilt 13° AŞAĞI · roll 0°                    │
│ sabitleme     "fixed tripod bolted to a high rock knoll to the south"         │
│ ⛔ HESAP — tilt formülü: KAMERA_DILI §3 (yatay 16:9 → kare yüksekliği 20,25 mm):│
│    yüzde(y,d) = 50 + 24·tan(tilt − atan((h − y)/d))/0,2025 (ALT kenardan)     │
│    px(x,d) = 960 + 1280,6·x/d (soldan · tiltte ±1–2 puan sapar — usta karede  │
│    ölçülür) · ufuk% = 50 + 24·tan 13°/0,2025 = %77,4 (üstten 244)              │
│    `bolum_uretici.py --kadraj` çıktısı:                                       │
│    davul dibi (ön)          y=0    · d 52 → %17,6 (890) ✓ alt onda birin üstü │
│    davul duvar tepesi (ön)  y=+4   · d 52 → %25,3 (807)                       │
│    iç zemin (kaide)         y=0    · d 64 → %27,8 (780) > ön duvar ✓ GÖRÜNÜR  │
│    iç zemin (arka)          y=0    · d 76 → %35,0 (702) → zemin bandı ≈105 px │
│    davul duvar tepesi (arka)y=+4   · d 76 → %40,6 (641)                       │
│    çatal kolu tepesi        y=+6,5 · d 64 → %38,4 (665)                        │
│    tüp yatay (G8)           y=+5,5 · d 64 → %36,8 (683) · x 1070–1250          │
│    tüp tepesi (dik park)    y=+12  · d 64 → %47,9 (563) · x 1136–1184 (48 px)  │
│    kubbe tepesi (davulda)   y=+16  · d 64 → %54,9 (487)                        │
│    kubbe asılı (G11)        taban +7 → %39,3 (656) · tepe +19 → %60,4 (428)    │
│    kubbe tepesi (havada G0) y=+18  · d 63 → %58,2 (451) < ufuk ✓               │
│    kubbe tepesi (sehpada)   y=+13,5· d 62 → %49,7 (544)                        │
│    kapı tepesi              y=+3   · d 52 → %23,3 (828) · x 1175–1237          │
│    yol                      y=0    · d 49 → %14,3 (925) ✓ alt onda birin üstü │
│    iskele kulesi tepesi     y=+7   · d 58 → %35,6 (695) · sol 872–938 · sağ    │
│                             1424–1490                                         │
│    davul x −2…+22 → 920–1400 (480 px)                                         │
│    sehpa (kubbe) x −28…−4 · d 62 → 382–877 · beşik x −32…−23 · d 50 → 140–371 │
│    istif alanı x −14…−8 · d 50 → 601–755 (üstten 870–913) · teras 1486–1829   │
│    vinç x −3 · d 84 → ≈914 (davulun arkasında)                                 │
│    ⭐ kanıt nesnesi ÇAM x +27…+33 · d 50 → 1652–1805 (153 px) · dip +2 → 870 · │
│       taç +16 → 551                                                           │
│    yarık (sağ önde, yön 159°) taban x ≈1307 → 45°'de 1258 · bant 1275–1340    │
│    yarık (önde, yön 189°, G19+) x ≈1160 · bant 1125–1195                       │
│    yarık (sehpada sağ önde) taban x ≈778 · bant 750–810                       │
│    iki kişi 1,7 m · d ≈51 (kapı) → ≈35 px · d ≈60 (korkuluk) → ≈30 px          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ KAMERA İSTASYONU (KUBBE · yalnız S17) ──────────────────────────────────────┐
│ lens 24 mm · f/8 · ISO 1600 · clamp mount, davul duvarının içinde, gözlem      │
│ katının arkasında · h +2,0 (kattan) · kaideye 10 m · bakış 160° (GGD, yarığa) ·│
│ tilt 0 · roll 0 · kadraj: büyük karanlık ekran x 140–780 · %12–50 (≈üçte bir)  │
│ · çatal x 900–1260 · yarık x 1300–1480 (≈180 px · %64 → üst kenar) · iki kişi  │
│ masanın sağ ucunda, sırtı dönük                                               │
│ ⚠️ iç kadraj hesaplanmadı, tarif edildi — G17′ usta iç karede ÖLÇÜLÜR          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① ⭐ DAĞ ÇAMI (SAĞ · x 1652–1805 · 551–870) — KANIT NESNESİ, kaya çıkıntısında,│
│    rüzgârla bükülmüş, düz koyu taç; mevsimle değişmez (iğne yapraklı)        │
│ ② İKİ UZAK TEPE — ikiz doruklu sivri tepe (sol) · uzun düz sırt (sağ) —       │
│    siluet her karede aynı · ⚠️ x'leri yaklaşık; usta karede ölçülür           │
│ ③ UFUK %77,4 (244) · ④ BULUT DENİZİNİN DÜZEYİ — yüzeyi akar, düzeyi sabit     │
│ ⑤ servis yolu (sol kenardan pede) · uçurum kenarı (davulun arkası)            │
│ ⑥ TAŞ ÖRGÜSÜ (uzun alçak sıralar, ince koyu derz) — iç klibin ortak cümlesi   │
│ + "The summit holds exactly one building site, this one, and exactly one      │
│   dome" — her NEGATIVE'de                                                     │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ tilt 13° → ufuk %77,4 · gök bandı üstten 0–244 (kapak başlığı burada)         │
│ yanlar: solda beşik + sehpa + istif + servis yolu · sağda kule + teras + çam   │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ — kanıt nesnesi alt 100 px'e (üstten > 980) ve  │
│ sağ üst 300×100 px'e (x > 1620 · üstten < 100) girmez ✓ (çam tacı 551, dip 870)│
│ ⚠️ keystone: tilt 13°'de davulun dikey kenarları hafif yakınsar — kabul edilen │
│    bedel (KAMERA_DILI §3 ③)                                                   │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ davul: Ø 24 m (x −2…+22 · eksen d 64) · 4 m · açık gri granit, uzun alçak     │
│   sıralar · tek kemerli ahşap kapı (≈2,5 × 3 m, önde) · duvar tepesinde çelik  │
│   halka ray · iç zemin Ø 22 m (koyu tahta → açık panel)                        │
│ kubbe: Ø 24 m yarım küre · tepe +16 (davulda) · tek gözlem yarığı ≈3 m genişlik│
│   tabandan tepeye · TEK bakır kapak (kızakta yukarı, tepeye kayar) · halka ray │
│   üstünde döner · yarık sağ önde (159°) → S18'de önde (189°)                   │
│ teleskop: kaide Ø 3 m · +2 · koyu gri çatal (kollar +6,5'e) · soluk beyaz tüp  │
│   Ø 2,4 m · 9 m · eksen +5,5 · dik parkta tepe +12 (kubbe içi 16 m ✓)         │
│ teras: x +23…+38 · d 56–72 · eski taş döşeme · S13'ten çelik korkuluk         │
│ yol: pedden kapıya (d ≈49) · eski: tekerlek izli çakıl + çatlak basamak →     │
│   yeni: geniş açık taş plaka + yeni basamak + alçak yol lambaları             │
│ ped: x −45…0 · çakıl · kubbe bakım sehpası (Ø 24, tahta yürüme yolu) · uzun   │
│   çelik beşik (9 m, önde solda) · istif alanı (önde) · iki iskele kulesi      │
│   (davulun iki yanında, ≈7 m)                                                  │
│ STRUCTURE'ın İngilizce tam hâli tek cümle (DERS 36): "When finished this will be│
│   a mountain-top observatory: a low round drum of pale grey granite, 24 metres │
│   across and 4 metres high, with an arched timber door and stone steps, under │
│   a copper dome of the same width that turns on a steel ring rail on the wall │
│   top and has one observing slit closed by a single copper shutter; inside, a │
│   large telescope with a dark grey fork mount and a long pale white tube; on  │
│   the right a paved terrace with a steel railing at the cliff edge." — 22      │
│   görselde (G17′ dâhil) BİREBİR                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 20 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az YAPI göstermez. Bu filmde söküm önce gelir (S0–S1:
> kubbe ve tüp YERİNDEN alınır ama kadrajda KALIR — sehpa ve beşik), sonra her parça onarılmış olarak geri döner.
> Kış görüntüsü YOK (karsız zirve — kış yalnız gökte berrak hava; DERS 7 tetiklenmez).

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | İSTASYON | KANIT NESNESİ (px) |
|:-:|:-:|---|---|:-:|:-:|:-:|:-:|---|
| 0 | 8,0 | KALDIRIR | kubbe havada → sehpaya (%100) · teleskop açığa çıkar | 1 gün | A | 07:35→07:45 | ANA | kubbe 716–1204 → 382–877 |
| 1 | 8,0 | SÖKER | tüp çataldan → beşiğe (%100) · çatal kalır | 1 gün | A | 07:45→07:55 | ANA | tüp 1136–1184 → beşik 140–371 |
| 2 | 8,0 | TEMİZLER | sarmaşık + kir → temiz taş (%0 → %100, soldan) | 6 hafta | B | 07:55→09:55 | ANA | davul 920–1400 renk |
| 3 | 8,0 | KAPLAR | kubbe yeşil → yeni bakır (%0 → %100) · eski kapak kalır | 3 ay | B | 09:55→11:55 | ANA | kubbe 382–877 renk |
| 4 | 8,0 | YENİLER | paslı ray → yeni ray (%0 → %100) | 3 hafta | A | 11:55→12:05 | ANA | duvar tepesi 807 bandı |
| 5 | 8,0 | DÖŞER | iç zemin koyu → açık panel (%0 → %100, arkadan) | 4 hafta | B | 12:05→14:05 | ANA | zemin bandı 702–807 |
| 6 | 8,0 | YENİLER | tüp panelleri kirli → yeni (%0 → %100) | 6 hafta | A | 14:05→14:15 | ANA | beşik 140–371 renk |
| 7 | 8,0 | GERİ GETİRİR | tüp beşikten → çatala, yatay (%100) | 1 gün | A | 14:15→14:25 | ANA | tüp 1070–1250 |
| 8 | 8,0 | SINAR | tüp yatay → dik park (tek hareket) | 1 gün | A | 14:25→14:35 | ANA | tüp tepesi 563 |
| 9 | 8,0 | DEĞİŞTİRİR | yeşil kapak → yeni bakır kapak (%100) | 2 hafta | A | 14:35→14:45 | ANA | yarık 750–810 renk |
| 10 | 8,0 | KALDIRIR | kubbe sehpadan → davulun üstünde asılı | 1 gün | A | 14:45→14:55 | ANA | kubbe → 920–1400 · 428 |
| 11 | 8,0 | OTURTUR | kubbe asılı → halka rayda (%100) · ⭐ DORUK | 1 gün | A | 14:55→15:05 | ANA | ⭐ kubbe tepesi 428 → 487 |
| 12 | 8,0 | DÖŞER | yol + basamak eski → yeni plaka (%0 → %100) · lambalar | 4 hafta | A | 15:05→15:15 | ANA | yol 925 bandı |
| 13 | 8,0 | ÇEVİRİR | teras kenarı açık → korkuluk (%0 → %100) | 3 hafta | A | 15:15→15:25 | ANA | teras 1486–1829 |
| 14 | 8,0 | TOPLAR | kuleler + sehpa + beşik + istif → kamyonla gider · gün batımı | 2 hafta | B | 15:25→17:25 | ANA | kuleler → 0 · gölge +55° |
| 15 | 8,0 | AYRILIR | vinç gider · lambalar belli belirsiz yanar | 1 gün | A | 17:25→17:35 | ANA | vinç 914 → 0 |
| 16 | 8,0 | AÇAR | kapak kapalı → tepeye kayar, yarık açık · kırmızı ışık | 10 dk | A | 17:35→17:45 | ANA | yarık 1275–1340 açık |
| 17 | 8,0 | YÖNELİR | (iç) teleskop son salınım → hizalı · ekran karanlık (bindirme) | 8 sn | G | 17:45 (+8 sn) ∥ S16 sonu | KUBBE | yarık ≈180 px |
| 18 | 8,0 | DÖNER | kubbe ≈30° döner: yarık sağ önden → öne · ilk yıldızlar | 10 dk | A | 17:45→17:55 | ANA | yarık 1275–1340 → 1125–1195 |
| 19 | 8,0 | GÖZLER | iki kişi korkuluğa · araç gider · TUTUŞ | 10 dk | A | 17:55→18:05 | ANA | ⭐ yarık önde · kişiler x ≈1600 |

```
IZGARA          8,0 sn × 20 · kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn) · müzik 120 BPM → her kesme ölçü başında
                (8,0 sn = 4 ölçü)
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: sahip senaryosunun biçimi (20 × 8,0, kart yok — hikâye SAPMA ②); yatay_2 README'deki sahip
                       izinli modül dışı ızgara (16.09.2026) — ⚠️ ama toplam süreyi KORUMAZ (2:00 → 2:40); emsal THE OLD
                       ROAD · THE HIDDEN FALLS · THE BURIED KHAN (15 × 8,0). ⚠️ BANDIN DIŞI: format 12 × 10,0.
                   (b) ritim klip İÇİNE: ① rejim nabzı — B'ler S2 · S3 · S5 · S14 (temizlik, kaplama, zemin, söküm + gün
                       batımı), G S17 (gerçek hız — teleskop); ② iş yönü değişir: yukarı-sola (S0 kubbe) · yukarı (S1 tüp) ·
                       soldan sağa (S2 temizlik · S3 bakır · S6 tüp panelleri) · çember (S4 ray · S18 dönüş) · arkadan öne
                       (S5 zemin) · sağa-aşağı (S7 tüp) · dikey dönüş (S8 test) · yukarı-sağa (S10) · aşağı (S11) · boyuna
                       (S12 yol · S13 korkuluk) · dışarı (S14–S15); ③ müzik katmanı = aşama (MUZIK.md)
                   (c) kabul edilen risk: eşit klipte ❷ RHYTHM kategorisi NOT TRIGGERED — sapma kurgudan gelirse (klip ≠ 8,0)
                       ❷ açılır ve ❺ final saniyesi kayar. Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
                       20 eşit kesme 15'ten fazla nabız demektir: METRONOM riski ARTAR.
REJİM SAYISI    ⚠️ ÜÇ rejim (A · B · G) — SANTIYE_HAREKETI §2 sınırı iki. Gerekçe: G yalnız iç klip S17'dir (teleskobun son
                salınımı gerçek hızda okunur); dış zincirde yalnız A + B. Geçiş KESMEDE (S16 → S17 → S18) [P5-c].
IŞIK GÜNÜ       Σ pencere = 15 A × 10 dk + 4 B × 2 sa = 150 dk + 8 sa = 10 sa 30 dk ≤ 14 ✓ · S17 (G) S16'nın içinde ∥ — toplanmaz
                07:35 (güneş 12°) → 18:05 (koyu mavi saat, güneş −8,5°)
BÖLÜM SINIRI    G10 — sahne S9 son karesi = sahne S10 ilk karesi; teleskop dik park, kubbe sehpada pembe bakır + YENİ kapak,
                dört sapanı vince bağlı, beşik boş, iskele kuleleri yerinde, yol eski, teras çıplak, gölge +47°, yaz —
                ikisinde de aynı [DERS 52]
TEK OLAY        S10 + S11 (sahip: "16 saniyelik tek olay iki klibe bölünür") — G11 ortak kare: kubbenin yüksekliği,
                yönü, sapanları, gün ışığı iki klipte aynı
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: DAĞ ÇAMI — G0'da ve usta karede (G20) aynı konum (x 1652–1805) ve aynı boy (153 px en · taç 551 ·
        dip 870) [DERS 25]; kaya çıkıntısında, iğne yapraklı, mevsimle değişmez. Yedek: ikiz doruklu tepe (siluet). İç
        klipte ortak çapa TAŞ ÖRGÜSÜ cümlesi (çam yarıktan görünmez — SAPMA ⑧).
LOOP    G20 ↔ G0: aynı kadraj · aynı çam · aynı iki tepe · ışık FARKLI (bilinçli — G0 sabah, G20 koyu mavi saat; tek gün):
        davulun üstünde havada yeşil kubbe / davulun üstünde yerleşik, yarığı kameraya açık kahverengi kubbe. Biçim
        kafiyesi: kubbenin yarım küre silueti iki karede aynı yerde (G0 716–1204 havada · G20 920–1400 oturmuş — yer
        değiştirmiş ama aynı nesne).
SÖKÜM   S0 düz kasalı kamyon (boş kasalar, gider) · S1 küçük kamyon · S2 küçük kamyon (kasalar) · S3–S6 düz kasalı kamyonlar
        (bakır · ray · zemin · tüp panelleri, boşalınca gider) · S8 taşıma çerçevesi kamyonla gider · S9 kamyon · S10
        yürüme yolu tahtaları istife · S11–S13 kamyonlar (plaka · korkuluk) · S14 İKİ İSKELE KULESİ + SEHPA + BEŞİK +
        İSTİF + kamyonlar · S15 VİNÇ (bomunu yatırır, sol yoldan çıkar) + küçük kamyon (alet kasaları) · S19 servis aracı —
        ekranda gider; yol + lambalar + korkuluk KALIR (kalıcı) [DERS 48 · P2-h]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
kubbe (eski)             → davuldan vinçle → soldaki bakım sehpası (x 382–877)                     → G0 · G1
tüp (eski)               → çataldan vinçle → öndeki uzun çelik beşik (x 140–371)                    → G1 · G2
sökülen sarmaşık + kir   → ekip → kasalarla istif alanı (x 601–755, pedin önü)                     → G2 · G3
yeni bakır               → düz kasalı kamyonda paletler → vinç → sehpanın yürüme yolu               → G3
yeni ray                 → düz kasalı kamyon · eski ray istife                                      → G4
zemin panelleri          → düz kasalı kamyonda paletler → vinç → açık davulun içi                   → G5
tüp panelleri            → düz kasalı kamyonda paletler → vinç → beşik                              → G6
tüp (yenilenmiş)         → beşik → vinç (çerçeve + dört sapan) → çatal                              → G7
yeni kapak               → S8 sonunda kamyonla → vinç → kızaklar · eski kapak istife                → G9
kubbe (yeni bakır)       → sehpa → vinç (dört sapan) → davulun üstü → halka ray                     → G10 · G11
taş plakalar             → S11 sonunda düz kasalı kamyonla → vinç → yol                              → G12
korkuluk modülleri       → düz kasalı kamyonda demetler → vinç → teras kenarı                        → G13
küçük sandıklar          → servis aracı → kapı                                                      → G16 · G18
GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL (prompta yalnız vekil girer):
   aynanın ve optiğin bakımı → beşikte panel panel yenilenen tüp (S6) · motor/elektrik → S8'de dikilen tüp + S16'da kayan
   kapak + yanan yol lambaları + S18'de dönen kubbe · gözlem → S17 ekran (bindirme)
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① kameraya açık yarık + içindeki loş kırmızı ışık (x 1125–1195 · üstten 487 → 807, ilk okunan, en sıcak) → ② yarıkta göğe
   dönük soluk beyaz tüp → ③ bütün kubbe (kahve bakır) + temiz davul (920–1400) + açık renkli yol ve basamaklar → ④
   korkulukta iki küçük kişi (x ≈1600 · ≈30 px) → ⑤ çam (kanıt) + iki uzak tepe + bulut denizi + ilk yıldızlar
FİNAL KARE KANITI  ffmpeg -ss 159.0 -i teslim.mp4 -frames:v 1 kanit.jpg   (S19 tutuşu 156,0–160,0 içinde · koyu mavi saat,
                   okunur [DERS 45]) · kart YOK → son kare = G20
```

---

## 🖼️ KARE TABLOSU — 21 ana görsel + G17′ [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Gölge yönü kadrajda: 0 = kameradan uzağa · − sola · + sağa (|x| > 90 = kameraya doğru). Güneş DİSKİ anılmaz.
> Sayılar `bolum_uretici.py --tablo` çıktısıdır (30° K · δ −15° · güneş saati · kamera bakışı 0°).

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| G0 | 07:35 | 115° | 12,0° | −65° | berrak soluk gök, bulut denizi beyaz | kış · hava çok berrak, tepeler keskin | ⭐ AÇILIŞ — yeşil kubbe havada · tozlu teleskop davulda · iskele kuleleri |
| G1 | 07:45 | 117° | 13,9° | −63° | aynı | aynı | kubbe sehpada · tüp sapanda |
| G2 | 07:55 | 118° | 15,8° | −62° | berrak | aynı | çatal boş · tüp beşikte · bom ucu kadraj dışı |
| G3 | 09:55 | 142° | 35,9° | −38° | birkaç küçük yüksek bulut | bahar | taş temiz · ray paslı · bakır paleti vinçte · istif: sarmaşık |
| G4 | 11:55 | 178° | 45,0° | −2° | aynı | bahar · yeni bakır pembe | kubbe yeni bakır + YEŞİL kapak · ray parçası vinçte |
| G5 | 12:05 | 182° | 45,0° | +2° | aynı | aynı | ray yeni · zemin koyu · zemin paleti vinçte |
| G6 | 14:05 | 218° | 35,9° | +38° | aynı | aynı | zemin açık panel · tüp paneli paleti vinçte |
| G7 | 14:15 | 221° | 34,5° | +41° | aynı | aynı | tüp yenilenmiş, çerçevede, sapanlı |
| G8 | 14:25 | 223° | 33,0° | +43° | uzakta yükselen beyaz bulutlar | yaz | tüp çatalda YATAY · boş çerçeve vinçte |
| G9 | 14:35 | 225° | 31,5° | +45° | aynı | aynı | tüp dik park · yeni kapak vinçte |
| G10 | 14:45 | 227° | 30,0° | +47° | aynı | aynı | ⭐ BÖLÜM SINIRI — kubbe yeni kapakla sehpada, sapanlı |
| G11 | 14:55 | 229° | 28,4° | +49° | aynı | aynı | kubbe davulun üstünde ASILI, hizalı · sehpa boş |
| G12 | 15:05 | 231° | 26,7° | +51° | aynı | yaz · bakır pembeden kahveye dönmeye başlar | kubbe davulda · plaka paleti vinçte · yol eski |
| G13 | 15:15 | 233° | 25,0° | +53° | aynı | aynı | yol yeni + lambalar (sönük) · korkuluk demeti vinçte |
| G14 | 15:25 | 235° | 23,2° | +55° | berrak, ince yüksek bulut | sonbahar · bakır sıcak kahve | korkuluk tamam · kuleler, sehpa, beşik, istif yerinde |
| G15 | 17:25 | 253° | −0,1° | — (güneş ufukta) | gün batımı, bulut denizi pembe | sonbahar · berrak | saha temiz · vinç, bom ucu kadraj dışı |
| G16 | 17:35 | 254° | −2,2° | — (güneş ufkun altında) | erken mavi saat | aynı | yarık kapalı · lambalar yanık · servis aracı yolda |
| G17 | 17:45 | 255° | −4,3° | — | yarıkta koyu mavi gök | aynı | 🔭 KUBBE İÇİ — tüp yarığa iniyor · ekran karanlık · iki kişi |
| G17′ | 17:45 +8 sn | 255° | −4,3° | — | aynı | aynı | 🔭 KUBBE SON KARESİ — tüp hizalı, durgun |
| G18 | 17:45 | 255° | −4,3° | — | mavi saat | aynı | yarık açık SAĞ ÖNDE · kırmızı ışık · tüp dışarı bakar |
| G19 | 17:55 | 256° | −6,4° | — | koyu mavi saat, ilk yıldızlar | aynı | yarık ÖNDE · iki kişi kapıda |
| G20 | 18:05 | 258° | −8,5° | — | ⭐ koyu mavi saat, parlak yıldızlar | aynı | ⭐ USTA KARE — yarık önde açık · iki kişi korkulukta |

```
KUBBE DEFTERİ (kare kilidi [P10-e])   G0 havada (716–1204 · tepe 451), yeşil · G1–G3 sehpada (382–877 · 544), yeşil · G4–G9
   sehpada, pembe bakır + ESKİ YEŞİL KAPAK · G10 sehpada, yeni kapak · G11 davulun üstünde asılı (920–1400 · 428) · G12+
   davulda (920–1400 · 487) · G12 pembe → G14+ kahve · yarık: G0–G16 kapalı, SAĞ ÖNDE (sehpada 750–810 · davulda 1275–1340)
   · G17–G18 açık, sağ önde · G19–G20 açık, ÖNDE (1125–1195)
   ⛔ kubbe ikiye ÇOĞALMAZ: G1–G10'da davul açık, kubbe yalnız sehpada · G11'de sehpa boş, kubbe havada · G12+ yalnız davulda
TELESKOP DEFTERİ   G0–G1 çatalda dik, tozlu (1136–1184 · 563) · G2–G7 çatal boş; tüp beşikte (140–371): G2–G6 kirli, G7
   yenilenmiş + çerçeve · G8 çatalda yatay (1070–1250 · 683) · G9–G11 dik park (563) · G12–G16 kubbenin altında, görünmez ·
   G18+ tüpün ucu yarıkta
ZEMİN · YOL · TERAS   iç zemin G0–G5 koyu, G6+ açık (G12'den sonra kubbenin altında) · yol G0–G12 eski, G13+ yeni, lambalar
   G16+ yanık · teras G0–G13 çıplak kenar, G14+ korkuluk · iskele kuleleri + sehpa + beşik + istif G0–G14 · vinç G0–G15
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G20 usta kare → G19 (iki kişi kapıda, araç pedde) → G18 (yarık sağ önde) → G16 (yarık kapalı, ışıksız kubbe, lambalar) →
   G15 (vinç, bom ucu dışarıda, pad boş) → G14 (kuleler, sehpa, beşik, istif geri gelir) → G13 (korkuluk yok) → G12 (yol
   eski) → G11 (kubbe davulun üstünde asılı) → G10 (kubbe sehpada) → G9 (yeşil kapak) → G8 (tüp yatay) → G7 (tüp beşikte,
   çerçevede) → G6 (tüp kirli) → G5 (zemin koyu) → G4 (ray paslı) → G3 (kubbe yeşil) → G2 (taş kirli, sarmaşıklı) → G1
   (tüp çatalda) → G0 (kubbe havada)
   KUBBE İÇİ: G17′ ana G18'in ışığıyla ÖNCE → G17 (tüp yarığın yukarısında) · ayrı zincir, ana zincire bağlanmaz
   ⚠️ ters inşada kubbe KALKAR: G12 → G11 → G10 adımlarında kubbe davuldan havaya, sonra sehpaya taşınır — iki kubbe
   çizilmez, px elle ölçülür
   sonra I2V S0 (G0→G1) … S19 (G19→G20) — her klip iki uca kilitli, üretim 9,0 sn, baştan 1,0 kırp · S16 G16 → G18
```

## 🧪 PİLOT ÜÇLÜ [DERS 62 · KILAVUZ_REHBERI §8 adım 2b]

```
⛔ Üretim başlamadan, aşağıdaki üçü geçmeden kalan klipler üretilmez:
① FİNAL      G20 + G19 + G18 + S18 — kubbe halkasında ≈30° döner, yarık sağ önden öne gelir; davul KIPIRDAMAZ, kubbe biçim
             değiştirmez, yarık tek kalır · ardından S19 tutuşu (son 4 sn yalnız bulut denizi akar) [C1-b]
② EN BÜYÜK   G0 + G1 + S0 — 24 m kubbe havada: dört sapan, tek parça, yavaş; kopyalanmaz, sapandan kopmaz [DERS 8 · 57];
   DEĞİŞİKLİK  altındaki teleskop ilk karede tanınır · S0 = 00:00 (kanca)
③ İÇ KLİP    G17 + G17′ + S17 — teleskop yarığa tek yumuşak hareketle hizalanır, büyük ekran KARANLIK kalır (model ekranda
             görüntü üretirse bindirme yine yapılır ama sızan yazı/şekil ❶ bulgusu olur)
PİLOT SONRASI İLK  S10 + S11 (G10 · G11 · G12) — kubbenin 16 sn'lik dönüşü; G11'de asılı kubbe iki klipte aynı yükseklik ve yön
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     30,0° K · ışık günü tarihi: δ −15° (sonbahar sonu — ışık tek gün; takvim sahadan) · doğuş 06:36 · batış 17:24
                (güneş saati) · kamera bakışı 0° (kuzey) → kadraj −37° … +37° · güneş 115° → 258°: sabah kameranın ARKASINDA
                sağda, öğle tam arkada, akşam arkada solda — HİÇBİR karede kadrajda değil, ters ışık YOK [P8-h]
DAVUL IŞIĞI     davulun ön yüzü güneye (kameraya) bakar → bütün gün önden ışık: sabah sağdan (gölgeler sola ve uzağa),
                öğle düz (G4–G5 gölge kameradan uzağa), öğleden sonra soldan sıcak (S10–S13) · S14'te gün batımı · G15+ güneş yok
GÖLGE SÜPÜRMESİ rejim B klipte: S2 (−62° → −38°: 24°) · S3 (−38° → −2°: 36°) · S5 (+2° → +38°: 36°) · S14 (+55° → güneş batar)
                · rejim A klipte fark edilmez → yüzeyle kanıtlanır
MEVSİM YAYI     kış (G0–G2: çok berrak, tepeler keskin) → bahar (G3–G7: küçük yüksek bulutlar, yeni bakır pembe) → yaz (G8–G13:
                uzakta yükselen beyaz bulutlar) → sonbahar (G14–G20: berrak, bakır kahve) · taşıyıcı: GÖK + BAKIRIN RENGİ
                (yeni bakır haftalar içinde pembeden kahveye döner — betonun kürlenmesinin karşılığı) · çam iğne yapraklı,
                değişmez (çapa) · ⚠️ sahip metni "kısa bir sonbahar günü hissi" der; ışık sonbahar günüdür, mevsim gökte
KIŞ             görüntü YOK (karsız zirve) · DERS 7 tetiklenmez
GECE            yok · final KOYU MAVİ SAAT, güneş −8,5° (G20) · zifiri değil: bakır, taş, açık yarık ve iki kişi okunur;
                yarıktaki kırmızı ışık kadrajın en sıcak noktası [DERS 45] · Samanyolu YOK (hikâye SAPMA ⑭)
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   ANA h +28,0 · D_eksen 64,0 · D_kenar 52,0 · bakış 0° · tilt 13° aşağı · roll 0 · KUBBE (S17) h +2 · bakış 160° · tilt 0
YAPI     davul 920–1400 · ön dip 890 · ön duvar tepesi 807 · iç zemin 702–807 · kubbe (davulda) tepe 487 · kapı 1175–1237 ·
         tüp dik 1136–1184 · 563 · tüp yatay 1070–1250 · 683
KUBBE    havada 716–1204 · 451 (G0) · sehpada 382–877 · 544 (G1–G10) · asılı 920–1400 · 428 (G11) · davulda (G12+) ·
         yarık sağ önde 1275–1340 → önde 1125–1195
ÇAPALAR  ① ÇAM x 1652–1805 · 551–870 (kanıt nesnesi 153 px) · ② iki uzak tepe · ③ ufuk 244 · ④ bulut denizi düzeyi ·
         ⑤ taş örgüsü (iç klip)
IZGARA   20 × 8,0 · kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn) · kart YOK · 160,0 sn · 120 BPM
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_FIRST_LIGHT   → sonuç QA_SPEC §8'de (10.10.2026)
✅ FIX'ler ve beyanları (hepsi elle okundu):
   · ARAÇ KUTU SETİ ölçülmedi — beyanlı; üretim araç kapısıyla açılır
   · süreler eşit (8,0) — düz ızgara (sahip senaryosu, SAPMA ②); beş mercekte ❷ RHYTHM eşit klipte tetiklenmez
✅ YASAK KELİME taraması 0 · kelime kilitleri (crane G0–G15 · glow/lit S15+ · red light S16+ · stars S18+ · yarık "open"
   S16+) betikle doğrulandı (10.10.2026 · 42 blok)
✅ 00_ANALIZ yedi dosya · hikâye onayı 10.10.2026 (TUR 3 · SAPMA ①–⑰ sahip okur)
⛔ ARAÇ KAPISI koşulmadı → THE_FIRST_LIGHT_URETIM_GUNLUGU.md §0
⛔ PİLOT ÜÇLÜ koşulmadı → S18 · S0 · S17
⛔ EKRAN BİNDİRMESİ görüntüsü seçilmedi → günlük §5 (kaynak + lisans)
⛔ SÜRE / KLASÖR — 160 sn yatay_2_dk bandının dışında (SAPMA ②) → sahip kararı
```
