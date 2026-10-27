# 🧭 KILAVUZ REHBERİ — Buradan Başla

> **Bu dosya adres verir ve ÜÇ TABLOYU tutar.** Detay diğer kılavuzlarda kalır;
> ama bu üç tablo (Değişmezler · Aşama Merdiveni · Negatif Çekirdek) her filmde
> fiilen kullanıldığı için burada tam metin olarak durur.
>
> Bir sayıyı iki yerde tutmak, birini yanlış tutmaktır.

---

# 1. 🎯 DÖRT SORU → OKUMA LİSTEN

Yeni bir filme başlarken **sırayla** cevapla. Her cevap bir sonrakini daraltır.

```
⓪ FORMAT?       dikey 9:16 (dikey_shorts · 60 s bandı · §2.1–2.7)
                yatay 16:9 merdiveni (yatay_2/4/6/8_dk_filmler · 12/24/36/48 × 10 s · §2.8)
                                                    → format klasörünün README'si
① YAPI TİPİ?    kule · konut · köprü · baraj · stadyum · yol/tünel · liman · türbin
                · ⭐ kayar kalıpla silo/baca/şaft (§9b · 17.09.2026)
                · ⭐ şehir içi çökük / altyapı onarımı (§6b · 19.09.2026 · aşağı bakış)
                                                    → YAPI_TIPI_KARTLARI.md
② SAHA?         şehir içi · kırsal · kıyı · dağ/eğim · kar · çöl
                                                    → SAHA_VE_IKLIM_KARTLARI.md
③ ZAMAN YAYI?   toplam kaç ay/yıl 60 saniyeye sığıyor + hangi mevsimler geçiyor
                                                    → ZAMAN_VE_ISIK_KILAVUZU.md
④ KAMERA?       hibrit (4 ana + 2 detay) · saf tek istasyon · çok istasyon
                                                    → KAMERA_ISTASYONU_KILAVUZU.md
                ⭐ ÖNCE bakış ailesi: değişim YÜKSEKLİK mi, ALAN mı, SEVİYE mi →
                  hiza (tilt 0) / yüksek çapraz (aşağı bakış) · tilt ≠ 0 ise kadraj formülü
                                                    → KAMERA_DILI_KILAVUZU.md §2.3 · §3
```

### Her filmde okunacaklar (değişmez)

```
□ §3  DEĞİŞMEZLER TABLOSU     (bu dosyada — her promptta birebir tekrarlanır)
□ §4  AŞAMA MERDİVENİ         (bu dosyada — plan bundan doğar)
□ §5  GÜNEŞ SAATİ KİLİDİ      (bu dosyada)
□ §6  VAAT / DİRENÇ / BEDEL   (bu dosyada — konsept kapısı, geçmezse plan yazılmaz)
□ §7  NEGATİF ÇEKİRDEK        (bu dosyada — tam metin, her prompta yapıştırılır)
□ §9  BİLİNEN TUZAKLAR        (bu dosyada)
□ PROMPT_SABLONU.md           (görsel + iki uçlu I2V iskeleti · T2V YOK)
□ DERSLER.md                  (ölçülmüş hatalar — DERS 1–64)
□ VARSAYIMLAR.md              (ölçülmemiş: D · A · F1 · C — DİZİN durum sütunu ⬜ ✅ ❌)
□ PLAN_OKUMALARI.md           (P kodları — uzman okuması · plan kararları)

── ⭐ 08.09.2026 · A5–A8 ARAŞTIRMASINDAN DOĞAN DÖRT KILAVUZ ──
□ ARAC_KARTLARI.md            ⛔ EN ÖNCE — kutu seti ölçülmeden ızgara yazılmaz
□ INSAAT_YONTEMI_KILAVUZU.md  merdiven satırı = eleman + ara hâl (%25/%50/%75)
□ SANTIYE_HAREKETI_KILAVUZU.md merdiven satırı = sıkıştırma rejimi (A·B·C)
□ KURGU_VE_TESLIM_KILAVUZU.md kurgudan önce okunur (kırpma bütçesi süreyi yer)

── ⭐ 11.09.2026 · A9–A12 ARAŞTIRMASINDAN DOĞAN DÖRT KILAVUZ — dört prompt BLOĞUNUN sözlüğü ──
□ MALZEME_VE_DOKU_KILAVUZU.md     SITE TEXTURE — korpus üçlüsü · bant kuralı · saha kartı · yaşlanma
□ FIZIK_VE_AGIRLIK_KILAVUZU.md    PHYSICS — yük yolu · söküm fiili · hammadde yığını · robotik gövde
□ PERSPEKTIF_VE_OLCEK_KILAVUZU.md COMPOSITION — referans nesne (px) · kesir cümlesi · sayı testi
□ HAVA_VE_ATMOSFER_KILAVUZU.md    TIME RATE + LIGHTING — üç rejim × gök · iki kare arası gök/gölge
   ⛔ dördü de prompt_kontrol.py §10d'de sonlanır; kaynak denetimi
      arastirma/SONUCLAR/A9-A12_DENETIM.md (12 kaynağın 4'ü yanlış atıf)

── ⭐ 17.09.2026 · A13–A18 ARAŞTIRMASINDAN DOĞAN TEK KILAVUZ ──
□ KAMERA_HAREKETI_KILAVUZU.md     ⭐ "kamera hareketi" istendiğinde HANGİ KATMAN:
                                  ① üretim (SABİT · değişmedi) · ② kurgu (yakınlaşma ·
                                  sahip kararı · ÖLÇÜLMEDİ) · ③ kadraj içi (serbest)
   ⛔ YALNIZ kurgu yakınlaşması olan filmde okunur; olmayan filmde §7 yeter.
   ⚠️ Bu kuşakta prompt YOK ve kaynak ÇEKİLEMİYOR — denetim
      arastirma/SONUCLAR/A13-A18_DENETIM.md (tek sayı indi, o da burada hesaplandı)

── ⭐ 18.09.2026 · 15 FİLMİN ÇAPRAZ ANALİZİNDEN DOĞAN TEK KILAVUZ — prompttan ÖNCE ──
□ SAHNE_PLAN_KARTI.md            ⭐ BEŞ SORU klip başına: ① malzeme nerede · ② hangi
                                  taşıyıcı · ③ nereye oturuyor · ④ klip sonunda ne değişti
                                  · ⑤ sabit kalanlar → I2V MOTION FOCUS paragrafı
   ⛔ Beş sorusu cevaplı olmayan sahnenin promptu yazılmaz (kart A adım 7b · Y2 adım 3).
   ⚠️ Kaynak QA/ARSIV_12_MERCEK/QA_CAPRAZ_ANALIZ/ (sayılar: araclar/capraz_sayim.py) — ölçülmedi,
      VARSAYIMLAR.md C1 bölümünde VARSAYIM (C1-a…h); kapı FIX, BLOCK değil.

── ⭐ 20.09.2026 · A19 DIŞ RAPORUNDAN DOĞAN TEK KILAVUZ — istasyondan ÖNCE ──
□ KAMERA_DILI_KILAVUZU.md        ⭐ KARAR CÜMLESİ (§0) · DEĞİŞİM BOYUTU → BAKIŞ AİLESİ (§2.3) ·
                                  ⭐ TİLTLİ KADRAJ FORMÜLÜ (§3 — KAMERA_ISTASYONU §3 yalnız tilt 0°)
                                  · katsayı δ = pencere/(L×f) (§5) · raporun promptları neden
                                  kapıdan geçmez (§7) · negatif alan sorusu (§8)
   ⛔ tilt ≠ 0 olan her planda (aşağı bakış ailesi) §3 formülü zorunlu; tilt 0'da §3 gereksiz.
   ⚠️ Kaynak A19 — prompt YOK ama kaynakça ÇEKİLDİ (11'in 10'u iddiaya ait);
      denetim arastirma/SONUCLAR/A19_DENETIM.md · yeni SAYI inmedi, iki formül indi.

── ⭐ 07.10.2026 · A25–A29 ARAŞTIRMASINDAN DOĞAN BEŞ KILAVUZ — koşullu okunur ──
□ UZUN_FORM_ANLATI_KILAVUZU.md     ⭐ her YATAY filmde: merak zinciri (§3) · yeniden kanca (§4) · final
                                  ve son ekran (§6) · yayından sonra eğri → sahne (§7)
□ ISTASYON_VE_IC_MEKAN_KILAVUZU.md ikinci sabit kamera ya da iç mekân istendiğinde — dört şart (§0)
□ SU_VE_YANSIMA_KILAVUZU.md        suyun kotu değişen ya da yansıma yazılan her filmde — SU KOTU DEFTERİ
□ ISIK_FINALI_KILAVUZU.md          final mavi saatte ya da yapının ışıklarıyla bitiyorsa — IŞIK DEFTERİ
□ ONARIM_VE_YENIDEN_URETIM_KILAVUZU.md QA raporu geldikten sonra (AGENTS kart R adım 10)
   ⚠️ Kaynak A25–A29 — kaynakça ÇEKİLDİ (33 satır: 20 ✅ · 8 ⚠️ · 5 ❌); denetim
      arastirma/SONUCLAR/A25-A29_DENETIM.md · inen sayılar bu makinede yeniden hesaplandı.

── ⭐ 15.10.2026 · A35–A38 ARAŞTIRMASINDAN VE THE SKY STATION QA (DERS 65–84) ENKAZINDAN DOĞAN KILAVUZ ──
□ MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md ⭐ çok odaklı sahneler, kanyon/uçurum ve şantiye araçları:
                                  Bounding Box ve derinlik (z) karantinası (§1) · STRICT ZONE IMMUNITY (§1)
                                  · kontrollü mimari sözlük: ⛔ truss yok · deck hijyeni (§2) · Exit Before Swap (§3)
                                  · tek hareketli aktör N_max = 1 ve amaçlı iş döngüsü (§4) · Void Immunity ve zemin şasi kökü (§5)
                                  · montaj öncelik grafiği (DAG) ve geriye yıkım kilidi (§6) · müzik token yasağı (§7)
   ⛔ çok odaklı, açık teraslı, kanyonlu veya araçlı her filmde ZORUNLU.
   ⚠️ Kaynak A35–A38 — kaynakça ÇEKİLDİ (32 satır: 24 ✅ · 6 ⚠️ · 2 ❌); denetim arastirma/SONUCLAR/A35-A38_DENETIM.md.

── ⭐ 15.10.2026 · A39–A42 ARAŞTIRMASINDAN DOĞAN KILAVUZ — ara hâl aşımı, kümülatif devamlılık ve mikro-doyum ──
□ MONOTONIK_ILERLEME_VE_FAZ_KAPISI_KILAVUZU.md ⭐ ara hâl aşımı (%25 tavanı) ve yo-yo söküm engeli (§1) ·
                                  dondurulmuş baz elemanlar (COMMITTED BASELINE) ve sıfır kaymalı demirleme (§2) ·
                                  söküm ve montaj faz kapısı (IRREVERSIBLE PHASE GATE) ve 8s WBS (§3) ·
                                  üç fazlı kinematik kurgu ve çoklu etki elemanı (≥3 el) (§3.4) ·
                                  sabit kadrajda nöroestetik tutunma, 6. sn mikro-doyum ve 7. sn merak tohumu (§4)
   ⛔ aşamalı inşaat, restorasyon, söküm veya sabit kadrajlı her filmde ZORUNLU.
   ⚠️ Kaynak A39–A42 — kaynakça ÇEKİLDİ (28 satır: 23 ✅ · 4 ⚠️ · 1 ❌); denetim arastirma/SONUCLAR/A39-A42_DENETIM.md.
```

```
⭐ 08.09.2026 — ALTINCI FİLM ÖLÇÜLDÜ, DÖRT SATIR EKLENDİ [DERS 35-44]:
   □ STRUCTURE bloğu yalnız BU SAHNEDE AYAKTA OLANI tarif eder; tam hâl tek
     cümleye iner ("When finished this will be a …")     [DERS 36 · kapı var]
   □ Metin yasağı HİÇBİR nesne adı anmaz — "on any surface" [DERS 35 · kapı var]
   □ ACTIVITY'de en az bir makine büyüyen elemanı NESNE alır [DERS 43 · kapı var]
   □ Geniş sahada İKİ mesafe: D_kenar ve D_eksen             [DERS 38 · kapı var]

⭐ SIRA ÖNEMLİ: ARAC_KARTLARI plandan ÖNCEDİR.
   Klip süreleri kutuludur ({4,6,8} · {5,10} · {5,9}) ve tek klipte teslim
   edilebilecek en uzun sahne = (en büyük kutu − 1,00 sn). Bu sayı bilinmeden
   §2.2'nin ritim ızgarası yazılamaz [A7-a · A7-b].
   ⛔ THE LONG DAY'de bilinmiyordu: plan 4-10 sn yazdı, araç 6,0 verdi,
      ⑥ METRONOM dördüncü kez geldi [DERS 31].
```

## 1.2 ⭐ film_md'DEN NE DEVRALINDI, NE TERS ÇEVRİLDİ

Bu depo `film_md`'nin iskeletini devraldı. Ama timelapse, uzay filminin bir
alt türü değil — bazı kuralları **tersine çevirir.** Bir kuralı sebebini
bilmeden taşımak, o kuralı yanlış yere taşımaktır.

| film_md kuralı | Burada | Sebep |
|---|---|---|
| Character Bible her promptta kelimesi kelimesine | ✅ **YAPI BIBLE** aynı disiplinle | Model hafızasızdır; her prompt tek başına yeterli olmalı |
| Karakter sadakati = aynı yüz | ✅ **Yapı sadakati = aynı bina** | 6 sahnede 6 farklı bina, bu türün 1 numaralı ölüm sebebidir |
| ≥3 açı tipi · kurulum çeşitliliği zorunlu | ⛔ **TERS: kamera SABİT** | Timelapse'in tanımı sabit kameradır. Çeşitlilik burada kusurdur |
| Kesme = mekân/açı değişimi | ⛔ **TERS: kesme = ZAMAN sıçraması** | Aynı kadraj, farklı ay. Kesmenin taşıdığı bilgi budur |
| Fizik defteri (g · m/s · newton) | 🔄 **Güneş saati + aşama defteri** (derece · gün · kat) | Sayı disiplini aynı, sayının konusu farklı |
| Novum = imkânsız fizik | 🔄 **Novum = zaman sıkışması** | "Bu imkânsız" değil, "bu boş arsa ŞU oluyor" |
| Kadrajda tek insan, ikinci insan yasak | 🔄 **İnsan = ölçek referansı ve hız çizgisi** | §9.4'e bak — yasak değil, BULANIK |
| Metin yasağı (D138: yasağın KAPSAMI) | ✅ **Daha da sert** | Şantiye tabela/logo/yelek/vinç yazısıyla doludur — bu türün en yoğun metin riski |
| "Fotogerçekçi insan duygusu" AI algısı cezası | 🎁 **Bu risk burada YOK** | Kadrajda okunur yüz yoksa tekinsiz vadi de yoktur. Yapısal avantaj |

⭐ **Bir bedava avantajla başlıyoruz:** 9:16 kadraj + yükselen yapı doğal
eşleşmedir. `film_md` kozmik ölçeği dikeye sığdırmak için sürekli savaştı;
burada kadrajın boş olduğu yer (üst) tam da yapının büyüdüğü yerdir.

---

# 2. 📐 FORMAT KARTI — DİKEY TIMELAPSE (9:16)

> §2.1–§2.7 dikey hattır (`dikey_shorts/`). ⭐ **Yatay 16:9 merdiveni §2.8'dedir** (14.09.2026):
> 12 · 24 · 36 · 48 sahne × 10,0 s; iskelet `FILM_KLASOR_SABLONU/`, betik `araclar/film_klasoru_ac.sh`.

## 2.1 ⛔ TESLİM YAPISI — her planda beyan edilir

> ⛔ **05.10.2026 · SAHİP KURALI — DİKEY SHORTS KESİN 7 SAHNE [DERS 58].** Aşağıdaki
> 10 × 6,0 kutusu ve §2.3–§2.6 TARİHÇEDİR; yeni dikey plan şu yapıyla yazılır:
>
> ```
> IZGARA         7 sahne × 8,0 sn = 56,0 sn          ← künyede kelimesi kelimesine (kapı arar)
> SAHNE BLOĞU    7 sahne × 8,0 sn = 56,0 sn          ← QA merceklerinin konusu · usta kare G7 · 7 I2V
> KAPAK KARTI    1 kart × N,N sn · SONDA · kaynak GN   ← ⭐ sahip kuralı 16.10.2026: HER filmin sonunda kapak
>                (paylaşım dosyasının saniyesiyle)      kartı; ihraç beyanı ölçer [DERS 63 · 85]
> MÜZİK          ⛔ YOK — diegetik ses yatağı         ← sahip kuralı 21.09.2026
> YASAK KELİME   crane · hoist · …  ya da  — (yok)   ← hiçbir promptta, negatifte bile [DERS 59]
> PAYLAŞIM       2x — ~28,0 sn sahne bloğu (+kart)   ← üretim 1x; QA ve ihraç --hiz 2 ile koşar
> ```
> ⭐ **16.10.2026 · SAHİP KURALI — HER FİLMİN SONUNDA KAPAK [DERS 85].** Kart = platform kapağının kendisi
> (başlık metniyle), sahne bloğundan SONRA. ① Kaynak GN: kapak usta kareden türer (sahip kuralı 19.09.2026) —
> ayrı üretilmiş "güzel" kapak başka dünya olur (POOL ROOM: alçak kamera, gündüz, fazladan saksı). ② Kart,
> son klibin 4–8 sn TUTUŞU bittikten sonra girer; erime kullanılacaksa ≤ 1 sn ve tutuşun DIŞINDA (POOL ROOM'da
> 2,1 sn erime finalin son 2 sn'sini örttü). ③ Süre plana yazılır: `KAPAK KARTI 1 kart × 5,0 sn (sonda ·
> erime 0,5 sn)` — ihrac_kontrol süre = blok/hız + kart. ④ Yazı yalnız kartta; sahnelerde yazı yasağı sürer.
> ⑤ Yerleşim `DIKEY_TIMELAPSE_KAPAK_KILAVUZU.md` §0 · §3 + başlık bandı Ü/O/A, ışık ve stil `KAPAK_STIL_KILAVUZU.md` (25.10.2026): GN'de ana yapı y %29–58, başlık sakin alanı (Ü bandı) y %60–71
> (alttan) — plan KADRAJ KİLİTLERİ tablosuna "kapak çekirdeği" satırı · yayından önce `kapak_prova.py` [DERS 94].
> Brief 6 ya da 8 sahne verirse plan yine 7 ile yazılır ve bu sahibe söylenir.
> `prompt_kontrol.py` §10f dikeyde 7 dışını, 8,0 dışını, künye satırı eksikliğini,
> günlüksüz klasörü ve PİLOT ÜÇLÜ'süz planı BLOCK'lar.

```
SAHNE BLOĞU    10 sahne × 6,0 sn = 60,0 sn    ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn =  5,0 sn     ← konusu DEĞİL, ayrı denetlenir
               ⛔ KONUM: teslimin SON 5 saniyesi. Süreyi yazıp konumu
                  yazmamak, okuyanı intro sanmaya bırakır [A1-b].
─────────────────────────────────────────────
TOPLAM                            65,0 sn
```

⛔ **KAPAK KARTI BİR SAHNE DEĞİLDİR ve beyan edilmezse QA'yı çökertir
[DERS 4].** v1'de kart beyansızdı; üç mercek onu 7. sahne sandı, ①'in
ANCHOR IDENTITY'sini 0/10 yaptı ve ④'ün FİNAL VURUŞUNU FAIL'e düşürdü.
Rapor haklıydı — eksik olan belgeydi. Kart artık planın ilk sayfasında
sayıyla durur ve rubriklerin künyesinde `SCENE BLOCK / END CARD` alanı vardır.

## 2.2 ⭐ SÜRELER EŞİT DEĞİLDİR — RİTİM KURALI [DERS 13]

```
⛔ ÖLÇÜLDÜ: on kesme 6,0 · 5,8 · 6,2 · 6,0 · 5,9 · 5,9 · 6,0 · 6,2 · 6,0
   → ⑥ RHYTHM 0/10 · VERDICT METRONOM · "THE CUT THAT CARRIES THE FILM: NONE"
   → ve proje sahibi filmi "hâlâ yavaş" okudu.
   Halbuki kesme aralığı 10 sn'den 6 sn'ye İNDİRİLMİŞTİ.

⭐ HIZ, KESME SIKLIĞI DEĞİL, KESME VARYANSIDIR.
   Eşit aralıklı bir dizi tempo üretmez, NABIZ üretir. Hızlanma hissi
   beklentinin BOZULMASINDAN doğar, aralığın kısalmasından değil.
```

> ⭐ **DIŞARIDAN DOĞRULANDI [A2-a].** Bu cümle bir rapor teşhisinden
> türetilmişti ve ölçülmemişti; artık mekanizması adlandırılmış: izleyiciyi
> bağlayan şey ortalama çekim kısalığı değil, çekim uzunluklarının **1/f
> varyansı**. Eşit dizi varyansı sıfırlar, beyin diziyi çözer ve
> habitüasyona girer — bu yüzden 10 sn → 6 sn indirimi hızlandırmadı:
> aralığı kısalttı, **tahmin edilebilirliği bozmadı.**
> ⭐ Aynı bulgu DERS 24'ü de açıklıyor: ritim OLAY SINIRINDAN (kesme)
> sayılır, klip içeriğinden sayılmaz.
> ⚠️ Ve bandımıza bir soru soruyor [A2-b]: modern ortalama çekim uzunluğu
> 4 sn'nin altında, bizim izinli bandın ortancası 6,0. Izgara değişmedi —
> ama varyans seçilirken **kısa uç tercih edilir.**

Süreler eşit olmaz ama **ölçüye oturur** — müzik hizası korunur:

```
120 BPM → ölçü 2,0 sn → izinli süreler  4 · 6 · 8 · 10
160 BPM → ölçü 1,5 sn → izinli süreler  4,5 · 6 · 7,5 · 9

⛔ SÜTUN PLANDA KALMAZ [DERS 31]: LONG DAY varyansı yazdı, kurgu 10 × 6,0
   kesti, METRONOM 4. kez. Yayından önce: bash araclar/kesme_kontrol.sh

KURAL   en az İKİ sahne KISA · en az BİR sahne UZUN
        doruk sahnesi kendinden ÖNCEKİYLE hız KONTRASTI yapar
        ⭐ ve SÜRE sütununun EN BÜYÜK değeri doruktadır [P2-f]
        toplam 60,0 sn SABİT kalır

ÖRNEK (160 BPM):  6 · 4,5 · 6 · 4,5 · 6 · 7,5 · 6 · 4,5 · 6 · 9  = 60,0
                  ↑ kısa kısa                ↑ nefes        ↑ doruk uzun
```

> ⭐ **18.09.2026 · SAHİP KURALI VE KARŞI KAYIT [C1-e].** Proje sahibi dikey
> shorts'ta sahne süresini SABİT ilan etti (sayı filmin PLAN künyesinde; süre
> varyansı önerilmez). Yukarıdaki DERS 13 · 24 · 44 kaydı SİLİNMEZ — ölçülmüştür
> — ama artık şu okumayla durur: **eşit süre tek başına kötü ritim değildir.**
> Ritmi taşıyan şey sürenin dağılımı değil, her klibin **bir öncekinden farklı bir
> görünür sonuç** taşımasıdır: görsel değişimin büyüklüğü · eylemin yönü · ses
> vurgusu klipten klibe farklılaşır; aynı işin aynı görünümü iki klipte tekrar
> ederse METRONOM oradan doğar, süreden değil. Denetimi KURGU_VE_TESLIM §2.4'te.
> `prompt_kontrol.py`'nin "süreler eşit" FIX'i sahip beyanlı düz ızgarada
> BEKLENENDİR: düzeltilmez, plana kabul edilmiş risk olarak yazılır.
> ⚠️ Bu okuma dış değerlendirmeden geldi ve ÖLÇÜLMEDİ — izleyici deney planının
> 3-4. adımı (QA/ARSIV_12_MERCEK/QA_CAPRAZ_ANALIZ/06) tam bunu ölçer.

## 2.3 NEDEN 10 SAHNE — iki ayrı kazanç

```
① HIZ      Kesme aralığı 10 sn'den 6 sn'ye indi: aynı dakikada 10 kesme.
           Dikey formatta ritmi taşıyan şey kamera hareketi değil (kamera
           sabit), KESMEDİR. Kesme sıklaşınca film hızlanır.
② GÜVENLİK Sahne başına DEĞİŞİM AZALDI. v1'de tek klipte 13 kat çıkıyordu
           ve model geometriyi eritti (② GEOMETRIC STABILITY 0/10).
           10 aşamaya bölününce her klip TEK ve KÜÇÜK bir iş adımı taşır.
           ⭐ Yani daha hızlı film, aynı zamanda daha az riskli filmdir.
           Bu ikisi genelde çelişir; burada çelişmiyor.
```

## 2.4 Kart

```
YAPI:        10 sahne × 6,0 sn + 1 kapak kartı × 5,0 sn
             ⛔ Klip süresi bir TERCİH değil, ARACIN AYARI. Plan yazılmadan
                önce tek bir test klibi üretilir ve ızgara O SAYIDAN yazılır:
                  ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
                Ölçülen 6,0 değilse (örn. 6,004) bütün zaman kodları ve
                müzik ızgarası O SAYIDAN türetilir [D-d].

DOSYA:       Tek .md · film klasörünün içinde
İMAJ:        ⭐ N+1  (10 sahne → 11) · kapak AYRI ÜRETİLMEZ, GN'den türer
VİDEO:       ⭐ N klip × I2V = 10 prompt · ⛔ T2V YOK [§2.7 ②]
             ⇒ film başına toplam 2N+1 = 21 prompt
ÜRETİM:      image → image-to-video   ⭐ I2V BİRİNCİL VE İKİ KAREYLE KİLİTLİ
             ⛔ İKİ KEYFRAME ZİNCİRİ — formatın kendisi [§2.7]:
                klip n'in ilk karesi Gn, son karesi G(n+1)'dir; her görsel
                bir öncekinin karesinden türetilir (§8 ters inşa) [DERS 5]
ŞABLON:      TIMELAPSE_SISTEM_PROMPTU.md
KAPI:        araclar/prompt_kontrol.py (üretimden ÖNCE)
             + FİNAL KARE KANITI (§8 adım 9)
             + QA dört mercek (yayından ÖNCE · QA/00_README)

DİL:         Belgeler TÜRKÇE · üretim promptları İngilizce
             ⛔ BAŞLIK, AÇIKLAMA, HASHTAG ve KAPAK METNİ İNGİLİZCEDİR.
                Yalnız QA raporları ve depo belgeleri Türkçedir.

KRİTİK FARK: Sahneler arası değişen tek şey ZAMANDIR. Kamera, arka plan,
             yapı tasarımı ve kadraj on sahnede de birebir aynıdır.
             ⛔ VE KESMEDE ZAMAN DA ATLAMAZ [§2.7 ①]: dikişin iki yakası
                aynı karedir. Zaman yalnız klibin İÇİNDE akar.

GÜVENLİ ALAN (1080×1920):
             ÜST   ilk 200-254 px   sekmeler, profil
             ALT   son 484 px       açıklama, müzik, CTA  ← y=1436 altı GÖRÜNMEZ
             SAĞ   son 242 px       beğen / paylaş / yorum
             SOL   ilk 122 px
             KURAL: yapının TACI y=254'ün üstüne çıkmaz.
                    Aşama kanıtı asla y=1436'nın altında ve sağ 242 px'te durmaz.
```

## 2.5 REFERANS AŞAMA IZGARASI — şehir içi kule, 10 sahne

```
S0  arsa · İLK KAZI BAŞLAR          ← kanca İLERİ yönlüdür [DERS 3]
S1  kazı derinleşir                 (çukur istasyonu)
S2  iksa tamam · donatı serilir     (çukur istasyonu)
S3  radye dökümü · bodrum çıkar
S4  çekirdek yükselir · VİNÇ KURULUR
S5  ilk katlar — 5. döşeme komşunun çatı hizasında
S6  KIŞ ① kar yağar, kat döngüsü yavaşlar
S7  KIŞ ② kar erir, çamur, döngü hızlanır → karkas tamamlanır
S8  cephe aşağıdan yukarı sarılır
S9  ⭐ USTA KARE — teslim · ikindi · gölge komşunun cephesinde
─────────────────────────────────────────────────────────────
KART  5,0 sn · başlıklı kapak · SAHNE DEĞİL

⛔ TERS AÇILIŞ KULLANILMAZ [DERS 3]. v1'de S0 bitmiş kuleyle açılıp geriye
   söküldü; ④ "sabotages its own promise" dedi, ③ "cut 1 to cut 2 reverses
   time entirely" dedi. Kanca artık ileri yönlüdür ve vaadi BAŞLIKLI KAPAK
   taşır.
⭐ KIŞ İKİ SAHNEDİR [DERS 7]. Bir mevsim tek klipte hem başlayıp hem
   bitemez; erime görünmezse izleyici iki kış saydığı için filmin süresini
   şişik okur (v1: plan 14 ay, rapor "1,5-2 yıl").
```

## 2.6 ⚠️ 5 SAHNELİK VARYANT VE BEDELİ — ölçüldü

> ⛔ `siparisler/MOTOR_5_SAHNE.md` **02.09.2026'da kaldırıldı** (harici bot
> yolu kapandı). O dosyanın tek ölçülmüş içeriği buydu ve buraya taşındı —
> QA raporlarındaki "MOTOR_5_SAHNE" atıfları bu bölümü işaret eder.

Depo ızgarası 10 × 6,0 = 60,0 sn'dir. Beşe inmek meşrudur ama **dört şeyi
kırar** ve dördü de plana yazılmadan ızgara seçilmez:

| Kural | 10 sahnede | 5 sahnede | Ne yapılıyor |
|---|---|---|---|
| Kesme başına aşama sıçraması | küçük | ⛔ **~2 katı** | ters inşa artık tavsiye değil **ZORUNLU** |
| Ritim [DERS 13] | varyans yazılabilir | ⚠️ 5 eşit kesme = **METRONOM riski** | aşağıya bak |
| Kış iki sahne [DERS 7] | 10'da 2 (%20) | 5'te 2 (**%40**) | kış S2–S3 çiftini alır, başka yere konmaz |
| Detay istasyonu | en fazla 2 | ⛔ **0** | beş sahne de ANA istasyondan |

```
⭐ VARYANSLI IZGARA (120 BPM ölçüsüne oturur, toplam 30,0)
                              6,0 · 4,0 · 6,0 · 4,0 · 10,0 = 30,0 sn
                               3     2     3     2     5    ← ölçü sayısı
⛔ DÜZ IZGARA                  6,0 · 6,0 · 6,0 · 6,0 · 6,0  = 30,0 sn
```

### ⛔ DÜZ IZGARA İKİ KEZ KOŞULDU, İKİ KEZ DÜŞTÜ

```
THE CLOSING SPAN · on kesme 6,0 · 5,8 · 6,2 · …   → ⑥ RİTİM 0/10 · METRONOM
THE NARROW LOT   · dört kesme 6,0 · 6,0 · 6,0 · 6,0 → ⑥ RİTİM 4/10 · METRONOM
  "rigidly spaced 6.0-second intervals … establishing a mechanical metronome
   rhythm rather than an intentional narrative arc or release"
İki farklı ızgarada, iki farklı filmde, aynı hüküm.
```

⛔ **Ve makine bunu yakalamaz:** `prompt_kontrol.py` süre eşitliğini yalnız
6 satır ve üstünde BLOCK eder; 5 satırlık tabloda eşik altında kalır. Beş
sahnede süre eşitliğini yakalayan tek şey ⑥ merceğidir — yani ÜRETİMDEN SONRA.

⭐ **Düz ızgara yine de isteniyorsa** (proje sahibinin kilidi meşru bir
sebeptir) plana yalnız (a) gerekçe ve (b) **kabul edilen risk** yazılır.

```
⛔ TELAFİ ARANMAZ — DENENDİ VE DÜŞTÜ [DERS 24]
   THE MOUNTAIN DOOR'da varyans klibin İÇİNE taşındı: her klipte tek iş
   adımı başka bir saniyede patlıyordu (1,2 · 3,6 · 4,8 · 2,4 · 5,0) ve
   vuruş haritası beş I2V'nin beşine de yazılmıştı.
   ⑥ RHYTHM 0/10 · METRONOM — deponun EN DÜŞÜK ritim skoru.
   Mercek klip içi varyansı hiç görmedi, yalnız kesme aralığını okudu.
   ⭐ Sebep: kamera sabit olduğu için ritmi taşıyan tek şey KESMEDİR.
      Klibin içindeki olay bir vuruş değil, bir içeriktir.
⭐ Ritim isteniyorsa SÜRE SÜTUNU değişir. Başka bir yol ölçülmedi.
```

### ⭐ 5 SAHNENİN ÖLÇÜLMÜŞ TEK KOŞUSU — birebir taşınan tuttu, çevrilen düştü

`THE NARROW LOT` (harici GPT → OpenArt · `QA/ARSIV_12_MERCEK/RAPORLAR/THE_NARROW_LOT.md`):

| Brief'in dayattığı şey | Ne oldu | Ölçüm |
|---|---|---|
| `The scene begins exactly as the provided image.` | 5/5 birebir | ① FRAME IDENTITY **10** |
| `does not move at any point` | 5/5 birebir | ① CAMERA LOCK **10** |
| `occupies exactly the same width of the frame` | 5/5 birebir | ① ANCHOR IDENTITY **10** |
| çapa bloğu **SAYIYLA** (6 kat · 3 baca · 5 pencere) | 5/5 birebir | ⑤ **SAME WORLD** |
| YAPI BIBLE sayıları (oturum · aks) | **0/5 — düştü** | ② STRUCTURE IDENTITY **2** |
| `COMPOSITION` bloğu + güvenli alan | **0/5 — nesre çevrildi** | ① SAFE AREA **4** |
| `TIME RATE` I2V'de | **0/5 — yalnız görselde** | ③ TIME RATE **0** |

⭐ Kural: **birebir dayatılan her cümle 10/10 aldı; anlatılan her şey düştü.**
Bu, 5 sahnelik ızgaraya değil PROMPT MİMARİSİNE ait bir derstir
[DERS 18 · 19 · 20] ve on sahnede de geçerlidir.

---

## 2.7 ⭐ İKİ KEYFRAME ZİNCİRİ — FORMATIN KENDİSİ

> ⛔ **BU BİR VARYANT DEĞİL, FORMATTIR** — 08.09.2026, proje sahibinin kararı.
> Bu tarihten sonra yazılan her film böyle kurulur. Önceki altı film ESKİ
> FORMATTIR, arşivdir ve yeniden üretilmez; prompt kapısı onlara "ESKİ FORMAT"
> der ve geçirmez.

```
foto1 ─ video1 ─ foto2 ─ video2 ─ foto3 ─ video3 ─ foto4 ─ …

Her videonun SOLUNDAKİ foto onun İLK karesi,
                SAĞINDAKİ foto onun SON karesidir.
```

### Sayılar — hepsi tek kuraldan çıkar

```
N sahne  →  N+1 GÖRSEL  ·  N I2V  ·  0 T2V  =  2N+1 prompt
                                               (10 sahne → 21 · 6 sahne → 13)

G0        klip 0'ın ilk karesi · filmin ilk karesi
Gn        klip n−1'in SON karesi VE klip n'in İLK karesi ⭐ tek kare, iki iş
GN        ⭐ USTA KARE — yalnız son klibin hedefi, SAHNE DEĞİLDİR.
          Üretimde İLK üretilen kare budur (§8 adım 2) ve kapak da bundan
          türer [MUZIK_VE_KAPAK §2.2].
klip n    G(n) → G(n+1) · iki ONAYLI kareyle kilitli

⛔ Sahne görselleri sahne bloğunun içindedir ("Scene n of N").
   Usta kare AYRI bölümdedir; prompt kapısı onu sahne saymaz, ama YOKSA
   BLOCK verir — zincirin son halkası odur.
⛔ Plana N satırlık aşama merdiveninin YANINA N+1 satırlık KARE TABLOSU
   yazılır: her görsel ne gösteriyor, hangi klipte, hangi rolde (ilk kare ·
   dikiş · son kare).
```

### Ne değişti — dört madde

```
① KESME ARTIK ZAMAN SIÇRAMASI DEĞİL
   Dikişin iki yakası AYNI KAREDİR: kesmede ışık, gölge, toz ve yapı
   ATLAMAZ. ⇒ §2.4'ün ve §8 adım 7'nin "kesme = zaman sıçraması" satırı
   DÜŞTÜ. Zaman yalnız klibin İÇİNDE akar; her sahne kendi zamanını kendisi
   göstermek zorundadır ve TIME RATE cümlesi artık zamanın TEK taşıyıcısıdır.

② T2V YEDEĞİ DÜŞTÜ
   Metinden üretilen klip iki uca kilitlenemez: zinciri taşımaz, dikişi kırar.
   Bir klip tutmazsa yedek, AYNI İKİ KAREDEN yeniden koşmaktır.
   ⇒ Film başına prompt sayısı 30'dan 21'e iner (10 sahne).

③ KIRPMA ASİMETRİKTİR
   Klibin SON karesi bir HEDEFTİR; atılırsa dikiş kaybolur. Kırpma payının
   tamamı BAŞTAN alınır → KURGU_VE_TESLIM §2.

④ ARAÇ KAPISINA SEKİZİNCİ SORU
   "Araç İKİ kare (ilk + son) alıyor mu?" Almıyorsa bu format o araçta
   ÜRETİLMEZ. Plan tek kareli I2V'ye DÜŞÜRÜLMEZ — araç değiştirilir.
   → ARAC_KARTLARI §4 ölçüm ⑧.
```

### I2V'nin iki ucu — birebir, çevrilmeden [DERS 20]

```
İLK CÜMLE   The scene begins exactly as the provided image.
SON CÜMLE   The shot ends exactly on the second provided image: its last
            frame is that image, matched frame for frame — same framing,
            same light, same objects in the same places.

⛔ İkisi de prompt kapısının aradığı İMZADIR. Nesre çevrilirse kapı BLOCK verir.
⭐ Sebebi §2.6'nın tablosudur: birebir dayatılan her cümle 10/10 aldı,
   anlatılan her şey düştü.
```

### Neden — üç ölçüm

```
⑤ DEVAMLILIK beş filmde beş kez düştü ve beşinde de sebep DİKİŞTİ
  (CLOSING SPAN 9/9 kusurlu dikiş · MOUNTAIN DOOR 4/4 · DUST YEAR 9'un 7'si).
  Zincir bunu YAPISAL olarak kapatır: dikişin yerinde kare hiç değişmez.
① KAMERA KİLİDİ artık promptun iyi niyetine değil GEOMETRİYE bağlanır [A3-d]:
  ilk/son kare, aracın kilit KANALIDIR — MOUNTAIN DOOR'da aynı cümle bir
  araçta 10/10, başkasında 0/10 almıştı [DERS 23].
⑥ METRONOM beş kez geldi ve DERS 44 ölçtü: gerekçe süre varyansı değil
  "anchor survival across the seams" idi. Zincir tam onu hedefler.
```

### ⛔ QA MERCEKLERİ DEĞİŞMEZ — format kendini aynı rubrikte kanıtlar

```
⑤ DEVAMLILIK ve ⑥ GEÇİŞ rubriklerine "dikiş sürekli olmalı" YAZILMAZ.
İkisi de mod V/D ile koşar ve mercek plandan habersizdir [değişmez ⑦].
⭐ Sebep: format dikişi YAPISAL olarak kapattığını iddia ediyor. İddiayı
  sınayacak olan, iddiayı bilmeyen bir okuyucudur. Rubriği formata göre
  ayarlamak, ölçümü kaybetmektir.
```

### ⛔ BEDELİ — bu format neyi kaldırdı [değişmez ⑤]

```
· "AYLAR GEÇİYOR"U KESME TAŞIMAZ. Uzun zaman yayları artık yalnız klip
  içinde anlatılır; sıçramayla gelen ucuz zaman duygusu gitti.
· T2V YEDEĞİ YOK. Araç bir klipte tutmazsa elde metin yolu kalmaz.
· BİR GÖRSEL DAHA üretilir ve zincir bir halka uzar: N+1 kare, N+1 kapı.
· ARAÇ BAĞIMLILIĞI SERTLEŞTİ: iki kareli modu olmayan araçta format yürümez.
· ⚠️ VE HİÇ ÖLÇÜLMEDİ. Zincir bu depoda hiçbir filmde koşulmadı [AGENTS §6];
  format artık en yüksek kaldıraçlı VE en az sınanmış karardır. Zincire karşı
  bir iddia da var (§8 adım 3a) ve o da koşulmadı. İlk koşacak film:
  BEFORE NIGHTFALL.
```

---

## 2.8 ⭐ YATAY MERDİVEN — 16:9 · 12 / 24 / 36 / 48 SAHNE × 10,0 s 🆕 14.09.2026

> **Sahip kararı (14.09.2026):** kardeş depo `film_md`'nin yatay film klasörü şablonu bu depoya
> taşındı — dört format klasörü, sekiz dosyalı iskelet, `00_ANALIZ/`, açma betiği. **İçerik bu
> deponun kılavuzları ve dersleridir**: `film_md`'nin tema / novum / kurulum yayı / karakter
> kapıları ve D-numaralı dersleri burada geçmez (§1.2). Değişen tek şey kadraj ve uzunluktur;
> zincir (§2.7), değişmezler (§3), merdiven (§4), güneş saati (§5), konsept kapısı (§6), negatif
> çekirdek (§7) ve ters inşa (§8) aynen geçerlidir.

```
KLASÖR             yatay_2_dk_filmler   yatay_4_dk_filmler   yatay_6_dk_filmler   yatay_8_dk_filmler
SAHNE × KLİP       12 × 10,0            24 × 10,0            36 × 10,0            48 × 10,0
SAHNE BLOĞU        120,0 s (2:00)       240,0 s (4:00)       360,0 s (6:00)       480,0 s (8:00)
+ KAPAK KARTI      5,0 s → 125,0        5,0 s → 245,0        5,0 s → 365,0        5,0 s → 485,0
GÖRSEL / I2V       13 / 12              25 / 24              37 / 36              49 / 48      (N+1 · T2V YOK)
BÖLÜM DOSYASI      2 × 6 · sınır G6     2 × 12 · sınır G12   2 × 18 · sınır G18   2 × 24 · sınır G24
QA BİRİMİ          FİLM                 FİLM                 BÖLÜM (2 yarım × 12) BÖLÜM (2 yarım × 12)
IŞIK GÜNÜ          B ağırlıklı          A ağırlıklı          A + ≤3 B             A + ≤3 B
MÜZİK              120 BPM · ölçü 2,0 s · 5 ölçü/sahne · kesmeler her 10,0 s · müziksiz pencere S0
IZGARA             ⛔ DÜZ N × 10,0 — sahip beyanı; karşı kayıt DERS 13 · 24 · 44 (düz üç kez METRONOM,
                   varyanslı üç kez RHYTHM). Ritim isteniyorsa SÜRE sütunu (izinli 4 · 6 · 8 · 10 · 12).
KLİP KUTUSU        10,0 s teslim → {5,10} kutusu; ⛔ ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · 31]
```

### Kadraj hesabı — yatay [KAMERA_ISTASYONU §3'ün 16:9 hâli]

Tam kare 24 mm, kare eni 36 mm; 16:9 kırpmada kare boyu 20,25 mm. Bir noktanın kare içindeki yeri:

```
   yüzde(y)  = 50 + 118,5 · (y − h) / D          dikey yer, ALT kenardan   (dikeyde katsayı 66,7)
   yüzde(x)  = 50 + 66,7 · x / D                 yatay yer, SOLDAN (x = eksenden sağa metre)
   D (taç %82 için) = (H − h) / 0,27              dikeyde (H − h)/0,48 — kamera 1,8 KAT UZAĞA gider
   px (1080p) = 1280 · boy(m) / D                 referans nesne piksel boyu — dikeyle AYNI katsayı

   ① UFUK tilt 0°'da yine tam %50'dedir.
   ② KADRAJIN BOŞ YERİ YANLARDIR, üst değil: dikeyde yapı kadrajın boş üstüne büyüyordu; yatayda
      iki yan SAHAYA kalır → arka plan çapalarından en az biri yapının SOLUNDA, en az biri SAĞINDA
      durur ve her promptta adıyla yazılır. Yapı gölgesi yana düşer — süpürme yatayda uzun okunur.
   ③ TİLT yine 0°: kadraj yetmiyorsa kamera YÜKSELİR ya da uzaklaşır, eğilmez.
   ⚠️ Bu hesap formülden türedi, ÖLÇÜLMEDİ — ilk yatay filmin ① koşusu doğrular.
```

### Güvenli alan — 1920×1080 ⬜ ÖLÇÜLMEDİ (varsayılan)

```
ÜST     ilk 60 px      oynatıcı başlık/paylaş bandı (üstüne gelince)   → yapının TACI buraya girmez
ALT     son 100 px     ilerleme çubuğu + kontroller                    → kanıt nesnesi buraya girmez
SAĞ ÜST 300 × 100 px   bilgi kartı                                      → kanıt nesnesi buraya girmez
SON EKRAN  son 5–20 s  öğeler kadrajı kaplar → kapak kartı 5,0 s o bandın içindedir; final kanıtı
           kartta değil, son sahnenin ≥2,0 s'lik TUTUŞUNDADIR
COMPOSITION cümlesi: "the crown of the structure sits below the top eighth of the frame and the
working level sits above the bottom quarter of the frame; nothing that proves progress falls into
the bottom tenth or the top-right corner of the frame."
⛔ Sayılar ilk yatay filmin ① koşusunda ölçülür ve BURAYA yazılır; README'ler buraya işaret eder.
```

### Işık günü toplanır — rejim sütunu [SANTIYE_HAREKETI §1 · §2.7 ①]

```
Kesmede ışık atlamaz (dikişin iki yakası aynı kare) → filmin ışık günü KLİPLERİN PENCERE TOPLAMIDIR:
   Σ = (A × 10 dk) + (B × 2 saat) + (C × 9 saat)  ≤ 14 saat (06:00 → 20:00) — gece yalnız sahip kararıyla
   12 sahne   6 × B + 6 × A = 13 h    ✓  (tek ışık günü B ağırlıklı — dikey filmlerle aynı)
   24 sahne   5 × B + 19 × A = 13,2 h ✓  (A ağırlıklı; B klipleri doruk ve kış sahnelerine)
   36 sahne   3 × B + 33 × A = 11,5 h ✓
   48 sahne   3 × B + 45 × A = 13,5 h ✓ — C YOK (gölgesiz klip en uzun klip olamaz [DERS 40])
   Takvim (haftalar / aylar) SAHADAN okunur (tarla · ağaç · kar · su), ışıktan değil [P1-c].
   Rejim A'da gölge klip içinde fark edilmez → iş YÜZEYLE ve makineyle kanıtlanır (§3); rejim B
   klipleri gölge süpürmesini taşır [DERS 32 · 47]. PLAN §AŞAMA MERDİVENİ toplamı yazar,
   03_SAHNE_SIRALAMASI §4 hesaplar. ⚠️ Hesaptır, ölçülmedi.
```

### Aşama merdiveni uzayınca ne olur

```
Sahne arttıkça YAPI BÜYÜMEZ, AŞAMA İNCELİR: her eleman ara hâlleriyle (%25 / %50 / %75) kendi
satırını alır [INSAAT_YONTEMI §2 · DERS 37]; kış yine iki sahne [DERS 7]; monoton büyüme yasası aynı.
36/48 sahne için SÜRE ≥ 2 yıl olan kartlar (köprü · baraj · liman · stadyum) doğal adaydır; 12 sahne
için türbin · villa · yol (6–12 ay). Detay istasyonu kuralı değişmez (≤2 klip · üç koşul ·
KAMERA_ISTASYONU §1); ⬜ uzun formda bölüm başına 2'ye çıkarılıp çıkarılmayacağı sahip kararı.
```

### ⭐ MODÜL DIŞI IZGARA — sahip izniyle (16.09.2026)

```
Modül ızgarası (12/24/36/48 × 10,0) bandın kendisidir. Sahip başka bir ızgara isterse:
  · toplam süre KORUNUR (N × klip + 5,0 sn kart) · kadraj hesabı, ışık günü tavanı ve zincir DEĞİŞMEZ
  · betik parametre alır:  bash araclar/film_klasoru_ac.sh <FMT> <FILM> <SAHNE> <KLIP>
    sahne sayısı TEK olabilir (B1 = ceil(N/2) · B2 = kalan); betik bandın dışını UYARIR, engellemez
  · PLAN'ın künyesine ve §DÜZ IZGARA BEYANI'na gerekçe yazılır; müzik ölçüsü klipten türer (klip ÷ 2 ölçü)
İLK KOŞU  THE_OLD_ROAD — yatay_2_dk_filmler'de 15 × 8,0 (2 dk hattı, 14 kesme). Ölçüm yayından sonra.
```

### İskelet ve kapılar

```
KLASÖR    <FMT>/<FILM>/  →  00_ANALIZ/ (6 dosya + sahne tablosu) · <FILM>_PLAN · _BOLUM_1 · _BOLUM_2
          (+ USTA KARE) · _KAPAK · _MUZIK · _YAYIN_PAKETI · _QA_SPEC · _URETIM_GUNLUGU
          kopyalanabilir hâli kilavuzlar/FILM_KLASOR_SABLONU/ · betik araclar/film_klasoru_ac.sh
          ⛔ elle cp -r yapılmaz; ⛔ format klasörünün köküne .md bırakılmaz (sayaç uyarır)
BÖLÜM     iki dosya YAZIM birimidir, üretim sırası değil; sınır bir KAREDİR (G_k), kesme değil —
          BOLUM_1'in son I2V'si G_k'de biter, G_k BOLUM_2'nin ilk görselidir [DERS 52]
KAPI      python3 araclar/prompt_kontrol.py <FMT>/<FILM>     ⭐ KLASÖR MODU (PLAN + BOLUM_1 + BOLUM_2)
          bash araclar/kesme_kontrol.sh <teslim> <FILM>_PLAN.md · bash araclar/qa_paket.sh <FMT>/<FILM> …
          6/8 dk yarım master: qa_paket.sh --bolum 1|2 · ham QA/HAM/<FILM>/<FILM>_B1_Q<n>_<AD>_HAM.md ·
          QA/TABLO.md iki satır (B1 · B2) · QA/FILMLER tek dosya
ONAY      00_ANALIZ/00_HIKAYE_ONAYI.md — sahne sahne öneri, açık onay, sonra dosya (onay-once-uretim)
DİKEY     ayrı hat: oradaki film buraya taşınmaz, buradaki film oraya kırpılmaz (kadraj hesabı,
          güvenli alan, ızgara farklı — CAPRAZ_YAYIN tek master)
```

---

# 3. 🔒 DEĞİŞMEZLER TABLOSU — bu depodaki en önemli tablo

`film_md`'nin Character Bible'ının karşılığıdır ve aynı disiplinle işler:
**her görsel promptta birebir, kısaltmasız tekrarlanır.** `[DEĞİŞMEZLER]`
gibi köşeli parantez atfı YASAKTIR — model belgeyi okumaz, promptu çizer.

Her filmin başında doldurulur:

```
┌─ KAMERA İSTASYONU (ana) ────────────────────────────────────────────┐
│ lens          24 mm küresel · f/8 · ISO 100                         │
│ yükseklik     24,0 m — karşı bloğun çatı parapeti                   │
│ mesafe        yapının güney yüzünden 72 m                           │
│ bakış açısı   215° (güneybatı) · tilt 0° · roll 0°                  │
│ sabitleme     "bolted to a fixed tripod, absolutely zero movement"   │
│ ⛔ Bu dört sayı KAMERA_ISTASYONU §3 formülünden çıkar, seçilmez:     │
│    D = (H − h) / 0,48  →  (58 − 24) / 0,48 = 71 m ≈ 72 m            │
└─────────────────────────────────────────────────────────────────────┘

┌─ ARKA PLAN ÇAPALARI — en az 3, isimlendirilmiş ─────────────────────┐
│ ① sağda 5 katlı kırmızı tuğla apartman, çatısında iki baca          │
│ ② solda tek servi ağacı, gövdesi eğik                               │
│ ③ arkada alçak sırt hattı, üzerinde dağınık düşük yapı silueti      │
│ ⛔ Bunlar HER karede aynı yerde, aynı boyutta, aynı şekildedir.      │
│    Timelapse'i timelapse yapan şey yapının değişmesi DEĞİL,          │
│    arkasındakinin değişmemesidir.                                    │
└─────────────────────────────────────────────────────────────────────┘

┌─ UFUK VE ÇERÇEVE ──────────────────────────────────────────────────┐
│ ufuk çizgisi   kare yüksekliğinin tam %50'sinde — tilt 0° geometrisi │
│                (bu bir tercih değil, sonuçtur · KAMERA_ISTASYONU §3)│
│ yapı tabanı    %27,8 · yapı tacı %81,5 — altı sahnede de aynı       │
│ şantiye sınırı mavi panel çit, kadrajın %25-28 bandında             │
│ yol            sağ alt köşeden kadraja giren asfalt, sabit          │
└─────────────────────────────────────────────────────────────────────┘

┌─ YAPI BIBLE — tamamlanmış hâlin sabit geometrisi ──────────────────┐
│ kat sayısı     18                                                   │
│ oturum         24 × 18 m                                            │
│ kat yüksekliği 3,20 m · toplam 58 m                                 │
│ aks düzeni     6 × 4 kolon, 4,0 m aralık                            │
│ çekirdek       kuzeydoğu köşede tek betonarme çekirdek              │
│ cephe          antrasit alüminyum çerçeve + açık gri cam            │
│ taç            düz çatı, çatı parapeti 1,10 m, tek mekanik hacim    │
│ ⛔ Bu satırlar S0'da bile geçerlidir: S0'da bina YOKTUR ama          │
│    üretilecek olan bina BUDUR ve ters üretimde referanstır.          │
│ ⭐ SAYI TESTİ [P2-b]: izleyici kadrajda SAYABİLİR mi? Sayabilir      │
│    (18 kat · 3 baca) → prompta. Sayamaz (62 lamba · %27,8) → SPEC'e; │
│    prompta yapısal hâli: "one evenly spaced line of lights".         │
└─────────────────────────────────────────────────────────────────────┘
```

> ⛔ **DEĞİŞMEZ BLOĞUNA GEÇİCİ EKİPMAN YAZILMAZ [DERS 1].** "Değişmez",
> "kadrajda hep görünen" demek değil, "filmin ömrü boyunca DEĞİŞMEYEN"
> demektir. Şantiye çiti, vinç, iskele, konteyner, kalıp ve tırmanan
> platform kadrajda görünür ama SÖKÜLÜR — onlar `SITE TEXTURE` / `ACTIVITY`
> bloğuna yazılır ve §4'ün SÖKÜM SATIRI'nda takip edilir. Bu ayrımı
> yapmayan bir plan, çitin söküldüğü sahnede kendi değişmez bloğunu
> ihlal eder ve prompt kapısı bunu BLOCK olarak görür.
>
> ⛔ **DEĞİŞMEZ, "aynı kelimelerle yazılan" demektir, "aynı şeyi anlatan"
> demek değildir.** Servi ağacını bir promptta *"a tall cypress"*, ötekinde
> *"a dark narrow tree"* diye yazarsan model iki farklı ağaç çizer ve
> arka plan çapası çöker. Blok bir kez yazılır, kopyalanır.

---

# 4. 🪜 AŞAMA MERDİVENİ — planın omurgası

`film_md`'nin vuruş tablosunun karşılığı. Sahne haritasından ÖNCE doldurulur.

### Tek yasa: MONOTON BÜYÜME

```
Aşama N, Aşama N-1'in EKRANDA GÖRÜNEN HER ŞEYİNİ içerir + yeni iş.
Yapılmış bir iş geri alınmaz, yer değiştirmez, boyut değiştirmez.
TEK İSTİSNA: geçici olduğu ilan edilen ekipman (vinç · kalıp · iskele ·
konteyner · şantiye çiti) sökülebilir — ama sökülüşü PLANA YAZILIR,
sahne sırasında kendiliğinden kaybolmaz.
```

### Şablon — 10 satır

| S | SÜRE | AŞAMA | EKRANDA VAR OLAN | YENİ OLAN | TEMSİL | MEVSİM TAŞIYICISI | KANIT NESNESİ | İSTASYON |
|:-:|---:|---|---|---|---|---|---|---|
| 0 | arsa · ilk kazı | çit · konteyner · moloz | ilk ekskavatör iz açar | 1 gün | yaz | açılan ilk yarık | ANA |
| 1 | kazı derinleşir | + çukur | çukur 6 m | 3 hafta | yaz | çukur ağzı | ÇUKUR |
| 2 | iksa + donatı | + iksa perdesi | donatı hasırı | 5 hafta | erken sonbahar | çukur tabanı 13 m | ÇUKUR |
| 3 | radye + bodrum | + temel · bodrum | zeminden çıkış | 2 ay | sonbahar | zemin kotu geçildi | ANA |
| 4 | çekirdek + vinç | + çekirdek | ⭐ VİNÇ KURULDU | 2 ay | geç sonbahar | vinç mastı | ANA |
| 5 | ilk katlar | + 5 kat | kalıp döngüsü | 6 hafta | erken kış | ⭐ 5. döşeme = komşu çatısı | ANA |
| 6 | KIŞ ① kar yağar | + 9 kat | döngü yavaşlar | 2 ay | kış · kar birikir | kat sayısı yavaş artıyor | ANA |
| 7 | KIŞ ② kar erir | + 18 kat | döngü hızlanır | 2 ay | ilkbahar · erime + çamur | ⭐ ufku geçiş → gökyüzü | ANA |
| 8 | cephe | + cephe tepeye kadar | vinç sökülüyor | 3 ay | yaz | cephe hattının tırmanışı | ANA |
| 9 | ⭐ teslim | + tamamlanmış yapı | ışıklar · peyzaj | 1 gün | erken sonbahar · ikindi | ⭐ gölge komşunun cephesinde | ANA |

```
⭐ İKİ YENİ SÜTUN — ikisi de BOŞ BIRAKILAMAZ

SÜRE                Izgaraya oturan süre (§2.2). On sahnenin süresi eşitse
                    tablo geçersizdir: en az iki kısa, en az bir uzun [DERS 13].

MEVSİM TAŞIYICISI   O sahnede mevsimi EKRANDA taşıyan NESNE.
                    ⛔ "kış" bir taşıyıcı değildir; "yamaçtaki kar çizgisi",
                       "çıplak dallar", "sararmış ot", "su seviyesi" taşıyıcıdır.
                    ⛔ Taşıyıcı yoksa iki seçenek: (a) kadraja bir taşıyıcı
                       SOK, (b) o sahne mevsim BEYAN ETMEZ ve güneş yüksekliği
                       tek saat göstergesi olur.
                    Ölçüldü: iki sahnede taşıyıcı yoktu ("bare rock, no
                    foliage, no weather carrier") ve ③ filmin 34 aylık
                    süresini "yaklaşık bir yıl" okudu [DERS 14].
```

⛔ **İSTASYON BÜTÇESİ: en fazla 2 detay sahnesi, ve her ikisi de bir ÇAPA
taşır.** v1'de çukur sahnesinde hiçbir çapa görünmedi (① C3 0/10) ve mercek
o klibin aynı şantiye olduğunu doğrulayamadı. Detay istasyonu, çapasız
kurulamaz.

### ⭐ İki satır daha — profesyonel okumadan [P1-a · P1-f]

```
KİNETİK İMZA   her satıra TEK FİİL: iz açar · keser · teleskoplanır · indirir ·
               boşaltır · gömer · yükseltir · kapatır · aydınlanır.
               ⛔ Ardışık iki satırda aynı fiil = tablo geçersiz [P1-f].
İLK 20 SANİYE  S1-S3'ün her biri FARKLI TÜRDEN ve BÜYÜK bir değişim taşır.
               "stok büyüdü" türü hazırlık adımı kendi sahnesini almaz [P1-a].
               Test: S3'ün son karesi ile S0'ın ilk karesi yan yana konunca
               yapının TÜRÜ okunuyor mu?
```

### Üç zorunlu satır

```
① KANIT NESNESİ:  her sahnede ilerlemeyi ekranda KANITLAYAN tek nesne.
   "bina büyüdü" bir kanıt değildir — kaç kat, hangi hizada, neye göre.
   Kanıt nesnesi arka plan çapalarından birine göre ölçülür:
   "the slab edge now sits level with the roof ridge of the brick block."

   ⛔ VE AYRICA ⑤ İÇİN BİR "AYNI YER" NESNESİ SEÇİLİR — taşınamayacak,
      sökülmeyecek, beş karede de aynı yerde duracak tek bir şey.
      ⭐ Bu nesne bir PROMPT maddesi değil, bir ÜRETİM KAPISI maddesidir
         [DERS 25]: zincir_kontrol.sh'in her koşusunda iki karede de aynı
         yerde olduğu ELLE doğrulanır. Kaybolduysa kare ATILIR.
      Ölçüldü: MOUNTAIN DOOR'da nesne (2,4 m granit kaya) beş promptun
      beşine de birebir yazılmıştı ve filmin İLK dikişinde kayboldu;
      ⑤ "THE OBJECT THAT PROVES IT IS THE SAME PLACE: NONE FOUND" yazdı.
      Zincirden geçmeyen bir çapa, modelden dilenen bir iyiliktir.

② LOOP SATIRI:  S5'in son karesi ile S0'ın ilk karesi AYNI kadrajdır.
   Boş arsa → bitmiş kule, aynı çerçeve. Viral ödeme burasıdır.

③ SÖKÜM SATIRI: vinç/iskele/çit hangi sahnede kurulur, hangi sahnede
   sökülür. Yazılmazsa model onları rastgele yok eder ve devamlılık ölür.
   ⭐ VE NASIL [P2-h]: her kalem I2V'de bir FİİL alır ("stripped panel by
      panel and stacked on the flatbed, which drives out of frame").
      Söküm bir eylemdir, bir kaybolma değil; ⑦ ve ⑧ bunu ölçer.
```

---

# 5. ☀️ GÜNEŞ SAATİ KİLİDİ

Bir timelapse'in sahte durmasının en sık sebebi ışığın rastgele olmasıdır.
Gölge, saatin kendisidir.

```
İKİ AYRI SAAT VAR — KARIŞTIRMA:

  SAHNE İÇİ SAAT   10 saniyenin İÇİNDE geçen zaman (genelde 1 gün)
                   → gölge kadrajı süpürür, bulutlar çizgi olur
  SAHNELER ARASI   sahneler ARASINDA geçen zaman (hafta/ay/mevsim)
                   → güneşin yıl içindeki yüksekliği ve rengi değişir

HER PROMPTTA SAYIYLA YAZILIR:
  "sun azimuth 118°, elevation 34°, shadows falling to the west-north-west"

KURALLAR
  · Sahne içinde güneş TEK YÖNDE ilerler — geri dönmez, atlamaz.
  · Sahneler arası mevsim tek yönde ilerler: yaz→sonbahar→kış→ilkbahar→yaz.
    Geri giden bir mevsim, izleyicinin fark etmeden güvenini kaybettiği şeydir.
  · Kış sahnesinde gölgeler UZUN ve güneş ALÇAK (elevation ≤ 22°).
    Yaz öğlesinde KISA ve YÜKSEK (≥ 60°). Bu iki sayı mevsimi ışıkla anlatır.
  · Gece sahnesi kullanılacaksa yalnız S5'te: ışıklar kat kat yanar.
    Bu, filmin tek "duygusal" anıdır ve bir kez kullanılır.
```

---

# 6. 🚪 KONSEPT KAPISI — VAAT / DİRENÇ / BEDEL

> **Bu bölüm `film_md`'nin 30.08.2026 tarihli hat teşhisinden doğrudan
> devralındı ve o teşhisin bedeli 18 filmdir.** Orada bulunan şey şuydu:
> dört üretim önlemi birikip sessizce bir tür yarattı — *isimsiz, sessiz,
> yalnız, hareketsiz.* Kimse o türü seçmedi; BİRİKTİ. Timelapse'in aynı
> tuzağı şudur: **teknik olarak kusursuz ama hiçbir şey anlatmayan güzel
> bir büyüme animasyonu.** İlacı ilk günden yazıyoruz.

Plan yazılmadan önce üç satır doldurulur:

```
VAAT:    bu şantiye NE OLACAK — video başlamadan önce bile var olan iş
DİRENÇ:  coğrafya / iklim / ölçek bunu NASIL zorlaştırıyor
BEDEL:   kazanmak için ne yok oluyor

⛔ KAPI: "büyüyor", "yükseliyor", "tamamlanıyor" VAAT DEĞİLDİR —
   bunlar formatın kendisidir, filmin konusu değil.
⛔ KAPI: DİRENÇ boşsa video bir slayt gösterisidir. Her yapı bir şeye
   direnir: kış · su · eğim · rüzgâr · dar parsel · trafik · zemin.
⛔ KAPI: BEDEL boşsa filmin sonu "bitti" olur, "oldu" olmaz.
⛔ KAPI [P1-b]: DİRENÇ satırının üçüncü alanı EKRANDA NASIL — hangi sahnede,
   hangi tekrarlı hareketle, hangi biriken nesneyle. Boşsa direnç bible
   bilgisidir, film bilgisi değil ("900 ton metinde güçlü, görüntüde yok").
```

Ve üç kabul testi (`film_md` novum kapısının timelapse hâli):

```
① TEK KARE TESTİ    Tek donmuş karede izleyici (a) NE yapıldığını ve
                    (b) sürecin NERESİNDE olunduğunu 1 saniyede söyleyebiliyor mu?
② KİNETİK BAĞIMSIZLIK  Değişim, 10 saniyelik SABİT bir planın içinde
                    metin/anlatıcı olmadan görülebiliyor mu?
③ BAŞLIK ŞEMASI    Vaat ≤5 kelimelik bir başlığa çevrilebiliyor mu?
④ OMURGA CÜMLESİ   On vuruş, her biri ≤4 kelime, tek satır, ok işaretleriyle
                   [P1-k]. Yazılamayan vuruş = olmayan sahne; aynı şeyi
                   söyleyen iki vuruş = fazla sahne. Merdiven BUNDAN türer.

Dördü de ✅ değilse KONSEPT REDDEDİLİR, klasör açılmaz.
```

### ⭐ İZLEYİCİ KAPISI — dört zorunlu satır [C2-a…d · 05.10.2026]

> 31 filmin ④ TESLİM raporundan çıktı (C2): ④ 9+ alan altı filmin altısı da bir
> **İŞLEV ANIYLA** biter; kancası 9-10 olanlar **tanıdık bir nesneyle** açılır;
> döngü 9-10 yalnız en üst grupta. ⚠️ Kaynak değerlendirici yargısıdır, izleyici
> verisi değil — `apexait/IZLEYICI_DEFTERI.md` doğrular ya da düşürür.

```
İŞLEV ANI:        son klipte ne ÇALIŞIYOR — yanar · açılır · akar · döner · kalkar · durulur.
                  "Bitmiş yapı durur" İŞLEV ANI DEĞİLDİR (STONE TOWER · GLASS WALL ·
                  IRON BRIDGE ④ 5,7-7,5). Olay finalin İLK yarısında, ikinci yarı TUTUŞ (adım 9).
AÇILIŞ NESNESİ:   G0'da izleyicinin 1 sn'de tanıdığı nesne + ona ne oluyor (tehdit · tuhaflık ·
                  terk). Çimin sökülmesi · taşkın tehdidi · paslı gemi · mavi kapı = kanca 9-10;
                  boş tarlada hafriyat = 4-6 (EMPTY RIDGE · MOUNTAIN DOOR · NARROW LOT).
DİRENÇ EKRANDA:   yukarıdaki P1-b satırı — kadrajda GÖRÜNEN düşman (deniz · fırtına · ışık yarışı
                  · eğim). "Rüzgâr beklenir" ekranda yoktur (EMPTY RIDGE direnç 2).
DÖNGÜ KAFİYESİ:   G7 ile G0 aynı yerde aynı biçimi taşır (G0'da 47 px kaya tacı → G7'de aynı yerde
                  gövde) · İŞLEV ANI kadrajda KALIR (BACK TO WATER döngü 3: tekne kadrajdan çıktı) ·
                  G7 ışığı G0'a geri bağlanır.

⛔ KAPI: dikey planın künyesinde İŞLEV ANI · AÇILIŞ NESNESİ · DÖNGÜ KAFİYESİ satırları yoksa
   prompt_kontrol.py BLOCK verir [§10f · C2]. DİRENÇ zaten §6'nın kendi satırıdır.
⭐ KONU SEÇİMİ [C2-e]: VAR OLANI DÖNÜŞTÜRMEK (havuz→sinema · çim→oda · gemi→bahçe) sıfırdan
   inşadan daha iyi okundu (④ ≈7,8 · ≈6,2). Uzay ancak tanıdık/gizemli bir nesneyle tuttu
   (FIRST GUEST'in kapısı). Sıfırdan inşa seçilirse İŞLEV ANI iki kat önemlidir.
⚠️ 07.10.2026 [A30-a]: dış havuz (26 vaka) bu ayrımı NE doğruladı NE düşürdü — onarım iki grupta da
   çoğunluk. C2-e değerlendirici okuması olarak kalır; izleyici sınavı IZLEYICI_DEFTERI S1–S2.
⛔ YORUM TUZAĞI YOK [A33-b · 07.10.2026]: filme kasıtlı hata konmaz ("uzman düzeltsin"), metne
   "find the mistake · send this to · tag a friend" yazılmaz — Meta 2017 engagement bait · TikTok FYF
   "Tricking others into increasing engagement". Düzeltme yorumu, doğru yapılmış filmin kendiliğinden
   ürünüdür (KANAL_KIMLIGI §4 birinci halka).
```

### ⭐ AÇILIŞ DÜZENİ — S0 ekranda 4 saniyedir, ilk saniye karar saniyesidir [C2-h · 05.10.2026]

> Shorts akışında izleyici 1-3 sn'de kaydırır ya da kalır (A1 · `IZLEYICI_DEFTERI` KAYDIRMADI %).
> 2x paylaşımda S0'ın 8 saniyesi ekranda 4 sn'dir: **her 1x saniye ekranda yarım saniye.**
> Kanca 9-10 alan filmler (DEEP END · VANISHING ROOM · BLUE DOOR · LAST HARBOR · FIRST GUEST ·
> TIDE GATE) aynı dört vuruşu taşıyor; 4-6 alanlar (EMPTY RIDGE · MOUNTAIN DOOR · NARROW LOT)
> hiçbirini. ⛔ Sınırlar değişmez: ters açılış YOK [DERS 3] · öncesi/sonrası bölme YOK (sahip
> 19.09.2026) · ekranda YAZI YOK · müzik YOK. Merak bunlarsız kurulur.

```
EKRAN (2x)  1x        VURUŞ          NE OLUR                                        ÖRNEK
──────────  ────────  ─────────────  ─────────────────────────────────────────────  ──────────────────────────────
0,0         G0        ① NESNE        AÇILIŞ NESNESİ kadrajın ≥ 1/3'ü, ortada, 120 px  paslı gemi · yapraklı boş havuz
                                     testinde tanınır · "yanlış" hâlde (terk · çürük  · kusursuz çim · paslı silo
                                     · tehdit altında). Boş arazi AÇILIŞ DEĞİLDİR.
0,0-1,0     0-2 sn    ② DOKUNUŞ      eylem İLK KAREDE BAŞLAMIŞTIR ve NESNEYE dokunur:   kapaklar yuvarlanır · çim
                                     açar · söker · keser · boşaltır. Isınma yok,      sökülür · su tahliye olur
                                     "bekleyen saha" yok. İlk ses nesnenin sesi.
1,0-2,0     2-4 sn    ③ İPUCU        GELECEĞİN bir parçası kadraja girer ama AMACI     fidan kasaları rıhtıma iner ·
                                     okunmaz — merak boşluğu. Sonucu göstermez         kırmızı perde topu · cam sandık
                                     (spoiler bütçesi MUZIK_VE_KAPAK §3.3).
2,0-4,0     4-8 sn    ④ ÖLÇEK        iş büyür: ekip ve makine çoğalır (İŞ YOĞUNLUĞU),  ikinci vinç gelir · ekip
                                     ilk kesmede (4,0) S1'in ilk karesi GÖZLE açık     ikiye bölünür · havuz boş
                                     biçimde ileridedir — "ilk kesme ödülü".

MERAK SORUSU   künyede tek satır, ≤ 6 kelime, izleyicinin 1. saniyede sorduğu soru:
               "Bu gemiye ne yapıyorlar?" · "Çimin altında ne var?" — FİNAL onu cevaplar
               (İŞLEV ANI), KAPAK cevabı ima eder, BAŞLIK soruyu söyler.
REJİM S0       A ya da B — hareket ilk saniyede görünür. C (insan silinir) ve G (gerçek zaman,
               çok yavaş) S0'da KULLANILMAZ.
KADRAJ         açılış nesnesi ile işlev anının yeri AYNI (DÖNGÜ KAFİYESİ): izleyici ilk saniyede
               baktığı yerde sonucu görür.
⭐ SEÇENEK     S0 GERİ ÇEKİLME AÇILIŞI [C2-i]: ① NESNE ve ② DOKUNUŞ yakın kadrajda (n× kırpma),
               1x'in ilk 2,5 sn'sinde HOME'a geri çekilir, ③ ④ HOME'da oynar. KURGU kırpmasıdır,
               kamera hareketi değil · tavan ölçülmeden yapılmaz · S0 HOME'da biter →
               KAMERA_HAREKETI_KILAVUZU §4.2

⛔ KAPI (dikey): künyede 'MERAK SORUSU:' yok → BLOCK · S0 I2V'si "from the first frame" ile eylemi
   ilk karede başlatmıyor → BLOCK · S0 rejim C ya da G → FIX.
⚠️ ÖLÇÜLMEDİ — dört vuruş ④ raporlarından türedi. IZLEYICI_DEFTERI'nde 'AÇILIŞ' sütunu
   (nesne · dokunuş · ipucu) KAYDIRMADI % ile karşılaştırılır; üç filmde aynı yön → kural.
```

---

# 7. 🚫 NEGATİF ÇEKİRDEK (tam metin — her prompta yapıştır)

Saha ve yapı kartlarından gelen maddeler bunun ÜSTÜNE eklenir.

⭐ **SIRA VE UZUNLUK [P2-c]:** blok üç katmandır ve bu sırayla yazılır —
① süreklilik katilleri (kamera · çapa · geometri · morph · teleport ·
desteksiz parça; kapı imzaları burada) · ② metin yasağı yüzey yüzey ·
③ estetik yasaklar, en kısa. Hedef ≤1.000 karakter; aşağıdaki tam metin
referanstır, filme inerken bu sırayla KIRPILIR.

⭐ **SAHNEYE ÖZGÜ DIŞLAMA [C1-g · 18.09.2026]:** evrensel uzun blok tek başına
hiçbir arızayı engellemez — 15 filmde çekirdek her prompta yapıştırıldı ve F01 ·
F04 · F05 yine geldi (QA/ARSIV_12_MERCEK/QA_CAPRAZ_ANALIZ/03). Negatif prompt, doğru eylemin
(MOTION FOCUS) ve sağlam referansın (zincir + 3 nirengi) YERİNİ TUTMAZ; onların
yanına, modelin desteklediği biçimde **kısa ve o sahneye özgü 1-3 dışlama**
eklenir ("no second crane", "no snow on the deck"). DERS 35 kalır: metin yasağı
hiçbir nesne adı anmaz. 05_NIHAI_RAPOR'un ilk sürümündeki "tüm promptlara
kilitlenecek evrensel NEGATIVE bloğu" önerisi bu gerekçeyle alınmadı.

```
Locked-off camera on a fixed tripod — the camera never pans, tilts, zooms,
rolls, shakes or drifts, and the framing is identical from the first frame to
the last. Same site, same building, same background in every frame: the horizon
line, the neighbouring buildings, the road, the trees and the ridge behind them
never change shape, position, size or spacing. The structure is one single rigid
building that only ever gains material — nothing already built is removed, moved,
resized or redesigned; the column grid, the bay spacing, the floor height and the
footprint stay exactly as described. No readable text, letters, digits, numbers
or symbols anywhere in the frame — not on the hoarding, the safety signage, the
crane, the machinery, the shipping containers, the workers' vests and helmets,
the trucks, the scaffolding, the formwork or the facade. Nothing in this frame
has been branded, labelled, numbered or annotated by anyone: no company logos,
no flags, no floor numbers, no licence plates, no warning pictograms, no
measurement or survey marks. No melting or warping geometry, no swimming texture,
no opacity fades, no fading into existence, no hologram appearance, no CGI appearing
effect, no floating structure, no floor slab without support beneath it, no crane hanging
from nothing, no machine hovering above the ground. Everything obeys gravity and
stays in continuous physical contact with the ground or the structure. No cuts,
no dissolves, no fades, no transitions, no jump cuts, no camera teleportation, no
angle change. No subtitles, no captions, no title card, no end card, no credits,
no watermark. No architectural visualisation look, no real-estate render look, no
Unreal Engine look, no CGI aesthetic, no video game aesthetic, no miniature or toy
look, no tilt-shift blur. This is a working construction site: mud, tyre ruts,
stacked material, offcuts, tarpaulins, puddles and clutter are present and
untidy. Photorealistic documentary photography, 35mm film grain.
```

**Zaman hızı — TEK CÜMLE, TÜM ÖZNELER [DERS 15]:**

```
Everything in this frame is time-lapsed at the same rate: the clouds, the
shadows, the machines, the people and the vehicles all move at the same
accelerated speed. Nothing in the frame moves at normal speed.
```

> ⛔ **MODEL GÖKYÜZÜNÜ HIZLANDIRIR, YERİ HIZLANDIRMAZ.** Ölçüldü: *"clouds
> race across the sky in heavy time-lapse, while the workers move at near
> real-time speeds"* · *"trucks move at normal video speed"* (③ TIME RATE
> 0/10 · ① PEOPLE 0/10). Prompt "soft motion streaks" diyordu ve tutmadı:
> hız tek tek öznelere yazılınca model onu bir GÖRÜNÜM tarifi sanıyor, bir
> ZAMAN AYARI değil. Cümle promptun BAŞINA, tek parça olarak konur.
> ⭐ Ek önlem: kadrajdaki insan ve araç SAYISINI AZALT — ne kadar az varsa
> o kadar az bozulur.
>
> ⛔ **YOK YAZILAN ÖZNE VAR OLUR [DERS 33]:** insansız filmde "Any suited
> figure appears only as soft motion streaks" astronot ÜRETTİ (① PEOPLE
> 0/10). Kadrajda olmayan özne prompta HİÇ girmez — koşulla, yasakla, "any"
> ile bile. İnsansız film "No people are present." der; kapı bu beyanı
> görünce insan kuralı cümlesini aramaz.
>
> ⭐ GÜNEŞ KAMERA ARKASINDAYSA [DERS 32]: "the sun stays behind the camera
> for the whole shot; its only sign is the shadows" — azimut satırı kalır,
> disk anılmaz. LONG DAY'de güneş üç klipte kadraja girdi.
>
> ⭐ ÖZNE LİSTESİ SAHADAN YAZILIR [P1-e → DERS 33]: kapı imzası (`time-lapsed at the
> same rate`) korunur, ama "the clouds … the people" yalnız o kadrajda VARSA
> yazılır. Negatifte yasaklanan bir özneyi pozitif cümlede saymak modele
> istenmeyeni hatırlatır. Ay filminde liste: gölge · robotik araç · mafsallı
> makine · güneşi izleyen panel.
>
> ⚠️ **ÜÇÜNCÜ SEÇENEK VAR VE BU CÜMLEYİ HİÇ YAZMIYOR [A3-e].** Bu cümle iki
> ayrı yere yazıldı (görsel · I2V) ve iki kez düştü (DERS 15 · DERS 18).
> Dış rapor sebebini adlandırıyor — *anlamsal ayrıştırma*: model "timelapse"
> komutunu alınca gökyüzünü hızlandırıyor, insanı ve aracı anatomik gerçek
> zaman bandında üretiyor. Önerilen çözüm promptu düzeltmek değil TERSİNE
> çevirmek: prompta "timelapse" yazma, her şeyin gerçek zamanlı ve yavaş
> aktığı bir klip üret, hızı KURGUDA ver. O zaman bulut, gölge, toz, vinç,
> insan ve araç aynı çarpanla hızlanır — çünkü hızı model değil kurgu verir.
> ⛔ Bu depoda koşulmadı ve bedeli ölçülmedi (6,0 sn'lik klipten ne kadar
> kullanılabilir kare kalıyor, gölge süpürmesi o kısa gerçek zamanda okunur
> hâlde kalıyor mu). Cümle yerinde duruyor; alternatif ARAÇ KAPISINDA
> (§8 adım 0b) test klibiyle birlikte denenir.

**Kamera kilidi — POZİTİF ve ÖLÇÜLEBİLİR hâl [DERS 6 · DERS 11'de DOĞRULANDI]:**

```
The framing is identical in the first frame and in the last frame: the named
background anchor occupies exactly the same width of the frame at both ends of
the shot, and the horizon stays at exactly half the frame height throughout.
The camera is bolted down and does not move, drift, breathe or reframe.
```

> ⛔ Yalnız `no zoom, no pan, no tilt` yazmak YETMEDİ (v1 · ① CAMERA LOCK
> 4/10: bütün klip boyunca yavaş bir push-in). Yasak modele ne YAPACAĞINI
> söylemez; ölçülebilir bir çapa söyler.

**Vinç bulunan her filmde ayrıca:**

```
The tower crane is one continuous rigid steel lattice mast standing on a
concrete base at ground level, with an unbroken load path from the hook to the
mast to the ground — the mast never floats, never bends, never changes height
within a shot, and the jib stays perfectly straight. The hook block hangs
vertically under the trolley on a single taut cable and never swings faster than
a slow pendulum, and it always carries a visible load.
```

> ⛔ **KANCA YAZIYLA TUTMUYOR [DERS 8].** v1'de yük yolu cümlesi altı promptun
> altısındaydı ve 0:21'de kanca halattan koptu, havada asılı kaldı
> (① C1 0/10 · ② LOAD PATH 0/10). Kanca küçük + ince + hareketli:
> modelin en zayıf olduğu üçlü. Risk yazıyla değil KALDIRILARAK çözülür —
> her sahnede ikisinden biri plana yazılır:
> ```
> (a) KANCA YÜKLÜ VE DÜŞEY   kancada görünür bir yük var, halat düşey.
>                            BOŞ KANCA hiçbir promptta yazılmaz.
> (b) KANCA KADRAJ DIŞI      bom kadrajın üst kenarının üstünde kalır,
>                            yalnız mast görünür.
> ```
> Vinç TİPİ (renk + baş tipi: flat-top / saddle jib) değişmezler bloğuna
> yazılır — v1'de 0:40'ta vinç tip değiştirdi.

> ⛔ **NEGATİF ÇEKİRDEĞİN HER MADDESİ SAHA KARTINA KARŞI OKUNUR [DERS 16].**
> Doğru bir kural yanlış sahaya taşınırsa yanlış olur. Ölçülmüş vaka:
> çekirdek `no star trails` diyordu — o madde ŞEHİR kartından geliyordu
> (şehirde yıldız görünmez ve model onu abartır). Dağ vadisinde gece uzun
> pozlamada yıldız **iz bırakır**; izsiz yıldız timelapse'i yalanlar ve
> ① C4 ile ③ C1 birlikte 0/10 aldı.
> ```
> şehir gecesi     → "no star trails, no light streaks in the sky"
> dağ/çöl gecesi   → "stars render as concentric arcs about 30 degrees long,
>                     centred on the pole star, consistent with a two-hour
>                     exposure"
> ```
> ⭐ **"SHORT" BİR SAYI DEĞİLDİR [A4-c].** Dünya saatte 15° döner: 1 saat
> pozlama 15°, 2 saat 30°, 6 saat 90° (çeyrek daire) yay verir. 24 mm tam
> karede yıldız ancak ~21 saniyeye kadar nokta kalır. İz istiyorsan kaç
> derece istediğini yaz — DERECE ve POZLAMA SAATİ birlikte
> (ZAMAN_VE_ISIK §5). Sayısız bir iz tarifi, DERS 19'un gökyüzü hâlidir.
>
> Film yazılırken çekirdek madde madde okunur; saha kartıyla çelişen madde
> o filmde TERSİNE çevrilir ve gerekçesi plana yazılır.

> ⛔ **METİN YASAĞININ KAPSAMI, YASAĞIN KENDİSİ KADAR ÖNEMLİDİR.**
> `film_md` Ders 138: yasak cümlesi kısaltılırken öznesi daralıyor.
> *"The crane carries no logo"* vinci korur; tabelayı, yeleği, konteyneri
> ve çiti korumaz. Şantiye, bu depodaki en yoğun metin yüzeyidir —
> yasak YÜZEY YÜZEY sayılır, tek nesneye bağlanmaz.
>
> ⭐ **F10 ÜÇ AYRI DURUMDUR [C1-g]:** ⓐ modelin UYDURDUĞU yazı (tabela, yelek,
> gökte harf) — negatif + yüzey yüzey yasak buna bakar · ⓑ KAYNAK GÖRSELDEKİ iz
> (usta karede kalmış bir logo, zincirle her kareye taşınır) — kaynak temizlenir,
> prompt değil · ⓒ HİZMETİN FİLİGRANI (köşe damgası) — araç kapısı ④ ve
> CAPRAZ_YAYIN filigran yasağı. Üçü ayrı teşhis edilir; görüntüden hareketle
> "eğitim verisi sızıntısı" diye adlandırılmaz — o bir kaynak iddiasıdır, gözlem değil.

---

# 8. 🏭 ÜRETİM AKIŞI — ⭐ TERS İNŞA

> Bu akışın 2. ve 3. adımı bu deponun en yüksek kaldıraçlı kararıdır.
> Altı kareyi ayrı ayrı üretirsen altı farklı bina ve altı farklı arka plan
> alırsın; geriye inerken saha, arka plan, çerçeve ve tasarım zaten kilitlidir.

```
0. KONSEPT KAPISI   §6 — VAAT/DİRENÇ/BEDEL + üç test. Geçmezse plan yok.

0b. ⛔ ARAÇ KAPISI — PLANDAN ÖNCE, TEK TEST KLİBİ [DERS 23]
                    Seçilen I2V aracıyla tek klip üretilir ve İKİ şey ölçülür:
                      ① ffprobe ile SÜRE (ızgara o sayıdan yazılır [D-d])
                      ② KAMERA HAREKET EDİYOR MU?
                    ⛔ Ediyorsa o araçla BU FORMAT ÜRETİLMEZ. Prompt
                       düzeltilmez — ARAÇ değiştirilir.
                    ⭐ Ölçüldü: aynı ölçülebilir çapa cümlesi bir araçta
                       ① CAMERA LOCK 10/10, başka araçta 0/10 aldı. Hareket
                       promptun değil, modelin ön ayarıdır.
                    ⭐ ÜÇÜNCÜ SORU EKLENDİ [A3-d]: "bu araçta kamerayı
                       GEOMETRİK olarak kilitleyecek bir kanal var mı?"
                       Kilit prompt katmanında değil geometri katmanında
                       yaşıyor: kamera poz matrisi (sıfır vektörü), statik
                       mod parametresi ya da ilk/son kare kilidi. Kanal
                       yoksa kilit yalnız modelin iyi niyetine bağlıdır ve
                       DERS 23 tam olarak o niyetin ölçümüdür.
                    ⭐ ÜÇÜNCÜ SORU [DERS 32]: test klibinde bir nesnenin
                       GÖLGESİ ilk ve son karede aynı açıda mı? Aynıysa o
                       araçla bu format üretilmez — gölge süpürmesi, kamera
                       kilidi gibi aracın özelliğidir (üç film, üç ölçüm).
                    ⛔ SEKİZİNCİ SORU — FORMATIN KENDİSİ [§2.7 ④]: araç İKİ
                       KARE (ilk + son) alıyor mu? Almıyorsa bu format o
                       araçta ÜRETİLMEZ; plan tek kareli I2V'ye düşürülmez,
                       ARAÇ değiştirilir.
                    Geçen aracın adı ve hangi kilit kanalını taşıdığı
                    plana YAZILIR — <FILM>_URETIM_GUNLUGU.md'nin ilk
                    satırı budur [DERS 28].

1. PLAN             §3 Değişmezler + §4 Aşama Merdiveni + §5 güneş saati
                    doldurulur. Sahne haritası bu üç tablodan TÜRER,
                    tersi olmaz.

2. ⭐ USTA KARE      GN ÜRETİLİR — tamamlanmış yapı, ANA istasyondan.
                    ⭐ GN son SAHNE değil, son KLİBİN HEDEF KARESİDİR [§2.7].
                    ⛔ KAPI: bina ikna edici değilse, arka plan çapaları
                       okunmuyorsa ya da kadraj güvenli alana oturmuyorsa
                       DİĞER BEŞ SAHNE ÜRETİLMEZ. Usta kare filmin tapusudur.
                    ⭐ FİNAL HİYERARŞİ [P1-h]: plana yazılmış ÜÇ şey bu
                       sırayla okunuyor mu? Okunmuyorsa kare yeniden —
                       kompozisyonla, nesne ekleyerek değil.
                    ⛔ USTA KARE KLİBİ olay bütçesinden MUAF DEĞİLDİR
                       [P1-g]: loop ışığı bir olaydır, geriye TEK olay kalır.

2b. ⛔ FİNAL ÜRETİLEBİLİRLİK TESTİ — zincirin İLK HALKASI [C1-b · 18.09.2026]
                    Bütün filmi üretip hatayı SON sahnede keşfetmek en pahalı
                    yoldur (BUILT FROM DUST · THE DUST YEAR · CLOSING SPAN:
                    ⑧ YÖNTEM 0,0 — üçü de sonuna kadar üretildi). Adım 3'e
                    geçmeden ÜÇ PARÇA üretilir ve sahip onaylar:
                      (a) REFERANS   GN + üç sabit nirengi px'iyle işaretli
                                     (KAMERA_ISTASYONU §7) — PLAN §DEĞİŞMEZLER'e
                      (b) İLK HALKA  GN → G(N−1) image-to-image; zincir_kontrol.sh
                                     ilk kez BURADA koşulur (önceki = ana = GN)
                      (c) FİNAL      G(N−1) → GN arasında final I2V: vaat edilen
                                     sonuç GÖRÜNÜR (çark döner · su geçer · kapanış
                                     tamamlanır); tutuş kuralı adım 9 [P2-i]
                          + PİLOT    en zor montaj hareketinin klibi (beş soru
                                     kartı dolu — SAHNE_PLAN_KARTI) — hangi sahne
                                     olduğu 04_UYARI_NOTLARI'ndan okunur
                    ⛔ (c) ÜRETİLEMİYORSA KAPSAM DARALIR: sahne çıkar, vaat
                       küçülür; prompt "düzeltilip" tekrar denenmez [DERS 23'ün
                       mantığı — araç değişir, plan zorlanmaz].
                    ⭐ Bu adım §2.7 "iki onaylı kare arası" kuralıyla ÇELİŞMEZ:
                       (b) zincirin ilk halkasıdır, (c) o iki kare arasındadır.
                    KALDIRDIĞI: "önce hepsini üret, sonra bakarız" imkânı.
                       Karşılığı, üçüncü klipte kesilen bir filmin bedelidir.
                    Günlük: URETIM_GUNLUGU §1b PİLOT ÜÇLÜ.

3. ⛔ GERİYE İNŞA — BU BİR ÖNERİ DEĞİL, KAPIDIR [DERS 5]
                    ⭐ ZİNCİR = EDİT [P2-a]: her kare master'ın TARİHSEL
                       SÜRÜMÜDÜR (parça kaldır / ekle), "esinle" yeni
                       üretim değil. Üretim notu kare başına tek satır:
                       "master'dan ne KALDIRILDI / ne EKLENDİ". Ve her
                       I2V iki ONAYLI kare arasında üretilir; somut hedef
                       karesi olmayan I2V yazılmaz.
                    S9'dan image-to-image ile geriye inilir ve HER SAHNE
                    BİR ÖNCEKİNİN KARESİNDEN TÜRETİLİR — sıfırdan değil:
                       S9 → cepheyi kaldır                  → S8
                       S8 → üst katları kaldır              → S7
                       S7 → karı geri koy, katları indir    → S6
                       S6 → 5 kata indir                    → S5
                       S5 → çekirdeğe indir, vinci küçült   → S4
                       S4 → yapıyı kaldır, bodrumu aç       → S3
                       S3 → temeli kaldır, çukuru aç        → S2 · S1
                       S1 → çukuru doldur, arsayı boşalt    → S0
                    ⛔ ZİNCİR KIRILIRSA KALAN SAHNELER ÜRETİLMEZ, zincire
                       dönülür. v1'de bu adım atlandı ve altı kare bağımsız
                       üretildi: ② STRUCTURE IDENTITY 0/10, üç farklı bina.
                       YAPI BIBLE'ın birebir tekrarı TEK BAŞINA YETMEDİ —
                       bu ölçülmüş bir sonuçtur, varsayım değil.
                    Detay istasyonları da zincirin İÇİNDEN üretilir: ana
                    istasyondaki aynı aşamanın karesi referans alınır.

3a. ⚠️ ZİNCİRE KARŞI BİR İDDİA VAR — okunmadan zincir koşulmaz [A3-a]
                    Dış rapor, ardışık image-to-image'in matematiksel olarak
                    hata BİRİKTİRDİĞİNİ söylüyor: her adım bir öncekinin
                    ÇIKTISINI referans aldığı için, denoising gücü 0,15-0,20
                    gibi çok düşük tutulsa bile konturlar ve dokular her
                    kopyada mikroskobik kayar; zincirin sonunda usta kareyle
                    ilk kare arasında topolojik bağ kalmaz.
                    ⛔ BU BİR VARSAYIMDIR VE §8'İ DEVİRMEZ. Ters inşa DERS 5
                       · 12 · 25'ten doğdu ve o üçü bu depoda ÖLÇÜLDÜ.
                       Ölçülmüş bir dersi, koşulmamış bir iddia yenmez.
                    ⚠️ AMA ZAMANLAMASI ÖNEMLİ: ters inşa bu depoda HİÇ
                       KOŞULMADI (AGENTS §6). En yüksek kaldıraçlı adım, aynı
                       zamanda en az sınanmış adım — ve iddia sınamadan ÖNCE
                       geldi. İlk koşuda bu satır hatırlanır: zincir kırılıyorsa
                       sebep uygulama hatası OLMAYABİLİR.

3c. ⭐ ALTERNATİF — "MERKEZİ ÇATI" GEOMETRİ KİLİDİ [A3-b]
                    Zincir (S9→S8→S7…) yerine on sahnenin HEPSİ tek bir
                    merkezden türetilir — aralarında I2I ilişkisi kurulmaz:
                      ① 3D kaba kütle: kat siluetleri, pencere açıklıkları,
                         aks düzeni. Kamera o yazılımın İÇİNDE konumlanır
                         ve kilitlenir (§3'ün dört sayısı oraya girer).
                      ② Aynı kilitli kameradan on aşama renderı (depth/MLSD)
                      ③ Renderlardan I2I KULLANMADAN doğrudan text-to-image;
                         geometri kanalı 0,6-0,8 ağırlık bandında
                      ④ Renk ve ışık için usta kare referans olarak ~0,5
                    ⭐ NEDEN: kümülatif hata yok, çünkü zincir yok. Yapı
                       koordinatları 3D haritada durur, modelin hafızasında
                       değil.
                    ⭐ VE DERS 19'U TAŞIR: 3D kaba kütle, YAPI BIBLE'ın
                       sayılarının geometrik hâlidir — sayıyı prompta yazmak
                       yerine kameranın önüne koyar.
                    ⛔ BEDELİ: hatta bir araç (3D yazılım) ve bir emek adımı
                       girer. Ve bu da koşulmadı — ters inşa gibi varsayım.
                    ⛔ SEÇİM PLANA YAZILIR: hangi yol seçildiyse gerekçesiyle.
                       İki yolu aynı filmde karıştırmak, hangisinin tuttuğunu
                       ölçülemez yapar.

3b. ⛔ ZİNCİR KAPISI — HER KAREDEN SONRA, SONRAKİNE GEÇMEDEN ÖNCE [DERS 12]
                       bash araclar/zincir_kontrol.sh <onceki_onayli> <yeni>
                    Kadrajın KENARLARINI karşılaştırır: istasyon aynıysa
                    kenarlar (çapaların yaşadığı yer) sabit kalır, değişen
                    yalnız MERKEZ olur. Çıkış kodu 2 = ZİNCİR KIRILDI.
                    ⛔ Kırıldıysa o kare ATILIR, önceki onaylı kareye dönülür
                       ve yeniden türetilir. SONRAKİ SAHNELER ÜRETİLMEZ —
                       zincir kırıkken üretilen her kare kaybedilmiş karedir.
                    ⭐ NEDEN ARAÇ: bu kural iki filmde de YAZILIYDI ve iki
                       filmde de atlandı. Yazılı kural kapı değildir;
                       kapı KOŞULAN bir şeydir.

4. PROMPT           ⭐ 2N+1 prompt yazılır: N+1 görsel (G0…GN) + N I2V.
                    ⛔ T2V YAZILMAZ [§2.7 ②] — metinden üretilen klip iki uca
                       kilitlenemez ve dikişi kırar.
                    ⛔ Her I2V'nin İKİ UCU da birebir cümleyle kilitlenir
                       (§2.7 "I2V'nin iki ucu"). Kapı ikisini de arar.
                    ⛔ Her prompt tek başına çalışır — belge atfı yasak.

5. PROMPT KAPISI    python3 araclar/prompt_kontrol.py <dosya>
                    uzunluk · yasak kelime · negatif çekirdek imzası ·
                    "Scene N of 7" tutarlılığı · güneş azimut satırı ·
                    değişmezler bloğunun birebir tekrarı.
                    ⭐ 05.10.2026 §10f (DERS 58-62): dikey 7 × 8,0 · YASAK KELİME satırı ve
                    taraması · sahada olmayan nesneyi adlandıran metin yasağı · havasız
                    sahada yanma kelimesi · inşaat nesnesine 'vanish/disappear' · günlük
                    ve PİLOT ÜÇLÜ (S6 adıyla) → BLOCK · MOTION FOCUS'ta adı geçmeyen yeni
                    eleman → FIX.
                    Çıkış kodu 2 = BLOCK → üretme.

6. VİDEO            ⭐ Her I2V İKİ ONAYLI KARE ARASINDA üretilir: klip n'e
                    Gn ilk kare, G(n+1) son kare olarak verilir. Somut hedef
                    karesi olmayan I2V yazılmaz.
                    ⛔ VE HER KLİPTEN SONRA ÖLÇÜLÜR: klibin son karesi ile
                       hedef görsel arasında zincir_kontrol.sh. Çıkış 2 =
                       araç iki kareli modu taşımıyor → §2.7 ④, araç değişir.
                    Onaylanmamış görselden video üretme, boşa gider.

7. KURGU            N klip · 0 kesme içi · sert kesme aralarda · geçiş efekti YOK.
                    ⛔ KESME ARTIK ZAMAN SIÇRAMASI DEĞİLDİR [§2.7 ①]: dikişin
                       iki yakası aynı karedir, kesmede hiçbir şey atlamaz.
                    ⛔ KIRPMA ASİMETRİKTİR: pay BAŞTAN alınır, sondan alınmaz —
                       son kare hedeftir [KURGU_VE_TESLIM §2].

8. MÜZİK + KAPAK    MUZIK_VE_KAPAK.md — müzik tek parça, BPM ızgaraya oturur;
                    kapak metinsiz + 120 px posta pulu testi.
                    ⛔ DİKEYDE MÜZİK YOK (sahip kuralı 21.09.2026) ve kart yalnız PLAN
                       "var" diyorsa eklenir — ihraçta ölçülür (adım 9d).

9b. ⛔ KAPAK KANITI [DERS 30]  kapak, teslim mp4'ünün S9 karesinden türemiş mi:
                       ffmpeg -ss <kaynak sn> -i teslim.mp4 -frames:v 1 s9_kaynak.jpg
                       bash araclar/zincir_kontrol.sh s9_kaynak.jpg kapak.png
                    Çıkış 2 = kapak başka bir dünya → TESLİM EDİLMEZ.
9c. ⛔ KESME KANITI [DERS 31]  bash araclar/kesme_kontrol.sh teslim.mp4 <plan>
                    Kurgu planın SÜRE sütununa oturmuyorsa yeniden kesilir.
9. ⛔ FİNAL KARE KANITI   ⭐ 05.10.2026 [C2-b]: DİKEY FİNAL KLİBİ = 4 sn OLAY + 4 sn TUTUŞ.
                    2x paylaşımda 8 sn'lik final 4 sn kalır; İŞLEV ANI 1x'in 0-4 sn'sinde
                    biter, 4-8 sn sonucu gösterir (2x'te ekranda 2 sn). Final I2V'si
                    "from about four to eight seconds …" cümlesiyle tutuşu yazar — kapı arar.
                    Örnek: THE DEEP END — ışıklar 1-2,5 · projektör 2,5-4,5 · sonra figür
                    yürür ve oturur, ışık sabit.
                    ⭐ Usta kare klibinin son ≥2,0 sn TUTUŞTUR [P2-i]:
                    yapı ve ışık sabit, yalnız leke akar; kanıt karesi
                    bu tutuşun içinden alınır. Teslimden önce tek komut:
                       ffmpeg -ss <saniye> -i teslim.mp4 -frames:v 1 kanit.jpg
                    SPEC'te yazan "S5 · 0:5X · ekranda GÖRÜLMESİ gereken şey"
                    o karede gerçekten var mı? Yoksa FİLM TESLİM EDİLMEMİŞTİR
                    — klip sayısı ve süre tutsa bile.
                    (film_md D141: kapı klip sayar, vuruş saymaz. Üretilmiş iki
                     dikey filmin ikisinde de kaybolan şey FİNALDİ.)

9d. ⛔ İHRAÇ KANITI [DERS 63]  PAYLAŞILACAK dosyaya (dikey 2x):
                       bash araclar/ihrac_kontrol.sh <film_klasoru> paylas_2x.mp4 --hiz 2
                    Makine: süre (56/hız + kart yalnız planda varsa) · çözünürlük ·
                    final tutuşu 2,0/hız sn (SSIM). Elle ✓: müzik yok · okunur
                    yazı/logo/promo/"AI TIMELAPSE" yok · kart = GN dünyası.
                    Çıkış 2 ya da işaretsiz madde = PAYLAŞILMAZ. QA aynı dosyayla:
                       bash araclar/qa_paket.sh --hiz 2 <film_klasoru> paylas_2x.mp4
10. PAKETLEME       başlık ≤40 karakter · açıklama · hashtag · sabit yorum
                    + ⛔ GERÇEKLİK BEYANI (§9.6)
```

---

# 9. ⚠️ BİLİNEN TUZAKLAR

> Bu bölüm üretim denemelerinden büyüyecek. Bugünkü maddeler `film_md`'nin
> ölçülmüş derslerinin bu türe çevrilmiş hâlidir; koşulduklarında
> `DERSLER.md`'ye numaralı ders olarak inerler.

### 9.1 ⛔ ARKİTEKTÜREL RENDER ÇUKURU — bu türün 1 numaralı estetik hatası
Model "inşaat" görünce parlak bir emlak render'ı üretmeye yatkındır: temiz
zemin, mükemmel cam, boş şantiye, mavi gökyüzü, gölgesiz ışık. Gerçek şantiye
**dağınıktır.**

⛔ **KORPUSU OLMAYAN SAHADA ÇUKUR CGI'DİR [DERS 34].** Korpus cümlesinin
kuralı, testi ve örnekleri 11.09.2026'da `MALZEME_VE_DOKU_KILAVUZU.md` §1'e
TAŞINDI (burada tekrarlanmaz). Yüzey listesi de artık saha başına o kılavuzun
§5 kartından gelir — tek cümle her sahaya kopyalanmaz [A9-g].

### 9.2 ⛔ BİNA DEĞİŞİYOR
En sık ve en öldürücü bozulma. İlacı üç katmanlıdır ve üçü birden gerekir:
(a) YAPI BIBLE birebir tekrarı · (b) ters inşa (§8) · (c) `no redesign,
same column grid, same bay spacing, same footprint` cümlesi.

> ⛔ **VE ÜÇÜ DIŞINDA KALAN İKİ ŞEY BU İŞİ YAPMAZ [A3-c]:**
> **sabit seed** başlangıç gürültüsünü sabitler, ama zincirde referans görsel
> her adımda değiştiği için geometriyi kilitleyemez. **Referans görsel kilidi**
> (usta kareyi referans vermek) stil, renk ve atmosfer taşır — pencere adedi
> ve kat yüksekliği gibi UZAMSAL kısıtları taşımaz.
> ⭐ DERS 19'un araç tarafı: "as described" boş bir işaretçiydi; referans
> görseli de boş bir işaretçidir. Uzamsal kısıt ancak GEOMETRİ kanalından
> (depth · çizgi haritası · 3D kaba kütle) geçer — stil kanalından geçmez.

### 9.3 ⛔ ARKA PLAN KAYIYOR
Yapıya bakarken arkadaki tuğla blok kat kazanır, servi yer değiştirir, sırt
hattı düzleşir. İzleyici bunu bilinçli fark etmez ama "aynı yer" hissi ölür.
Çapalar isimlendirilir ve her promptta aynı kelimelerle yazılır (§3).

### 9.4 🔄 İNSAN VE ARAÇ — yasak değil, BULANIK
`film_md` ikinci insanı yasakladı çünkü model klon üretiyordu. Burada insan
**ölçek referansıdır** ve olmadan yapının büyüklüğü okunmaz. Ama net bir yüz,
tekinsiz vadi riskidir. Çözüm timelapse'in kendi diline zaten yazılı:

```
"Workers appear only as soft motion streaks and blurred figures, none of them
sharp, none of them facing the camera, no readable face anywhere. Vehicles
entering and leaving the site render as smeared light and colour trails."
```
Bu, hem ölçeği verir hem AI-yüz cezasını yapısal olarak kapatır.

### 9.5 ⛔ 10 SANİYEDE ÇOK ŞEY OLUYOR
Bir sahne bir aşamadır. Bir sahnede hem kazı hem karkas hem cephe geçerse
model geometriyi eritir. Sahne içi değişim bütçesi: **bir gün + bir görünür
iş adımı.** Fazlası merdivenin bir sonraki basamağıdır, aynı klibin içi değil.

### 9.6 ⛔ KAPAK KARTI SAHNE SANILIYOR [DERS 4]
Teslim dosyasının son 5 saniyesi karttır ve **başka bir binadır.** Planda
beyan edilmezse mercekler onu son sahne sayar ve film, olmayan bir devamlılık
ihlalinden ceza yer. `TESLİM YAPISI` satırı §2.1'dedir.

### 9.7 ⛔ MEVSİM TEK KLİPTE BAŞLAYIP BİTİYOR [DERS 7]
Kar bir klipte yağıp aynı filmin bir sonraki klibinde yok olursa izleyici iki
kış sayar ve filmin süresini şişik okur. Kış **iki sahnedir**: biri birikme,
biri erime. Erime görünmezse mevsim yayı kırılır.

### 9.8 ⛔ GERÇEKLİK BEYANI — kanal koruması
Bu filmler AI üretimidir ve gerçek bir projeyi belgelemezler.

```
· Gerçek firma adı, logo, proje adı, şehir/parsel iddiası KULLANILMAZ.
· Açıklamada "yapay zekâ ile üretilmiştir" satırı bulunur.
· Gerçek bir yapının birebir kopyası üretilmez; yapı tipi kartından türetilir.
Sebep: bu türün izleyicisi videoyu belgesel sanır. Sanmasına izin vermek,
kanalın ilk şikâyette kaybedeceği şeydir.
```

### 9.9 ⭐ "AI BELLİ OLUYOR" İLE "ZAMAN OKUNMUYOR" AYNI ARIZADIR [A4-f]

AI tespit araçlarının en yüksek başarıyı aldığı iki kanal şu: **(a) ardışık
karelerde gölge geometrisinin tutarlılığı**, **(b) optik akış yörüngesindeki
eğrilik ve ani sarsıntı.**

```
⭐ İKİSİ DE BU DEPONUN ZATEN DÜŞTÜĞÜ YERLER:
   DERS 18 · beş klipte gölge açı değişimi 0° ölçüldü
   DERS 15 · gökyüzü timelapse hızında, yer gerçek zamanda aktı

⛔ VE BU BİR GİZLENME HEDEFİ DEĞİLDİR. İçerik AI olarak beyan ediliyor
   (değişmez ⑥ · ⑫) ve beyan kaldırılmıyor. Maddenin değeri şu:
   ⭐ TESPİT ARACININ BAKTIĞI YER, İZLEYİCİNİN SAHTE BULDUĞU YERDİR.
      Yani bu iki kanal bir arıza listesidir — gölge tutarlılığı ve hız
      birliği düzelirse film hem daha az "AI" görünür hem zamanı okunur.
      Aynı işi iki sebeple yapıyoruz; sebeplerden biri yeterdi.
```

---

# 10. 🔧 BAKIM NOTLARI

```
· Bu dosya ADRES verir + üç tabloyu tutar. Başka hiçbir kılavuzun içeriği
  buraya kopyalanmaz; kopyalanırsa ikisi ayrışır ve hangisinin doğru olduğu
  kaybolur.
· Yeni kural bir DERSTEN doğar, fikirden değil. Ders = ölçülmüş bozulma
  (hangi film, hangi saniye, ne oldu). Ölçüm yoksa "OKUMA" diye işaretlenir.
· Yeni kural eklerken sor: bunu MODEL mi uygular, İNSAN mı? İnsansa prompta
  değil plana yazılır. Belge büyümez, sadeleşir [P1-j].
· film_md'nin 40 kılavuzu bu deponun hedefi DEĞİLDİR. O depo kendi teşhisinde
  hacmin çekirdek arızayı engellemediğini ölçtü. Dosya ancak bir ders
  taşıyorsa açılır.
```
