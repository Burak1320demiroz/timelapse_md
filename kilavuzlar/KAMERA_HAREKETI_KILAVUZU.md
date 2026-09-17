# 🎬 KAMERA HAREKETİ KILAVUZU — üç katman

> **Bu depoda kamera yoktur.** Slider, moco kafası, encoder, ND filtre, enstantane,
> IBIS — hiçbiri burada bir karar değildir, çünkü hiçbiri burada bir cihaz değildir.
> Bu kılavuz, "kamera hareketi" istendiğinde o isteğin **hangi katmanda**
> karşılanacağını söyler ve her katmanın bedelini yazar.
>
> Kaynak: dördüncü kuşak araştırma (A13–A18 · 17.09.2026) ·
> denetim `arastirma/SONUCLAR/A13-A18_DENETIM.md`
> ⚠️ **Bu kuşaktan kılavuza tek bir SAYI indi** (§3'ün tavan formülü) ve o da
> rapordan değil, denetimde bu makinede hesaplandı. Geri kalan her madde
> MEKANİZMADIR ve `DERSLER.md` DÖRDÜNCÜ KUŞAK bölümünde **VARSAYIM** olarak durur.

---

# 0. 🚪 ÖNCE BU — "kamera hareketi" istendiğinde sorulacak tek soru

```
İSTENEN NEDİR?
  ⓐ kadrajın İÇİNDEKİ bir şey hareket etsin         → KATMAN 3 · §7 · BEDELSİZ
  ⓑ izleyicinin dikkati bir ayrıntıya gitsin          → KATMAN 2 · §3 · BEDELİ VAR
  ⓒ derinlik/paralaks hissi doğsun                    → ⛔ HİÇBİR KATMAN VEREMEZ · §2.3
  ⓓ "gerçek çekim gibi dursun"                        → KATMAN 3 · §7 ④ (bulut gölgesi)

⛔ En sık yapılan hata ⓐ'yı ⓑ sanmaktır. THE DARK ROCK'ta beğenilen hareketin
   tamamı ⓐ idi ve o filmde kamera HİÇ hareket etmez (16.09.2026 · GİZLİ VAHA notu).
   İstek "kamera hareketi" diye gelir; incelenince çoğu zaman kadraj içi harekettir.
```

---

# 1. 🧱 ÜÇ KATMAN

```
KATMAN 1 · ÜRETİM        I2V klibinin kendisi              ⛔ SABİT — DEĞİŞMEDİ
KATMAN 2 · KURGU         teslim zaman çizgisindeki kırpma  ⭐ 16.09.2026'da AÇILDI
KATMAN 3 · KADRAJ İÇİ    sabit kadrajın içindeki olaylar   ✅ her zaman serbest
```

## 1.1 ⛔ KATMAN 1 NEDEN KAPALI KALIYOR — dört ölçüm

```
① CAMERA LOCK 0/10      beş klipte yavaş push-in belirdi; istenmemişti  [DERS 6 · 11]
② SIX SEPARATE SHOTS    dört istasyon + hareket → film "altı ayrı görüntü" okundu
③ DERS 52               istasyon değişen kesmede yapı yüzdesi sıçradı  [P2-e ÖLÇÜLDÜ]
④ DERS 56               bir PARÇAYA yazılan hareket fiili YAPIYA sıçradı
```

Ve dördüncü kuşak bunu dışarıdan **doğruluyor**: kesintisiz kamera hareketi,
timelapse'in kendi zamansal ivmesiyle çakışınca doku bozulması (motion drift)
üretir [A14-c]. Yani katman 1'i açmak, aracın en zayıf olduğu iki şeyi —
geometri sadakati ve hareket — aynı klipte birden istemektir.

```
⛔ KATMAN 1'İN KİLİDİ NEGATİF ÇEKİRDEKTEDİR ve oradan kaldırılmaz:
   KILAVUZ_REHBERI §7 · "The camera is bolted down and does not move, drift,
   breathe or reframe." Ölçülebilir çapa cümlesi de orada [DERS 11].
⛔ Tek istisna DENEME olarak yazılır, ana pakete girmez ve ayrı değerlendirilir
   (örnek: THE NARROW GORGE §KURGU 4 · "FİZİKSEL HAREKET DENEMESİ").
```

---

# 2. 🗺️ ON SEKİZ HAREKET — hangisi bu boruhattında ÜRETİLEBİLİR

A13 ve A18'in saydığı hareketlerin tamamı, bu depoda ne olduklarıyla birlikte.
**Sol sütun rapordan, sağ sütun bu depodan.**

| Hareket | Bu depoda | Gerekçe |
|---|:-:|---|
| Locked-off (sabit) | ✅ **FORMAT** | `KILAVUZ_REHBERI §1.2` — timelapse'in tanımı |
| Push-in / Pull-out | ⚠️ **yalnız KURGU** | fiziksel kamera yok; kırpmayla yapılır → §3 |
| İleri-geri simetrik (HOME'a dönüş) | ⚠️ **yalnız KURGU** | anlatı değeri en yüksek olan; §3'ün konusu |
| Yanal slider (tracking) | ⛔ | paralaks ister; kırpma paralaks üretmez → §2.3 |
| Pan (yatay çevrinme) | ⛔ | 9:16'da özne kadrajdan çıkar [A18-f]; ayrıca katman 1 |
| Tilt (dikey çevrinme) | ⛔ | katman 1 · keystone `KAMERA_ISTASYONU §3 ③` |
| Pedestal / crane (dikey) | ⛔ | katman 1 |
| Orbit / arc (yörünge) | ⛔ | istasyon değişimi demektir [DERS 52] |
| Parallax (slider + ters pan) | ⛔ | iki eksenli; ikisi de katman 1 |
| Top-down (kuş bakışı) | ⚠️ **KARE olarak** | sabit hover kare olur, HAREKET olmaz [`KAMERA_ISTASYONU §5`] |
| Macro-to-wide | ⛔ | odak motoru + fiziksel geri çekilme |
| Hyperlapse | ⛔ | fiziksel yürüyüş aksı |
| Motorlu motion-control | ⛔ | cihaz yok |
| Dijital zoom / keyframe | ✅ **KURGU** | ⭐ bu kuşağın tek yeni imkânı → §3 |
| Speed ramp | ⛔ | tek zaman oranı kuralı [DERS 15 · 50] |
| Match cut / aynı kadraja dönüş | ✅ **ZATEN VAR** | G0 ↔ GN çifti; §5 |
| Kusursuz loop | ⚠️ **KISMEN** | kadraj döngüsü olur, DURUM döngüsü olmaz → §5 |
| Kadraj içi kinetik | ✅ **SERBEST** | §7 — dokuz araç |

## 2.3 ⛔ KIRPMA PARALAKS ÜRETMEZ — bu cümle vaadin sınırıdır

A13 §15'in kendi ifadesiyle: dijital yakınlaşmada **sıfır paralaks** vardır;
ön plan ve arka plan aynı oranda büyür, optik perspektif değişmez.

```
⇒ KURGU YAKINLAŞMASI DERİNLİK VAAT EDEMEZ. Yaptığı tek şey DİKKAT YÖNETİMİDİR:
  izleyiciye "şimdi şuraya bak" der. Derinlik isteniyorsa çözüm kamerada değil
  KOMPOZİSYONDADIR (ön plan nesnesi · üç mesafe · `PERSPEKTIF_VE_OLCEK`).
⛔ Plana "derinlik/paralaks artar" yazılmaz. THE NARROW GORGE'da yalnız
  FİZİKSEL HAREKET DENEMESİ satırında yazılıdır ve o satır ana pakete girmez.
```

---

# 3. 🔍 KURGU YAKINLAŞMASI — HOME PAKETİ

> İlk uygulaması: `dikey_shorts/THE_NARROW_GORGE/` §KURGU (16.09.2026 · sahip kararı).
> Bu bölüm o paketin **genel hâlidir**; film kendi tablosunu kendi dosyasında tutar.

## 3.1 HOME — tanım

```
HOME = planın BÜTÜN yüzdelerini üreten geniş kompozisyon.
       (yükseklik · D_eksen · odak · bearing · tilt · roll — altısı da
        `KAMERA_ISTASYONU §2`nin satırından gelir, değişmez)

⛔ N+1 GÖRSEL KARENİN HEPSİ HOME'DA ÜRETİLİR. Yakınlaşma bir ÜRETİM kararı
   değil, bir KURGU kararıdır; anahtar kareler üretilmiş kareyi kırpar.
⛔ HER SAHNE HOME'DA BAŞLAR VE HOME'DA BİTER. Kesmeye asla yakınlaşmış hâlde
   girilmez — yoksa ⑤ DEVAMLILIK iki ayrı istasyon okur [DERS 52].
```

## 3.2 ⛔ ALTI KURAL

```
① KAMERA GERİ DÖNER, İNŞAAT DÖNMEZ
   Kadraj HOME'a dönerken sahnedeki iş GERİ ALINMAZ. Dönüş için klip TERS
   OYNATILMAZ; yalnız ölçek ve konum anahtar kareleriyle yapılır.
   KAPI: klibin son karesi ↔ G(n+1) · zincir_kontrol.sh · çıkış 2 = klip ATILIR.

② ÇAPA HOME'DA VE SAHNE SINIRINDA AYNI PİKSELDEDİR
   Yakınlaşmada çapanın yer değiştirmesi BEKLENENDİR. Ama yakın kadrajda da
   EN AZ BİR çapa görünür kalır; görünmüyorsa izleyici ikinci bir istasyon okur.
   KAPI: HOME karelerinde çapa kayması ≤ 4 px [DERS 25'in el kontrolüyle birlikte].

③ AYNI BÜYÜTME VE AYNI HIZ EĞRİSİ İKİ KEZ KULLANILMAZ
   Tekrarlanan yakınlaşma, kesme metronomunun yakınlaşma hâlidir [DERS 13 · 44].

④ SABİT SAHNE, YAKINLAŞAN SAHNENİN NEFESİDİR
   Yakınlaşma her sahneye konmaz. Sabit kalan sahneler ritmin yarısıdır;
   hepsi hareket ederse hiçbiri hareket etmiyor demektir.

⑤ IŞIK VEYA MEVSİM DEĞİŞEN SAHNEDE YAKINLAŞMA YOK
   İki değişken aynı klipte yarışır; taşıyıcı okunmaz olur [DERS 14 · 52].

⑥ GEÇİŞ SESİ HER YAKINLAŞMAYA KONMAZ
   Konursa hareket bir efekt olur, bir anlatı değil [`MUZIK_VE_KAPAK §1`].

⭐ ⑦ HEDEF, ANLATININ NESNESİDİR — YAPININ TEPESİ DEĞİL [P3-f · 17.09.2026]
   Yakınlaşma, geniş planda fark edilmeyecek kadar küçük olan ama filmin
   BEDELİNİ ya da ÖDÜLÜNÜ taşıyan şeye gider. Kaybolan iz ile onun yerini alan
   şey AYNI YAKIN KOMPOZİSYONDA görünmelidir; sığmıyorsa YERLEŞİM düzeltilir,
   ikinci bir hareket eklenmez. Önce zemine sonra tepeye savrulan iki ayrı
   hareket finali dağıtır.
   ⚠️ VE YAKIN KADRAJDA §DEĞİŞMEZLER'İN YÜZDELERİ GEÇERSİZDİR: o sayılar
   HOME'a aittir. Yakın kadrajın kendi çapası ayrıca adlandırılır.
```

## 3.3 ⛔ ÇÖZÜNÜRLÜK KAPISI — bu kuşaktan inen TEK sayı

```
        YAKINLAŞMA TAVANI = kaynak genişliği / teslim genişliği

ÖLÇTÜM (17.09.2026 · A13-A18_DENETIM §1.5) — 1080 × 1920 teslimde:
   kaynak 1080 × 1920  →  1,00×   (yakınlaşma YOK)
   kaynak 1674 × 2976  →  1,55×
   kaynak 1836 × 3264  →  1,70×
   kaynak 2160 × 3840  →  2,00×

⛔ BÜYÜTME (upscale) BU TAVANI SAĞLAMAZ. Tavan aracın GERÇEKTEN verdiği
   piksel sayısından okunur — ffprobe ile, üretim günlüğüne yazılarak.
⛔ Araç tavanı vermiyorsa TABLO YENİDEN YAZILIR, prompt zorlanmaz.
⛔ Kırpma dikdörtgeni kaynağın DIŞINA taşamaz: yakınlaşmanın hedefi kadrajın
   kenarına yakınsa üstte/yanda boş kenar oluşur.
```

⭐ A13 ">%120 pikselleşir" der; bu **yanlış değil, eksik koşulludur** — kaynak
ile teslim aynı olduğunda doğrudur. Bizde kaynak teslimden büyük olabildiği için
eşik sabit bir yüzde değil, bir ORANDIR.

## 3.4 Plana yazılacak tablo — sütunları

```
| S | fiil | kamera (1,0× → n× → 1,0×) | anahtar kareler (klip içi sn) |
    yakında görülen | HOME'a dönünce kazanılan |

⛔ YAKINLAŞMA HEDEFİNİN x/y PİKSELİ G KARELERİ ÜRETİLMEDEN YAZILMAZ — ölçülmemiştir.
   Yazılabilecek olan hedef NESNEDİR ("savak dudağı + kapak"), koordinat değil.
```

---

# 4. ⏱️ İLK SANİYE — kanca

```
A14 · A15 · A16 üçü de aynı şeyi söylüyor: karar ilk 0–1 saniyede veriliyor.
BİZDE bunun karşılığı ŞUDUR:

⛔ DEĞİŞİM İLK SANİYE DOLMADAN BAŞLAR — ve G0'DA HENÜZ OLMAMIŞTIR.
   G0 "bozulmamış hâli" tanıtır; bozan eylem klibin İÇİNDE, ilk saniyede olur.
   Açılış ne boş bir bekleyiş ne de bitmiş bir olaydır: araç temas hâlinde
   hazırdır (kova kenara dayalı · kırıcı tool'u kayaya değmiş) ve ilk kırılma
   0,3–0,8 sn arasında gerçekleşir.

⭐ DÜZELTME — 17.09.2026 [P3-a]: bu madde 16.09.2026'da "G0'da değişim ZATEN
   BAŞLAMIŞ olmalıdır" diye yazılmıştı ve YANLIŞTI. Uzman okuması ölçtü: ilk
   yara G0'da açıksa açılışın EN DEĞERLİ OLAYI klibin dışında kalır ve izleyici
   neyin bozulduğunu göremez, çünkü bozulmamış hâli hiç görmemiştir.
   Kural: izleyici BÜTÜN ŞEKLİ ve ONU BOZAN EYLEMİ aynı klipte görür.
⚠️ THE NARROW GORGE bu düzeltmeden ÖNCE yazıldı ve G0'ında yara açıktır;
   ölçüm sırası geldiğinde bu fark okunur.
```

## 4.1 ⚠️ TERS AÇILIŞ — üçüncü kez önerildi, üçüncü kez alınmadı

```
ÖNERİ      "finali ilk 0,5–1 sn'de flaş kare olarak göster" [A14 · A15]
KARŞI KAYIT DERS 3 (ters açılış ölçüldü) · A1-b (vaat KAPAĞA taşındı) · P2-l ①
KARAR      Kapak SONDA kalır. Değişmedi.

⭐ AMA ARTIK ASİMETRİ VAR: üç dış kaynak öneriyor, bizim karşı kaydımız TEK
   filmden geliyor. Bu ölçülmeyi hak eder ve ölçümü ŞUDUR:
   aynı filmin iki teslimi — biri kartsız, biri ilk 0,8 sn'de USTA KAREDEN
   alınmış tek flaş kareyle — ve yalnız TUTUNMA karşılaştırılır.
   ⛔ Denenene kadar plana yazılmaz.
```

---

# 5. 🔁 LOOP — kadraj döngüsü olur, DURUM döngüsü olmaz

```
A14 · A18  "son kare ilk kareye bağlanırsa tekrar izleme artar"
BİZDE      G0 ile GN zaten AYNI KADRAJDIR (HOME) — kadraj döngüsü HAZIR.

⛔ AMA DURUM DÖNGÜSÜ İMKÂNSIZDIR VE İSTENMEZ: bu filmler bir şeyin
   İNŞA EDİLDİĞİNİ gösterir. Son kare ilk kareye "bağlanırsa" yapı sökülmüş
   olur — filmin vaadini geri alır [KILAVUZ_REHBERI §6 · BEDEL].
⇒ Bizim loop'umuz GÖRSEL DEĞİL KAVRAMSALDIR: aynı kadraj, başka bir dünya.
   Tekrar izlemeyi çağıran şey dikişin görünmezliği değil, İKİ UCUN FARKIDIR.
⭐ Bu yüzden kapak da G0/GN ikilisinden türetilir [DERS 30 · `MUZIK_VE_KAPAK §2.2`].
```

---

# 6. 🥁 RİTİM — kesme eklemeden olay eklemek

```
DIŞARIDAN   Shorts için önerilen açı değişimi 2,5–3,5 sn [A14] · ortalama plan
            süresi 1,5–3,5 sn [A18]
BİZDE       dikey ızgara 6,0 sn · son iki film 8,0 sn
```

⛔ Bandı takip etmek ızgarayı ikiye katlamaktır: **her kesme yeni bir anahtar
kare ve yeni bir klip ister** (§2.7 · N sahne = N+1 kare). Bedeli film başına
iki katı üretim ve iki katı zincir riskidir.

```
⭐ ÇÖZÜM: KESME SIKLIĞINI DEĞİL, OLAY SIKLIĞINI ARTIR.
   Bir sahne içinde izleyicinin saydığı "olay" sayısını üç kaynak üretir:

   ① SÜRE VARYANSI          `KILAVUZ_REHBERI §2.2` — kesme aralığı eşit olmaz
   ② ÜÇ VURUŞ               klip içi "First … Then … Finally" (2 · 4 · 2 sn)
   ③ ⭐ KURGU YAKINLAŞMASI   §3 — KESME OLMADAN bir vuruş ekler

   ③'ün değeri budur ve tek başına yakınlaşmayı meşru kılan şey de budur:
   ızgarayı bozmadan, zinciri uzatmadan, klip başına bir olay daha verir.
⚠️ Ama DERS 44 uyarıyor: kesme ANLAM taşımıyorsa süre boşa gider. Aynısı
   yakınlaşma için de geçerlidir — anlamı olmayan yakınlaşma bir efekttir.
```

---

# 7. 🎭 KATMAN 3 — KADRAJ İÇİ KİNETİK (bedelsiz katman)

Sabit kadrajda hareket üreten, ölçülmüş araçlar. Tam liste ve örnekleri:
`dikey_shorts/THE_HIDDEN_OASIS/…_DIKEY_TIMELAPSE.md` §KİNETİK PAKET (dokuz araç).

```
① KENAR GEÇİŞİ     her sahnede bir şey kadrajı bir kenardan kat eder
② DİKEY SÜPÜRME    9:16'nın ekseninde inen/çıkan tek bir şey (su · kabin · kalıp)
③ GÖLGE SÜPÜRMESİ  zamanın taşıyıcısı · `SANTIYE_HAREKETI` · [DERS 32 · 47]
④ GÖK OLAYI        bulut gölgesinin kadrajı geçmesi — "kamera kaydı" hissine
                   en yakın MEŞRU araç
⑤ ÜÇ VURUŞ         klip içi ritim
⑥ ÖDÜLÜN GECİKMESİ ödül son klibin son çeyreğinde · öncesinde fiili anılmaz [DERS 56]
⑦ YÜZEY SINIRI     ıslak/kuru · temiz/kirli sınırının yüzeyi süpürmesi
⑧ İZ BIRAKAN ARAÇ  palet/lastik izi birikir, sonra süpürülür
⑨ EKİP LEKESİ      insan silinmez, İZ olarak vardır (rejim B)
```

⭐ **Bu katman hiçbir kapıyı zorlamaz.** Kamera kilidi kapalı kalır, çözünürlük
şartı doğmaz, ⑤ DEVAMLILIK riski yoktur. "Kamera hareketi" isteği geldiğinde
**önce burası denenir**, §3 sonra gelir.

---

# 8. 📐 KADRAJ GEOMETRİSİ — sayılar başka dosyada

```
GÜVENLİ ALAN (9:16)   `KAMERA_ISTASYONU §6` — dört kenar, piksel piksel
KADRAJ YÜZDESİ        `KAMERA_ISTASYONU §3` — formül · D_kenar ve D_eksen [DERS 38]
KOMPOZİSYON CÜMLESİ   `PERSPEKTIF_VE_OLCEK` — kesir/piksel çapası
KAPAK VE PAKETLEME    `MUZIK_VE_KAPAK §2 · §3` ve §4 (dördüncü kuşak eki)
```

```
⚠️ A14'ün "900 × 1400 evrensel güvenli alan" rakamı DENETİMDE DÜŞTÜ:
   kendi marj tablosuyla çelişiyor (en kötü hâl 940 × 979). Bizim zarfımız
   zaten daha dar ve DEĞİŞMEDİ [A13-A18_DENETIM §1.3].
```

---

# 9. 🚦 KAPILAR — yakınlaşma varsa bunlar ölçülür

```
ARAÇ KAPISI      ⑨ ÇÖZÜNÜRLÜK: ffprobe ile kaynak genişliği · tavan §3.3'ten
                 hesaplanır ve üretim günlüğüne YAZILIR [`ARAC_KARTLARI §4`]
ÜRETİM GÜNLÜĞÜ   her yakınlaşan klip için: büyütme · anahtar kare saniyeleri ·
                 HOME dönüşünde çapa kayması (px) · son kare ↔ G(n+1) zincir
QA_SPEC          "KURGU KAPISI" bölümü: çözünürlük · HOME dönüşü · ileri durum ·
                 yakın kadrajda çapa · kırpma sınırı · ritim
QA MERCEĞİ       ① KARE ve ⑤ DEVAMLILIK bu hareketi "istasyon değişimi" sayarsa
                 hüküm BEKLENEN kabul edilir ve rapora "sahip kararı" diye geçer —
                 yeniden üretim sebebi DEĞİLDİR [THE NARROW GORGE · 16.09.2026]
```

---

# 10. ⚠️ BU KILAVUZUN STATÜSÜ

```
⛔ KATMAN 2 (kurgu yakınlaşması) ÖLÇÜLMEMİŞTİR.
   Deponun iki yazılı maddesini açıkça geçersiz kılar — `KILAVUZ_REHBERI §1.2`
   ("format kimliği sabit kameradır") ve `DERSLER P2-l ②` ("crop push-in →
   alınmadı"). Karar proje sahibinindir (16.09.2026) ve ölçümü THE NARROW
   GORGE'dur. Film üretilip QA'dan geçtikten sonra bu bölüm ya numaralı bir
   derse döner ya düşer.

⛔ KATMAN 1 ÜÇ KEZ ÖLÇÜLDÜ VE ÜÇÜNDE DE DÜŞTÜ. Bu kılavuz onu açmaz.
✅ KATMAN 3 ölçülmüş araçlardan oluşur ve serbesttir.

⭐ KARŞILAŞTIRMA BORCU: THE NARROW GORGE yayınlandıktan sonra, sabit kadrajlı
   filmlerle tutunma açısından karşılaştırılır ve sonuç DERSLER.md'ye yazılır.
   Bu kılavuzun varlık sebebi o ölçümdür; ölçüm gelene kadar her satırı VARSAYIMDIR.
```
