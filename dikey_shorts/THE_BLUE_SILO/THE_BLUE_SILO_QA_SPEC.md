# 🔬 THE BLUE SILO — QA SPEC

```
⛔ Bu dosya PLANIN DEĞİL, TESLİMİN kapısıdır. Her madde TEK KAREDE ya da TEK KLİPTE ölçülür.
   Ölçülemeyen bir madde bu dosyaya yazılmaz.
KAYNAK  dikey_shorts/THE_BLUE_SILO/THE_BLUE_SILO_DIKEY_TIMELAPSE.md
IZGARA  6 × 8,0 = 48,0 sn · 7 görsel (G0–G6) + 6 I2V · ⭐ REJİM B × 5 → G × 1 (saat son kesmede durur)
SCENE BLOCK / END CARD   48,0 sn sahne bloğu · ⛔ KAPAK KARTI YOK
DURUM   ⛔ ÜRETİLMEDİ — hiçbir madde henüz KOŞULMADI
```

---

## 1. ⭐ FİNAL KARE KANITI — 47,95 sn (S5'in son karesi)

```
KOMUT    ffmpeg -ss 47.95 -i teslim.mp4 -frames:v 1 kanit.jpg
O KAREDE GÖRÜNMESİ GEREKEN — yedisi birden:
  ① ⭐ tank DOLU ve içeriden TURKUAZ ışıyor: su yüzeyi yakın yüzde üstten 364 ± 4 · silo x 212 → 720 (508 ± 4 px)
  ② ⭐ GÜMÜŞ SÜRÜ tankın İÇİNDE, resifin çevresinde halka: üstten 1038 → 1270 bandında, x ≈ 300 → 640
  ③ ⭐ PASLI TAÇ: koni makasları pas renginde, tepe halkası x 469 · üstten 302
  ④ 18 açık gri çember — alt üç çember arası 44 ± 4 px, en üst arası 132 ± 4 px · kenar galerisi tepede
  ⑤ beyaz tanker sağda (x 753 → 887), hortumu dipteki ağza (x 627 · üstten 1372) bağlı
  ⑥ kalabalık x 233 → 694, başlar üstten ≈ 1385, HEPSİNİN sırtı kameraya; mavi saat, rıhtım ve ambar OKUNUR (DERS 45)
  ⑦ üç çapa yerinde: rıhtım kenarı (üstten 1570) · tuğla ambar (mahya 992) · ufuk %50 ve liman feneri (x 796)
⛔ Yedisinden biri yoksa FİLM TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.
⛔ TUTUŞ YOK: bu filmin finali HAREKETİN KENDİSİDİR (rejim G · P5-a). Kanıt karesi son karedir ve G6'nın
   birebir kendisidir; sürü bu karede halka hâlinde olmalıdır.
```

---

## 2. ⭐ SÜRÜ KAPISI — filmin ödülü, üretimin İLK sınavı (S5 · pilot)

```
NEREDE   S5 (G5 → G6). Sürü G0–G5'te YOKTUR; yalnız S5'te, yalnız dipteki ağızdan gelir.
  ① KAYNAK TEK: sürü yalnız giriş ağzından (x 627 · üstten 1372) çıkar. Tankın başka bir yerinde beliren balık,
     yukarıdan inen sürü ya da ilk karede zaten içeride duran sürü = klip düşer [P3-c · DERS 48 · 49].
  ② ⭐ HİÇ BALIK TANKIN DIŞINDA DEĞİL: havuz suyunda, rıhtımda ya da gökte balık = klip düşer.
  ③ SIRA: 0,0–1,0 sn tank BOŞ · ≈ 1,0 vana · 1,5–4,0 gümüş akıntı ağızdan yukarı ve yana açılır · 4,0–8,0 halka
     ve yavaş dönüş (ön yüzde soldan sağa). ⛔ Sürü yön değiştirip geri giderse ya da dağılıp kaybolursa düşer.
  ④ YÜKSEKLİK: 8,0'de sürü alt üçte birdedir (üstten 1038 → 1270). Tankın üst yarısını dolduran sürü = hız fiziği
     ihlali (kefal ≈ 1 m/sn · 6,5 sn) → klip düşer.
  ⑤ SAYI KESİRSİZ: sürü bir BULUTTUR; tek tek balık sayılmaz. Ama G5'te sıfırdır, S5 boyunca kesin artar ve
     ⛔ hiçbir karede azalmaz.
⭐ KORPUS KONTROLÜ: "aquarium|crane|oil tank|elevator|ship" desenleri yedi görselin ve altı I2V'nin İNGİLİZCE
   metninde 0 olmalı (plan Türkçesinde DEĞİL — orada uyarı olarak geçer).
   ⭐ KOŞULACAK (yalnız PROMPTLAR bölümünün kod blokları):
      sed -n '/^# 🎥 PROMPTLAR/,/^# 🎞️ KURGU/p' <plan.md> | awk '/^```$/{f=!f;next} f' \
        | grep -ciE "(^|[^a-z])(aquariums?|cranes?|oil tanks?|elevators?|ships?)([^a-z]|$)"     → 0
   ⭐ "fish" yalnız 2 blokta (12 = S5 I2V · 13 = G6):
      sed -n '/^# 🎥 PROMPTLAR/,/^# 🎞️ KURGU/p' <plan.md> \
        | awk '/^```$/{f=!f; if(f) n++; next} f && tolower($0) ~ /(^|[^a-z])fish(es)?([^a-z]|$)/ {print n}' | sort -u   → 12 13
   ⭐ POZİTİF KONTROL [P23-f]: aynı komut "silos?" ile 13 blok buluyor (bilinen pozitif) — desen çalışıyor.
      "trucks?" ile 6 blok: 1 · 6 · 10 · 11 · 12 · 13 (G0 forklift · S2 kamyonlar · S4 · G5 · S5 · G6).
⛔ YEDEK: S5 tutmazsa KAPSAM DARALIR — G5'te sürü ZATEN içeridedir, S5 yalnız dönüşü gösterir; "ilk giriş" vuruşu düşer
   (sahip kararı).
```

---

## 3. ⭐ ŞEFFAF PANEL KAPISI — ikinci pilot (S3) [DERS 49 · 57 · P15-g]

```
NEREDE   S3 (G3 → G4).
  ① KAYNAK KADRAJDA: G3'te sol apronda sandıklar (x 7 → 193 · üstten ≈ 1414). G4'te boş, yassı istif.
  ② SIRA ALTTAN YUKARI: sekiz sıra, her biri ≈ 0,9 sn; her sıranın 16 bölmesi birlikte kapanır. Camın üst kenarı
     1402 → 1269 → 1137 → 1004 → 872 → 739 → 607 → 474 → 342. ⛔ Yukarıdan aşağı ya da atlayarak = düşer.
  ③ ⛔ SAYDAMLIKTAN BELİRME YOK: her sıra siyah kauçuk derzi ve gök yansımasıyla birlikte, platformun geçişiyle gelir.
     Derzsiz, yansımasız, "sisle" beliren cam = klip düşer.
  ④ ⭐ SON PANEL ≈ 7,0 sn: en üst sıra, ön bölme (x 452 çevresi). Kanıt karesi: S3 7,0 ve 7,5 sn.
  ⑤ PLATFORM: 7,2–8,0 sn saçağın altında cıvatalanır; halatlar çözülür. G4–G6'da galeri tepededir (üstten 372).
⛔ YEDEK: S3 tutmazsa KAPSAM DARALIR — G3'te alt dört sıra ZATEN camlıdır; S3 yalnız üst dört sırayı gösterir.
```

---

## 4. ⭐ DEFTER KAPISI — ÇALIŞAN KENAR + ÇEMBER SIKLIĞI + PAS YIĞINI

```
ÇALIŞAN KENAR (yakın yüz, üstten px) — her klipte TEK kenar, TEK yön
  klip  kenar                    G(n)    G(n+1)   yön    tolerans
  S0    pasın üst kenarı         342  →  1402     ⬇      ±6
  S1    boyanın üst kenarı       1402 →  342      ⬆      ±6
  S2    yeni çemberlerin alt ucu 342  →  1357     ⬇      ±4   (çember 9 → 18)
  S3    camın üst kenarı         1402 →  342      ⬆      ±6
  S4    ⭐ su seviyesi           1380 →  364      ⬆      ±4
  ⛔ DÜŞME ① kenar klip içinde ters yöne gider (pas geri gelir · boya iner · su düşer) → klip düşer.
  ⛔ DÜŞME ② bir klipte İKİ katman değişir (ör. S3'te su görünür, S4'te cam eklenir) → klip düşer.

ÇEMBER SIKLIĞI (G3–G6 · yakın yüz) — filmin DİRENÇ kanıtı
  yeni çemberler üstten   1357 · 1313 · 1225 · 1181 · 1092 · 1048 · 938 · 805 · 673
  eski kuşaklar üstten    1402 · 1269 · 1137 · 1004 · 872 · 739 · 607 · 474 · 342
  ⭐ ÖLÇÜM: en alttaki üç çember aralığı (1402→1357→1313) ≈ 44 px · en üstteki aralık (474→342) 132 px.
  ⛔ Çemberler EŞİT aralıklıysa (model ortalaması) DİRENÇ kanıtı düşer → G3 yeniden üretilir.

PAS YIĞINI (BEDEL)
  kare        G0   G1   G2   G3   G4   G5   G6
  yığın       —    ✓    ✓    —    —    —    —      (x 97 → 245 · üstten 1379 → 1453)
  sandık      —    —    —    ✓    yassı yassı yassı
  ⛔ G3'ten sonra apronda pas yığını görülürse kare düşer. ⛔ Sandık G2'de görülürse kaynak ERKEN gelmiştir.

PASLI TAÇ — yedi karede AYNI
  ⛔ Koni makasları G0–G6'nın hepsinde PAS rengindedir ve yerindedir (tepe halkası x 469 · üstten 302 ± 3).
     S1'de griye boyanırsa ya da S0'da sökülürse kare düşer [Tasarım ① · RİSKLER ⑨].
```

---

## 5. ⭐ IŞIK VE ZAMAN KAPISI — iki saat

```
S0–S4 — GÖLGE SÜPÜRMESİ (rejim B)
  kare   saat    azimut   yükseklik   gölge (kadrajda: 0 uzağa · − sol · + sağ)
  G0     09:00   112,0°   42,1°       −83° · silonun gölgesi ambarın çatısında
  G1     11:00   150,5°   59,3°       −45°
  G2     13:00   209,5°   59,3°       +15° · ön yüz TAM önden aydınlık
  G3     15:00   248,0°   42,1°       +53°
  G4     17:00   270,6°   20,1°       +76° · boş camın sol yarısı altın, sağ yarısı mavi
  —      18:53   288,9°   −0,8°       batış — S4 içinde ≈ 7,3 sn
  ⛔ DÜŞME ① gölge yönü hiçbir karede geri dönmez (soldan sağa monoton).
  ⛔ DÜŞME ② B kliplerinde gölgeler DONMAZ [DERS 47].
  ⛔ DÜŞME ③ taban ışığı batıştan ÖNCE yanarsa (S4 7,3 sn'den önce) ışık sırası yanlıştır.

S5 — SAAT DURUR, SÜRÜ SAYILIR (rejim G)
  G5  güneş −2,0° · ışık 1 · sürü 0      G6  güneş −2,0° · ışık 1 · sürü halka
  ⛔ DÜŞME ④ S5'te gök rengi değişirse saat durmamıştır — rejim kaçağı.
  ⭐ DÜŞME ⑤ G6'da rıhtım, ambar ya da kalabalık siyah siluetse film düşer [DERS 45].
⛔ GÜNEŞ HİÇBİR KAREDE KADRAJDA DEĞİL (azimut 112° → 290°, kadraj 352,1° … 37,9°) [DERS 32 · 39].
```

---

## 6. ⛔ G5 = G6 KİMLİĞİ — kapak kanıtının kendisi

```
ARADA SEKİZ SANİYE VAR. Altı şey BİREBİR aynı olmalı:
  ① silo, 16 dikme, 18 çember, 8 sıra panel, paslı koni, galeri (±2 px)
  ② su seviyesi (364), resif, kum, yosunun yeri; turkuaz ışık
  ③ ışık: gök koyu mavi, solda soluk turuncu pay — kararmaz
  ④ tanker ve hortum (x 753 → 887 · ağız x 627)
  ⑤ ÜÇ ÇAPA ±2 px: rıhtım kenarı · tuğla ambar · ufuk ve liman feneri
  ⑥ kalabalığın KONUMU (x 233 → 694)
İZİN VERİLEN DÖRT FARK — başka hiçbiri değil:
  ⓐ sürü (0 → halka)
  ⓑ vanadaki işçinin duruşu
  ⓒ kalabalıkta birkaç kolun kalkması
  ⓓ yosun salınımı ve havuz dalgacıkları
⛔ Beşinci bir fark varsa kapak kanıtı düşer [DERS 30].
⭐ KOŞ:  bash araclar/zincir_kontrol.sh g6_kaynak.jpg kapak.png   → çıkış 0 olmalı
```

---

## 7. KADRAJ KİLİTLERİ — ±2 px [sahip kararı 19.09.2026]

```
⭐ SIRA ÖNEMLİ: önce ÜÇ ÇAPAYA bak. Üçü tutmuyorsa geri kalanı ölçme, İSTASYON oynamıştır.
  ① RIHTIM KENARI         %18,24 (üstten 1570) · kenardan kenara · demir babalar
  ② TUĞLA AMBAR           x 0 → 212 · mahya 992 · saçak 1102
  ③ UFUK + LİMAN FENERİ    %50,00 (960 px) · EĞİM SIFIR · fener x 796, üstten 969 → 1003
SONRA yapı kilitleri:
  silo dış çizgisi        x 212 → 720 (508 px) · yakın taban 1402 · yakın saçak 342 · teğet saçak 437
  koni tepe halkası       x 469 · üstten 302
  ön dikme                x 452 · bölme 121 px
  platform                tepe güverte 381 · dip güverte 1385
  resif tepesi (G2+)      üstten 1067 · x 284 → 668
⛔ GÜVENLİ ALAN: kanıt nesnelerinin hiçbiri üstten 254'ün üstüne, x 122'nin soluna ya da x 864'ün sağına geçmez.
   ⚠️ Beyanlı üç sınır: kalabalığın ayakları (1472) alt çeyrekte · tanker sağ ucu x 887 · pas yığını tabanı 1453.
⛔ HAVUZ SU SEVİYESİ KİLİT DEĞİLDİR ama SABİTTİR: Karadeniz'de gelgit ≈ 10 cm; rıhtım kenarının altındaki su hattı
   yedi karede aynı yerdedir (> 3 px oynarsa kare düşer).
```

---

## 8. YÜK YOLU VE FİZİK KAPISI [FIZIK_VE_AGIRLIK · DERS 8 · 46 · 57]

```
  PLATFORM   güverte → dört gergin tel halat → saçağa cıvatalı konsol kirişler → saçak kuşağı → dikmeler → taban
             ⛔ G0–G3'te halatlar her karede görünür ve GERGİNDİR (G1 ve G3'te platform dipte, halatlar gevşek
             değil — platform apronun hemen üstünde ASILI durur). G4'ten sonra halat yoktur: galeri dikmelere cıvatalı.
  S0         sac → bulon sökülür → platform güvertesi → forklift → sol apron (yığın)
  S1         kaya → yükleyici kovası → açık bölme → taban (resif) · kum → yükleyici → taban · boya → platform → dikme
  S2         çember parçası → platform → dikmelerin iç yüzü (cıvata) · yosun → küvet → kaya (ip)
  S3         panel → sandık → davit → platform → bölme, çemberin İÇİ
  S4         su → havuz → emme borusu → konteyner → taban boruları → tank
  S5         sürü → tanker → hortum → giriş ağzı → tank
  G5–G6      su → paneller → çemberler (dışa basınç) → dikmeler → taban
  ⛔ Her karede en az ÜÇ temas cümlesi. ⛔ VİNÇ YOK — kadrajda kanca, bom ya da göğe uzanan halat görülürse kare düşer.
  ⛔ Çemberler ve paneller S4'te KIPIRDAMAZ (dolan su altında şişme, eğilme, ayrılma = düşer).
```

---

## 9. SAYIM KAPISI [DERS 55]

```
Yedi karenin yedisinde de kadrajda ŞUNLAR VARDIR:
  ① silo (bir) ② rıhtım kenarı ③ tuğla ambar ④ ufuk ve liman feneri
Yedi karenin hiçbirinde kadrajda ŞUNLAR YOKTUR:
  ⛔ ikinci silo · silo bataryası · tahıl elevatörü kulesi · ikinci tank · petrol tankı · gemi
  ⛔ G5'ten önce kalabalık NET hâlde (S4 6,0–8,0 sn'de iz olarak gelir) · G4'ten önce tanker (S4 5,5 sn'de gelir)
  ⛔ G6'dan önce balık
⚠️ EN OLASI MODEL ARIZASI: silo korpusu ÇOĞULDUR; "tank + harbour" petrol tankı çağırır. Her kare bu listeye karşı okunur.
```

---

## 10. ⭐ REJİM KAPISI — B × 5 → G × 1

```
  S0–S4  rejim B · 2 sa / 8 sn = 900× · işçiler YUMUŞAK İZ (2–5 kişi) · havuz suyu parlak düz · bulutlar ufka doğru
                                         akar ve uzar · gölge 23°–60° süpürür · S4'ün son 2 sn'sinde kalabalık İZ
  S5     rejim G · 8 sn / 8 sn =   1× · ⭐ kalabalık NET, sırtı kameraya, yüz okunmaz, İZ YOK · sürü gerçek hızda ·
                                         havuzda küçük dalgacıklar · bulutlar DURUR · gölge yok (güneş battı)
  ⛔ B kliplerinde net, donmuş figür = rejim kaçağı [DERS 15 · 50].
  ⛔ G klibinde iz bırakan figür, akan bulut ya da bir anda tankı dolduran sürü = rejim kaçağı.
  ⭐ 40,0'DAKİ DİKİŞ BEYANLIDIR [P5-c · P10-b]: havuz suyu parlaklıktan dalgacığa, kalabalık izden nete döner.
     TANK SUYU iki rejimde de durgundur — orada dikiş YOKTUR.
```

---

## 11. ⭐ SES KAPISI — DİEGETİK

```
⛔ MÜZİK YOK. Yatak: liman — havuz duvarına vuran küçük dalga, uzakta martı, hafif rüzgâr.
  ① ⭐ İLK SES (0,0–1,0): paslı bulon gıcırtısı + düşen oluklu sacın uzun, titrek gümbürtüsü.
  ② 16,0–24,0 darbeli anahtar — filmin ilk ritmik sesi; çemberler sıklaştıkça patlamalar SIKLAŞIR.
  ③ 24,0–32,0 sekiz "tunk" kümesi; ⭐ son panel tek "tunk" + kısa sessizlik.
  ④ ⭐ 32,0–40,0 dolan su — PERDESİ YÜKSELİR. ≈ 39,5 röle "klak".
  ⑤ ⭐ 40,0–41,0 SESSİZLİK PENCERESİ: pompa yok, motor yok. ⛔ Buraya efekt konmaz.
  ⑥ ⭐ 41,0 vana: tek metalik "tak". Ölçüm: bu 0,2 saniyenin tepe seviyesi önceki 1,0 saniyenin RMS'inden en az
     12 dB yüksek.
  ⑦ ⭐ 41,5–48,0 kabarcık + kalabalığın susması ve tek "oo". SES KANITI: ilk ses bir DÜŞÜŞ, son ses bir NEFES.
  ⛔ Anlatıcı, anlaşılır konuşma, "epik" vurgu efekti, gemi düdüğü YOK · martı en fazla bir kez · 150 Hz altında
     tek taşıyıcı yok.
```

---

## 12. ZAMAN VE IŞIK GÜNÜ

```
REJİM      5 × B (2 sa) + 1 × G (8 sn) = 10 sa 0 dk 8 sn
PENCERE    09:00 → 19:00:08 (yerel güneş saati) · 41,3° kuzey · 16 ağustos · δ +13,5° · batış 18:53
IŞIK GÜNÜ  ≤ 14 sa ✓ · gece yok · final mavi saatte, güneş −2,0° (DERS 45 — okunur)
⭐ MERTEBE BEYANI [HAVA_VE_ATMOSFER §5 · P1-c]: "tek bir ağustos günü, sabahtan alacakaranlığa". ③ merceğinin
   "TIME READ FROM THE FILM ALONE" satırı bununla karşılaştırılır. ⚠️ Gerçekte bu iş aylar sürer — "aylar" okunursa
   bu bir hata değil, beyanlı hız bedelinin görünmesidir.
```

---

## 13. ⚠️ BİLİNEN RİSKLER — üretimden önce oku

```
① ⭐ EN BÜYÜK RİSK — SÜRÜ (§2). Pilot S5. ⛔ Pilot üçlü geçmeden kalan klipler üretilmez.
② ⭐ İKİNCİ RİSK — ŞEFFAF PANEL (§3). İkinci pilot S3.
③ KORPUS: silo bataryası, petrol tankı, kavram sanatı akvaryum (§9 · §2 korpus kontrolü).
④ SU YÜKSELİŞİ: su seviyesi düşerse ya da "fade" ile dolarsa S4 düşer (§4).
⑤ ÇEMBER SIKLIĞI EŞİTLENİR (§4) · ⑥ PASLI TAÇ BOYANIR ya da SÖKÜLÜR (§4)
⑦ DONUK İŞÇİ (§10) · ⑧ KARANLIK FİNAL (§5 ⑤) · ⑨ HAVUZ SUYU DİKİŞİ (§10 — beyanlı)
⑩ HIZ: tek günde silodan tanka ve aynı akşam balık — beyanlı bedel; ④ / ⑧ "bu kadar hızlı olmaz" derse kusur değildir.
⑪ ⭐ KAPAKTA SPOİLER. Kapak dolu tankı gösterir (sahip kuralı: kapak = GN). Beyanlıdır [KAPAK §1].
```
