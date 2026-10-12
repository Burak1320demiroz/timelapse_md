# 🏞️ THE_HIDDEN_FALLS — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **15 × 8,0 sn = 120,0 sn** | Kapak kartı: **⛔ YOK** | Toplam: **120,0 sn**
Prompt yapısı: ⭐ **15 sahne → 14 ana görsel (G0…G6 · G8…G12 · G14 · G15) + 2 salon ilk karesi (G7 · G13) + 2 salon son karesi (G7′ · G13′) + 15 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G9**
Yapı: **kireçtaşı ocağının uzak duvarına yaslanan iki katlı, tam cam cepheli yapı (45 m) — sağ ucunda çift yükseklikte cam salon, önünden şelale** (kart yok: `YAPI_TIPI_KARTLARI` §10 şablonuyla 00_ANALIZ/02 §2'de yazıldı; en yakın emsal THE GLASS WALL cam cephe · THE DEEP END havuz → yapı) · Saha: **terk edilmiş kireçtaşı ocağı, 38° K, ılıman, karsız** (kart yok: `SAHA_VE_IKLIM_KARTLARI` §3.7 şablonuyla 02 §2 — kırsal §3.2 + dağ §3.4'ten)
Zaman yayı: **gerçekte ≈15 ay (ilkbahar → ertesi yaz başı) → 120 saniye** · film mertebe anlatır: *"bir yaz inşaat, bir sonbahar bahçe, bir bahar dolum"* [P1-c] · ÜSLUP BEYANI: takvim tek bir günün ışığına sıkıştırıldı (THE OLD ROAD · THE SLOW TAKEOFF emsali)
Işık günü: **06:30 → 19:20 (mavi saat) · Σ rejim penceresi 12 sa 50 dk ≤ 14** — kesmede ışık atlamaz [§2.7 ①] · mavi saat = sahip senaryosu ("Akşam olur … ışıklar yanar")
Kamera mimarisi: **MAIN STATION** — 13 sahne + usta kare · **SALON STATION** (ikinci istasyon) — 2 sahne: S7 · S13 · ⚠️ ISTASYON_VE_IC_MEKAN §1 iki sınırı AŞAR (filmin %13'ü > %10 · S13 final bölgesinde) — sahip senaryosu 08.10.2026 [§0 ① ② ③ tutar · ④ beyanlı]
Izgara: ⛔ **DÜZ — 15 × 8,0** · ⚠️ BANDIN DIŞI (format 12 × 10,0) — sahip izinli varyant (yatay_2 README, 16.09.2026) + sahip senaryosu 08.10.2026 · §DÜZ IZGARA BEYANI
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 08.10.2026 (TUR 1 · SAPMA ①–⑭)
Havuz kaydı: `apexait/YAYIN_PLANI.md` — ⬜ satır açılmadı (16:9 hattı dikey ızgaraya sayılmaz; sahip kararı bekliyor) · siluet ailesi: **suya dönen çukur / cam yapı** (THE DEEP END · THE GLASS WALL ile akraba → ardışık yayınlanmaz)

_"İlk karede kirli suyla dolu, paslı bir yükleme platformunun durduğu ölü bir taş ocağı; son karede aynı çukur turkuaz bir göl, uzak duvarın dibinde ışıklı bir cam yapı ve salonunun önünden akan bir şelale."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     15 sahne × 8,0 sn                       = 120,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     ⛔ YOK — sahip senaryosu 08.10.2026: "tam 2 dakika"; film adı yalnız küçük resme eklenir
               (THE SLOW TAKEOFF · THE BORROWED HILL emsali) · teslim son ana görüntüyle biter; ihrac_kontrol.sh --kart YOK
──────────────────────────────────────────────────────────────
TOPLAM                                                     120,0 sn
HIZ             1x (yatay hat 2x'e çevrilmez — 2x yalnız dikey paylaşım kuralıdır [DERS 58])
MÜZİK           ⛔ YOK (varsayım) — sahip senaryosu müzik değil SES tarif etti: makine/metal → ahşap/cam → şelale +
               içeriden boğuk su · SES TABLOSU THE_HIDDEN_FALLS_MUZIK.md · ⬜ sahip müzik isterse eklenir
               (yatay hatta müzik serbest, sahip 05.10.2026) · hikâye SAPMA ⑫
YASAK KELİME    hotel · resort · spa · pool · fountain · dam · dynamite · blast · explosion · mine · mining · shanghai · wonderland · underwater · aquarium · infinity · neon
               ⭐ [DERS 59 · 42 · P23-b] hiçbir promptta, negatifte bile — otel/spa/havuz korpusu fayanslı yüzme havuzu ve
                  otel kulesi, "dam" baraj, "fountain" süs çeşmesi, patlatma kelimeleri maden ocağı makinesi, "underwater ·
                  aquarium · infinity" su altı odası ve sonsuzluk havuzu, "shanghai · wonderland" GERÇEK PROJE çağırır.
                  Şelalenin indiği yer "the turquoise water", ocak "quarry basin" yazılır.
KELİME KİLİDİ   "crane" yalnız G0–G8 + S0–S8 I2V [P7-e] · "turquoise" yalnız S10 I2V ve G11'den sonra · "waterfall"
               yalnız S11 I2V ve G12'den sonra · STRUCTURE'da su, göl ve şelale YOK (yalnız yapı) [DERS 36]
İKİNCİ İSTASYON BEYANI  SALON STATION · S7 (∥ S8 · 13:10–13:20) · S13 (∥ S12'nin son 8 sn · gerçek zaman) · bakış 180° ·
               ortak çapa iki cümle birebir (kireçtaşı duvarlar + havzadaki sütun) [ISTASYON_VE_IC_MEKAN §0 ④]
BÖLÜM DOSYASI   BOLUM_1 = S0–S8 (0–72,0)  ·  BOLUM_2 = S9–S14 + USTA KARE (72,0–120,0)  ⚠️ betiğin ceil(15/2)=8 bölmesi
               DEĞİL — salon klibi S7 sınıra düşmesin (hikâye SAPMA ⑩)
QA BİRİMİ       FİLM (tek master × 5 mercek · ❶ ❷ ❸ kör · ❹ ❺ belgeli) — QA/HAM/THE_HIDDEN_FALLS/
```

⛔ Kart olmadığı için platform son ekranı **son 5 saniyeye konmaz** ya da yalnız gök bandına (üstten 0–300 px) konur — perde, salon ve köprüdeki üç kişinin üstüne yerleştirilmez.
⚠️ Son sahnenin (S14) son 4,0 sn'lik TUTUŞU final kanıtıdır (`QA_SPEC` §1): üç kişi korkulukta durur, şelale akar, ışıklar yanık, başka hiçbir şey değişmez.
⭐ Platform küçük resmi (kapak) G15'ten gelir (sahip kararı 19.09.2026 — öncesi/sonrası bölme yok); senaryo: "şelalenin arkasındaki sıcak ışıklı cam salon belirgin".

### ⭐ İZLEYİCİ KAPISI [C2-a…d · KILAVUZ_REHBERI §6]

```
İŞLEV ANI         S11 şelale gerçek hızda AKMAYA BAŞLAR → S12 ışıklar tek karede yanar → S13 perdenin arkasından içerisi →
                  S14 köprüde üç kişi. Olay S14'ün ilk yarısında (0–4 sn: yürüyüş), ikinci yarı TUTUŞ (4–8 sn).
AÇILIŞ NESNESİ    G0: kirli suyla dolmuş dev taş ocağı (kadrajın tamamı) + ona ne oluyor: vinç paslı yükleme platformunu
                  dibinden koparmış, suyun üstünden taşıyor. 120 px'te okunan: üç yanda gri duvar, dipte koyu su, ortada sütun.
DİRENÇ EKRANDA    ① çukur — S0 vinçte platform, S1 inen kirli su ve ortaya çıkan basamaklar · ② duvar — S3 havzanın üstünden
                  uzanan vinç kolu, S8 ipteki ekip ve duvara tırmanan boru · ③ su kotu — S10 yükselen su platformun 3 m altında durur
DÖNGÜ KAFİYESİ    G15 ↔ G0 aynı kadraj, aynı sütun (x 922–1050): G0'da sütunun dibi kirli suda (üstten 872), G15'te turkuaz suda
                  (770); G0'da duvarın dibinde paslı platform (x ≈960), G15'te aynı yerde ışıklı yapı. Işık FARKLI, bilinçli:
                  sabah 06:30 gölgesi ↔ mavi saat. İşlev anı (şelale) kadrajda KALIR [BACK TO WATER döngü 3 dersi].
MERAK SORUSU      Buraya ne yapıyorlar?
AÇILIŞ DÜZENİ     ① NESNE kirli sulu ocak · ② DOKUNUŞ "From the first frame the hopper is already moving" (vinç) ·
                  ③ İPUCU duvarın dibindeki boş zemin + giriş terasındaki kamyon — amacı okunmaz · ④ ÖLÇEK vinç + ekskavatör +
                  iki işçi duvarın dibinde küçücük · AÇILIŞ GERİ ÇEKİLMESİ ⛔ YOK (SG — sabit geniş; 1080p'de kırpma tavanı ölçülmedi)
```

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Kirli suyla dolu ölü bir taş ocağını boşaltıp duvarının dibine cam cepheli bir yapı kurmak, çukuru turkuaz suyla
         doldurmak ve yapının salonunun önünden bir şelale akıtmak.
DİRENÇ   ① çukur (36 m duvarlar, dipte kirli su — her şey tek terastan, tek vinçle iner)
         ② su kotu (çukur dolacak ama platform, köprü ve teras kuru kalmalı)  ③ kaya duvarı (şelalenin suyu duvarın üst
         basamağından gelmek zorunda — kanal ve boru)
         EKRANDA NASIL [P1-b]:  S0 · vinçte paslı platform  ·  S1 · inen su, ortaya çıkan basamaklar  ·  S3 · havzanın
                                üstünden uzanan vinç kolu  ·  S8 · ipteki ekip  ·  S10 · platformun 3 m altında duran su
BEDEL    ⭐ Kirli, durgun su ve paslı yükleme platformu — G0'da platform duvarın dibinde (x ≈960 · üstten ≈570–650), su
         sütunun dibini örter (872); S0'da platform gider, S1'de su gider; G11'de aynı çukur turkuaz suyla dolu (770).
         Okuma bilinçli: "çukur temizlendi" değil, "ölü sanayi çukuru yaşayan bir göl ve bir yapı oldu".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            kirli su + paslı platform                                         ✅
  □ kadrajda görünüyor mu?    platform x ≈960 · su sütun dibinde 872 → 770 (turkuaz) · alt %40 bandında ✅
  □ cevap "zaman geçiyor" mu? hayır — "ölü çukur yaşayan göl oldu, şelale çalışıyor"                ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: su var mı, ne renk · yapı kaç kat, camlı mı · köprü var mı · şelale akıyor mu
② KİNETİK BAĞIMSIZLIK   ✅ her klipte makine, ekip, su ya da ışık hareket eder (vinç · pompa · ekskavatör · pompa kolu · cam ·
                           ip ekibi · bahçıvan · hortum · şelale · ışık · üç kişi)
③ BAŞLIK ŞEMASI         ✅ kapak "THE HIDDEN FALLS" (3 kelime) · ⚠️ sahip başlığı 66 karakter (kural ≤40) — YAYIN_PAKETI
④ OMURGA CÜMLESİ [P1-k] ✅ platform gider → su gider → temel dökülür → iskelet yükselir → köprü oturur → teras döşenir →
                           camlar takılır → salon döşenir → kanal ve boru → bahçe → su dolar → şelale akar → ışıklar yanar →
                           perdenin arkası → köprüde üç kişi
```

⚠️ **THE DEEP END ile aile benzerliği [P16-a]:** ikisinde de su bir çukura geri gelir. AYIRICI FARK: DEEP END'de havuz bir
salona DÖNÜŞÜR (su gider); burada su GELİR ve yapı suyun üstünde kalır, final bir şelalenin ARKASINDAN bakar. THE GLASS WALL
ile cam cephe akrabalığı: orada cam duvarın kendisidir, burada cam şelalenin arkasındaki perdedir. Ardışık yayınlanmaz.

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera (ana) · aynı salon kamerası (S7 · S13)
                          ② kanıt nesnesi: kireçtaşı SÜTUN (x 922–1050 · üstten 668 → dip 949 · 128 px · 14 ana karede birebir;
                             iki kamerada da görünür — salonda x 1347–1457)
                          ③ çapa: uzak kenar çizgisi düz (üstten 308) + çapraz pas çatlağı (494,319 → 704,598)
                          ④ çapa: şemsiye çam (sol üst x ≈155) · ⑤ çapa: yıkık taş kulübe (sağ üst x 1741–1818 · 233–284)
                          ⑥ yapı tek parça: x 751–1339 (588 px) G4 → G15 ±2 px · çatı 507 · platform 619 — yalnız camlanır, büyümez
                          ⑦ su kotu defteri: +3 (G0–G1) · kuru (G2–G10) · +7 (G11–G15) — platformun 3 m altı ASLA aşılmaz
                          ⑧ insan: A/B'de iz ("soft motion streaks") · G'de küçük figür / sırtı kameraya, yüz okunmaz
P1.5 · fırsat buldukça   kenar otu rengi (taze yeşil → saman → yeşil) · gölge süpürmesi (B: S1 · S2 · S5 · S9 · S10) ·
                          bahçenin dolgunlaşması (G10 fide → G15 tam yaprak) · yansıma bandı (G14–G15 üstten 703–808)
SPEC · yalnız belge      azimut/yükseklik dereceleri (kapı şartı) · px tabloları · salon px'leri
```

**Malzeme kimliği (her promptta):** *soluk gri kireçtaşı · koyu gri çelik · berrak cam · soluk meşe/ahşap · turkuaz su* — korpus: "documentary site photograph on colour negative film" [DERS 34 · 42].
**İnsan kararı:** ekip var — A/B'de iz; S11 iki işçi + pompa evinde biri (G, küçük, yüz okunmaz); S13 salonda bir kişi (G, sırtı kameraya); S14–G15 üç kişi köprüde (G, ≈25 px, yüz okunmaz).
**Vinç kararı [DERS 8 · 22 · 46 · 57]:** sarı paletli kafes bomlu vinç giriş terasında (x ≈268) G0–G8; kanca her karede YÜKLÜ ("with a … on the hook"): G0 platform · G1 platform kamyonda gevşek sapanlarla · G2 donatı kafesi demeti · G3 çelik demet · G4 köprü açıklığı (kaldırma kirişi) · G5 tahta paleti · G6 vakumlu cam çerçevesi · G8 boru demeti. S8'de bomunu indirip nakliye yolundan çıkar. ⚠️ Köprü İKİ 16 m açıklık + orta ayak (SAPMA ⑨) — 32 m tek parça havada taşınmaz [DERS 57].
**Korpus kararı [DERS 55]:** taş ocağı korpusu çok makineli, çok çukurludur → NEGATIVE'de her karede: "The quarry holds exactly one building site, this one, at the foot of the far wall".
**Yapı adı kararı [DERS 42 · P23-b]:** "hotel · resort · spa" (otel kulesi) → "a long two-storey building … with a double-height glass salon" · "pool" (fayanslı havuz) → "the turquoise water" · "dam / weir" (baraj) → "a straight steel lip" · "mine" → "quarry".

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0,
                 yani en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp [A7-b]; kutu tam 8,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 15 sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.
                 ⭐ ⑧ "araç ilk + son kare alıyor mu" ve ⑨ salon istasyonu için ikinci referans görsel kabul ediyor mu.

┌─ KAMERA İSTASYONU (ANA) ─────────────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 (G13–G15 ISO 800) · tam kare YATAY │
│ yükseklik     h = +16,0 m (havza tabanından) — güney duvarının dar basamağı    │
│ mesafe        D_duvar = 110,0 m (uzak duvarın dibine) · D_cephe = 98,0 m ·       │
│               D_sütun = 50,0 m · kadraj altı: taban 0 m'de 37,9 m [DERS 38]     │
│ bakış açısı   bearing 0° (kuzey) · tilt 0° · roll 0°                           │
│ sabitleme     "bolted to the rock of a narrow bench high on the south wall"   │
│ ⛔ HESAP (KILAVUZ_REHBERI §2.8 · f=24 · yatay · yüzde ALT kenardan):            │
│    yüzde(y) = 50 + 118,5·(y − h)/D         x(m, eksenden) → %50 + 66,7·x/D    │
│    ⚠️ "taç %82 → D = (H − h)/0,27" yapıya UYGULANMAZ: konu yapı değil OCAKTIR — │
│       yapı 45 m enli ama 8,5 m yüksek; taç = uzak kenar çizgisi %71,5 (308)     │
│    uzak kenar   y=+36 · D 110 → %71,5 (üstten 308) · üst basamak +30 → %64,9 (379) │
│    çatı         y=+18,5 · D 98 → %53,0 (507) · çatı dudağı +18,8 · D 96 → %53,5 (502) │
│    platform     y=+10 · D 98 → %42,7 (619) ✓ çalışma seviyesi ≥ %25             │
│    su +7 (perdenin dibi, D 96) → %38,9 (660) · kirli su +3 → %34,3 (710)         │
│    havza tabanı 0 · D 98 → %30,7 (749)                                          │
│    kanıt nesnesi SÜTUN x −1,5…+3,5 · D 50 → x 922–1050 · tepe +11 → %38,2 (668) │
│       · dip 0 → %12,1 (949) · su +7 → 770 · kirli su +3 → 872                   │
│    yapı x −16…+29 (D 98) → x 751–1339 · salon x +13…+29 → 1130–1339            │
│    perde x +19…+29 (D 96) → x 1213–1347 · 502 → 660 (158 px)                    │
│    köprü x −48…−16 (D 94) → x 306–742 · güverte +10,5 → %43,1 (615)             │
│    giriş terası x −60…−48 (D 95) → x 151–313 · +10 → 621 · vinç tabanı x ≈268   │
│    sol çapa çam x −66 · D 105 → x ≈155 · dip 296 · taç tepesi +50 → 125         │
│    sağ çapa kulübe x +61…+67 · D 100 → x 1741–1818 · 233–284 (77 × 51 px)        │
│    çatlak (−40, +35) → (−22, +11) · D 110 → (494, 319) → (704, 598)             │
│ ⛔ YANSIMA (SU_VE_YANSIMA §1 · x = D·h/(h+y), kamera suyun 9 m üstünde): çatı    │
│    (+11,5) → 43 m → üstten 808 · cam dibi (+3,5) → 70,6 m → 703 → yansıma bandı │
│    üstten 703–808 (G12–G15) · sütun (D 50) bandın x 922–1050'sini örter         │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ KAMERA İSTASYONU (SALON · ikinci istasyon · 2 klip) ─────────────────────────┐
│ "SALON STATION — fixed clamp mount bolted to the rock face at the back of the │
│  double-height glass salon, lens 12 metres above the basin floor, 10 metres   │
│  from the glass front, bearing 180 degrees, tilt 0 degrees, zero roll"        │
│ lens +12,0 (salon zemini +10,5 + 1,5) · x +21 · ufuk %50 (540) · cam dibi %32,2 │
│   (üstten 732) → cam kadrajın tüm enini %32'den yukarı kaplar                   │
│ ① çapa: sütun camdan x 1347–1457 · tepe %48,0 (561) · su %39,8 (650) — ana    │
│   SITE ile 2 ORTAK CÜMLE, birebir (kireçtaşı duvarlar + havzadaki sütun) [DERS 10] ✓ │
│ ② istasyon kendi içinde sabit ✓ · ③ iki klip, aynı istasyon ✓                 │
│ ④ dış büyüme TAŞIMAZ: S7 S8 ile AYNI on dakikadır (∥ · SAPMA ④), S13 S12'nin son│
│   sekiz saniyesidir (∥ · SAPMA ⑤); ana kare iki yakada aynı (S6 → G8 ← S8 ·     │
│   S12 → G14 ← S14) ✓ · camdan görünen dünya klip boyunca değişmez              │
│ ⚠️ iki kamera TERS yöne bakar (0° ↔ 180°) → kompozit YOK [ISTASYON §3 ②]; elle  │
│   denetim: sütun aynı biçim, aynı su kotu, aynı mevsim                         │
│ ⚠️ perde salonun yalnız sağdaki 10 m'sini örter (x +19…+29) → salondan bakınca   │
│   kadrajın SOL x 106–1173'ü; sütun açık camda (x 1347–1457)                     │
│ ⚠️ ISTASYON §1: ≤ %10 (burada 2/15 = %13) · final bölgesinde iç klip yasak      │
│   (S13 %87–93) — AŞILDI, sahip senaryosu                                       │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① ŞEMSİYE ÇAM (SOL ÜST · x ≈155 · dip 296 · taç 125) — batı kenarında, her dem │
│    yeşil (mevsimle değişmez)                                                  │
│ ② YIKIK TAŞ KULÜBE (SAĞ ÜST · x 1741–1818 · 233–284) — doğu kenarında, çatısız │
│ ③ UZAK KENAR çizgisi düz (308) + çapraz pas çatlağı (494,319 → 704,598)        │
│ ④ ⭐ SÜTUN (ORTA · x 922–1050 · 668–949) — KANIT NESNESİ, iki kamerada ortak    │
│ ⑤ nakliye yolu + giriş terası (SOL · x 0–313) — eğimli tek rampa              │
│ + "The quarry holds exactly one building site…" korpus kilidi — her NEGATIVE'de │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ tilt 0 → ufuk %50 (kenar çizgisi ufkun ÜSTÜNDE, %71,5 — kamera kenardan 20 m  │
│ aşağıda) · yapının tepesi %53 · çalışma seviyesi %42,7 ≥ %25                  │
│ yanlar: solda batı duvarı + nakliye yolu + giriş terası + köprü · sağda doğu   │
│ duvarı + basamaklı bahçe + pompa evi + boru                                   │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ (§2.8 varsayılanı) — kanıt nesnesi alt 100 px'e │
│ (üstten > 980) ve sağ üst 300×100 px'e (x > 1620 · üstten < 100) girmez ✓       │
│ ⚠️ kulübe sağ üstte ama üstten 233–284 → bilgi kartı bandının (<100) ALTINDA ✓  │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ ocak: 120 m (D-B, x ±60) × 110 m (K-G) · kenar +36 · havza tabanı 0 ·          │
│   orta basamak +4 (D 75–92) · dip basamağı +6 (D 92–110) · uzak duvarda üst     │
│   basamak +30 · doğu duvarında bahçe basamakları +14 · +20 · +26               │
│ paslı yükleme platformu: 8 × 6 m · 7 m boy · dört ayak · x 0…+8 dip basamağında │
│ temel: 49 × 20 m (x −16…+33 · D 90–110) · dip basamağı +6 → üst +10 (4 m) ·    │
│   sağ ucunda pompa evi (x +29…+33) — temel x 751–1391                         │
│ köprü ayağı: 1,5 × 1,5 m · x −32 · D 94 · orta basamak +4 → +10                 │
│ yapı: 45 × 12 m (D 98–110) · iki kat (+10,5 · +14,5) · çatı +18,5 · 15 bölme   │
│   (3 m) · sol kısım x −16…+13 (29 m, iki kat) · salon x +13…+29 (16 m, 8 m çift │
│   yükseklik) · çatı dudağı salonun üstünde camdan 2 m ileride (D 96 · +18,8)   │
│ teras: x −16…+13 × 8 m (D 90–98) · +10 · ince çelik korkuluk                   │
│ köprü: 2 × 16 m açıklık · x −48…−16 · güverte +10,5 · korkuluk 1,1 m           │
│ kanal: üst basamak +30 · x −5…+27 · çentik x +19…+29 (salonun üstü)             │
│ boru: Ø 0,6 m · x +31 (duvarda, D 110 → x ≈1321) · +10 → +30 · pompa evi 4 × 6 m │
│ şelale: kaya yüzü +30 → +18,5 (11,5 m) · çatıdan dudağa · perde +18,8 → +7      │
│   (11,8 m) · en 10 m (x +19…+29) · camdan 2 m önde                              │
│ su: kirli +3 (G0–G1) · kuru (G2–G10) · turkuaz +7 (G11–G15) → platform 3 m,     │
│   köprü 3,5 m yukarıda · dip basamağı 1 m, orta basamak 3 m su altında          │
│ bahçe: doğu basamakları 3 sıra · 3 zeytin giriş terasında (köprü başı) ·        │
│   kanal boyunca eğreltiotu · teras korkuluğunda alçak saksılar                 │
│ salon içi: 1 uzun ahşap masa + 12 sandalye · alçak kanepe + 2 koltuk (sağda)    │
│ STRUCTURE'ın İngilizce tam hâli tek cümle (DERS 36): "When finished this will be │
│   a long two-storey building with a full-height glass front, 45 metres wide,   │
│   standing on a raised concrete base against the foot of the far quarry wall,  │
│   with a double-height glass salon at its right end, a timber terrace along its │
│   front and a steel footbridge to the entrance terrace." — 18 görselde BİREBİR │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 15 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az yapı göstermez (sökümler GEÇİCİ ekipmandır; su
> iki yönlüdür: S1 iner, S10 yükselir — negatif tek yönlü su kilidi yazmaz [P16-c]). Kış görüntüsü YOK (ılıman,
> karsız — "kış İKİ sahne" kuralı tetiklenmez). ∥ = salon klibi, komşu ana klibin AYNI zamanı.

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | İSTASYON | KANIT NESNESİ (px) |
|:-:|:-:|---|---|---|:-:|:-:|:-:|---|
| 0 | 8,0 | KALDIRIR | paslı yükleme platformu dipte → vinçte → kamyonda (%100) | 1 gün | A | 06:30→06:40 | ANA | platform x ≈960 → giriş terası (x ≈268) |
| 1 | 8,0 | BOŞALTIR | kirli su +3 → taban (su birikintisi) · basamaklar %0 → %100 görünür | 3 hafta | B | 06:40→08:40 | ANA | sütun dibinde su 872 → kuru 949 |
| 2 | 8,0 | DÖKER | yükseltilmiş temel 0 → %100 · köprü ayağı 0 → 1 | 1 ay | B | 08:40→10:40 | ANA | temel üstü 619 · x 751–1391 |
| 3 | 8,0 | DİKER | çelik iskelet 0 → %100 (iki kat · sağ uç çift yükseklik) | 6 hafta | A | 10:40→10:50 | ANA | iskelet tepesi 619 → 507 |
| 4 | 8,0 | YERLEŞTİRİR | köprü açıklığı 0 → 2 (terastan ayağa, ayaktan temele) | 1 hafta | A | 10:50→11:00 | ANA | köprü x 306–742 · 615 |
| 5 | 8,0 | KAPLAR | ahşap teras %0 → %100 (soldan sağa) · çatı kapanır · istif → 0 | 4 hafta | B | 11:00→13:00 | ANA | teras x 751–1130 · istif → 0 |
| 6 | 8,0 | CAMLAR | cam cephe %0 → %100 (önce salon, sonra sağdan sola) · yansıma | 4 hafta | A | 13:00→13:10 | ANA | cam bölme 0 → 15 |
| 7 | 8,0 | DÖŞER | salon: boş → masa + 12 sandalye + oturma grubu (%100) | 1 hafta | A | 13:10→13:20 ∥ | SALON | salon: boş → masa + oturma |
| 8 | 8,0 | YOLLAR | üst basamak kanalı %0 → %100 · boru pompa evinden kanala · vinç gider | 3 hafta | A | 13:10→13:20 | ANA | kanal (379) · boru x ≈1321 (çatının üstünde) · vinç → 0 |
| 9 | 8,0 | DİKER ② | bahçe: doğu basamakları 0 → 3 sıra · zeytin 0 → 3 · eğreltiotu | 3 hafta | B | 13:20→15:20 | ANA | doğu basamakları gri → yeşil şerit |
| 10 | 8,0 | DOLDURUR | su taban → +7 m (%100) · orta basamak + sütun dibi batar · platform kuru | 3 ay | B | 15:20→17:20 | ANA | ⭐ sütunda su dipten → 770 (turkuaz) |
| 11 | 8,0 | AKAR | şelale: kuru → kanal → kaya → çatı → perde → su (%100) | 8 sn | G | 17:20 (+8 sn) | ANA | ⭐ perde 502 → 660 · x 1213–1347 |
| 12 | 8,0 | YANAR | gün batımı → mavi saat · ışıklar tek karede · 3 kişi köprü ucuna | 1 akşam | B | 17:20→19:20 | ANA | ışık 0 → hepsi · yansıma 703–808 |
| 13 | 8,0 | IŞIR | salon içi: perde akar · masa hazır · bir kişi okur | 8 sn | G | 19:20 (−8 sn → 0) ∥ | SALON | perde salonun sol x 106–1173'ü |
| 14 | 8,0 | DURULUR | üç kişi köprü ucundan 5 m içeri, korkulukta durur (final tutuş) | 8 sn | G | 19:20 (+8 sn) | ANA | kişiler x 688 → 619 · tutuş |

```
IZGARA          8,0 sn × 15 · kesmeler 8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn) · müzik YOK (BPM ızgarası yok)
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: sahibin kendi senaryosu (15 × 8,0 = 2:00, 08.10.2026) ve yatay_2 README'deki sahip
                       izinli 15 × 8,0 varyantı (16.09.2026); emsal THE OLD ROAD (15 × 8,0) · THE SLOW TAKEOFF (30 × 8,0).
                       ⚠️ BANDIN DIŞI: format 12 × 10,0.
                   (b) ritim klip İÇİNE: ① rejim nabzı — B'ler S1 · S2 · S5 · S9 · S10 · S12 (gölge süpürmesi, su), G'ler
                       S11 · S13 · S14 (gerçek hız — su ve insan); ② iş yönü değişir: yana (S0 platform) · aşağı (S1 su) ·
                       yukarı (S3 iskelet · S8 boru · S10 su) · soldan sağa (S5 teras) · sağdan sola (S6 cam) · aşağı (S11
                       şelale) · ③ ses katmanı = aşama (MUZIK.md SES TABLOSU) ④ istasyon nabzı: iki salon klibi (S7 · S13).
                   (c) kabul edilen risk: eşit klipte ❷ RHYTHM kategorisi NOT TRIGGERED (beş mercekli rubrik) — sapma
                       kurgudan gelirse (klip ≠ 8,0) ❷ açılır ve ❺ final saniyesi kayar [IRON BRIDGE · GLASS WALL].
                       Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
REJİM SAYISI    ⚠️ ÜÇ rejim (A · B · G) — SANTIYE_HAREKETI §2 sınırı iki. Gerekçe: B gölge süpürmesini ve suyun inip
                çıkmasını taşır [A12-j], G senaryonun "hareketi su sağlar" isteğidir (şelalenin başlaması gerçek hızda
                okunur); geçişler KESMEDE (S10 → S11 · S11 → S12 · S12 → S14) [P5-c]. Emsal: THE SLOW TAKEOFF (A+B+G, beyanlı).
IŞIK GÜNÜ       Σ pencere = 5 A × 10 dk + 6 B × 2 sa + 2 G × 8 sn = 50 dk + 12 sa ≈ 12 sa 50 dk ≤ 14 ✓
                (salon klipleri S7 ∥ S8 · S13 ∥ S12 sonu — toplama girmez) · 06:30 → 19:20 (mavi saat, güneş −5,8°)
BÖLÜM SINIRI    G9 — sahne S8 son karesi = sahne S9 ilk karesi (ANA istasyon); kanal ve boru tamam, vinç yok, havza kuru,
                gölge +43°, yaz sonu — ikisinde de aynı [DERS 52]. Salon klibi S7 sınıra DÜŞMEZ (SAPMA ⑩).
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: kireçtaşı SÜTUN — G0'da ve usta karede (G15) aynı konum (x 922–1050) ve aynı boy (128 px en ·
        tepe 668) [DERS 25]; dibi G0–G1 kirli suda (872), G2–G10 kuru (949), G11–G15 turkuaz suda (770). Gövdesi değişmez.
        İki kameranın ortak nesnesidir (salonda x 1347–1457). Yedek: yıkık kulübe x 1741–1818 · şemsiye çam x ≈155.
LOOP    G15 ↔ G0: aynı kadraj · aynı çapalar · aynı sütun · ışık FARKLI (bilinçli — G0 06:30 sabah gölgesi, G15 mavi saat;
        tek gün): duvarın dibinde paslı platform / aynı yerde ışıklı yapı. Biçim kafiyesi: sütunun dibi kirli su (872)
        → turkuaz su (770); havzanın rengi kahverengi-yeşil → turkuaz.
SÖKÜM   S0 paslı platform (vinç → kamyon → nakliye yolu, S1) · S1 pompalar ve hortumlar (S2'de dürülü, S3'te yok) · S3
        kalıp kerestesi (vinç kamyona yükler) · S5 tahta ve panel istifleri · S6 cam sandıkları ve kamyonlar · S8 VİNÇ
        (bomunu indirir, nakliye yolundan çıkar) · S9 bitki paletleri ve kamyon · S10 dolum hortumları (römorka) · S12 son
        aletler (araba + kamyon) — ekranda gider; temel, köprü ayağı, kanal, boru, pompa evi KALIR (kalıcı) [DERS 48 · P2-h]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
paslı platform (giden)    → vinç kancası → düz kasalı kamyon (giriş terası)                 → G0 · G1
kirli su (giden)          → iki dizel pompa (orta basamak) → hortum → nakliye yolu           → G1
temel betonu, donatı       → vinçte donatı kafesi demeti · beton pompa kamyonu (giriş terası) → G2
çelik iskelet              → iki uzun kamyon (giriş terası) · vinç                            → G3
köprü açıklıkları          → giriş terasında kaldırma kirişli iki açıklık istifi               → G4
teras tahtası, çatı paneli → temelin önünde tahta istifleri + panel demetleri                 → G5
cam                        → iki kamyonda yüksek cam sandıkları · vakumlu kaldırma çerçevesi   → G6
salon mobilyası            → yan kapının yanında sarılı mobilya yığını (salon istasyonu)      → G7
kanal betonu, boru         → üst basamakta ekip · vinçte boru demeti · pompa evi              → G8
bitki, zeytin, toprak      → giriş terasında paletler · kök topu sarılı üç zeytin · küçük kamyon → G9
dolum suyu                 → kenardaki pompa kamyonundan iki büyük hortum (nakliye yolu)      → G10
şelale suyu                → gölden pompa evi → boru → kanal → çentik → kaya → çatı → dudak     → G11 · S11
GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL (prompta yalnız vekil girer):
   sol kısmın iç döşemesi → S12 iki katın camlarında yanan ışık · salonun döşenmesi → SALON İSTASYONU (S7) ·
   elektrik → S12 ışıklar tek karede · su devridaimi → pompa evi + boru (S8) + S11 vanayı açan işçi ·
   temel ankrajı → temel üstündeki ankraj civataları (G3)
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① perdenin arkasında ışıklı salon (x 1130–1339 · 507–619 — ilk okunan, en sıcak) → ② şelale perdesi ve köpüğü
   (1213–1347 · 502–660) → ③ cam cephenin ışığı ve suda yansıması (üstten 703–808) → ④ köprüde üç kişi (x ≈619 · 25 px)
   → ⑤ basamaklı bahçe + sütun (kanıt)
FİNAL KARE KANITI  ffmpeg -ss 119.0 -i teslim.mp4 -frames:v 1 kanit.jpg   (S14 tutuşu 116,0–120,0 içinde · mavi saat,
                   okunur [DERS 45]) · kart YOK → son kare = G15
```

---

## 🖼️ KARE TABLOSU — 14 ana görsel + 2 salon ilk + 2 salon son karesi [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Gölge yönü kadrajda: 0 = kameradan uzağa · − sola · + sağa (|x| > 90 = kameraya doğru). Güneş DİSKİ anılmaz.
> 🪟 = SALON istasyonu. S6 I2V'si G8'e, S12 I2V'si G14'e biter (ana); G7 → G7′ ve G13 → G13′ salon klibi.
> Sayılar `bolum_uretici.py --tablo` çıktısıdır (38° K · δ +15° · güneş saati).

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| G0 | 06:30 | 82° | 15,0° | -98° | soluk sabah, küçük yüksek bulut | ilkbahar başı · kenar otu taze yeşil, sarı çiçek | ⭐ AÇILIŞ — kirli su +3 · paslı platform vinçte |
| G1 | 06:40 | 84° | 16,9° | -96° | aynı | aynı | platform kamyonda · pompalar suya hortumlu |
| G2 | 08:40 | 104° | 40,4° | -76° | açık, küçük bulut | aynı | havza kuru · temel kazıklı · vinçte donatı |
| G3 | 10:40 | 137° | 61,0° | -43° | açık mavi, küme bulut | yaz başı · ot yeşil-altın | temel + ayak · vinçte çelik |
| G4 | 10:50 | 141° | 62,3° | -39° | aynı | aynı | ⭐ çelik iskelet tamam (00:32) · iki köprü açıklığı terasta |
| G5 | 11:00 | 146° | 63,5° | -34° | aynı | aynı | köprü yerinde · tahta istifleri |
| G6 | 13:00 | 214° | 63,5° | +34° | puslu soluk mavi | yaz · ot saman sarısı | teras + çatı · cam sandıkları |
| G7 | 13:10 | 219° | 62,3° | salon içi (camdan ışık bandı) | aynı (salondan) | yaz (camdan, kuru havza) | 🪟 salon camlı, boş · mobilya kapıda |
| G7′ | 13:20 | 223° | 61,0° | salon içi (camdan ışık bandı) | aynı | aynı | 🪟 salon döşeli (masa · 12 sandalye · oturma) |
| G8 | 13:10 | 219° | 62,3° | +39° | aynı | aynı | cam cephe tamam · kanal başladı · vinçte boru |
| G9 | 13:20 | 223° | 61,0° | +43° | puslu, birkaç yüksek bulut | yaz sonu · ot saman | ⭐ BÖLÜM SINIRI — kanal + boru tamam · vinç yok · bitkiler terasta |
| G10 | 15:20 | 256° | 40,4° | +76° | yağmur sonrası, dağınık bulut | sonbahar · ilk yağmur izleri, ot dipten yeşerir | bahçe dikili · havza kuru · hortumlar hazır |
| G11 | 17:20 | 276° | 16,9° | +96° | açık, birkaç küçük bulut | ilkbahar · ot yeşil, bahçe yaprak açıyor | ⭐ havza turkuaz +7 · kanal kuru |
| G12 | 17:20 +8 sn | 276° | 16,9° | +96° | aynı | aynı | ⭐ şelale akıyor · ışıklar sönük |
| G13 | 19:20 −8 sn | 294° | −5,8° | salon içi (güneş yok) | derin mavi (salondan) | yaz başı (camdan) | 🪟 salon: perde akar · masa hazır · bir kişi |
| G13′ | 19:20 | 294° | −5,8° | salon içi (güneş yok) | aynı | aynı | 🪟 aynı, sekiz saniye sonra |
| G14 | 19:20 | 294° | −5,8° | — (güneş ufkun altında) | derin mavi saat | yaz başı · bahçe tam yaprak | bütün ışıklar yanık · üç kişi köprü ucunda |
| G15 | 19:20 +8 sn | 294° | −5,8° | — (güneş ufkun altında) | ⭐ derin mavi saat | aynı | ⭐ USTA KARE — üç kişi korkulukta · şelale · yansıma |

```
SU KOTU (kare kilidi [P10-e])   G0–G1 kirli su +3 (orta basamak 1 m, dip basamağı 3 m kuru; sütunun dibi 872) ·
   G2–G10 KURU (su birikintisi; duvarlarda +3'te soluk kir çizgisi) · S10 dolum (milky grey → turkuaz) · G11–G15 +7
   (dip basamağı 1 m, orta basamak 3 m su altında; platform 3 m, köprü güvertesi 3,5 m üstte; sütun tepesinin 4 m altı)
   ⛔ +7 ASLA aşılmaz — "the water stands about three metres below the top of the raised base" her dolu karede
   TANIK ÇİZGİ [P10-g]: G2–G10 duvarlarda +3 kir çizgisi (kuru) · G11–G15 o çizgi SU ALTINDA → yazılmaz; yerine su
   çizgisinin hemen üstünde ince ıslak kaya bandı
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G15 usta kare → G14 (kişiler köprü ucunda) → G12 (ışıklar sönük, gün batımı öncesi) → G11 (şelale yok, kanal kuru) →
   G10 (su yok, hortumlar) → G9 (bahçe yok) → G8 (kanal yarım, vinç geri) → G6 (cam yok) → G5 (teras yok) → G4 (köprü
   terasta) → G3 (iskelet yok) → G2 (temel yok) → G1 (kirli su) → G0 (platform dipte)
   SALON: G7′ önce (G8–G9 dünyası: kuru havza, yaz) → G7 (mobilya kapıya geri) · G13′ G14'ün ışığıyla → G13 (perdenin
   kıvrımları, sayfa) — G13′ salon dokusu G7′'den türetilir (aynı oda, mobilya aynı yerde). Salon kareleri ana zincire
   zincir_kontrol ile BAĞLANMAZ (başka istasyon).
   sonra I2V S0 (G0→G1) … S14 (G14→G15) — her klip iki uca kilitli, üretim 9,0 sn, baştan 1,0 kırp
```

## 🧪 PİLOT ÜÇLÜ [DERS 62 · KILAVUZ_REHBERI §8 adım 2b]

```
⛔ Üretim başlamadan, aşağıdaki üçü geçmeden kalan klipler üretilmez:
① FİNAL      G15 + G14 + S14 — mavi saat, perdenin arkasında ışıklı salon, yansıma, gerçek hızda üç kişi ve 4 sn tutuş [C1-b]
② EN BÜYÜK   G11 + G12 + S11 — şelalenin başlaması gerçek hızda: su önü kanaldan kayaya, çatıdan dudağa, perde suya ≈6 sn'de;
   DEĞİŞİKLİK  yapı, köprü, sütun ve gölgeler kıpırdamaz · S11 = 01:28
③ DİRENEN    G10 + G11 + S10 — dolum: su +7'de DURUR, platform ve köprü kuru, yapı GERİLEMEZ [IRON BRIDGE 00:51 dersi] ·
              + salon S13 (istasyon değişimi, ❶ SEPARATE IMAGES riski; perde iki kamerada aynı yerde)
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     38,0° K · ışık günü tarihi: δ +15° (ışık tek gün; takvim sahadan) · doğuş 05:12 · batış 18:48 (güneş
                saati) · kamera bakışı 0° (kuzey) → kadraj −37° … +37° · güneş 82° → 294°: sabah sağda (doğu kenarının
                ardında, havza gölgede), öğle arkada (uzak duvar ve cephe aydınlık), akşam solda (batı kenarının ardında) —
                HİÇBİR karede kadrajda değil [P8-h]
                ⚠️ salon istasyonu güneye (180°) bakar: S7'de güneş 219°–223°, +61° — kadrajın ÜSTÜNDE (dikey yarı açı 22,9°),
                yalnız camdan zemine ışık bandı düşer · S13 mavi saat, güneş −5,8°
GÖLGE           doğu duvarının gölgesi sabah havzayı örter (06:30 · 36 m / tan 15° = 134 m — havzanın tamamı); batı duvarının
                gölgesi 17:20'de 118 m (su seviyesinde 95 m → yalnız doğu kenarı güneşte) · S12'de güneş batar
GÖLGE SÜPÜRMESİ rejim B klipte: S1 (−96° → −76°: 20°) · S2 (−76° → −43°: 33°) · S5 (−34° → +34°: 68°) · S9 (+43° → +76°: 33°) ·
                S10 (+76° → +96°: 20°) · S12 (+96° → güneş batar) · rejim A klipte fark edilmez → yüzeyle kanıtlanır
MEVSİM YAYI     ilkbahar başı (G0–G2: kenar otu taze yeşil) → yaz (G3–G9: yeşil-altın → saman) → sonbahar (G10: ilk yağmur,
                kayada ıslak izler, ot dipten yeşerir) → ilkbahar (G11–G12: ot yeşil, bahçe yaprak açar) → yaz başı (G13–G15:
                bahçe tam yaprak) · taşıyıcı: KENAR OTU (ana) · bahçe · su kotu · iş — şemsiye çam her dem yeşil (çapa)
KIŞ             görüntü YOK (ılıman, karsız) — dolum kış yağmuru + pompayla S10'da (temsil 3 ay) · DERS 7 tetiklenmez
GECE            yok · final MAVİ SAAT, güneş −5,8° (G13–G15) — senaryo "Akşam olur" · zifiri değil: yapı, perde, yansıma ve
                köprüdeki üç kişi okunur, ışıklar kadrajın en parlak kaynağı [DERS 45]
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   ANA: h +16,0 · D_duvar 110,0 · D_cephe 98,0 · bakış 0° · tilt 0 · roll 0
         SALON: h +12,0 · cama 10,0 m · x +21 · bakış 180° · tilt 0 · roll 0 (yalnız S7 · S13)
YAPI     temel x 751–1391 · yapı x 751–1339 · üst 619 · çatı 507 · salon 1130–1339 · perde 1213–1347 · 502 → 660 · köprü 306–742 · 615
ÇAPALAR  ① çam x ≈155 · 125–296 · ② kulübe x 1741–1818 · 233–284 · ③ kenar 308 · çatlak (494,319) → (704,598) ·
         ④ SÜTUN x 922–1050 · 668 → 949 (kanıt nesnesi 128 px)
SU       +3 (G0–G1) · kuru (G2–G10) · +7 (G11–G15) → üstten 710 · — · 660 (perde dibi) · sütunda 872 · 949 · 770
IZGARA   15 × 8,0 · kesmeler 8,0 · 16,0 · … · 112,0  (14 kesme, her 8,0 sn) · kart YOK · 120,0 sn
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_HIDDEN_FALLS   → sonuç QA_SPEC §8'de (08.10.2026)
✅ FIX'ler ve beyanları (hepsi elle okundu):
   · ARAÇ KUTU SETİ ölçülmedi — beyanlı; üretim araç kapısıyla açılır
   · süreler eşit (8,0) — sahip ızgarası; beş mercekte ❷ RHYTHM eşit klipte tetiklenmez
   · S11 (şelale başlar) · S13 (salon, perde) · S14 (final): ACTIVITY'de ≥3 el / geçişli fiil / malzeme akışı eksik —
     KASITLI: bunlar ödül ve sakin anlardır, şantiye bitti [P4-f · C1-d]; ❸'e PARKED gerekçesi SPEC §5 DECLARED WORLD'de
   · DERS 61 "YENİ eleman" ×2 (S7 → G8 · S13 → G14) — YANLIŞ ALARM: kapı salon karesini (G7 · G13) bir sonraki ANA kareyle
     karşılaştırıyor; o elemanlar ana zincirde G4–G6'dan beri var (THE SLOW TAKEOFF'taki aynı yanlış alarm)
✅ YASAK KELİME taraması 0 · kelime kilitleri (crane G0–G8 · turquoise S10+ · waterfall S11+) betikle doğrulandı
✅ 00_ANALIZ altı dosya · hikâye onayı 08.10.2026 (TUR 1 · SAPMA ①–⑭ sahip okur)
⛔ ARAÇ KAPISI koşulmadı → THE_HIDDEN_FALLS_URETIM_GUNLUGU.md §0
⛔ PİLOT ÜÇLÜ koşulmadı → S14 · S11 · S10 (+ S13)
```
