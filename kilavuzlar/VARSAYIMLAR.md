# 🧪 VARSAYIMLAR — dışarıdan geldi, burada ölçülmedi

> **Varsayım = gerekçeli ama bu depoda ölçülmemiş madde.** Kaynağı başka bir depo (D · F1),
> dış araştırma raporu (A) ya da kendi QA raporlarımızın sentezi (C). Hiçbiri kural değildir;
> her biri ilk üretimden ya da izleyici verisinden sonra ya numaralı derse döner (`DERSLER.md`)
> ya düşer. Düşen madde SİLİNMEZ — düştüğü yazılır.
>
> 08.10.2026'da `DERSLER.md`'den ayrıldı: ölçülmüş ders ile ölçülmemiş varsayım aynı dosyada
> aynı ağırlıkta okunuyordu. Plan okumaları (P kodları) `PLAN_OKUMALARI.md`'de.
> Metin birebir taşındı; yeni olan yalnız bu önsöz ve DİZİN'in **durum** sütunu.
>
> Kodlar değişmedi: `[A5-a]` · `[C2-e]` · `[D-f]` atıfları aynen geçerli.

---

## 📋 DİZİN — 221 kod · ⬜ açık 185 · ✅ ölçüldü 29 · ❌ düştü 7

```
DURUM SÜTUNU — üç değer, dördüncüsü yok
  ⬜ açık      bu depoda ölçülmedi. Kaynağı doğrulanmış olması (platform ✅ · akademik ✅)
               ölçüm DEĞİLDİR; o bilgi "kaynak" sütununda durur.
  ✅ ölçüldü   bu depoda ölçüldü ya da yeniden hesaplandı: bir filmin QA'sında (→ DERS n)
               ya da bu makinede koşarak (ÖLÇTÜM). Hücre kanıtın yerini yazar.
  ❌ düştü     ölçüm ya da denetim iddiayı düşürdü; madde silinmez, düştüğü yazılır.
⛔ Durum yalnız kanıtla değişir: DERS numarası · ÖLÇTÜM satırı · denetim dosyası.
   "Mantıklı görünüyor" ⬜'yi ✅ yapmaz. Sayılar: bash araclar/sayac.sh
```

### D — film_md

| kod | başlık | kaynak | durum |
|---|---|---|---|
| D-a | MODEL BELGEYİ OKUMAZ, PROMPTU ÇİZER | — | ⬜ açık |
| D-b | YASAĞIN KAPSAMI, YASAĞIN KENDİSİ KADAR ÖNEMLİ | — | ⬜ açık |
| D-c | POZİTİF HÂL, YASAKTAN İYİ TUTAR | — | ⬜ açık |
| D-d | IZGARA PLANDAN DEĞİL ARAÇTAN YAZILIR | — | ⬜ açık |
| D-e | KAPI KLİP SAYAR, VURUŞ SAYMAZ | — | ⬜ açık |
| D-f | YASAKLAR BİRBİRİNİ GÖRMEZ VE BİRİKİR | — | ⬜ açık |
| D-g | RİSK DARALTILIR, YASAK GENİŞLETİLİR — arada boşluk kalır | — | ⬜ açık |

### A1–A4 · birinci kuşak

| kod | başlık | kaynak | durum |
|---|---|---|---|
| A1-a | SÜRE BANDI ÇELİŞKİSİ — 65 sn'ye karşı 15-30 sn | pazarlama blogu | ⬜ açık |
| A1-b | KAPAK KARTININ YERİ BEYAN EDİLMİYOR | bizim açığımız | ⬜ açık |
| A1-c | SESSİZLİK DEĞİL, FOLEY YOKLUĞU | pazarlama blogu | ⬜ açık |
| A1-d | AI BEYANI ERİŞİM CEZASI DEĞİL; RİSK BEYANSIZLIKTA | araç dokümanı | ⬜ açık |
| A2-a | ⭐ İZOKRONİK DİZİ, ÖNGÖRÜSEL KODLAMAYA YENİLİR | akademik | ⬜ açık |
| A2-b | MODERN ORTALAMA ÇEKİM UZUNLUĞU 4 SANİYENİN ALTINDA | akademik | ⬜ açık |
| A2-c | DÜŞÜK GÖRSEL HAREKETLİ KADRAJ DAHA HIZLI KESİLİR | akademik | ⬜ açık |
| A2-d | KUSURSUZ LOOP DİKİŞİ TEKRAR İZLEMEYİ ARTIRIYOR | pazarlama blogu | ⬜ açık |
| A2-e | KESME MÜZİĞİN VURUŞUNA MİLİSANİYE HİZALANIR | akademik | ⬜ açık |
| A3-a | ⛔⭐ ARDIŞIK I2I ZİNCİRİ HATA BİRİKTİRİR — matematiksel | akademik | ⬜ açık |
| A3-b | ⭐ ALTERNATİF: "MERKEZİ ÇATI" (hub-and-spoke) geometri kilidi | — | ⬜ açık |
| A3-c | SABİT SEED VE REFERANS GÖRSEL GEOMETRİYİ TAŞIMAZ | araç dokümanı | ⬜ açık |
| A3-d | KAMERA KİLİDİ GEOMETRİK OLARAK ÇÖZÜLÜR, PROMPTLA DEĞİL | — | ⬜ açık |
| A3-e | ⭐ AYNI HIZ SORUNU PROMPTTA DEĞİL, POST'TA ÇÖZÜLÜYOR | araç dokümanı | ⬜ açık |
| A3-f | START-END FRAME ENTERPOLASYONU DİKİŞİ TAMAMEN KALDIRIR | — | ⬜ açık |
| A4-a | ⭐⭐ BETON KÜRLENMESİ — HER SAHADA ÇALIŞAN YENİ TAŞIYICI | akademik | ⬜ açık |
| A4-b | GÖLGE DÖNGÜSÜNÜN PİK SAYISI = YIL SAYISI | akademik | ⬜ açık |
| A4-c | YILDIZ İZİ POZLAMAYLA DERECEYE BAĞLI | akademik | ⬜ açık |
| A4-d | VİNÇ ENGEL LAMBASI DÜZENSİZ ÇAKAR, SÜREKLİ YANMAZ | araç dokümanı | ⬜ açık |
| A4-e | GECE ARAÇ FARI SÜREKLİ IŞIK ŞERİDİ BIRAKIR | akademik | ⬜ açık |
| A4-f | AI TESPİTİNİN BAKTIĞI YER: GÖLGE YÖNÜ + OPTİK AKIŞ | akademik | ⬜ açık |

### A5–A8 · ikinci kuşak

| kod | başlık | kaynak | durum |
|---|---|---|---|
| A5-a | ⭐ ARA HÂL, GEÇİCİ EKİPMANLA TANIMLANIR | mekanizma | ⬜ açık |
| A5-b | ⭐ ÜÇ TARTIŞMASIZ İŞ KANITI | mekanizma | ⬜ açık |
| A5-c | ⭐ ÖLÇTÜM — KADRAJ 33,7 × 60,0 m · 32 px/m | — | ✅ ölçüldü · ÖLÇTÜM |
| A5-d | ÜÇ STANDART ATFI YANLIŞ ÇIKTI | düzeltildi | ⬜ açık |
| A6-a | ⭐⭐ SIKIŞTIRMA REJİMİ — bu kuşağın tek yeni KAVRAMI | — | ⬜ açık |
| A6-b | ⭐ ÖLÇTÜM — GÖLGE DÖNÜŞÜ 116°-191°, "135°" DEĞİL | — | ✅ ölçüldü · ÖLÇTÜM |
| A6-c | ⭐ ÖLÇTÜM — SIKIŞTIRMA ARİTMETİĞİ TUTUYOR | — | ✅ ölçüldü · ÖLÇTÜM |
| A6-d | ⭐ İŞ, İNSANLA DEĞİL YÜZEYLE KANITLANIR | mekanizma | ⬜ açık |
| A6-e | ⛔ RAPOR KENDİ TABLOSUYLA ÇELİŞTİ | çözüldü | ⬜ açık |
| A7-a | ⭐⭐ KLİP SÜRELERİ KUTULUDUR — DERS 31'İN GERÇEK SEBEBİ | — | ✅ ölçüldü · DERS 31 doğrulandı |
| A7-b | ⭐ ÖLÇTÜM — ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn | — | ✅ ölçüldü · ÖLÇTÜM |
| A7-c | ⭐ NEGATİF NEREYE YAZILIR | mekanizma | ⬜ açık |
| A7-d | ⭐ ARAÇ ÖLÇÜMÜ ÜÇ DEĞİL YEDİ SORUDUR | — | ⬜ açık |
| A7-e | ⛔ ENVANTER KULLANILAMAZ | rapor düştü | ❌ düştü · rapor düştü |
| A7-f | ⛔ DERS 2 İLE ÇATIŞTI, DERS 2 KAZANDI | kart S §3 | ❌ düştü · DERS 2 kazandı |
| A8-a | ⭐⭐ ÖLÇTÜM — KESME KAPISI KÖRDÜ, AÇIK SANILIYORDU | — | ✅ ölçüldü · ÖLÇTÜM |
| A8-b | ⭐ ÖLÇTÜM — İKİ KOMUT ÇALIŞMIYOR, DÖRDÜ ÇALIŞIYOR | — | ✅ ölçüldü · ÖLÇTÜM |
| A8-c | ⭐ İKİNCİ BAĞIMSIZ KESME DEDEKTÖRÜ: YDIF | — | ⬜ açık |
| A8-d | DURUŞA KES, HAREKETE DEĞİL | mekanizma | ⬜ açık |
| A8-e | ⛔ İKİ SAYI DÜŞTÜ | kaynaksız | ❌ düştü · kaynaksız |
| A8-f | ⭐ ÇELİŞKİYİ ORTALAMADI | rapor + | ⬜ açık |
| A78-a | ⭐ SÜRE ZİNCİRİ: kutu seti (A7) + kırpma bütçesi (A8) birleşince | — | ⬜ açık |
| A56-a | ⭐ İNSAN ÇELİŞKİSİ: A5 döşemede işçi gösteriyor, A6 aynı klipte insanın | — | ⬜ açık |

### A9–A12 · üçüncü kuşak

| kod | başlık | kaynak | durum |
|---|---|---|---|
| A9-a | ⛔ KORPUS ADI + ALET + IŞIK ÜÇLÜSÜ | VARSAYIM | ⬜ açık |
| A9-b | BETON KÜRLENME TAKVİMİ SAYIYLA | VARSAYIM · standart adı doğru | ⬜ açık |
| A9-c | PAS HIZI İKLİME BAĞLI (ISO 9223 sınıfları) | VARSAYIM · standart adı doğru | ⬜ açık |
| A9-d | ⭐ ÖLÇTÜM — 0,5 m EŞİĞİ NESNE İÇİNDİR, BANT AŞAR | — | ✅ ölçüldü · ÖLÇTÜM |
| A9-e | ÜÇ ZAMAN YAYI × GÖRÜNÜR DEĞİŞİM | VARSAYIM | ⬜ açık |
| A9-f | RÜZGÂRSIZ DÜNYADA TOZ YALNIZ FAALİYETLE BİRİKİR — P1-d'yi doğrular. | — | ⬜ açık |
| A9-g | ⛔ EVRENSEL SITE TEXTURE HAVASIZ SAHADA FİZİK DIŞI | YENİ · kapı | ⬜ açık |
| A10-a | YÜK YOLU ZİNCİRİ · 18 ELEMAN | VARSAYIM · standart adları doğru | ⬜ açık |
| A10-b | ⭐ SÖKÜM BİR FİİLDİR — eleman başına: kılıf sıyrılır · kriko gevşer | — | ⬜ açık |
| A10-c | ⭐ HAMMADDE İSTİF FORMATI — kafes yatay · dikme paletli sepette · profil | — | ⬜ açık |
| A10-d | ÖLÇTÜM — MAKİNE–ZEMİN PİKSEL TABLOSU 15/15 tutuyor (makine ölçüleri | — | ✅ ölçüldü · 15/15 |
| A10-e | ⭐ ROBOTİK GÖVDE SÖZLÜĞÜ | VARSAYIM | ⬜ açık |
| A10-f | ÖLÇTÜM — DÜŞÜK g: Ay'da sarkaç periyodu √6 = 2,45 kat uzun; toz balistik, | — | ✅ ölçüldü · ÖLÇTÜM |
| A10-g | İHLAL SÖZLÜĞÜ · 11 SATIR + POZİTİF ENGEL | İDDİA — benchmark adı var, DOI yok | ✅ ölçüldü → DERS 53 |
| A10-h | ⛔ "6 sn yerine 2 sn × 3 klip" — formatla çelişir, ALINMADI; araç | — | ⬜ açık |
| A10-i | ⛔ "Everything rests on the ground" ASILI YÜKÜ YALANLAR | YENİ · kural | ⬜ açık |
| A11-a | ÖLÇTÜM — REFERANS NESNE DEFTERİ 7/7 tutuyor (1,5 m söve 48 px | — | ✅ ölçüldü · 7/7 |
| A11-b | ⛔ ÖLÇEĞİ DEĞİŞEN NESNE REFERANS OLAMAZ (yapı · vinç · iskele · berm) | VARSAYIM | ⬜ açık |
| A11-c | UFUK %50 TİLT 0° — formül, KAMERA §3'te zaten var. Raporun atfı yanlış | — | ⬜ açık |
| A11-d | "1/3 KURALI UFKU %33/66'YA İTER" | VARSAYIM — atıf ❌ PiT | ⬜ açık |
| A11-e | ⭐ GenScale: T2I modelleri GÖRELİ ÖLÇEĞİ tutturamıyor (1.643 ölçüm) | KAYNAK ✅ | ⬜ açık |
| A11-f | ⭐ NumBench: küçük tam sayı tutar, sayı büyüdükçe çöker (1–100 test) | KAYNAK ✅ | ⬜ açık |
| A11-g | SpatialGenEval: uzamsal komut darboğaz (21 model · 1.230 prompt) | KAYNAK ✅ | ⬜ açık |
| A11-h | T2I-CompBench++ [KAYNAK ✅] — "boyut çapası doğruluğu artırır" özette | — | ⬜ açık |
| A11-i | ⭐ AR HATA BİRİKİMİ (FreqForcing) [KAYNAK ✅] → A3-a'yı doğrular. | — | ⬜ açık |
| A11-j | MLSD > Depth > Canny; IP-Adapter geometri taşımaz | VARSAYIM — MLSD atfı ❌, IP-Adapter atfı ❌ | ⬜ açık |
| A11-k | ⛔ ÖRNEK CÜMLE KESİRLERİ TABLOYLA TUTMUYOR (ÖLÇTÜM) | kural | ✅ ölçüldü · ÖLÇTÜM |
| A11-l | Kamera sayıları prompta yazılmakla kilitlenmez; poz kanalı | VARSAYIM — atıf ❌ CamPilot | ⬜ açık |
| A12-a | ÖLÇTÜM — BULUT × REJİM: cumulus 10 m/s → 100× 6 km · 1200× 72 km | — | ✅ ölçüldü · ÖLÇTÜM |
| A12-b | ⛔ GÖLGE 15°/SAAT DÜŞTÜ — A6-b ÖLÇTÜM ile çelişir (9 saatte 116–191°). | — | ❌ düştü · A6-b ile çelişti |
| A12-c | ÖLÇTÜM — YER TABLOSU: kamyon 100×'te ~1 kare · işçi 100×'te ~5 kare | — | ✅ ölçüldü · ÖLÇTÜM |
| A12-d | ATMOSFERİK PERSPEKTİF 6 hava × 4 mesafe + cümle | İDDİA · kaynak boş | ⬜ açık |
| A12-e | HAVASIZ / İNCE ATMOSFER: Ay siyah gök · keskin gölge · yakın ufuk; | — | ⬜ açık |
| A12-f | YAĞIŞ KLİP İÇİ: ıslanma 1–3 dk · kuruma 30 dk–4 sa · kar 3–5 cm/sa | — | ⬜ açık |
| A12-g | ⭐ GÖLGESİZ SAHNEDE ALTI TAŞIYICI: pus halesi · toz duvarı · ıslak-kuru | — | ⬜ açık |
| A12-h | ANLAMSAL AYRIŞMA MEKANİZMASI | İDDİA · kaynaksız | ⬜ açık |
| A12-i | ⭐ İKİ KARE ARASI PROJEKSİYON | VARSAYIM · DERS 47 ile uyumlu | ⬜ açık |
| A12-j | 100× REJİMDE KAR YAĞIP ERİYEMEZ — DERS 7'yi fizikle doğrular. | — | ⬜ açık |

### A13–A18 · dördüncü kuşak

| kod | başlık | kaynak | durum |
|---|---|---|---|
| A13-a | ⚠️ YİRMİ FORMÜLÜN YİRMİSİ DE TUTTU — VE YİRMİSİ DE UYGULANAMAZ | ÖLÇTÜM | ✅ ölçüldü · tuttu, uygulanamaz |
| A13-b | ⭐ DİJİTAL YAKINLAŞMA SIFIR PARALAKS ÜRETİR | VARSAYIM · fizik | ⬜ açık |
| A13-c | ⭐ YAKINLAŞMA TAVANI = kaynak genişliği / teslim genişliği | ÖLÇTÜM · kapı | ✅ ölçüldü · ÖLÇTÜM |
| A13-d | 180° ENSTANTANE KURALI, BİZİM MOTION STREAK ŞARTIMIZIN OPTİK KARŞILIĞI | — | ⬜ açık |
| A14-a | ⭐ KARAR İLK 0–1 SANİYEDE VERİLİYOR | VARSAYIM | ⬜ açık |
| A14-b | ÇIPA VE KEŞİF DENGESİ (sürenin çoğu sabit ana kamerada) | VARSAYIM | ⬜ açık |
| A14-c | ⭐ KESİNTİSİZ KAMERA HAREKETİ + TIMELAPSE HIZI = DOKU BOZULMASI | VARSAYIM | ⬜ açık |
| A14-d | ⛔ LOOP: BİZDE KADRAJ DÖNGÜSÜ OLUR, DURUM DÖNGÜSÜ OLMAZ | YENİ | ⬜ açık |
| A14-e | ❌ "900×1400 evrensel güvenli alan" DÜŞTÜ | DENETİM | ❌ düştü · denetim |
| A14-f | 9:16'DA YATAY PAN ÖZNEYİ KADRAJDAN ÇIKARIR — dikey eksen tercih edilir. | — | ⬜ açık |
| A15-a | ⛔ CTR BANTLARI · "%25–30 yüz" · "60.000 kat" KILAVUZA İNMEDİ | İDDİA | ⬜ açık |
| A15-b | ⭐ KARŞILAŞTIRMA ARACI KAZANANI İZLEME SÜRESİ PAYINA GÖRE SEÇER | İDDİA · araç dokümanı | ⬜ açık |
| A15-c | ⭐ SAĞ ALT KÖŞEYİ SÜRE ETİKETİ KAPATIR | İDDİA · araç dokümanı | ⬜ açık |
| A16-a | ⭐ SAPMA ÇARPANI YÖNTEMİ: başarı toplam izlenme değil, KANAL ORTALAMASINA | — | ⬜ açık |
| A16-b | ❌ TABLO HATASI: 1.200.000/25.000 = 48x; rapor 48.000x yazıyor. On bir | — | ❌ düştü · tablo hatası |
| A16-c | KÜÇÜK KANAL, BÜYÜK KANALIN KAPAĞINI KOPYALAYAMAZ: tanınmayan yüz/minimalizm | — | ⬜ açık |
| A17-a | YZ KAPAK KUSURLARI (plastik cilt · anatomi · tutarsız ışık kaynağı) — bizim | — | ⬜ açık |
| A17-b | 1280×720 · 2 MB · 16:9 — uzun format kapağının teknik zarfı. Dikeyde | — | ⬜ açık |
| A17-c | ⚠️ KISA DİKEY FORMATTA A/B TESTİ YOK — deneme uzun formata ertelenir. | — | ⬜ açık |
| A18-a | ⛔ ÇELİŞKİ — SABİT KAMERA KUSUR MU, İMZA MI | ÖLÇÜLMEMİŞ | ⬜ açık |
| A18-b | MERKEZ KİLİTLEME: dikeyde ana dönüşüm alanı kadrajın orta şeridinde durur. | — | ⬜ açık |
| A18-c | "ÇEVRE ELEMANLARINI SABİTLEME" — nesne değişirken arka plan ve ışık sabit. | — | ⬜ açık |
| A18-d | TEPEDEN 90° KADRAJ en yüksek ikinci sıklık — bizde YOK ve olmayacak: | — | ⬜ açık |
| A18-e | FİNALDE GERİ ÇEKİLME (pull-out reveal) — bizde finalin karşılığı USTA | — | ⬜ açık |
| A18-f | ❌ YÜZDE TABLOLARI 100 ETMİYOR (%102,5 ve %97,5): bir video çift, bir video | — | ❌ düştü · yüzdeler 100 etmiyor |

### A19 · kamera dili

| kod | başlık | kaynak | durum |
|---|---|---|---|
| A19-a | ⭐ KAYNAKÇA ÇEKİLDİ — 11'İN 10'U İDDİAYA AİT | DOĞRULANDI · bu makinede | ✅ ölçüldü · bu makinede |
| A19-b | ⭐ DEĞİŞİM BOYUTU → BAKIŞ AİLESİ | VARSAYIM · karar çerçevesi | ⬜ açık |
| A19-c | ⭐ TİLTLİ KADRAJ FORMÜLÜ — üç film yaklaşık formül kullanmış | ÖLÇTÜM · türetim | ✅ ölçüldü · türetim |
| A19-d | KATSAYI FORMÜLÜ REJİM TABLOSUNU BAĞIMSIZ ÜRETTİ | ÖLÇTÜM | ✅ ölçüldü · ÖLÇTÜM |
| A19-e | POZLAMA ≈ İNTERVALİN YARISI → İZ | VARSAYIM · optik | ⬜ açık |
| A19-f | TELE SIKIŞTIRMAZ, KONUM SIKIŞTIRIR · ZOOM ≠ DOLLY | VARSAYIM · optik | ⬜ açık |
| A19-g | ⛔ HAREKET REÇETELERİ ALINMADI | ÇELİŞKİ · karar değişmedi | ⬜ açık |
| A19-h | ⚠️ NEGATİFTE "NO" — Veo "öğe adı yaz" diyor, imzalar kalıyor | araç dokümanı ✅ · kısmi çelişki | ⬜ açık |
| A19-i | ⚠️ TERS AÇILIŞ DÖRDÜNCÜ KEZ ÖNERİLDİ — alınmadı | ÇELİŞKİ | ⬜ açık |
| A19-j | "HER HAREKETİN GEREKÇESİ TEK CÜMLE" — katman 2 tablosu bunu zaten ister | VARSAYIM | ⬜ açık |
| A19-k | RAPORUN KAYIT KARTI = BİZİM ON BLOK; SEKİZ PROMPTU KAPIDAN GEÇMEZ | VARSAYIM | ⬜ açık |
| A19-l | 15 BELİRTİNİN 14'Ü BİZDE KARŞILIKLI, 7'Sİ NUMARALI DERS | dış doğrulama | ⬜ açık |
| A19-m | ⚠️ YATAYDAN SHORTS KESİTİ — AÇIK SORU | sahip kararı | ⬜ açık |
| A19-n | TEST MATRİSİ ALTIDAN BİRE İNER | VARSAYIM | ⬜ açık |

### A20–A24 · QA onarımı

| kod | başlık | kaynak | durum |
|---|---|---|---|
| A20-a | ⭐ GEM / PROJE DOSYALARI HER SOHBETE GİRER | araç dokümanı ✅ · çekildi | ⬜ açık |
| A20-b | GERİ OKUMA YALNIZ OKUNABİLENE — dosya adı + belgenin ilk satırı | VARSAYIM · Ç2 | ⬜ açık |
| A20-c | SIZINTI METİNDEN ÖLÇÜLÜR — liste + kanarya terimi | VARSAYIM | ⬜ açık |
| A20-d | FAIL CLOSED — eksik/yanlış/sızdırmış koşunun puanı yok, doldurulmaz | VARSAYIM · klinik eksik veri ilkesi | ⬜ açık |
| A21-a | ⭐ MODEL SAYMAZ — 1 fps örnekleme, 2x'te klip başına ~4 kare | araç dokümanı ✅ + ÖLÇTÜM | ✅ ölçüldü · ÖLÇTÜM |
| A21-b | ÖLÇÜLMÜŞ OLGULAR BLOĞU RUBRİĞİN İÇİNDE | VARSAYIM · hibrit düzen | ⬜ açık |
| A21-c | ⛔ KESME EŞİKLE BULUNMAZ — top-N KALIR | ÖLÇTÜM · bu makinede | ✅ ölçüldü · bu makinede |
| A21-d | DOĞRULAMA KATMANI D1–D5 — dosya dışı damga raporu düşürür | VARSAYIM · tolerans ±0,5 sn | ⬜ açık |
| A21-e | ⚠️ HANGİ DOSYA — süreç mercekleri 1x master, izleyici mercekleri 2x | sahip kararı | ⬜ açık |
| A22-a | FORMAT DEĞİŞKENLERİ BLOĞU — kart · müzik · hız · klip rubrikte varsayılmaz | VARSAYIM | ⬜ açık |
| A22-b | KANITSIZ 10 YOK — 7'nin üstü zaman damgası ister | VARSAYIM · rapor da öyle etiketledi | ⬜ açık |
| A22-c | ORTALAMA KODDA · önce gerekçe sonra puan | akademik ✅ · 2606.09410 · CheckEval | ⬜ açık |
| A22-d | ⭐ KÖTÜ OLAN KAZANIR — "hüküm kazanır" yarıya indi | ÇELİŞKİ Ç3 · karar | ⬜ açık |
| A22-e | ⭐ KUSUR SAHİPLİĞİ — bir kusur tek mercekte puan kırar | VARSAYIM · ayırt edici geçerlilik | ⬜ açık |
| A23-a | TEST-TEKRAR PİLOTU 3 × 4 × 3 · medyan · aralık eşiği | VARSAYIM · eşikler bizim | ⬜ açık |
| A23-b | TOHUMLANMIŞ KUSUR SETİ — 10'un 5'i düzeltildi | ÖLÇTÜM · bu makinede | ✅ ölçüldü · bu makinede |
| A23-c | ÇAPA FİLM — puan > 1,0 oynarsa hakem değişti [VARSAYIM] ⇒ QA_KALIBRASYON §4 | — | ⬜ açık |
| A23-d | DIŞ GEÇERLİLİK: ρ 0,50 için 29–30 film (rapor 28) | ÖLÇTÜM · yeniden hesaplandı | ✅ ölçüldü · yeniden hesaplandı |
| A24-a | ⭐ KANITTAN TÜRET — elle özet uzlaştırmasız durmaz | düzenleyici belge ✅ · FDA Q12 (rapor Q15 dedi) | ⬜ açık |
| A24-b | DURUM MODELİ — ham rapor varsa film en az ÜRETİLDİ [VARSAYIM] ⇒ QA_KAYIT §1 | — | ⬜ açık |
| A24-c | HAM DOKUNULMAZ → ESKİ ARŞİV EŞLEME TABLOSUYLA | ÇELİŞKİ Ç5 · karar | ⬜ açık |
| A24-d | TEK AD ŞEMASI <FILM>_<n>_<MERCEK>_HAM.md · n = MERCEK numarası [karar · Ç6] ⇒ QA_KAYIT §3 | — | ⬜ açık |

### A25–A29 · film yazımından doğan kılavuzlar

| kod | başlık | kaynak | durum |
|---|---|---|---|
| A25-a | ⭐ MERAK ZİNCİRİ — her soru bir klipte açılır, ileride bir klipte cevaplanır | akademik ✅ · Loewenstein 1994 | ⬜ açık |
| A25-b | AÇILIŞ–FİNAL KAFİYESİ — dikeyin DÖNGÜ'sü yatayda döngü değildir | VARSAYIM | ⬜ açık |
| A25-c | SON EKRAN son 5–20 sn · video ≥ 25 sn · kartsız filmde tutuş o süre kadar | platform ✅ · YouTube Help | ⬜ açık |
| A25-d | EĞRİ → SAHNE: S = ⌊t / klip⌋ · 7. ve 28. gün · typical = son 10 benzer video | platform ✅ + aritmetik | ⬜ açık |
| A25-e | ⚠️ Ç1 — THE SLOW TAKEOFF kalkışı 0:40 bir ÖLÇÜM SORUSUDUR | sahip kararı korunur | ⬜ açık |
| A26-a | ⭐ MEKÂN KESİNTİSİ BÖLÜTLEMEZ, EYLEM KESİNTİSİ BÖLÜTLER | akademik ✅ · Magliano & Zacks 2011 · Ç3 | ⬜ açık |
| A26-b | DİKEY EK · YATAY KLİP — "≤ 2 sn ek" ile "iki detay sahnesi" çelişkisi kapandı | karar · Ç2 | ⬜ açık |
| A26-c | KOMPOZİT YALNIZ İKİ KAMERA AYNI YÖNE BAKIYORSA | VARSAYIM · bizim geometri | ⬜ açık |
| A26-d | İÇ MEKÂN DİLİ — pencere ışık lekesi kayar · mobilya akar · yüz okunmaz | VARSAYIM · pratik | ⬜ açık |
| A26-e | ⬜ QA ❶ BEYAN SATIRI — kör merceğe ikinci kamera söylenir mi | sahip kararı · açık | ⬜ açık |
| A27-a | ⭐ YANSIMA x = D·h/(h+y) · kadrajda ufkun 118,5·(h+y)/D altında | ÖLÇTÜM · bu makinede 12/12 | ✅ ölçüldü · 12/12 |
| A27-b | FRESNEL SIYIRMADA GÜÇLENİR · AYNA BEAUFORT 0–1'DE KALIR | akademik ✅ · Cox–Munk · NOAA · Ç4 | ⬜ açık |
| A27-c | BULANIK TAŞKIN SUYU KAHVE-OPAK · ISLAK BETON + DURGUN SU = "HAVUZ" | VARSAYIM · DERS 54 ile | ⬜ açık |
| A27-d | SU KOTU DEFTERİ — kot sabit nesneye göre kesirle · tanık çizgi kalıcı | VARSAYIM · TIDE GATE ✅ okundu | ⬜ açık |
| A27-e | SU ÜSTÜNDE TAŞIT ≤ 13 m / 8 sn (G rejimi) — rota HESAPLANIR | ÖLÇTÜM · aritmetik · kano 4–6 km/sa | ✅ ölçüldü · aritmetik |
| A27-f | REJİM DİLİ — A/B'de su "kademeli yükselir", dalgacık YAZILMAZ; G'de titreşir | VARSAYIM · raporun 1/3'ü inmedi | ⬜ açık |
| A28-a | ⭐ ALACAKARANLIK TABLOSU — −0,833°'den dakika · pencere −2…−6° | ÖLÇTÜM · bu makinede 9/9 | ✅ ölçüldü · 9/9 |
| A28-b | ⭐ A VE B REJİMİNDE IŞIK TEK KAREDE YANAR | ÖLÇTÜM · aritmetik · P12-d | ✅ ölçüldü · aritmetik |
| A28-c | OLUMSUZLAMA ÇAĞIRIR — "no flare" yazılmaz, pozitif tarif edilir | akademik ⚠️ · NegT2IBench 2610.03084 | ⬜ açık |
| A28-d | IŞIK DEFTERİ — armatür · takıldığı klip · sönük kareler · grup · sıra · K · yansıma | VARSAYIM · P11-d | ⬜ açık |
| A28-e | ÖNCE IŞIKLI USTA KARE — ışıksız kareler ondan geriye türetilir | VARSAYIM · DERS 5 ile | ⬜ açık |
| A29-a | ⭐ ZİNCİRDE BÖLGE DÜZELTME YOK — video inpainting / v2v dikiş karesini bozar | VARSAYIM · format gereği | ⬜ açık |
| A29-b | KLİBİ BÖL — araya yeni bir kare (Gn½) koymak iki zincirli klip üretir | VARSAYIM · pratik | ⬜ açık |
| A29-c | DURMA KURALI 3 / 6 — aynı eylem 3 kez · toplam 6 deneme → sahneyi yeniden tasarla | VARSAYIM · eşik bizim | ⬜ açık |
| A29-d | ⭐ KARE DEĞİŞİRSE İKİ KLİP · İKİ DİKİŞ SINANIR | aritmetik · zincir gereği | ⬜ açık |
| A29-e | BEŞ KÖK NEDEN → TEK EYLEM — ARAÇ · PROMPT · KARE · KURGU · PLAN | VARSAYIM · arşiv örnekleri | ⬜ açık |

### A30–A34 · viral 2026

| kod | başlık | kaynak | durum |
|---|---|---|---|
| A30-a | ⛔ DIŞ HAVUZ İKİ GRUBU AYIRMIYOR, YAPIŞTIRIYOR | ÖLÇTÜM · tablodan yeniden sayım | ✅ ölçüldü · yeniden sayım |
| A30-b | ⚠️ A18-a AÇIK KALDI — üçüncü rapor da ölçümsüz | karar · Ç3 | ⬜ açık |
| A30-c | DOĞRULANAN VAKALAR — iki yapay zekâ timelapse'i YATAY şehir evrimi (2,44 M · 20 K); dört ger… | — | ⬜ açık |
| A31-a | ⭐ GÖRÜNTÜLEME = ERİŞİM · ENGAGED VIEWS = FİLM | platform ✅ · Ç8 | ⬜ açık |
| A31-b | "KAYDIRMADI %" = "How many chose to view" (Studio → Analiz → İçerik → Shorts) | platform ✅ · eşik ❌ | ⬜ açık |
| A31-c | ⭐ SHORTS'TA A/B TESTİ YOK — "A/B testing is not available for Shorts" | platform ✅ · A17-c doğrulandı | ⬜ açık |
| A31-d | ORİJİNAL > YENİDEN PAYLAŞIM — filigran, başka yerde yayımlanmış ya da HIZI değiştirilmiş içe… | — | ⬜ açık |
| A31-e | INSTAGRAM SİNYALLERİ — watch time · likes · sends (erişim başına); bağlantısız erişimde gönd… | — | ⬜ açık |
| A31-f | ARAÇ ŞARTLARI — Shorts → ilgili video ve uzun form A/B: advanced features · Trial Reels: pro… | — | ⬜ açık |
| A32-a | ⭐ YOUTUBE 2026 METNİ FORMAT KARTINI TARİF EDİYOR | platform ✅ · 1311392 · spam 2801973 | ⬜ açık |
| A32-b | YAPAY ZEKÂ ETİKETİ OTOMATİK VE DEĞİŞTİRİLEMEZ — C2PA'lı dosyada YouTube kendisi koyar ("can… | — | ⬜ açık |
| A32-c | İTİRAZ VİDEOSU — 21 gün (ön uyarıda 7) · < 5 dk · liste dışı · yeni yükleme · ilk 30 sn kana… | — | ⬜ açık |
| A32-d | ETİKETİN BEDELİ İZLEYİCİDE — "AI-generated" etiketi duygusal içerikte etkileşimi düşürür, ge… | — | ⬜ açık |
| A32-e | INSTAGRAM 31.08.2026 ERİŞİM SINIRI YALNIZ YAPAY ZEKÂ KİŞİSİ OLAN PROFİLLER | platform ✅ · Ç2 | ⬜ açık |
| A33-a | ⚠️ HUŞU → PAYLAŞIM ZAYIFLADI | akademik ✅ — yön zayıf | ⬜ açık |
| A33-b | ⛔ YORUM TUZAĞI YOK — kasıtlı hata · "find the mistake" · "send this to…" · "tag a friend" | — | ⬜ açık |
| A33-c | ASMR ETKİSİ YALNIZ DUYARLI İZLEYİCİDE — Poerio 2018: kalp −3,41 vuruş/dk (d = 0,39), yalnız… | — | ⬜ açık |
| A33-d | YORUM TÜRÜ SAYIMI — beş tür (övgü · şüphe · teknik düzeltme · mizah · soru), 7. gün, ilk 50… | — | ⬜ açık |
| A34-a | ⭐ YPP 01.02.2027 — yeni başvuran: 1.000 abone + 8.000 saat / 365 gün ya da 20 M Shorts / 90… | — | ⬜ açık |
| A34-b | KADANS — ayda 4–7 yükleme medyan görüntüleme büyümesi %1,32/ay, 12+ %2,18/ay (vidIQ, 10,2 M… | — | ⬜ açık |
| A34-c | SİLME YOK — "very, very good reason … keep your videos public or unlist them" (Beaupré 23.03… | — | ⬜ açık |
| A34-d | İKİ FORMAT, İKİ ÖNERİ SİSTEMİ — "separate recommendation systems … understand cross-format v… | — | ⬜ açık |
| A34-e | KARAR PENCERESİ — dikey 7. gün · yatay 7 + 28 · kanal içi son 5 medyanı · tek değişken | — | ⬜ açık |

### F1 — kardeş depo

| kod | başlık | kaynak | durum |
|---|---|---|---|
| F1-a | ⭐ MARSTA İZ SİLİNİR, AYDA İZ BİRİKİR | VARSAYIM | ⬜ açık |
| F1-b | ÖRTÜ 1,5–2,5 m REGOLİT = GÜNEŞ PATLAMASI SIĞINAĞI MERTEBESİ | VARSAYIM | ⬜ açık |
| F1-c | BASINÇ KABI KÖŞELİ OLAMAZ — iç basınç köşede yırtar. Küre ideal, fırlatma | — | ⬜ açık |
| F1-d | ⛔ AY BLOĞU MARS'A YAPIŞTIRILMAZ | VARSAYIM · kapı | ⬜ açık |
| F1-e | ⛔ "fabric · cloth · blanket" PROMPT GÖVDESİNE GİRMEZ | VARSAYIM | ⬜ açık |

### C1 — çapraz analiz

| kod | başlık | kaynak | durum |
|---|---|---|---|
| C1-a | ⭐ BEŞ SORU KARTI — malzeme nerede · taşıyıcı · nereye oturur · ne değişti | — | ⬜ açık |
| C1-b | ⭐ FİNAL ÜRETİLEBİLİRLİK TESTİ — zincirin ilk halkası: referans + ilk I2I | — | ⬜ açık |
| C1-c | ⭐ MOTION FOCUS — I2V'de tek ana iş, kendi paragrafında, "from … onto …" | — | ⬜ açık |
| C1-d | ⭐ İŞE BAĞLI HAREKET — hareket sayısı değil ana işe hizmet; yükü tutan vinç | — | ⬜ açık |
| C1-e | ⭐ EŞİT SÜRE TEK BAŞINA KÖTÜ RİTİM DEĞİLDİR — ritmi klip başına FARKLI | — | ⬜ açık |
| C1-f | ⭐ ORANSAL KAYMA EŞİĞİ + 3 NİRENGİ + ANA REFERANS — eşik = genişlik × oran; | — | ⬜ açık |
| C1-g | ⭐ SAHNEYE ÖZGÜ DIŞLAMA — evrensel negatif blok tek başına engellemez; | — | ⬜ açık |
| C1-h | ⭐ ÜÇ NOKTA KONTROLÜ — açılış (sorun + başlamış eylem) · kapak (yalnız | — | ⬜ açık |

### C2 — içerik okuması

| kod | başlık | kaynak | durum |
|---|---|---|---|
| C2-a | ⭐ FİNALDE BİR ŞEY ÇALIŞIR — en güçlü ayırıcı. ④ 9+ altı filmin altısı işlev anıyla biter | — | ⬜ açık |
| C2-b | FİNAL 4 + 4 — 2x paylaşımda 8 sn'lik final 4 sn kalır; olay 0-4, tutuş 4-8 (ekranda 2 sn). | — | ⬜ açık |
| C2-c | KANCA = TANIDIK NESNE + ONA NE OLUYOR. Kanca 9-10: çim sökülür · taşkın tehdidi · terk edilm… | — | ⬜ açık |
| C2-d | DÖNGÜ en zayıf alt puan; kıran üç şey: ödül kadrajdan çıkar (BACK TO WATER 3) · son kare baş… | — | ⬜ açık |
| C2-e | KONU: var olanı dönüştürmek/onarmak (④ ≈7,8) > durağan finalli sıfırdan inşa (≈6,2). Uzay ya… | — | ⬜ açık |
| C2-f | ⑥ RİTİM İLGİYİ AÇIKLAMIYOR: BROKEN CLIMB ⑥ 9,9 / ④ 5,1 · DEEP END METRONOM / ④ 9,9. Filmi ta… | — | ⬜ açık |
| C2-g | ⭐ İŞ YOĞUNLUĞU — artan şey tek işin etrafındaki EL, klip başına iş SAYISI değil (sahip isteğ… | — | ⬜ açık |
| C2-h | ⭐ AÇILIŞ DÜZENİ — S0 2x'te ekranda 4 sn; dört vuruş: ① NESNE (tanıdık, ≥1/3 kadraj, "yanlış" | — | ⬜ açık |
| C2-i | ⭐ S0 GERİ ÇEKİLME AÇILIŞI — sahip önerisi (05.10.2026): açılış nesnesinin ayrıntısında yakın | — | ⬜ açık |

---

## 🧬 DEVRALINAN DERSLER — `film_md`'de ölçüldü, burada VARSAYIM

> ⛔ Aşağıdakiler bu depoda **ölçülmedi.** Başka bir depoda, başka bir türde
> ölçüldüler ve buraya çeviri olarak taşındılar. İlk üretimden sonra her biri
> ya numaralı bir derse dönüşür ya da düşer. Bugün elde bulgu değil,
> **gerekçeli varsayım** var — ve bunu böyle yazmak, ölçüm gibi yazmaktan
> iyidir.

```
D-a  MODEL BELGEYİ OKUMAZ, PROMPTU ÇİZER
     film_md D45: köşeli parantez atfı ("[CHARACTER BIBLE]") model tarafından
     ekrana ETİKET olarak çizilebiliyor. → Burada: DEĞİŞMEZLER bloğu her
     promptta birebir tekrarlanır, atıf verilmez.

D-b  YASAĞIN KAPSAMI, YASAĞIN KENDİSİ KADAR ÖNEMLİ
     film_md D138: "no digits" kalıbı kostümü koruyor, ZEMİNİ korumuyordu;
     model kaldırım çatlağına ölçü yazdı ve altı QA merceğinin altısı da
     görmedi. → Burada: metin yasağı YÜZEY YÜZEY sayılır (tabela, yelek, kask,
     vinç, konteyner, kamyon, iskele, cephe).

D-c  POZİTİF HÂL, YASAKTAN İYİ TUTAR
     film_md D59 + D139: "no backpack" modele ne KOYACAĞINI söylemez; boş bir
     yüzeyi doldurmak zorundadır. → Burada: "no clean site" yerine
     "mud, ruts, puddles, stacked material, tarpaulins, clutter" yazılır.

D-d  IZGARA PLANDAN DEĞİL ARAÇTAN YAZILIR
     film_md D124: klip süresi bir tercih değil aracın ayarı. Ölçülmeden
     yazılan 48 sn ızgarası üç filmde de kaydı. → Burada: ffprobe ile ölç,
     sonra müzik ızgarasını kur.

D-e  KAPI KLİP SAYAR, VURUŞ SAYMAZ
     film_md D141: kurgu kapısının üç satırı da geçti ve film FİNALİNİ teslim
     etmedi. Üretilmiş iki dikey filmin ikisinde de kaybolan şey finaldi.
     → Burada: FİNAL KARE KANITI her SPEC'te zorunlu (KILAVUZ_REHBERI §8/9).

D-f  YASAKLAR BİRBİRİNİ GÖRMEZ VE BİRİKİR
     film_md 05_DIKEY_HAT_TESHISI (30.08.2026): dört ayrı üretim önlemi
     (klon · sessizlik · isimsizlik · kesme yasağı) tek tek doğruydu; dördü
     üst üste gelince hikâyenin çalıştığı bütün malzemeyi kaldırdı ve kimsenin
     seçmediği bir tür BİRİKTİ. → Burada: her yeni yasak eklenirken "bu
     yasağın kaldırdığı ANLATIM nedir" satırı yazılır. Yazılmayan yasak
     kabul edilmez.

D-g  RİSK DARALTILIR, YASAK GENİŞLETİLİR — arada boşluk kalır
     film_md §3.1: "model kaza eseri klon çizmesin" → "filmde ikinci insan
     olamaz"a dönüştü. Kaza ≠ kadro. → Burada: insan yasaklanmadı, BULANIK
     yazıldı (KILAVUZ_REHBERI §9.4). Ölçek korunur, tekinsiz vadi kapanır.
```

---

## 🔬 ARAŞTIRMADAN DEVRALINAN — dış raporda okundu, burada VARSAYIM

> ⛔ **Hiçbiri bu depoda ölçülmedi.** Kaynak: `arastirma/SONUCLAR/A1..A4_GEMINI_HAM.md`
> (Gemini Deep Research · 03.09.2026 · dört promptun kısa sürümü). İlk üretimden
> sonra her biri ya numaralı bir derse dönüşür ya düşer.
>
> ⚠️ **ETİKET UYARISI — bu, raporun kendi etiketine güvenmediğimiz ilk vaka.**
> Rapor her bulguya ÖLÇÜLDÜ / İDDİA / VARSAYIM yazdı, ama **A1'in ÖLÇÜLDÜ
> etiketlerinin çoğu SEO içerik çiftliğine dayanıyor** (autofaceless.ai ·
> retensis.com · klap.app · dynamoi.com · socialync.io · posteverywhere.ai ·
> virvid.ai · frameos.studio). Bir sayının yanında ÖLÇÜLDÜ yazması, o sayının
> ölçüldüğü anlamına gelmez — **kaynağı ölçer.** Aşağıda kaynak sınıfı
> `[akademik]` · `[araç dokümanı]` · `[pazarlama blogu]` olarak ayrıca yazılıdır
> ve yalnız ilk ikisi kılavuza tek satır indi.
>
> ⭐ İki rapor koşulmadı: dördü de tek bota gitti. Kart S §4 gereği çelişki
> görünür değil — bu, aşağıdaki her maddenin ikinci bir zayıflığıdır.

### A1 — VİRAL ANATOMİ  ⚠️ en zayıf kaynak sınıfı

```
A1-a  SÜRE BANDI ÇELİŞKİSİ — 65 sn'ye karşı 15-30 sn        [pazarlama blogu]
      Rapor: en yüksek tutunma 15-30 sn bandında; 60 sn üstünde tamamlanma
      oranı %41'e düşüyor. Bizim format 65 sn.
      ⛔ KILAVUZ DEĞİŞMEDİ. Kaynak sınıfı bir format kararını taşımaz ve
         çelişki tek bota koşuldu. §2.1 yerinde duruyor.
      ⭐ Ama bu, YAYINDAN SONRA ilk ölçülecek şeydir: kanalın kendi tutunma
         eğrisi bu bandı ya doğrular ya düşürür [apexait/YAYIN_PLANI].

A1-b  KAPAK KARTININ YERİ BEYAN EDİLMİYOR                   [bizim açığımız]
      Rapor kartı hem intro hem outro varsayarak iki ayrı felaket senaryosu
      yazdı — çünkü prompt kartın NEREDE olduğunu söylemiyordu.
      ⭐ Bulgu raporda değil, PROMPTUMUZDA: teslim yapısı satırı (§2.1)
         kartın süresini yazıyor, KONUMUNU yazmıyor.
      KİLİT  Teslim yapısı satırı konumu da yazar: kart SON 5 saniyedir.
      KALDIRDIĞI  Hiçbir şey — satır bir kelime uzadı. [D-f]

A1-c  SESSİZLİK DEĞİL, FOLEY YOKLUĞU                        [pazarlama blogu]
      Rapor: bu türde viral olan "sessiz" videoların taşıyıcısı arka plan
      müziği değil ASMR/foley (tuğla, mala, kesme, ortam).
      ⭐ MUZIK_VE_KAPAK §1.3 zaten "diegetik ses yatağı müziğin altında
         sürer" diyor — yani kural VAR, ağırlığı yok. Varsayım: yatak
         eşlikçi değil TAŞIYICI olabilir.

A1-d  AI BEYANI ERİŞİM CEZASI DEĞİL; RİSK BEYANSIZLIKTA     [araç dokümanı]
      Üç platformda da beyanın kendisi erişim cezası üretmiyor; ceza
      beyansız yakalanmakta (TikTok kademeli yaptırım).
      ⭐ Bu bulgu §9.8 ve apexait/youtube/POLITIKA_VE_RISK §2 ile ÇELİŞMİYOR,
         onları DOĞRULUYOR. Değişmez ⑫ yerinde kalır.
      ⚠️ Karşı taraf akademik: "AI info" etiketi etkileşimi düşürmüyor ama
         algılanan insan eforunu ve içerik güvenini düşürüyor. Yani ceza
         algoritmada değil İZLEYİCİDE — ve bu, ölçülebilir bir şey değil.
```

### A2 — RİTİM VE TUTUNMA  ⭐ en güçlü kaynak sınıfı · DERS 13'Ü DIŞARIDAN DOĞRULUYOR

```
A2-a  ⭐ İZOKRONİK DİZİ, ÖNGÖRÜSEL KODLAMAYA YENİLİR             [akademik]
      Cutting (Cornell · 150 film · 1935-2005): izleyiciyi bağlayan şey
      ortalama çekim kısalığı değil, çekim uzunluklarının 1/f (pembe gürültü)
      varyansı. Eşit aralıklı dizi varyansı sıfırlar; beyin diziyi çözer ve
      habitüasyona girer (vMMN tepkisi tetiklenmez).
      ⭐ BU, DERS 13'ÜN MEKANİZMASIDIR. Depo "hız = kesme varyansı" cümlesini
         bir rapor teşhisinden türetmişti ve ölçmemişti. Artık dışarıdan
         gerekçesi var: 10 sn → 6 sn indirimi hızlandırmadı çünkü
         TAHMİN EDİLEBİLİRLİĞİ bozmadı.
      ⛔ VE DERS 24'Ü DE AÇIKLIYOR: klip İÇİ varyans metronomu kırmadı çünkü
         beyin ritmi OLAY SINIRINDAN (kesme) sayar, klip içeriğinden saymaz.
      NEREYE  KILAVUZ_REHBERI §2.2 (tek satır) — kural değişmiyor, gerekçesi
              güçleniyor.

A2-b  MODERN ORTALAMA ÇEKİM UZUNLUĞU 4 SANİYENİN ALTINDA         [akademik]
      Sesli sinemanın ilk yıllarında ~10 sn olan ASL bugün 4 sn'nin altında.
      ⚠️ Bizim izinli süre bandı: 120 BPM → 4 · 6 · 8 · 10 ve ortancası 6,0.
         Yani bandımız modern ASL'nin ÜSTÜNDE ve ortancası iki katı.
      VARSAYIM  Varyans bandı KISA tarafa kaydırılabilir: aynı ölçü
                disiplininde 160 BPM (4,5 · 6 · 7,5 · 9) daha kısa bir
                ortanca verir ve 120 BPM'in 4,0'ı zaten izinlidir.
      ⛔ IZGARA DEĞİŞMEDİ. §2.2 bandı duruyor; bu madde yalnız "hangi uçtan
         seçilir" sorusuna cevap veriyor.

A2-c  DÜŞÜK GÖRSEL HAREKETLİ KADRAJ DAHA HIZLI KESİLİR           [akademik]
      Görsel aktivite indeksi (VAI) düşük olan sabit kadrajlar, dikkat
      kaybını önlemek için daha kısa kesilmeli. İzleyici karedeki yeni
      bilgiyi ilk 1,5-3 saniyede tüketiyor.
      ⭐ Bizim S0 ve S9'u (1 gün · en az iş adımı) tam bu tanıma giriyor —
         ve ZAMAN_VE_ISIK §7 onlara "zamanı yavaşlatır" diye UZUN süre
         veriyor. Varsayım: yavaşlatma niyeti doğru, süresi ölçüsüz.

A2-d  KUSURSUZ LOOP DİKİŞİ TEKRAR İZLEMEYİ ARTIRIYOR       [pazarlama blogu]
      A/B testi iddiası: replay +%18,7 · etkileşim +%16,1.
      ⭐ LOOP SATIRI ZATEN ZORUNLU (§4 · ikinci zorunlu satır) ve hiç
         ölçülmedi — dört filmin dördünde de loop dikişi denetlenmedi.
      ⚠️ Kaynak zayıf ama kural bizde zaten var; bu madde kuralı değil
         DENETİMİ hatırlatıyor.

A2-e  KESME MÜZİĞİN VURUŞUNA MİLİSANİYE HİZALANIR                [akademik]
      Görsel kesme ile işitsel vuruş aynı milisaniyede olduğunda çoklu
      duyusal kazanç etkisi (gain effect) oluşuyor; izleyici kesmeyi
      görmüyor, hissediyor.
      ⭐ MUZIK_VE_KAPAK §1.1 zaten kesmeleri ölçü başına oturtuyor. Bu madde
         toleransı daraltıyor: "ölçü başında" yetmez, VURUŞUN ÜSTÜNDE.
      NEREYE  MUZIK_VE_KAPAK §1.1 (tek satır)
```

### A3 — ZİNCİR VE TUTARLILIK  ⭐⭐ EN AĞIR BULGU · §8'İN ÇEKİRDEĞİNE DOKUNUYOR

```
A3-a  ⛔⭐ ARDIŞIK I2I ZİNCİRİ HATA BİRİKTİRİR — matematiksel  [akademik]
      Difüzyon tabanlı ardışık I2I (SDEdit / DDIM inversion) her adımda
      latenti yeniden gürültüleyip çözüyor. Hata yayılımı ayrık PF-ODE ile
      modellenmiş: δ(t−1) = A(t)·δ(t) + B(t)·ε(t). Her adım bir öncekinin
      ÇIKTISINI referans aldığı için kuantizasyon hatası birikiyor —
      denoising gücü 0.15-0.20 gibi çok düşük tutulsa bile konturlar,
      pencere çerçeveleri ve dokular her kopyada mikroskobik kayıyor.
      Zincirin sonuna gelindiğinde usta kare ile ilk kare arasında
      topolojik bağ kalmıyor.
      ⛔ BU, DEPONUN EN YÜKSEK KALDIRAÇLI KARARINA KARŞI BİR İDDİADIR.
         §8 adım 3 ("S9'dan geriye image-to-image, her sahne bir öncekinin
         KARESİNDEN") tam olarak bu mekanizmanın tarifi.
      ⭐ VE ZAMANLAMASI ÖNEMLİ: ters inşa bu depoda HİÇ KOŞULMADI
         (AGENTS §6). Yani iddia, sınanmamış adımın sınanmasından ÖNCE geldi.
      ⛔ KILAVUZ HENÜZ DEĞİŞMEDİ ve değişmemeli: bir varsayım, ölçülmüş
         DERS 5 · 12 · 25'i devirmez. Ama §8'e bir UYARI satırı indi.

A3-b  ⭐ ALTERNATİF: "MERKEZİ ÇATI" (hub-and-spoke) geometri kilidi
                                                        [araç dokümanı]
      Zincir (A→B→C→D) yerine, on sahnenin HEPSİ tek bir merkezden türetilir:
        ① 3D kaba kütle (shoebox) — kat siluetleri, pencere açıklıkları,
           aks düzeni. Kamera bu yazılımın İÇİNDE konumlanır ve KİLİTLENİR.
        ② Aynı kilitli kameradan on aşama renderı (depth ya da canny/MLSD)
        ③ Bu renderlardan I2I KULLANMADAN doğrudan text-to-image;
           ControlNet-Union depth/MLSD ağırlığı 0.6-0.8 bandında
           (0.8 üstü doku esnekliğini öldürüyor, 0.6 altı kolon/kiriş
            detayını halüsinasyona bırakıyor)
        ④ Renk ve ışık paleti için usta kare IP-Adapter ile ~0.5 ağırlıkta
      ⭐ NEDEN ÖNEMLİ: kümülatif hata YOK, çünkü zincir yok. Yapı
         koordinatları 3D haritada duruyor, modelin hafızasında değil.
      ⭐ VE DERS 19'U TAŞIYOR: "sayısız bir bible bible değildir" — 3D kaba
         kütle, bible'ın SAYILARININ geometrik hâlidir. Sayıyı prompta
         yazmak yerine kameranın önüne koyuyor.
      ⛔ BEDELİ: hattın dışında bir araç (3D yazılım) ve bir emek adımı
         giriyor. Ve bu depoda hiç koşulmadı — ters inşa gibi o da varsayım.
      NEREYE  KILAVUZ_REHBERI §8 (tek satır · seçenek olarak)

A3-c  SABİT SEED VE REFERANS GÖRSEL GEOMETRİYİ TAŞIMAZ    [araç dokümanı]
      Seed başlangıç gürültüsünü sabitler; I2I döngüsünde referans görsel
      her adımda değiştiği için seed geometriyi kilitleyemiyor.
      IP-Adapter / referans kilidi ise stil, renk ve atmosfer taşıyor —
      pencere adedi ve kat yüksekliği gibi UZAMSAL kısıtları taşımıyor.
      ⭐ DERS 19'un araç tarafı: "as described" boş işaretçiydi; referans
         görseli de boş bir işaretçidir. Uzamsal kısıt ancak GEOMETRİ
         kanalından (depth/MLSD/3D) geçer.

A3-d  KAMERA KİLİDİ GEOMETRİK OLARAK ÇÖZÜLÜR, PROMPTLA DEĞİL
                                                        [araç dokümanı]
      Açık kaynak tarafta CameraCtrl kamerayı Plücker gömüleriyle 3D uzayda
      kodluyor; sabit istasyon için hareket matrisi sıfır vektörüne
      sabitleniyor ve klipler arası uzatılabiliyor. Ticari tarafta Runway
      Gen-3 JSON'unda zoom/horizontal/vertical/roll = 0.0 "static mode"
      açıyor (tek blokta ~10 sn), Kling start-end frame iki kilitli görsel
      arasında istasyonu referans alıyor (tek blokta ~15 sn).
      ⭐ BU, DERS 23'Ü DIŞARIDAN DOĞRULUYOR: aynı çapa cümlesi bir araçta
         ① CAMERA LOCK 10/10, başkasında 0/10 aldı. Sebep artık adlandırılmış
         — hareket promptun değil, modelin ön ayarı; ve kilit prompt
         katmanında değil GEOMETRİ katmanında yaşıyor.
      ⛔ ARAÇ KAPISI (§8 adım 0b) yerinde kalır ve GÜÇLENİR: test klibinde
         sorulacak soru "hareket ediyor mu" ile birlikte artık şu da olur —
         "bu araçta kamerayı geometrik olarak kilitleyecek bir kanal var mı?"

A3-e  ⭐ AYNI HIZ SORUNU PROMPTTA DEĞİL, POST'TA ÇÖZÜLÜYOR [araç dokümanı]
      Model "timelapse" komutunu alınca gökyüzünü hızlandırıp insanı/aracı
      anatomik gerçek zaman bandında üretiyor (anlamsal ayrıştırma —
      semantic decoupling). Rapordaki fiziksel çözüm promptu düzeltmek
      DEĞİL, promptu TERSİNE çevirmek:
        · prompta "timelapse" YAZILMAZ
        · her şeyin gerçek zamanlı ve YAVAŞ aktığı bir klip üretilir
        · klip kurguda %5000-%10000 hızlandırılır
      Böylece bulut, gölge, toz, vinç, insan ve araç aynı çarpanla hızlanır —
      çünkü hızı model değil kurgu veriyor.
      ⭐ BU, DERS 15 VE DERS 18'İN ÜÇÜNCÜ DENEMESİDİR. İki ders de aynı
         cümleyi iki farklı yere yazdı (görsel · I2V) ve ikisi de düştü.
         Üçüncü seçenek cümleyi hiç yazmamak.
      ⚠️ BEDELİ ÖLÇÜLMEDİ: %5000 hızlandırma 6,0 saniyelik bir klipten ne
         kadar kullanılabilir kare bırakıyor, ve zaman AKIŞI (gölge süpürmesi)
         o kadar kısa gerçek zamanda okunur hâlde kalıyor mu — bilinmiyor.
      NEREYE  KILAVUZ_REHBERI §7 (zaman hızı bloğuna uyarı) ·
              PROMPT_SABLONU §2

A3-f  START-END FRAME ENTERPOLASYONU DİKİŞİ TAMAMEN KALDIRIR
                                                        [araç dokümanı]
      İki kilitli görsel (boş arsa · usta kare) tek video latentinin içinde
      birleştirilirse arada kesme yoktur; yapı değişimi, kamera respawn'ı
      ve dikiş kusuru kökten kalkıyor.
      ⛔ AMA BU BİZİM FORMATIMIZI YIKAR: kesme = zaman sıçraması bu türün
         tanımı (KILAVUZ_REHBERI §1.2). Dikişi kaldırmak, filmi tek bir
         morph'a çevirir ve on aşamalı merdiveni siler.
      ⭐ Kullanılabilir hâli: SAHNE İÇİ. Bir sahnenin ilk ve son karesi
         zincirden geliyorsa, aradaki 6,0 saniye enterpolasyonla üretilebilir
         ve o sahnenin içi dikişsiz olur. Sahneler ARASI kesme korunur.
```

### A4 — GERÇEKLİK İMZASI  ⭐ nesne düzeyi taşıyıcı listesi · DERS 14'ÜN BOŞLUĞUNU DOLDURUYOR

```
A4-a  ⭐⭐ BETON KÜRLENMESİ — HER SAHADA ÇALIŞAN YENİ TAŞIYICI  [akademik]
      Taze dökülen beton, hidrasyon ve nem kaybıyla günler boyunca
      koyu ıslak griden mat açık kemik rengine açılıyor (hiperspektral
      ölçüm: 600-750 nm görünür bandında yansıma artışı).
      ⭐ BU DEPONUN HİÇ KULLANMADIĞI BİR TAŞIYICIDIR ve iki şeyi birden
         çözer:
           ① ARDIŞIK DÖKÜMLER ARASINDAKİ KONTRAST bir SAAT'tir: alt katlar
              açık ve kürlenmiş, üst kat taze ve koyu. Aradaki fark, o iki
              dökümün arasından kaç ay geçtiğini EKRANDA gösteriyor.
           ② ÇÖLDE VE KAYA VADİSİNDE ÇALIŞIR. ZAMAN_VE_ISIK §6 çölde
              "mevsim görünmez, zaman yalnız gölge ve yapı ile anlatılır"
              diyor — beton kürlenmesi tam olarak "yapı ile anlatmanın"
              nesne düzeyindeki hâlidir.
      ⭐ VE DERS 14'ÜN ÖLÇÜLMÜŞ ARIZASINA DOĞRUDAN CEVAP: iki sahnede
         mevsim "Indeterminate — bare rock and concrete with no foliage,
         weather, or sun-height carriers" okunmuştu. O karelerde BETON
         VARDI ve taşıyıcı sayılmıyordu.
      KİLİT (İngilizce · pozitif · ölçülebilir):
         "The lower floors are pale bone-grey fully cured concrete, while
          the slab poured most recently is still dark, wet and blotchy —
          the colour boundary between them sits exactly at the [n]th floor
          slab edge."
      KALDIRDIĞI  Hiçbir şey. Beton zaten kadrajda; artık bir saat taşıyor.
      NEREYE  ZAMAN_VE_ISIK §6 · SAHA_VE_IKLIM (kart başına) · PROMPT_SABLONU

A4-b  GÖLGE DÖNGÜSÜNÜN PİK SAYISI = YIL SAYISI                  [akademik]
      Gölge boyu L = h / tan(α); yaz gündönümünde en kısa, kış gündönümünde
      en uzun. 34 aylık bir film, gölge boyunun uzama-kısalma döngüsünde
      ÜÇ maksimum ve ÜÇ minimum pikine ulaşmak zorunda.
      ⭐ ③ merceğinin "34 ay yerine yaklaşık bir yıl" okumasının (DERS 14)
         mekanizması bu: izleyici bir tam güneş döngüsü görüyor ve bir yıl
         sayıyor. Zaman yayı kaç yılsa, gölge o kadar kez uzayıp kısalır.
      VARSAYIM  Aşama merdiveninin GÜNEŞ satırı bugün yalnız azimut ve
                yükseklik yazıyor. Yıl sayısı ≥2 olan filmlerde gölge
                BOYUNUN da sahne sahne yazılması gerekebilir.
      NEREYE  ZAMAN_VE_ISIK §2 (tek satır)

A4-c  YILDIZ İZİ POZLAMAYLA DERECEYE BAĞLI                      [akademik]
      Dünya saatte 15° dönüyor. 24 mm tam karede yıldız ~21 saniyeye kadar
      NOKTA kalıyor (500 kuralı: 500/24 ≈ 20,8). Üstünde iz başlıyor:
        1 saat → 15°   ·   2 saat → 30°   ·   3,5 saat → 52,5°   ·
        6 saat → 90° (çeyrek daire)
      Kutba yakın izler iç içe daire, göksel ekvatorda düz çizgi.
      ⭐ DERS 16 "dağ/çöl gecesi → stars render as short concentric trails"
         diyordu — "short" bir sayı değil. Artık sayı var.
      KİLİT (İngilizce · pozitif):
         "The stars render as concentric arcs about [n] degrees long,
          centred on the pole star, consistent with a [n]-hour exposure."
      NEREYE  ZAMAN_VE_ISIK §5 · KILAVUZ_REHBERI §7 (gece satırı)

A4-d  VİNÇ ENGEL LAMBASI DÜZENSİZ ÇAKAR, SÜREKLİ YANMAZ    [araç dokümanı]
      ICAO/FAA gereği kule vinci tepe lambası dakikada 20-40 kez çakan bir
      flaşördür. Uzun dönem timelapse aralığı 10-15 dakikada bir karedir;
      yani deklanşörün açık olduğu milisaniyede lambanın yanık olması
      RASTLANTISALDIR.
      ⭐ Doğru görünüm: ardışık karelerde düzensiz yanıp sönen, bazen
         tamamen karanlık kalan bir nokta. Sürekli yanan bir neon iz
         timelapse'i yalanlar.
      KALDIRDIĞI  Gece kadrajındaki "sürekli kırmızı tepe ışığı" — bu türün
                  kolay atmosfer kazancıydı. Karşılığı: gece sahnesinin
                  fiziği doğru okunuyor.

A4-e  GECE ARAÇ FARI SÜREKLİ IŞIK ŞERİDİ BIRAKIR                [akademik]
      Uzun pozlamada (10-20 sn) şantiyede hareket eden araçların farları
      kesintisiz beyaz (ön) ve kırmızı (arka) ışık hatları çiziyor. AI
      üretiminde bunlar donmuş kısa fırça darbelerine ya da iz bırakmayan
      parlak noktalara dönüşüyor — hareket bulanıklığı fiziğinin
      okunamaması.
      ⭐ KILAVUZ_REHBERI §9.4 zaten "vehicles render as smeared light and
         colour trails" diyor. Bu madde onu GECEYE bağlıyor ve renk verir.

A4-f  AI TESPİTİNİN BAKTIĞI YER: GÖLGE YÖNÜ + OPTİK AKIŞ        [akademik]
      Tespit araçlarının en yüksek başarıyı aldığı iki kanal: (a) ardışık
      karelerde gölge geometrisinin tutarlılığı, (b) optik akış
      yörüngesindeki eğrilik ve ani sarsıntı.
      ⭐ İKİSİ DE BİZİM ZATEN DÜŞTÜĞÜMÜZ YERLER: DERS 18'de beş klipte
         gölge açı değişimi 0° ölçüldü; DERS 15'te gökyüzü ile yer farklı
         hızlarda aktı. Yani "AI belli oluyor" ile "zaman okunmuyor" aynı
         arızanın iki adı.
      ⚠️ VE BİZİM İÇİN BU BİR KAÇINMA HEDEFİ DEĞİL: içerik AI olarak
         beyan ediliyor (değişmez ⑥ · ⑫). Bu maddenin değeri gizlenmek
         değil, ARIZA LİSTESİ olması — tespit araçlarının baktığı yer,
         izleyicinin sahte bulduğu yerdir.
```

---

## 🔬 İKİNCİ KUŞAK ARAŞTIRMA — A5–A8 · 08.09.2026

> Kaynak: `arastirma/SONUCLAR/A5..A8_GEMINI_HAM.md` · Denetim ve doğrulama:
> `arastirma/SONUCLAR/A5-A8_DENETIM.md`
>
> ⭐ **BU KUŞAKTA BİR ŞEY DEĞİŞTİ:** A1–A4'te raporun etiketine güvenmedik ama
> sayısını da denetleyemedik. Bu kuşakta **dört raporun sayıları bu depoda
> yeniden hesaplandı ve ffmpeg ile koşturuldu.** Üç sayı düştü, iki komut
> çalışmadı, bir eşik kör çıktı. Aşağıdaki maddelerden **ÖLÇTÜM** yazanlar
> artık varsayım değil — bu makinede ölçüldü. Diğerleri VARSAYIM olarak kalır.
>
> ⚠️ Dördü de yine TEK BOTA koşuldu [kart S §4] ve hiçbirinde çözümlenebilir
> kaynak (URL · DOI · belge adı) yok. Bu, her maddenin ikinci zayıflığıdır.

### A5 — İNŞA YÖNTEMİ  ⭐ ⑧ APPEARED'in panzehiri

```
A5-a  ⭐ ARA HÂL, GEÇİCİ EKİPMANLA TANIMLANIR                    [mekanizma]
      Bir elemanın "yapılıyor" olduğunun tek görsel kanıtı, o elemanın
      NİHAİ hâlinde bulunmayan geçici bir nesnedir: kalıp · donatı kafesi ·
      iskele · dikme · tırmanır kalıp · kür örtüsü · gergin sapan.
      ⇒ kilavuzlar/INSAAT_YONTEMI_KILAVUZU.md §2-§3
      KAPI: prompt_kontrol.py — AT THIS STAGE'de geçici ekipman yoksa FIX.

A5-b  ⭐ ÜÇ TARTIŞMASIZ İŞ KANITI                                [mekanizma]
      gergin sapan · toz bulutu · ıslak beton parlaklığı. Üçü de fizikle
      bağlı, 40 m'de okunur ve POZİTİF yazılabilir.

A5-c  ⭐ ÖLÇTÜM — KADRAJ 33,7 × 60,0 m · 32 px/m
      24 mm eşd. · 40 m · 9:16. Rapor "10-15 kat" dedi; hesap YİRMİ kat verdi.
      Okunabilirlik eşiği ≈ 0,5 m: insan 58 px (GÖRÜNÜR), kalıp panosu 19 px,
      donatı 3 px (görünmez).
      ⛔ RAPORUN İMASI DÜŞTÜ: insan 40 metrede görünür. İnsanı yok eden
         mesafe değil, zaman sıkıştırmasıdır [A6-a].
      KAPI: prompt_kontrol.py — 0,5 m altı nesne adı geçerse FIX.

A5-d  ÜÇ STANDART ATFI YANLIŞ ÇIKTI                             [düzeltildi]
      ASTM A325/A490 2015'te F3125 altında birleşti · EN 13830 montaj sırası
      şart koşmaz · ASTM D698 laboratuvar deneyidir, saha tabaka kalınlığını
      yazmaz. Görsel sonuç etkilenmiyor.
      ⇒ KILAVUZ KURALI: prompta STANDART ADI YAZILMAZ, görünen şey yazılır.
```

### A6 — ŞANTİYE HAREKETİ  ⭐ ⑦ PARKED'in panzehiri · ⚠️ kendi içinde çelişti

```
A6-a  ⭐⭐ SIKIŞTIRMA REJİMİ — bu kuşağın tek yeni KAVRAMI
      Bir klipte gök · gölge · insan · makine · toz AYNI SAATE tabidir.
      Rejim seçilmezse model her birine ayrı hız verir — DERS 15'in kaynağı budur.
      REJİM A (10 dk · 100x) · B (2 saat · 1200x) · C (iş günü · 5400x)
      ⇒ kilavuzlar/SANTIYE_HAREKETI_KILAVUZU.md §1-§2
      KAPI: prompt_kontrol.py — TIME RATE'te rejim penceresi yoksa FIX;
            rejim C + görünür insan cümlesi varsa BLOCK.

A6-b  ⭐ ÖLÇTÜM — GÖLGE DÖNÜŞÜ 116°-191°, "135°" DEĞİL
      Rapor "güneş saatte 15° gider → 9 saatte 135°" dedi ve ÖLÇÜLDÜ etiketledi.
      15°/saat SAAT AÇISIDIR, azimut değil. 40°N için hesapladım:
          9 saatte  ekinoks 150,2° · yaz 190,7° · kış 115,9°
          öğle civarı hız  ekinoks 23,1°/sa · yaz 46,3°/sa · kış 15,3°/sa
      ⇒ DERS 32'nin sayısal karşılığı buradan gelecekti ve rapor yanlıştı.
      ⇒ Tam tablo: SANTIYE_HAREKETI_KILAVUZU §1.

A6-c  ⭐ ÖLÇTÜM — SIKIŞTIRMA ARİTMETİĞİ TUTUYOR
      60x · 300x · 1440x · 5400x dördü de doğrulandı. 9 saat / 6 sn = 5400x,
      30 fps'de kare başına 180 sn. Raporun doğru olan tek sayı grubu.

A6-d  ⭐ İŞ, İNSANLA DEĞİL YÜZEYLE KANITLANIR                   [mekanizma]
      Sekiz yüzey kanıtı: iz · eksilen istif · kuruyan çamur · hortum
      güzergâhı · sökülmüş kalıp yığını · toz · saha aydınlatması · yüzey
      dönüşümü. Rejim C'de kanıtın TAMAMI buradadır.
      KAPI: prompt_kontrol.py — ACTIVITY'de iki hareket eden + bir yüzey
            kanıtı yoksa FIX.

A6-e  ⛔ RAPOR KENDİ TABLOSUYLA ÇELİŞTİ                          [çözüldü]
      Tablo "5400x'te insan kaybolur" diyor, yedi promptun yedisi "motion
      streak insan" istiyor. Çözüm A6-a'da: rejim klip başına seçilir.
```

### A7 — ARAÇ PROFİLİ  ⭐⭐ tek en değerli bulgu · ⛔ envanteri kullanılamaz

```
A7-a  ⭐⭐ KLİP SÜRELERİ KUTULUDUR — DERS 31'İN GERÇEK SEBEBİ
      Araç serbest süre vermez, kutuya yuvarlar: {4,6,8} · {5,10} · {5,9}.
      On klibin onunun da 6,0 çıkması bundandır — prompt tutmadığı için değil.
      ⭐ ÖLÇTÜM: plan 6·4·6·4·6·6·8·4·6·10, {4,6,8} kutusuyla DOKUZ SAHNEDE
        TAM OTURUYOR (atılacak 0 sn). ⇒ ⑥ METRONOM ARACIN DEĞİL KURGUNUN
        ARIZASIYDI. DERS 31 doğrulandı ve mazereti kalktı.

A7-b  ⭐ ÖLÇTÜM — ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn
      Kırpma bütçesi (uçlardan 10-15 kare) süreyi yer.
      SERT SONUÇ: tek klipte teslim edilebilecek EN UZUN SAHNE =
      (en büyük kutu − 1,00). {4,6,8} → 7,00 sn · {5,9} → 8,00 · {5,10} → 9,00.
      ⇒ {4,6,8} veren araçla plana 8 ya da 10 sn'lik sahne YAZILAMAZ.
      KAPI: prompt_kontrol.py — kutu setinden türeyen tavan aşılırsa BLOCK.

A7-c  ⭐ NEGATİF NEREYE YAZILIR                                  [mekanizma]
      "no" görsel karşılığı olmayan bir sözdizimi öğesidir; yanındaki isim
      yüksek ağırlıklı vektöre döner. Ayrı negatif alan vektörü ÇIKARIR,
      metin içi negatif EKLER. ⇒ DERS 33'ün dışarıdan doğrulanması.
      ⛔ Raporun "%85 sızma" sayısı kaynaksız — mekanizma indi, sayı inmedi.

A7-d  ⭐ ARAÇ ÖLÇÜMÜ ÜÇ DEĞİL YEDİ SORUDUR
      süre/kutu · kamera kayması · gölge dönüşü · negatif sızması · prompt
      tavanı · ilk kare sadakati · en büyük kutu.
      ⇒ kilavuzlar/ARAC_KARTLARI.md §4-§5.

A7-e  ⛔ ENVANTER KULLANILAMAZ                                   [rapor düştü]
      Sorulan 11 aracın dördü (Gen-4 · Seedance · Hailuo · Pika) her sütunda
      BİLİNMİYOR; Gen-4 soruldu, Gen-3 anlatıldı; üç sürüm tarihi çürük.
      ⇒ ARAC_KARTLARI.md doldurulmuş kart İÇERMEZ; boş açılır, üretim günü
        ölçülerek doldurulur.

A7-f  ⛔ DERS 2 İLE ÇATIŞTI, DERS 2 KAZANDI                      [kart S §3]
      Rapor "2.000 karakter altı daha iyi" dedi (kaynaksız); DERS 2 bu depoda
      "4.500-5.500 karakter" diye ölçüldü. KILAVUZ DEĞİŞMEDİ.
      Araç kartına "prompt tavanı" ölçüm satırı eklendi.
```

### A8 — KURGU VE TESLİM  ⭐ en disiplinli rapor · ⛔ iki komudu çalışmıyor

```
A8-a  ⭐⭐ ÖLÇTÜM — KESME KAPISI KÖRDÜ, AÇIK SANILIYORDU
      Sabit kadraj + aynı yapı + yalnız aşama ilerleyen 10 klipli sentetik
      teslimde ölçtüm:
          eşik 0,40 (A8'in önerdiği)       → 0 kesme
          eşik 0,30 (kesme_kontrol.sh'nin) → 0 kesme
          gerçek kesme skorları  0,01629 – 0,02217
          klip içi en yüksek     0,00538
      ⇒ Eşik 15-25 kat fazlaydı. ⑥ METRONOM kapısı hiç çalışmamıştı.
      ⭐ ÇÖZÜM: eşik kaldırıldı, TOP-N geldi. Plandaki kesme sayısı kadar en
        yüksek skor seçilir. Sentetikte 9/9 tam isabet; THE LONG DAY vakası
        (plan varyanslı, kurgu düz) yeniden kurulduğunda 9 kesmenin 8'ini
        yakaladı ve çıkış 1 verdi.
      ⇒ araclar/kesme_kontrol.sh yeniden yazıldı.

A8-b  ⭐ ÖLÇTÜM — İKİ KOMUT ÇALIŞMIYOR, DÖRDÜ ÇALIŞIYOR
      ⛔ signalstats komutu raporundaki hâliyle hiçbir şey basmıyor
         (eşleşen satır 0). Doğrusu: signalstats,metadata=print:key=...YDIF
      ⚠️ ebur128'in "I:" satırı Summary bloğundadır; `tail` ile kaçar.
      ✅ ffprobe süre · ffprobe fps · ebur128 · son kare dışa aktarımı koştu.

A8-c  ⭐ İKİNCİ BAĞIMSIZ KESME DEDEKTÖRÜ: YDIF
      Kesmelerde 1,66-2,26 · klip içi en yüksek 0,54. scene_score ile aynı
      kesmeleri bulmuyorsa kurgu incelenir.

A8-d  DURUŞA KES, HAREKETE DEĞİL                                 [mekanizma]
      Bizim formatta her kesme bir AY atlar; kesilen hareket öbür tarafta
      yoktur. Kesme, mikro hareketin en sakin olduğu ana düşer.

A8-e  ⛔ İKİ SAYI DÜŞTÜ                                          [kaynaksız]
      "%18,7 tekrar izlenme artışı" ve "son kart 2-3 sn ideal, 5 sn öldürür"
      — ikisi de ÖLÇÜLDÜ etiketli, ikisi de kaynaksız.
      ⇒ Kapak kartı 5,0 sn YERİNDE KALDI. Yayından sonra kanalın kendi
        tutunma eğrisiyle ölçülür [A1-a ile aynı muamele].

A8-f  ⭐ ÇELİŞKİYİ ORTALAMADI                                    [rapor +]
      LUFS · gamma · dosya boyutu satırlarında iki değeri yan yana bırakıp
      "BİLİNMİYOR" yazdı. Kart S §4'ün istediği tam olarak budur.
      ⇒ −14 LUFS kararımız yerinde; çelişki artık KAYITLI.
```

### ⭐ DÖRT RAPORUN BİRLEŞMESİNDEN ÇIKAN — hiçbirinde tek başına yok

```
A78-a ⭐ SÜRE ZİNCİRİ: kutu seti (A7) + kırpma bütçesi (A8) birleşince
      üretim süresi, sahne tavanı ve plan ızgarası tek bir aritmetiğe oturuyor.
      Ne A7 ne A8 bunu tek başına söylüyor.

A56-a ⭐ İNSAN ÇELİŞKİSİ: A5 döşemede işçi gösteriyor, A6 aynı klipte insanın
      kaybolduğunu söylüyor. İkisi de doğru — FARKLI REJİMLERDE. Ortalama
      alınmadı; rejim beyanı kuralı bu çelişkiden doğdu.
```

---

## 🔬 ÜÇÜNCÜ KUŞAK ARAŞTIRMA — A9–A12 · 11.09.2026

> Kaynak: `arastirma/SONUCLAR/A9..A12_GEMINI_HAM.md` · Denetim: `A9-A12_DENETIM.md`
>
> ⭐ **BU KUŞAKTA İKİ ŞEY DEĞİŞTİ:** (1) v2 promptları ÇÖZÜMLENEBİLİR KAYNAK şart
> koştu ve raporlar DOI/standart adı getirdi; 12 kaynak çekildi — 7 tuttu,
> 4 başka makaleye çıktı, 1 erişilemedi. Yeni arıza sınıfı: kaynak VAR ama
> iddiaya AİT DEĞİL. (2) Sayılar yine bu depoda yeniden hesaplandı: kadraj ve
> piksel tabloları TUTTU; A12'nin gölge satırı A6-b ile çelişti ve DÜŞTÜ.
> Aşağıda **KAYNAK ✅** yazanlar çekilip doğrulandı; **ÖLÇTÜM** yazanlar bu
> makinede hesaplandı; diğerleri VARSAYIM/İDDİA'dır ve öyle iner.
>
> ⚠️ Dördü de yine TEK BOTA koşuldu [kart S §4].

### A9 — MALZEME VE DOKU  ⭐ SITE TEXTURE bloğunun sözlüğü

```
A9-a  ⛔ KORPUS ADI + ALET + IŞIK ÜÇLÜSÜ                          [VARSAYIM]
      Rapor her malzemeye bir "külliyat + kamera/lens/ışık" yazdı. Külliyat
      adlarının çoğu UYDURMA tanımdır ("Concrete Pouring Field Archive");
      DERS 34'ün testi (adı arama motoruna yaz) bunlara da uygulanır ve düşer.
      Ayakta kalan kısım: korpus cümlesi ALETİYLE anılır (Mastcam-Z · Kodak
      KAI-2020 CCD gerçek). ⇒ MALZEME §1
A9-b  BETON KÜRLENME TAKVİMİ SAYIYLA                              [VARSAYIM · standart adı doğru]
      0–1 gün koyu ıslak (CIE Y %15–20) · 1–3 gün alacalı · 3–7 gün Y %35–45 ·
      7–28 gün kemik grisi Y %60–70, L* ~75, kür kimyasalı tebeşir izi.
      ⭐ "3 gün fark ekranda okunur" — A4-a'nın sayısal hâli. ⇒ MALZEME §4
A9-c  PAS HIZI İKLİME BAĞLI (ISO 9223 sınıfları)                   [VARSAYIM · standart adı doğru]
      C1–C2 şehir: aylar · C5–CX kıyı/endüstri: 80–200 µm/yıl · kumlanmış çelikte
      flash rust saatler. ⇒ MALZEME §4
A9-d  ⭐ ÖLÇTÜM — 0,5 m EŞİĞİ NESNE İÇİNDİR, BANT AŞAR
      0,2 m genişlikte pas akıntısı 6 px'tir ama 1–3 m uzunlukta ÇİZGİ olarak
      okunur; yağ damlası 2–5 px → okunmaz. ⇒ SITE TEXTURE bant ve alan yazar,
      nesne saymaz. ⇒ MALZEME §2 · kapı
A9-e  ÜÇ ZAMAN YAYI × GÖRÜNÜR DEĞİŞİM                              [VARSAYIM]
      1–3 yıl: döküm yaş farkı · pas sınıfı geçişi · toprak→asfalt · cam tozu.
      Aylar: kürlenme tonu · asfalt soğuması · iz derinliği · kür örtüsü.
      TEK GÜN: ıslak parlaklık 6 saatte matlaşır · asfalt buharı · yeni iz ·
      birikinti küçülür. Kürlenme rengi tek günde OKUNMAZ. ⇒ MALZEME §4
A9-f  RÜZGÂRSIZ DÜNYADA TOZ YALNIZ FAALİYETLE BİRİKİR — P1-d'yi doğrular.
A9-g  ⛔ EVRENSEL SITE TEXTURE HAVASIZ SAHADA FİZİK DIŞI            [YENİ · kapı]
      "mud · standing puddles" Ay/Mars'ta yazılamaz. ⇒ prompt_kontrol.py §10d
```

### A10 — FİZİK VE AĞIRLIK  ⭐ PHYSICS bloğunun sözlüğü

```
A10-a YÜK YOLU ZİNCİRİ · 18 ELEMAN                                 [VARSAYIM · standart adları doğru]
      eleman → temas → destek → zemin; BS 5975 · EN 12812 · EN 12811 · EN 1090-2.
      Bölüm numaraları çekilmedi. ⇒ FIZIK §1
A10-b ⭐ SÖKÜM BİR FİİLDİR — eleman başına: kılıf sıyrılır · kriko gevşer ·
      panel devrilir · masa kalıp dışarı sürülür · sapan gevşer · gergi toplanır.
      P2-h'nin sözlüğü. ⇒ FIZIK §2
A10-c ⭐ HAMMADDE İSTİF FORMATI — kafes yatay · dikme paletli sepette · profil
      takozda · boru uç uca · kablo makarada · modül sandıkta. DERS 48'in
      sözlüğü. ⇒ FIZIK §2
A10-d ÖLÇTÜM — MAKİNE–ZEMİN PİKSEL TABLOSU 15/15 tutuyor (makine ölçüleri
      ekipman belgesinden, belge çekilmedi). CAT 320 palet 25 px · LTM kriko
      230 px · IPEx palet 6 px. ⇒ FIZIK §3
A10-e ⭐ ROBOTİK GÖVDE SÖZLÜĞÜ                                      [VARSAYIM]
      excavator → autonomous bucket-drum regolith extractor rover ·
      loader → uncrewed bulk regolith transport rover platform ·
      crane → robotic gantry manipulator strut · dozer → autonomous site
      leveling implement, exposed sensor array. Gövde: MLI battaniye · LIDAR
      sensör direği · güneş paneli/RTG. DERS 41'in İngilizce hâli. ⇒ FIZIK §3
A10-f ÖLÇTÜM — DÜŞÜK g: Ay'da sarkaç periyodu √6 = 2,45 kat uzun; toz balistik,
      bulut yok; counter-rotating tambur (NASA IPEx). ⇒ FIZIK §3
A10-g İHLAL SÖZLÜĞÜ · 11 SATIR + POZİTİF ENGEL                      [İDDİA — benchmark adı var, DOI yok]
      floating · clipping · pass-through · warping · split-merge · identity
      drift · count · opacity fade · unsupported cantilever · gövdesiz kanca ·
      dönmeyen palet. "Etkili/zayıf" dereceleri KAYNAKSIZ. ⇒ FIZIK §4
A10-h ⛔ "6 sn yerine 2 sn × 3 klip" — formatla çelişir, ALINMADI; araç
      kapısına ölçüm sorusu (4 sn vs 8 sn klipte ⑫ farkı).
A10-i ⛔ "Everything rests on the ground" ASILI YÜKÜ YALANLAR        [YENİ · kural]
      Her sahnede ASILI olan (kanca · sapan · vantuz) ayrı yazılır; genel
      cümle yasak değil, EKSİKTİR. ⇒ FIZIK §5 · kapı
```

### A11 — PERSPEKTİF VE ÖLÇEK  ⭐ COMPOSITION bloğunun sözlüğü

```
A11-a ÖLÇTÜM — REFERANS NESNE DEFTERİ 7/7 tutuyor (1,5 m söve 48 px ·
      5 m fener kaidesi 160 px · 15 m mesa 480 px · 10 m krater 320 px).
      Nesne SEÇİMİ varsayım. ⇒ PERSPEKTIF §1
A11-b ⛔ ÖLÇEĞİ DEĞİŞEN NESNE REFERANS OLAMAZ (yapı · vinç · iskele · berm)  [VARSAYIM]
      Kule vinç DOI'si 403. ⇒ PERSPEKTIF §1
A11-c UFUK %50 TİLT 0° — formül, KAMERA §3'te zaten var. Raporun atfı yanlış
      (2211.12432 kalibrasyon makalesi); geometri kaynak istemez.
A11-d "1/3 KURALI UFKU %33/66'YA İTER"                              [VARSAYIM — atıf ❌ PiT]
A11-e ⭐ GenScale: T2I modelleri GÖRELİ ÖLÇEĞİ tutturamıyor (1.643 ölçüm) [KAYNAK ✅]
      ⇒ ölçek yalnız cümleyle kilitlenmez; referans nesne + kanal. PERSPEKTIF §1 · §5
A11-f ⭐ NumBench: küçük tam sayı tutar, sayı büyüdükçe çöker (1–100 test) [KAYNAK ✅]
      DERS 19 + P2-b'yi dışarıdan doğrular. "10 üstü" eşiği raporun okuması. ⇒ §3
A11-g SpatialGenEval: uzamsal komut darboğaz (21 model · 1.230 prompt) [KAYNAK ✅]
      "%90 sağ/sol karıştırıyor" özette yok → İDDİA. Piksel/yüzde konumu
      metinle tutmaz; GLIGEN (kutu koordinatı) istisna [araç]. ⇒ §2
A11-h T2I-CompBench++ [KAYNAK ✅] — "boyut çapası doğruluğu artırır" özette
      yok → İDDİA. ⇒ §4
A11-i ⭐ AR HATA BİRİKİMİ (FreqForcing) [KAYNAK ✅] → A3-a'yı doğrular.
      Attention sink (Rolling Forcing) [KAYNAK ✅]: ilk kareye kilit → A3-b
      hub mantığıyla aynı yön. ⇒ §5
A11-j MLSD > Depth > Canny; IP-Adapter geometri taşımaz           [VARSAYIM — MLSD atfı ❌, IP-Adapter atfı ❌]
      A3-c ile aynı yönde. Depth Anything V2 MAE 0,454 m ORMAN benchmark'ında.
A11-k ⛔ ÖRNEK CÜMLE KESİRLERİ TABLOYLA TUTMUYOR (ÖLÇTÜM)          [kural]
      1,5 m = 48 px = 1/22, "one tenth" değil. Kesir usta karede ölçülen
      pikselden hesaplanır. ⇒ §4 · kapı
A11-l Kamera sayıları prompta yazılmakla kilitlenmez; poz kanalı  [VARSAYIM — atıf ❌ CamPilot]
      DERS 23 + A3-d ile aynı.
```

### A12 — HAVA VE ATMOSFER  ⭐ gök cümlesinin sözlüğü

```
A12-a ÖLÇTÜM — BULUT × REJİM: cumulus 10 m/s → 100× 6 km · 1200× 72 km ·
      5400× 324 km. Raporun "kadraj geçişi %" yüzdeleri irtifayı mesafe
      saydığı için 2–5 kat şişkin; NİTEL sonuç ayakta: şerit · akış · silinme.
      Bulut hızları VARSAYIM. ⇒ HAVA §1
A12-b ⛔ GÖLGE 15°/SAAT DÜŞTÜ — A6-b ÖLÇTÜM ile çelişir (9 saatte 116–191°).
      Raporun 2 numaralı örnek cümlesindeki "thirty degrees" de düştü.
      SANTIYE_HAREKETI §1 geçerli. ⇒ HAVA §1 uyarı satırı
A12-c ÖLÇTÜM — YER TABLOSU: kamyon 100×'te ~1 kare · işçi 100×'te ~5 kare
      saydam silüet · 1200×+ ikisi de silinir. Optik yorum VARSAYIM. ⇒ HAVA §1
A12-d ATMOSFERİK PERSPEKTİF 6 hava × 4 mesafe + cümle                 [İDDİA · kaynak boş]
      ⇒ HAVA §2
A12-e HAVASIZ / İNCE ATMOSFER: Ay siyah gök · keskin gölge · yakın ufuk;
      Mars butterscotch gök + mavi gün batımı (tau); buz gezegeni whiteout  [İDDİA/VARSAYIM]
      ⇒ HAVA §5
A12-f YAĞIŞ KLİP İÇİ: ıslanma 1–3 dk · kuruma 30 dk–4 sa · kar 3–5 cm/sa
      (ÖLÇTÜM: 9 saatte 27–45 cm · 5 cm = 1,6 px) · bayrak Nyquist'te silinir  [VARSAYIM]
      ⇒ HAVA §3
A12-g ⭐ GÖLGESİZ SAHNEDE ALTI TAŞIYICI: pus halesi · toz duvarı · ıslak-kuru
      sınırı · projektör gölgesi · beton kürlenme · yıldız izi (2 sa = 30°, ÖLÇTÜM)
      DERS 40'ın çıkış kapısı. ⇒ HAVA §4
A12-h ANLAMSAL AYRIŞMA MEKANİZMASI                                   [İDDİA · kaynaksız]
      FVD kare keskinliğini zamansal gerçekliğe yeğler; hareket öncülleri insan
      hızında. Çözüm 1 = gerçek zamanlı üret, kurguda hızlandır (A3-e ile aynı).
      Çözüm 2'nin cümlesi imzayı bozar, ALINMADI (denetim §3.5).
A12-i ⭐ İKİ KARE ARASI PROJEKSİYON                                 [VARSAYIM · DERS 47 ile uyumlu]
      G(n) ve G(n+1)'de gölge açısı rejime göre FARKLI çizilir; bulut konumu
      rüzgârın projeksiyonu; 1200×'te ilk karedeki bulut son karede kadrajdan
      çıkmıştır. Aynı açıyla çizilmiş iki kare, "gölge oynamadı"nın sebebidir.
      ⇒ HAVA §6 · PROMPT_SABLONU §1 LIGHTING satırı
A12-j 100× REJİMDE KAR YAĞIP ERİYEMEZ — DERS 7'yi fizikle doğrular.
```

---

## 🔬 DÖRDÜNCÜ KUŞAK ARAŞTIRMA — A13–A18 · 17.09.2026

> Kaynak: `arastirma/SONUCLAR/A13…A18_BEYANSIZ_HAM.md` (altı rapor, tek yapıştırma)
> Denetim: `arastirma/SONUCLAR/A13-A18_DENETIM.md`
>
> ⛔ **BU KUŞAĞIN İKİ YENİ ZAYIFLIĞI VAR ve her maddeden önce okunur:**
> (1) **PROMPT YOK** — raporlar bu depoda yazılmış bir A<n> promptuna cevap değil;
> ne SORULDUĞU bilinmiyorsa ne DIŞARIDA BIRAKILDIĞI da bilinmiyor.
> (2) **KAYNAK ÇEKİLEMİYOR** — `[cite: n]` işaretleri var, kaynakça yok. A9–A12'de
> 12 kaynak çekilebilmişti; burada çekilecek bir şey yok.
> ⇒ Bu kuşaktan kılavuza **tek bir sayı indi** (A13-c) ve o da raporun değil,
> bu makinedeki hesabın sayısıdır.
>
> ⭐ Ve bu kuşak, kapanmış bir tartışmayı yeniden açtı: **kurgu yakınlaşması.**
> Karar araştırmadan değil, proje sahibinden geldi (16.09.2026) — araştırma
> yalnız sınırını ve bedelini yazdırdı. ⇒ `KAMERA_HAREKETI_KILAVUZU.md`

### A13 — MOTION-CONTROL VE KAMERA HAREKETİ  ⭐ yeni kılavuzun omurgası

```
A13-a ⚠️ YİRMİ FORMÜLÜN YİRMİSİ DE TUTTU — VE YİRMİSİ DE UYGULANAMAZ  [ÖLÇTÜM]
      T=N×I · N=T×fps · D_kare=D_toplam/N · T_simetrik=(2N_yarı+N_bekleme)×I:
      hepsi yeniden hesaplandı, hepsi tuttu. Dört kuşakta ilk kez aritmetik temiz.
      ⛔ Ama tamamı FİZİKSEL KAMERAYI anlatır; bu depoda kamera yoktur. Doğru
         olmak, uygulanabilir olmak değildir. ⇒ KAMERA_HAREKETI §2
A13-b ⭐ DİJİTAL YAKINLAŞMA SIFIR PARALAKS ÜRETİR                    [VARSAYIM · fizik]
      Ön plan ve arka plan aynı oranda büyür; optik perspektif değişmez.
      ⇒ Kurgu yakınlaşması DERİNLİK vaat edemez, yalnız DİKKAT yönetir.
         Plana "paralaks/derinlik artar" YAZILMAZ. ⇒ KAMERA_HAREKETI §2.3
A13-c ⭐ YAKINLAŞMA TAVANI = kaynak genişliği / teslim genişliği      [ÖLÇTÜM · kapı]
      Rapor ">%120 pikselleşir" der — kaynak = teslim olduğunda doğru, bizde
      eksik koşullu. 1080×1920 teslimde: 1674×2976 → 1,55× · 1836×3264 → 1,70× ·
      2160×3840 → 2,00×. Upscale bu tavanı SAĞLAMAZ. ⇒ KAMERA_HAREKETI §3.3
A13-d 180° ENSTANTANE KURALI, BİZİM MOTION STREAK ŞARTIMIZIN OPTİK KARŞILIĞI —
      A4/DERS 50 ile aynı yönde, yeni bir şey söylemiyor.
```

### A14 — KAMERA HAREKETİ VE İZLEYİCİ TUTMA

```
A14-a ⭐ KARAR İLK 0–1 SANİYEDE VERİLİYOR                            [VARSAYIM]
      ⇒ Bizde karşılığı: G0'da DEĞİŞİM ZATEN BAŞLAMIŞ olmalı — boş arsa değil,
        ilk müdahalenin görüldüğü arsa. THE NARROW GORGE'un 1. düzeltmesi.
        ⇒ KAMERA_HAREKETI §4
A14-b ÇIPA VE KEŞİF DENGESİ (sürenin çoğu sabit ana kamerada)        [VARSAYIM]
      Oran çözümlenemiyor, yön bizim formatımızla aynı. ⇒ KAMERA_HAREKETI §3.2 ④
A14-c ⭐ KESİNTİSİZ KAMERA HAREKETİ + TIMELAPSE HIZI = DOKU BOZULMASI [VARSAYIM]
      DERS 56 ile aynı yönde; katman 1'in kapalı kalma gerekçesini dışarıdan
      destekler. ⇒ KAMERA_HAREKETI §1.1
A14-d ⛔ LOOP: BİZDE KADRAJ DÖNGÜSÜ OLUR, DURUM DÖNGÜSÜ OLMAZ         [YENİ]
      Son kare ilk kareye "bağlanırsa" yapı sökülmüş olur ve film vaadini geri
      alır. Bizim loop'umuz kavramsaldır: aynı kadraj, başka dünya.
      ⇒ KAMERA_HAREKETI §5
A14-e ❌ "900×1400 evrensel güvenli alan" DÜŞTÜ                       [DENETİM]
      Kendi marj tablosuyla çelişiyor; en kötü hâl 940×979. Bizim zarfımız
      (KAMERA_ISTASYONU §6) zaten daha dar ve DEĞİŞMEDİ.
A14-f 9:16'DA YATAY PAN ÖZNEYİ KADRAJDAN ÇIKARIR — dikey eksen tercih edilir.
      Bizde ikisi de katman 1'de; yalnız kadraj içi DİKEY SÜPÜRME olarak kalır.
```

### A15 · A16 · A17 — KAPAK VE PAKETLEME

```
A15-a ⛔ CTR BANTLARI · "%25–30 yüz" · "60.000 kat" KILAVUZA İNMEDİ   [İDDİA]
      Kaynak sınıfı pazarlama; 00_README §3 adım 2b gereği durduruldu.
A15-b ⭐ KARŞILAŞTIRMA ARACI KAZANANI İZLEME SÜRESİ PAYINA GÖRE SEÇER [İDDİA · araç dokümanı]
      ⇒ Kapak yarışı CTR yarışı değildir; tıklatıp tutamayan kapak kaybeder.
        §3.3 spoiler bütçesini güçlendirir. ⇒ MUZIK_VE_KAPAK §4.3
A15-c ⭐ SAĞ ALT KÖŞEYİ SÜRE ETİKETİ KAPATIR                          [İDDİA · araç dokümanı]
      ⇒ 120 px testine üçüncü soru eklendi. ⇒ MUZIK_VE_KAPAK §4.2
A16-a ⭐ SAPMA ÇARPANI YÖNTEMİ: başarı toplam izlenme değil, KANAL ORTALAMASINA
      GÖRE sapmadır. ⇒ Yayın ölçümümüzün metriği bu olmalı [apexait/YAYIN_PLANI].
A16-b ❌ TABLO HATASI: 1.200.000/25.000 = 48x; rapor 48.000x yazıyor. On bir
      satırın onu tuttu, biri bin kat şişik — ve o satır örüntü kanıtı sayılmış.
A16-c KÜÇÜK KANAL, BÜYÜK KANALIN KAPAĞINI KOPYALAYAMAZ: tanınmayan yüz/minimalizm
      soğuk izleyicide karşılık bulmaz. ⇒ Bizde zaten yüz yok; odak YAPININ kendisi.
A17-a YZ KAPAK KUSURLARI (plastik cilt · anatomi · tutarsız ışık kaynağı) — bizim
      kapağımız usta kareden türediği için bu risk FİLMDE çözülür, kapakta değil.
A17-b 1280×720 · 2 MB · 16:9 — uzun format kapağının teknik zarfı. Dikeyde
      kapak yüklemesi ayrı yüzeydir. ⇒ MUZIK_VE_KAPAK §4.3 uyarısı
A17-c ⚠️ KISA DİKEY FORMATTA A/B TESTİ YOK — deneme uzun formata ertelenir.
```

### A18 — VİRAL TIMELAPSE KAMERA ÖRÜNTÜLERİ

```
A18-a ⛔ ÇELİŞKİ — SABİT KAMERA KUSUR MU, İMZA MI                     [ÖLÇÜLMEMİŞ]
      A14: "tamamen sabit kamera 10. saniyeden sonra %40 kayıp".
      A18: aynı veri setinde EN SIK kullanılan hareket = sabit kamera, ve
      merkez-kilitli sabit kadraj "kesin bulgu" sayılıyor.
      ⇒ Aynı yapıştırmada gelen iki rapor ters yönde konuşuyor. Kart S §4:
        bu değişken ÖLÇÜLMEMİŞTİR ve bu bilgi sayının kendisinden değerlidir.
        ⛔ Format kimliği bu kuşak yüzünden DEĞİŞMEZ.
A18-b MERKEZ KİLİTLEME: dikeyde ana dönüşüm alanı kadrajın orta şeridinde durur.
      ⇒ KAMERA_ISTASYONU §6 zarfıyla aynı yönde, yeni bir sayı getirmiyor.
A18-c "ÇEVRE ELEMANLARINI SABİTLEME" — nesne değişirken arka plan ve ışık sabit.
      ⇒ Negatif çekirdeğin arka plan cümlesinin birebir aynısı [§7]. Doğrulama.
A18-d TEPEDEN 90° KADRAJ en yüksek ikinci sıklık — bizde YOK ve olmayacak:
      şantiyede kuş bakışı sabit istasyon kurulamaz, drone HAREKET olarak yasak.
A18-e FİNALDE GERİ ÇEKİLME (pull-out reveal) — bizde finalin karşılığı USTA
      KAREDİR ve zaten en geniş hâldir; geri çekilecek yer yoktur.
A18-f ❌ YÜZDE TABLOLARI 100 ETMİYOR (%102,5 ve %97,5): bir video çift, bir video
      hiç sayılmış. ⇒ Tablolar SIRALAMA olarak okunur, ORAN olarak değil.
```

---

## 🔬 A19 — KAMERA DİLİ · 20.09.2026 · tek rapor, sahip köke bıraktı

> Kaynak: `arastirma/SONUCLAR/A19_KAMERA_DILI_HAM.md` (kökteki VIRAL_TIMELAPSE_KAMERA_KILAVUZU.md
> buraya taşındı) · Denetim: `arastirma/SONUCLAR/A19_DENETIM.md` · Kılavuz: `KAMERA_DILI_KILAVUZU.md`
>
> ⭐ **Dört kuşakta en temiz kaynakça:** 11 kaynağın 10'u bu makinede açıldı ve iddiaya AİT
> çıktı (beş YouTube sayfası · matjoez · YouTube Yardım · Nikon ×2 · Veo rehberi · zeitraffer).
> ⛔ **Ama hiçbiri "hangi açı daha çok izlenir" sorusunu ölçmüyor** ve rapor bunu kendisi
> yazıyor ("bu bir viral formül değildir"). Prompt yine YOK. Bu kuşaktan kılavuza YENİ SAYI
> inmedi; iki FORMÜL indi (biri bizim türetmemiz) ve bir KARAR ÇERÇEVESİ.
> Her madde VARSAYIMDIR; ilk sınavı tiltli üç filmin usta kare ölçümüdür.

```
A19-a ⭐ KAYNAKÇA ÇEKİLDİ — 11'İN 10'U İDDİAYA AİT                    [DOĞRULANDI · bu makinede]
      İzlenme · tarih · ekipman (D750 + Rokinon 12 mm) · bölüm işaretleri · "1 pic a day
      değil" cümlesi · Veo "no/don't" tavsiyesi · YouTube 31.03.2025 — hepsi sayfada.
      ⛔ Kaynak sınıfı bir şeyi KANITLAMAZ: hiçbiri açı→izlenme ölçmez. ⇒ A19_DENETIM §1.1
A19-b ⭐ DEĞİŞİM BOYUTU → BAKIŞ AİLESİ                                 [VARSAYIM · karar çerçevesi]
      "Tepeden ALANI, yandan SEVİYEYİ, çapraz İKİSİNİ gösterir; seçim videonun sorduğu
      soruya bağlıdır." Konsept kapısı ile Değişmezler arasında yazılı olmayan adım.
      ⇒ KAMERA_DILI §0 karar cümlesi + §2.3 tablosu (tilt bandı aileden gelir, seçilmez).
A19-c ⭐ TİLTLİ KADRAJ FORMÜLÜ — üç film yaklaşık formül kullanmış      [ÖLÇTÜM · türetim]
      KAMERA_ISTASYONU §3 yalnız tilt 0° için kesin. HIDDEN OASIS · SWALLOWED BUS (−40°) ·
      BACK TO WATER (−22°) açıyı kareye ORANTILI dağıtan doğrusal formülle yazıldı;
      rektilineer lens tanjantla dağıtır: yüzde = 50 + f·tan(tilt − atan((h−y)/d))/0,36.
      24 mm'de en büyük fark 2,9 puan — planı düşürmez, yöntemi düzeltir. Ufuk yalnız
      tilt'e bağlı: 50 + f·tan(tilt)/0,36. ⇒ KAMERA_DILI §3 · KALDIRDIĞI: göz kararı tilt.
A19-d KATSAYI FORMÜLÜ REJİM TABLOSUNU BAĞIMSIZ ÜRETTİ                  [ÖLÇTÜM]
      δ = pencere/(L×f) · oran = δ×f → SANTIYE_HAREKETI §1'in A·B·C satırları aynen çıkıyor
      (6 s). 8 s ızgarada sayı değişir; SANTIYE'ye EKLENMEZ, formül KAMERA_DILI §5'te.
A19-e POZLAMA ≈ İNTERVALİN YARISI → İZ                                 [VARSAYIM · optik]
      Rejim B'de δ 30–40 s → 15–20 s pozlama → insan İZ olur; G'de δ 0,033 s → iz yok.
      DERS 47 · 50 · A13-d'nin dördüncü dış doğrulaması; "soft motion streaks" üslup değil
      pozlamadır. ⇒ KAMERA_DILI §5
A19-f TELE SIKIŞTIRMAZ, KONUM SIKIŞTIRIR · ZOOM ≠ DOLLY                 [VARSAYIM · optik]
      A13-b (sıfır paralaks) ile aynı yön; detay istasyonu 50 mm "yakın" değil aynı D'den
      DAR bakıştır. ⇒ KAMERA_DILI §4 · PERSPEKTIF §4 ölçek cümlesi
A19-g ⛔ HAREKET REÇETELERİ ALINMADI                                    [ÇELİŞKİ · karar değişmedi]
      slider 40 cm · orbit 20° · dolly out 1,5 m · pedestal 0,7 m · "finalde geri çekilme"
      → katman 1 üç kez düştü [KAMERA_HAREKETI §1.1]; final usta karedir [A18-e].
      Raporun kendi "önce sabit sürümü dene · tek hareket" uyarısı bizim kuralın gevşek hâli.
A19-h ⚠️ NEGATİFTE "NO" — Veo "öğe adı yaz" diyor, imzalar kalıyor      [araç dokümanı ✅ · kısmi çelişki]
      İmzalar ölçülmüş kapı [DERS 35]; gövde zaten pozitif [DERS 11]; DERS 33 aynı yönde.
      ⇒ Araç kartına SORU (⑨ adayı): ayrı negatif alanda "no X" ile "X" aynı sonucu veriyor mu.
      Ölçülmeden kural olmaz. ⇒ KAMERA_DILI §8
A19-i ⚠️ TERS AÇILIŞ DÖRDÜNCÜ KEZ ÖNERİLDİ — alınmadı                  [ÇELİŞKİ]
      DERS 3 · A1-b · P2-l ① · A14/A15 · şimdi A19 §12. Dış 4, iç karşı kayıt 1 film.
      Ölçüm borcu KAMERA_HAREKETI §4.1'de yazılı; rapor da bunu DENEY olarak öneriyor.
A19-j "HER HAREKETİN GEREKÇESİ TEK CÜMLE" — katman 2 tablosu bunu zaten ister [VARSAYIM]
      "yakında görülen · HOME'a dönünce kazanılan" sütunları [KAMERA_HAREKETI §3.4];
      ikisi dolmayan yakınlaşma plana yazılmaz. ⇒ KAMERA_DILI §6
A19-k RAPORUN KAYIT KARTI = BİZİM ON BLOK; SEKİZ PROMPTU KAPIDAN GEÇMEZ [VARSAYIM]
      Aynı on alan, bizde her biri imzalı. Promptlar T2V (iki uç yok) · "Scene n of N" yok ·
      milimetre yazıyor · rejim beyanı yok · dördü hareket ister. Çeviri kuralı: mm plana,
      metre+derece prompta. ⇒ KAMERA_DILI §7
A19-l 15 BELİRTİNİN 14'Ü BİZDE KARŞILIKLI, 7'Sİ NUMARALI DERS         [dış doğrulama]
      "temizlenen yeniden kirleniyor" = DERS 5 · "malzeme kayboluyor" = DERS 48 · "bina
      eğiliyor" = DERS 19 · "final acele" = DERS 45 · "orbitte arka değişir" = DERS 52 …
      Raporun düzeltme sırası (süreklilik → kadraj → ritim → efekt) = kart R 6a. ⇒ §12
A19-m ⚠️ YATAYDAN SHORTS KESİTİ — AÇIK SORU                             [sahip kararı]
      4K yatay master → 1215×2160 merkez kırpma ayrıntı korur; 1080p → 608×1080 üretmez.
      CAPRAZ_YAYIN §1 "tek master" bu soruyu kapsamıyor; yatay HOME dikey kesite göre
      kurulmadı. ⇒ KAMERA_DILI §9 — karar verilirse CAPRAZ_YAYIN'a iner.
A19-n TEST MATRİSİ ALTIDAN BİRE İNER                                    [VARSAYIM]
      A2/B2/C2 katman 2 (NARROW GORGE ölçümü) · C1 alçak yok · B1 tepeden yalnız kare.
      Test edilebilen: aile İÇİNDE tilt bandı ve h/D, aynı yapı tipinde iki film, tek
      değişken [06_IZLEYICI_DENEY_PLANI]. Kayıt satırına AÇI etiketi (aile · tilt · h/D).
```

---

## 🔬 A20–A24 — QA ONARIMI · 06.10.2026 · beş rapor, prompt bu depoda yazıldı

> Kaynak: `arastirma/SONUCLAR/A20…A24_GEMINI_HAM.md` · Denetim: `arastirma/SONUCLAR/A20-A24_DENETIM.md` ·
> Kılavuzlar: `QA_KOSU` · `QA_OLCUM_ZEMINI` · `RUBRIK_YAZIM` · `QA_KALIBRASYON` · `QA_KAYIT`.
>
> Tetikleyen: 06.10.2026 QA denetimi (393 ham · 37 film) — 2x kopya ≥ 6 filmde "kesik" okundu ·
> kör merceklerde plan sızıntısı · belgesiz / yanlış belgeli koşular · %31 kanıtsız 10,0 ·
> INDEX'te 5 "üretilmedi" film. 61 atıf çekildi: 32 ✅ · 24 ⚠️ (çoğu gerçek makale, başka konu) ·
> 2 ❌ · 3 ❓. Rapordan doğrudan inen sayı yalnız Gemini API dokümanının üç değeri.
> Her madde VARSAYIMDIR; ilk sınavı kalibrasyon pilotu ve kör merceklerin geçici sohbette yeniden koşusu.

```
A20-a ⭐ GEM / PROJE DOSYALARI HER SOHBETE GİRER                      [araç dokümanı ✅ · çekildi]
      Gem bilgi dosyaları o Gem'in bütün sohbetlerine, proje dosyaları projedeki sohbetlere
      girer; kişisel bağlam varsayılan açık; geçici sohbet kapatır. Kör sızıntının en olası
      sebebi bugünkü "proje içinde koşu" düzenidir (kanıtı: projenin içeriği — sahip bilir).
      ⇒ QA_KOSU §1 · KALDIRDIĞI: "yeni sohbet = temiz oturum" varsayımı.
A20-b GERİ OKUMA YALNIZ OKUNABİLENE — dosya adı + belgenin ilk satırı    [VARSAYIM · Ç2]
      Süre geri okuması kapı değildir (model süre ölçmüyor). ⇒ QA_KOSU §2.2
A20-c SIZINTI METİNDEN ÖLÇÜLÜR — liste + kanarya terimi                [VARSAYIM]
      Kör merceğe "plan gördün mü" sorulmaz; plandaki sayı ve adlar raporda aranır.
      "belge yok" cümlesi sızıntı DEĞİLDİR. ⇒ QA_KOSU §3.1
A20-d FAIL CLOSED — eksik/yanlış/sızdırmış koşunun puanı yok, doldurulmaz [VARSAYIM · klinik eksik veri ilkesi]
      ⇒ QA_KOSU §4 · RUBRIK_YAZIM §4.2 (N=…)
A21-a ⭐ MODEL SAYMAZ — 1 fps örnekleme, 2x'te klip başına ~4 kare       [araç dokümanı ✅ + ÖLÇTÜM]
      Gemini API varsayılan 1 kare/sn (fps ayarlanabilir · ~70 token/kare); sohbet arayüzünün
      örneklemesi belgesiz. Bizim ölçüm: aynı dosyada 1…23 klip. ⇒ QA_OLCUM_ZEMINI §1
A21-b ÖLÇÜLMÜŞ OLGULAR BLOĞU RUBRİĞİN İÇİNDE                          [VARSAYIM · hibrit düzen]
      2x beyanı yapıştırma çizgisinin ÜSTÜNDE kaldı [DERS 63 açığı]. ⇒ QA_OLCUM_ZEMINI §2
A21-c ⛔ KESME EŞİKLE BULUNMAZ — top-N KALIR                           [ÖLÇTÜM · bu makinede]
      PySceneDetect -t 27 düşük kontrastlı sentetik kesmenin 6'sından 3'ünü buldu;
      kesme_kontrol top-N 6/6. "%99" kaynaksız (aracın kendi ölçümü %63–85).
      tblend+blackframe yavaş timelapse'i baştan sona "statik" sayıyor. ⇒ QA_OLCUM_ZEMINI §2
A21-d DOĞRULAMA KATMANI D1–D5 — dosya dışı damga raporu düşürür          [VARSAYIM · tolerans ±0,5 sn]
A21-e ⚠️ HANGİ DOSYA — süreç mercekleri 1x master, izleyici mercekleri 2x  [sahip kararı]
A22-a FORMAT DEĞİŞKENLERİ BLOĞU — kart · müzik · hız · klip rubrikte varsayılmaz [VARSAYIM]
      ⇒ RUBRIK_YAZIM §1 · temizlik listesi §6
A22-b KANITSIZ 10 YOK — 7'nin üstü zaman damgası ister                   [VARSAYIM · rapor da öyle etiketledi]
      Sınavı: ilk üç filmde 10,0 oranı ve kanıtlı-10 oranı. ⇒ RUBRIK_YAZIM §2.2
A22-c ORTALAMA KODDA · önce gerekçe sonra puan                           [akademik ✅ · 2606.09410 · CheckEval]
      Biçim zorlaması akıl yürütmeyi düşürüyor, gecikmeli yapı kurtarıyor. ⇒ RUBRIK_YAZIM §4.1 · §7
A22-d ⭐ KÖTÜ OLAN KAZANIR — "hüküm kazanır" yarıya indi                  [ÇELİŞKİ Ç3 · karar]
      Kötü hüküm iyi kategoriyi ezer; iyi hüküm sahip kategori ≤ 3'ü ezemez → rapor tutarsız.
A22-e ⭐ KUSUR SAHİPLİĞİ — bir kusur tek mercekte puan kırar              [VARSAYIM · ayırt edici geçerlilik]
      ⑨ ⑩'un çoğu ⑦ ⑧'in sorusu → ⚠️ sahip kararı (emekli · daralt · bugünkü). ⇒ RUBRIK_YAZIM §5
A23-a TEST-TEKRAR PİLOTU 3 × 4 × 3 · medyan · aralık eşiği              [VARSAYIM · eşikler bizim]
      Determinizm varsayılmaz (Ç1 — iki rapor da kaynağa uymuyor). ⇒ QA_KALIBRASYON §1
A23-b TOHUMLANMIŞ KUSUR SETİ — 10'un 5'i düzeltildi                     [ÖLÇTÜM · bu makinede]
      drawtext yok · scale zaman çizelgesi yok · loop süre ekliyor · crop boyut değiştiriyor ·
      drawbox kaybettirmiyor. Set KABA kusur ölçer; gerçek arızalar geçmiş kesitlerden.
A23-c ÇAPA FİLM — puan > 1,0 oynarsa hakem değişti                        [VARSAYIM] ⇒ QA_KALIBRASYON §4
A23-d DIŞ GEÇERLİLİK: ρ 0,50 için 29–30 film (rapor 28)                  [ÖLÇTÜM · yeniden hesaplandı]
      Defter ~23 filmle yalnız yön gösterir. 06_IZLEYICI_DENEY_PLANI arşiv, defter bağlayıcı.
A24-a ⭐ KANITTAN TÜRET — elle özet uzlaştırmasız durmaz                  [düzenleyici belge ✅ · FDA Q12 (rapor Q15 dedi)]
      ⇒ QA_KAYIT §0 · §5 (U1–U10)
A24-b DURUM MODELİ — ham rapor varsa film en az ÜRETİLDİ                  [VARSAYIM] ⇒ QA_KAYIT §1
A24-c HAM DOKUNULMAZ → ESKİ ARŞİV EŞLEME TABLOSUYLA                     [ÇELİŞKİ Ç5 · karar]
      Raporun YAML enjeksiyonu inmedi; yeni hamlarda künye kaydederken yazılır. ⇒ QA_KAYIT §2
A24-d TEK AD ŞEMASI <FILM>_<n>_<MERCEK>_HAM.md · n = MERCEK numarası     [karar · Ç6] ⇒ QA_KAYIT §3
```

---

## 🔬 A25–A29 — FİLM YAZIMINDAN DOĞAN BEŞ KILAVUZ · 07.10.2026 · beş rapor, prompt bu depoda yazıldı

> Kaynak: `arastirma/SONUCLAR/A25…A29_GEMINI_HAM.md` · Denetim: `arastirma/SONUCLAR/A25-A29_DENETIM.md` ·
> Kılavuzlar: `UZUN_FORM_ANLATI` · `ISTASYON_VE_IC_MEKAN` · `SU_VE_YANSIMA` · `ISIK_FINALI` · `ONARIM_VE_YENIDEN_URETIM`.
>
> Tetikleyen: 07.10.2026 THE SLOW TAKEOFF yazımı (yatay 4:00 · 30 × 8 sn · iki kokpit klibi · bahar seli ·
> mavi saat · kano finali) — shorts kurallarının yatay karşılığı yok · ikinci istasyon kuralları çelişiyor ·
> su ve ışık kılavuzsuz · QA hükmünden onarıma giden yol yazılı değil. 33 atıf çekildi: 20 ✅ · 8 ⚠️ · 5 ❌.
> Hesaplar bu makinede koştu (alacakaranlık 9/9 · yansıma 12/12 · kano · kare süresi); BİZİM yansıma
> bandı hesabımız düzeldi (794–891 → 786–883 px). Raporların kendi "ÖLÇÜLDÜ" yüzdelerinin çoğu inmedi.
> Her madde VARSAYIMDIR; ilk sınavı THE SLOW TAKEOFF üretimi, QA'sı ve yayını.

```
A25-a ⭐ MERAK ZİNCİRİ — her soru bir klipte açılır, ileride bir klipte cevaplanır  [akademik ✅ · Loewenstein 1994]
      İlk büyük sonuç 30. saniye civarında ("Intro" ölçüsü — platform ✅); en büyük soru EN SON
      cevaplanır; ortada art arda dört klipte yeni bir şey yoksa sahne eklenir/taşınır.
      ⇒ UZUN_FORM §0 · §3 · §4 · KALDIRDIĞI: "yatayda shorts kuralları aynen geçer" varsayımı.
A25-b AÇILIŞ–FİNAL KAFİYESİ — dikeyin DÖNGÜ'sü yatayda döngü değildir      [VARSAYIM]
      Aynı yer, karşıt hâl (çamurdaki gövde ↔ ışıklı ev). ⇒ UZUN_FORM §1
A25-c SON EKRAN son 5–20 sn · video ≥ 25 sn · kartsız filmde tutuş o süre kadar  [platform ✅ · YouTube Help]
      Bölümler (chapters): ≥ 3 damga, ilki 0:00, her biri ≥ 10 sn ✅ — tutmaya etkisi BİLİNMİYOR.
      ⇒ UZUN_FORM §6 · ⚠️ Ç6: raporun "olay bitimden 15–20 sn önce" önerisi kartsız 4 sn tutuşla çelişir.
A25-d EĞRİ → SAHNE: S = ⌊t / klip⌋ · 7. ve 28. gün · typical = son 10 benzer video  [platform ✅ + aritmetik]
      Key moments ≥ 60 sn video ve ≥ 100 izlenme ister ✅. Test & compare İZLENME SÜRESİ payını ölçer,
      tutma eğrisini değil ✅. Tek videodaki gözlem kural değildir — ÜÇ FİLM KURALI. ⇒ UZUN_FORM §7
A25-e ⚠️ Ç1 — THE SLOW TAKEOFF kalkışı 0:40 bir ÖLÇÜM SORUSUDUR             [sahip kararı korunur]
      Bilgi boşluğu "erken doruk merakı bitirir" der; sahip YouTube'un "güçlü anı öne al" önerisini
      seçti. Sınav: 0:56 sonrası eğride düşüş var mı (S7–S8). ⇒ UZUN_FORM §2
A26-a ⭐ MEKÂN KESİNTİSİ BÖLÜTLEMEZ, EYLEM KESİNTİSİ BÖLÜTLER              [akademik ✅ · Magliano & Zacks 2011 · Ç3]
      Raporun EST yorumu ("yer değişimi olay sınırıdır") ölçümle ters — ölçüm kazandı. İkinci kamera
      AYNI işin ikinci bakışıdır; o kesmede iş sürer. ⇒ ISTASYON §0 · §1
A26-b DİKEY EK · YATAY KLİP — "≤ 2 sn ek" ile "iki detay sahnesi" çelişkisi kapandı  [karar · Ç2]
      Dikeyde ikinci istasyon EK'tir (merdiven satırı almaz); yatayda tam KLİP'tir (8 sn, satır alır).
      Doruk, bölüm sınırı ve final ikinci kamerada OLMAZ (THE SLOW TAKEOFF S14 → S13 · SAPMA ⑧).
      ⇒ ISTASYON §1 karar tablosu
A26-c KOMPOZİT YALNIZ İKİ KAMERA AYNI YÖNE BAKIYORSA                      [VARSAYIM · bizim geometri]
      Raporun prompt şablonu bizim tilt 0 · tek SITE düzenine uymadı, inmedi. Paralel zaman: S12 → G14 ← S14;
      ana dış kare iki yakada aynı kalır, iç klibin kendi iki karesi (Gn′). "Aynı yer" doğrulaması elle:
      ortak çapa + ufuk %50; LightGlue gerçek ✅ ama kurulu değil, eşiği kaynaksız. ⇒ ISTASYON §2 · §3
A26-d İÇ MEKÂN DİLİ — pencere ışık lekesi kayar · mobilya akar · yüz okunmaz  [VARSAYIM · pratik]
      Ana kameradan iç iş OKUNMAZ (kabin penceresi ≈ 8 px) — içeriyi ya ikinci kamera ya taşınan
      parçalar anlatır. ⇒ ISTASYON §4 · §5 bloklar (kapı BLOCK 0)
A26-e ⬜ QA ❶ BEYAN SATIRI — kör merceğe ikinci kamera söylenir mi        [sahip kararı · açık]
      Beyan körlüğü bozar, beyansızlık "SEPARATE IMAGES" riskidir; ölçülmedi. ⇒ ISTASYON §6
A27-a ⭐ YANSIMA x = D·h/(h+y) · kadrajda ufkun 118,5·(h+y)/D altında     [ÖLÇTÜM · bu makinede 12/12]
      Rapor bizim formülü bağımsız verdi ✅ ve bizim kare tablosundaki hatayı buldu: THE SLOW TAKEOFF
      yansıma bandı 786–883 px (eski 794–891). ⇒ SU §1 · KALDIRDIĞI: "yansıma her suda görünür".
A27-b FRESNEL SIYIRMADA GÜÇLENİR · AYNA BEAUFORT 0–1'DE KALIR             [akademik ✅ · Cox–Munk · NOAA · Ç4]
      Raporun "2–3 m/s" dalgacık eşiği ❌; Beaufort 1 = 0,3–1,5 m/s. Durgun ayna promptta sakin hava ister.
      ⇒ SU §2
A27-c BULANIK TAŞKIN SUYU KAHVE-OPAK · ISLAK BETON + DURGUN SU = "HAVUZ"   [VARSAYIM · DERS 54 ile]
      ⇒ SU §3 · su gelmeden önceki karede durgun su YOK.
A27-d SU KOTU DEFTERİ — kot sabit nesneye göre kesirle · tanık çizgi kalıcı  [VARSAYIM · TIDE GATE ✅ okundu]
      Yükselme ve çekilme AYRI kliplerdir; su bir yönden gelir, o yöne gider. ⇒ SU §8 · PLAN'a zorunlu
A27-e SU ÜSTÜNDE TAŞIT ≤ 13 m / 8 sn (G rejimi) — rota HESAPLANIR          [ÖLÇTÜM · aritmetik · kano 4–6 km/sa]
      4 / 6 km/sa → 8 sn'de 8,9 / 13,3 m. BACK TO WATER teknesi kadrajdan çıktı; THE SLOW TAKEOFF
      kano rotası kısaltıldı. ⇒ SU §7
A27-f REJİM DİLİ — A/B'de su "kademeli yükselir", dalgacık YAZILMAZ; G'de titreşir  [VARSAYIM · raporun 1/3'ü inmedi]
      VideoPhy-2 "%47,7" hiçbir kaynakta yok ❌ · Physics-IQ sıralaması düzeltildi ⚠️. ⇒ SU §5 · §6
A28-a ⭐ ALACAKARANLIK TABLOSU — −0,833°'den dakika · pencere −2…−6°        [ÖLÇTÜM · bu makinede 9/9]
      cos(HA) = [sin(alt) − sinφ·sinδ] / (cosφ·cosδ) · 4 dk/derece. Raporun tablosu doğru ama
      referansı yanlış etiketli. THE SLOW TAKEOFF 47° K · δ +12° · −4,4° = 19:20. ⇒ IŞIK §1
A28-b ⭐ A VE B REJİMİNDE IŞIK TEK KAREDE YANAR                           [ÖLÇTÜM · aritmetik · P12-d]
      A: kare başına 2,5 sn · B: 30 sn — bir anahtarın açılışı bir kareden kısadır. Sıra = grupların
      farklı anlarda yanması ("first … then … last …"), fade değil. ⚠️ Ç5. ⇒ IŞIK §2
A28-c OLUMSUZLAMA ÇAĞIRIR — "no flare" yazılmaz, pozitif tarif edilir      [akademik ⚠️ · NegT2IBench 2610.03084]
      11 modelin 9'u olumsuzlamada kötüleşiyor; başarısız çıktıların %41,5'i olumsuzlanan nesneyi çiziyor.
      DERS 33 · 35 · 59'u ilk kez dış ölçüm destekliyor (sayı raporda karışık verildi, makaleden düzeltildi).
      ⇒ IŞIK §5
A28-d IŞIK DEFTERİ — armatür · takıldığı klip · sönük kareler · grup · sıra · K · yansıma  [VARSAYIM · P11-d]
      Final ışıklıysa PLAN'a zorunlu; armatür birkaç klip önce SÖNÜK takılı görünür. ⇒ IŞIK §4
A28-e ÖNCE IŞIKLI USTA KARE — ışıksız kareler ondan geriye türetilir        [VARSAYIM · DERS 5 ile]
      Kapak bu kareden (GN) — öncesi/sonrası bölünmüş kapak YOK. Küçük resimde kontrast WCAG ✅ ölçüsüyle.
      ⇒ IŞIK §6
A29-a ⭐ ZİNCİRDE BÖLGE DÜZELTME YOK — video inpainting / v2v dikiş karesini bozar  [VARSAYIM · format gereği]
      Raporun "postta düzelt" yolunun çoğu iki-kare kilidiyle çelişir; çapraz geçiş zaten yasak.
      ⇒ ONARIM §0 · §1.2
A29-b KLİBİ BÖL — araya yeni bir kare (Gn½) koymak iki zincirli klip üretir  [VARSAYIM · pratik]
      Yöntemsiz belirme ve tek klipte iki büyük iş için ilk eylem. ⇒ ONARIM §1.2 · §2
A29-c DURMA KURALI 3 / 6 — aynı eylem 3 kez · toplam 6 deneme → sahneyi yeniden tasarla  [VARSAYIM · eşik bizim]
      Raporun matris yüzdeleri uydurmaydı, inmedi. ⇒ ONARIM §5
A29-d ⭐ KARE DEĞİŞİRSE İKİ KLİP · İKİ DİKİŞ SINANIR                      [aritmetik · zincir gereği]
      Gn hem S(n−1)'in sonu hem S(n)'in başı; onarımdan sonra iki dikişte zincir_kontrol + kanıt nesnesi
      elle. LPIPS / RAFT ölçüsü ⬜ açık. ⇒ ONARIM §3 · §4
A29-e BEŞ KÖK NEDEN → TEK EYLEM — ARAÇ · PROMPT · KARE · KURGU · PLAN        [VARSAYIM · arşiv örnekleri]
      MOUNTAIN DOOR (araç) · DEEP STEP (prompt) · STONE DRAGON (kare) · GLASS WALL (kurgu). Sürüm adı
      G<n>_K<k> / S<n>_K<k>; günlük §5'e her deneme bir satır. ⇒ ONARIM §1 · §6 · AGENTS kart R adım 10
```

---

## 🔬 A30–A34 — VİRAL 2026 · KANAL YAYINA ÇIKMADAN · 07.10.2026 · beş rapor, prompt bu depoda yazıldı

> Kaynak: `arastirma/SONUCLAR/A30…A34_GEMINI_HAM.md` · Denetim: `arastirma/SONUCLAR/A30-A34_DENETIM.md` ·
> İndiği yer: `apexait/TUR_HARITASI` (yeni) · `youtube/POLITIKA_VE_RISK` · `CAPRAZ_YAYIN` · `IZLEYICI_DEFTERI` ·
> `YAYIN_PLANI` · `tiktok/` · `instagram/HESAP_KIMLIGI` · `KILAVUZ_REHBERI §6`.
>
> Tetikleyen: 37 film üretildi, 0 yayın — tür, platform, politika, paylaşım ve büyüme hakkında tek ölçüm yok.
> 84 atıf satırı çekildi: 32 ✅ · 32 ⚠️ · 18 ❌ · 2 ⬜. Platform kuralları resmî sayfalardan birebir çekildi ve
> kuşağın en sağlamı çıktı; akademik ve pazarlama yüzdeleri en zayıfı. A30'un tablosu bu makinede yeniden sayıldı
> (iki grup ters yazılmıştı). Bir kanal dosyası bayat çıktı (tiktok §5 · Ç10). Raporların sahip kurallarını bozan
> önerileri ve iki ⛔ önerisi (kasıtlı hata · gönderme çağrısı) inmedi. Her madde VARSAYIMDIR; ilk sınavı açılış
> bloğu ve 7. gün defteri.

```
A30-a ⛔ DIŞ HAVUZ İKİ GRUBU AYIRMIYOR, YAPIŞTIRIYOR                     [ÖLÇTÜM · tablodan yeniden sayım]
      ≥ 1 M = 11 (8 gerçek, 2 yapay zekâ — ikisi YATAY) · < 1 M = 15 (15'i yapay zekâ, 12'si Shorts) ·
      ≥ 1 M yapay zekâ DİKEY Shorts = 0. Kamera, süre, ses, etiket aynı çizgide ayrılıyor; hiçbiri tek
      başına okunamaz. Konu (onarım) iki grupta da çoğunluk — C2-e'yi ne doğruladı ne düşürdü.
      ⇒ TUR_HARITASI §1 · KILAVUZ_REHBERI §6 notu · KALDIRDIĞI: — (raporun "üst çeyrek" yüzdeleri inmedi)
A30-b ⚠️ A18-a AÇIK KALDI — üçüncü rapor da ölçümsüz                       [karar · Ç3]
      A30 "dikeyde kusur" (yapışık veri) ↔ A32 "halüsinasyonu azaltır" ↔ A33 "huşuyu büyütür" — üçü VARSAYIM.
      Kapanış tek okumayla: yapay zekâ DİKEY Shorts içinde sabit ↔ hareketli. Gerçek ↔ yapay zekâ kıyası
      bu soruyu CEVAPLAMAZ. ⛔ Format kimliği değişmez. ⇒ TUR_HARITASI §4 · §5
A30-c DOĞRULANAN VAKALAR — iki yapay zekâ timelapse'i YATAY şehir evrimi (2,44 M · 20 K); dört gerçek
      video elle inşa/onarım (22,9 M · 42,5 M · 4,0 M · 1,23 M)            [web ✅ · n = 6 · okuma 07.10.2026]
      ⇒ TUR_HARITASI §2 — yön, kural değil · vaka defteri §5 açıldı (hedef 30)
A31-a ⭐ GÖRÜNTÜLEME = ERİŞİM · ENGAGED VIEWS = FİLM                      [platform ✅ · Ç8]
      Shorts 31.03.2025, bütün formatlar 24.08.2026: oynatma başlar başlamaz sayılır. Kazanç engaged
      views'tan; YPP uygunluğu "qualified views". ⇒ IZLEYICI_DEFTERI §1b · POLITIKA §5
A31-b "KAYDIRMADI %" = "How many chose to view" (Studio → Analiz → İçerik → Shorts)  [platform ✅ · eşik ❌]
      "%40–50 kaydırırsa dağıtım durur" anonim, düşük kaliteli işaretli forum yanıtı — eşik kullanılmaz.
      Ort. izlenme engaged views üzerinden ve döngüsüz hesaplanır; ">%100" yalnız kullanıcı raporu ⚠️.
      ⇒ IZLEYICI_DEFTERI §1b · KALDIRDIĞI: — (evrensel eşik zaten yasaktı)
A31-c ⭐ SHORTS'TA A/B TESTİ YOK — "A/B testing is not available for Shorts"   [platform ✅ · A17-c doğrulandı]
      Uzun formda başlık + küçük resim, masaüstü, advanced features. Dikeyde kapak/başlık KURALLA verilir.
      ⇒ CAPRAZ_YAYIN §4.1 · POLITIKA §5
A31-d ORİJİNAL > YENİDEN PAYLAŞIM — filigran, başka yerde yayımlanmış ya da HIZI değiştirilmiş içerik
      Instagram'da geri planda (2023 · 2024 · 30.04.2026); TikTok kopyayı önermez  [platform ✅]
      ⇒ CAPRAZ_YAYIN §1.1 resmî dayanak · aynı filmi aynı platformda iki kez yükleme yasağın parçası
A31-e INSTAGRAM SİNYALLERİ — watch time · likes · sends (erişim başına); bağlantısız erişimde gönderme ağır
      [platform temsilcisi ✅ · Mosseri 22.01.2025] ⇒ IZLEYICI_DEFTERI §1b · §4 paylaşım sütunu
A31-f ARAÇ ŞARTLARI — Shorts → ilgili video ve uzun form A/B: advanced features · Trial Reels: profesyonel
      hesapta ≥ 200 takipçi                                                [platform ✅]
      ⇒ YAYIN_PLANI §4 açılış kutusu · CAPRAZ_YAYIN §4.1
A32-a ⭐ YOUTUBE 2026 METNİ FORMAT KARTINI TARİF EDİYOR                    [platform ✅ · 1311392 · spam 2801973]
      "content that looks like it's made with a template" · "templated storylines … with minimal or no
      narrative, commentary, or educational value" · "Automated or synthetic mass-production". 16.07.2026
      üç gruba ayrıldı (PARA kuralı). İlaç değişmez (POLITIKA §1.3), ama ② katman (sabit yorum = anlatı ve
      öğretici değer) artık para kazanmanın ŞARTI. ⛔ Anlatıcı eklenmez, klip süresi oynatılmaz.
      ⇒ POLITIKA §1.1b · KALDIRDIĞI: "② bir paketleme kalemidir" okuması
A32-b YAPAY ZEKÂ ETİKETİ OTOMATİK VE DEĞİŞTİRİLEMEZ — C2PA'lı dosyada YouTube kendisi koyar ("can not be
      adjusted"), TikTok 09.05.2024'ten beri ("you won't be able to remove"); fotogerçekçide oynatıcıda,
      27.05.2026'dan beri Shorts'ta overlay; tek başına öneriyi ve parayı etkilemez  [platform ✅]
      ⇒ POLITIKA §2 · CAPRAZ_YAYIN §2 · beyan kutusu yine işaretlenir (yaptırım beyansızlıkta)
A32-c İTİRAZ VİDEOSU — 21 gün (ön uyarıda 7) · < 5 dk · liste dışı · yeni yükleme · ilk 30 sn kanal URL'si ·
      14 günde yanıt · ret → 90 gün                                        [platform ✅ · 9564590]
      Kanıtı zaten depoda: plan · promptlar · reddedilen kareler (G<n>_K<k>) · onarım günlüğü · QA · kurgu.
      ⇒ POLITIKA §6 kriz kartı
A32-d ETİKETİN BEDELİ İZLEYİCİDE — "AI-generated" etiketi duygusal içerikte etkileşimi düşürür, geç beyan
      yapay zekâ ÜRETİMİNDE işe yaramaz (Seeger ve ark. 2026 · iki çalışma n≈696); beyan güveni azaltır
      (Schilke & Reimann 2025 · 13 deney > 5.000)                          [akademik ✅ · rapor N'leri ve atfı ❌]
      Beyan zorunlu kalır (platform + KILAVUZ_REHBERI §9.8) ve AÇILIŞTA kalır. ⇒ POLITIKA §2
A32-e INSTAGRAM 31.08.2026 ERİŞİM SINIRI YALNIZ YAPAY ZEKÂ KİŞİSİ OLAN PROFİLLER  [platform ✅ · Ç2]
      "Creators who simply use AI tools … don't need to add the label". Kanal adındaki "AI" bu kurala ne
      gerekir ne çarpar. ⇒ instagram/HESAP_KIMLIGI §6 · KANAL_KIMLIGI §1 değişmez
A33-a ⚠️ HUŞU → PAYLAŞIM ZAYIFLADI                                       [akademik ✅ — yön zayıf]
      Berger & Milkman 2012: 6.956 makale, e-posta paylaşımı, huşu +%30 / SS — mekanizma iki ön kayıtlı
      tekrarda tutmadı (Prowten 2024) · WeChat 387 K makalede (Yu 2025) sevinç ve öfke ↓ · Piff 2015 etkileri
      2026 tekrar dizisinde büyük ölçüde tutmadı · "oddly satisfying" üzerine nicel çalışma YOK.
      ⇒ konsept kapısına FİKİR PUANLAMA kartı İNMEDİ · İŞLEV ANI kuralı (C2-a) dış kanıt beklemez
A33-b ⛔ YORUM TUZAĞI YOK — kasıtlı hata · "find the mistake" · "send this to…" · "tag a friend"
      [platform ✅ · Meta 18.12.2017 engagement bait · TikTok FYF "Tricking others into increasing engagement"]
      Raporun "sessiz uzman tuzağı / Cunningham Yasası" ve A31'in "DM tetikleyici ibare" önerileri bu kuralla
      kapandı. ⇒ KILAVUZ_REHBERI §6 İZLEYİCİ KAPISI · CAPRAZ_YAYIN §6 □9 · IZLEYICI_DEFTERI §4
A33-c ASMR ETKİSİ YALNIZ DUYARLI İZLEYİCİDE — Poerio 2018: kalp −3,41 vuruş/dk (d = 0,39), yalnız ASMR
      yanıtlayanlarda · Barratt & Davis 2015 öz-seçilmiş N = 475         [akademik ✅]
      Müziksiz kural bir sahip kuralıdır, dış kanıtla "kanıtlanmadı" — A30'un "bilimsel olarak ispat" cümlesi
      turizm reels'i makalesine dayanıyordu ❌. ⇒ —
A33-d YORUM TÜRÜ SAYIMI — beş tür (övgü · şüphe · teknik düzeltme · mizah · soru), 7. gün, ilk 50 yorum,
      iki türe uyan TEKNİK DÜZELTME sayılır                               [VARSAYIM · yöntem bizim]
      "Gerçek mi" yorumu cevapsız bırakılmaz (POLITIKA §3 sabit cevap · Ç5). ⇒ IZLEYICI_DEFTERI §4
A34-a ⭐ YPP 01.02.2027 — yeni başvuran: 1.000 abone + 8.000 saat / 365 gün ya da 20 M Shorts / 90 gün;
      Shorts akışı saati sayılmaz                    [platform ✅ değişiklik · sayı basın + blog · Studio'dan doğrula]
      0 aboneli kanal eski eşiğe yetişemez → hesap yeni eşikle. Karar yönü aynı; yatay ayağın yükü iki kat.
      ⇒ POLITIKA §5 · §5.1 · ⬜ yatay kadans sahip kararı (denetim §8 K1)
A34-b KADANS — ayda 4–7 yükleme medyan görüntüleme büyümesi %1,32/ay, 12+ %2,18/ay (vidIQ, 10,2 M kanal)
      [bağımsız analiz ✅ · korelasyon, nedensellik değil] ⇒ YAYIN_PLANI §1 · kadans kuralı değişmez
A34-c SİLME YOK — "very, very good reason … keep your videos public or unlist them" (Beaupré 23.03.2024)
      [platform temsilcisi ✅] ⇒ POLITIKA §6 doğrulandı · YAYIN_PLANI §6.3
A34-d İKİ FORMAT, İKİ ÖNERİ SİSTEMİ — "separate recommendation systems … understand cross-format viewing";
      Shorts'un uzun formu düşürdüğüne kanıt yok · "format-aware discovery" ve "50–500 tohum kitle" blog
      [platform ✅ · iddia ❌] ⇒ YAYIN_PLANI §2 · köprü = ilgili video bağlantısı (§7)
A34-e KARAR PENCERESİ — dikey 7. gün · yatay 7 + 28 · kanal içi son 5 medyanı · tek değişken ·
      engaged views < 100 kıyasa girmez                                    [VARSAYIM · eşikler bizim]
      Raporun 72 sa / 14 gün / 30 gün pencereleri ve "5 videoda < %40 → formatı sorgula" eşiği kaynaksız.
      ⇒ YAYIN_PLANI §6.3 · §4.1 ⬜ 90 gün önerisi (sahip onayı bekler)
```

---

## 🛰️ F1 — KARDEŞ DEPODAN DEVRALINAN · film_md · 17.09.2026

> Kaynak: `../film_md/kilavuzlar_ve_sistem_dosyalari/UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md`
> ⛔ **ÇİFTE VARSAYIM:** bu maddeler o depoda da ölçülmedi (kılavuzun kendi §0'ı
> "DÜRÜST KAYIT — bu kılavuzun sınırları" diye açılıyor). Burada VARSAYIMDIR ve ilk
> üretimden sonra ya derse döner ya düşer.
> ⚠️ Ve `KILAVUZ_REHBERI §1.2` gereği film_md'nin tema/novum/karakter kapıları BURADA
> GEÇMEZ; aşağıdakiler yalnız FİZİKSEL ve GÖRSEL maddelerdir.

```
F1-a  ⭐ MARSTA İZ SİLİNİR, AYDA İZ BİRİKİR                        [VARSAYIM]
      Ayda patika hiç silinmez: ezilir, sıkışır, altındaki koyu regolit çıkar ve
      kararır. Marsta patika DOLAR ve yumuşar; her yüzey aynı kızıl okside boyanır.
      ⇒ Yaş, izin keskinliğiyle değil KAYBOLMASIYLA okunur. İkisi TERS çalışır.
      ⇒ THE BORROWED HILL'in ikinci zaman taşıyıcısı budur. ⇒ MALZEME_VE_DOKU §4
F1-b  ÖRTÜ 1,5–2,5 m REGOLİT = GÜNEŞ PATLAMASI SIĞINAĞI MERTEBESİ  [VARSAYIM]
      ⛔ "Dünya atmosferi eşdeğeri" DEĞİLDİR — eşdeğerlik için ~6,5 m gerekir.
      Görsel sonuç: üs narin bir laboratuvar değil, GÖMÜLÜ BİR TÜMSEKTİR.
      ⚠️ P4-g ile birlikte okunur: kalınlık tasarım varsayımıdır, koruma iddiası değil.
F1-c  BASINÇ KABI KÖŞELİ OLAMAZ — iç basınç köşede yırtar. Küre ideal, fırlatma
      kaportası silindiri dayatır: her şey silindir, kapsül ya da torustur. [VARSAYIM]
      ⇒ Kemer kaburgalı tonoz doğru biçimdir. ⇒ YAPI_TIPI_KARTLARI (kart açılacak)
F1-d  ⛔ AY BLOĞU MARS'A YAPIŞTIRILMAZ                              [VARSAYIM · kapı]
      Mars'ta atmosferik saçılma VARDIR: "no atmospheric haze" ve "shadows absolutely
      black" cümleleri orada FİZİK HATASI yazdırır. Gölge zayıf ve yumuşak kenarlıdır,
      dolgu ışığı motivasyonludur — bu MEŞRUDUR, render hatası değildir.
      ⇒ HAVA_VE_ATMOSFER · araç kapısı ⑫ (THE BORROWED HILL günlüğü)
F1-e  ⛔ "fabric · cloth · blanket" PROMPT GÖVDESİNE GİRMEZ         [VARSAYIM]
      Model onları yeryüzü kumaşı sanıp dalgalandırır. Pozitif ve KATI adla yazılır:
      "taut foil-skinned insulation panels" · "a weighted mesh clamped at its edges".
      ⚠️ Dünya filmlerinin "curing blanket" sözcüğü uzay sahasına TAŞINMAZ.
      ⇒ MALZEME_VE_DOKU · PROMPT_SABLONU
```

---

## 🔎 C1 — ÇAPRAZ ANALİZ · 15 film · 12 mercek · 18.09.2026 · dış değerlendirmeyle düzeltildi

> Kaynak: `QA/ARSIV_12_MERCEK/QA_CAPRAZ_ANALIZ/` (01-06) — `QA/ARSIV_12_MERCEK/HAM_RAPORLAR/` altındaki 15 dikey
> filmin ham raporlarının çapraz okuması + aynı gün gelen dış değerlendirme.
> Sayılar: `python3 araclar/capraz_sayim.py` (elle yazılan ilk sürüm 138 dedi,
> matris 132 veriyordu; ② İNŞA 11/15 dedi, 9/15'ti — sayı tek yerde durur).
>
> ⛔ **BU BÖLÜMDEKİ HİÇBİR MADDE ÖLÇÜLMÜŞ DERS DEĞİLDİR.** Çapraz analiz geçmiş
> filmlerin RAPORLARINI okudu, yeni film üretmedi; dış değerlendirme bir okumadır.
> Kaynak sınıfı: ÖLÇÜLMÜŞ QA raporlarının SENTEZİ + dış okuma → hepsi VARSAYIM.
> Her madde ilk pilot üretimden sonra ya numaralı derse döner ya düşer. Kapıdaki
> karşılıkları bu yüzden FIX/INFO, BLOCK değil.
>
> ⭐ Bu kuşağın düzelttiği varsayım: "prompta etiket koyunca sorun çözülür."
> Etiket PLANLAMA kontrolüdür; görüntü ayrı aşamada doğrulanır (QA/00_README §7).

```
C1-a ⭐ BEŞ SORU KARTI — malzeme nerede · taşıyıcı · nereye oturur · ne değişti ·
      ne sabit; prompttan ÖNCE, klip başına                     [VARSAYIM · sentez]
      ② İNŞA 9/15, ⑩ SEBEP 4/5 filmde 4,0 altı; F01 · F05 · F08 aynı sorunun üç yüzü.
      ⇒ kilavuzlar/SAHNE_PLAN_KARTI.md · 00_SAHNE_TABLOSU "BEŞ SORU" sütunu ·
        üretim günlüğü "beş soru ✓" + "baş/orta/son" hücreleri
C1-b ⭐ FİNAL ÜRETİLEBİLİRLİK TESTİ — zincirin ilk halkası: referans + ilk I2I
      halkası + çalışan final, üçü onaylanmadan zincir sürmez   [VARSAYIM · sentez]
      BUILT FROM DUST · DUST YEAR · CLOSING SPAN sonuna kadar üretildi, ⑧ 0,0.
      ⇒ KILAVUZ_REHBERI §8 adım 2b · üretim günlüğü §1b PİLOT ÜÇLÜ · AGENTS kart B 1b
C1-c ⭐ MOTION FOCUS — I2V'de tek ana iş, kendi paragrafında, "from … onto …"
      kalıbı; ≥3 yapı elemanı = birden fazla iş                 [VARSAYIM · dış okuma]
      Google I2V rehberi "prompt for motion only" der; depodaki P2-d ile aynı yön.
      ⇒ PROMPT_SABLONU §2 · prompt_kontrol.py §10e (FIX)
      ⚠️ _blok() I2V'de sona kadar yakalar — ayrı ayıklayıcı, boş satıra kadar
         (165 I2V'de ölçüldü: eski ayıklayıcıyla 128 yanlış geçiş)      [ÖLÇTÜM]
C1-d ⭐ İŞE BAĞLI HAREKET — hareket sayısı değil ana işe hizmet; yükü tutan vinç
      PARKED değil; finalde şantiye hareketi aranmaz; toz/egzoz kanıt değil
                                                                [VARSAYIM · sentez]
      OVER_THE_WALL: ⑪ 9,3 · ⑧ 0,0 · ⑩ 1,3 — araç varlığı ≠ yapıyla bağ.
      ⇒ SANTIYE_HAREKETI §3 not · §4 giriş · §4.7 · PROMPT_SABLONU ACTIVITY ·
        prompt_kontrol.py ACTIVITY >4 → INFO
C1-e ⭐ EŞİT SÜRE TEK BAŞINA KÖTÜ RİTİM DEĞİLDİR — ritmi klip başına FARKLI
      görünür sonuç taşır; sahip dikey süreyi sabit ilan etti  [VARSAYIM · dış okuma]
      ⛔ DERS 13 · 24 · 44 SİLİNMEDİ — ölçülmüş karşı kayıt olarak durur.
      ⇒ KILAVUZ_REHBERI §2.2 karşı kayıt · KURGU_VE_TESLIM §2.4 klip içi denetim ·
        prompt_kontrol.py "süreler eşit" FIX mesajı (beyanlı) · 06 deney adım 3-4 ölçer
C1-f ⭐ ORANSAL KAYMA EŞİĞİ + 3 NİRENGİ + ANA REFERANS — eşik = genişlik × oran;
      genel kayma ile yerel deformasyon ayrılır; her kare öncekiyle VE usta kareyle
                                                                [VARSAYIM · dış okuma]
      "2 px" dört yerde kopyalıydı → tek yer: zincir_kontrol.sh ESIK_KAYMA_ORAN.
      ⚠️ Oran deponun ölçülmüş 2 px @ 1080'inden türedi; dış okumanın "%1"i alınmadı
         — sahip 19.09.2026'da onayladı. MOTION FOCUS kapısı da sahip kararıyla FIX kaldı.
      ⇒ KAMERA_ISTASYONU §7 · zincir_kontrol.sh (ölçek eşitleme · px satırı · 3. argüman)
      ⛔ Betik hatası ÖLÇÜLDÜ: farklı çözünürlükte SSIM boş dönüyor, awk boş dizeyi
         0 sayıp her eşiği ⛔ veriyordu — sebep söylenmeden.               [ÖLÇTÜM]
C1-g ⭐ SAHNEYE ÖZGÜ DIŞLAMA — evrensel negatif blok tek başına engellemez;
      F10 üç ayrı durumdur (uydurma yazı · kaynak izi · filigran)  [VARSAYIM · dış okuma]
      ⇒ KILAVUZ_REHBERI §7 giriş + metin yasağı notu
C1-h ⭐ ÜÇ NOKTA KONTROLÜ — açılış (sorun + başlamış eylem) · kapak (yalnız
      gerçekleşen) · final (çalışan sonuç); kadraj döngüsü var, durum döngüsü
      aranmaz                                                    [VARSAYIM · dış okuma]
      F09 6/14 filmde. Açılış tercihi KURAL DEĞİL, 06 deney adım 1-2'de ölçülür.
      ⇒ MUZIK_VE_KAPAK §5 · KURGU_VE_TESLIM §7
```

---

## 🎯 C2 — İÇERİK OKUMASI · 31 film · ④ TESLİM · 05.10.2026 · ⚠️ değerlendirici yargısı, izleyici verisi değil

> ⛔ **06.10.2026 · ZAYIF KANIT [DERS 64]:** ④'ün 36 koşusundan yalnız 9'u plan görerek koşuldu.
> C2 maddeleri YÖN gösterir, kural değildir; ilk sınavı beş mercekli ❺ TESLİM koşularıdır.

> 31 üretilmiş filmin ④ TESLİM (vaat · kanca · döngü · direnç · final) ve ⑥ GEÇİŞ alt puanları yan
> yana okundu. ⛔ Karıştırıcı: en üst filmlerin hepsi 21.09 sonrası olgun süreçle üretildi; konu ve
> süreç etkisi kısmen iç içe. Her madde `apexait/IZLEYICI_DEFTERI.md` ile doğrulanana kadar VARSAYIM.

```
C2-a  ⭐ FİNALDE BİR ŞEY ÇALIŞIR — en güçlü ayırıcı. ④ 9+ altı filmin altısı işlev anıyla biter
      (ışık yanar · kapı açılır · su durulur); durağan bitmiş yapı ④ 4,4-7,5 (STONE TOWER · GLASS
      WALL · IRON BRIDGE · NARROW LOT). → KILAVUZ_REHBERI §6 İŞLEV ANI satırı · kapı BLOCK (satır varlığı)
C2-b  FİNAL 4 + 4 — 2x paylaşımda 8 sn'lik final 4 sn kalır; olay 0-4, tutuş 4-8 (ekranda 2 sn).
      BACK TO PLUMB bırakma anı 2x'te 1,25 sn kaldı, ④ final 4/10. → §8 adım 9 · kapı BLOCK
C2-c  KANCA = TANIDIK NESNE + ONA NE OLUYOR. Kanca 9-10: çim sökülür · taşkın tehdidi · terk edilmiş
      havuz · mavi kapı. 4-6: boş tarlada hafriyat (EMPTY RIDGE "without clear intent"). Kanca tek
      başına yetmez (STAR DOCK · DARK ROCK kanca 9, ④ 5,5-6,1). → AÇILIŞ NESNESİ satırı
C2-d  DÖNGÜ en zayıf alt puan; kıran üç şey: ödül kadrajdan çıkar (BACK TO WATER 3) · son kare başka
      ışık/mevsim (IRON BRIDGE 5) · araya kart girer. → DÖNGÜ KAFİYESİ satırı
C2-e  KONU: var olanı dönüştürmek/onarmak (④ ≈7,8) > durağan finalli sıfırdan inşa (≈6,2). Uzay yalnız
      tanıdık/gizemli nesneyle tuttu (FIRST GUEST). Oyma iki kez bitiş kartında kimlik kaybetti.
C2-f  ⑥ RİTİM İLGİYİ AÇIKLAMIYOR: BROKEN CLIMB ⑥ 9,9 / ④ 5,1 · DEEP END METRONOM / ④ 9,9. Filmi taşıyan
      kesme ANLAMIN değiştiği kesmedir (rejim G'ye geçiş · çatı kalkar · ışık döner).
NEREYE KILAVUZ_REHBERI §6 İZLEYİCİ KAPISI · §8 adım 9 · prompt_kontrol.py §10f · PROMPT_SABLONU FİNAL KLİBİ ·
       apexait/IZLEYICI_DEFTERI.md (doğrulama) · AGENTS kart A 6a · kart Y 7b
```

```
C2-g  ⭐ İŞ YOĞUNLUĞU — artan şey tek işin etrafındaki EL, klip başına iş SAYISI değil (sahip isteği
      05.10.2026). ⑦ İŞ üst filmler 9,3-10, erken filmler 1,3-3,8 (PARKED). Üç katman: ana işe ≥3 el ·
      klip başına görünür malzeme akışı · arka planda sonraki klibin hazırlığı. C1-d'nin kalabalık
      sınırı 4 → 6. ⛔ "en az üç rejim A" önerisi kalibrasyonda düştü (DEEP END · VANISHING ROOM rejim
      A'sız 9,6+). → SANTIYE_HAREKETI §4.8 · kapı FIX (pilot ölçülene kadar)
C2-h  ⭐ AÇILIŞ DÜZENİ — S0 2x'te ekranda 4 sn; dört vuruş: ① NESNE (tanıdık, ≥1/3 kadraj, "yanlış"
      hâlde) ② DOKUNUŞ (eylem ilk karede başlamış, nesneye dokunur) ③ İPUCU (geleceğin parçası,
      amacı okunmaz) ④ ÖLÇEK (iş büyür, ilk kesmede S1 gözle ileride). MERAK SORUSU künyede ≤6
      kelime; final onu cevaplar. → KILAVUZ_REHBERI §6 AÇILIŞ DÜZENİ · kapı BLOCK (soru satırı ·
      "from the first frame") · FIX (S0 rejim C/G). ⚠️ ④ raporlarından türedi, izleyiciyle ölçülmedi.
```

```
C2-i  ⭐ S0 GERİ ÇEKİLME AÇILIŞI — sahip önerisi (05.10.2026): açılış nesnesinin ayrıntısında yakın
      başla, geri çekil, yapım başlasın. KATMAN 2 (kurgu kırpması) olarak alındı, KATMAN 1 değil: I2V
      HOME'da üretilir, model geri çekilseydi klip G1'e oturmazdı. §3.1 "HOME'da başlar"ın tek istisnası
      S0'ın ilk karesi (filmin başı dikiş değildir); S0 HOME'da BİTER. Büyütme ≤ ölçülen tavan (kaynak
      genişliği / 1080) — araç 1080 veriyorsa YAPILAMAZ. Ease-out, 1x'te ≤ 2,5 sn. SEÇENEK, zorunlu
      değil (her filmde aynı açılış şablona döner). → KAMERA_HAREKETI §4.2 · KILAVUZ_REHBERI §6 AÇILIŞ
      DÜZENİ · kapı (yalnız ✅ VAR planda) · ihrac_kontrol ⑧ · IZLEYICI_DEFTERI S6. ⚠️ ÖLÇÜLMEDİ.
```
