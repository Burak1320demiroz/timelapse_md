# 🛶 THE_SKY_CANAL — Yatay Timelapse Planı

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 I2V PROMPT` başlıkları YALNIZ
> bölüm dosyalarında bulunur; kapı betiği promptu başlıktan sayar ve klasör modunda bu dosyayı
> bölümlerle BİRLEŞTİRİR — plana konan örnek bir prompt sahne dizisine karışır.

Yatay Timelapse Production Document
Format: **16:9 (YATAY)** · 1920×1080 · 30 fps | Sahne: **20 × 8,0 sn = 160,0 sn** | Kapak kartı: **⛔ YOK** | Toplam: **160,0 sn**
Prompt yapısı: ⭐ **20 sahne → 21 görsel (G0…G20) + 20 I2V · T2V YOK** [`KILAVUZ_REHBERI` §2.7] · bölüm sınırı karesi **G10**
Yapı: **nehir vadisi üstünde tekne taşıyan çelik kanal köprüsü — 100 m, üç açıklık (30 + 40 + 30), üstü açık çelik oluk (iç 8 m × 2 m), iki beton ayak + iki kıyı mesnedi, yakın tarafta bakım yolu + korkuluk, iki uçta düşey kalkan çelik kapak** (en yakın kart `YAPI_TIPI_KARTLARI` §3 KÖPRÜ — konsol/kablo değil, vinçle parça montajı; 00_ANALIZ/02 §2a'da bu film için yazıldı) · Saha: **derin, ağaçlı nehir vadisi, 47° K** (`SAHA_VE_IKLIM_KARTLARI` kırsal/dağ satırı ⚠️ birebir yok; 02 §2b)
Zaman yayı: **gerçekte ≈5 ay üst yapı (geç ilkbahar → ekim) + tek dolum günü → 160 saniye** · film mertebe anlatır: *"bir bahar parçalar, bir yaz oluk, bir sonbahar su ve tekne"* [P1-c] · ÜSLUP BEYANI: takvim tek bir ekim gününün ışığına sıkıştırıldı (THE FIRST LIGHT emsali)
Işık günü: **08:20 → 16:43 (altın saat) · Σ rejim penceresi 8 sa 23 dk ≤ 14** — kesmede ışık atlamaz [§2.7 ①]
Kamera mimarisi: **MAIN STATION** — 20 klip + usta kare, **%100** · ikinci istasyon YOK
Izgara: ⛔ **DÜZ — 20 × 8,0** · ⚠️ BANDIN DIŞI (format 12 × 10,0 · 2:00) — sahip senaryosunun biçimi, toplam 2:40 (hikâye SAPMA ②) · §DÜZ IZGARA BEYANI
Hikâye onayı: `00_ANALIZ/00_HIKAYE_ONAYI.md` ONAY ✅ 11.10.2026 (TUR 1 · "hazırla" · 20 satır · SAPMA ①–⑱)
Havuz kaydı: `apexait/YAYIN_PLANI.md` — ⬜ satır açılmadı (sahip kararı) · siluet ailesi: **yatay köprü + su finali** (THE IRON BRIDGE köprü + nehir akrabası; THE EDEN ARK su alıp tekne yüzdürme akrabası)

_"İlk karede iki ayağın arasındaki boşluğun üstünde askıda bir çelik parça ve solda havuzda bekleyen kırmızı tekne; son karede aynı vadinin üstünde suyla dolu kanal köprüsü ve köprünün sağ ucuna varmış aynı tekne, aşağıda akan nehir."_

---

## 📦 TESLİM YAPISI

```
SAHNE BLOĞU     20 sahne × 8,0 sn                       = 160,0 sn   ← QA merceklerinin konusu
KAPAK KARTI     ⛔ YOK — tam 160,0 sn (sahip senaryosu: "son kare kapaktır; ek afişe kesilmez") · ihrac_kontrol.sh --kart YOK
──────────────────────────────────────────────────────────────
TOPLAM                                                     160,0 sn
HIZ             1x (yatay hat 2x'e çevrilmez — 2x yalnız dikey paylaşım kuralıdır [DERS 58])
MÜZİK           ✅ VAR — altta, sözsüz, ölçülü, 120 BPM (8,0 sn = 4 ölçü) · diegetik yatak ÖNDE (vinç · çelik · su · tekne
               motoru) · sahip senaryosu "Ses ve müzik" · THE_SKY_CANAL_MUZIK.md
YASAK KELİME    aqueduct · roman · arch · viaduct · lock · dam · waterfall · cascade · fountain · pool · swimming · ship · ferry · yacht · float · drone · neon · pontcysyllte · magdeburg · elbe · telford
               ⭐ [DERS 59 · 55 · 42] hiçbir promptta, negatifte bile — "aqueduct · roman · arch · viaduct" taş kemerli Roma su
                  kemerini ve demiryolu viyadüğünü çağırır (hikâye SAPMA ⑯); "lock · dam" kanal havuzu yerine kilit
                  odası ve baraj; "waterfall · cascade · fountain" oluktan vadiye dökülen su; "pool · swimming" açık
                  mavi kaplamalı oluğu yüzme havuzuna çevirir; "ship · ferry · yacht · float" tekneyi büyütür ve suyun
                  üstünde havada çizer [SU_VE_YANSIMA §7]; "drone · neon" kamera hareketi ve parlayan su; "pontcysyllte ·
                  magdeburg · elbe · telford" GERÇEK YER ve kişi
KELİME KİLİDİ   "crane" yalnız G0–G12 + S0–S12 I2V [P7-e] · oluğun içinde su ("shallow · sheet of water · water line · three
               quarters of the wall") yalnız S13 I2V ve G14'ten sonra — öncesi "dry" [DERS 54] · iç kaplama "blue" yalnız
               S8 I2V ve G9'dan sonra · "charcoal" yalnız S11 I2V ve G12'den sonra · kapaklar "raised" yalnız S16 I2V ve
               G17'den sonra · tekne "glides · wake" yalnız S17 I2V ve G18'den sonra · STRUCTURE'da su, tekne, renk yok
               (yalnız yapı) [DERS 36]
BÖLÜM DOSYASI   BOLUM_1 = S0–S9 (0–80,0)  ·  BOLUM_2 = S10–S19 + USTA KARE (80,0–160,0) · ceil(20/2)=10
QA BİRİMİ       FİLM (tek master × 5 mercek · ❶ ❷ ❸ kör · ❹ ❺ belgeli) — QA/HAM/THE_SKY_CANAL/
```

⛔ Kart olmadığı için platform son ekranı **son 5 saniyeye konmaz** ya da yalnız gök bandına (üstten 0–149 px) konur — sağ uçtaki tekne (x ≈1240–1370), açık kapaklar ve oluğun üstüne yerleştirilmez.
⚠️ Son sahnenin (S19) ikinci yarısı TUTUŞTUR (final kanıtı 156,0–160,0, `QA_SPEC` §1): tekne durur, burnu sağ kapakta; yalnız nehir akar ve iz söner.
⭐ Platform küçük resmi (kapak) G20'den gelir (sahip kararı 19.09.2026 — öncesi/sonrası bölme yok).

### ⭐ İZLEYİCİ KAPISI [C2-a…d · KILAVUZ_REHBERI §6]

```
İŞLEV ANI         S13 vana açılır, ilk su → S15 seviye kıyılarla eşitlenir → S16 kapaklar KALKAR → S17 tekne köprüye girer →
                  S18 nehrin üstünden geçer → S19 sağ kapakta durur. Köprü kullanılır, yalnız bitmez.
AÇILIŞ NESNESİ    G0: iki ayağın arasındaki boşluğun yanında, sol açıklığın üstünde askıdaki çelik parça (x ≈540–844) +
                  solda havuzda kırmızı tekne (x 161–381 · ≈220 px) · ona ne oluyor: montaj ilk karede SÜRÜYOR (parça
                  iniyor). 120 px'te okunan: yeşil vadide gri bir yatay çizgi + ortada boşluk + solda kırmızı leke.
DİRENÇ EKRANDA    ① boşluk ve ağırlık — S0 askıdaki sol parça · S1 kıyıdan kalkan sağ parça · S2 nehrin kıyısından dimdik
                  yükselen merkez parça (hepsi dört sapanla, tek parça) · ② su — kuru mat oluk (G13) · soldan ilerleyen
                  sığ su (S13–S14) · yükselen seviye (S15) · kapalı kapaklar (G0–G16) · ③ tekne — 17 klip bekler
DÖNGÜ KAFİYESİ    G20 ↔ G0 aynı kadraj, aynı çam (x 1475–1547), aynı iki ayak (844 · 1182): G0'da tekne SOLDA havuzda,
                  köprü yok, boşluk açık; G20'de AYNI tekne SAĞDA köprünün ucunda, köprü suyla dolu. Işık FARKLI,
                  bilinçli: serin sabah ↔ altın saat; ağaçlar açık yeşil ↔ sonbahar.
MERAK SORUSU      Bu tekne buradan nasıl geçecek?
AÇILIŞ DÜZENİ     ① NESNE askıdaki sol açıklık parçası · ② DOKUNUŞ "From the first frame the span section is already moving" ·
                  ③ İPUCU solda havuzda bekleyen kırmızı tekne + kapalı kapak — tekne nereye gidecek, belli; nasıl gidecek,
                  belli değil · ④ ÖLÇEK iki büyük paletli vinç + ayak tepesindeki ekip (iz) + aşağıdaki nehir ·
                  AÇILIŞ GERİ ÇEKİLMESİ ⛔ YOK (sabit geniş)
DÖRT TERCİH (sahip) ilk 24 sn'de somut sonuç (S2 sonu: kıyılar birleşir) · 20/20 aynı kamera · su üç ayrı durum (ilk akış ·
                  karşıya ulaşma · derinleşme) · altın saat finali, kapak son kareden — sahibin kurgu tercihi, ölçülmüş bir
                  formül değil
```

---

## 🚪 KONSEPT KAPISI [`KILAVUZ_REHBERI` §6]

```
VAAT     Bir vadinin üstündeki hazır ayaklar, iki kıyıdaki kanalı birleştiren ve tekne taşıyan bir su köprüsüne dönüşür.
DİRENÇ   ① boşluk ve ağırlık (üç dev çelik parça, 30–40 m, tek parça vinçle)  ② su (kuru oluk soldan, kademe kademe dolar;
         seviye eşitlenmeden kapak açılmaz)  ③ tekne (17 klip bekler; geçiş ancak her şey bitince)
         EKRANDA NASIL [P1-b]:  S0–S2 · askıdaki ve yükselen parçalar  ·  S3–S7 · ızgara → taban → duvarlar → bağlantı  ·
                                S8 · mavi bant  ·  S13–S15 · ilerleyen su cephesi ve seviye  ·  S16 · kalkan kapaklar
BEDEL    ⭐ boşluk + şantiye: G0'da iki ayağın arası açık (x 844–1182), iki vinç, parça istifleri, kalaslar, kapalı kapaklar;
         boşluk S2'de kapanır, vinçler ve istifler S12'de gider, kapaklar S16'da kalkar. G20'de aynı yerde dolu köprü.
         Okuma bilinçli: "köprü yapıldı" değil, "tekne vadiyi geçti".

KANAL TEZİ KAPISI [apexait/KANAL_KIMLIGI §2.1]
  □ ne kayboluyor?            boşluk + vinçler + istifler + kalaslar + kapalı kapaklar                   ✅
  □ kadrajda görünüyor mu?    boşluk 844–1182 · vinç tabanları x ≈413 / 1605 · kapak çerçeveleri 529 / 1383 ✅
  □ cevap "zaman geçiyor" mu? hayır — "su geldi, kapaklar kalktı, tekne geçti"                          ✅
```

### Dört kabul testi

```
① TEK KARE TESTİ        ✅ donmuş karede: kaç açıklık oturmuş (0 · 1 · 2 · 3) · ızgara mı taban mı · kaç duvar · uçlar bağlı mı ·
                           iç yüzey gri mi mavi mi · bakım yolu ve korkuluk var mı · dış astar mı kömür grisi mi · vinç var mı ·
                           oluk kuru mu, sığ su nerede, dolu mu · kapaklar kapalı mı açık mı · tekne nerede
② KİNETİK BAĞIMSIZLIK   ✅ her klipte vinç, ekip, kamyon, su cephesi, kapak, tekne ya da servis aracı hareket eder; nehir hep akar
③ BAŞLIK ŞEMASI         ✅ kapak yazısız (yedek: "THE SKY CANAL", 3 kelime) · yayın başlığı YAYIN_PAKETI (33 karakter ≤ 40)
④ OMURGA CÜMLESİ [P1-k] ✅ indirir → yerleştirir → birleştirir → bağlar → kapatır → yükseltir → tamamlar → bağlar → kaplar → kurar →
                           çevirir → boyar → toplar → akıtır → ilerletir → doldurur → açar → girer → geçer → VARIR
```

⚠️ **Aile benzerliği [P16-a]:** THE IRON BRIDGE ile köprü + nehir akrabalığı; AYIRICI FARK: orada kemer ve taşkın, burada
oluk + dolum + TEKNE (köprü bir kullanıcıyla biter). THE EDEN ARK ile su alıp yüzdürme ortak; burada su bir kanaldan gelir ve
tekne yer değiştirir. Ardışık yayınlanmamalı (YAYIN_PLANI §3 — sahip kararı).

---

## 🎯 ÖNCELİK KATMANLARI — üretim sadeleştirme geçişi

```
P0 · bunlarsız film yok   ① aynı kamera (ana istasyon %100)
                          ② kanıt nesnesi: ÇAM (x 1475–1547 · üstten 622–819 · 72 px · 21 karede birebir)
                          ③ çapa: iki ayak (x 844 · 1182) + iki mesnet (538 · 1398) + nehir (köprü altında x ≈1002) ·
                             ④ ufuk %86 (149)
                          ⑤ köprü tek hat: x 538 → 1398 · yakın üst kenar %38 → %48 — G3 → G20 ±2 px; yalnız KAZANIR
                             (ızgara · taban · duvarlar · bağlantı · mavi · bakım yolu · korkuluk · kömür grisi)
                          ⑥ SU KOTU DEFTERİ (aşağıda) — kuru (G0–G13) → onda bir (G14–G15) → dörtte üç (G16+)
                          ⑦ TEKNE DEFTERİ (aşağıda) — havuzda bağlı (G0–G16) → köprüde (G18–G19) → sağ kapakta (G20)
                          ⑧ insan: A/B'de iz ("soft motion streaks") · Y'de küçük figür, sırtı kameraya · teknede tek dümenci
                          ⑨ vinç kancası: ya YÜKLÜ ya bom ucu kadraj dışında — boş kanca hiç yok (VİNÇ DEFTERİ)
P1.5 · fırsat buldukça   ağaçların rengi (açık yeşil → koyu yeşil → ilk sarı → sonbahar) · gölge süpürmesi (B: S3 · S8 · S11) ·
                          dolu oluktaki gök parıltısı · teknenin V izi
SPEC · yalnız belge      azimut/yükseklik dereceleri (kapı şartı) · px tabloları
```

**Malzeme kimliği (her promptta):** *açık renkli beton ayaklar · açık gri astarlı çelik → koyu kömür grisi · açık mavi mat iç kaplama · galvanizli bakım yolu ve korkuluk · sarı paletli vinçler · kırmızı gövdeli, krem kabinli tekne · berrak su · yeşil ağaçlı yamaçlar · açık gri çakıl* — korpus: "documentary site photograph on colour negative film" [DERS 34 · 42].
**İnsan kararı:** ekip var — A/B'de iz; dolum günü vanada ve bakım yolunda iki-dört kişi; teknede tek dümenci (sırtı kameraya); hiçbir yüz okunmaz.
**Vinç kararı [DERS 8 · 22 · 46 · 57]:** iki büyük sarı paletli vinç, gri kafes bom: SOL vinç sol pedde, havuzun ötesinde (x ≈413 · üstten 609) · SAĞ vinç sağ pedde (x ≈1605 · üstten 592) · G0–G12. Bom uçları hep kadrajın üstünden çıkar (uç ≈ +100 m) — kanca halatı yukarıdan iner, yükü kadrajdadır. VİNÇ DEFTERİ aşağıda; S12'de ikisi de bomunu indirir ve servis yollarından çıkar; G13'ten sonra "crane" kelimesi yok [P7-e].
**Uzun rijit yük [DERS 57]:** ⚠️ VAR — sol parça (30 m), sağ parça (30 m), merkez parça (40 m). Önlem: S0 ilk karede ASILI, hedefin bir metre üstünde (yalnız oturma); S1 kısa yol (kıyı pedinden sağ açıklığa); S2 yalnız DİMDİK yukarı, tek vinç, yayıcı kiriş (hikâye SAPMA ⑤). Her biri dört sapanla, yavaş, tek parça; ikinci kopya yazılmaz ("exactly two piers"). PİLOT ② = S2.
**Korpus kararı [DERS 55]:** kanal + köprü + vadi korpusu çoğuldur (ikinci köprü, demiryolu viyadüğü, baraj) → NEGATIVE'de her karede: "The valley holds exactly one canal bridge, this one, on exactly two piers, and exactly one boat."
**Yapı adı kararı [DERS 42]:** "steel canal bridge" + "water trough" yazılır; "aqueduct" YASAK (Roma kemeri); tekne "small red canal boat with a cream cabin" (gemi/feribot/yat YASAK); kaplama "pale blue lining" (havuz/fayans YOK).

---

## 🔒 DEĞİŞMEZLER TABLOSU [`KILAVUZ_REHBERI` §3 — dört kutu]

```
KARAR CÜMLESİ [KAMERA_DILI §0]: İzleyici köprünün parça parça kurulmasını, oluğun suyla dolmasını ve teknenin geçişini görecek.
                 Çam, iki ayak, nehir ve sırtlar aynı kalacak. Kamera YÜKSEK ÇAPRAZ aileden (h 85 · tilt 17° aşağı) bakacak —
                 oluğun içi, köprünün yüksekliği ve aşağıdaki nehir ancak böyle aynı karede okunur. Hareket YOK.

ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — üretim günü ARAC_KARTLARI §4 sekiz ölçümle doldurulur [DERS 23 · 31 · D-d].
                 Bu plan yazılabilir, üretim açılamaz. Her sahne 8,0 sn teslim → SAHNE TAVANI ≥ 8,0,
                 yani en büyük kutu ≥ 9,0 (üret 9,0 → baştan 1,0 kırp [A7-b]; kutu tam 8,0 ise kırpma payı YOK).
                 {4,6,8} çıkarsa 20 sahnenin hepsi iki zincirli klip (ara kare Gn′) — karar sahibe döner.

┌─ KAMERA İSTASYONU (ANA · tek istasyon) ──────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100 · tam kare YATAY (36 × 20,25 mm)   │
│ yükseklik     h = +85,0 m (nehir suyundan) — sol yamaçta kaya çıkıntısı       │
│ mesafe        D_eksen = 135,0 m (köprünün ortası — BÜTÜN px buradan) ·        │
│               D_kenar ≈ 107 m (çam) · sol havuz ≈ 124 · sol mesnet ≈ 121 ·     │
│               sağ mesnet ≈ 160 [DERS 38]                                       │
│ bakış açısı   bearing 20° (KKD, vadinin yukarısı) · tilt 17° AŞAĞI · roll 0°   │
│ köprü ekseni  görüntü düzlemine 20° (sağ uç uzakta) — üç çeyrek çapraz         │
│ sabitleme     "fixed tripod bolted to a rock ledge high on the left valley    │
│               slope"                                                          │
│ ⛔ HESAP — iğne deliği izdüşümü (yatay 16:9, f 24 → 1280 px):                  │
│    px = 960 + 1280·Xc/Zc · üstten = 540 − 1280·Yc/Zc (kamera eksenine dönük)  │
│    ufuk üstten 540 − 1280·tan 17° = 149 (%86)                                 │
│    `bolum_uretici.py --kadraj` çıktısı:                                       │
│    sol mesnet duvar tepesi   x 538 · üstten 670 (%38) · dibi 737              │
│    sol kapak çerçevesi tepesi x 529 · 589                                     │
│    sol ayak tepesi / dibi    x 844 · 684 / 882                                │
│    sağ ayak tepesi / dibi    x 1182 · 636 / x 1172 · 819                       │
│    sağ mesnet duvar tepesi   x 1398 · 561 (%48) · kapak çerçevesi tepesi 497  │
│    oluk merkez (s 0)         yakın duvar tepesi 609 · uzak duvar tepesi 587 · │
│                              uzak taban 603 · su çizgisi (+36,5) 591 ·        │
│                              kiriş altı 656 · korkuluk 607                    │
│    ⭐ oluğun içi: bakış 20,3° · yakın duvar tabanın 5,0 m'sini gizler → uzak  │
│       3,0 m + uzak duvarın iç yüzü görünür (merkezde ≈16 + 6 px)              │
│    tekne (havuz) x 161–381 · 691–719 · kabin tepesi 682 (≈220 px)              │
│    havuz sonu x 65 · sağ kanal (s 70) x 1505 · 539                             │
│    sol vinç tabanı x 413 · 609 · sağ vinç tabanı x 1605 · 592                  │
│    sağ parça istifi x 1491–1687 · 543–569                                     │
│    merkez parça kalasta x 839–1152 · 804–890 (nehrin üstünde, ayakların dibinde)│
│    nehir köprü altında x 1002 · 888 (%18) · 300 m yukarıda x 981 · 514         │
│    ⭐ kanıt nesnesi ÇAM x 1475–1547 (72 px) · tepe 622 (%42) · dip 819          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — kalıcı, geçici ekipman GİRMEZ [DERS 1] ────────────────┐
│ ① ⭐ ÇAM (SAĞ · x 1475–1547 · 622–819) — KANIT NESNESİ, sağ yamaçta kaya        │
│    çıkıntısında, düz taçlı, iğne yapraklı: mevsimle değişmez                  │
│ ② İKİ AYAK (x 844 · 1182) + İKİ MESNET (538 · 1398) — G0'dan beri hazır       │
│ ③ NEHİR — vadi tabanında, kameraya doğru akar, merkez açıklığın altından      │
│ ④ UFUK %86 (149) — iki uzun ağaçlı sırt · ⑤ iki kanal kolu (sol havuz · sağ   │
│    kıvrım) · dolum borusu (sol kapak çerçevesinin yanında, G0'dan beri)       │
│ + "The valley holds exactly one canal bridge, this one, on exactly two piers, │
│   and exactly one boat" — her NEGATIVE'de                                     │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ─────────────────────────────────────────────────────────────┐
│ tilt 17° → ufuk %86 · gök bandı üstten 0–149 (yedek kapak başlığı burada)     │
│ yanlar: solda havuz + tekne + sol ped + vinç · sağda sağ ped + vinç + çam      │
│ güvenli alan 16:9 ⬜ ÖLÇÜLMEDİ — kanıt nesnesi alt 100 px'e (üstten > 980) ve  │
│ sağ üst 300×100 px'e (x > 1620 · üstten < 100) girmez ✓ (çam 622–819)          │
│ ⚠️ alt onda bir (üstten > 972): yalnız nehir ve yakın yamaç — ilerleme kanıtı  │
│    oraya düşmez ✓ (merkez parça kalasta en altta 890)                         │
│ ⚠️ keystone: tilt 17°'de ayakların düşey kenarları hafif yakınsar — kabul      │
│    edilen bedel (KAMERA_DILI §3 ③)                                            │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — her satır bir SAYI [DERS 19 · 36] ──────────────────────────────┐
│ köprü ekseni: s −50…+50 (100 m) · açıklıklar 30 + 40 + 30 · ayaklar s ±20 ·    │
│   mesnetler s ±50 · eksen görüntü düzlemine 20°                               │
│ ana kirişler: iki derin çelik kiriş, off ±4 · kot +31,5 → +35,0 (3,5 m) ·      │
│   parçalar: sol 30 m · merkez 40 m · sağ 30 m · enine kirişler eşit aralıklı   │
│ oluk: iç 8 m (off −4…+4) · taban +35,0 · duvar tepesi +37,0 (2 m) · dolu su    │
│   +36,5 (duvarın dörtte üçü, 1,5 m) · sığ su ≈ +35,2 (duvarın onda biri)       │
│ ayaklar: açık renkli beton, alt yamaçta (dip ≈ +8) · yatak tepesi +31,5        │
│ bakım yolu: yakın duvarın dışında konsollarda (off −4,4…−6) · +36,8 ·          │
│   korkuluk +37,9 · iki uçta çelik erişim basamakları                           │
│ kapaklar: s ±50 · çelik çerçeve tepesi +44 · kapak düşey kalkar (G17+ yukarıda)│
│ kanallar: su +36,5 (oluğun dolu seviyesi) · sol havuz s −50…−90, 16 m geniş ·  │
│   sağ kol s +50…+75 sonra ağaçlara kıvrılır                                    │
│ dolum borusu: sol havuzdan sol kapak çerçevesinin üstünden oluğa · büyük vana │
│ tekne: ≈18 m · ≈3,5 m geniş · kırmızı gövde, krem kabin · kabin tepesi +38,8   │
│ nehir: ≈15 m geniş, kot 0 · çakıl düzlükleri + yanında kaba yol                │
│ STRUCTURE'ın İngilizce tam hâli tek cümle (DERS 36): "When finished this will  │
│   be a navigable steel canal bridge: an open-topped steel water trough 100     │
│   metres long, 8 metres wide inside and 2 metres deep, carried high over the   │
│   valley on three spans by two tall pale concrete piers and two bank           │
│   abutments, with a walkway and railing along its near side and a             │
│   vertical-lift steel gate at each end where it meets the canal on each        │
│   bank." — 21 görselde BİREBİR                                                │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🪜 AŞAMA MERDİVENİ — 20 satır [`KILAVUZ_REHBERI` §4 · `INSAAT_YONTEMI` §2-§3 · `SANTIYE_HAREKETI` §1]

> Tek yasa: **MONOTON BÜYÜME** — hiçbir satır bir öncekinden az YAPI göstermez. S12'de şantiye gider (yapı aynı); S13–S16
> suyu ve kapakları ekler; S17–S19 yapıyı değiştirmez, KULLANIR. Kış görüntüsü YOK (takvim ilkbahar → sonbahar; DERS 7
> tetiklenmez).

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | MEVSİM TAŞIYICISI | KANIT NESNESİ (px) |
|:-:|:-:|---|---|:-:|:-:|:-:|---|---|
| 0 | 8,0 | OTURTUR | sol parça asılı → oturur (%100) | 1 gün | A | 08:20→08:30 | geç ilkbahar · açık yeşil | sol açıklık 538–844 |
| 1 | 8,0 | YERLEŞTİRİR | sağ parça pedden → sağ açıklık (%100) | 1 gün | A | 08:30→08:40 | aynı | sağ açıklık 1182–1398 |
| 2 | 8,0 | BİRLEŞTİRİR | merkez parça kalastan → dimdik yukarı (%100) · ⭐ kıyılar birleşir | 1 gün | A | 08:40→08:50 | aynı | boşluk 844–1182 kapanır |
| 3 | 8,0 | BAĞLAR | enine kirişler (%0 → %100, iki uçtan) | 3 hafta | B | 08:50→10:50 | aynı | köprü hattı 538–1398 |
| 4 | 8,0 | KAPATIR | taban panelleri (%0 → %100) | 3 hafta | A | 10:50→11:00 | yaz · koyu yeşil | nehir aralıkları kapanır |
| 5 | 8,0 | YÜKSELTİR | uzak duvar (%0 → %100) | 3 hafta | A | 11:00→11:10 | aynı | uzak duvar tepesi 587 |
| 6 | 8,0 | TAMAMLAR | yakın duvar (%0 → %100) · U oluk | 3 hafta | A | 11:10→11:20 | aynı | yakın duvar tepesi 609 |
| 7 | 8,0 | BAĞLAR | uç parçaları ↔ kapak çerçeveleri (%100) · kapaklar kapalı | 2 hafta | A | 11:20→11:30 | aynı | 529 · 1383 çerçeveler |
| 8 | 8,0 | KAPLAR | iç yüzey gri → açık mavi (%0 → %100, soldan) · KURU | 4 hafta | B | 11:30→13:30 | aynı | ⭐ mavi bant 587–609 |
| 9 | 8,0 | KURAR | bakım yolu + uç basamakları (%0 → %100) | 3 hafta | A | 13:30→13:40 | aynı | korkuluk hattı 607 |
| 10 | 8,0 | ÇEVİRİR | korkuluk (%0 → %100) | 2 hafta | A | 13:40→13:50 | aynı | korkuluk hattı 607 |
| 11 | 8,0 | BOYAR | dış astar → kömür grisi (%0 → %100, soldan) | 4 hafta | B | 13:50→15:50 | yaz sonu · ilk sarı lekeler | köprü rengi 538–1398 |
| 12 | 8,0 | TOPLAR | paletler + iki vinç çıkar · saha boşalır | 2 hafta | A | 15:50→16:00 | sonbahar · altın, turuncu | vinçler 413 · 1605 → 0 |
| 13 | 8,0 | AKITIR | ⭐ ilk su: borudan → sol ayağa kadar (onda bir) | 10 dk | A | 16:00→16:10 | aynı | su cephesi 538 → 844 |
| 14 | 8,0 | İLERLETİR | su cephesi sol ayaktan → sağ kapağa (onda bir) | 10 dk | A | 16:10→16:20 | aynı | su cephesi 844 → 1398 |
| 15 | 8,0 | DOLDURUR | onda bir → dörtte üç · kıyılarla eşit | 10 dk | A | 16:20→16:30 | aynı | su çizgisi uzak duvarda 591 |
| 16 | 8,0 | AÇAR | iki kapak kalkar (%100) · geçiş açık | 10 dk | A | 16:30→16:40 | aynı | kapaklar 529 · 1383 yukarı |
| 17 | 8,0 | GİRER | tekne havuzdan → köprüye, burnu sol ayakta | 1 dk | Y | 16:40→16:41 | aynı | tekne 161–381 → 620–796 |
| 18 | 8,0 | GEÇER | tekne → merkez açıklığın ortası · ⭐ DORUK | 1 dk | Y | 16:41→16:42 | aynı | ⭐ tekne 974–1121 · nehir 1002 |
| 19 | 8,0 | VARIR | tekne → sağ kapak, durur · TUTUŞ | 1 dk | Y | 16:42→16:43 | aynı | ⭐ tekne 1242–1368 |

```
IZGARA          8,0 sn × 20 · kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn) · müzik 120 BPM → her kesme ölçü başında
                (8,0 sn = 4 ölçü)
                ⛔ SÜTUN PLANDA KALMAZ [DERS 31]: yayından önce bash araclar/kesme_kontrol.sh <teslim> <bu dosya>
DÜZ IZGARA BEYANI  (a) gerekçe: sahip senaryosunun biçimi (20 × 8,0, kart yok — hikâye SAPMA ②); yatay_2 README'deki sahip
                       izinli modül dışı ızgara (16.09.2026) — ⚠️ ama toplam süreyi KORUMAZ (2:00 → 2:40); emsal THE FIRST
                       LIGHT (20 × 8,0). ⚠️ BANDIN DIŞI: format 12 × 10,0.
                   (b) ritim klip İÇİNE: ① rejim nabzı — B'ler S3 · S8 · S11 (kirişler · mavi · boya), Y S17–S19 (tekne,
                       yavaş); ② iş yönü değişir: aşağı (S0 oturma) · yana (S1) · DİMDİK yukarı (S2) · iki uçtan ortaya
                       (S3–S6 · S9–S10) · uçlara (S7) · soldan sağa (S8 · S11 · S13–S14) · dışarı (S12) · yukarı (S15
                       seviye · S16 kapaklar) · soldan sağa YOLCULUK (S17–S19); ③ müzik katmanı = aşama (MUZIK.md)
                   (c) kabul edilen risk: eşit klipte ❷ RHYTHM kategorisi NOT TRIGGERED — sapma kurgudan gelirse (klip ≠ 8,0)
                       ❷ açılır ve ❺ final saniyesi kayar. Karşı kayıt: varyanslı kurgu üç filmde RHYTHM aldı [DERS 44].
REJİM SAYISI    ⚠️ ÜÇ rejim (A · B · Y) — SANTIYE_HAREKETI §2 sınırı iki. Gerekçe: Y yalnız tekne klipleridir (S17–S19) ve
                ancak bu hızda tekne klip başına bir açıklık ilerler (≈40 m · 2,4 km/sa — SU_VE_YANSIMA §7 hız tablosu).
                A'da (10 dk) tekne bütün köprüyü bir saniyede geçer, G'de (8 sn) üç klipte ≈27 m ilerler. Geçiş KESMEDE
                (S16 → S17) [P5-c]. ⚠️ Y DEPODA YENİ, ÖLÇÜLMEDİ — kapı tanımaz ("one minute passes" REJİM sözlüğünde yok):
                S17 · S18 · S19 görselleri + I2V'leri + G20 = 7 beklenen FIX (§ÜRETİM ÖNCESİ DURUM). PİLOT ① ölçer.
IŞIK GÜNÜ       Σ pencere = 14 A × 10 dk + 3 B × 2 sa + 3 Y × 1 dk = 140 dk + 6 sa + 3 dk = 8 sa 23 dk ≤ 14 ✓
                08:20 (güneş 15,8°) → 16:43 (altın saat, güneş 6,2°)
BÖLÜM SINIRI    G10 — sahne S9 son karesi = sahne S10 ilk karesi; oluk mavi kaplı, bakım yolu + basamaklar tamam, korkuluk YOK,
                dış astar gri, iki vinçte korkuluk demeti, kapaklar kapalı, tekne havuzda, gölge +9°, yaz — ikisinde de aynı [DERS 52]
TEK DOLUM       S13 + S14 + S15 (sahip: "birbirinden kopuk üç dolum değildir") — kaynak aynı boru, yön soldan sağa, kot yalnız
                artar; her kesme öncekinin su cephesini ve seviyesini devralır
TEK GEÇİŞ       S17 + S18 + S19 — aynı tekne, aynı hız, aynı eksen; dönüş, ikinci tekne, yakın plan YOK
```

### Üç zorunlu satır

```
KANIT   "aynı yer" nesnesi: ÇAM — G0'da ve usta karede (G20) aynı konum (x 1475–1547) ve aynı boy (72 px en · tepe 622 · dip
        819) [DERS 25]; kaya çıkıntısında, iğne yapraklı, mevsimle değişmez (çevresindeki yapraklı ağaçlar değişir). Yedek:
        iki ayak (x 844 · 1182 — G0'dan beri hazır).
LOOP    G20 ↔ G0: aynı kadraj · aynı çam · aynı ayaklar · ışık FARKLI (bilinçli — G0 serin sabah, G20 altın saat; tek gün) ·
        ağaçlar FARKLI (açık yeşil → sonbahar): solda havuzda bekleyen kırmızı tekne + boşluk / sağda köprünün ucunda
        aynı tekne + dolu köprü. Biçim kafiyesi: tekne iki karede kanal ekseninde, burnu sağa dönük.
SÖKÜM   S0 kalas kamyonu · S1 serbest kalaslar sağ pedde istif · S2 merkez kalaslar nehir kıyısında yığın → S3 küçük
        kamyonla gider · S3–S11 düz kasalı kamyonlar (kiriş · panel · duvar · uç · boya · bakım yolu · korkuluk), boşalınca
        gider · S12 İKİ VİNÇ (bomlarını indirir, servis yollarından çıkar) + boş paletler + kamyonlar · S13–S16 servis
        aracı gelir-gider · S19 servis aracı gider — ekranda; bakım yolu + korkuluk + basamaklar + boru KALIR (kalıcı)
        [DERS 48 · P2-h]
```

### Malzeme kaynağı ve gizli iş [DERS 48 · P2-g]

```
ELEMAN → KAYNAK (kadrajda nerede birikiyor) → İLK GÖRÜLDÜĞÜ KARE
sol parça               → (önceden kaldırılmış) sol vinçte asılı                                       → G0
sağ parça               → sağ pedde kalaslar üstünde (x 1491–1687) → sağ vinç                           → G0 · G1
merkez parça            → vadi tabanında kalaslar üstünde, nehrin üstünde (x 839–1152) → sol vinç       → G0 · G2
enine kirişler          → düz kasalı kamyonlar (iki ped) → iki vinç                                    → G3 (S2 sonunda gelir)
taban panelleri         → paletler, kamyonlar → iki vinç                                               → G4
duvar panelleri         → kamyonlar → iki vinç (uzak S5 · yakın S6)                                    → G5 · G6
uç parçaları            → kamyonlar → iki vinç                                                         → G7
kaplama variller        → sol pedde kamyon → sol vinç → oluğun içi (mavi S8) · bakım yolu (gri S11)    → G8 · G11
bakım yolu + basamaklar → kamyonlar → iki vinç → konsollar                                             → G9
korkuluk modülleri      → demetler, kamyonlar → iki vinç                                               → G10
SU                      → sol havuzdan dolum borusu (SITE, G0'dan beri) → oluğun sol ucu               → G14
GİZLİ İŞ (kamera görmez) → GÖRÜNÜR VEKİL (prompta yalnız vekil girer):
   cıvatalar ve contalar → panel panel büyüyen yüzey · kaynak/sızdırmazlık testi → kuru, mat kalan oluk (S8–S12) ·
   kapak mekanizması → S16'da çerçevede kalkan kapaklar · su seviyesi ölçümü → bakım yolunda su çizgisine bakan iki kişi (S15)
```

### Final hiyerarşi [P1-h] · kanıt karesi

```
① sağ uçta kırmızı tekne + krem kabin (x 1242–1368 · üstten 549–575, ilk okunan, en sıcak renk) → ② dolu oluğun gök parıltılı
   su bandı + kalkık kapaklar → ③ bütün köprü (kömür grisi, galvanizli korkuluk) iki ayağın üstünde → ④ çok aşağıda nehir
   (x ≈1002) ve gölgedeki vadi tabanı → ⑤ çam (kanıt) + sonbahar yamaçları + sırtlar
FİNAL KARE KANITI  ffmpeg -ss 159.0 -i teslim.mp4 -frames:v 1 kanit.jpg   (S19 tutuşu 156,0–160,0 içinde · altın saat, okunur
                   [DERS 45]) · kart YOK → son kare = G20
```

---

## 🖼️ KARE TABLOSU — 21 görsel [`KILAVUZ_REHBERI` §2.7 · `ZAMAN_VE_ISIK` §2]

> Gölge yönü kadrajda: 0 = kameradan uzağa · − sola · + sağa (|x| > 90 = kameraya doğru). Güneş DİSKİ anılmaz.
> Sayılar `bolum_uretici.py --tablo` çıktısıdır (47° K · δ −9° · güneş saati · kamera bakışı 20°).

| G | SAAT | AZİMUT | YÜKSEKLİK | GÖLGE YÖNÜ | GÖK / BULUT | MEVSİM TAŞIYICISI | YAPI DURUMU (AT THIS STAGE özeti) |
|:-:|:-:|:-:|:-:|:-:|---|---|---|
| G0 | 08:20 | 123° | 15,8° | −77° | serin, ince yüksek bulut | geç ilkbahar · açık yeşil | ⭐ AÇILIŞ — sol parça ASILI · sağ parça pedde · merkez kalasta · tekne havuzda |
| G1 | 08:30 | 125° | 17,2° | −75° | aynı | aynı | sol açıklık oturmuş · sağ parça sapanlı · sol vinç bom ucu dışarıda |
| G2 | 08:40 | 127° | 18,6° | −73° | aynı | aynı | iki yan açıklık · merkez parça kalasta, sol vince sapanlı · sağ bom dışarıda |
| G3 | 08:50 | 129° | 19,9° | −71° | aynı | aynı | ⭐ üç açıklık birleşik, iki kiriş açık · kiriş demetleri vinçlerde |
| G4 | 10:50 | 160° | 31,9° | −40° | küçük bulutlar | yaz · koyu yeşil | ızgara tamam · panel paletleri vinçlerde |
| G5 | 11:00 | 162° | 32,4° | −38° | aynı | aynı | taban kapalı · duvar panelleri vinçlerde |
| G6 | 11:10 | 165° | 32,9° | −35° | aynı | aynı | uzak duvar tamam |
| G7 | 11:20 | 168° | 33,3° | −32° | aynı | aynı | U oluk tamam · uçlarda açık derz |
| G8 | 11:30 | 171° | 33,6° | −29° | aynı | aynı | uçlar bağlı · iç gri astar, KURU · sol vinçte varil paleti, sağ bom dışarıda |
| G9 | 13:30 | 206° | 30,5° | +6° | aynı | aynı | ⭐ iç açık mavi, kuru, mat · bakım yolu parçaları vinçlerde |
| G10 | 13:40 | 209° | 29,7° | +9° | aynı | aynı | ⭐ BÖLÜM SINIRI — bakım yolu + basamaklar · korkuluk demetleri vinçlerde |
| G11 | 13:50 | 211° | 28,9° | +11° | aynı | yaz sonu · ilk sarı lekeler | korkuluk tamam · dış gri astar · sol vinçte varil paleti |
| G12 | 15:50 | 239° | 14,3° | +39° | alçalan sıcak ışık | sonbahar · altın, turuncu, pas | dış KÖMÜR GRİSİ · boş paletler vinçlerde |
| G13 | 16:00 | 241° | 12,8° | +41° | aynı | aynı | saha boş · vinç YOK · oluk KURU · vanada iki kişi |
| G14 | 16:10 | 243° | 11,3° | +43° | aynı | aynı | sığ su (onda bir) sol uçtan sol ayağa |
| G15 | 16:20 | 245° | 9,8° | +45° | aynı | aynı | sığ su bütün boyda, sağ kapağa kadar |
| G16 | 16:30 | 247° | 8,2° | +47° | altın saat başlar | aynı | su dörtte üç, kıyılarla eşit · kapaklar KAPALI · teknede dümenci |
| G17 | 16:40 | 249° | 6,7° | +49° | altın saat | aynı | kapaklar YUKARIDA · tekne havuzda, halat çözülmüş |
| G18 | 16:41 | 249° | 6,5° | +49° | aynı | aynı | tekne köprüde, burnu sol ayakta (620–796) |
| G19 | 16:42 | 250° | 6,3° | +50° | aynı | aynı | tekne merkez açıklıkta (974–1121) |
| G20 | 16:43 | 250° | 6,2° | +50° | ⭐ altın saat | aynı | ⭐ USTA KARE — tekne sağ uçta, burnu sağ kapakta (1242–1368) |

```
SU KOTU DEFTERİ [SU_VE_YANSIMA §8 · P10-e]   (kot duvar yüksekliğinin kesriyle · duvar 2 m · referans: kıyı kanalları +36,5)
   G0–G13   oluk KURU, mat (G0–G8 gri astar · G9–G13 açık mavi) — durgun su YOK [DERS 54] · kanal kolları +36,5, kapakların ardında
   G14      sığ su ≈ onda bir · sol kapaktan SOL AYAĞA kadar (x 538 → 844) · ötesi kuru · yükseliyor
   G15      sığ su ≈ onda bir · bütün boy, SAĞ KAPAĞA kadar (538 → 1398) · yükseliyor
   G16+     dörtte üç (+36,5) · kıyı kanallarıyla EŞİT · su çizgisi uzak duvarda üstten ≈591 · üstünde dar kuru mavi bant · sabit
   ⛔ su hiçbir karede duvarı aşmaz, vadiye akmaz; kaynak tek (boru); yön tek (soldan sağa); düşüş YOK ("never dropping")
   TANIK ÇİZGİ — taşkın yok; dolu seviyenin üstünde kalan dar kuru mavi bant her G16+ karesinde aynı yükseklikte
TEKNE DEFTERİ [SU_VE_YANSIMA §7 · P25-c]   (≈18 m · kanal ekseninde · burnu hep sağa)
   G0–G16   sol havuzda, yakın kıyıya bağlı (x 161–381 · 691–719) · G16'da dümenci kıçta
   G17      halat çözülmüş, kıyıdan hafif açık (aynı x) · kapaklar yukarıda
   G18      köprüde, burnu sol ayakta (s −42…−24 · x 620–796 · 631–653)
   G19      merkez açıklıkta (s −4…+14 · x 974–1121 · 590–609) — altında nehir x 1002
   G20      sağ uçta, burnu sağ kapak çerçevesinde (s +30…+48 · x 1242–1368 · 549–575) — tamamı kadrajda ✓
   klip başına ≈38–40 m (Y ≈1 dk · 0,65 m/s) · dönüş yok · ikinci tekne yok · havada değil, suda ("sits on the water")
VİNÇ DEFTERİ [DERS 8 · 46]   (S = sol vinç · R = sağ vinç · YÜK = kancada görünür yük · DIŞ = bom ucu + halat kadrajın üstünde)
   G0  S YÜK sol parça (asılı) · R YÜK sağ parçaya bağlı dört sapan        G7  S/R YÜK uç parçası
   G1  S DIŞ · R YÜK sağ parça (sapanlı)                                  G8  S YÜK varil paleti · R DIŞ
   G2  S YÜK merkez parça (yayıcı kiriş) · R DIŞ                          G9  S/R YÜK bakım yolu parçası
   G3  S/R YÜK enine kiriş demeti                                         G10 S/R YÜK korkuluk demeti
   G4  S/R YÜK taban paneli paleti                                        G11 S YÜK varil paleti · R DIŞ
   G5  S/R YÜK duvar paneli                                               G12 S/R YÜK boş palet demeti
   G6  S/R YÜK duvar paneli                                               G13+ vinç YOK
   ⚠️ kanca DIŞ → YÜK geçişi klip SONUNDA yazılır (S1 sonu: sol vinç merkez parçaya bağlanır · S7/S10 sonu: sağ bom yukarı) ·
      S12'de bomlar inerken kanca boş — THE FIRST LIGHT S15 emsali, beyanlı
ÜRETİM SIRASI (ters · zincirli · her adımda araclar/zincir_kontrol.sh + kanıt nesnesi ELLE):
   G20 usta kare → G19 (tekne merkezde) → G18 (tekne sol ayakta) → G17 (tekne havuzda, kapaklar yukarıda) → G16 (kapaklar
   kapalı) → G15 (sığ su bütün boy) → G14 (sığ su sol yarı) → G13 (oluk kuru) → G12 (vinçler + paletler geri gelir) →
   G11 (dış gri astar) → G10 (korkuluk yok) → G9 (bakım yolu yok) → G8 (iç gri) → G7 (uçlarda derz) → G6 (yakın duvar yok)
   → G5 (uzak duvar yok) → G4 (taban yok, ızgara) → G3 (ızgara yok) → G2 (merkez parça kalasta) → G1 (sağ parça pedde) →
   G0 (sol parça asılı)
   ⚠️ ters inşada SU ÇEKİLİR (G16 → G13): oluk her adımda KURU ve mat çizilir, ıslak iz bırakılmaz [DERS 54]
   ⚠️ ters inşada PARÇALAR KALKAR (G3 → G0): merkez parça kalaslara, sağ parça pede döner — iki kopya çizilmez, px elle ölçülür
   sonra I2V S0 (G0→G1) … S19 (G19→G20) — her klip iki uca kilitli, üretim 9,0 sn, baştan 1,0 kırp
```

## 🧪 PİLOT ÜÇLÜ [DERS 62 · KILAVUZ_REHBERI §8 adım 2b]

```
⛔ Üretim başlamadan, aşağıdaki üçü geçmeden kalan klipler üretilmez:
① FİNAL      G20 + G19 + G18 + S18 + S19 — tekne yavaşlatılmış zamanda (Y) düz gider, dönmez, kopyalanmaz, suyun içinde
             kalır; altında nehir; S19 son 4 sn TUTUŞ (yalnız iz söner, nehir akar) [C1-b] · Y rejimi burada ilk kez ölçülür
② EN BÜYÜK   G2 + G3 + S2 — 40 m'lik merkez parça vadi tabanından DİMDİK yukarı, tek vinç, dört sapan, tek parça, yavaş;
   DEĞİŞİKLİK  kopyalanmaz, sapandan kopmaz [DERS 8 · 57]; iki ayak kıpırdamaz; kıyılar birleşir (00:16–00:24)
③ SU         G13 + G14 + S13 — kuru mat oluğa borudan gelen ilk sığ su: kaynak görünür, yön soldan sağa, kot onda bir,
             duvarı aşmaz, oluk "belirmez" — dolumun geri kalanı (S14–S15) bunun üstüne kurulur
PİLOT SONRASI İLK  S0 (G0 · G1 — açılış: askıdaki sol parça 0. saniyede iniyor mu) + S14 · S15 (tek dolumun devamı)
```

---

## ☀️ GÜNEŞ SAATİ VE MEVSİM [`ZAMAN_VE_ISIK` §2 · §6 · §7]

```
ENLEM / YÖN     47,0° K · ışık günü tarihi: δ −9° (ekim ortası — ışık tek gün; takvim sahadan) · doğuş ≈06:39 · batış ≈17:21
                (güneş saati) · kamera bakışı 20° (KKD) → kadraj −17° … +57° azimut · güneş 123° → 250°: sabah kameranın
                SAĞINDA ve biraz arkasında (bağıl +103°), öğle arkada sağda, öğleden sonra arkada solda (bağıl −130°) —
                HİÇBİR karede kadrajda değil, ters ışık YOK [P8-h]
KÖPRÜ IŞIĞI     köprünün yakın yüzü kameraya (GGB) bakar → sabah yandan (sağdan, gölgeler sola), öğle arkadan, öğleden sonra
                arkadan-soldan sıcak · altın saatte (G16–G20) köprü, yamaçlar ve tekne sıcak ışıkta, vadi tabanı gölgede
GÖLGE SÜPÜRMESİ rejim B klipte: S3 (−71° → −40°: 31°) · S8 (−29° → +6°: 35°) · S11 (+11° → +39°: 28°) · rejim A klipte fark
                edilmez → yüzeyle kanıtlanır · Y klipte (1 dk) sabit
MEVSİM YAYI     geç ilkbahar (G0–G3: açık yeşil) → yaz (G4–G10: koyu yeşil) → yaz sonu (G11: ilk sarı lekeler) → sonbahar
                (G12–G20: altın, turuncu, pas) · taşıyıcı: YAMAÇLARDAKİ YAPRAKLI AĞAÇLAR (LIGHTING bloğunun mevsim cümlesi;
                SITE bloğu birebir kalsın diye orada) · çam iğne yapraklı, değişmez (kanıt)
KIŞ             görüntü YOK · DERS 7 tetiklenmez
GECE            yok · final ALTIN SAAT, güneş 6,2° (G20) · tekne, su ve aşağıdaki boşluk küçük ekranda okunur [DERS 45]
```

---

## 🔐 MASTER LOCK — üretime giren sayılar (SPEC §2-§3 ile aynı)

```
KAMERA   ANA h +85,0 · D_eksen 135,0 · D_kenar ≈107 (çam) · bakış 20° · tilt 17° aşağı · roll 0 · köprü ekseni 20°
YAPI     sol mesnet 538 · 670 · sol ayak 844 · 684–882 · sağ ayak 1182 · 636–819 · sağ mesnet 1398 · 561 · oluk merkez
         587 / 603 / 609 · kiriş altı 656 · kapak çerçeveleri 529 · 589 / 1383 · 497
SU       kuru G0–G13 · onda bir G14–G15 · dörtte üç (+36,5, uzak duvarda 591) G16+
TEKNE    havuz 161–381 (G0–G17) · 620–796 (G18) · 974–1121 (G19) · 1242–1368 (G20)
ÇAPALAR  ① ÇAM x 1475–1547 · 622–819 (kanıt nesnesi 72 px) · ② iki ayak · ③ nehir x 1002 · 888 · ④ ufuk 149 · ⑤ kanal kolları + boru
IZGARA   20 × 8,0 · kesmeler 8,0 · 16,0 · … · 152,0  (19 kesme, her 8,0 sn) · kart YOK · 160,0 sn · 120 BPM
```

## 🧾 ÜRETİM ÖNCESİ DURUM

```
✅ prompt kapısı  python3 araclar/prompt_kontrol.py yatay_2_dk_filmler/THE_SKY_CANAL   → sonuç QA_SPEC §8'de (11.10.2026)
✅ FIX'ler ve beyanları (hepsi elle okundu):
   · ARAÇ KUTU SETİ ölçülmedi — beyanlı; üretim araç kapısıyla açılır
   · süreler eşit (8,0) — düz ızgara (sahip senaryosu, SAPMA ②); beş mercekte ❷ RHYTHM eşit klipte tetiklenmez
   · REJİM Y (≈1 dk) kapı sözlüğünde yok — S17 · S18 · S19 görsel + I2V + G20 = 7 FIX, beyanlı (hikâye SAPMA ⑩ · PİLOT ①)
✅ YASAK KELİME taraması 0 · kelime kilitleri (crane G0–G12 · oluk suyu S13+ · blue S8+ · charcoal S11+ · raised S16+ ·
   glides/wake S17+) betikle doğrulandı (11.10.2026 · 41 blok)
✅ 00_ANALIZ yedi dosya · hikâye onayı 11.10.2026 (TUR 1 · SAPMA ①–⑱ sahip okur)
⛔ ARAÇ KAPISI koşulmadı → THE_SKY_CANAL_URETIM_GUNLUGU.md §0
⛔ PİLOT ÜÇLÜ koşulmadı → S18 + S19 · S2 · S13
⛔ SÜRE / KLASÖR — 160 sn yatay_2_dk bandının dışında (SAPMA ②) → sahip kararı
```
