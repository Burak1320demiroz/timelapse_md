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
│   │  ── ikinci kuşak · 08.09.2026 · A5–A8 araştırmasından doğdu ──
│   ├── INSAAT_YONTEMI_KILAVUZU.md   ⭐ ara hâller (%25/%50/%75) · geçici ekipman
│   │                                   · okunabilirlik eşiği 0,5 m · ⑧'in kapısı
│   ├── SANTIYE_HAREKETI_KILAVUZU.md ⭐ SIKIŞTIRMA REJİMİ (A·B·C) · gölge süpürmesi
│   │                                   · sekiz yüzey kanıtı · ⑦'nin kapısı
│   ├── ARAC_KARTLARI.md             ⛔ BOŞ AÇILIR · kutu seti · sahne tavanı ·
│   │                                   SEKİZ soruluk ölçüm · negatifin yeri
│   ├── KURGU_VE_TESLIM_KILAVUZU.md  ⭐ kırpma bütçesi · TOP-N kesme kanıtı ·
│   │                                   yedi ölçümlük yayın öncesi QC
│   └── DERSLER.md                   ölçülmüş dersler + devralınan varsayımlar
│                                     ⭐ DERS 35-44 · altıncı film (THE DUST YEAR)
│                                       yedisinin kapısı prompt_kontrol.py §10c'de
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
├── QA/                              🔍 SEKİZ MERCEK · ÜRETİMDEN SONRA
│   ├── 00_README.md                 ⭐ klasör rehberi: mod sistemi · çalıştırma
│   ├── 00_INDEX.md                  ⭐ PROJEDEKİ TEK SAYAÇ + tamlık matrisi
│   ├── 1_KARE_QA.md                 ① sabitlik + temizlik · mod V (doküman YOK)
│   ├── 2_INSA_QA.md                 ② aynı bina + inşa mantığı · mod D
│   ├── 3_ZAMAN_QA.md                ③ güneş saati + akış · mod V · TAM KURGU
│   ├── 4_TESLIM_QA.md               ④ vaat/bedel/kurgu · mod D
│   ├── 5_DEVAMLILIK_QA.md           ⑤ dikiş denetimi · dünya · mod V
│   ├── 6_GECIS_QA.md                ⑥ kesmenin kendisi · ritim · mod D
│   ├── 7_IS_QA.md                   ⑦ şantiye hiç duruyor mu · büyümenin sebebi · mod V
│   ├── 8_YONTEM_QA.md               ⑧ her parça sıfırdan, yapımı görünerek · mod D
│   ├── T1..T8                       skor tabloları
│   ├── RAPORLAR/                    film başına kalıcı kayıt (ajanın özeti)
│   └── HAM_RAPORLAR/                modelin ham çıktısı ⛔ DOKUNULMAZ
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
│   ├── SONUCLAR/                    ham bot çıktısı ⛔ DOKUNULMAZ
│   └── SONUCLAR/A5-A8_DENETIM.md    ⭐ dört raporun doğruluk denetimi:
│         üç sayı yeniden hesaplandı ve düştü · iki ffmpeg komudu koşmadı ·
│         bir eşik kör çıktı. ⛔ Rapordan doğrudan inen SAYI yoktur.
│   ⛔ Araştırma bulgusu DERS DEĞİLDİR. En fazla gerekçeli varsayımdır ve
│      DERSLER.md'nin DEVRALINAN bölümüne A<n>-x koduyla girer.
│
└── araclar/
    ├── sayac.sh                     sayıları dosya sisteminden hesaplar
    ├── prompt_kontrol.py            ÜRETİMDEN ÖNCE koşan kapı · çıkış 2 = BLOCK
    ├── zincir_kontrol.sh            ⭐ ÜRETİM ARASI kapı · her kareden sonra
    ├── kare_al.sh                   ① ve ⑤ için kare grabları
    ├── qa_paket.sh                  ⭐ QA KOŞU PAKETİ · sekiz mercek · günlük kapısı [DERS 28-29]
    └── kesme_kontrol.sh             ⛔ YAYIN ÖNCESİ · kurgu SÜRE sütununa uydu mu [DERS 31]
```

**Format kartı, yapı/saha kartları, negatif çekirdek → hepsi `KILAVUZ_REHBERI.md`
ve komşularında. Burada tekrarlanmaz.**

---

# 2. GÖREV KARTLARI

## 🏗️ A — YENİ FİLM YAZACAĞIM

```
0. IZGARA             kart G — 10 sahne (varsayılan) mı, 5 sahne mi.
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
6. TESLİM YAPISI      ⛔ sahne bloğu + KAPAK KARTI 5,0 sn AYRI beyan edilir.
                      Beyansız kart QA'yı çökertir [DERS 4].
7. KLİP SÜRESİ        ⛔ ÖLÇ: ffprobe ile test klibi. Izgarayı ondan yaz.
                      ⭐ Süreler KUTULUDUR [A7-a]. Plana ARAÇ KUTU SETİ satırı
                        yazılır ve sahne tavanı = (en büyük kutu − 1,00 sn)
                        aşılmaz [ARAC_KARTLARI §2]. Aşılırsa prompt kapısı BLOCK.
8. PROMPTLAR          PROMPT_SABLONU iskeletiyle · ⭐ 2N+1 prompt:
                      N+1 GÖRSEL (G0…GN · sonuncusu USTA KARE, ayrı bölümde)
                      + N I2V · ⛔ T2V YOK [KILAVUZ_REHBERI §2.7]
                      ⛔ Her I2V'nin İKİ UCU da birebir cümleyle kilitlenir;
                        kapı ikisini de arar · blok ETİKETLERİ birebir [DERS 20]
                      ⭐ AT THIS STAGE'e INSAAT_YONTEMI §5'ten ara hâl cümlesi
                      ⭐ TIME RATE'e SIKIŞTIRMA REJİMİ (A·B·C) beyanı [A6-a]
                      ⭐ ACTIVITY'ye iki hareket eden + bir yüzey kanıtı [A6-d]
9. MÜZİK + KAPAK      MUZIK_VE_KAPAK — 120 BPM (3 ölçü/sahne) · kapak SON
                      sahnenin usta karesinden türer ve ⭐ İNGİLİZCE BAŞLIK taşır
10. PAKETLEME         ⛔ başlık/açıklama/hashtag/yorum İNGİLİZCE
11. QA_SPEC           kilit listesi + ⛔ FİNAL KARE KANITI satırı
12. PROMPT KAPISI     python3 araclar/prompt_kontrol.py <dosya>

DOSYA:  dikey_shorts/<PROJE>/<PROJE>_DIKEY_TIMELAPSE.md
```

## 🤝 G — IZGARA SEÇİMİ (10 sahne mi, 5 sahne mi)

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
        ② KAMERA HAREKET EDİYOR MU? (>2 px ise bu araçla üretilmez)
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
2d. ⛔ YEDİ ÖLÇÜM  KURGU_VE_TESLIM_KILAVUZU §6 — biçim · süre · kesme · LUFS ·
      açılış penceresi · flicker · final kare + kapak. Yedisinin çıktısı
      üretim günlüğü §4'e YAZILIR; yazılmamışsa yayın yok.
3. 120 PX TESTİ hem kapağa hem S0'ın 0. karesine (sips -Z 120)
4. İHRAÇ        1440p+ · BT.709 · 48 kHz · −14 LUFS · −1,0 dBTP
5. PAKETLEME    başlık/açıklama/hashtag/sabit yorum + ⛔ GERÇEKLİK BEYANI
                → doldurulmuş kanal şablonu: apexait/youtube/PAKETLEME_SABLONU.md
6. ⛔ AI BEYANI ÜÇ PLATFORMDA DA, elle, kendi beyanınla:
                YouTube  Studio → Ayrıntılar → "Altered content"
                TikTok   paylaşım ekranı → AIGC anahtarı
                Instagram gelişmiş ayarlar → AI/dijital içerik
                Açıklamadaki gerçeklik beyanı bunun YERİNE GEÇMEZ; ayrı yüzey.
                apexait/youtube/POLITIKA_VE_RISK.md §2 · CAPRAZ_YAYIN §2
7. ⛔ QA        → kart Q. Dört mercek YÜKLEMEDEN ÖNCE koşulur.
8. ÇAPRAZ       apexait/CAPRAZ_YAYIN.md §6 — tek master · filigran · C2PA
9. YÜKLEME      ÜÇ HESAP, aynı gün, native (CAPRAZ_YAYIN §4 sırası):
                apexait/youtube/PAKETLEME_SABLONU.md   §5
                apexait/instagram/PAKETLEME_SABLONU.md §5
                apexait/tiktok/PAKETLEME_SABLONU.md    §5
```

## 🔍 Q — FİLM ÜRETİLDİ, QA KOŞULACAK

```
⛔ ÖN KOŞUL: film ÜRETİLMİŞ olmalı. Rubrik promptu değil VİDEOYU eleştirir;
   plana koşulan bir rubrik, prompt kapısının işini tekrar eder.

1. MAKİNE       ⭐ bash araclar/qa_paket.sh <film_klasoru> <teslim.mp4> [kapak]
                → kare_al.sh'ı koşar + QA/KOSU/<FILM>/ altına sekiz paket:
                  girdi satırı + eklenecek dosyalar + rubrik [DERS 29].
                ⛔ Üretim günlüğü yoksa DURUR [DERS 28].
                (kare_al.sh tek başına: bash araclar/kare_al.sh <teslim.mp4> 10)
2. ① KARE       rubrik + tam kurgu + kareler     ⛔ DOKÜMAN VERME (mod V)
3. ③ ZAMAN      rubrik + TAM KURGU               ⛔ DOKÜMAN VERME · tek klip GEÇERSİZ
4. ⑤ DEVAMLILIK rubrik + tam kurgu + kareler     ⛔ DOKÜMAN VERME (mod V)
4b. ⑦ İŞ       rubrik + tam kurgu + kareler     ⛔ DOKÜMAN VERME (mod V)
5. ② İNŞA       rubrik + tam kurgu + QA_SPEC     (mod D)
6. ④ TESLİM     rubrik + tam kurgu + plan + kapak (mod D)
7. ⑥ GEÇİŞ      rubrik + tam kurgu SESLİ + plan  (mod D)
8. ⑧ YÖNTEM     rubrik + tam kurgu + QA_SPEC     (mod D)

⛔ 0. GİRDİ SATIRI — HER KOŞUDAN ÖNCE, TEK SATIR [DERS 27]
      Koşuya başlamadan yaz ve raporun başına yapıştır:
         "verilen girdiler: <dosya adları>"
      ⛔ bash araclar/kare_al.sh <teslim.mp4> <n> ① ve ⑤'ten ÖNCE koşulur.
         DÖRT filmde de koşulmadı.
      ⭐ Ölçüldü [DERS 27]: MOUNTAIN DOOR'da QA_SPEC üretimden ÖNCE hazırdı
         ve mercekler yine belgesiz koştu. Eksik olan BELGE değil, YORDAM.

⭐ SIRA ÖNEMLİDİR: doküman körlüğü isteyen dördü (① · ③ · ⑤ · ⑦) ÖNCE koşulur.
   Önce SPEC'i okuyup sonra "mod V" koşmak, körlüğü zaten kaybetmiş olmaktır.
⛔ ASGARİ SET: ① + ② + ⑤. Bu üçü koşulmadan film YAYINLANMAZ.
Her koşuda BAŞKA HİÇBİR ŞEY verilmez: medya + rubrik + (mod D ise) tek belge.
```

## 📥 R — QA RAPORU GELDİ

```
1. HAM ÇIKTI     QA/HAM_RAPORLAR/<FILM>_<MERCEK>_HAM.md olarak KAYDET
                 ⛔ düzenleme, kısaltma, özetleme YOK — bu kanıttır
2. UNVERIFIABLE  rapor künyeyi dolduramadıysa PUANLAMA. Eksiği tamamla, TEKRARLA.
3. VERDICT ÖNCE  skorlardan ÖNCE hüküm satırını oku. Hüküm ile ortalama
                 çelişiyorsa HÜKÜM KAZANIR ve kararı o belirler.
4. SKOR SATIRI   QA/T<n>_*.md tablosuna satır ekle (mod V ise Ⓥ işaretle)
5. DOKÜMAN       ① ve ③'ün "QUESTIONS FOR THE DOCUMENT" listesini plandan
                 CEVAPLA. ⭐ Rubriğin ikinci yarısı budur.
6. ZAMAN TAHMİNİ ③'ün "TIME READ FROM THE FILM ALONE" satırını planın zaman
                 yayıyla karşılaştır. Uzaksa film kendi süresini anlatamıyor —
                 hiçbir kategori bunu yakalamaz.
6a. ⭐ ZİNCİR ÖNCE [P2-k]: ⑤ SAME WORLD ve ⑧ MADE hükmü tutmadıysa diğer
                 merceklerin skoru YORUMLANMAZ; film "zincir koşulmadı" diye
                 kapanır. Kamera çözüldü (DERS 11); sıradaki tek soru dünya
                 ve yapı kalıtımıdır.
6b. KANIT NESNESİ ⑤'in "THE OBJECT THAT PROVES IT IS THE SAME PLACE" satırını
                 oku. NONE FOUND ise film aynı yerde geçmiyor demektir ve bu,
                 skor ortalaması ne olursa olsun yeniden üretim sebebidir.
6c. RİTİM        ⑥'nın METRONOM hükmü geldiyse çözüm PROMPTTA değil PLANDA:
                 aşama merdiveninin SÜRE sütunu eşitlenmiş demektir [DERS 13].
6d. MOD DENETİMİ ② ④ ⑥ ⑧ raporunun ilk satırı "RUN INCOMPLETE" diyorsa skoru
                 tabloya YAZMA — satırı "belgesiz koşuldu — TEKRARLANACAK"
                 diye aç ve koşuyu belgeyle TEKRARLA [DERS 17].
6e. İŞ VE YÖNTEM  ⑦'nin "THE GROWTH NOBODY MADE" ve ⑧'in "THE FIRST PIECE THAT
                 APPEARED" satırlarını oku. NONE değilse: ⑦ için o zaman damgasının
                 sahnesi, ⑧ için o parçanın yapıldığı sahne yeniden üretilir —
                 ortalama ne olursa olsun. Parça adı T8 tablosuna yazılır.
7. KALICI KAYIT  QA/RAPORLAR/<FILM>.md (skor · hüküm · en ağır üç bulgu ·
                 karar: hangi sahne yeniden üretilecek, hangi kusur kabul edildi)
8. TAMLIK        QA/00_INDEX.md matrisini ve sayımı güncelle
9. YENİ DERS     yeni bir bozulma çıktıysa kart D
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
5. VARSAYIM     kabul edilen bulgu kilavuzlar/DERSLER.md'nin DEVRALINAN
                bölümüne A<n>-x koduyla girer — numaralı derse DEĞİL.
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

```
· DERSLER.md'deki maddelerin TAMAMI devralınmış varsayımdır; bu depoda
  hiçbiri ölçülmedi. İlk üretimden sonra ya derse dönüşürler ya düşerler.
· prompt_kontrol.py yalnız METİN denetler; anlam denetlemez. Kapıdan geçen
  bir prompt iyi bir prompt değildir, yalnız biçimsel olarak eksiksizdir.
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

# başlıksız / SPEC'siz film klasörü var mı — çıktı boş olmalı
for d in dikey_shorts/*/; do
  ls "$d" | grep -q "_DIKEY_TIMELAPSE.md" || echo "EKSİK PLAN: $d"
  ls "$d" | grep -q "_QA_SPEC.md"         || echo "EKSİK SPEC: $d"
done

# prompt kapısı tüm filmlerde
for f in dikey_shorts/*/*_DIKEY_TIMELAPSE.md; do python3 araclar/prompt_kontrol.py "$f"; done

# ham raporu olup skor tablosunda satırı olmayan film (işlenmemiş rapor)
ls QA/HAM_RAPORLAR/*_HAM.md 2>/dev/null | sed 's|.*/||; s|_[A-Z]*_HAM\.md||' | sort -u
```
