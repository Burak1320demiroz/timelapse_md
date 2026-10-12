# 🎭 THE_SUNKEN_STAGE — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **20 × 8,0 sn = 160,0 sn** | Kapak kartı: **⛔ YOK** | Toplam: **160,0 sn**
Prompt yapısı: ⭐ **20 sahne → 21 görsel (G0…G20) + 20 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G10**
Yapı: **ormanda bir çukurun dibinde, su basmış, terk edilmiş açık hava tiyatrosu — 12 geniş, eş merkezli yarım daire taş oturma terası (iç yarıçap 16 m → dış 30,4 m, basamak 1,2 m × 0,6 m) · üç radyal taş merdiven · 26 × 13 m dikdörtgen taş sahne platformu · sonradan: ahşap oturma tahtaları, ahşap sahne, sahnenin arka üçte birinde bakır renkli yelpaze akustik kabuk, iki teknik kule, iki taş döşeli giriş yolu** (en yakın kart `YAPI_TIPI_KARTLARI` STADYUM satırı ⚠️ birebir değil — burada inşa değil TAHLİYE + ONARIM + DONATIM; sıra 00_ANALIZ/02 §2a'da bu film için yazıldı) · Saha: **sonbahar karışık ormanı içinde derin çukur, 47° K** (`SAHA_VE_IKLIM_KARTLARI` kırsal satırı ⚠️ birebir yok; 02 §2b)
Zaman yayı: **gerçekte ≈4–5 ay (birkaç günlük tahliye → aylarca onarım ve donatım → açılış akşamı) → 160 saniye** · film mertebe anlatır: *"bir sabah su çekilir, bir mevsim taş ve ahşap, bir akşam konser"* [P1-c] · ÜSLUP BEYANI (sahip senaryosu): bütün iş tek bir kısa ekim gününün ışığına sıkıştırıldı — "tek günde yapıldı" iddiası DEĞİLDİR, ekranda süre vaadi yok
Işık günü: **09:20 → 17:50 (mavi saat, güneş −4,9°) · Σ rejim penceresi 8 sa 30 dk ≤ 14** — kesmede ışık atlamaz [§2.7 ①]
Kamera mimarisi: **MAIN STATION** — 20 klip + usta kare, **%100** · ikinci istasyon YOK
Izgara: ⛔ **DÜZ — 20 × 8,0** · ⚠️ BANDIN DIŞI (format 12 × 10,0 · 2:00) — sahip senaryosunun biçimi, toplam 2:40 (hikâye SAPMA ②) · §DÜZ IZGARA BEYANI
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 12.10.2026 (TUR 1 · "bunu bozmadan hazırla … bol iş, bol hareket, bol işçi" · 20 satır · SAPMA ①–⑯)
Havuz kaydı: `apexait/YAYIN_PLANI.md` — ⬜ satır açılmadı (sahip kararı) · siluet ailesi: **yukarıdan bakılan çanak + ışık finali** (THE DEEP END su çekilen havuz + küçük ışıklar akrabası; THE LAST CIRCLE çanak/halka akrabası)

_"İlk karede kahverengi suyun içinden yalnız iki taş yayın çıktığı, kenarında pompaların çalıştığı su basmış bir çukur; son karede aynı çukurda, mavi akşamda ışıkları yanmış, seyirciyle dolu bir tiyatro ve bakır kabuğun altında çalan küçük bir topluluk."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     20 sahne × 8,0 sn                       = 160,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     ⛔ YOK — tam 160,0 sn (sahip senaryosu: "Afiş veya kapanış kartı eklenmez") · ihrac_kontrol.sh --kart YOK
──────────────────────────────────────────────────────────────
TOPLAM                                                     160,0 sn
HIZ             1x (yatay hat 2x'e çevrilmez — 2x yalnız dikey paylaşım kuralıdır [DERS 58])
MÜZİK           ✅ VAR — sahip senaryosu "Ses tasarımı": diyalogsuz; çevre sesi + görünen işle eşleşen kısa mekanik sesler +
               özgün ya da lisanslı tek parça; S8–S13 kademeli büyür, S14–S16 geri çekilir, S18'de sahnedeki topluluğun
               AÇILIŞ PARÇASINA dönüşür (diegetik), S19 alkış · 120 BPM (8,0 sn = 4 ölçü) · THE_SUNKEN_STAGE_MUZIK.md
YAZI            ⛔ YOK (tercih edilen sürüm) · yedek: S0'da tek kısa cümle "THIS PLACE WILL HEAR APPLAUSE AGAIN." kurguda,
               taş yayları örtmeden — görüntü modeline YAZDIRILMAZ (hikâye SAPMA ⑭)
YASAK KELİME    amphitheatre · amphitheater · arena · colosseum · stadium · roman · greek · ancient · ruin · ruins · temple · statue · column · archaeology · archaeological · arch · fireworks · confetti · laser · flare · bloom · glow · rays · beam · haze · smoke · fog · drone · neon · lake · pond · pool · swimming · fountain · boat
               ⭐ [DERS 59 · 55 · 42] hiçbir promptta, negatifte bile — "amphitheatre · arena · colosseum · stadium · roman ·
                  greek · ancient · ruin · temple · statue · column · archaeology · arch" antik/arkeolojik harabe ve stadyum
                  korpusunu çağırır (sahip: "gerçek bir arkeolojik keşif olarak sunulmaz", "no fictional ruins"); "fireworks ·
                  confetti · laser · flare · bloom · glow · rays · beam · haze · smoke · fog" sahip yasağı + ışık kılavuzunun
                  pozitif-tarif kuralı [ISIK_FINALI §5]; "drone · neon" kamera hareketi ve gündüz gibi gece; "lake · pond ·
                  pool · swimming · fountain · boat" su basmış çanağı göle/havuza çevirir, yıkama püskürtmesini fıskiyeye,
                  suya tekne koyar
KELİME KİLİDİ   kahverengi taşkın suyu ("floodwater · brown water · water line") yalnız G0–G2 + S0–S2 I2V · "mud" yalnız G3 +
               S2–S3 I2V · "crane" yalnız G5–G13 + S4–S13 I2V [P7-e] · TAKILI oturma tahtaları S6 I2V + G7'den · çelik ızgara
               S7 I2V + G8'den · ahşap sahne S8 I2V + G9'dan · dikili kaburgalar S9 I2V + G10'dan · "copper" S10 I2V +
               G11'den · "towers" S11 I2V + G12'den (STRUCTURE tam hâli hariç) · lambalar YANIK S15 I2V + G16'dan · oturan
               seyirci ("seated audience") S16 I2V + G17'den · alkış yalnız S19 I2V + G19–G20 · STRUCTURE'da renk, su, ışık,
               insan yok (yalnız yapı) [DERS 36] · tarama betiği 41 blokta 0 ihlal (12.10.2026)
BÖLÜM DOSYASI   BOLUM_1 = S0–S9 (0–80,0)  ·  BOLUM_2 = S10–S19 + USTA KARE (80,0–160,0) · ceil(20/2)=10
QA BİRİMİ       FİLM (tek master × 5 mercek · ❶ ❷ ❸ kör · ❹ ❺ belgeli) — QA/HAM/THE_SUNKEN_STAGE/
```

⛔ Kart olmadığı için platform son ekranı **son 5 saniyeye konmaz** ya da yalnız gök bandına (üstten 0–105 px) konur — sahnenin, kabuğun (x ≈785–1135 · üstten 267–470) ve dolu sıraların üstüne yerleştirilmez.
⚠️ Son sahnenin (S19) ikinci yarısı TUTUŞTUR (final kanıtı 156,0–160,0, `QA_SPEC` §1): sahne ışıkta, seyirci yumuşak alkışlar, ağaç tepeleri hafif sallanır; yapıda hiçbir şey değişmez. Son kare donmaz (sahip: "Son sekiz saniyeyi dondurulmuş bir görselle doldurmak" yasak).
⭐ Platform küçük resmi (kapak) G20'den gelir (sahip kararı 19.09.2026 + sahip senaryosu — öncesi/sonrası bölme yok).

### ⭐ İZLEYİCİ KAPISI [C2-a…d · KILAVUZ_REHBERI §6]

```
İŞLEV ANI         S15 lambalar gruplar hâlinde yanar → S16–S17 seyirci iki yoldan ve üç merdivenden gelip oturur → S18 ana sahne
                  ışıkları gerçek zamanda yükselir, topluluk çalmaya başlar → S19 müzik yükselir, alkış. Tiyatro yalnız
                  bitmez, KULLANILIR.
AÇILIŞ NESNESİ    G0: kahverengi suyun içinden çıkan iki üst taş yay (orta üstten ≈814–858 · yanlarda ≈433) + sol üstte çalışan
                  pompalar ve suya inen kalın siyah hortumlar · ona ne oluyor: su İLK KAREDE alçalıyor, yeni yaylar beliriyor.
                  120 px'te okunan: kahverengi bir çukur + altta iki açık renkli eş merkezli yay + solda sarı lekeler.
DİRENÇ EKRANDA    ① su ve çamur — S0–S2 alçalan su (11. teras → 7. teras → sahnenin üstü → yok) · S3 kalın çamur · S4 kirli
                  taş ② hasar — S1'de beliren kırık sol merdiven (S5'te onarılır) ③ boşluk — sahne çıplak taş (S7–S8 ahşap
                  sahne, S9–S10 kabuk) ④ boş sıralar — G0–G16 hiç seyirci yok
DÖNGÜ KAFİYESİ    G20 ↔ G0 aynı kadraj, aynı yarık kaya (x 286–384), aynı iki çam, aynı arka duvar: G0'da çanak kahverengi suyla
                  dolu, yalnız iki yay; G20'de aynı on iki yay seyirciyle dolu, su yerine ışık. Işık FARKLI, bilinçli: sabah ↔
                  mavi saat.
MERAK SORUSU      Suyun altında ne var?
AÇILIŞ DÜZENİ     ① NESNE sudan çıkan iki taş yay · ② DOKUNUŞ "From the first frame the water line is already sliding down" ·
                  ③ İPUCU yayların aynı merkezli olması + sol üstte pompalar — bunun bir çukur değil bir yapı olduğu 8. saniyede
                  anlaşılır, ne olduğu (sahne) henüz değil · ④ ÖLÇEK hortumları taşıyan ekipler (insan dış kenarda ≈58 px) +
                  pompalar + kamyon · AÇILIŞ GERİ ÇEKİLMESİ ⛔ YOK (sabit geniş)
ÜÇ TERCİH (sahip) keşif gecikmez (ilk 8 sn'de yaylar, ilk 24 sn'de bütün tiyatro) · dönüşüm uzaktan okunur (kahverengi su → açık taş →
                  sıcak ahşap → bakır kabuk → ışık ve kalabalık) · final verilen sözü tutar (yapı kullanılır, son kare donmaz) —
                  sahibin kurgu tercihi, ölçülmüş bir formül değil
BOL İŞ (sahip)    "bol iş olan, bol hareketli, bol işçili": S0–S14'ün her klibinde en az iki ekip + bir makine/araç + görünür
                  malzeme akışı (hortum · çamur · yıkama hortumu · taş blok · tahta demeti · modül · panel · kaburga · sandık ·
                  kule · döşeme taşı · palet · sandalye); ekip cümlesi "Dozens of workers … move fast in crews" (A) / "show only
                  as faint soft motion streaks" (B)
```

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Ormandaki su basmış bir çukurun altından dev bir açık hava tiyatrosu çıkar, onarılır ve aynı akşam konserle açılır.
DİRENÇ   ① su (çanak kahverengi taşkın suyuyla dolu; pompalarla, tek yönde, kademe kademe çekilir)  ② çamur ve kir (kalın çamur
         makineyle, silt basınçlı suyla gider)  ③ hasar ve eksik (kırık sol merdiven; çıplak sahne, kabuk yok, ışık yok)
         ④ boş sıralar (seyirci ancak her şey bitince gelir)
         EKRANDA NASIL [P1-b]:  S0–S2 · alçalan su çizgisi  ·  S3 · küçülen çamur yığınları  ·  S4 · kirli → açık taş bandı
                                aşağı iner  ·  S5 · kapanan merdiven boşluğu  ·  S6–S10 · ahşap yaylar, sahne, kabuk  ·
                                S15–S19 · yanan ışıklar ve dolan sıralar
BEDEL    ⭐ su + şantiye: G0'da çanak suyla dolu, pompalar, tanklar, hortumlar; su S2'de biter, çamur S3'te, vinç + pompalar +
         tanklar + paletler S13'te gider. G20'de aynı yerde ışıklı, dolu bir tiyatro. Okuma bilinçli: "tiyatro yapıldı" değil,
         "gölet yeniden alkış duydu".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            su + çamur + kir + kırık merdiven + pompalar, tanklar, vinç, paletler                        ✅
  □ kadrajda görünüyor mu?    su çizgisi orta üstten 814 → 748 → 717 → yok · pompalar x ≈232 · vinç x ≈578 · hasar x ≈656–708 ✅
  □ cevap "zaman geçiyor" mu? hayır — "su çekildi, taş temizlendi, sahne kuruldu, seyirci geldi"                         ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: su hangi terasın dibinde (11 · 7 · 3 · yok) · çamur var mı · taş kirli mi temiz mi, ıslak
                           mı · sol merdiven kırık mı · ahşap tahta kaç sırada · sahne taş mı ızgara mı ahşap mı · kaç kaburga ·
                           kabuk kaplı mı · kule var mı · yollar taş mı toprak mı · vinç, pompa var mı · lambalar yanık mı · kaç
                           sıra dolu · ana ışık açık mı
② KİNETİK BAĞIMSIZLIK   ✅ her klipte ekip + makine ya da seyirci hareket eder; su, yıkama suyu, ışık, insan akışı görünür
③ BAŞLIK ŞEMASI         ✅ kapak "THE SUNKEN STAGE" (3 kelime) · ⚠️ yayın başlığı sahibinin 54 karakteri (sınır 40 — SAPMA ⑮,
                           YAYIN_PAKETI'nde 40 altı yedek)
④ OMURGA CÜMLESİ [P1-k] ✅ boşaltır → açığa çıkarır → kurutur → temizler → yıkar → onarır → oturtur → çatar → kaplar → diker →
                           kaplar → kurar → döşer → boşaltır → yerleştirir → yakar → getirir → doldurur → açar → ALKIŞLATIR
```

⚠️ **Aile benzerliği [P16-a]:** THE DEEP END ile "su çekilen çanak + küçük ışıklar" akrabalığı; AYIRICI FARK: orada bir havuz
yeniden su alır, burada su GİDER ve yerine insanlar gelir; final bir kullanıcı kalabalığıdır. THE LAST CIRCLE ile halka/çanak
geometrisi ortak. Ardışık yayınlanmamalı (YAYIN_PLANI §3 — sahip kararı).

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera (ana istasyon %100)
                          ② kanıt nesnesi: YARIK KAYA (x 286–384 · üstten 94–201 · 98 px · 21 karede birebir)
                          ③ çapa: on iki teras + üç merdiven (sayı ve yer sabit) · dış kenar en geniş x 266 → 1654 · orta
                             merdiven tepesi üstten 858 · ④ arka duvar 344 · iki çam x 1490–1557 · ağaç çizgisi %90 (105)
                          ⑤ yalnız KAZANIR: su gider → taş temiz → merdiven tam → ahşap tahta → ahşap sahne → kaburga → kabuk
                             → kule → yol → ışık → seyirci (hiçbir yapı geri gitmez)
                          ⑥ SU KOTU DEFTERİ (aşağıda) — yalnız ALÇALIR: +6,1 (G0) → +4,1 (G1) → +1,5 (G2) → yok (G3)
                          ⑦ SEYİRCİ DEFTERİ (aşağıda) — oturan yerinde kalır; kimse koltukta "belirmez"
                          ⑧ insan: A/B'de iz ("soft motion streaks") · G'de küçük figür, sırtı kameraya · yüz okunmaz
                          ⑨ vinç kancası: ya YÜKLÜ ya bom ucu kadraj dışında — boş kanca yok (VİNÇ DEFTERİ)
                          ⑩ IŞIK DEFTERİ — lambalar önce SÖNÜK takılır, A'da grup grup TEK KAREDE yanar
P1.5 · fırsat buldukça   gölge süpürmesi (B: S4 · S6 · S10) · ıslak taşın kuruması (G5 → G7) · bakırın alçak güneşte ısınması
                          (S10 sonu) · gökyüzünün maviye koyulaşması (S15–S17)
SPEC · yalnız belge      azimut/yükseklik dereceleri (kapı şartı) · px tabloları
```

**Malzeme kimliği (her promptta):** *açık renkli kireçtaşı gibi soluk taş (önce siltle koyu, sonra temiz) · sıcak kahverengi ahşap oturma tahtaları · sıcak ahşap sahne · bakır renkli dış panelli, açık ahşap iç yüzlü kabuk · koyu çelik kuleler · sarı pompalar ve vinç · gri tanklar · turuncu iş kıyafetli ekipler · altın/turuncu/pas sonbahar ormanı, iki koyu yeşil çam* — korpus: "documentary site photograph on colour negative film" [DERS 34 · 42].
**İnsan kararı (sahip: "bol işçili"):** ekip her iş klibinde çok — A'da "small figures with soft motion streaks", B'de "faint soft motion streaks"; S14'te küçük bir müzik topluluğu sahnede; S16–S19 seyirci (A'da iz, G'de sırtı kameraya küçük figürler); hiçbir yüz okunmaz, yakın plan yok, dudak/çalgı ayrıntısı yok.
**Vinç kararı [DERS 8 · 22 · 46 · 57]:** tek büyük sarı mobil vinç, sahnenin solundaki hardstand'de destek ayakları üstünde (x ≈578 · üstten 465) · S4 sonunda gelir, S13'te gider (G5–G13). Bom dik kalkınca ucu kadrajın üstünden çıkar (vinçten bom ucu +40 m → üstten ≈ −450). VİNÇ DEFTERİ aşağıda; G14'ten sonra "crane" kelimesi yok [P7-e].
**Uzun rijit yük [DERS 57]:** ⚠️ KISMEN — kavisli çelik kaburgalar (≈14 m, S9) ve kule çerçeveleri (≈9 m, S11). Önlem: her biri tek tek, iki/dört gergin sapanla, hardstand'deki kamyondan sahnenin arkasına KISA yol (≈20–40 m); ilk karede kancada (G9 · G11); yerine oturunca cıvatalanır; kopya yazılmaz ("seven ribs", "two towers").
**Korpus kararı [DERS 55]:** açık hava tiyatrosu + orman korpusu çoğul olabilir (ikinci tribün, antik harabe, stadyum) → NEGATIVE'de her karede: "The hollow holds exactly one theatre, this one, with exactly twelve terraces and exactly three stair aisles."
**Yapı adı kararı [DERS 42]:** "open-air theatre" + "stone seating terraces" + "stage platform" + "acoustic shell" yazılır; "amphitheatre · arena · colosseum · stadium · ruin · ancient" YASAK; su "opaque brown floodwater" (göl/gölet/havuz YASAK); ışık pozitif tarifle ("small warm points with crisp edges").

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
KARAR CÜMLESİ [KAMERA_DILI §0]: İzleyici suyun çekilip tiyatronun ortaya çıkmasını, taşın temizlenip ahşap ve bakırla donatılmasını ve
                 aynı akşam seyirciyle dolmasını görecek. Yarık kaya, iki çam, arka duvar ve on iki teras aynı kalacak. Kamera
                 YÜKSEK EĞİK aileden (h 22 · tilt 27° aşağı · tiyatronun ekseninde) bakacak — yayların eş merkezli olduğu, sahne
                 ve gök ancak böyle aynı karede okunur. Hareket YOK.

ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0,
                 yani en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp [A7-b]; kutu tam 8,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 20 sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.

┌─ KAMERA İSTASYONU (ANA · tek istasyon) ──────────────────────────────────────┐
│ lens          16 mm doğrusal (rectilinear) · f/8 · ISO 100 (akşam 400–1600) ·  │
│               tam kare YATAY (36 × 20,25 mm) → f = 853 px · yatay görüş 96,7° │
│ yükseklik     h = +22,0 m (orkestra zemininden) — dış kenarın üstündeki sırtta │
│               kaya çıkıntısı (12. terasın üstünden +14,8 m)                    │
│ mesafe        D_eksen = 44,0 m (orkestranın merkezine — BÜTÜN px buradan) ·   │
│               D_kenar ≈ 16 m (dış kenarın ortası) · sahne 51,9 m · yarık kaya  │
│               115,4 m [DERS 38]                                                │
│ bakış açısı   bearing 15° (KKD — tiyatronun ekseni boyunca sahneye) · tilt 27° │
│               AŞAĞI · roll 0° · tiyatronun ekseninde (simetrik — SAPMA ④)       │
│ sabitleme     "fixed tripod bolted to a rock outcrop on the ridge above the    │
│               near rim of the theatre"                                         │
│ ⛔ HESAP — iğne deliği izdüşümü (yatay 16:9, f 16 → 853 px):                    │
│    px = 960 + 853·Xc/Zc · üstten = 540 − 853·Yc/Zc (kamera eksenine dönük)    │
│    ufuk üstten 540 − 853·tan 27° = 105 (%90) · ağaç çizgisi (200 m) 105        │
│    `bolum_uretici.py --kadraj` çıktısı:                                       │
│    ⭐ yarık kaya x 286–384 (98 px) · tepe 94 (%91) · dip 201                   │
│    iki çam x 1490–1557 · tepeler 22–33 · dipler 163–173                        │
│    arka duvar x 479–1441 · üstten 344 (%68)                                    │
│    sahne ön kenarı x 719–1201 · 539 (%50) · arka kenar 767–1153 · 451 ·        │
│      merkez 490                                                                │
│    kabuk taban x 785–1135 · 470 · ön dudak 319 · tepe 267 (%75)                │
│    kuleler x 689 / 1231 · dip 500 · tepe 349 (%68)                             │
│    dış kenar (12. teras arkası) φ −60/+60 x 266 / 1654 · 543 (en geniş) ·     │
│      φ ±90 x 395 / 1525 · 414 · φ 0 (orta) 858 (%21)                           │
│    orkestra kenarı (orta) 708 · sol merdiven 775·677 → 383·736 (sol giriş) ·  │
│      orta 960·708 → 858 · sağ giriş 1537·736                                   │
│    hasar (sol merdiven, 4.–6. teras) x 656–708 · 687–695                       │
│    giriş yolları kadraj kenarına x 109 / 1811 · 892 (%17)                      │
│    vinç x 578 · 465 · pompalar x 232 · 344 · tanklar x 178–372 · 309–330 ·     │
│      servis yolu sol kenardan (≈326) → hardstand 587 · 471                     │
│    insan (1,7 m): sahnede 26 px · 6. terasta 41 px · dış kenarda 58 px         │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① ⭐ YARIK KAYA (SOL ÜST · x 286–384 · 94–201) — KANIT NESNESİ, yamaçta, tepeden│
│    dibe koyu bir çatlakla yarılmış açık renkli tek kaya: hiç değişmez         │
│ ② İKİ ÇAM (SAĞ ÜST · x 1490–1557) — ağaç çizgisinin üstüne çıkar, koyu yeşil  │
│ ③ ARKA DUVAR (alçak kuru taş · 344) + sahnenin arkasındaki çimenli şev        │
│ ④ AĞAÇ ÇİZGİSİ %90 (105) · ⑤ servis yolu (sol kenardan hardstand'e) ·         │
│    sonbahar ormanı (altın · turuncu · pas — sabit)                            │
│ + "The hollow holds exactly one theatre, this one, with exactly twelve        │
│   terraces and exactly three stair aisles" — her NEGATIVE'de                   │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ tilt 27° → ufuk %90 · gök bandı üstten 0–105 (ince ama finalde mavi okunur)   │
│ yanlar: solda servis yolu + pompalar + tanklar + kaya + vinç · sağda çamlar   │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ — kanıt nesnesi alt 100 px'e (üstten > 980) ve  │
│ sağ üst 300×100 px'e (x > 1620 · üstten < 100) girmez ✓ (kaya 94–201)          │
│ ⚠️ giriş yolları (S12) alt köşelere uzanır — alt onda bire (üstten > 972)      │
│    yalnız uçları düşer; ilerleme kanıtı yolun girişe yakın kısmında okunur    │
│ ⚠️ 16 mm geniş açı: kenarlarda doğrusal gerilme (dış yaylar yanlarda uzar) —  │
│    kabul edilen bedel; çanağın %72'si (266 → 1654) ve gök aynı karede         │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ merkez O = orkestra zemini (z 0) · +y sahneye · tiyatro ekseni bearing 15°    │
│ teraslar: 12 · ön kenar yarıçapı 16,0 + 1,2·(k−1) · basamak 1,2 m × 0,6 m ·    │
│   12. teras üstü +7,2 · dış kenar 30,4 · yarım daire φ −90…+90                │
│ merdivenler: 3 radyal, φ −30 · 0 · +30 · 1,6 m geniş · teras başına 2 basamak │
│ üst geçit: dış kenarın arkasında 30,4–32,0 · +7,2 · girişler φ ±30            │
│ sahne platformu: taş · x ±13 · y −3…+10 (26 × 13 m) · üstü +1,2 · yeni ahşap   │
│   sahne +1,6 (çelik ızgara + panel, platformun içinde)                         │
│ kabuk: arka üçte bir (y +5,7…+10) · yedi kavisli çelik kaburga · taban ±11 ·  │
│   tepe +13,2 · ön dudak +11 · dış yüz bakır renkli panel · iç yüz açık ahşap ·│
│   iç kenarında armatür sırası                                                  │
│ kuleler: 2 · x ±16 · y +2 · +1,2 → +10,2 (9 m) · koyu çelik kafes ·            │
│   hoparlör + ışık üniteleri                                                    │
│ arka duvar: y +16 · +6,5 tabanlı alçak kuru taş duvar (x ±34) · önünde şev    │
│ servis yolu: sol kenar (+11) → hardstand (x −20…−30, y +2…+14, z 0)           │
│ pompalar: 2 sarı römork pompa (−48, 12, +8) · 3 gri çökeltme tankı yol        │
│   kenarında (−56…−44) · siyah emiş hortumları · deşarj borusu sol kenara      │
│ su: G0 +6,1 · G1 +4,1 · G2 +1,5 · G3 0 (çamur)                                │
│ seyirci kapasitesi: ≈1.600 yer (12 yay − 3 merdiven, 0,5 m/kişi)               │
│ STRUCTURE'ın İngilizce tam hâli tek cümle (DERS 36): "When finished this will │
│   be a restored open-air theatre in a forest hollow: twelve broad concentric  │
│   semicircular stone seating terraces with timber seat boards and three       │
│   radial stone stair aisles around a level orchestra floor, a timber stage on │
│   the original rectangular stone stage platform, a fan-shaped acoustic shell  │
│   over the rear third of the stage, two compact technical towers flanking the │
│   stage, and two paved audience paths." — 21 görselde BİREBİR                 │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 20 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az YAPI göstermez. S0–S2'de su GİDER (yapı zaten oradadır, açığa
> çıkar — "belirmez"); S3–S4 kir gider; S5–S12 yapı KAZANIR; S13'te şantiye gider (yapı aynı); S14–S19 yapıyı KULLANIR. Kış
> görüntüsü YOK (tek sonbahar günü; DERS 7 tetiklenmez).

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | MEVSİM TAŞIYICISI | KANIT NESNESİ (px) |
|:-:|:-:|---|---|:-:|:-:|:-:|---|---|
| 0 | 8,0 | BOŞALTIR | su 11. terasın dibinden → 7.'nin dibine (+6,1 → +4,1) | ½ gün | A | 09:20→09:30 | sonbahar (sabit) · ışık: sabah | su çizgisi orta 814 → 748 |
| 1 | 8,0 | AÇIĞA ÇIKARIR | su → sahnenin hemen üstü (+1,5) · üç merdiven bağlanır · sol hasar görünür | ½ gün | A | 09:30→09:40 | aynı | su 748 → 717 · hasar 656–708 |
| 2 | 8,0 | KURUTUR | son sığ su hortuma · ⭐ dikdörtgen sahne çamurdan çıkar | ½ gün | A | 09:40→09:50 | aynı | sahne ön kenarı 719–1201 · 539 |
| 3 | 8,0 | TEMİZLER | kalın çamur → yükleyici → damperli kamyon (%0 → %100) | 1 hafta | A | 09:50→10:00 | aynı | çamur yığınları sahnede → 0 |
| 4 | 8,0 | YIKAR | basınçlı yıkama, dış kenardan orkestraya (%0 → %100) · ıslak | 2 hafta | B | 10:00→12:00 | aynı · ışık: öğleye | ⭐ açık taş bandı 858 → 708 |
| 5 | 8,0 | ONARIR | sol merdiven + teras uçları taş blokla (%0 → %100) | 2 hafta | A | 12:00→12:10 | aynı | hasar 656–708 kapanır |
| 6 | 8,0 | OTURTUR | ahşap oturma tahtaları 12 terasa, alttan yukarı (%0 → %100) | 3 hafta | B | 12:10→14:10 | aynı · ışık: öğleden sonra | ⭐ 12 kahverengi yay |
| 7 | 8,0 | ÇATAR | çelik döşeme ızgarası sahneye, soldan (%0 → %100) | 1 hafta | A | 14:10→14:20 | aynı | ızgara 719–1201 |
| 8 | 8,0 | KAPLAR | ahşap döşeme panelleri, önden arkaya (%0 → %100) | 1 hafta | A | 14:20→14:30 | aynı | sıcak sahne 719–1201 |
| 9 | 8,0 | DİKER | yedi kavisli çelik kaburga, soldan (%0 → %100) | 1 hafta | A | 14:30→14:40 | aynı | kaburgalar 785–1135 · tepe 267 |
| 10 | 8,0 | KAPLAR | bakır dış panel + ahşap iç modül, aşağıdan (%0 → %100) | 4 hafta | B | 14:40→16:40 | aynı · ışık: alçalan güneş | ⭐ kabuk 785–1135 · 267–470 |
| 11 | 8,0 | KURAR | iki teknik kule (%100) + sönük basamak lambaları | 1 hafta | A | 16:40→16:50 | aynı · ışık: altın saat | kuleler 689 · 1231 · tepe 349 |
| 12 | 8,0 | DÖŞER | iki giriş yolu, kenardan girişe (%0 → %100) + sönük yol lambaları | 2 hafta | A | 16:50→17:00 | aynı | yollar 109 → 383 · 1811 → 1537 |
| 13 | 8,0 | BOŞALTIR | vinç + pompalar + tanklar + paletler çıkar · saha açılır | 2 gün | A | 17:00→17:10 | aynı | vinç 578 · pompalar 232 → 0 |
| 14 | 8,0 | YERLEŞTİRİR | sandalye + sehpa + kutu sahneye · küçük topluluk oturur | 1 sa | A | 17:10→17:20 | aynı · son güneş | topluluk sahnenin ön üçte ikisinde |
| 15 | 8,0 | YAKAR | lambalar gruplar hâlinde: basamak → kabuk → yol · ana ışık sönük | 10 dk | A | 17:20→17:30 | aynı · gün batımı | ⭐ ışık kümeleri |
| 16 | 8,0 | GETİRİR | ilk seyirci: yollar → girişler → merdivenler → alt + orta sıra (≈⅓) | 10 dk | A | 17:30→17:40 | aynı · mavi saat | alt sıralar dolar |
| 17 | 8,0 | DOLDURUR | üst sıralar dolar (çoğu) · koridorlar açık | 10 dk | A | 17:40→17:50 | aynı · mavi saat | çanak dolu |
| 18 | 8,0 | AÇAR | ⭐ ana sahne ışıkları karanlıktan tama (≈3 sn) · müzik başlar | 8 sn | G | 17:50:00→17:50:08 | aynı · derin mavi | ⭐ sahne ön kenarı 719–1201 ışıkta |
| 19 | 8,0 | ALKIŞLATIR | müzik yükselir · alkış (0–4 sn) · TUTUŞ (4–8 sn) | 8 sn | G | 17:50:08→17:50:16 | aynı | ⭐ kaya 286–384 · dolu çanak |

```
IZGARA          8,0 sn × 20 · kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn) · müzik 120 BPM → her kesme ölçü başında
                (8,0 sn = 4 ölçü)
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: sahip senaryosunun biçimi (20 × 8,0, kart yok — hikâye SAPMA ②); emsal THE FIRST LIGHT ·
                       THE SKY CANAL (20 × 8,0). ⚠️ BANDIN DIŞI: format 12 × 10,0.
                   (b) ritim klip İÇİNE: ① rejim nabzı — B'ler S4 · S6 · S10 (yıkama · ahşap · bakır), G'ler S18 · S19 (gerçek
                       zaman, final); ② iş yönü değişir: aşağı (S0–S2 su) · yana (S3 çamur sahneden yola) · yukarıdan aşağı
                       (S4 yıkama) · tek nokta (S5 merdiven) · aşağıdan yukarı (S6 tahtalar) · soldan sağa (S7) · önden arkaya
                       (S8) · yelpaze (S9) · aşağıdan yukarı (S10) · iki yana (S11) · kenarlardan içeri (S12) · dışarı (S13) ·
                       yoldan sahneye (S14) · ışık grupları (S15) · dışarıdan içeri ve aşağı (S16–S17 seyirci) · ışık (S18) ·
                       alkış dalgası öndan arkaya (S19); ③ müzik katmanı = aşama (MUZIK.md)
                   (c) kabul edilen risk: eşit klipte ❷ RHYTHM kategorisi NOT TRIGGERED — sapma kurgudan gelirse (klip ≠ 8,0)
                       ❷ açılır ve ❺ final saniyesi kayar. Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
REJİM SAYISI    ⚠️ ÜÇ rejim (A · B · G) — SANTIYE_HAREKETI §2 sınırı iki. Gerekçe: G yalnız final klipleridir (S18 · S19) ve
                rejim G'nin tanımı tam budur: "yalnız filmin SON sahnelerinde ve yalnız hareket ÖDÜLSE" (sahne ışıklarının
                doğal hızda yükselmesi, alkış, rüzgâr — sahip: "seyircide küçük, doğal hareketler"). A'da (75×) alkış titreşir,
                ışık tek karede patlar. Geçiş KESMEDE (S17 → S18, 144,0) [P5-c]. ⚠️ G depoda ölçülmedi (ONE MORE TURN tanımı) —
                kapı tanır ("eight seconds pass" + "moves at natural speed"). PİLOT ① ölçer.
IŞIK GÜNÜ       Σ pencere = 15 A × 10 dk + 3 B × 2 sa + 2 G × 8 sn = 150 dk + 6 sa + 16 sn = 8 sa 30 dk ≤ 14 ✓
                09:20 (güneş 23,7°) → 17:50:16 (mavi saat, güneş −4,9°)
MAVİ SAAT       güneş −2…−6° penceresi [ISIK_FINALI §1]: S16 (−1,5 → −3,2) · S17 (−3,2 → −4,9) = İKİ A klibi ✓ (sınır iki) ·
                S15 gün batımı geçişi (+0,1 → −1,5) · S18–S19 G (−4,9, 16 sn) — final kareleri −4,9° ✓ (−4…−6)
BÖLÜM SINIRI    G10 — S9 son karesi = S10 ilk karesi; yedi çıplak kaburga sahnenin arkasında, kabuk KAPLANMAMIŞ, ahşap sahne
                tamam, 12 sırada ahşap tahta, vinçte kabuk paneli sandığı, pompalar yolda, gölge +29°, öğleden sonra — ikisinde
                de aynı [DERS 52]
TEK TAHLİYE     S0 + S1 + S2 — aynı pompalar, aynı hortumlar, su yalnız ALÇALIR; her kesme öncekinin su çizgisini devralır
                (8,0 · 16,0)
TEK AKŞAM       S15 + S16 + S17 + S18 + S19 — yanan lamba bir daha sönmez; oturan seyirci yerinde kalır; 144,0'de rejim A → G
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: YARIK KAYA — G0'da ve usta karede (G20) aynı konum (x 286–384) ve aynı boy (98 px en · tepe 94 · dip
        201) [DERS 25]; tepeden dibe koyu çatlaklı tek açık renkli kaya, yamaçta; hiç değişmez. Yedek: iki çam (x 1490–1557 —
        G'de tepeleri hafif sallanır, yeri sabit) + arka duvar (344).
LOOP    G20 ↔ G0: aynı kadraj · aynı kaya · aynı çamlar · aynı on iki yay · ışık FARKLI (bilinçli — G0 sabah, G20 mavi saat; tek
        gün): G0'da kahverengi suyun içinden iki taş yay / G20'de aynı yayların hepsi seyirciyle dolu ve ışıklı. Biçim kafiyesi:
        su çizgisinin yayı (G0) ↔ ön sıradaki seyircinin yayı (G20) aynı merkezli.
SÖKÜM   S0–S2 hortum ucu ekipleri, kamyon (yedek hortum) · S2 sonu kalas yürüme yolları · S3 yükleyiciler + damperli kamyonlar
        (çamur gider) · S4 su tankeri · S5–S12 kamyonlar (taş · tahta · ızgara · panel · kaburga · sandık · kule · döşeme taşı),
        boşalınca gider · S13 VİNÇ (bomunu indirir, servis yolundan çıkar) + İKİ POMPA (römorkla) + ÜÇ TANK (kamyonla) + boş
        paletler + kalaslar · S15 beyaz minibüs gider — ekranda; lambalar + kuleler + yollar KALIR (kalıcı) [DERS 48 · P2-h]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
su (giden)              → hortumlar → pompalar → çökeltme tankları → deşarj borusu (sol kenar)      → G0
çamur (giden)           → küçük paletli yükleyici → tekerlekli yükleyici → damperli kamyon → yol    → G3
silt (giden)            → yıkama mızrakları (tanker) → gri yıkama suyu → orkestra → hortum           → G4
taş bloklar             → kamyonda paletler (hardstand) → vinç → sol merdiven                       → G5
ahşap oturma tahtaları  → kamyonda demetler → vinç → orkestrada istif → ekipler merdivenden taşır    → G6
döşeme ızgarası         → kamyonda modüller → vinç → sahne                                          → G7
döşeme panelleri        → kamyonda paletler → vinç → sahne                                          → G8
kavisli kaburgalar      → uzun kamyon → vinç → sahnenin arkasındaki taban plakaları                  → G9
kabuk panelleri         → kamyonda sandıklar → vinç → makaslı platformlar → kaburgalar              → G10
kuleler + üniteler      → kamyonda çerçeve + sandıklar → vinç → sahnenin iki yanı                   → G11
basamak lambaları       → (ekip, el) → üç merdivenin kenarı                                         → G11 (S11 içinde)
döşeme taşları          → küçük damperler → yol kenarında paletler → ekipler                        → G12
sandalye/sehpa/kutular  → beyaz minibüs (hardstand) → yan rampa → sahne · el arabası                → G14
seyirci                 → iki taş yol (kadraj kenarından) → girişler → üç merdiven → sıralar         → G16
GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL (prompta yalnız vekil girer):
   suyun arıtılması → gri tanklar + sol kenara giden boru · harç kuruması → yeni blokların açık derzleri (S5–S6) · elektrik
   tesisatı → ekiplerin kulelere ve lambalara döşediği kablolar (S11 · S14) · ses kontrolü → sahnenin solundaki şalter panosu (S15)
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① ışıktaki sahne + küçük topluluk + bakır kabuk (x 719–1201 · üstten 267–539, ilk okunan, en parlak) → ② dolu sıralar (on iki yay,
   sırtı kameraya küçük figürler) + yanık basamak lambaları + üç açık koridor → ③ iki koyu kule (689 · 1231) + iki ışıklı yol → ④
   arka duvar + mavi saatte sonbahar ormanı + gök bandı → ⑤ yarık kaya (kanıt) + iki çam
FİNAL KARE KANITI  ffmpeg -ss 159.0 -i teslim.mp4 -frames:v 1 kanit.jpg   (S19 tutuşu 156,0–160,0 içinde · mavi saat, okunur
                   [DERS 45]) · kart YOK → son kare = G20
```

---

## 🖼️ KARE TABLOSU — 21 görsel [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Gölge yönü kadrajda: 0 = kameradan uzağa · − sola · + sağa (|x| > 90 = kameraya doğru). Güneş DİSKİ anılmaz.
> Sayılar `bolum_uretici.py --tablo` çıktısıdır (47° K · δ −9° · güneş saati · kamera bakışı 15°). G16+ güneş ufkun altında → gölge yok.

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| G0 | 09:20 | 136° | 23,7° | −59° | açık, ince yüksek bulut | sonbahar (sabit) | ⭐ AÇILIŞ — su 11. terasın dibinde · iki üst yay dışarıda · pompalar çalışıyor |
| G1 | 09:30 | 139° | 24,8° | −56° | aynı | aynı | su 7. terasın dibinde · altı yay dışarıda |
| G2 | 09:40 | 141° | 25,9° | −54° | aynı | aynı | ⭐ on iki yay + üç merdiven · sol hasar · sahne ince su altında |
| G3 | 09:50 | 143° | 27,0° | −52° | küçük bulutlar | aynı | su YOK · kalın çamur · kalas yolları · yükleyiciler, damperliler |
| G4 | 10:00 | 146° | 28,0° | −49° | aynı | aynı | çamur gitti · taş silt filmli, donuk · tanker + yıkama ekipleri dış kenarda |
| G5 | 12:00 | 180° | 34,0° | −15° | aynı | aynı | ⭐ taş temiz, ISLAK · vinç geldi (taş blok paleti) · sol hasar duruyor |
| G6 | 12:10 | 183° | 34,0° | −12° | aynı | aynı | merdiven tam · taş kuruyor (lekeli) · vinçte tahta demeti |
| G7 | 14:10 | 217° | 27,0° | +22° | aynı | aynı | ⭐ 12 sırada ahşap tahta · taş kuru · vinçte ızgara modülü |
| G8 | 14:20 | 219° | 25,9° | +24° | aynı | aynı | sahnede çelik ızgara · vinçte panel paleti |
| G9 | 14:30 | 221° | 24,8° | +26° | aynı | aynı | ahşap sahne tamam · vinçte kaburga · taban plakaları |
| G10 | 14:40 | 224° | 23,7° | +29° | aynı | aynı | ⭐ BÖLÜM SINIRI — yedi çıplak kaburga · vinçte panel sandığı |
| G11 | 16:40 | 249° | 6,7° | +54° | alçalan sıcak ışık | aynı | ⭐ kabuk tamam (bakır + ahşap) · vinçte kule çerçevesi |
| G12 | 16:50 | 251° | 5,1° | +56° | altın saat | aynı | iki kule · sönük basamak lambaları · vinç bomu dik (dışarıda) · toprak yollar |
| G13 | 17:00 | 253° | 3,4° | +58° | aynı | aynı | taş yollar + sönük yol lambaları · vinçte boş palet demeti · pompalar duruyor |
| G14 | 17:10 | 255° | 1,8° | +60° | son güneş | aynı | ⭐ saha boş — vinç, pompa, tank YOK · beyaz minibüs · sıralar boş |
| G15 | 17:20 | 257° | 0,1° | +62° | gün batımı | aynı | topluluk sahnede · bütün lambalar SÖNÜK · şalter panosu |
| G16 | 17:30 | 258° | −1,5° | — | alacakaranlık | aynı | ⭐ basamak + kabuk + yol lambaları YANIK · ana ışık sönük · sıralar boş |
| G17 | 17:40 | 260° | −3,2° | — | mavi saat | aynı | sıraların ≈⅓'ü dolu (alt + orta) · yollarda akış |
| G18 | 17:50:00 | 262° | −4,9° | — | derin mavi | aynı | sıraların çoğu dolu · koridorlar açık · ana ışık SÖNÜK |
| G19 | 17:50:08 | 262° | −4,9° | — | aynı | aynı | ana ışık TAM · topluluk çalıyor |
| G20 | 17:50:16 | 262° | −4,9° | — | ⭐ derin mavi, okunur | aynı | ⭐ USTA KARE — alkış · ön sıralarda birkaç kişi ayakta |

```
SU KOTU DEFTERİ [SU_VE_YANSIMA §8 · P10-e]   (kot terasların ön kenarına göre · teras basamağı 0,6 m · su yalnız ALÇALIR)
   G0     +6,1 · 11. terasın dibi (orta üstten 814 · yanlar 433 · x 445–1475) · 10. terasın kenarı suyun hemen altında · çekiliyor
   G1     +4,1 · 7. terasın dibi (orta 748 · yanlar 467 · x 542–1378) · altı teras dışarıda · çekiliyor
   G2     +1,5 · 3. terasın dibi, sahne platformunun 0,3 m üstü (orta 717 · yanlar 510) · ince su tabakası · çekiliyor
   G3     yok — orkestra ve sahne kalın koyu ıslak çamur; su GERİ GELMEZ
   G4–G6  yıkama suyu (gri, akan) yalnız S4 içinde; G5 ıslak taş, G6 lekeli kuruyor; durgun su YOK [DERS 54]
   ⛔ kaynak yok, çıkış tek (pompalar → tanklar → sol kenar); yön tek (aşağı); yükselme YOK ("never rising")
   TANIK ÇİZGİ — çekilen su teraslarda koyu, siltli, ıslak taş bırakır (G1–G3); S4 yıkaması onu sildiğinde temiz taş bir daha
   kirlenmez
ISLAKLIK DEFTERİ   G0–G3 silt-koyu ıslak · G4 donuk kuru silt filmi · G5 ⭐ temiz, ıslak, koyu (yıkandı) · G6 kuruyor, alt sıralarda
                   lekeler · G7+ kuru, açık taş
VİNÇ DEFTERİ [DERS 8 · 46]   (YÜK = kancada görünür yük · DIŞ = bom ucu + halat kadrajın üstünde)
   G0–G4   vinç YOK (S4 sonunda servis yolundan gelir, destek ayaklarını açar, taş paletini kaldırır)
   G5  YÜK taş blok paleti          G9   YÜK kavisli çelik kaburga         G13  YÜK boş palet demeti
   G6  YÜK tahta demeti             G10  YÜK kabuk paneli sandığı        G14+ vinç YOK
   G7  YÜK ızgara modülü            G11  YÜK kule çerçevesi
   G8  YÜK panel paleti             G12  DIŞ (bom dik — yük yok)
   ⚠️ YÜK → DIŞ: S11 sonu (kuleyi bırakır, bomu dikleştirir) · DIŞ → YÜK: S12 sonu (bom iner, ekip palet demetini bağlar) ·
      S13'te bom katlanırken kanca boş — THE FIRST LIGHT S15 · THE SKY CANAL S12 emsali, beyanlı
IŞIK DEFTERİ [ISIK_FINALI §4]
   armatür / grup            takıldığı klip   sönük kareler   grup   yanma · saniye (film)                    renk           yansıma
   basamak lambaları (3 merdiven) S11        G12–G15         1      S15 ≈ 121 sn (ilk grup, TEK KAREDE)      sıcak          —
   kabuk iç armatürleri       S10              G11–G15         2      S15 ≈ 123 sn                             sıcak          —
   yol lambaları (2 yol)      S12              G13–G15         3      S15 ≈ 125 sn                             sıcak          —
   ana sahne ışıkları (kuleler) S11            G12–G18         4      S18 144,0 → ≈147,0 sn (G, karanlıktan    sıcak beyaz    —
                                                                     tama ≈3 sn yükselir — gerçek zaman)
   ⛔ A'da "fades in · gradually · slowly lights up" YAZILMAZ; her grup bir anda · negatifte ışık etkisinin adı YOK
SEYİRCİ DEFTERİ [P24-e · P25-c]
   G0–G15  sıralar BOŞ (G15'te topluluk sahnede, ≈12 küçük figür)
   G16     sıralar boş · girişlerde ikişer görevli · lambalar yanık
   G17     ≈⅓ dolu: alt ve orta sıralar · yollarda akış · üst sıralar boş
   G18     sıraların çoğu dolu · üç koridor açık · oturan herkes G17'deki yerinde
   G19–G20 aynı · G20'de ön sıralarda birkaç kişi ayakta alkışlıyor
   ⛔ kimse koltukta "belirmez" — her kişi yoldan, girişten, merdivenden yürür; tek karede bütün sıralar dolmaz (sahip)
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G20 usta kare → G19 (alkış yok) → G18 (ana ışık sönük) → G17 (seyirci ⅓) → G16 (sıralar boş) → G15 (lambalar sönük) → G14
   (topluluk yok) → G13 (vinç, pompa, tank geri gelir) → G12 (yollar toprak) → G11 (kuleler yok, lambalar yok) → G10 (kabuk
   kaplanmamış) → G9 (kaburga yok) → G8 (ahşap sahne yok — ızgara) → G7 (ızgara yok) → G6 (ahşap tahta yok) → G5 (merdiven
   kırık, taş ıslak) → G4 (taş kirli, vinç yok) → G3 (çamur) → G2 (ince su) → G1 (su 7. teras) → G0 (su 11. teras)
   ⚠️ ters inşada SU YÜKSELİR (G3 → G0): yapı su altında da AYNI geometride; bir teras ya görünür ya suyun altındadır — "eriyen"
      basamak yok, px elle (su çizgisi defterden)
   ⚠️ ters inşada SEYİRCİ GİDER (G18 → G16): oturanlar yer değiştirmeden azalır; boş sıra çizilirken tahtalar ve lambalar aynı
   sonra I2V S0 (G0→G1) … S19 (G19→G20) — her klip iki uca kilitli, üretim 9,0 sn, baştan 1,0 kırp
```

## 🧪 PİLOT ÜÇLÜ [DERS 62 · KILAVUZ_REHBERI §8 adım 2b]

```
⛔ Üretim başlamadan, aşağıdaki üçü geçmeden kalan klipler üretilmez:
① FİNAL      G20 + G19 + G18 + S18 + S19 — rejim G (gerçek zaman) burada ilk kez ölçülür: ana ışık ≈3 sn'de yükseliyor mu,
             seyirci sabit oturuyor mu (sırtı kameraya, yüz yok), alkış küçük hareket mi, kimse belirip kaybolmuyor mu;
             S19 son 4 sn TUTUŞ (yapı kıpırdamaz, yalnız alkış ve ağaç tepeleri) [C1-b]; gök MAVİ ve okunur (−4,9°)
② EN BÜYÜK   G0 + G1 + S0 — ⭐ açılış ve en büyük değişiklik: su TEK YÖNDE alçalır, yeni yaylar sudan "çıkar" ama "belirmez"
   DEĞİŞİKLİK  (yapı baştan suyun altındadır — sahip: "suyun yüzeyinin taşa dönüşmesi" yasak), aynı merkez, aynı basamak
             boyu; su yükselmez, kaynamaz [DERS 54 · su kılavuzu §6] · 0. saniyede hareket var mı
③ AKŞAM      G15 + G16 + S15 — üç ışık grubu sırayla, her biri TEK KAREDE yanıyor mu; kabuk ve basamaklar sıcak, gök soluk
             maviye dönüyor; hiçbir ışık etkisi (hale, huzme) çizilmiyor [ISIK_FINALI §5]
PİLOT SONRASI İLK  S1 · S2 (tahliyenin devamı, sahnenin çamurdan çıkışı) + S10 (bakır kabuk — B rejiminde en gösterişli değişim) +
                   S16 (ilk seyirci akışı)
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     47,0° K · ışık günü tarihi: δ −9° (ekim ortası) · doğuş ≈06:34 · batış (−0,833°) ≈17:26 (güneş saati) · kamera
                bakışı 15° (KKD) → kadraj −33° … +63° azimut · güneş 136° → 262°: sabah kameranın SAĞINDA ve arkasında (bağıl
                +121°), öğle tam arkada, öğleden sonra arkada solda (bağıl −126°) — HİÇBİR karede kadrajda değil, ters ışık YOK [P8-h]
TİYATRO IŞIĞI   sahne ve kabuk kameraya (GGB) bakar → sabah yandan (sağdan, gölgeler öne-sola), öğle arkadan (gölgeler uzağa),
                öğleden sonra arkadan-soldan sıcak; altın saatte (G11–G14) bakır kabuk, sahne ve ağaç tepeleri sıcak ışıkta,
                çanağın dibi gölgede; G16+ güneş ufkun altında, ışık düz ve yumuşak, lambalar en parlak
GÖLGE SÜPÜRMESİ rejim B klipte: S4 (−49° → −15°: 34°) · S6 (−12° → +22°: 34°) · S10 (+29° → +54°: 25°, uzar) · rejim A klipte fark
                edilmez → yüzeyle kanıtlanır · G klipte (8 sn) yok
MAVİ SAAT       −0,833° 17:26 · −2° 17:33 · −4° 17:45 · −6° 17:57 (bu makinede hesaplandı, ISIK_FINALI §1 formülü) · final 17:50
                (−4,9°) — pencerenin içinde; gök mavi, yapı ve ağaçlar okunur, siyah siluet DEĞİL [DERS 45]
MEVSİM          tek sonbahar günü — ağaçlar altın, turuncu, pas (SITE bloğunda sabit); iki çam koyu yeşil · taşıyıcı IŞIKTIR (sabah →
                öğle → altın saat → mavi saat), takvim değil (ÜSLUP BEYANI) · ⚠️ DERS 14'ün "mevsim taşıyıcısı" sütunu burada
                ışık evresini taşır
KIŞ / GECE      görüntü YOK · DERS 7 tetiklenmez · final mavi saat (gece değil)
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   ANA h +22,0 (orkestradan) · D_eksen 44,0 · D_kenar ≈16 · bakış 15° · tilt 27° aşağı · roll 0 · 16 mm · eksen üstünde
YAPI     12 teras (16,0 → 30,4 · +0,6/basamak · +7,2) · 3 merdiven φ −30/0/+30 · sahne 26 × 13 (+1,2) · kabuk tepe 267 · kuleler
         689 / 1231 · tepe 349 · arka duvar 344 · dış kenar en geniş 266 → 1654 · orta 858
SU       +6,1 (G0) · +4,1 (G1) · +1,5 (G2) · yok (G3+) — yalnız alçalır
SEYİRCİ  G0–G16 boş · G17 ≈⅓ · G18–G20 çoğu dolu · koridorlar açık
IŞIK     G0–G15 lambalar sönük · G16+ basamak + kabuk + yol yanık · ana ışık G19+
ÇAPALAR  ① YARIK KAYA x 286–384 · 94–201 (kanıt nesnesi 98 px) · ② iki çam 1490–1557 · ③ arka duvar 344 · ④ ufuk 105 · ⑤ servis yolu
IZGARA   20 × 8,0 · kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn) · kart YOK · 160,0 sn · 120 BPM
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_SUNKEN_STAGE   → sonuç QA_SPEC §8'de (12.10.2026)
✅ FIX'ler ve beyanları (hepsi elle okundu):
   · ARAÇ KUTU SETİ ölçülmedi — beyanlı; üretim araç kapısıyla açılır
   · süreler eşit (8,0) — düz ızgara (sahip senaryosu, SAPMA ②); beş mercekte ❷ RHYTHM eşit klipte tetiklenmez
✅ YASAK KELİME taraması 0 · kelime kilitleri (floodwater G0–G2 · crane S4 I2V–G13 · copper S10+ · towers S11+ · lamba yanık
   S15+ · audience S16+ · applause S19+) betikle doğrulandı (12.10.2026 · 41 blok)
✅ 00_ANALIZ yedi dosya · hikâye onayı 12.10.2026 (TUR 1 · SAPMA ①–⑯ sahip okur)
⛔ ARAÇ KAPISI koşulmadı → THE_SUNKEN_STAGE_URETIM_GUNLUGU.md §0 (⑩ rejim G ölçümü eklendi)
⛔ PİLOT ÜÇLÜ koşulmadı → S18 + S19 · S0 · S15
⛔ SÜRE / KLASÖR — 160 sn yatay_2_dk bandının dışında (SAPMA ②) → sahip kararı
```
