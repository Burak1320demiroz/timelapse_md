# 🤖 AGENTS.md — Ajan Çalışma Kontratı

> **Bu dosyayı her görevden önce oku.** Amacı sana içerik öğretmek değil,
> **nereye yazacağını** söylemek. Ne yaptığını anlatan kılavuzlar ayrı yerde
> durur; burası "hangi olay olduğunda hangi dosyalar değişir" haritasıdır.
>
> **Kural:** Bu dosyaya sayı yazma. Sayı isteyen her cümle kaynağa işaret eder.
> Bir sayıyı iki yerde tutmak, birini yanlış tutmaktır.

---

# 0. İLK 60 SANİYE

```
1. bash araclar/sayac.sh              → gerçek durum
2. kilavuzlar/KILAVUZ_REHBERI.md      → üretim bilgisi
3. §2 görev kartlarından kendi görevini bul
4. git status                          → temiz mi başlıyorsun
```

**Kılavuz okumadan film yazma. Görev kartı okumadan dosya güncelleme.**

---

# 1. DEPO HARİTASI

```
timelapse_md/
├── AGENTS.md · CLAUDE.md · README.md
│
├── kilavuzlar/                      ⭐ SİSTEMİN BEYNİ
│   ├── KILAVUZ_REHBERI.md           ⭐ BURADAN BAŞLA — karar ağacı · format kartı
│   │                                   · DEĞİŞMEZLER · AŞAMA MERDİVENİ · güneş
│   │                                   saati · konsept kapısı · negatif çekirdek
│   │                                   ⭐ §2.7 İKİ KEYFRAME ZİNCİRİ — FORMATIN
│   │                                     KENDİSİ: foto–video–foto · N+1 görsel
│   │                                   · üretim akışı (ters inşa) · tuzaklar
│   ├── TIMELAPSE_SISTEM_PROMPTU.md  ⭐ MOTOR — depo İÇİNDE film yazarken
│   │                                   (GPT'ye gitmez) · 10×6,0
│   ├── YAPI_TIPI_KARTLARI.md        kule · konut · köprü · baraj · stadyum ·
│   │                                   yol/tünel · liman · türbin · villa
│   ├── SAHA_VE_IKLIM_KARTLARI.md    şehir · kırsal · kıyı · dağ · kar · çöl
│   ├── ZAMAN_VE_ISIK_KILAVUZU.md    iki saat · güneş satırı · 10 sn bütçesi
│   ├── KAMERA_ISTASYONU_KILAVUZU.md hibrit mimari · kadraj HESABI · güvenli alan
│   ├── PROMPT_SABLONU.md            görsel + İKİ UÇLU I2V iskeleti · ⛔ T2V YOK
│   ├── MUZIK_VE_KAPAK.md            BPM ızgarası · katman=kat · 120 px testi ·
│   │                                   paketleme · GERÇEKLİK BEYANI
│   ├── DIKEY_TIMELAPSE_KAPAK_KILAVUZU.md ⭐ dikey kapak: çekirdek 780×840 · başlık kutusu ·
│   │                                   3:4/4:5/1:1 provası · §0 depo uyarlaması (16.10.2026)
│   ├── KAPAK_STIL_KILAVUZU.md       ⭐ dikey kapağın GÖRÜNÜŞÜ: üç orta başlık bandı (Ü·O·A) · ışık reçetesi R1–R3 ·
│   │                                   ışık varyantı I0/I1/I2 (GN kadrajı sabit, ileri saat) · stil S1–S4 (25.10.2026)
│   │  ── ikinci kuşak · 08.09.2026 · A5–A8 araştırmasından doğdu ──
│   ├── INSAAT_YONTEMI_KILAVUZU.md   ⭐ ara hâller (%25/%50/%75) · geçici ekipman
│   │                                   · okunabilirlik eşiği 0,5 m · ⑧'in kapısı
│   ├── SANTIYE_HAREKETI_KILAVUZU.md ⭐ SIKIŞTIRMA REJİMİ (A·B·C) · gölge süpürmesi
│   │                                   · sekiz yüzey kanıtı · ⑦'nin kapısı
│   ├── ARAC_KARTLARI.md             ⛔ BOŞ AÇILIR · kutu seti · sahne tavanı ·
│   │                                   SEKİZ soruluk ölçüm · negatifin yeri
│   ├── KURGU_VE_TESLIM_KILAVUZU.md  ⭐ kırpma bütçesi · TOP-N kesme kanıtı ·
│   │                                   yedi ölçümlük yayın öncesi QC
│   │  ── üçüncü kuşak · 11.09.2026 · A9–A12 araştırmasından doğdu · §10d kapısı ──
│   ├── MALZEME_VE_DOKU_KILAVUZU.md  SITE TEXTURE · korpus üçlüsü · BANT kuralı ·
│   │                                   saha kartı · malzeme = saat
│   ├── FIZIK_VE_AGIRLIK_KILAVUZU.md PHYSICS · yük yolu · söküm fiili · hammadde
│   │                                   yığını · robotik gövde · ihlal sözlüğü
│   ├── PERSPEKTIF_VE_OLCEK_KILAVUZU.md COMPOSITION · referans nesne (px) · kesir
│   │                                   cümlesi · sayı testi · kanal (sınır: KAMERA)
│   ├── HAVA_VE_ATMOSFER_KILAVUZU.md TIME RATE + LIGHTING · üç rejim × gök ·
│   │                                   iki kare arası gök/gölge · altı taşıyıcı
│   │  ── dördüncü kuşak · 17.09.2026 · A13–A18 araştırmasından doğdu ──
│   ├── KAMERA_HAREKETI_KILAVUZU.md  ⭐ "kamera hareketi" istendiğinde hangi KATMAN:
│   │                                   üretim (sabit) · kurgu (yakınlaşma · HOME
│   │                                   paketi · çözünürlük kapısı) · kadraj içi
│   │                                   ⛔ katman 2 ÖLÇÜLMEDİ — sahip kararı
│   │  ── beşinci kuşak · 18.09.2026 · 15 filmin ÇAPRAZ ANALİZİNDEN doğdu (C1) ──
│   ├── SAHNE_PLAN_KARTI.md          ⭐ BEŞ SORU prompttan ÖNCE: malzeme nerede · taşıyıcı ·
│   │                                   nereye oturur · ne değişti · ne sabit → I2V MOTION
│   │                                   FOCUS · kapısı prompt_kontrol.py §10e (FIX)
│   │  ── altıncı kuşak · 20.09.2026 · A19 dış raporundan doğdu (sahip köke bıraktı) ──
│   ├── KAMERA_DILI_KILAVUZU.md      ⭐ istasyondan ÖNCE: karar cümlesi · DEĞİŞİM BOYUTU →
│   │                                   BAKIŞ AİLESİ · ⭐ TİLTLİ KADRAJ FORMÜLÜ (aşağı bakış
│   │                                   ailesi · KAMERA_ISTASYONU §3 yalnız tilt 0) · katsayı
│   │  ── yedinci kuşak · 06.10.2026 · A20–A24 araştırmasından doğdu · QA ONARIMI ──
│   ├── QA_KOSU_KILAVUZU.md          ⭐ kör mercek GEÇİCİ SOHBETTE, proje/Gem DIŞINDA (Gem dosyaları
│   │                                   her sohbete girer) · geri okuma · sızıntı · fail closed
│   ├── QA_OLCUM_ZEMINI_KILAVUZU.md  ⭐ model SAYMAZ: süre · hız · kesme · kart ÖLÇÜLMÜŞ OLGULAR
│   │                                   bloğuyla rubriğin İÇİNDE · top-N kalır · D1–D5
│   ├── RUBRIK_YAZIM_KILAVUZU.md     format değişkenleri · kanıtsız en fazla 7 · ortalama kodda ·
│   │                                   KÖTÜ OLAN KAZANIR · kusur sahipliği · temizlik listesi
│   ├── QA_KALIBRASYON_KILAVUZU.md   test-tekrar pilotu 3×4×3 · tohumlanmış kusur seti (sınandı) ·
│   │                                   çapa film · QA ↔ izleyici (ρ 0,5 için 29–30 film)
│   ├── QA_KAYIT_KILAVUZU.md         durum modeli · künye · eşleme tablosu (ham dokunulmaz) ·
│   │                                   tek ad şeması · uzlaştırma U1–U10
│   │  ── sekizinci kuşak · 07.10.2026 · A25–A29 araştırmasından doğdu · THE SLOW TAKEOFF yazımı ──
│   ├── UZUN_FORM_ANLATI_KILAVUZU.md ⭐ yatay 2–8 dk: MERAK ZİNCİRİ · ilk büyük sonuç ≈ 30 sn ·
│   │                                   en büyük soru en son · son ekran 5–20 sn · eğri → sahne
│   ├── ISTASYON_VE_IC_MEKAN_KILAVUZU.md ikinci sabit kamera: dört şart · dikey EK / yatay KLİP ·
│   │                                   paralel zaman zinciri · mekân kesmesi bölütlemez · iç mekân dili
│   ├── SU_VE_YANSIMA_KILAVUZU.md    ⭐ yansıma x = D·h/(h+y) · Fresnel · Beaufort · SU KOTU DEFTERİ ·
│   │                                   tanık çizgi · taşıt yolu ≤ 13 m / 8 sn
│   ├── ISIK_FINALI_KILAVUZU.md      mavi saat dakika tablosu · A/B'de ışık TEK KAREDE yanar ·
│   │                                   IŞIK DEFTERİ · olumsuzlama çağırır (NegT2IBench)
│   ├── ONARIM_VE_YENIDEN_URETIM_KILAVUZU.md ⭐ hüküm → kök neden → tek eylem · kare değişirse iki
│   │                                   klip · iki dikiş sınanır · zincirde inpainting YOK · 3/6
│   │  ── onuncu kuşak · 15.10.2026 · A35–A38 & THE SKY STATION QA (DERS 65–84) doğurdu ──
│   ├── MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md ⭐ Bounding Box · STRICT ZONE IMMUNITY ·
│   │                                   ⛔ truss yok · Exit Before Swap · N_max = 1 · Void Immunity
│   │  ── on birinci kuşak · 15.10.2026 · A39–A42 araştırmasından doğdu ──
│   ├── MONOTONIK_ILERLEME_VE_FAZ_KAPISI_KILAVUZU.md ⭐ ara hâl aşımı (yo-yo) · dC/dt ≥ 0 · COMMITTED BASELINE
│   │                                   · sıfır kaymalı demirleme · faz kapısı (IRREVERSIBLE GATE) · 8s WBS
│   │                                   · 3 fazlı kurgu · çoklu etki (≥3 el) · nöroestetik mikro-doyum (5.5-7s)
│   ├── FILM_KLASOR_SABLONU/         ⭐ yatay iskeletin kopyalanabilir hâli (§2.8) —
│   │                                   film_klasoru_ac.sh buradan kopyalar; kapı atlar
│   ├── DERSLER.md                   ⭐ yalnız ÖLÇÜLMÜŞ dersler (DERS 1–64) + film blokları
│   │                                   ⭐ DERS 35-44 · altıncı film (THE DUST YEAR)
│   │                                     yedisinin kapısı prompt_kontrol.py §10c'de
│   ├── VARSAYIMLAR.md               🆕 08.10.2026 · D · A · F1 · C kodları — ölçülmemiş ·
│   │                                   DİZİN'de DURUM sütunu: ⬜ açık · ✅ ölçüldü · ❌ düştü
│   └── PLAN_OKUMALARI.md            🆕 08.10.2026 · P kodları — uzman okumaları (P1 · P2) ·
│                                       plan kararları (P3…P25) · aynı DURUM sütunu
│
├── dikey_shorts/                    9:16 · film klasörleri
│   └── <PROJE>/
│        ├── <PROJE>_DIKEY_TIMELAPSE.md   plan + promptlar + müzik + paket
│        ├── <PROJE>_QA_SPEC.md           kilit listesi + FİNAL KARE KANITI satırı
│        └── <PROJE>_KAPAK.md             kaynak kare + kapak promptu + başlığın
│                                          dizilişi (sayıyla) + testler
│   ⭐ URETIM_GUNLUGU_SABLONU.md   klip başına üretim kaydı · QA paketinin kapısı [DERS 28]
│   ⛔ FİLM BU DEPODA YAZILIR. Harici bota sipariş verme yolu (siparisler/)
│      02.09.2026'da kapatıldı; ölçülmüş içeriği KILAVUZ_REHBERI §2.6'da.
│
├── yatay_2_dk_filmler/              ⭐ 14.09.2026 · YATAY 16:9 MERDİVENİ — film_md'nin film
├── yatay_4_dk_filmler/                 klasörü şablonu, BU deponun kılavuz ve dersleriyle
├── yatay_6_dk_filmler/                 (KILAVUZ_REHBERI §2.8). Sahne sayısı ve ızgara: her
├── yatay_8_dk_filmler/                 klasörün README'si. Köke yalnız README; sayaç uyarır.
│   └── <FILM>/
│        ├── 00_ANALIZ/                 yazımdan ÖNCE: 00_HIKAYE_ONAYI (sahip onayı) · okuma
│        │                              çizelgesi · ders hasadı · konsept+risk · sıralama ·
│        │                              uyarılar · 05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU
│        ├── <FILM>_PLAN.md             değişmezler · merdiven · kare tablosu — ⛔ PROMPT YOK
│        ├── <FILM>_BOLUM_1.md          sahne blokları (görsel + I2V) · ilk yarı
│        ├── <FILM>_BOLUM_2.md          ikinci yarı + ## 🌟 USTA KARE (GN)
│        ├── <FILM>_KAPAK.md · _MUZIK.md · _YAYIN_PAKETI.md (İngilizce) · _QA_SPEC.md
│        └── <FILM>_URETIM_GUNLUGU.md   ÜRETİM doldurur · qa_paket.sh kapısı [DERS 28]
│   ⛔ Klasör ELLE açılmaz: bash araclar/film_klasoru_ac.sh <FMT> <FILM>
│   ⛔ Kapı KLASÖR MODUNDA: python3 araclar/prompt_kontrol.py <FMT>/<FILM>
│
├── QA/                              🔍 BEŞ MERCEK · ÜRETİMDEN SONRA · ⭐ 06.10.2026 yeniden kuruldu
│   ├── 00_README.md                 ⭐ beş mercek · çalıştırma · rapor geldiğinde · klasör
│   ├── Q1_GORUNTU.md                ❶ tek kamera, tek timelapse · görüntü katı mı · mod V
│   ├── Q2_ZAMAN_KESME.md            ❷ zaman tek yönde · kesme "zaman" mı · mod V (+ ölçülmüş olgular)
│   ├── Q3_SANTIYE.md                ❸ her kesmede aynı dünya · şantiye çalışıyor mu · mod V
│   ├── Q4_INSA.md                   ❹ SPEC'teki yapı · parça parça · davetli kadro · mod D
│   ├── Q5_TESLIM.md                 ❺ vaat · final vuruşu · kanca · döngü · kapak · mod D
│   ├── TABLO.md                     ⭐ TEK SAYAÇ + film × mercek (her hücre bir hama bağlı)
│   ├── HAM/<FILM>/                  modelin ham çıktısı + künye ⛔ DOKUNULMAZ
│   ├── FILMLER/<FILM>.md            film başına kayıt · olay tablosu · karar · ders
│   └── ARSIV_12_MERCEK/             ⛔ DONDURULDU · 12 mercek · 393 ham · 31 rapor · INDEX ·
│                                       çapraz analiz · 00_ARSIV.md (temizlenmiş puanlar) ·
│                                       00_ESLEME.tsv (her ham → durum)
│
├── apexait/                         📺 KANAL — QA'dan sonrası · ÜÇ HESAP
│   ├── README.md                    yapı · okuma sırası · açık işler
│   ├── KANAL_KIMLIGI.md             ⭐ üçünde de aynı: tez ("her film bir
│   │                                   BEDEL gösterir") · kanal negatif
│   │                                   çekirdeği · palet · logo şartnamesi
│   ├── YAYIN_PLANI.md               ⭐ üçünde de aynı: kadans · iki ayak ·
│   │                                   siluet sırası · film havuzu · ölçüm
│   ├── CAPRAZ_YAYIN.md              ⭐ üçünde de aynı: tek master · filigran
│   │                                   yasağı · C2PA · güvenli alan zarfı
│   ├── IZLEYICI_DEFTERI.md          7. gün sayıları · paylaşım ve yorum türü
│   ├── TUR_HARITASI.md              2025–2026 dış vaka havuzu · harita ÇIKMADI
│   │                                   kaydı · vaka defteri [A30 · 07.10.2026]
│   ├── youtube/                     POLITIKA_VE_RISK · PAKETLEME_SABLONU
│   ├── instagram/                   HESAP_KIMLIGI  · PAKETLEME_SABLONU
│   └── tiktok/                      HESAP_KIMLIGI  · PAKETLEME_SABLONU
│   ⛔ Kökteki üç dosya platform klasörlerine KOPYALANMAZ (CAPRAZ_YAYIN §5)
│
├── arastirma/                       🔬 DIŞARIDAN BİLGİ · üretimden ÖNCE
│   ├── 00_README.md                 ⭐ dört promptun akışı · sonuç geldiğinde
│   │                                   ne yapılır (ham kayıt → etiket → ders)
│   ├── A1_VIRAL_ANATOMI.md          ne yayılıyor · paketleme · süre · kapak
│   ├── A2_RITIM_VE_TUTUNMA.md       kanca · kesme varyansı · loop · ses
│   ├── A3_ZINCIR_VE_TUTARLILIK.md   ⭐ aynı bina · aynı kamera · aynı hız
│   ├── A4_GERCEKLIK_IMZASI.md       timelapse fiziği · mevsim taşıyıcısı ·
│   │                                   AI işaretleri · beyan politikası
│   ├── A5_INSA_YONTEMI.md        ⭐ eleman eleman yapım sırası · ara hâller
│   ├── A6_SANTIYE_HAREKETI.md       ACTIVITY kaynağı · iz · yüzey kanıtı
│   ├── A7_ARAC_PROFILI.md           aracın ölçülmüş davranışı · test protokolü
│   ├── A8_KURGU_VE_TESLIM.md        kesme · dikiş · final · kapak · teslim QC
│   │  ✅ A5–A8 08.09.2026'da koşuldu; dördü de bir kılavuz doğurdu
│   │     (INSAAT_YONTEMI · SANTIYE_HAREKETI · ARAC_KARTLARI · KURGU_VE_TESLIM).
│   ├── A9_MALZEME_VE_DOKU.md        yüzey · kirlilik katmanı · yaşlanma (v2)
│   ├── A10_FIZIK_VE_AGIRLIK.md      yük yolu · söküm · robotik gövde · katılık (v2)
│   ├── A11_PERSPEKTIF_VE_OLCEK.md   referans nesne · sayı sadakati · kanal (v2)
│   ├── A12_HAVA_VE_ATMOSFER.md      bulut × rejim · derinlik · iki kare arası gök (v2)
│   │  ✅ A9–A12 11.09.2026'da koşuldu; dördü de bir kılavuz doğurdu
│   │     (MALZEME_VE_DOKU · FIZIK_VE_AGIRLIK · PERSPEKTIF_VE_OLCEK · HAVA_VE_ATMOSFER).
│   └── SONUCLAR/A9-A12_DENETIM.md   ⭐ 12 kaynak çekildi: 7 tuttu · 4 yanlış atıf ·
│         gölge 15°/saat ikinci kez düştü · piksel tabloları tuttu.
│         ⛔ Yeni arıza sınıfı: kaynak VAR ama iddiaya AİT DEĞİL.
│   ├── SONUCLAR/A19_DENETIM.md      ⭐ 20.09.2026 · kökteki kamera rehberi taşındı: 11 kaynağın
   │                                   10'u çekildi ve tuttu · yeni sayı yok · tiltli formül açığı
   ├── SONUCLAR/                    ham bot çıktısı ⛔ DOKUNULMAZ
│   └── SONUCLAR/A5-A8_DENETIM.md    ⭐ dört raporun doğruluk denetimi:
│         üç sayı yeniden hesaplandı ve düştü · iki ffmpeg komudu koşmadı ·
│         bir eşik kör çıktı. ⛔ Rapordan doğrudan inen SAYI yoktur.
│   ⛔ Araştırma bulgusu DERS DEĞİLDİR. En fazla gerekçeli varsayımdır ve
│      VARSAYIMLAR.md'ye A<n>-x koduyla girer (kuşak bölümü + DİZİN satırı ⬜ açık).
│
└── araclar/
    ├── sayac.sh                     sayıları dosya sisteminden hesaplar
    ├── prompt_kontrol.py            ÜRETİMDEN ÖNCE koşan kapı · çıkış 2 = BLOCK
    ├── zincir_kontrol.sh            ⭐ ÜRETİM ARASI kapı · her kareden sonra · 3. argüman = ana
    │                                   referans (GN) · px kayma eşiğini basar (KAMERA_ISTASYONU §7)
    ├── capraz_sayim.py              QA_CAPRAZ_ANALIZ skor matrisini yeniden hesaplar
    ├── kare_al.sh                   ① ve ⑤ için kare grabları
    ├── qa_paket.sh                  ⭐ QA KOŞU PAKETİ · beş mercek · ölçülmüş olgular rubriğin İÇİNDE · --master · günlük kapısı [DERS 28-29 · 63]
    ├── kesme_kontrol.sh             ⛔ YAYIN ÖNCESİ · kurgu SÜRE sütununa uydu mu · --hiz 2 [DERS 31 · 63]
    ├── ihrac_kontrol.sh             ⛔ PAYLAŞIMDAN ÖNCE · süre/hız · kart · final tutuşu · müzik/yazı listesi [DERS 63]
    └── film_klasoru_ac.sh           ⭐ yatay film klasörünü şablondan açar, sahne satırlarını
                                        damgalar, okuma çizelgesini üretir (kart Y2)
```

**Format kartı, yapı/saha kartları, negatif çekirdek → hepsi `KILAVUZ_REHBERI.md`
ve komşularında. Burada tekrarlanmaz.**

---

# 2. GÖREV KARTLARI

## 🏗️ A — YENİ FİLM YAZACAĞIM

```
0. IZGARA             ⛔ DİKEY = KESİN 7 SAHNE × 8,0 sn = 56,0 sn (sahip kuralı 05.10.2026 · DERS 58).
                      Üretilir 1x, PAYLAŞILIR 2x (~28 sn + kart planda varsa). Brief 6 ya da 8
                      sahne verirse plan yine 7 ile yazılır ve bu sahibe söylenir. Kapı BLOCK'lar.
                      (yatay: kart G · Y2)
1. KONSEPT KAPISI     KILAVUZ_REHBERI §6 — VAAT / DİRENÇ / BEDEL + üç test.
                      ⛔ Üçü de ✅ değilse klasör AÇILMAZ.
2. KART SEÇİMİ        YAPI_TIPI_KARTLARI (inşa sırası) + SAHA_VE_IKLIM_KARTLARI
                      ⭐ + INSAAT_YONTEMI §3 — her merdiven satırı bir ELEMAN
                        ve bir ARA HÂL (%25/%50/%75) taşır [A5-a]
3. DEĞİŞMEZLER        §3'ün dört kutusu doldurulur. Kamera sayıları
                      KAMERA_ISTASYONU §3 formülünden ÇIKAR, seçilmez.
                      ⛔ YAPI BIBLE'ın HER satırı bir SAYI taşır [DERS 19].
4. AŞAMA MERDİVENİ    §4 tablosu (ızgara kaç sahneyse o kadar SATIR) + üç
                      zorunlu satır (KANIT · LOOP · SÖKÜM) · kış İKİ sahne
5. GÜNEŞ SAATİ        ZAMAN_VE_ISIK — mevsim yayı ve temsil süreleri
                      ⛔ Açı ve yükseklik I2V'ye de yazılır [DERS 18].
6. TESLİM YAPISI      ⛔ sahne bloğu + KAPAK KARTI (⭐ 16.10.2026: HER filmde SONDA, GN'den, süresiyle) + MÜZİK (dikey: ⛔ YOK)
                      AYRI satırlarla beyan edilir. Beyansız kart QA'yı çökertir [DERS 4];
                      beyan ihracta ihrac_kontrol.sh ile ölçülür [DERS 63].
6a. İZLEYİCİ KAPISI  ⛔ künyeye İŞLEV ANI · AÇILIŞ NESNESİ · DÖNGÜ KAFİYESİ · MERAK SORUSU satırları
                      · S0 = AÇILIŞ DÜZENİ (nesne · dokunuş · ipucu · ölçek; eylem "from the first
                      frame") · her klipte İŞ YOĞUNLUĞU (≥3 el · malzeme akışı · arka plan hazırlığı)
                      [KILAVUZ_REHBERI §6 · SANTIYE_HAREKETI §4.8 · C2]
                      ⭐ SEÇENEK: S0 GERİ ÇEKİLME AÇILIŞI (yakın ayrıntı → HOME, kurgu kırpması) —
                      plana 'AÇILIŞ GERİ ÇEKİLMESİ ✅/⛔' + tavan satırları [KAMERA_HAREKETI §4.2 · C2-i]
                      [KILAVUZ_REHBERI §6 · C2] · final klibi 4 sn olay + 4 sn tutuş [§8 adım 9]
6b. YASAK KELİME      ⛔ künyeye 'YASAK KELİME  a · b · c' satırı [DERS 59]: filmin istemediği her
                      nesne (vinçsiz: crane · hoist · jib · derrick · tarihi: truck · machinery ·
                      Ay: flame · smoke · thrust · plume). HİÇBİR promptta, NEGATİFTE BİLE geçmez —
                      kelimeyi anmak nesneyi çağırır. Yasak yoksa: 'YASAK KELİME  — (yok)'.
6c. ÜRETİM GÜNLÜĞÜ    ⛔ plan yazılırken açılır: cp dikey_shorts/URETIM_GUNLUGU_SABLONU.md
                      dikey_shorts/<PROJE>/<PROJE>_URETIM_GUNLUGU.md — yoksa kapı BLOCK [DERS 62]
7. KLİP SÜRESİ        ⛔ ÖLÇ: ffprobe ile test klibi. Izgarayı ondan yaz.
                      ⭐ Süreler KUTULUDUR [A7-a]. Plana ARAÇ KUTU SETİ satırı
                        yazılır ve sahne tavanı = (en büyük kutu − 1,00 sn)
                        aşılmaz [ARAC_KARTLARI §2]. Aşılırsa prompt kapısı BLOCK.
7b. SAHNE PLAN KARTI  ⭐ SAHNE_PLAN_KARTI — klip başına BEŞ SORU cevaplanır
                      (yatay: 00_SAHNE_TABLOSU sütunu · dikey: kare tablosu + günlük).
                      ⛔ Beş sorusu cevaplı olmayan sahnenin promptu yazılmaz [C1-a].
8. PROMPTLAR          PROMPT_SABLONU iskeletiyle · ⭐ 2N+1 prompt:
                      N+1 GÖRSEL (G0…GN · sonuncusu USTA KARE, ayrı bölümde)
                      + N I2V · ⛔ T2V YOK [KILAVUZ_REHBERI §2.7]
                      ⛔ Her I2V'nin İKİ UCU da birebir cümleyle kilitlenir;
                        kapı ikisini de arar · blok ETİKETLERİ birebir [DERS 20]
                      ⭐ AT THIS STAGE'e INSAAT_YONTEMI §5'ten ara hâl cümlesi
                      ⭐ TIME RATE'e SIKIŞTIRMA REJİMİ (A·B·C) beyanı [A6-a]
                      ⭐ ACTIVITY'ye iki hareket eden + bir yüzey kanıtı [A6-d]
                        — sayı değil ANA İŞE hizmet [C1-d]
                      ⭐ I2V'ye MOTION FOCUS paragrafı (kartın ①②③④'ü) [C1-c]
                      ⛔ FARK = HAREKET [DERS 61]: G(n+1)'de olup G(n)'de olmayan HER büyük eleman
                        o klibin MOTION FOCUS'unda adıyla, kaynak → taşıyıcı → hedef. Anamıyorsan
                        eleman o klibe ait değildir — merdiven bölünür.
                      ⛔ 'vanish · disappear' inşaat nesnesine yazılmaz; TAŞIYAN yazılır [DERS 61]
                      ⛔ metin yasağı yalnız SAHADA OLAN yüzeyi sayar ya da 'on any surface' der [DERS 59]
                      ⛔ havasız sahada flame · smoke · exhaust · thrust · jet · plume YOK [DERS 60]
                      ⛔ PİLOT ÜÇLÜ bölümü final klibi S6'yı ve en büyük değişikliğin klibini adıyla
                        anar [DERS 62]
8b. KAMERA HAREKETİ?  "hareket" isteniyorsa ÖNCE KAMERA_HAREKETI_KILAVUZU §0:
                      istek kadraj içi mi, kurgu yakınlaşması mı. Yakınlaşma
                      varsa plana KURGU bölümü + araç kapısına çözünürlük ölçümü.
9. MÜZİK + KAPAK      MUZIK_VE_KAPAK — 120 BPM (3 ölçü/sahne) · kapak SON
                      sahnenin usta karesinden türer ve ⭐ İNGİLİZCE BAŞLIK taşır
                      ⭐ DİKEY: DIKEY_TIMELAPSE_KAPAK_KILAVUZU §0 · §3 — GN ana yapı y %29–58,
                      başlık bandı Ü/O/A + ışık + stil → KAPAK_STIL_KILAVUZU §2 · §3 · §4 (plan kadraj tablosuna
                      yazılır · ⛔ en üstte/en altta değil) · kapak = SON KART
10. PAKETLEME         ⛔ başlık/açıklama/hashtag/yorum İNGİLİZCE
11. QA_SPEC           kilit listesi + ⛔ FİNAL KARE KANITI satırı
12. PROMPT KAPISI     python3 araclar/prompt_kontrol.py <dosya>

DOSYA:  dikey_shorts/<PROJE>/<PROJE>_DIKEY_TIMELAPSE.md
        ⭐ YATAY (16:9): kart Y2 — aynı adımlar, sekiz dosyalı iskelet + 00_ANALIZ;
          plan <FMT>/<FILM>/<FILM>_PLAN.md, promptlar _BOLUM_1/_BOLUM_2 [KILAVUZ_REHBERI §2.8]
```

## 🤝 G — IZGARA SEÇİMİ (dikey: SEÇİLMEZ — 7 × 8,0 · yatayda modül)

```
⛔ 05.10.2026 · SAHİP KURALI [DERS 58]: DİKEY SHORTS KESİN 7 SAHNE × 8,0 sn = 56,0 sn.
   Üretilir 1x, paylaşılır 2x. Aşağıdaki 10 × 6,0 / 5 × 6,0 kaydı TARİHÇEDİR — yeni dikey
   planda kullanılmaz. prompt_kontrol.py dikeyde 7 dışını, 8,0 dışını ve künyede
   'IZGARA     7 sahne × 8,0 sn = 56,0 sn' satırı olmayanı BLOCK'lar.
```

```
⭐ YATAY MERDİVEN (14.09.2026): ızgara formattan gelir, seçilmez — sahne sayısı ve klip süresi
   klasörün README'sinde ve KILAVUZ_REHBERI §2.8'de. Bandın dışı = sahip izni + PLAN'a gerekçe.
   Düz ızgara sahip beyanıdır; karşı kayıt (DERS 13 · 24 · 44) PLAN §DÜZ IZGARA BEYANI'nda durur.
```

```
⛔ 02.09.2026: HARİCİ BOTA SİPARİŞ VERME YOLU KAPATILDI. `siparisler/`
   kaldırıldı. Film artık yalnız kart A ile, DEPO İÇİNDE yazılır.
   Sebep: harici bot deponun hiçbir dosyasını okuyamıyordu ve uzun brief
   botu kendi düzenini kurmaya itiyordu — blok etiketleri nesre dönüyor,
   hem kural hem prompt kapısı düşüyordu [DERS 20].

VARSAYILAN     10 × 6,0 = 60,0 sn + kapak 5,0        KILAVUZ_REHBERI §2.1
VARYANT         5 × 6,0 = 30,0 sn + kapak 5,0        KILAVUZ_REHBERI §2.6
                ⚠️ Bedeli o bölümde tabloyla yazılı: sıçrama 2 katı ·
                   METRONOM riski · kış %40 · detay istasyonu YOK.
                   Bedeli okumadan ızgara seçme.

⛔ DÜZ IZGARA (bütün sahneler eşit süre) İKİ KEZ ÖLÇÜLDÜ, İKİ KEZ DÜŞTÜ
   (⑥ METRONOM). Yine de seçilecekse plana (a) gerekçe ve (b) ritmin
   klip İÇİNE nasıl taşındığı yazılır [KILAVUZ_REHBERI §2.6].
   ⚠️ prompt_kontrol.py süre eşitliğini 5 satırlık tabloda YAKALAYAMAZ
      (eşik 6 satır). Beş sahnede bu kapı yoktur; ⑥ merceği ölçer.
```

## 🏗️ Y2 — YATAY FİLM YAZACAĞIM (16:9 merdiveni) 🆕 14.09.2026

```
0. FORMAT          yatay_2 / 4 / 6 / 8_dk_filmler — README'sini oku; sahne sayısı oradan (§2.8)
1. HİKÂYE ONAYI    sahne sahne öneri SOHBETTE yazılır → sahip onaylar → ancak sonra klasör açılır
                   (onay-once-uretim). Onaylı metin 00_ANALIZ/00_HIKAYE_ONAYI.md'ye, ONAY tarihli.
2. KLASÖR          bash araclar/film_klasoru_ac.sh <FMT> <FILM>   ⛔ elle cp -r YOK
3. 00_ANALIZ       sırayla: 00_OKUMA_CIZELGESI (betikten) → 01 ders hasadı → 02 konsept + risk
                   (VAAT/DİRENÇ/BEDEL · yapı + saha kartı · 16:9 kamera hesabı · vinç · ışık günü)
                   → 03 sıralama (inşa sırası → N satır · Σ rejim ≤ 14 h · bölüm sınırı karesi)
                   → 04 uyarılar (tekrar eden arıza tablosu her satır cevaplı) → 05 sahne tablosu
                   (⭐ BEŞ SORU sütunu dolu — SAHNE_PLAN_KARTI; KAPI ✅ olmadan prompt yok)
4. PLAN            kart A adım 1-7 aynen — <FILM>_PLAN.md (⛔ prompt yok) · ARAÇ KUTU SETİ satırı
5. USTA KARE       önce BOLUM_2'nin ## 🌟 USTA KARE bölümü (GN) — kapak kaynağı
6. PROMPTLAR       BOLUM_1 (S0…S(k−1)) · BOLUM_2 (S(k)…S(N−1)) — kart A adım 8 aynen; bölüm
                   sınırı G_k tek kare, ışık/yapı atlamaz [DERS 52]
7. KAPAK · MÜZİK · YAYIN PAKETİ · QA_SPEC   kart A adım 9-11 (SPEC künyesi: sahne saatleri · PART GRID)
8. KAPI            python3 araclar/prompt_kontrol.py <FMT>/<FILM>   ⭐ KLASÖR MODU
9. ÜRETİM          kart B aynen (ters zincir GN → G0 · günlük klip başına) — bölüm dosyası
                   üretim sırası DEĞİLDİR
10. QA             kart Q aynen; 6/8 dk'da iki yarım master (qa_paket.sh --bolum 1|2), ham rapor
                   <FILM>_B1_Q<n>_<AD>_HAM.md, TABLO iki satır (B1 · B2), FILMLER tek dosya

DOSYA:  <FMT>/<FILM>/  (iskelet: kilavuzlar/FILM_KLASOR_SABLONU/ · kart: KILAVUZ_REHBERI §2.8)
```

## 🔎 P — PROMPTLAR YAZILDI, ÜRETİM BAŞLAMADI

```
1. python3 araclar/prompt_kontrol.py <dosya>   → GO / FIX / BLOCK
2. BLOCK ise üretme, düzelt, tekrar koş
3. Tutarlılık listesi (TIMELAPSE_SISTEM_PROMPTU §4) elle koşulur
```

## 🎥 B — ÜRETİM SIRASI

```
⛔ 0. ARAÇ KAPISI — HER ŞEYDEN ÖNCE [DERS 23 · 32 · A7-d]
      ⭐ 08.09.2026: ÜÇ SORU YEDİYE ÇIKTI → kilavuzlar/ARAC_KARTLARI.md §4
      Tek prompt (ARAC_KARTLARI §5) · BEŞ klip · SEKİZ ölçüm:
        ① ffprobe süre → KUTU SETİ · ızgara o sayıdan yazılır [D-d]
        ② KAMERA HAREKET EDİYOR MU? (eşik KAMERA_ISTASYONU §7 — aşıyorsa bu araçla üretilmez)
        ③ GÖLGE DÖNÜYOR MU? (ilk/son karede aynı açıysa DUR)
        ④ NEGATİF SIZIYOR MU? (metin içi ve ayrı alan ayrı ayrı) [DERS 33]
        ⑤ PROMPT TAVANI — promptun son nesnesi kaç klipte göründü?
        ⑥ İLK KARE SADAKATİ — zincir_kontrol.sh ile
        ⑦ EN BÜYÜK KUTU geliyor mu? → sahne tavanını belirler
        ⭐⑧ ARAÇ İKİ KARE (ilk+son) ALIYOR MU? Almıyorsa BU FORMAT O ARAÇTA
           ÜRETİLMEZ [KILAVUZ_REHBERI §2.7 ④] — plan tek kareli I2V'ye
           düşürülmez, ARAÇ değişir.
      ⛔ Araç kartı doldurulmadan tek kare üretilmez [ARAC_KARTLARI §6].
      ⛔ ÜRETİM GÜNLÜĞÜ AÇILIR [DERS 28]: dikey_shorts/<PROJE>/<PROJE>_URETIM_GUNLUGU.md
         (şablon: dikey_shorts/URETIM_GUNLUGU_SABLONU.md)
         ilk satır = araç kapısı sonucu; sonra klip başına tek satır:
           S<n> · araç+ayar · kaynak kare · prompt birebir mi (değilse ne) ·
           zincir_kontrol: geçti/düştü · kanıt nesnesi elle ✓/✗ · ffprobe süre
         Günlüksüz filme QA paketi açılmaz (qa_paket.sh durur).
      ⛔ Ediyorsa o araçla BU FORMAT ÜRETİLMEZ. Prompt düzeltilmez.
      Ölçüldü: aynı çapa cümlesi bir araçta ① 10/10, başkasında 0/10.

⛔ SIRA TERSTİR VE ZİNCİRLİDİR (KILAVUZ_REHBERI §8 · §2.7):
   ⭐ FORMAT: foto1 – video1 – foto2 – video2 – … Her videonun SOLUNDAKİ foto
      onun İLK karesi, SAĞINDAKİ foto SON karesidir. N sahne = N+1 görsel.
   1. USTA KARE (GN) üretilir → KAPI: ikna edici değilse DUR
   1b. ⛔ PİLOT ÜÇLÜ — FİNAL ÜRETİLEBİLİRLİK TESTİ [KILAVUZ_REHBERI §8 adım 2b · C1-b]:
       (a) GN + 3 nirengi işaretli referans · (b) ilk halka GN → G(N−1) + zincir_kontrol ·
       (c) o iki kare arasında çalışan FİNAL I2V + en zor montajın pilot klibi.
       Üçü sahip onayı almadan adım 2 sürmez; (c) üretilemiyorsa KAPSAM DARALIR.
       Günlük §1b. Her zincir_kontrol koşusunda üçüncü argüman GN verilir.
   2. Usta kareden GERİYE image-to-image: GN → G(N-1) → … → G0
   3. ⛔ HER KAREDEN SONRA, SONRAKİNE GEÇMEDEN ÖNCE:
         bash araclar/zincir_kontrol.sh <onceki_onayli> <yeni>
      Çıkış 2 = ZİNCİR KIRILDI → kareyi AT, önceki onaylı kareye dön,
      yeniden türet. SONRAKİ SAHNELERİ ÜRETME.
      ⛔ VE HER KOŞUDA "AYNI YER" KANIT NESNESİ ELLE DOĞRULANIR [DERS 25]:
         iki karede de aynı yerde mi? Değilse kare ATILIR — betik geçse bile.
         Ölçüldü: nesne beş promptta da yazılıydı ve ilk dikişte kayboldu.
   4. Detay istasyonları da zincirin İÇİNDEN üretilir, çapa taşır
   5. Her I2V İKİ ONAYLI KARE ARASINDA üretilir: klip n'e G(n) ilk kare,
      G(n+1) son kare olarak verilir. Hedef karesi olmayan I2V yazılmaz.
      ⛔ Her klipten sonra: klibin SON karesi ile hedef görsel arasında
         zincir_kontrol.sh. Çıkış 2 = araç iki kareli modu taşımıyor.

⭐ NEDEN BU ADIM ARAÇLA BAĞLANDI [DERS 12]: bu kural iki filmde de yazılıydı
   ve iki filmde de atlandı. İki film de bu yüzden düştü. prompt_kontrol.py
   METNİ denetler; üretim SIRASINI denetleyemez. Yazılı kural kapı değildir.
```

## 📡 Y — TESLİM VE YAYIN

```
0. ⛔ KIRPMA    her klibin baş ve sonundan 10-15 kare atılır [A7-b · A8]
                ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn
                → KURGU_VE_TESLIM_KILAVUZU §2
1. KURGU        klip sayısı KILAVUZ_REHBERI §2.1 · sert kesme · geçiş YOK
                + kapak kartı (SAHNE DEĞİL, ayrı beyan edilir [DERS 4])
                ⭐ DURUŞA kes, harekete değil [A8-d · §3]
2. ⛔ FİNAL KARE KANITI
      ffmpeg -ss <saniye> -i teslim.mp4 -frames:v 1 kanit.jpg
   SPEC'te yazan şey o karede görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
2b. ⛔ KAPAK KANITI [DERS 30]  S9 kaynak karesi + kapak → zincir_kontrol.sh
      Çıkış 2 = kapak filmden türememiş → TESLİM YOK.
2c. ⛔ KESME KANITI [DERS 31]  bash araclar/kesme_kontrol.sh teslim.mp4 <plan>
      Kurgu planın SÜRE sütununa oturmuyorsa yeniden kesilir.
      ⭐ 08.09.2026: betik EŞİKTEN TOP-N'e geçti [A8-a]. Ölçüldü — eski eşik
        (0,30) ve A8'in önerdiği (0,40) bizim formatta SIFIR kesme buluyordu;
        kapı açık sanılıyordu, KAPALIYDI.
2e. ⛔ İHRAÇ KANITI [DERS 63]  PAYLAŞILACAK dosyaya (dikey: 2x):
      bash araclar/ihrac_kontrol.sh <film_klasoru> paylas_2x.mp4 --hiz 2
      Makine: süre = 28,0 (+kart yalnız planda varsa) · 1080×1920 · final tutuşu (SSIM).
      Elle ✓: müzik YOK · okunur yazı/logo/promo/"AI TIMELAPSE" YOK · kart = GN dünyası.
      Çıkış 2 ya da işaretsiz madde = PAYLAŞILMAZ. Sonuç günlük §4 ⑧'e.
2f. ⛔ KLİP KANITI [DERS 86 · 85]  ihraçtan ÖNCE:
      python3 araclar/klip_eslestir.py yayin.mp4 S0.mp4 … SN.mp4 --hiz 2
      Her üretilen klip yayında (⛔ yok · ⚠️ kırpılmış), sıra doğru, son klipten sonra kuyruk (kart) yok.
      Arızalı klip kurgudan DÜŞÜRÜLMEZ, yeniden üretilir — atlanan halkada iş tek kesmede belirir.
2d. ⛔ YEDİ ÖLÇÜM  KURGU_VE_TESLIM_KILAVUZU §6 — biçim · süre · kesme · LUFS ·
      açılış penceresi · flicker · final kare + kapak. Yedisinin çıktısı
      üretim günlüğü §4'e YAZILIR; yazılmamışsa yayın yok.
3. 120 PX TESTİ hem kapağa hem S0'ın 0. karesine (sips -Z 120)
3b. ⛔ KAPAK PROVASI (dikey)  python3 araclar/kapak_prova.py kapak.png — 3:4 · 4:5 · 1:1 merkez kırpma +
      140 px; üç soru ✓ + gerçek platform önizlemesi [DIKEY_TIMELAPSE_KAPAK_KILAVUZU §9 · §11 · DERS 94]
      + KAPAK_STIL_KILAVUZU §6: başlık bandda · kontrast ≥ 4,5:1 ölçüldü · ışık varyantı I2 ise §3.4 kapısı
4. İHRAÇ        1440p+ · BT.709 · 48 kHz · −14 LUFS · −1,0 dBTP
5. PAKETLEME    başlık/açıklama/hashtag/sabit yorum + ⛔ GERÇEKLİK BEYANI
                → doldurulmuş kanal şablonu: apexait/youtube/PAKETLEME_SABLONU.md
6. ⛔ AI BEYANI ÜÇ PLATFORMDA DA, elle, kendi beyanınla:
                YouTube  Studio → Ayrıntılar → "Altered content"
                TikTok   paylaşım ekranı → AIGC anahtarı
                Instagram gelişmiş ayarlar → AI/dijital içerik
                Açıklamadaki gerçeklik beyanı bunun YERİNE GEÇMEZ; ayrı yüzey.
                apexait/youtube/POLITIKA_VE_RISK.md §2 · CAPRAZ_YAYIN §2
7. ⛔ QA        → kart Q. Beş mercek YÜKLEMEDEN ÖNCE koşulur; öldürücü hüküm (❶ ❸ ❹) varsa yüklenmez.
7b. ⭐ 7. GÜN    apexait/IZLEYICI_DEFTERI.md — sahip dört sayıyı yazar (kaydırmadı % · ort. izlenme % ·
                engaged · abone); ajan sayı UYDURMAZ, yalnız QA sütunlarını ve analizi yapar [C2].
8. ÇAPRAZ       apexait/CAPRAZ_YAYIN.md §6 — tek master · filigran · C2PA
9. YÜKLEME      ÜÇ HESAP, aynı gün, native (CAPRAZ_YAYIN §4 sırası):
                apexait/youtube/PAKETLEME_SABLONU.md   §5
                apexait/instagram/PAKETLEME_SABLONU.md §5
                apexait/tiktok/PAKETLEME_SABLONU.md    §5
```

## 🔍 Q — FİLM ÜRETİLDİ, QA KOŞULACAK

```
⛔ ÖN KOŞUL: film ÜRETİLMİŞ olmalı. Rubrik promptu değil VİDEOYU eleştirir.

1. MAKİNE       ⭐ bash araclar/qa_paket.sh [--hiz 2] [--master <1x.mp4>] <film_klasoru> <yayin.mp4> [kapak]
                → kare_al.sh + kesme_kontrol.sh (top-N) + ffprobe + SSIM → ÖLÇÜLMÜŞ OLGULAR
                → QA/KOSU/<FILM>/Q<n>_<AD>_paket.md × 5 · blok rubriğin İÇİNDE · künye taslağı üstte
                ⭐ dikeyde hız 2: yayın kopyası verilir; master varsa ❸ ❹ onunla koşar
                ⛔ Üretim günlüğü yoksa DURUR [DERS 28].
2. ❶ GÖRÜNTÜ        paket + video + kareler            ⛔ BELGE YOK
3. ❷ ZAMAN VE KESME paket + video                      ⛔ BELGE YOK
4. ❸ ŞANTİYE        paket + video + kareler            ⛔ BELGE YOK
5. ❹ İNŞA           paket + video + QA_SPEC + plan     (mod D)
6. ❺ TESLİM         paket + yayın dosyası + plan + kapak (mod D)

⛔ YALITIM [QA_KOSU §1]: her mercek AYRI, GEÇİCİ sohbette, Gemini projesi/Gem DIŞINDA.
   Gem/proje dosyaları o Gem'in bütün sohbetlerine girer — plan oradaysa kör mercek görür.
⭐ SIRA: kör üçlü (❶ ❷ ❸) ÖNCE. Önce belge görüp sonra "kör" koşmak körlüğü kaybetmektir.
⛔ ÖLDÜRÜCÜ: ❶ SEPARATE IMAGES · ❸ REBUILT · ❹ DIFFERENT → film YAYINLANMAZ.
⭐ Seçilen arşiv filmleri yeniden koşulur: ARSIV_12_MERCEK/00_ARSIV.md §6.
```

## 📥 R — QA RAPORU GELDİ

```
1. HAM ÇIKTI     QA/HAM/<FILM>/<FILM>_Q<n>_<AD>_HAM.md — paketteki künye üstte, model çıktısı
                 altta · ⛔ düzenleme, kısaltma, özetleme YOK [QA/HAM/00_README]
2. GERİ OKUMA    ilk üç satır: dosya adı · belgeler · görülen klip [QA_KOSU §2.2]
                 dosya adı ya da belge tutmuyorsa → koşu YOK, yeniden koş (geçici sohbet)
2b. AJAN ÖLÇÜMÜ yayın dosyası yereldeyse merceklerden ÖNCE: ffprobe · 1 sn kare panosu · klip başına 4 fps pano ·
                 kapak_prova.py · kart ses kuyruğu · gök bandı rengi — plan ↔ ekran tablosu bunun üstüne kurulur [DERS 100]
3. DOĞRULAMA     D1–D6 [QA_OLCUM_ZEMINI §5] · kör raporda sızıntı taraması [QA_KOSU §3]
                 ⭐ D6 [DERS 90]: puanı kayda geçirmeden önce yayının 1 sn'lik kare panosu + klip_eslestir —
                 raporun kurgu tablosu dosyaya karşı doğrulanır · plan SAYISI (kadraj yüzdesi) kör raporda = SIZINTI
                 · mod D ilk satırı RUN INCOMPLETE → durum EKSİK, puan YOK
4. DURUM         TAM · EKSİK · YANLIŞ GİRDİ · SIZINTI · TUTARSIZ [QA_KAYIT §1.2] — künyeye
5. PUAN          mercek puanı = tetiklenen kategorilerin ortalaması — AJAN hesaplar
                 hüküm ↔ kategori: KÖTÜ OLAN KAZANIR · iyi hüküm + sahip kategori ≤ 3 → TUTARSIZ
                 [RUBRIK_YAZIM §4]
6. HÜKÜM SATIRLARI ❶ THE BODY THAT MELTED WORST · ❸ THE OBJECT THAT PROVES IT IS THE SAME PLACE
                 · THE GROWTH NOBODY MADE · ❹ THE FIRST PIECE THAT APPEARED · THE MOST DAMAGING
                 INTRUDER · ❺ WHAT THE PLAN PROMISED THAT NEVER REACHED THE SCREEN —
                 NONE değilse o sahne yeniden üretim adayıdır, ortalama ne olursa olsun.
7. DOKÜMAN       kör üçlünün QUESTIONS FOR THE DOCUMENT listesini plandan CEVAPLA.
8. KAYIT         QA/FILMLER/<FILM>.md (şablon FILMLER/00_README) · OLAY TABLOSU (E01…) ·
                 KARAR · DERS → QA/TABLO.md satırı · bash araclar/sayac.sh (U1 · U2)
9. YENİ DERS     yeni bir bozulma çıktıysa kart D
10. ONARIM       hüküm satırı NONE değilse ya da puan düştüyse: kök neden → tek eylem → iki dikiş
                 sınaması → günlük §5 satırı (G<n>_K<k>) [ONARIM_VE_YENIDEN_URETIM_KILAVUZU]
```

## 🔬 S — ARAŞTIRMA SONUCU GELDİ

```
⛔ ÖN KOŞUL: harici araştırma botu bu deponun hiçbir dosyasını okuyamaz.
   arastirma/A<n>_*.md dosyaları bu yüzden kendi kendine yeter [D-a].

1. HAM KAYIT    gelen çıktı → arastirma/SONUCLAR/A<n>_<BOT>_HAM.md
                ⛔ düzenleme · kısaltma · özetleme YOK — bu kanıttır
                künye beş satırı elle doldurulur (bot · tarih · kesildi mi)
2. ETİKET       raporun her bulgusunda ÖLÇÜLDÜ / İDDİA / VARSAYIM etiketi
                aranır. ⛔ Etiketsiz bulgu KURAL ÜRETMEZ — okuma sayılır.
3. ÇELİŞKİ ÖNCE raporun "BİZİM FORMATIMIZLA ÇELİŞENLER" bölümü ilk okunur.
                Bir kılavuz maddesi ÖLÇÜLMÜŞ bir bulguyla çelişiyorsa
                KILAVUZ değişir, bulgu değil.
4. İKİ RAPOR    aynı prompt iki bota koşulduysa iki dosya ayrı durur.
                ⛔ Ortalama ALINMAZ: iki rapor aynı sayıyı farklı veriyorsa
                   o sayı ölçülmemiştir ve bu bilgi sayının kendisinden
                   değerlidir.
5. VARSAYIM     kabul edilen bulgu kilavuzlar/VARSAYIMLAR.md'ye A<n>-x koduyla
                girer: kuşak bölümüne madde + DİZİN'e satır (durum ⬜ açık) —
                numaralı derse DEĞİL. Durum yalnız kanıtla değişir (DERS n · ÖLÇTÜM · denetim).
                ⛔ Araştırma bulgusu ders değildir; ders bu depoda ölçülmüş
                   bozulmadır. İlk üretimden sonra ya derse döner ya düşer.
6. KİLİT        prompta inecek her cümle İngilizce ve POZİTİF hâlde yazılır —
                yasak değil, ölçülebilir çapa [DERS 11].
7. KILAVUZ      madde hangi kılavuza iniyorsa oraya tek satır + kaynak kodu
```

## 📚 D — YENİ DERS ÇIKTI

```
1. kilavuzlar/DERSLER.md → kalıba göre yaz (film · sahne · saniye · ne oldu)
2. ⛔ "KALDIRDIĞI" satırı zorunlu — bu kilidin engellediği anlatım imkânı ne?
   Yazılmayan yasak kabul edilmez [D-f].
3. Kilit hangi kılavuza iniyorsa oraya tek satır ekle
4. DERSLER.md dizin tablosuna satır
5. Ders bir varsayımdan doğduysa ya da birini düşürdüyse: VARSAYIMLAR.md / PLAN_OKUMALARI.md
   DİZİN satırının durumu → "✅ ölçüldü → DERS n" ya da "❌ düştü · DERS n". Madde silinmez.
```

## 🧱 H — YENİ KART EKLENDİ (yapı tipi / saha)

```
1. İlgili kart dosyasına §X.Y olarak ekle (şablon her dosyanın sonunda)
2. KILAVUZ_REHBERI §1 karar ağacına seçenek olarak yaz
3. Kart bir DERSTEN ya da gerçek bir inşa sırasından doğar, fikirden değil
```

---

# 3. DEĞİŞMEZ KURALLAR

```
① SAYI TEK YERDE DURUR. Sayı isteyen belge kaynağa işaret eder.
② KILAVUZ OKUMADAN FİLM YAZILMAZ.
③ PROMPT KAPISINDAN GEÇMEDEN ÜRETİM YAPILMAZ.
④ ÜRETİM SIRASI TERSTİR — usta kare önce.
⑤ HER YENİ YASAK, KALDIRDIĞI ANLATIMI YAZAR. Yazmayan yasak eklenmez.
⑥ GERÇEK PROJE / FİRMA / LOGO İDDİASI YOK. Her videoda gerçeklik beyanı.
⑦ ① · ③ · ⑤ · ⑦ MERCEĞİNE DOKÜMAN VERİLMEZ. Verilirse o rapor geçersizdir.
⑧ TESLİM YAPISI HER PLANDA BEYAN EDİLİR: sahne bloğu + kapak kartı ayrı.
⑨ ZİNCİRLİ ÜRETİM BİR KAPIDIR VE ARAÇLA KOŞULUR:
   her karede zincir_kontrol.sh. Koşulmayan kapı kapı değildir.
   ⭐ VE ZİNCİR ARTIK FORMATTIR [KILAVUZ_REHBERI §2.7]: her klip İKİ onaylı
   kareye kilitlidir — solundaki foto ilk karesi, sağındaki son karesi.
⑩ VERDICT SATIRI SKOR ORTALAMASINI YENER.
⑪ COMMIT VE PUSH'U YALNIZ PROJE SAHİBİ ATAR.
⑫ HER YÜKLEMEDE "ALTERED CONTENT" BEYANI İŞARETLENİR. Beyan para kazanmayı
   etkilemez; beyansızlık kanalı etkiler [apexait/youtube/POLITIKA_VE_RISK.md §2].
```

---

# 4. YAZIM STANDARDI

```
· Belgeler TÜRKÇE. Yalnız üretim promptlarının içi İngilizce.
· Emoji başlıklar korunur — dosyalar arası gezinmeyi taşıyan şey odur.
· Kural yazarken GEREKÇE yaz. Gerekçesiz kural, ilk baskıda esnetilir.
· Bir kuralı taşırken NEREDEN geldiğini yaz (film_md D-x gibi).
· ⛔ / ⭐ / ⚠️ işaretleri anlam taşır: ⛔ kapı · ⭐ en önemli · ⚠️ dikkat.
```

---

# 5. COMMIT KURALI

```
⛔ Ajan commit ve push ATAMAZ (.claude/settings.json deny).
İş bitince ajan: değişen dosyaları listeler, önerilen commit mesajını yazar,
commit'i sahibine bırakır.
```

---

# 6. BİLİNEN AÇIKLAR — bunlara güvenme

> ⛔ **05.10.2026 · KAPI SIKILAŞTI (§10f · DERS 58-63).** Bu tarihten önce yazılmış bütün planlar
> `prompt_kontrol.py`'de BLOCK verir (YASAK KELİME satırı · sahada olmayan nesneyi sayan metin
> yasağı · dikey günlük/PİLOT · 6-8 sahnelik dikey). Üretilmiş filmler için bu ARŞİVDİR; ÜRETİLMEMİŞ
> bir plan üretime alınacaksa önce bu kapıdan geçirilir. Dikeyde 6 sahnelik THE BLUE SILO ve
> THE SEA MILL 7. sahne için sahip onayı bekler (onay önce, üretim sonra).

```
· VARSAYIMLAR.md ve PLAN_OKUMALARI.md'deki kodların büyük çoğunluğu ⬜ AÇIKTIR —
  bu depoda ölçülmedi (sayı: bash araclar/sayac.sh "kod durumu"). İlk üretimden ya da
  izleyici verisinden sonra ya DERSLER.md'ye derse dönüşürler ya düşerler.
· prompt_kontrol.py yalnız METİN denetler; anlam denetlemez. Kapıdan geçen
  bir prompt iyi bir prompt değildir, yalnız biçimsel olarak eksiksizdir.
  ⭐ 18.09.2026 ölçüldü: 15 filmin planı kapıdan geçti, ② İNŞA'da çoğu düştü.
  Kapıyı geçmek görüntüde doğru eylemi garanti etmez — ikinci aşama (klip
  baş/orta/son + zincir_kontrol) ayrı koşulur [QA/00_README §6].
· Kadraj hesabı (KAMERA_ISTASYONU §3) tam kare dikey (36 mm kare yüksekliği)
  varsayar. Başka sensör/araç kullanılırsa formülün 36 sabiti değişir.
· Ters inşa (image-to-image ile geriye) bu depoda BEŞ filmde de koşulmadı
  (LONG DAY dâhil — ya da koşuldu ve günlük yok [DERS 28]) — akışın
  en yüksek kaldıraçlı adımı aynı zamanda en az sınanmış adımıdır.
  ⚠️ VE ARTIK ONA KARŞI BİR İDDİA VAR: dış araştırma, ardışık
     image-to-image'in matematiksel olarak hata BİRİKTİRDİĞİNİ söylüyor ve
     zincirsiz bir alternatif öneriyor. İddia da alternatif de koşulmadı.
     Zincir ilk kez koşulurken bu okunur [KILAVUZ_REHBERI §8 adım 3a · 3c].
· Araştırma raporunun kendi ÖLÇÜLDÜ etiketine güvenilmez. 03.09.2026
  koşusunda etiketlerin bir kısmı SEO içerik çiftliğine dayanıyordu; etiketin
  yanına KAYNAK SINIFI yazma adımı bu yüzden eklendi (arastirma/00_README §3).
```

---

# 7. DOĞRULAMA — iş bitince çalıştır

```bash
bash araclar/sayac.sh
python3 araclar/capraz_sayim.py     # (arşiv) QA_CAPRAZ_ANALIZ sayıları matrisle uyuşuyor mu

# başlıksız / SPEC'siz film klasörü var mı — çıktı boş olmalı (beş format klasörü)
for d in dikey_shorts/*/ yatay_*_dk_filmler/*/; do
  [ -d "$d" ] || continue
  ls "$d" | grep -qE "_(DIKEY_TIMELAPSE|PLAN)\.md" || echo "EKSİK PLAN: $d"
  ls "$d" | grep -q "_QA_SPEC.md"                  || echo "EKSİK SPEC: $d"
done

# prompt kapısı tüm filmlerde (yatay: klasör modu)
for f in dikey_shorts/*/*_DIKEY_TIMELAPSE.md; do python3 araclar/prompt_kontrol.py "$f"; done
for d in yatay_*_dk_filmler/*/; do [ -d "$d" ] && python3 araclar/prompt_kontrol.py "$d"; done

# ham raporu olup TABLO'da satırı olmayan film → sayac.sh "U1" satırları (çıktı boş olmalı)
bash araclar/sayac.sh | grep -E "U1|U2" 
```
