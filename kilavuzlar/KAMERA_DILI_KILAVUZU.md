# 🎯 KAMERA DİLİ KILAVUZU — istasyon kurulmadan ÖNCE sorulan sorular

> `KAMERA_ISTASYONU` kadrajı **hesaplar** (altı alan · formül · güvenli alan).
> `KAMERA_HAREKETI` "hareket" isteğinin **hangi katmanda** karşılanacağını söyler.
> Bu kılavuz ikisinden ÖNCE gelir: **hangi değişimi göstereceksin, o değişim hangi
> bakıştan okunur, kamera o bakışa ne kadar tilt ve yükseklikle oturur.** Bu soru
> cevaplanmadan §3'ün formülüne girilecek h · D · tilt yoktur.
>
> Kaynak: A19 · 20.09.2026 · proje sahibinin köke bıraktığı dış rapor
> (`arastirma/SONUCLAR/A19_KAMERA_DILI_HAM.md`) · denetim `A19_DENETIM.md`.
> ⭐ Dört kuşakta en temiz kaynakça (11'in 10'u çekildi, hepsi iddiaya ait) — ama
> **hiçbir kaynak "hangi açı daha çok izlenir" sorusunu ölçmüyor** ve rapor bunu kendisi
> yazıyor. Buradaki her madde MEKANİZMADIR; `DERSLER.md` A19 bölümünde VARSAYIM olarak
> durur. Rapordan inen YENİ SAYI: sıfır. İnen iki FORMÜL (§3 · §5) bu makinede hesaplandı.

---

# 0. 🚪 ÖNCE BU — karar cümlesi

Raporun tek cümlelik şablonu, bizim konsept kapısı (`KILAVUZ_REHBERI §6`) ile
Değişmezler tablosu (`§3`) arasındaki boşluğu dolduruyor. VAAT/DİRENÇ/BEDEL neyin
anlatılacağını, Değişmezler kameranın nerede olduğunu söyler; **ikisinin arasında
"bu değişim hangi bakıştan görünür" sorusu yazılı değildi.**

```
KARAR CÜMLESİ — plana §DEĞİŞMEZLER'in hemen ÜSTÜNE, tek paragraf:

   İzleyici [DEĞİŞEN ÖZELLİK] farkını görecek.            ← VAAT'in görünür boyutu
   [SABİT REFERANS] aynı kalacak.                          ← üç nirengi + "aynı yer" nesnesi
   Kamera [BAKIŞ AİLESİ · yükseklik · tilt] üzerinden bakacak. ← §2 tablosundan
   Hareket [YOK / yalnız kurgu §KURGU] — çünkü [YENİ BİLGİ].  ← KAMERA_HAREKETI §0

⛔ Cümle dolmadan h · D · tilt SEÇİLMEZ. Sayı formülden çıkar [KAMERA_ISTASYONU §3];
   ama formüle girecek TILT ve YÜKSEKLİK AİLESİ buradan gelir.
⭐ "Sinematik olsun" · "drone açısı" · "makro" bir bakış tarifi DEĞİLDİR [rapor §3]:
   drone 15 m'de çapraz da bakar, 80 m'de tepeden de; "makro" bir açı değil bir
   büyütmedir. Tarif ALTI ayrı karardır ve bizde şöyle karşılanır:

   rapor §3 kararı        bizde                                   nerede
   ─────────────────      ──────────────────────────────────      ─────────────────────
   kamera türü            SANAL — tek satır, tartışılmaz          KAMERA_HAREKETI giriş
   lens                   24 mm ana · 35 · 50 kilit               KAMERA_ISTASYONU §5
   konum ve açı           altı alan (h · D · bearing · tilt · roll) KAMERA_ISTASYONU §2
   çekim ölçeği           HOME = genel plan · detay = orta plan    §4 bu kılavuz
   kamera hareketi        katman 1 SABİT · 2 kurgu · 3 kadraj içi KAMERA_HAREKETI §1
   zaman yöntemi          SENTETİK timelapse · rejim = pencere    §5 bu kılavuz
```

---

# 1. ⛔ ÇELİŞENLER ÖNCE — üç madde, üçü de değişmedi

Tam gerekçe `A19_DENETIM.md §2`. Burada yalnız karar:

```
① HAREKET SEÇENEK DEĞİL   rapor slider · orbit · dolly out · pedestal reçeteleri veriyor.
                          Katman 1 üç kez ölçüldü, üçünde düştü [KAMERA_HAREKETI §1.1].
                          Raporun "önce sabit sürümü dene · tek hareket" uyarısı bizim
                          kuralımızın gevşek hâlidir; ⛔ olan kalır.
② NEGATİFTE "NO" KALIR    Veo dokümanı "no/don't yerine öğe adı" der (çekildi ✅). Bizim
                          imzalar ölçülmüş kapıdır [DERS 35]; gövde zaten POZİTİF [DERS 11].
                          → §8: araç kartına SORU olarak iner, kural olarak değil.
③ TERS AÇILIŞ YOK         "sonucu önden göster" dördüncü kez önerildi. DERS 3 ölçtü;
                          kapak sonda kalır [KAMERA_HAREKETI §4.1]. Ölçüm borcu aynı.
```

---

# 2. 🗺️ AÇI ATLASI — bakış aileleri, bizim dille

Raporun §4'ü sinema sözlüğüdür; **bu depoda karşılığı tilt ve yüksekliktir.** Bir bakış
ailesi seçmek, §3'ün formülüne girecek iki sayının BANDINI seçmektir.

## 2.1 Dört bakış ailesi

| Aile | Kamera–konu ilişkisi | Ne gösterir | Bizde | Bedeli |
|---|---|---|---|---|
| **HİZA** (konu hizası) | tilt 0° · h ≈ anlatının yüksekliği | profil · YÜKSEKLİK · dikeyler dik | ⭐ KULE ailesi varsayılanı: `KAMERA_ISTASYONU §3` ③ "tilt verme, kamerayı yükselt" | zemindeki düzen okunmaz; ufuk %50'ye kilitlenir |
| **ALÇAK** | kamera konunun altında, yukarı bakar | yükselme · büyüklük | ⚠️ yok — keystone + zemin işi gizler; 9:16'da gök boşa gider | çalışma alanı kaybolur |
| **YÜKSEK ÇAPRAZ** | yukarıdan eğimli (tilt −15…−45°) | yüzey alanı + hacim BİRLİKTE | ⭐ AŞAĞI BAKIŞ ailesi: SWALLOWED BUS (−40°) · BACK TO WATER (−22°) · HIDDEN OASIS kalıbı | keystone; ufuk yukarı kayar (§3) — gök bandı daralır |
| **TEPEDEN** (90°) | optik eksen zemine dik | plan · sınır · yüzey düzeni | ⚠️ yalnız KARE olarak, sabit hover [`KAMERA_ISTASYONU §5` · A18-d] | düşey derinlik SIFIR — çukur, kat, su seviyesi okunmaz |

```
⭐ RAPORUN EN İŞE YARAR CÜMLESİ: "Havuz dolumunda tepeden açı suyun kapladığı ALANI,
   yan açı SEVİYEYİ, çapraz açı İKİSİNİ birlikte gösterir. Seçim, videonun sorduğu
   soruya bağlıdır." — BACK TO WATER'ın h=12 · tilt −22° kararının gerekçesi budur ve
   plan yazılırken bu cümle yoktu. Artık var: §2.3 tablosu.
```

## 2.2 Nesneye göre yön — hangi yüz kadrajda

| Rapor §4B | En iyi gösterdiği | Bizde nerede | Not |
|---|---|---|---|
| Cepheden | simetri · aynı yüzeyin değişimi | kule/cephe filmleri · bearing yüzeye dik | derinlik azalır; ön plan referansı şart [PERSPEKTIF §2] |
| Üç çeyrek çapraz | ön yüz + yan yüz · alan + derinlik | ⭐ varsayılan bearing: yapının köşesine 30–60° | ön plandaki nesne arkayı örtebilir → güvenli alan |
| Tam yandan | yükseklik · SU SEVİYESİ · profil · katman | baraj kreti · havuz suyu · köprü açıklığı | geniş sahanın öbür yanı görünmez |
| Camdan kesit | kök · dolum · çökelme | ⛔ yok — şantiyede kesit yüzeyi yoktur | — |
| Ufku AŞAĞIDA bırakan | gök gelişimi | ⛔ gök taşıyıcı değil, gölge taşıyıcı [DERS 15 · 47] | zemin dönüşümü küçülür |
| Ufku YUKARIDA bırakan | zemin · gölge · su akışı | ⭐ aşağı bakış ailesi — ufuk §3 ile hesaplanır | gök bandı kapak başlığına ancak yeter |
| Eğik ufuk | tasarlanmış dengesizlik | ⛔ roll 0 — altı alanın biri, kapı arar | "bina eğiliyor mu" sorusu ölçütü bozar |
| Araç/nesneye bağlı | platform sabit, dünya akar | ⛔ bizde istasyon DÜNYAYA sabit; "gemiye sabit" ayrı formattır (rapor §2A) | prompta "tripod bolted to the vessel" YAZILMAZ |

## 2.3 ⭐ DEĞİŞİM BOYUTU → BAKIŞ AİLESİ — bu kılavuzun tablosu

Konsept kapısındaki VAAT'in **görünür boyutu** hangisi? Tek cevap ver; iki boyut
gerekiyorsa çapraz seç ve bedelini yaz.

| Değişen şey | Görünür boyut | Bakış ailesi | tilt bandı | h · D ilişkisi | Yapı kartı örneği |
|---|---|---|---|---|---|
| kat · kule · direk · silo yükselir | YÜKSEKLİK | HİZA | 0° | `§3` ②: D = f·(H−h)/11,5 · taç %82 | kule · türbin · kayar kalıp silo (§9b) |
| açıklık kapanır · kret yükselir | YÜKSEKLİK + UZUNLUK | HİZA / hafif çapraz | 0…−10° | eksen yapının ORTA açıklığına | köprü · baraj |
| çukur açılır/kapanır · yol yüzeyi | ALAN + DERİNLİK | YÜKSEK ÇAPRAZ | −25…−45° | h ≥ D/2 · çukur tabanı kadrajın alt yarısında | çökük/altyapı (§6b) · yol |
| su seviyesi · dolum · boşalma | SEVİYE + ALAN | YÜKSEK ÇAPRAZ (yan bileşenli) | −15…−30° | bearing su kenarına açılı; duvar çizgisi referans | kuru havuz (kart adayı) · liman · baraj gölü |
| yüzey temizlenir · kaplanır · döşenir | ALAN (sınır ilerler) | YÜKSEK ÇAPRAZ ya da TEPEDEN kare | −30…−60° | sınırın ilerleme YÖNÜ kadrajın uzun eksenine (dikey) | stadyum çimi · plaza · çatı |
| hacim çıkar (konut · villa · stadyum) | ALAN + YÜKSEKLİK | ÜÇ ÇEYREK ÇAPRAZ, hafif yüksek | −5…−15° | köşeye 45° bearing · iki cephe | konut · villa · stadyum |

```
⛔ TEK KURAL: tilt SEÇİLMEZ, aileden gelir; sayısı §3'ün formülüyle KADRAJ KİLİTLERİNE
   çevrilir ve Değişmezler'e yazılır. "−30° güzel duruyor" bir gerekçe değildir.
⭐ İKİ BOYUT İSTENİYORSA çapraz seçilir ve BEDEL yazılır: yükseklik hizada, alan
   tepeden daha iyi okunurdu; çapraz ikisini de "yeterince" verir. Hangi boyutun
   kanıt nesnesi olduğu (§4 üç zorunlu satır ①) o bedeli sınırlar.
```

---

# 3. 📐 TİLTLİ KADRAJ FORMÜLÜ — `KAMERA_ISTASYONU §3`'ün genel hâli

`§3`'ün formülü **tilt 0° için kesindir** (f·tanθ'nın tilt 0 hâli) ve §3 ③ "tilt verme,
kamerayı yükselt" der. Bu kural KULE ailesi için doğrudur ve KALIR. Ama aşağı bakış
ailesinde tilt kaçınılmazdır ve depoda üç film tiltle yazıldı; üçü de açıyı kareye
**orantılı** dağıtan yaklaşık bir formül kullandı. Rektilineer lens açıyı **tanjantla**
dağıtır. Fark 24 mm'de en çok 2,9 puan (`A19_DENETIM §1.4`) — planı düşürmez, ama
yöntem burada düzelir.

```
DİKEY YÜZDE (alttan · tilt aşağı POZİTİF · f mm · 36 mm kare yüksekliği)

      yüzde(y, d) = 50 + f · tan( tilt − atan( (h − y) / d ) ) / 0,36

   h = kamera yüksekliği (m)   y = noktanın yerden yüksekliği (m)
   d = kameradan noktaya YATAY mesafe (m)   [geniş sahada d_eksen · DERS 38]

   tilt 0  →  50 + f·(y−h)/(0,36·d)  = §3 formülü  ✅ (özel hâl)

ÜÇ SONUÇ
   ① UFUK yalnız tilt'e bağlıdır:   ufuk% = 50 + f · tan(tilt) / 0,36
      24 mm: tilt 22° → %76,9 · tilt 30° → %88,5 · tilt 36,9° → %100 (ufuk kadrajdan çıkar)
      ⇒ GÖK BANDI = 100 − ufuk%. Kapak başlığı gök bandına yazılacaksa
        [MUZIK_VE_KAPAK §2.3] tilt bu bantla sınırlıdır.
   ② OPTİK EKSENİN VURDUĞU ZEMİN NOKTASI tam %50'dedir:  d_50 = h / tan(tilt)
      (lensten bağımsız · h 12 · tilt 22° → 29,7 m). Kanıt nesnesi bu mesafenin ÖTESİNDEYSE
      kadrajın üst yarısına, BERİSİNDEYSE alt yarısına düşer.
   ③ KEYSTONE tilt ile BÜYÜR: dikey çizgiler tan(tilt) oranında yakınsar. Aşağı bakış
      ailesinde bu kabul edilen bedeldir; kule ailesinde değildir (§3 ③).

YATAY YÜZDE (soldan · 24 mm kare genişliği · bearing'e göre yatay açı φ)
      yüzde_x = 50 + f · tan(φ) / 0,24        φ = atan(Δx / d) − (bakış çizgisiyle fark)
   ⚠️ Tiltli kadrajda yatay formül kenara doğru ±1–2 puan sapar (üç boyutlu döndürme
      ihmal edilir). Kilit değerleri usta karede ÖLÇÜLÜR; formül plan içindir.

ÇALIŞILMIŞ KONTROL — raporun kendi örneği (§4A: 28 mm · h 3 · d 8 · tilt 30°)
   ufuk %94,9 · 8 m'deki zemin %62,9 → gök yalnız üst %5. Yükselen yapıya YER YOK;
   yol onarımı ve küçük şantiye için doğru, kule için yanlış. Rapor da onu "yol
   onarımı, oda, küçük şantiye" için önermişti ✅.
```

```
⛔ KURAL: Değişmezler tablosunda tilt ≠ 0 ise KADRAJ KİLİTLERİ BU FORMÜLLE hesaplanır
   ve tablonun başına "tilt formülü: KAMERA_DILI §3" yazılır. §3'ün formülü tilt ≠ 0'da
   KULLANILMAZ; doğrusal açı formülü de kullanılmaz.
   KALDIRDIĞI: "göz kararı tilt" ve iki farklı yaklaşık formülün film başına
   yeniden türetilmesi. Karşılığı: üç filmin kilit tabloları ölçüldüğünde formül
   ya doğrulanır ya düşer (üretim günlüğü §1 usta kare ölçümü).
```

---

# 4. 🔭 LENS VE ÖLÇEK — lens bir sonuçtur

```
RAPORUN SIRASI  önce mesafe → sonra görüş alanı → sonra netlik derinliği.
                "Lens adını başa yazıp geometriyi ona uydurma."
BİZDE           aynı sıra zaten kural: sayı SEÇİLMEZ, formülden ÇIKAR [KAMERA_ISTASYONU §3]
                ve lens KİLİTLİDİR: 24 ana · 35 çukur · 50 detay [§5]. Raporun 24–35 mm
                "şantiye/yol" bandı bizim 24'ü kapsıyor; yeni sayı yok.

İKİ OPTİK GERÇEK — prompta değil PLANA yazılır (model optik hesap yapmaz)
   · "Tele sıkıştırmaz, KONUM sıkıştırır": aynı yerden lens değişince yalnız görüş alanı
     daralır; kadrajı eşitlemek için geri çekilince ön/arka oranı değişir.
     ⇒ Detay istasyonu 50 mm ile "yakın" DEĞİL, aynı D'den DAR bakıştır; ölçek cümlesi
       buna göre yazılır [PERSPEKTIF_VE_OLCEK §4].
   · "Zoom ≠ dolly": dolly paralaks üretir, zoom üretmez. Kurgu yakınlaşması zoom'dur
     ⇒ derinlik vaat edemez [A13-b · KAMERA_HAREKETI §2.3]. Rapor aynı şeyi söylüyor ✅.

NETLİK DERİNLİĞİ  bizde f/8 sabit [KAMERA_ISTASYONU §4.1]; "büyümenin ilerleyeceği bölge
                  netlik alanından çıkmasın" kuralı bizde otomatik sağlanır (tek istasyon,
                  bütün kadraj net). ⛔ "makro sinematik" bulanıklık YOK — 9.1 render çukuru.

ÇEKİM ÖLÇEĞİ — rapor §4C'nin beş ölçeği bizde iki istasyona iner
   çok geniş plan   ⛔ telefonda ana değişim seçilemez → 120 px testi düşer
   GENEL PLAN       ⭐ HOME — yapının tamamı + son hâlinin sığacağı boşluk (§3 ② taç %82)
   orta plan        detay istasyonu (≤2 sn ek · aşama değil · çapa görünür) [KAMERA_ISTASYONU §1]
   yakın plan       yalnız kurgu yakınlaşması (katman 2 · tavan §3.3) — üretimde yok
   makro            ⛔ yok

⭐ "SON BOYUTA YER BIRAK" (rapor §2C · §17): bizde bunun sayısı §3 ②'dir — taç %82'ye
   oturacak D. Bitki tepeden kesiliyor = kule tacı üst sekizliğe giriyor; aynı arıza,
   aynı formül.
⭐ "120 PX KONTROLÜ ilk ve son kareye": bizde var — kapak + S0'ın 0. karesi [kart Y adım 3 ·
   MUZIK_VE_KAPAK §2.5 · §5 üç nokta]. Rapor bunu "platform ölçütü değil, okunurluk
   kontrolü" diye adlandırıyor; bizim kullanımımız da odur.
```

---

# 5. ⏱️ ZAMAN YÖNTEMİ VE SIKIŞTIRMA KATSAYISI

Raporun §3'ü dört zaman yöntemi ayırır: klasik timelapse (fotoğraf dizisi) ·
hızlandırılmış video · hyperlapse · **sentetik timelapse.** Bizimki dördüncüsüdür ve
rapor onun için tek şart yazar: *"aynı görsel ilkeler kullanılabilir; fizik ve süreklilik
ayrıca denetlenir."* Bu depo o denetimin kendisidir (kapı · zincir · sekiz mercek).

```
KATSAYI — raporun §9 formülü, bizim rejim tablomuzu BAĞIMSIZ üretiyor [A19_DENETIM §1.3]

      δ  = pencere / (L × f)        sn/kare  (pencere = rejimin gerçek zaman penceresi)
      oran = δ × f  = pencere / L   (kaç kat hızlı)

   SANTIYE_HAREKETI §1'in A · B · C satırları bu formülden aynen çıkar (6 s · 30 fps).
   ⚠️ 8,0 s ızgarada sayılar değişir (oran = pencere / 8); SANTIYE §1 tablosu 6 s içindir.
      Sayı oraya EKLENMEZ — planı yazan formülü koşar ve kare tablosuna yazar.

⭐ "İKİ AYRI ZAMAN YAZ" (rapor §8A): "10 sn çıktı boyunca … sahnede 2 saatlik işlem
   sıkıştırılır." Bizde bu TIME RATE rejim beyanıdır [A6-a · SANTIYE §2] ve zaten
   kapıdadır. Rapor bunu KAMERA hareketini de zamana bağlamak için önerir — bizde
   kamera hareketi olmadığı için cümlenin yarısı yeter.

⭐ "DÜZENSİZ ÖRNEKLEME" (rapor §9): mesai saatleri kayıt → tek sabit hız yok, gölge ve
   mevsim atlar. Bizde bunun karşılığı §2.7 ①: zaman yalnız KLİP İÇİNDE akar, kesme
   zaman taşımaz; her klip kendi penceresini kendi gölgesiyle gösterir. Rapor arızayı
   tarif ediyor, biz onu yapısal olarak kapatmışız.

⭐ MOTION STREAK'İN OPTİK GEREKÇESİ (rapor §10): "akıcı hareket için pozlama ≈ intervalin
   yarısı." Rejim B'de δ = 30–40 s → 15–20 s pozlama → insan İZ olur, araç bulanır.
   DERS 47 · 50 · A13-d'nin dışarıdan dördüncü doğrulaması. Rejim A'da δ ≈ 2,5–3,3 s →
   1–2 s pozlama → insan tanınır ama yumuşak. Rejim G'de δ = 0,033 s → iz YOK.
   ⇒ SANTIYE §1'in "insan" sütunu bu hesabın sonucudur; prompta yazılan "soft motion
     streaks" bir üslup değil, pozlamanın kendisidir.
```

---

# 6. 🎬 HAREKET — sözlük başka dosyada, GEREKÇE CÜMLESİ burada

Raporun §8 sözlüğü (12 hareket) `KAMERA_HAREKETI §2`'de 18 hareket olarak zaten
sınıflandırılmış; tekrar edilmez. Bu kılavuza inen tek şey raporun **gerekçe kuralıdır:**

```
⭐ HER HAREKETİN GEREKÇESİ TEK CÜMLEDE: "Kamera geri çekilir; temizlenen küçük parçanın
   büyük bir avlunun parçası olduğu anlaşılır." — "daha epik durur" gerekçe DEĞİLDİR.
BİZDE   yalnız katman 2 (kurgu yakınlaşması) için geçerli ve tablosu zaten bu sütunu
        taşıyor: "yakında görülen · HOME'a dönünce kazanılan" [KAMERA_HAREKETI §3.4].
        ⛔ İki sütun da dolmayan yakınlaşma plana YAZILMAZ — §3.2 ⑦'nin aynısı.
⭐ "TEK HAREKET KURALI" (rapor): kısa klipte tek ana hareket. Bizde katman 2'de
   §3.2 ③–④ (aynı büyütme iki kez yok · sabit sahne nefestir) bunu zaten sağlıyor.
⭐ "YAKLAŞ VE GERİ ÇEKİL yalnızca başlangıca dönüyorsa döngüden ibarettir": HOME paketi
   (1,0× → n× → 1,0×) tam bu risktir; §3.2 ⑦ hedefi anlatının nesnesine bağlayarak
   cevaplar. Rapor "her videoda otomatik kullanma" der — §3.2 ④ ile aynı.
⛔ "FİNALDE GERİ ÇEKİLME" (rapor §15A alternatif · §19 A2/B2/C2): A18-e — final usta
   karedir, en geniş hâldir; geri çekilecek yer yoktur. Alınmadı, dördüncü kez.
```

---

# 7. ✍️ PROMPT DİLİ — raporun kayıt kartı bizim bloklarımızdır

## 7.1 Kayıt kartı ↔ blok eşlemesi

| Rapor §14 alanı | Bizde blok | Kapı |
|---|---|---|
| Başlangıç durumu | AT THIS STAGE (Gn) + kare tablosu | ✅ prompt_kontrol |
| Bitiş durumu — "tek kalıcı ilerleme" | AT THIS STAGE (Gn+1) + BEŞ SORU ④ [SAHNE_PLAN_KARTI] | ✅ §10e |
| Değişmeyecekler | DEĞİŞMEZLER + YAPI BIBLE + BEŞ SORU ⑤ | ✅ |
| Kamera | Camera: altı alan | ✅ |
| Lens görünümü | lens kilidi (24/35/50) — prompta "24 mm" yazılmaz, metre yazılır | ✅ |
| Hareket | NEGATIVE ilk katman + I2V "does not move at any point" | ✅ |
| Zaman — çıktı ve süreç ayrı | TIME RATE rejim beyanı | ✅ |
| Fizik — nereden gelir, nereye gider | PHYSICS + MOTION FOCUS "from … onto" | ✅ |
| Işık | LIGHTING + güneş satırı (az/el) | ✅ |
| Geçiş — sonraki klibe aktarılan referans | ⭐ İKİ UÇ: Gn+1 hem hedef hem sonraki ilk kare [§2.7] | ✅ |

⭐ Rapor bizim iskeletimizi bilmeden aynı on alanı yazmış. Fark: bizde her alan bir
İMZA taşır ve kapı onu arar; raporda alanlar serbest nesirdir.

## 7.2 ⛔ Raporun sekiz promptu neden kapıdan geçmez

| Prompt | Düşme sebebi | Bizde karşılığı |
|---|---|---|
| 16A avlu (locked, 3 m, 28 mm) | T2V (iki uç yok) · "Scene n of N" yok · "28mm equivalent" · "two adult workers" iz tarifi yok · rejim beyanı yok | tek geçerli bakış — Camera satırına çevrilir: *lens 3.0 metres above the courtyard floor, 7.0 metres from its centre, bearing …, tilt 30 degrees down, zero roll* + TIME RATE rejim B |
| 16B tepeden slab | tepeden yalnız KARE olur (§2.1); "gloved hands" rejim A insanıdır, iz/rejim beyanı yok · T2V | bizde yüzey sınırı ⑦ kadraj içi kinetik, insansız |
| 16C bitki yandan | konu dışı (yapı yok) | — |
| 16D bulut, sabit | gök tek taşıyıcı ⛔ DERS 15 · 47 — zemin hızlanmalı | gök fiili var ama zemin yok |
| 16E slider 40 cm | ⛔ katman 1 · paralaks isteği | KAMERA_HAREKETI §2.3 |
| 16F orbit 20° | ⛔ istasyon değişimi [DERS 52] | — |
| 16G dolly out 1,5 m | ⛔ katman 1; "final reveal" A18-e | HOME zaten en geniş |
| 16H gemiye bağlı kamera | ⛔ ayrı format — istasyon dünyaya sabit | — |

```
⭐ ÇEVİRİ KURALI — raporun "3 meters above, diagonally down, 28mm-equivalent" dili
   bizim Camera satırına şöyle iner: "lens N.N metres above <zemin adı>, N.N metres from
   <eksen nesnesi>, bearing N degrees, tilt N degrees down, zero roll." Milimetre
   YAZILMAZ; milimetre planın formül girdisidir, prompta metre ve derece iner.
```

## 7.3 Çelişen komutlar — kapı §12 zaten var, sözlüğü eksik

```
RAPOR §14A tablosu: "static camera, slow dolly in" · "fixed 35mm, dramatic zoom" ·
"top-down, deep vertical wall" · "same framing, full orbit" → birini seç.
BİZDE  prompt_kontrol §12 olumlu hareket kelimesini FIX'e düşürür:
       pan · tilt · zoom · dolly · orbit · tracking shot · handheld · gimbal · crane up ·
       push in · pull back.
⚠️ KAPI ADAYI: truck · pedestal · slider · arc · reveal · hyperlapse listede YOK.
   ⛔ Kör eklenmez — "truck" her promptta KAMYONDUR, "arc" kaynak arkıdır; ikisi de
      yanlış FIX üretir. Eklenecekse "camera trucks" · "the camera arcs" gibi ÖZNELİ
      kalıpla eklenir. Sahip kararı; bu kılavuz aracı değiştirmez.
⭐ "Top-down view, visible deep vertical front wall" çelişkisi bizde §2.1'in bedel
   sütunudur: tepeden bakışta düşey derinlik sıfır. Çukur filmi tepeden yazılmaz.
```

---

# 8. 🚫 NEGATİF — Veo'nun kuralı ile bizim imzalar

```
VEO (çekildi ✅)  ayrı negatif alanda "no walls" YAZMA; "walls" yaz. "no/don't" tavsiye edilmez.
BİZDE             imzalar "No readable text…" ile başlar ve kapı bunları ARAR [DERS 35].
                  DERS 33: "YOK yazılan özne VAR oldu" — koşullu cümle özne üretir.
                  DERS 11: gövdede pozitif ölçülebilir çapa TUTTU.
                  C1-g: evrensel blok tek başına engellemiyor; sahneye özgü 1–3 dışlama.

⇒ ÜÇ ŞEY AYNI ANDA DOĞRU:
   ① İmzalar KALIR (ölçülmüş kapı; dış doküman kapıyı kaldıramaz [kart S §3]).
   ② Gövde POZİTİF kalır (DERS 11) — Veo'nun tavsiyesiyle aynı yönde.
   ③ Aracın AYRI negatif alanı varsa oraya "no" ile başlayan cümle DEĞİL, öğe adı
      yazılır: "camera drift, flicker, warped geometry, object duplication, teleporting
      material, jump cut, text overlay, logo" [rapor §14A listesi · C1-g ile uyumlu].

⭐ ARAÇ KARTINA İNEN SORU [ARAC_KARTLARI §4 ölçüm adayı ⑨]:
   "Aracın ayrı negatif alanı var mı? Varsa 'no X' ile 'X' aynı sonucu veriyor mu?"
   İki klip, aynı prompt, yalnız negatif alanın biçimi farklı. Ölçülmeden kural olmaz.
```

---

# 9. 📱 DİKEY KADRAJ — bizde doğal 9:16, kırpma yok

```
RAPOR §11  1280×720'den 9:16 merkez kırpma → 405×720 (%31,6 genişlik kalır);
           3840×2160 → 1215×2160. Hesap tuttu [A19_DENETIM §1.2].
BİZDE      dikey filmler 9:16 DOĞAR: 3840 px boy, kırpma yok. Sorun yok.
           Güvenli alan: KAMERA_ISTASYONU §6 · platform zarfı: CAPRAZ_YAYIN §3 ·
           Instagram ızgarası 4:5 (kapak karesi) — raporun "kapak ile video kadrajını
           ayrı değerlendir" maddesi bizde CAPRAZ_YAYIN §3.2 olarak zaten var.

⚠️ AÇIK SORU — sahip kararı: YATAY MERDİVEN filmlerinden (16:9 · §2.8) Shorts kesiti
   alınacak mı? Alınacaksa raporun üç yolu:
     ⓐ 4K yatay masterdan 1215×2160 merkez kırpma → 1080×1920 (ayrıntı korunur)
     ⓑ 1080p masterdan kırpma → 608×1080 büyütülür → ayrıntı ÜRETMEZ ⛔
     ⓒ yatay kareyi dikey tuvale bütün yerleştirme (üst/alt boş) — tasarım kararı
   CAPRAZ_YAYIN §1 "tek master" der ve bu soruyu kapsamıyor. Karar verilirse oraya
   iner; bu kılavuz karar vermez. Tek uyarı: yatay HOME dikey kesite göre KURULMADI —
   kanıt nesnesi merkez şeritte değilse ⓐ hikâyeyi keser (rapor §11 · §17).
```

---

# 10. 🎞️ İLK KARE · DÖNGÜ · SES

```
DÖRT AÇILIŞ (rapor §12)          bizde
   açık sorun                    ⭐ G0: bütün şekil + onu bozan eylem AYNI klipte [KAMERA_HAREKETI §4 · P3-a]
   beklenen sonuç (tek tohum)    G0 boş arsa değildir — araç temas hâlinde hazır [§4]
   görünür sınır                 ⑦ YÜZEY SINIRI kadraj içi kinetik [KAMERA_HAREKETI §7]
   ölçek merakı (parça → bütün)  ⛔ geri çekilme ister; bizde HOME'da başlar

"SONUCU ÖNDEN GÖSTER"            dördüncü öneri · alınmadı · ölçüm borcu [§1 ③]
"DÖNGÜ: bitmiş binayı boş arsaya
 çevirmek süreklilik değildir"   ⭐ A14-d'nin aynısı: kadraj döngüsü VAR, durum döngüsü YOK
                                 [KAMERA_HAREKETI §5]. Rapor dışarıdan ikinci kez doğruladı.
"8 s klip: 0–1 başlangıç ·
 1–6 dönüşüm · 6–8 sonuç"        bizde ÜÇ VURUŞ (2·4·2) [KAMERA_HAREKETI §6 ②] ve
                                 "DURUŞA kes" [A8-d]. Aynı iskelet; sayılar bizde ölçüldü,
                                 raporda "başlangıç taslağı". Bizimki kalır.
SES                              "kamera talimatından ayrı cümle" — bizde prompta ses
                                 GİRMEZ; müzik ayrı dosya [MUZIK_VE_KAPAK §1]. Uyumlu.
```

---

# 11. 🧱 KONU REÇETELERİ ↔ YAPI KARTLARI

Raporun §13'ü on konu için bakış + lens + hareket önerir. Bizim kanal tezi "her film bir
BEDEL gösterir" [KANAL_KIMLIGI]; konu havuzu yapı kartlarıdır. Eşleme:

| Rapor konusu | Raporun bakışı | Bizde kart | Uyum |
|---|---|---|---|
| Yol onarımı · küçük şantiye | yüksek üç çeyrek · 24–35 · sabit · "malzeme yoktan belirmesin" | çökük/altyapı §6b · SWALLOWED BUS | ✅ birebir (DERS 48 dâhil) |
| Su dolumu · alan ortaya çıkar | tepeden alan / yandan seviye / çapraz ikisi · sabit duvar referansı | kuru havuz (kart adayı) · BACK TO WATER | ✅ §2.3 satırı buradan |
| Nesne restorasyonu | 45° çapraz · "çalıştığını göster" | ⭐ ödül = yapının ÇALIŞMASI [SANTIYE §4.7 · C1-d] | ✅ |
| Büyük nesnenin ölçeği | ayrıntıdan bütüne dolly out | ⛔ katman 1 | HOME'da başlar |
| Oda dönüşümü | köşeden 20–28 mm · 1,5–2 m | konut/villa iç mekân yok | — |
| Temizlik | tepeden/yüksek çapraz · sınır izlenir | ⑦ yüzey sınırı · stadyum çimi | ✅ kadraj içi |
| Bitki · kök | hiza · 40–85 · cam kesit | ⛔ konu dışı | — |
| Bulut · fırtına | 16–24 · altta arazi referansı · pan seçilebilir | ⛔ gök tek taşıyıcı olamaz [DERS 15] · pan ⛔ | — |
| Şehir hyperlapse | güzergâh · tek doğrultu | ⛔ katman 1 | — |
| Şantiye (EarthCam dersi) | "nihai yapının sığacağı genişlik/yüksekliği baştan hesapla · iki sabit çevre referansı · evreleri ayır · işçi hareketi ilerleme değil" | §3 ② taç hesabı · üç nirengi · INSAAT_YONTEMI ara hâller · C1-d | ✅ dördü de ölçülmüş kural |

```
⭐ RAPORUN ORTAK SONUCU (§2 sonu): "Büyüme için son boyuta yer bırakmak, inşaat için aynı
   geometriyi korumak, yolculuk için platform ile çevreyi ayırmak, deney için değişim
   sınırını göstermek FARKLI çözümlerdir. Hepsini tek 'viral kamera açısı' altında
   toplamak yanıltır." — §2.3 tablosunun varlık sebebi.
```

---

# 12. 🩹 HATA TABLOSU ↔ DERSLER — 15 belirtinin 14'ünün karşılığı var, 7'si numaralı DERS

Raporun §17'si deneyimden yazılmış; bizim ölçülmüş derslerle örtüşmesi, derslerin
dışarıdan ikinci kez doğrulanmasıdır. Sütun "bizde" boşsa ders yok demektir.

| Rapor belirtisi | Bizde |
|---|---|
| Çok hareket var, ilerleme anlaşılmıyor | C1-d ANA İŞ · SANTIYE §3 yüzey kanıtı · A6-d |
| Bina eğiliyor, duvarlar değişiyor | DERS 19 sayılı bible · §3 keystone · PERSPEKTIF §2 |
| Temizlenen bölüm yeniden kirleniyor | DERS 5 ters inşa · §2.7 zincir · BEŞ SORU ④ |
| Aletler ve malzeme birden kayboluyor | DERS 48 · SÖKÜM satırı fiille [P2-h] · DERS 57 |
| Parlaklık titremesi (gerçek çekim) | KURGU_VE_TESLIM §6 flicker ölçümü (yayın öncesi) |
| Görüntü sıçrıyor | zincir_kontrol eşik · üç nirengi [KAMERA_ISTASYONU §7] |
| Bitki tepeden kesiliyor | §3 ② taç %82 hesabı (son boyuta yer) |
| Makro ayrıntı netlikten çıkıyor | — (makro yok) |
| Dikey videoda işlem görünmüyor | doğal 9:16 + güvenli alan §6 · A18-b merkez şerit |
| Geri çekilmede perspektif değişmiyor | A13-b: bizde BEKLENEN — kurgu yakınlaşması paralaks üretmez |
| Orbit sırasında arka değişiyor | ⛔ orbit yok [DERS 52] |
| Kamera durmadan yön değiştiriyor | prompt_kontrol §12 · DERS 6 · 11 |
| Klipler birleşince nesne zıplıyor | §2.7 iki uç · DERS 20 · 25 · 52 |
| Final acele bitiyor | DERS 45 · A8-d duruşa kes · ÜÇ VURUŞ · KURGU §3 |
| İkinci sürüm daha az izleniyor | YAYIN_PLANI §6.2 üç-film kuralı · 06 deney planı |

```
⭐ RAPORUN DÜZELTME SIRASI: "önce fiziksel/görsel süreklilik, sonra kadraj, sonra ritim,
   en son süsleyici hareket ve efekt. Anlaşılmayan dönüşümü müzik veya daha hızlı kurguyla
   çözmeye çalışma." — kart R 6a'nın (ZİNCİR ÖNCE: ⑤ ve ⑧ tutmadıysa diğer skorlar
   yorumlanmaz) dışarıdan doğrulanmış hâli.
```

---

# 13. 📈 KANALDA TEST — altı sürüm bizde üçe iner

```
RAPOR §19   A1/A2 yüksek çapraz · B1/B2 tepeden · C1/C2 alçak çapraz × (sabit / finalde hareket)
BİZDE       A2 · B2 · C2 = katman 2 → THE NARROW GORGE ölçümü [KAMERA_HAREKETI §10]
            C1 alçak açı → bizde yok (§2.1)
            B1 tepeden → yalnız kare olarak, düşey derinliksiz (§2.1)
            ⇒ test edilebilir tek şey A1 — yani BAKIŞ AİLESİ değil, aile İÇİNDE tilt bandı
              (§2.3 · örn. −22° ↔ −35°) ve h/D oranı. O da aynı yapı tipinde iki filmde,
              tek değişkenle [06_IZLEYICI_DENEY_PLANI §3 · YAYIN_PLANI §6.2].
⛔ "Aynı anda konu, süre, açı, kapak değiştirilirse hangisi işe yaradı ayrılamaz" —
   rapor ve 06 planı aynı cümleyi kuruyor. Sahne süresi hiçbir adımda değişken değildir
   (sahip kuralı).
⭐ KAYIT SATIRI (rapor): tarih · konu · süre · açı · hareket · ilk kare · final · gösterge
   ve payda · sonuç · sonraki değişiklik. YAYIN_PLANI §6.1'in listesine "AÇI (aile · tilt ·
   h/D)" alanı eklenir — sayı değil etiket. Engaged views [06 §2 · YouTube 31.03.2025 ✅].
```

---

# 14. 🚫 UYGULANMAYANLAR — rapor doğru olabilir, burada cihaz yok

Kapsamlı okumanın kaydı: aşağıdakiler kılavuza İNMEDİ ve inmeyecek, sebebi tek: **bu
depoda fiziksel kamera yoktur** [KAMERA_HAREKETI giriş · A13-a].

```
rapor §6   kamera türleri tablosu · üç başlangıç kurulumu · GoPro Time Lapse/TimeWarp
rapor §7   tripod · slider · moco kafa · gimbal · dolly · jib · araç bağlantısı ·
           "hareket et dur çek" · "tripod gerçekten sabit mi" (⚠️ bunun bizdeki karşılığı
           zincir_kontrol'dür — istasyon kayması aracın hatasıdır, ayağın değil)
rapor §9   interval cihaz ayarları · intervalometre · "menüdeki anlam"
rapor §10  pozlama süresi · WB kilidi · deflicker · LED bantlanma · lens geçişi
           (⚠️ flicker yayın öncesi ÖLÇÜLÜR [KURGU_VE_TESLIM §6]; üretilmez, ölçülür)
rapor §2A  gemiye bağlı kamera · balıkgözü/doğrusal 12 mm farkı
rapor §16C–D · §16H  bitki · bulut · deniz promptları (konu dışı)
```

---

# 15. 🚦 KAPI — bu kılavuz nerede zorlanır

```
PLAN §DEĞİŞMEZLER   ⭐ KARAR CÜMLESİ (§0) tablonun üstünde · "tilt formülü: KAMERA_DILI §3"
                    satırı tilt ≠ 0 olan her planda.  ⚠️ prompt_kontrol bunu ARAMAZ
                    (SAHNE_PLAN_KARTI'nın ilk günü gibi); kapı olması sahip kararıdır.
KADRAJ KİLİTLERİ    tilt ≠ 0 → §3 formülü; tilt 0 → KAMERA_ISTASYONU §3. Karışık kullanılmaz.
ÜRETİM GÜNLÜĞÜ §1   usta karede ölçülen kilitler ↔ §3 formülü: fark yazılır. Üç filmde
                    (HIDDEN OASIS · SWALLOWED BUS · BACK TO WATER) ölçüm gelince bu
                    kılavuzun ilk sınavı odur.
ARAÇ KARTI          ⑨ adayı: negatif alan biçimi (§8) — ölçülmeden kural olmaz.
prompt_kontrol §12  kelime listesi adayı (§7.3) — özneli kalıpla, sahip kararıyla.
QA                  yeni mercek YOK. ① KARE ve ⑤ DEVAMLILIK zaten istasyonu ölçüyor;
                    bakış ailesinin "doğru" olup olmadığını yalnız izleyici verisi ölçer (§13).
```

---

# 16. ⚠️ BU KILAVUZUN STATÜSÜ

```
✅ ÖLÇÜLDÜ (bu makinede)   raporun 8 sayısı · rejim tablosunun bağımsız türetimi ·
                          tiltli formülün özel hâli · üç filmin ≤2,9 puan sapması
✅ DOĞRULANDI (kaynak)     11 kaynağın 10'u açıldı, iddiaya ait — sayaç, tarih, ekipman, bölüm
⛔ ÖLÇÜLMEDİ               §2.3 tablosunun İZLEYİCİ karşılığı ("bu boyut bu bakıştan daha
                          çok izlenir") — rapor da ölçmedi, kimse ölçmedi. Tablo, konsept
                          kapısının bir uzantısıdır; performans iddiası DEĞİLDİR.
⛔ DEĞİŞMEYEN              katman 1 kilidi · negatif imzalar · ters açılış · lens kilidi ·
                          SANTIYE §1 tablosu · MUZIK_VE_KAPAK §4.4 · KAMERA_ISTASYONU §3 ③ (kule)

⭐ İLK SINAV: tiltli üç filmden ilki üretildiğinde usta karedeki kilitler §3 formülüyle
   karşılaştırılır. ≤3 puan tutarsa formül DERS olur; tutmazsa §3 düşer ve
   KAMERA_ISTASYONU §3 ③'ün "tilt verme" kuralı aşağı bakış ailesine de yayılır.
```
