# 🚃 THE_LAST_CARRIAGE — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **20 × 8,0 sn = 160,0 sn** | Kapak kartı: **⛔ YOK** | Toplam: **160,0 sn**
Prompt yapısı: ⭐ **20 sahne → 21 görsel (G0…G20; G14 iç istasyon) + 20 I2V + 1 iç son kare (G14′) · T2V YOK** [`KILAVUZ_REHBERI` §2.7 · `ISTASYON_VE_IC_MEKAN` §2] · bölüm sınırı karesi **G10**
Yapı: **dar, derin bir kanyonu iki kaya rafı arasında aşan hazır koyu çelik tabliye (iki derin kiriş · her yanda dar yürüme yolu · ön kirişte teras dirsekleri) · üstüne indirilen tek eski yolcu vagonu (≈24 m · yuvarlak çatı · her uzun yüzde sekiz geniş pencere · iki uç giriş bölümü · tekerleksiz çelik alt şasi) · sonradan: pas temizliği, zümrüt yeşili boya + krem şerit, bakır renkli çatı, sekiz yeni cam, iki kısa çelik geçit, 15 × 6 m teras (çelik çerçeve · ahşap yan bölümler · ortada üç büyük cam döşeme paneli · şeffaf korkuluk), içeride ahşap masalar + deri banklar** (en yakın kart `YAPI_TIPI_KARTLARI` ⚠️ birebir yok — burada inşa değil YERLEŞTİRME + RESTORASYON + EKLENTİ; sıra 00_ANALIZ/02 §2a'da bu film için yazıldı) · Saha: **gri-kahverengi kayalık dar kanyon, iki kaya rafı, 47° K, ekim** (`SAHA_VE_IKLIM_KARTLARI` dağ satırı ⚠️ birebir yok; 02 §2b)
Zaman yayı: **gerçekte ≈3–5 ay (bir sabah kaldırma → aylarca restorasyon ve teras → açılış akşamı) → 160 saniye** · film mertebe anlatır: *"bir sabah vagon iner, bir mevsim boya, bakır ve cam, bir akşam ilk konuklar"* [P1-c] · ÜSLUP BEYANI (sahip senaryosu): bütün iş tek bir kısa ekim gününün ışığına sıkıştırıldı — "tek günde yapıldı" iddiası DEĞİLDİR, ekranda süre vaadi yok
Işık günü: **09:30 → 17:50 (mavi saat, güneş −4,9°) · Σ rejim penceresi 8 sa 20 dk ≤ 14** — kesmede ışık atlamaz [§2.7 ①]
Kamera mimarisi: **MAIN STATION** — 19 klip + usta kare, **%95** · **CARRIAGE STATION** (iç) — 1 klip (S14 · 112,0–120,0), %5 · §İKİNCİ İSTASYON BEYANI
Izgara: ⛔ **DÜZ — 20 × 8,0** · ⚠️ BANDIN DIŞI (format 12 × 10,0 · 2:00) — sahip senaryosunun biçimi, toplam 2:40 (hikâye SAPMA ②) · §DÜZ IZGARA BEYANI
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 12.10.2026 (TUR 1 · ajan önerisi + "hazırla aynı şekilde bol iş bol işçi" · 20 satır · SAPMA ①–⑱)
Havuz kaydı: `apexait/YAYIN_PLANI.md` — ⬜ satır açılmadı (sahip kararı) · siluet ailesi: **boşluk üstünde tek nesne + cam + ışık finali** (THE SLOW TAKEOFF tek büyük taşıt gövdesi + iç kamera akrabası; THE GLASS CROSSING cam yürüme yüzeyi akrabası)

_"İlk karede paslı bir yolcu vagonu, vinçte, derin bir kanyonun üstündeki çelik tabliyenin bir metre yukarısında asılı; son karede aynı vagon, mavi akşamda zümrüt yeşili ve ışıklı bir restoran, önündeki cam zeminin üstünde duran bir çift ve altlarında aynı uçurum."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     20 sahne × 8,0 sn                       = 160,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     ⛔ YOK — tam 160,0 sn (sahip senaryosu: "Ek logo, afiş veya kapanış kartı yok") · ihrac_kontrol.sh --kart YOK
──────────────────────────────────────────────────────────────
TOPLAM                                                     160,0 sn
HIZ             1x (yatay hat 2x'e çevrilmez — 2x yalnız dikey paylaşım kuralıdır [DERS 58])
MÜZİK           ✅ VAR — sahip senaryosu "Işık ve ses": konuşmasız, az ve görünür eyleme bağlı efektler + özgün ya da lisanslı
               sinematik müzik; S5–S10 kademeli büyür, S11 cam yerleşiminde kısa süre hafifler, S15'te motorlar uzaklaşır ve
               rüzgâr döner, S16–S19 restoranın iç uğultusu + ana tema · 120 BPM (8,0 sn = 4 ölçü) · THE_LAST_CARRIAGE_MUZIK.md
YAZI            ⛔ YOK (tercih edilen sürüm) · yedek: S0'da tek kısa cümle "DINNER ABOVE THE DROP." kurguda, vagonu ve boşluğu
               örtmeden — görüntü modeline YAZDIRILMAZ
YASAK KELİME    train · locomotive · tram · track · wheel · bogie · sleeper · platform · bridge · footbridge · fireworks · confetti · laser · neon · drone · fog · smoke · haze · mist · glow · bloom · rays · beam · flare · mirror · hole · signboard · menu · waterfall · river · collapse · collapsing · crash · cable car · double-decker
               ⭐ [DERS 59 · 55 · 42] hiçbir promptta, negatifte bile — "train · locomotive · tram · track · wheel · bogie ·
                  sleeper" ray, lokomotif ve tekerlek korpusunu çağırır (sahip: "ilk kareden son kareye kadar vagonun altında
                  tekerlek görünmez"); "platform" istasyon peronu, "bridge · footbridge" kanyonu aşan büyük köprü çizdirir
                  (taşıyıcı "steel support deck", bağlantı "gangway"); "fog · smoke · haze · mist" sahip: "kanyon sisi
                  bağlantıları örtmez"; "fireworks · confetti · laser · neon · glow · bloom · rays · beam · flare" ışık
                  kılavuzunun pozitif-tarif kuralı [ISIK_FINALI §5] + sahip "no fireworks"; "mirror · hole" sahip: "ayna gibi
                  opak cam … yüzeysiz bir delik üretilmez"; "signboard · menu" okunur yazı riski; "waterfall · river" kanyona
                  su koyar; "collapse · collapsing · crash" sahip: "vagon düşmez, kaya çatlamaz"; "drone" kamera hareketi;
                  "cable car · double-decker" vagonu teleferiğe ya da iki katlıya çevirir
KELİME KİLİDİ   "rust" yalnız G0–G3 + S0–S3 I2V · "emerald" S4 I2V + G5'ten · "copper" S4 I2V sonundan (palet) + G5'ten ·
               "crane" G0–G15 + S0–S15 I2V [P7-e] · "gangway" S6 I2V sonundan + G7'den · "terrace frame" S8 I2V sonundan + G9'dan ·
               "glass floor" S10 I2V sonundan + G11'den · ışık YANIK ("light fills · lamps are lit · lit windows") S16 I2V +
               G17'den · "guests" S17 I2V + G17 ACTIVITY'den (G17 AT THIS STAGE'de konuk yok) · "couple" S18 I2V + G19'dan ·
               STRUCTURE'da renk, ışık, insan yok (yalnız yapı) [DERS 36] · tarama betiği 42 blokta 0 ihlal (12.10.2026)
BÖLÜM DOSYASI   BOLUM_1 = S0–S9 (0–80,0)  ·  BOLUM_2 = S10–S19 + İÇ SON KARE G14′ + USTA KARE (80,0–160,0) · ceil(20/2)=10
QA BİRİMİ       FİLM (tek master × 5 mercek · ❶ ❷ ❸ kör · ❹ ❺ belgeli) — QA/HAM/THE_LAST_CARRIAGE/
```

⛔ Kart olmadığı için platform son ekranı **son 5 saniyeye konmaz** ya da yalnız gök bandına (üstten 0–168 px, sırt çizgisinin üstü) konur — vagonun (x ≈503–1586 · üstten 456–770), terasın ve cam bölümün (x ≈679–922 · üstten 708–843) üstüne yerleştirilmez.
⚠️ Son sahnenin (S19) ikinci yarısı TUTUŞTUR (final kanıtı 156,0–160,0, `QA_SPEC` §1): çift camın üstünde durur, içerideki ve terastaki konuklar küçük hareketler yapar, çam dalları hafif sallanır; yapıda hiçbir şey değişmez. Son kare donmaz (sahip: "Afiş, dondurulmuş kare veya kapanış kartı eklenmez").
⭐ Platform küçük resmi (kapak) G20'den gelir (sahip kararı 19.09.2026 + sahip senaryosu "Son karedeki ışıklı vagon, cam terastaki çift ve aşağıdaki boşluk" — öncesi/sonrası bölme yok).

### ⭐ İZLEYİCİ KAPISI [C2-a…d · KILAVUZ_REHBERI §6]

```
İŞLEV ANI         S16 ışıklar gruplar hâlinde yanar → S17 konuklar servis yolundan ve sol geçitten gelir, pencerelerde siluetler →
                  S18 gerçek zamanda konuklar terasa çıkıp oturur → S19 çift camın üstüne yürür, altında kanyon. Restoran yalnız
                  bitmez, KULLANILIR.
AÇILIŞ NESNESİ    G0: vinçte, kısa gergin sapanlarda asılı paslı vagon (x ≈503–1586), tabliyenin 1 m üstünde; altında koyu uçurum;
                  sol avluda büyük sarı vinç · ona ne oluyor: İLK KAREDE iniyor. 120 px'te okunan: kahverengi uzun bir kutu, iki
                  gri kaya arasında, solda sarı bir vinç, altında karanlık bir boşluk.
DİRENÇ EKRANDA    ① boşluk — vagon havada (S0), oturur, halatlar çözülür (S1) ② pas — kırık camlar (S2 sökülür), kahverengi gövde
                  (S3 çıplak gri) ③ erişimsizlik ve boş ön — geçitler S7–S8, teras iskeleti S9, ortası açık S10 ④ boş restoran —
                  G0–G16 hiç konuk yok
DÖNGÜ KAFİYESİ    G20 ↔ G0 aynı kadraj, aynı yarık kaya (x 1649–1806), aynı çatallı çam, aynı sırtlar: G0'da paslı vagon kancada,
                  boşluğun üstünde; G20'de aynı vagon tabliyede, ışıklı, önündeki camın üstünde bir çift — boşluk aynı, üstünde
                  hayat var. Işık FARKLI, bilinçli: sabah ↔ mavi saat.
MERAK SORUSU      Bu vagonu neden buraya koyuyorlar?
İKİNCİ SORU       Önündeki boş çerçeve neye dönüşecek? (S9–S10 açık iskelet ve ortadaki dikdörtgen → S11 üç cam panel)
AÇILIŞ DÜZENİ     ① NESNE asılı vagon · ② DOKUNUŞ "From the first frame the carriage is already sinking slowly and level" ·
                  ③ İPUCU hazır tabliye + önündeki dirsekler — vagonun bir şeye dönüşeceği belli, ne olduğu (restoran) değil ·
                  ④ ÖLÇEK halat tutan ekipler (geçitte insan ≈66 px) + vinç + kamyon · AÇILIŞ GERİ ÇEKİLMESİ ⛔ YOK (sabit)
ÜÇ TERCİH (sahip) keşif gecikmez (ilk 8 sn'de vagon oturur) · dönüşüm uzaktan okunur (pas kahverengi → gri → zümrüt + krem → bakır
                  → cam → teras → ışık ve insan) · final verilen sözü tutar (yapı kullanılır, son kare donmaz) — sahibin kurgu
                  tercihi, ölçülmüş bir formül değil
BOL İŞ (sahip)    "bol iş bol işçi": S0–S15'in her klibinde en az iki ekip + bir makine/araç + görünür malzeme akışı (cıvata
                  sandığı · boş kasa · eski cam · koltuk iskeleti · kum torbası · boya varili · bakır levha paleti · cam sehpası ·
                  geçit · çakıl torbası · taş basamak · teras çerçevesi · döşeme paleti · cam panel · korkuluk sandığı · masa ·
                  bank · palet); ekip cümlesi "Dozens of workers … move fast in crews" (A) / "show only as faint soft motion
                  streaks" (B); S16–S19'da garson ekibi + el arabası
```

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Paslı eski bir yolcu vagonu kanyonun üstündeki çelik tabliyeye indirilir, yenilenir, önüne cam tabanlı bir teras
         kurulur ve aynı akşam restoran olarak açılır.
DİRENÇ   ① boşluk (vagon havada; yalnız tabliyeye oturup cıvatalanınca güvende)  ② pas ve harap gövde (kırık camlar, pas, eski
         boya)  ③ erişim ve teras yok (vagon kayalardan kopuk, önü boş)  ④ boş restoran (konuk ancak her şey bitince gelir)
         EKRANDA NASIL [P1-b]:  S0 · son metreyi inen vagon  ·  S2 · boşalan sekiz açıklık  ·  S3 · soldan sağa ilerleyen gri
                                çelik bandı  ·  S4 · yeşilin ilerlemesi  ·  S5 · bakırın ilerlemesi  ·  S7–S8 · inen geçitler ·
                                S9–S11 · açık iskelet → ahşap → cam  ·  S16–S19 · yanan ışıklar ve gelen konuklar
BEDEL    ⭐ pas + şantiye: G0'da paslı vagon, vinç, kamyon, halat ekipleri; camlar S2'de, pas S3'te, vinç + telehandler +
         kamyonlar + kasalar + atık konteyneri S15'te gider. G20'de aynı yerde ışıklı bir restoran. Okuma bilinçli: "vagon
         kondu" değil, "son vagon kendi yolculuğunu bitirdi".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            pas + kırık camlar + boşluk + vinç, kamyon, kasalar                                        ✅
  □ kadrajda görünüyor mu?    vagon 503–1586 · vinç x ≈372 · cam bölüm 679–922 · yarık kaya 1649–1806                   ✅
  □ cevap "zaman geçiyor" mu? hayır — "vagon indi, temizlendi, boyandı, cam teras kuruldu, konuklar geldi"                ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: vagon havada mı tabliyede mi · halatlar bağlı mı · camlar eski mi, boş mu, yeni mi · gövde
                           pas mı gri mi yeşil mi · krem şerit var mı · çatı gri mi bakır mı · kaç geçit · teras iskelet mi, ahşap
                           mı, ortası açık mı camlı mı · korkuluk var mı · masa sayısı · vinç var mı · lambalar yanık mı · kaç konuk
② KİNETİK BAĞIMSIZLIK   ✅ her klipte ekip + makine ya da konuk hareket eder; kum, boya, levha, cam, ışık, insan akışı görünür
③ BAŞLIK ŞEMASI         ✅ kapak "THE LAST CARRIAGE" (3 kelime) · ⚠️ yayın başlığı sahibinin 43 karakteri (sınır 40 — SAPMA ⑯,
                           YAYIN_PAKETI'nde 39 karakterlik yedek)
④ OMURGA CÜMLESİ [P1-k] ✅ indirir → çözer → söker → sıyırır → boyar → kaplar → camlar → bağlar → bağlar → çatar → döşer → camlar →
                           çevirir → döşer → donatır → boşaltır → yakar → getirir → canlandırır → TAMAMLAR
```

⚠️ **Aile benzerliği [P16-a]:** THE SLOW TAKEOFF ile "tek büyük taşıt gövdesi yeni bir işe döner + iç kamera" akrabalığı; AYIRICI
FARK: orada uçak yerde yükseltilir, burada vagon uçurumun ÜSTÜNE konur ve final bir cam zemindir. THE GLASS CROSSING ile cam
yürüme yüzeyi ortak. Ardışık yayınlanmamalı (YAYIN_PLANI §3 — sahip kararı).

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera (ana istasyon %95 · iç istasyon yalnız S14)
                          ② kanıt nesnesi: YARIK KAYA (x 1649–1806 · üstten 405–673 · 157 px · 20 ana karede birebir; iç karede
                             uzak sol pencereden)
                          ③ çapa: TEK vagon, SEKİZ pencere, İKİ vestibül (sayı ve yer sabit) · vagon x 503–1586 · çatı 456 → 554 ·
                             alt şasi 621 → 770 · ④ çatallı çam x ≈260 · uzak sırtlar üstten 168 (%84)
                          ⑤ yalnız KAZANIR: vagon iner → çözülür → cam sökülür (eksilme değil, yenilenecek) → pas gider → yeşil →
                             bakır → cam → geçitler → iskelet → ahşap → cam taban → korkuluk → masa → ışık → konuk
                          ⑥ VAGON KİLİDİ — S0 sonunda oturur; bir daha kalkmaz, sallanmaz, kaymaz (S1'den itibaren LOCK cümlesi)
                          ⑦ KONUK DEFTERİ (aşağıda) — oturan yerinde kalır; kimse koltukta "belirmez"
                          ⑧ insan: A/B'de iz ("soft motion streaks") · G'de küçük figür, yandan/arkadan · yüz okunmaz
                          ⑨ vinç kancası: ya YÜKLÜ ya bom ucu kadraj dışında — boş kanca yok (VİNÇ DEFTERİ)
                          ⑩ IŞIK DEFTERİ — lambalar önce SÖNÜK takılır, A'da grup grup TEK KAREDE yanar
                          ⑪ CAM — kenar çerçevesi + gök yansıması; ayna gibi opak cam ya da yüzeysiz açıklık YOK
P1.5 · fırsat buldukça   gölge süpürmesi (B: S3 · S4 · S10) · yeşilin alçak güneşte koyulaşması (S10 sonu) · bakır çatının altın
                          saatte ısınması (S11–S13) · gökyüzünün maviye koyulaşması (S16–S17)
SPEC · yalnız belge      azimut/yükseklik dereceleri (kapı şartı) · px tabloları
```

**Malzeme kimliği (her promptta):** *pas kahverengi → çıplak donuk gri çelik → koyu zümrüt yeşili saten boya + krem şerit · bakır renkli çatı levhaları · koyu çelik tabliye, geçit ve teras çerçevesi · açık sıcak ahşap döşeme · üç büyük şeffaf cam panel (ince çelik çerçeve) · ince koyu dikmeli şeffaf korkuluk · gri-kahverengi kanyon kayası · çatallı çam · sarı vinç · turuncu iş kıyafetli ekipler* — korpus: "documentary site photograph on colour negative film" [DERS 34 · 42].
**İnsan kararı (sahip: "bol iş bol işçi" · senaryo: "insanlar az sayıda, uzaktan görülen yetişkin figürlerdir"):** ekip her iş klibinde çok — A'da "small figures with soft motion streaks", B'de "faint soft motion streaks"; S16'da garson ve mutfak ekibi; S17–S19 konuklar (A'da iz, G'de yandan/arkadan küçük figürler); hiçbir yüz okunmaz, yakın plan yok, çatal-bıçak-tabak ayrıntısı yok (senaryo).
**Vinç kararı [DERS 8 · 22 · 46 · 57]:** tek büyük sarı mobil vinç, sol avluda destek ayakları üstünde (x ≈372 · üstten 517) · G0'dan G15'e · S15'te gider. Bom dik kalkınca ucu kadrajın üstünden çıkar (üst kenar, kamera ekseninden +19,9°; vinçte bom ucu ≈+40 m → kadraj dışı). VİNÇ DEFTERİ aşağıda; G16'dan sonra "crane" kelimesi yok [P7-e].
**Uzun rijit yük [DERS 57]:** ⭐ VAGON (≈24 m) — S0 ilk karede tabliyenin 1 m üstünde, kısa gergin sapanlarla, bom başı tam üstünde ASILI başlar; klip yalnız son metreyi ve oturmayı gösterir; yerden kalkış YOK. Teras çerçeveleri (≈5 × 6 m, S9) ve iki geçit (≈3–4 m, S7–S8) — her biri ilk karede kancada, hedefin hemen üstünde; S9'da 2. ve 3. çerçeve kamyondan KISA yolla (≈20 m) gelir ⚠️ (02 R3).
**Korpus kararı [DERS 55]:** "railway carriage" korpusu çoğul ve raylı olabilir (tren dizisi, ray, istasyon) → NEGATIVE'de her karede: "The canyon holds exactly one carriage, with exactly eight broad windows along its near side and one vestibule at each end, its steel underframe sitting flat on the steel deck." Tekerlek ADIYLA hiçbir yerde yok (sahibin G00'ındaki "bogies and wheels have already been removed" cümlesi bu yüzden yazılmadı — pozitif: "steel underframe sitting flat on the steel deck").
**Yapı adı kararı [DERS 42]:** "old railway passenger carriage" + "steel support deck" + "gangway" + "terrace" + "glass floor panels" yazılır; "train · platform · bridge" YASAK.

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
KARAR CÜMLESİ [KAMERA_DILI §0]: İzleyici paslı bir vagonun uçurumun üstüne inip restorana dönüşmesini, önüne cam tabanlı bir teras
                 kurulmasını ve aynı akşam konuklarla dolmasını görecek. Yarık kaya, çatallı çam, uzak sırtlar ve tek vagonun
                 sekiz penceresi aynı kalacak. Kamera YÜKSEK ÜÇ ÇEYREK aileden (tabliyeden +11 m · tilt 14° aşağı · uzun yüze
                 ≈23° yandan) bakacak — vagonun uzun yüzü, çatısı, iki bağlantı, teras ve cam taban ancak böyle aynı karede
                 okunur. Hareket YOK.

ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0,
                 yani en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp [A7-b]; kutu tam 8,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 20 sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.

┌─ KAMERA İSTASYONU (ANA) ─────────────────────────────────────────────────────┐
│ lens          28 mm doğrusal (rectilinear) · f/8 · ISO 100 (akşam 800–1600) ·  │
│               tam kare YATAY (36 × 20,25 mm) → f = 1493 px · yatay görüş 65,5° │
│ yükseklik     h = +11,0 m (çelik tabliyenin üst yüzünden)                      │
│ mesafe        D_eksen = 32,3 m yatay (vagonun merkezine — BÜTÜN px buradan) ·  │
│               eğik 33,5 m · cam bölüm ≈26 m · yarık kaya 41,2 m [DERS 38]      │
│ bakış açısı   bearing 337° (KKB — kanyonun yukarısına) · tilt 14° AŞAĞI ·      │
│               roll 0° · vagonun uzun yüzüne ≈23° yandan (üç çeyrek)            │
│ sabitleme     "fixed tripod bolted to a rock spur on the right rim of the     │
│               canyon, downstream of the carriage"                              │
│ ⛔ HESAP — iğne deliği izdüşümü (yatay 16:9, f 28 → 1493 px):                   │
│    px = 960 + 1493·Xc/Zc · üstten = 540 − 1493·Yc/Zc (kamera eksenine dönük)  │
│    ufuk / uzak sırt üstten 540 − 1493·tan 14° = 168 (%84)                     │
│    `bolum_uretici.py --kadraj` çıktısı:                                       │
│    ⭐ yarık kaya x 1649–1806 (157 px) · tepe 405 (%62) · dip 655–673           │
│    çatallı çam dip x 260 · 622 · tepe x 196 · 77 (%93)                         │
│    vagon sol çatı 503 · 456 (%58) · sağ çatı 1586 · 554 (%49) · orta çatı 467 │
│    vagon alt şasi sol 515 · 621 (%43) · sağ 1563 · 770 (%29)                   │
│    pencere bandı 548 · 532 → 1507 · 641                                        │
│    G0 asılı vagon altı (+1 m, orta) 965 · 642                                  │
│    sol geçit avlu ucu 382 · 617 · sağ geçit raf ucu 1765 · 821                 │
│    kiriş mesnetleri sol 519 · 716 · sağ 1481 · 882                             │
│    teras ön kenar 455 · 755 (%30) → 1222 · 900 (%17) · arka sol 637 · 663     │
│    cam bölüm ön 679 · 798 → 922 · 843 · arka 812 · 708 → 1027 · 741            │
│    vinç x 372 · 517 · avlu 376 · 558 · servis yolu sol kenardan (≈511)         │
│    insan (1,7 m): cam bölümde 85 px · sol geçitte 66 px · teras masasında 79  │
│    cama bakış 22,6° (cam yukarıdan okunur)                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ İKİNCİ İSTASYON BEYANI [ISTASYON_VE_IC_MEKAN §0 · §6 · KAMERA_ISTASYONU §1] ─┐
│ ad            CARRIAGE STATION (iç) · yalnız S14 (112,0–120,0 sn) · 1 klip · %5│
│ kamera        "fixed clamp mount bolted high on the left end wall inside the  │
│               carriage, lens 3.1 metres above the steel support deck, 21      │
│               metres from the right end wall, bearing 90 degrees, tilt 14     │
│               degrees down, zero roll" · 28 mm · f/8 · ISO 200                │
│ px            sağ uç duvar x 884–1079 (195 px) · üstten 108 → dibi 318 ·       │
│               cam kapı x 949–1013 · yarık kaya uzak sol pencerede ≈x 399 · 233│
│               · uzak sırtlar pencerelerde üstten 168 (%84)                    │
│ şart ①        SABİT ✓ · ⚠️ tilt 0 DEĞİL: iki kamerada AYNI tilt 14° → ufuk iki │
│               kamerada üstten 168 (%84) — kuralın amacı (aynı ufuk) korunur,   │
│               sayısı değişir (hikâye SAPMA ③). Gerekçe: tilt 0'da cam taban    │
│               yukarıdan görünmez (h 11 m'de cama bakış 22,6° gerekir)          │
│ şart ②        ORTAK ÇAPA ✓ — iki SITE bloğunda BİREBİR iki cümle: "one large   │
│               pale rock split from top to bottom by a dark crack" · "a long    │
│               level line of distant blue ridges closes the view, at about      │
│               sixteen percent of frame height from the top" [DERS 10]          │
│ şart ③        DIŞ BÜYÜME TAŞIMAZ ✓ — S14 = S13 ile AYNI on dakika (17:10 →     │
│               17:20); S13 I2V G13 → G15 (ana) · S14 G14 → G14′ (iç) · S15 G15'ten│
│               · I2V'de "This shot shows the same stage as the previous shot    │
│               from the main station" cümlesi                                   │
│ şart ④        BEYANLI ✓ — burada + QA_SPEC künyesi + günlükte İSTASYON sütunu   │
│ karar tablosu konum %70–75 (gelişme bölümü ✓) · ilk üç klip, doruk (S11),     │
│               bölüm sınırı (G10) ve final (S16–S19) DIŞARIDA ✓ · konu: içeride  │
│               masa + bank (dışarıdan pencereler ≈40–60 px — KISMEN okunur ⚠️)  │
│ zaman taşıyıcı alçak güneş şeritleri sağ pencerelerden tabana, sol duvara      │
│               kayar ve söner (güneş +1,8° → +0,1°) · eşya akışı (istif 0'a)    │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① ⭐ YARIK KAYA (SAĞ · x 1649–1806 · 405–673) — KANIT NESNESİ, sağ rafta,      │
│    tabliyenin sağ ucunun arkasında, tepeden dibe koyu çatlakla yarılmış açık  │
│    renkli tek kaya: hiç değişmez · iç kamerada uzak sol pencereden görünür    │
│ ② ÇATALLI ÇAM (SOL · x ≈196–260 · 77–622) — sol rafın kenarında, iki gövde   │
│ ③ UZAK SIRTLAR üstten 168 (%84) · kanyonun sola kıvrılması · ormanlı yamaçlar │
│ ④ ÇELİK TABLİYE (iki derin kiriş · yürüme yolları · dirsekler) — G0'dan kalıcı │
│ ⑤ servis yolu (sol kenardan çakıllı avluya)                                    │
│ + "The canyon holds exactly one carriage, with exactly eight broad windows    │
│   along its near side and one vestibule at each end" — her NEGATIVE'de         │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ tilt 14° → uzak sırt %84 · gök bandı üstten 0–168 (finalde mavi okunur)       │
│ yanlar: solda servis yolu + avlu + vinç + çatallı çam · sağda sağ raf + yarık │
│ kaya + sağ geçit · altta kanyon gölgesi (teras önünden aşağısı)               │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ — kanıt nesnesi alt 100 px'e (üstten > 980)    │
│ girmez ✓ (dip 673) · ⚠️ sağ üst 300×100 px (x > 1620 · üstten < 100) boş ✓     │
│ (kaya tepesi 405)                                                              │
│ ⚠️ kanyon dibi kadrajda değil: "uçurum" teras önünden aşağı inen koyu kaya     │
│    duvarlarıyla okunur (üstten ≈900 → 1080)                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ merkez O = vagon tabanının ortası, tabliyenin üst yüzü (z 0) · +x doğu (vagon │
│   ekseni) · +y kuzey · kamera (12, −30, +11)                                   │
│ boşluk: iki kaya rafı x ±9 (≈18 m) · raflar −1,8 · kanyon ≥100 m derin          │
│ tabliye: iki derin koyu çelik kiriş x ±16 · yakın kiriş y −3 · kiriş altı −1,8 │
│   · mesnetler iki rafta çelik pedler (x ±10…±16) · iki yanda dar yürüme yolu + │
│   alçak korkuluk · yakın kirişte kısa teras dirsekleri                         │
│ vagon: x ±12,2 · y ±1,45 · çatı +4,2 (orta +4,6) · iç taban +1,0 · pencere     │
│   bandı +1,9…+2,9 · her uzun yüzde 8 geniş pencere · iki uç vestibül ·         │
│   tekerleksiz çelik alt şasi tabliyeye cıvatalı                                │
│ geçitler: sol x −15,5 (avlu kenarı → sol vestibül) · sağ x +15,5 (sağ vestibül │
│   → birkaç taş basamak → sağ raf patikası) · uçlarında lamba direkleri         │
│ teras: x ±7,5 · y −3…−9 (15 × 6 m) · üç çelik çerçeve modülü · ahşap sol + sağ │
│   bölüm + vagon boyunca 1 m şerit · cam orta bölüm x ±2,4 · y −4…−9 (üç panel, │
│   kauçuk taşıyıcılı çelik kenar çerçeve) · ince koyu dikme + şeffaf korkuluk + │
│   dibinde küçük ışık şeridi · dört masa (her ahşap bölümde iki)                │
│ iç: ahşap taban · açık panel duvarlar · krem tavan · iki sıra ahşap masa +     │
│   aralarında deri bank · sarkıt lamba sırası · sağ uç duvarda cam kapı         │
│ avlu: x −16…−28 · y −6…+10 · vinç (−24, 6) · servis yolu sol kenardan          │
│ STRUCTURE'ın İngilizce tam hâli tek cümle (DERS 36): "When finished this will │
│   be a cliff-edge restaurant made from one old railway passenger carriage, 24 │
│   metres long, with a rounded roof, eight broad windows along each side and a │
│   vestibule at each end, on a dark steel deck over a narrow deep canyon, with │
│   a gangway at each end and a timber terrace with a glass-floored middle in   │
│   front." — 21 görselde + G14′'de BİREBİR                                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 20 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az YAPI göstermez. S0–S1'de vagon YERİNE GELİR; S2'de eski camlar
> çıkar (yenisi S6'da — yapı kaybı değil, yenilemenin ilk adımı); S3–S6 vagon KAZANIR; S7–S13 bağlantılar ve teras KAZANIR; S14
> içerisi KAZANIR; S15'te şantiye gider (yapı aynı); S16–S19 yapıyı KULLANIR. Kış görüntüsü YOK (tek sonbahar günü; DERS 7 tetiklenmez).

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | MEVSİM TAŞIYICISI | KANIT NESNESİ (px) |
|:-:|:-:|---|---|:-:|:-:|:-:|---|---|
| 0 | 8,0 | İNDİRİR | ⭐ vagon tabliyenin 1 m üstünden tabliyeye · sapanlar bağlı | 1 sa | A | 09:30→09:40 | sonbahar (sabit) · ışık: sabah | vagon altı 642 → 685 (orta) |
| 1 | 8,0 | ÇÖZER | sapanlar çözülür · çapraz kiriş avluya · bom dik | 1 sa | A | 09:40→09:50 | aynı | vinç bomu dışarı |
| 2 | 8,0 | SÖKER | sekiz kırık cam soldan sağa → kasalar (8 → 0) | 2 gün | A | 09:50→10:00 | aynı | sekiz boş açıklık 548 → 1507 |
| 3 | 8,0 | SIYIRIR | pas → çıplak gri çelik, soldan sağa (%0 → %100) | 2 hafta | B | 10:00→12:00 | aynı · ışık: öğleye | ⭐ gri bant 503 → 1586 |
| 4 | 8,0 | BOYAR | astar → zümrüt gövde + krem şerit, soldan sağa (%0 → %100) | 2 hafta | B | 12:00→14:00 | aynı · ışık: öğleden sonra | ⭐ yeşil bant 503 → 1586 |
| 5 | 8,0 | KAPLAR | bakır levhalar çatıya, soldan sağa (%0 → %100) | 1 hafta | A | 14:00→14:10 | aynı | çatı 456 → 554 bakır |
| 6 | 8,0 | CAMLAR | sekiz yeni cam, soldan sağa (sehpa 8 → 0) | 3 gün | A | 14:10→14:20 | aynı | sekiz cam 548 → 1507 |
| 7 | 8,0 | BAĞLAR | sol geçit (%100) + iki sönük lamba | 1 hafta | A | 14:20→14:30 | aynı | geçit 382 · 617 |
| 8 | 8,0 | BAĞLAR | sağ geçit + taş basamaklar (%100) + iki sönük lamba | 1 hafta | A | 14:30→14:40 | aynı | geçit 1765 · 821 |
| 9 | 8,0 | ÇATAR | üç teras çerçevesi dirseklere, soldan sağa (3 → 0) | 1 hafta | A | 14:40→14:50 | aynı | iskelet ön kenar 455 → 1222 |
| 10 | 8,0 | DÖŞER | ahşap sol + sağ + şerit (%0 → %100) · orta AÇIK | 3 hafta | B | 14:50→16:50 | aynı · ışık: alçalan güneş | ⭐ ahşap bölümler · orta açıklık 679–922 |
| 11 | 8,0 | CAMLAR | ⭐ üç cam panel ortaya (1 vinç + 2 sehpadan) | 2 gün | A | 16:50→17:00 | aynı · ışık: altın saat | ⭐ cam 679–922 · 708–843 |
| 12 | 8,0 | ÇEVİRİR | korkuluk açık kenarlara (%0 → %100) + sönük ışık şeridi | 1 hafta | A | 17:00→17:10 | aynı | korkuluk 455 → 1222 |
| 13 | 8,0 | DÖŞER | dört dış masa + sandalye (0 → 4) | 1 gün | A | 17:10→17:20 | aynı · gün batımı | masalar ahşap bölümlerde |
| 14 | 8,0 | DONATIR | 🪟 iç: masa + bank (istif → %100) + sönük sarkıt lamba | 1 hafta | A | 17:10→17:20 (S13 ile paralel) | aynı · gün batımı (içeride güneş şeritleri) | uç duvar 884–1079 · kaya uzak sol pencerede |
| 15 | 8,0 | BOŞALTIR | vinç + telehandler + kamyonlar + kasalar çıkar | 1 gün | A | 17:20→17:30 | aynı · gün batımı | vinç 372 → 0 |
| 16 | 8,0 | YAKAR | ışıklar gruplar hâlinde: iç → geçitler → korkuluk | 10 dk | A | 17:30→17:40 | aynı · alacakaranlık | ⭐ ışık kümeleri |
| 17 | 8,0 | GETİRİR | ilk konuklar yol → avlu → sol geçit → içeri | 10 dk | A | 17:40→17:50 | aynı · mavi saat | pencerelerde siluetler |
| 18 | 8,0 | CANLANDIRIR | ⭐ gerçek zaman: konuklar terasa, üç masaya | 8 sn | G | 17:50:00→17:50:08 | aynı · derin mavi | dış masalar dolar |
| 19 | 8,0 | TAMAMLAR | çift cama yürür (0–4 sn) · TUTUŞ (4–8 sn) | 8 sn | G | 17:50:08→17:50:16 | aynı | ⭐ kaya 1649–1806 · çift camda |

```
IZGARA          8,0 sn × 20 · kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn) · müzik 120 BPM → her kesme ölçü başında
                (8,0 sn = 4 ölçü) · istasyon kesmeleri 112,0 (ana → iç) ve 120,0 (iç → ana)
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: sahip senaryosunun biçimi (20 × 8,0, kart yok — hikâye SAPMA ②); emsal THE FIRST LIGHT ·
                       THE SKY CANAL · THE SUNKEN STAGE (20 × 8,0). ⚠️ BANDIN DIŞI: format 12 × 10,0.
                   (b) ritim klip İÇİNE: ① rejim nabzı — B'ler S3 · S4 · S10 (pas · boya · ahşap), G'ler S18 · S19 (gerçek
                       zaman, final); ② iş yönü değişir: aşağı (S0 vagon) · yukarı (S1 kiriş) · soldan sağa (S2–S6 gövde) ·
                       iki uç (S7–S8 geçitler) · kameraya doğru (S9–S10 teras) · ortaya (S11 cam) · kenarlar (S12) · avludan
                       teras (S13) · koridor boyunca (S14 iç) · dışarı (S15) · ışık grupları (S16) · yoldan içeri (S17) ·
                       içeriden terasa (S18) · cama (S19); ③ müzik katmanı = aşama (MUZIK.md); ④ bir istasyon kesmesi (S14)
                   (c) kabul edilen risk: eşit klipte ❷ RHYTHM kategorisi NOT TRIGGERED — sapma kurgudan gelirse (klip ≠ 8,0)
                       ❷ açılır ve ❺ final saniyesi kayar. Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
REJİM SAYISI    ⚠️ ÜÇ rejim (A · B · G) — SANTIYE_HAREKETI §2 sınırı iki. Gerekçe: G yalnız final klipleridir (S18 · S19) ve
                rejim G'nin tanımı tam budur: "yalnız filmin SON sahnelerinde ve yalnız hareket ÖDÜLSE" (konukların yürüyüp
                oturması, çiftin cama adımı — senaryo: "hafif rüzgâr, içeride küçük hareketler, terastaki çift"). A'da (75×)
                yürüyen insan bulanık şerit olur. Geçiş KESMEDE (S17 → S18, 144,0) [P5-c]. ⚠️ G depoda ölçülmedi —
                kapı tanır ("eight seconds pass" + "moves at natural speed"). PİLOT ① ölçer.
IŞIK GÜNÜ       Σ pencere = 14 ana A × 10 dk + 3 B × 2 sa + 2 G × 8 sn = 140 dk + 6 sa + 16 sn = 8 sa 20 dk ≤ 14 ✓
                (S14 iç klip S13 ile AYNI on dakika — pencereye eklenmez) · 09:30 (güneş 24,8°) → 17:50:16 (mavi saat, −4,9°)
MAVİ SAAT       güneş −2…−6° penceresi [ISIK_FINALI §1]: S16 (−1,5 → −3,2) · S17 (−3,2 → −4,9) = İKİ A klibi ✓ (sınır iki) ·
                S15 gün batımı (+0,1 → −1,5) · S18–S19 G (−4,9, 16 sn) — final kareleri −4,9° ✓ (−4…−6)
BÖLÜM SINIRI    G10 — S9 son karesi = S10 ilk karesi; üç teras çerçevesi dirseklerde, ortası açık, döşemesiz; iki geçit + lambalar
                sönük; vagon yeşil + bakır + camlı; vinçte döşeme paleti; gölge sağa (bağıl −111°), öğleden sonra — ikisinde de
                aynı [DERS 52]
TEK KALDIRMA    S0 + S1 — aynı vinç, aynı çapraz kiriş, aynı dört sapan; vagon S0 sonunda oturur, S1'de sapanlar çözülür; vagon
                bir daha HİÇ kalkmaz (LOCK cümlesi S1'den)
TEK AKŞAM       S16 + S17 + S18 + S19 — yanan lamba bir daha sönmez; oturan konuk yerinde kalır; 144,0'de rejim A → G
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: YARIK KAYA — G0'da ve usta karede (G20) aynı konum (x 1649–1806) ve aynı boy (157 px en · tepe 405 ·
        dip 655–673) [DERS 25]; tepeden dibe koyu çatlaklı tek açık renkli kaya, sağ rafta; hiç değişmez. Yedek: çatallı çam
        (x ≈196–260 — G'de dalları hafif sallanır, yeri sabit) + uzak sırtlar (168).
LOOP    G20 ↔ G0: aynı kadraj · aynı kaya · aynı çam · aynı sırtlar · aynı vagon boyu ve sekiz pencere · ışık FARKLI (bilinçli —
        G0 sabah, G20 mavi saat; tek gün): G0'da paslı vagon boşluğun üstünde kancada / G20'de aynı vagon ışıklı, önünde
        camın üstünde bir çift. Biçim kafiyesi: G0'da vagonun altındaki 1 m boşluk ↔ G20'de çiftin ayağının altındaki cam ve
        uçurum.
SÖKÜM   S0 cıvata sandıkları (kamyon) · S1 çapraz kiriş avluya iner, boş kasalar yığılır · S2 dolu kasalar + atık konteyneri
        (kamyonla gider), kompresör gelir · S3 sonu kompresör gider, boya römorku gelir · S4–S14 kamyonlar (bakır · cam ·
        geçit · çerçeve · döşeme · korkuluk · masa) boşalınca gider · S11 cam sehpası ekiple taşınır · S15 VİNÇ (bomunu
        katlar, servis yolundan çıkar) + TELEHANDLER + kamyonlar + boş kasalar + paletler + atık konteyneri — ekranda; geçitler
        + lambalar + teras + korkuluk KALIR (kalıcı) [DERS 48 · P2-h]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
vagon                   → vinç kancası (G0'da zaten asılı) → tabliye                                → G0
cıvatalar               → kamyon → sandıklar → ekip → alt şasi                                     → S0 içinde
eski camlar (giden)     → camcılar (vakumlu tutucu) → yürüme yolu → avludaki kasalar → kamyon        → G2
pas (giden)             → kumlama hortumları (kompresör + kum haznesi) → brandalar → torbalar → palet → G3
boya                    → boya römorku + varil paletleri → püskürtme ekipleri                       → G4
bakır levhalar          → kamyon → vinçte palet → çatıdaki beşik → çatıcılar                        → G5
pencere camları         → kamyon → vinçte sehpa → yürüme yolu → camcılar                            → G6
geçitler                → kamyon → vinç → mesnetler                                                 → G7 · G8
taş basamaklar          → sağ raftaki istif → ustalar                                               → G8
teras çerçeveleri       → uzun kamyon (3) → vinç → dirsekler                                        → G9
ahşap döşeme            → kamyon → vinçte paletler → marangozlar                                    → G10
cam paneller            → vinçte vakumlu çerçeve (1) + sol ahşap bölümde sehpa (2) → cam el arabası  → G11
korkuluk                → vinçte sandık → sağ ahşap bölüm → camcılar                                → G12
dış masalar             → kamyon (avlu) → sol geçit → teras                                         → G13
iç masa + bank          → sağ cam kapının önündeki istif → koridor · el arabası                     → G14 (iç)
konuklar                → servis yolu (sol kenar) → avlu → sol geçit → sol vestibül → masalar        → G17
GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL (prompta yalnız vekil girer):
   tabliyenin tasarımı ve hesabı → ilk karede hazır kirişler ve mesnet pedleri · elektrik tesisatı → lamba direkleri,
   korkuluk dibindeki ışık şeridi, sarkıt lambalar (sönük takılır) · mutfak → S16'da mutfak ekibinin taşıdığı erzak kasaları
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① ışıklı sekiz pencere + zümrüt gövde + bakır çatı (x 503–1586 · üstten 456–770, ilk okunan, en parlak) → ② cam orta bölüm ve
   üstündeki çift (679–922 · 708–843; insan ≈85 px) → ③ terastaki masalar ve konuklar + korkuluk ışık şeridi → ④ iki geçit ve
   lambaları + tabliye + kanyon gölgesi → ⑤ yarık kaya (kanıt) + çatallı çam + mavi gök ve uzak sırtlar
FİNAL KARE KANITI  ffmpeg -ss 159.0 -i teslim.mp4 -frames:v 1 kanit.jpg   (S19 tutuşu 156,0–160,0 içinde · mavi saat, okunur
                   [DERS 45]) · kart YOK → son kare = G20
```

---

## 🖼️ KARE TABLOSU — 21 görsel + G14′ [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Bağıl güneş = güneş azimutu − kamera bakışı (337°); 0 = kameranın baktığı yön, − sol, + sağ, |x| > 90 = kameranın arkası.
> Sayılar `bolum_uretici.py --tablo` çıktısıdır (47° K · δ −9° · güneş saati). G16+ güneş ufkun altında → gölge yok.
> 🪟 G14 ve G14′ iç istasyonun kareleridir (bakış 90°; güneş iç kameraya göre arkada sağda, bağıl +165°).

| G | SAAT | AZİMUT | YÜKSEKLİK | BAĞIL GÜNEŞ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| G0 | 09:30 | 139° | 24,8° | +162° | açık, ince yüksek bulut | sonbahar (sabit) | ⭐ AÇILIŞ — paslı vagon tabliyenin 1 m üstünde asılı · halat ekipleri · kamyon |
| G1 | 09:40 | 141° | 25,9° | +164° | aynı | aynı | vagon tabliyede, cıvatalı · sapanlar bağlı · boş kasa kamyonu + telehandler |
| G2 | 09:50 | 143° | 27,0° | +166° | küçük bulutlar | aynı | sapanlar çözük · bom dik (dışarı) · çapraz kiriş avluda · eski camlar yerinde |
| G3 | 10:00 | 146° | 28,0° | +169° | aynı | aynı | sekiz açıklık BOŞ · paslı · kompresör + kum haznesi · brandalar |
| G4 | 12:00 | 180° | 34,0° | −157° | aynı | aynı | ⭐ gövde çıplak gri çelik · boya römorku · varil paletleri |
| G5 | 14:00 | 214° | 28,0° | −123° | aynı | aynı | ⭐ zümrüt + krem şerit · çatı gri · vinçte bakır levha paleti |
| G6 | 14:10 | 217° | 27,0° | −120° | aynı | aynı | çatı bakır · açıklıklar boş · vinçte cam sehpası |
| G7 | 14:20 | 219° | 25,9° | −118° | aynı | aynı | sekiz cam tamam · vinçte sol geçit |
| G8 | 14:30 | 221° | 24,8° | −116° | aynı | aynı | sol geçit + sönük lambalar · vinçte sağ geçit · taş basamak istifi |
| G9 | 14:40 | 224° | 23,7° | −113° | aynı | aynı | iki geçit · vinçte ilk teras çerçevesi · kamyonda iki çerçeve |
| G10 | 14:50 | 226° | 22,5° | −111° | aynı | aynı | ⭐ BÖLÜM SINIRI — teras iskeleti açık, ortası açıklık · vinçte döşeme paleti |
| G11 | 16:50 | 251° | 5,1° | −86° | alçalan sıcak ışık | aynı | ⭐ ahşap yan bölümler · orta açık · vinçte cam panel · sehpada iki panel |
| G12 | 17:00 | 253° | 3,4° | −84° | altın saat | aynı | ⭐ üç cam panel · kenarlar açık · vinçte korkuluk sandığı |
| G13 | 17:10 | 255° | 1,8° | −82° | gün batımı | aynı | korkuluk + sönük ışık şeridi · bom dik · masa kamyonu |
| G14 🪟 | 17:10 | 255° | 1,8° | (iç +165°) | pencerelerden | aynı | iç: kaplı salon, BOŞ · kapının önünde masa + bank istifi · güneş şeritleri |
| G14′ 🪟 | 17:20 | 257° | 0,1° | (iç +165°) | pencerelerden | aynı | iç: iki sıra masa + bank · sarkıt lambalar SÖNÜK · son güneş şeridi |
| G15 | 17:20 | 257° | 0,1° | −80° | gün batımı | aynı | dört dış masa · vinçte boş kasa demeti · telehandler · konteyner · lambalar sönük |
| G16 | 17:30 | 258° | −1,5° | — | alacakaranlık | aynı | ⭐ saha boş — vinç, kamyon YOK · beyaz minibüs · bütün lambalar SÖNÜK |
| G17 | 17:40 | 260° | −3,2° | — | mavi saat | aynı | ⭐ içerisi + geçitler + korkuluk YANIK · masalar örtülü, boş |
| G18 | 17:50:00 | 262° | −4,9° | — | derin mavi | aynı | içerideki masaların çoğu dolu (siluet) · dış masalar boş |
| G19 | 17:50:08 | 262° | −4,9° | — | aynı | aynı | üç dış masada konuk · çift sol ahşap bölümde |
| G20 | 17:50:16 | 262° | −4,9° | — | ⭐ derin mavi, okunur | aynı | ⭐ USTA KARE — çift camın ortasında, vadiye dönük |

```
VAGON DEFTERİ   G0 asılı (tabliyenin 1 m üstü, kısa gergin sapanlar, bom başı üstte) · G1 tabliyede, cıvatalı, sapanlar bağlı ·
                G2+ serbest, cıvatalı — vagon bir daha kalkmaz, sallanmaz, kaymaz; boyu, çatı çizgisi, sekiz pencere ve iki
                vestibül hiçbir karede değişmez [sahip: "Pencere açıklıkları hiçbir aşamada çoğalmaz veya yer değiştirmez"]
GÖVDE DEFTERİ   G0–G2 pas + eski camlar · G3 pas + boş açıklıklar · G4 çıplak gri çelik · G5 zümrüt + krem, çatı gri · G6 çatı bakır
                · G7+ sekiz yeni cam · temizlenen yer bir daha paslanmaz, boyanan yer bir daha soyulmaz
TERAS DEFTERİ   G0–G9 yalnız dirsek uçları · G10 üç çelik çerçeve, ortası açıklık · G11 ahşap yan bölümler + şerit, orta AÇIK
                (bu sonradan sökülen bir döşeme DEĞİL) · G12 üç cam panel · G13+ korkuluk · G15+ dört masa
VİNÇ DEFTERİ [DERS 8 · 46 · 57]   (YÜK = kancada görünür yük · DIŞ = bom ucu + halat kadrajın üstünde)
   G0  YÜK vagon (çapraz kirişle)    G5  YÜK bakır levha paleti      G10  YÜK döşeme paleti        G15  YÜK boş kasa demeti
   G1  YÜK çapraz kiriş (sapanlar    G6  YÜK cam sehpası             G11  YÜK cam panel (vakumlu)  G16+ vinç YOK
       vagona bağlı)                 G7  YÜK sol geçit               G12  YÜK korkuluk sandığı
   G2  DIŞ                           G8  YÜK sağ geçit               G13  DIŞ
   G3  DIŞ                           G9  YÜK teras çerçevesi         G14  (iç kare — vinç görünmez)
   G4  DIŞ
   ⚠️ YÜK → DIŞ: S1 sonu (kirişi avluya bırakır, bomu dikleştirir) · DIŞ → YÜK: S4 sonu (bom iner, bakır paleti bağlanır) ·
      YÜK → DIŞ: S12 sonu (sandığı bırakır, bomu dikleştirir) · DIŞ → YÜK: S13 sonu (bom iner, ekip boş kasa demetini bağlar) ·
      S15'te bom katlanırken kanca boş — THE FIRST LIGHT S15 · THE SKY CANAL S12 · THE SUNKEN STAGE S13 emsali, beyanlı
IŞIK DEFTERİ [ISIK_FINALI §4]
   armatür / grup            takıldığı klip   sönük kareler   grup   yanma · saniye (film)                    renk
   iç sarkıt lambalar         S14 (iç)         G14′–G16        1      S16 ≈ 129 sn (ilk grup, TEK KAREDE)      sıcak
   geçit lamba direkleri (4)  S7 · S8          G8–G16          2      S16 ≈ 131 sn                             sıcak
   korkuluk dibi ışık şeridi  S12              G13–G16         3      S16 ≈ 133 sn                             sıcak
   ⛔ A'da "fades in · gradually · slowly lights up" YAZILMAZ; her grup bir anda · negatifte ışık etkisinin adı YOK
KONUK DEFTERİ [P24-e · P25-c]
   G0–G16  konuk YOK (G16–G17'de garson ve mutfak ekibi)
   G17     konuk yok (ilk gruplar S17'de yoldan gelir) · masalar örtülü
   G18     içerideki masaların çoğu dolu (pencerelerde siluet) · dış masalar boş · cam boş
   G19     üç dış masada konuk · çift sol ahşap bölümde · cam boş
   G20     aynı + çift camın ortasında
   ⛔ kimse koltukta "belirmez" — her kişi yoldan, avludan, geçitten yürür; cam bölüm S19'a kadar boş (senaryo)
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G20 usta kare → G19 (çift camda değil) → G18 (dış masalar boş) → G17 (içerisi boş) → G16 (lambalar sönük) → G15 (vinç,
   telehandler, kamyonlar geri gelir) → G13 (masalar yok) → G12 (korkuluk yok) → G11 (cam yok, orta açık) → G10 (ahşap yok) →
   G9 (iskelet yok) → G8 (sağ geçit yok) → G7 (sol geçit yok) → G6 (camlar yok) → G5 (çatı gri) → G4 (gövde gri, krem yok) →
   G3 (pas) → G2 (eski camlar yerinde) → G1 (sapanlar bağlı) → G0 (vagon asılı, 1 m yukarıda)
   🪟 İÇ ZİNCİR ayrı: G14′ ÖNCE (ana G15'in saati ve ışığıyla) → G14 ondan (masa + bank geri alınarak, istif kapıda)
   ⚠️ zincir_kontrol ana kareleri birbirine, iç kareleri birbirine bağlar — ana kare ile iç kare zincir_kontrol'e VERİLMEZ
   sonra I2V S0 (G0→G1) … S13 (G13→G15) · S14 (G14→G14′) · S15 (G15→G16) … S19 (G19→G20) — üretim 9,0 sn, baştan 1,0 kırp
```

## 🧪 PİLOT ÜÇLÜ [DERS 62 · KILAVUZ_REHBERI §8 adım 2b]

```
⛔ Üretim başlamadan, aşağıdaki üçü geçmeden kalan klipler üretilmez:
① FİNAL      G20 + G19 + G18 + S18 + S19 — rejim G (gerçek zaman) burada ilk kez ölçülür: konuklar doğal hızda yürüyüp oturuyor mu,
             çift cama normal adımla mı geliyor (koşma, sarkma yok), yüz okunmuyor mu, kimse belirip kaybolmuyor mu; S19 son 4 sn
             TUTUŞ (yapı kıpırdamaz) [C1-b]; cam ayna ya da delik değil, kenar + yansıma + altında kanyon; gök MAVİ ve okunur
② EN BÜYÜK   G0 + G1 + S0 — ⭐ açılış ve DERS 57: vagon ilk karede ASILI, klip yalnız son metreyi indiriyor mu; vagon kopyalanıyor
   DEĞİŞİKLİK  mu (iki vagon), kanca/sapan yükten kopuyor mu, vagon sallanıyor mu, tekerlek/ray çiziliyor mu · 0. saniyede hareket
③ CAM        G11 + G12 + S11 — üç panel sırayla iniyor mu, cam okunuyor mu (kenar + gök yansıması), açıklık "boya" gibi
             kapanmıyor mu; altındaki kanyon görünür kalıyor mu
PİLOT SONRASI İLK  S3 · S4 (B rejiminde pas → gri → yeşil süpürmesi) + S14 (iç istasyon — ortak çapa pencerede okunuyor mu) +
                   S16 (üç ışık grubu)
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     47,0° K · ışık günü tarihi: δ −9° (ekim ortası) · batış (−0,833°) ≈17:26 (güneş saati) · kamera bakışı 337° (KKB)
                → kadraj 304° … 10° azimut · güneş 139° → 262°: sabah kameranın arkasında sağda (bağıl +162°), öğle arkada
                (−157°), öğleden sonra arkada solda (−123°), akşam solda (−86° → −75°) — HİÇBİR karede kadrajda değil (yarım
                görüş 32,7°), ters ışık YOK [P8-h]
VAGON IŞIĞI     vagonun yakın uzun yüzü güneye (≈180°) bakar → sabahtan öğleden sonraya önden aydınlık, altın saatte (G11–G13)
                soldan sıyırarak gelen sıcak ışık; kanyonun içi hep gölgede (derin); G16+ güneş ufkun altında, ışık düz, lambalar
                en parlak
İÇ IŞIK         iç kamera doğuya bakar (90°); güneş 255° → arkada sağda: alçak güneş sağ (güney) pencerelerden ince uzun şeritler
                düşürür, şeritler sol duvara kayar ve S14 sonunda söner (güneş +0,1°)
GÖLGE SÜPÜRMESİ rejim B klipte: S3 (+169° → −157°: 34°) · S4 (−157° → −123°: 34°) · S10 (−111° → −86°: 25°, uzar) · rejim A klipte fark
                edilmez → yüzeyle kanıtlanır · G klipte (8 sn) yok
MAVİ SAAT       −0,833° 17:26 · −2° 17:33 · −4° 17:45 · −6° 17:57 (ISIK_FINALI §1 formülü) · final 17:50 (−4,9°) — pencerenin içinde;
                gök mavi, yapı ve kayalar okunur, siyah siluet DEĞİL [DERS 45]
MEVSİM          tek sonbahar günü (SITE bloğunda sabit) · taşıyıcı IŞIKTIR (sabah → öğle → altın saat → mavi saat), takvim değil
                (ÜSLUP BEYANI) · ⚠️ DERS 14'ün "mevsim taşıyıcısı" sütunu burada ışık evresini taşır
KIŞ / GECE      görüntü YOK · DERS 7 tetiklenmez · final mavi saat (gece değil)
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   ANA h +11,0 (tabliyeden) · D_eksen 32,3 · bakış 337° · tilt 14° aşağı · roll 0 · 28 mm · üç çeyrek (≈23°)
         İÇ h +3,1 · sağ uç duvara 21 m · bakış 90° · tilt 14° aşağı · roll 0 · 28 mm · yalnız S14
YAPI     tek vagon x 503–1586 · çatı 456 → 554 · alt şasi 621 → 770 · 8 pencere · 2 vestibül · geçitler 382 · 617 / 1765 · 821 ·
         teras ön kenar 455 · 755 → 1222 · 900 · cam 679–922 · 708–843
VAGON    G0 asılı (+1 m) · G1+ tabliyede · bir daha kalkmaz
IŞIK     G0–G16 lambalar sönük · G17+ iç + geçit + korkuluk yanık
KONUK    G0–G17 yok · G18 içerisi çoğu dolu · G19–G20 + üç dış masa · çift G19 ahşapta, G20 camda
ÇAPALAR  ① YARIK KAYA x 1649–1806 · 405–673 (kanıt nesnesi 157 px) · ② çatallı çam ≈196–260 · ③ uzak sırtlar 168 · ④ tabliye
IZGARA   20 × 8,0 · kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn) · kart YOK · 160,0 sn · 120 BPM
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_LAST_CARRIAGE   → sonuç QA_SPEC §8'de (12.10.2026)
✅ FIX'ler ve beyanları (hepsi elle okundu):
   · ARAÇ KUTU SETİ ölçülmedi — beyanlı; üretim araç kapısıyla açılır
   · süreler eşit (8,0) — düz ızgara (sahip senaryosu, SAPMA ②); beş mercekte ❷ RHYTHM eşit klipte tetiklenmez
   · İSTASYON KESMESİ: kapı kareleri sırayla eşler; S13 (G13 → G15) ve S14 (iç) çiftlerinde "YENİ eleman" (DERS 61) uyarısı
     çıkarsa yanlış alarmdır [ISTASYON_VE_IC_MEKAN §2] — bu koşuda çıkmadı
✅ YASAK KELİME taraması 0 · kelime kilitleri (rust G0–G3 · emerald/copper S4+ · crane G0–G15 · gangway S6 sonu+ · glass floor
   S10 sonu+ · ışık yanık S16+ · guests S17+ · couple S18+) betikle doğrulandı (12.10.2026 · 42 blok)
✅ 00_ANALIZ yedi dosya · hikâye onayı 12.10.2026 (TUR 1 · SAPMA ①–⑱ sahip okur)
⛔ ARAÇ KAPISI koşulmadı → THE_LAST_CARRIAGE_URETIM_GUNLUGU.md §0 (⑨ iki istasyon tilt eşleşmesi · ⑩ rejim G ölçümü eklendi)
⛔ PİLOT ÜÇLÜ koşulmadı → S18 + S19 · S0 · S11
⛔ SÜRE / KLASÖR — 160 sn yatay_2_dk bandının dışında (SAPMA ②) → sahip kararı
```
