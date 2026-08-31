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
① YAPI TİPİ?    kule · konut · köprü · baraj · stadyum · yol/tünel · liman · türbin
                                                    → YAPI_TIPI_KARTLARI.md
② SAHA?         şehir içi · kırsal · kıyı · dağ/eğim · kar · çöl
                                                    → SAHA_VE_IKLIM_KARTLARI.md
③ ZAMAN YAYI?   toplam kaç ay/yıl 60 saniyeye sığıyor + hangi mevsimler geçiyor
                                                    → ZAMAN_VE_ISIK_KILAVUZU.md
④ KAMERA?       hibrit (4 ana + 2 detay) · saf tek istasyon · çok istasyon
                                                    → KAMERA_ISTASYONU_KILAVUZU.md
```

### Her filmde okunacaklar (değişmez)

```
□ §3  DEĞİŞMEZLER TABLOSU     (bu dosyada — her promptta birebir tekrarlanır)
□ §4  AŞAMA MERDİVENİ         (bu dosyada — plan bundan doğar)
□ §5  GÜNEŞ SAATİ KİLİDİ      (bu dosyada)
□ §6  VAAT / DİRENÇ / BEDEL   (bu dosyada — konsept kapısı, geçmezse plan yazılmaz)
□ §7  NEGATİF ÇEKİRDEK        (bu dosyada — tam metin, her prompta yapıştırılır)
□ §9  BİLİNEN TUZAKLAR        (bu dosyada)
□ PROMPT_SABLONU.md           (görsel + I2V + T2V iskeleti)
□ DERSLER.md                  (ölçülmüş hatalar)
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

## 2.1 ⛔ TESLİM YAPISI — her planda beyan edilir

```
SAHNE BLOĞU    10 sahne × 6,0 sn = 60,0 sn    ← QA merceklerinin konusu
KAPAK KARTI     1 kart × 5,0 sn =  5,0 sn     ← konusu DEĞİL, ayrı denetlenir
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

Süreler eşit olmaz ama **ölçüye oturur** — müzik hizası korunur:

```
120 BPM → ölçü 2,0 sn → izinli süreler  4 · 6 · 8 · 10
160 BPM → ölçü 1,5 sn → izinli süreler  4,5 · 6 · 7,5 · 9

KURAL   en az İKİ sahne KISA · en az BİR sahne UZUN
        doruk sahnesi kendinden ÖNCEKİYLE hız KONTRASTI yapar
        toplam 60,0 sn SABİT kalır

ÖRNEK (160 BPM):  6 · 4,5 · 6 · 4,5 · 6 · 7,5 · 6 · 4,5 · 6 · 9  = 60,0
                  ↑ kısa kısa                ↑ nefes        ↑ doruk uzun
```

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
İMAJ:        10  (+1 kapak = 11)
VİDEO:       10 klip × (I2V birincil · T2V yedek) = 20 prompt
ÜRETİM:      image → image-to-video   ⭐ I2V BİRİNCİL
             ⛔ ve sahneler arası ZİNCİRLİ: her görsel bir öncekinin
                karesinden türetilir (§8 ters inşa) [DERS 5]
ŞABLON:      TIMELAPSE_SISTEM_PROMPTU.md
KAPI:        araclar/prompt_kontrol.py (üretimden ÖNCE)
             + FİNAL KARE KANITI (§8 adım 9)
             + QA dört mercek (yayından ÖNCE · QA/00_README)

DİL:         Belgeler TÜRKÇE · üretim promptları İngilizce
             ⛔ BAŞLIK, AÇIKLAMA, HASHTAG ve KAPAK METNİ İNGİLİZCEDİR.
                Yalnız QA raporları ve depo belgeleri Türkçedir.

KRİTİK FARK: Sahneler arası değişen tek şey ZAMANDIR. Kamera, arka plan,
             yapı tasarımı ve kadraj on sahnede de birebir aynıdır.

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

### Üç zorunlu satır

```
① KANIT NESNESİ:  her sahnede ilerlemeyi ekranda KANITLAYAN tek nesne.
   "bina büyüdü" bir kanıt değildir — kaç kat, hangi hizada, neye göre.
   Kanıt nesnesi arka plan çapalarından birine göre ölçülür:
   "the slab edge now sits level with the roof ridge of the brick block."

② LOOP SATIRI:  S5'in son karesi ile S0'ın ilk karesi AYNI kadrajdır.
   Boş arsa → bitmiş kule, aynı çerçeve. Viral ödeme burasıdır.

③ SÖKÜM SATIRI: vinç/iskele/çit hangi sahnede kurulur, hangi sahnede
   sökülür. Yazılmazsa model onları rastgele yok eder ve devamlılık ölür.
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
```

Ve üç kabul testi (`film_md` novum kapısının timelapse hâli):

```
① TEK KARE TESTİ    Tek donmuş karede izleyici (a) NE yapıldığını ve
                    (b) sürecin NERESİNDE olunduğunu 1 saniyede söyleyebiliyor mu?
② KİNETİK BAĞIMSIZLIK  Değişim, 10 saniyelik SABİT bir planın içinde
                    metin/anlatıcı olmadan görülebiliyor mu?
③ BAŞLIK ŞEMASI    Vaat ≤5 kelimelik bir başlığa çevrilebiliyor mu?

Üçü de ✅ değilse KONSEPT REDDEDİLİR, klasör açılmaz.
```

---

# 7. 🚫 NEGATİF ÇEKİRDEK (tam metin — her prompta yapıştır)

Saha ve yapı kartlarından gelen maddeler bunun ÜSTÜNE eklenir.

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
no floating structure, no floor slab without support beneath it, no crane hanging
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
> dağ/çöl gecesi   → "stars render as short concentric trails"
> ```
> Film yazılırken çekirdek madde madde okunur; saha kartıyla çelişen madde
> o filmde TERSİNE çevrilir ve gerekçesi plana yazılır.

> ⛔ **METİN YASAĞININ KAPSAMI, YASAĞIN KENDİSİ KADAR ÖNEMLİDİR.**
> `film_md` Ders 138: yasak cümlesi kısaltılırken öznesi daralıyor.
> *"The crane carries no logo"* vinci korur; tabelayı, yeleği, konteyneri
> ve çiti korumaz. Şantiye, bu depodaki en yoğun metin yüzeyidir —
> yasak YÜZEY YÜZEY sayılır, tek nesneye bağlanmaz.

---

# 8. 🏭 ÜRETİM AKIŞI — ⭐ TERS İNŞA

> Bu akışın 2. ve 3. adımı bu deponun en yüksek kaldıraçlı kararıdır.
> Altı kareyi ayrı ayrı üretirsen altı farklı bina ve altı farklı arka plan
> alırsın; geriye inerken saha, arka plan, çerçeve ve tasarım zaten kilitlidir.

```
0. KONSEPT KAPISI   §6 — VAAT/DİRENÇ/BEDEL + üç test. Geçmezse plan yok.

1. PLAN             §3 Değişmezler + §4 Aşama Merdiveni + §5 güneş saati
                    doldurulur. Sahne haritası bu üç tablodan TÜRER,
                    tersi olmaz.

2. ⭐ USTA KARE      S9 ÜRETİLİR — tamamlanmış yapı, ANA istasyondan.
                    ⛔ KAPI: bina ikna edici değilse, arka plan çapaları
                       okunmuyorsa ya da kadraj güvenli alana oturmuyorsa
                       DİĞER BEŞ SAHNE ÜRETİLMEZ. Usta kare filmin tapusudur.

3. ⛔ GERİYE İNŞA — BU BİR ÖNERİ DEĞİL, KAPIDIR [DERS 5]
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

4. PROMPT           18 prompt yazılır (6 görsel + 6 I2V + 6 T2V yedek).
                    ⛔ Her prompt tek başına çalışır — belge atfı yasak.

5. PROMPT KAPISI    python3 araclar/prompt_kontrol.py <dosya>
                    uzunluk · yasak kelime · negatif çekirdek imzası ·
                    "Scene N of 6" tutarlılığı · güneş azimut satırı ·
                    değişmezler bloğunun birebir tekrarı.
                    Çıkış kodu 2 = BLOCK → üretme.

6. VİDEO            Onaylanmış her görselden I2V. Onaylanmamış görselden
                    video üretme, boşa gider.

7. KURGU            6 klip · 0 kesme içi · sert kesme aralarda.
                    Kesme = zaman sıçraması; geçiş efekti YOK.

8. MÜZİK + KAPAK    MUZIK_VE_KAPAK.md — müzik tek parça, BPM ızgaraya oturur;
                    kapak metinsiz + 120 px posta pulu testi.

9. ⛔ FİNAL KARE KANITI   Teslimden önce tek komut:
                       ffmpeg -ss <saniye> -i teslim.mp4 -frames:v 1 kanit.jpg
                    SPEC'te yazan "S5 · 0:5X · ekranda GÖRÜLMESİ gereken şey"
                    o karede gerçekten var mı? Yoksa FİLM TESLİM EDİLMEMİŞTİR
                    — klip sayısı ve süre tutsa bile.
                    (film_md D141: kapı klip sayar, vuruş saymaz. Üretilmiş iki
                     dikey filmin ikisinde de kaybolan şey FİNALDİ.)

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
**dağınıktır.** Negatif çekirdekteki `working construction site` cümlesi
pozitif hâliyle her prompt gövdesinde de tekrarlanır: çamur, lastik izi, su
birikintisi, istiflenmiş malzeme, branda, kesme artığı.

### 9.2 ⛔ BİNA DEĞİŞİYOR
En sık ve en öldürücü bozulma. İlacı üç katmanlıdır ve üçü birden gerekir:
(a) YAPI BIBLE birebir tekrarı · (b) ters inşa (§8) · (c) `no redesign,
same column grid, same bay spacing, same footprint` cümlesi.

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

---

# 10. 🔧 BAKIM NOTLARI

```
· Bu dosya ADRES verir + üç tabloyu tutar. Başka hiçbir kılavuzun içeriği
  buraya kopyalanmaz; kopyalanırsa ikisi ayrışır ve hangisinin doğru olduğu
  kaybolur.
· Yeni kural bir DERSTEN doğar, fikirden değil. Ders = ölçülmüş bozulma
  (hangi film, hangi saniye, ne oldu). Ölçüm yoksa "OKUMA" diye işaretlenir.
· film_md'nin 40 kılavuzu bu deponun hedefi DEĞİLDİR. O depo kendi teşhisinde
  hacmin çekirdek arızayı engellemediğini ölçtü. Dosya ancak bir ders
  taşıyorsa açılır.
```
