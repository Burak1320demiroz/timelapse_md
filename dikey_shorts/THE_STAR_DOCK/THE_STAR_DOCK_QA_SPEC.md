# 🔬 THE STAR DOCK — QA SPEC

```
⛔ Bu dosya PLANIN DEĞİL, TESLİMİN kapısıdır. Her madde TEK KAREDE ya da TEK KLİPTE ölçülür.
   Ölçülemeyen bir madde bu dosyaya yazılmaz.
KAYNAK  dikey_shorts/THE_STAR_DOCK/THE_STAR_DOCK_DIKEY_TIMELAPSE.md
IZGARA  7 × 8,0 = 56,0 sn · 8 görsel (G0–G7) + 7 I2V · ⭐ REJİM C × 3 → B × 1 → A × 3 (YAVAŞLAYAN SAAT)
SCENE BLOCK / END CARD   56,0 sn sahne bloğu · ⛔ KAPAK KARTI YOK
DURUM   ⛔ ÜRETİLMEDİ — hiçbir madde henüz KOŞULMADI
```

---

## 1. ⭐ FİNAL KARE KANITI — 55,5 sn (S6 tutuşunun içinde)

```
KOMUT    ffmpeg -ss 55.5 -i teslim.mp4 -frames:v 1 kanit.jpg
O KAREDE GÖRÜNMESİ GEREKEN — yedisi birden:
  ① iğ biçimli TEK gövde, halkaya OTURMUŞ: yaka %56,57 (üstten 834 px ± 4) · gövde 473 ± 4 px boy ·
     yaka 492 ± 4 px en · üst uç %72,99 (519 px)
  ② halkanın üstünde KAPALI kelepçe sırası ve halkanın soğuk beyaz ışık çemberi YANIK
  ③ iki biniş kolu ön-sol ve ön-sağ kulelerden yakaya DEĞİYOR
  ④ gece çizgisi ön-orta kulede ≈ 121 m (üstten ≈ 957 px); ön-orta kulede ÜÇ galeri yanık
  ⑤ gövdenin üst yarısı, halka ve kulelerin üstü GÜNEŞTE (DERS 45 — final aydınlık)
  ⑥ iki hangar ve rampa lambaları yanık; iki rover rampanın tepesinde
  ⑦ üç çapa yerinde: ikiz kaya · uzak sırt + çentik · gezegen (%93,8 aydınlık, aydınlık taraf yukarıda)
⛔ Yedisinden biri yoksa FİLM TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.
⭐ TUTUŞ [P2-i]: 54,0 – 56,0 sn arası gövde, halka ve kollar SABİTTİR; yalnız gece çizgisi tırmanır ve
   54,86 sn'de son lamba (ön-orta kule, 112 m galerisi) yanar. Kanıt karesi bu lambadan SONRA alınır.
```

---

## 2. ⭐ GÖVDE KAPISI — filmin en ağır tarifi, üretimin İLK sınavı [DERS 57 · 49]

```
NEREDE   S5 (G5 → G6) ve S6 (G6 → G7). Gövde G0–G5'te HİÇBİR karede yoktur.
NEDİR    dikey eksenli, iğ biçimli, 240 m'lik tek bir gövde; alt uçtan 80 m yukarıda 250 m'lik düz yaka;
         koyu gri seramik, ince açık renkli dikey nervürler, yakada tek sıra soluk ışık.

  ① GÖVDE BELİRMEZ. S5'te kadrajın ÜST KENARINDAN girer (2,5 – 4,0 sn); hiçbir karede saydamlıktan
     doğmaz, ortada bir yerde birden var olmaz. ⛔ Opaklık geçişi görülen klip DÜŞER [DERS 49].
  ② GÖVDE KOPYALANMAZ. Hiçbir karede iki gövde yoktur; hedefte bir kopya belirip kaynak silinmez
     [DERS 57'nin mekanizması]. ⛔ Aynı karede iki gövde = klip düşer.
  ③ GÖVDE BOYU SABİT. G6 ve G7'de 473 ± 4 px; S5'in 4,0 – 8,0 aralığında ve S6'nın tamamında boy
     değişmez (yalnız kotu değişir). ⛔ İnerken büyüyen/küçülen gövde = klip düşer.
  ④ GÖVDE DİK VE DÜZ. Ekseni düşeydir (±1°); sallanmaz, yatmaz, dönmez.
  ⑤ İTİŞİN TEK İZİ TOZDUR. Alev, parlama, hale, görünür jet YOKTUR — havasızlıkta itiş görünmez,
     yalnız tepeden savrulan toz halkası (yassı, temiz yaylar, asılı kalmaz).
  ⑥ S5'İN İLK 2,5 SANİYESİ: gövde kadrajda DEĞİLKEN gölgesi güneşteki kulelerin ve halkanın üstünden
     önden arkaya kayar. Gölgenin kenarı keskindir.
⭐ KORPUS KONTROLÜ: "alien|spaceship|ufo|mothership|saucer|crane" desenleri sekiz görselin ve yedi I2V'nin
   İNGİLİZCE metninde 0 olmalı (plan Türkçesinde DEĞİL — orada uyarı olarak geçer).
   ⭐ KOŞULACAK (yalnız PROMPTLAR bölümünün kod blokları — plan Türkçesi bu kelimeleri UYARI olarak taşır):
      sed -n '/^# 🎥 PROMPTLAR/,/^# 🎞️ KURGU/p' <plan.md> | awk '/^```$/{f=!f;next} f' \
        | grep -ciE "\b(alien|spaceship|ufo|mothership|saucer|crane)\b"                       → 0
   ⚠️ DESEN FİLMİN KENDİ SÖZLÜĞÜNE KARŞI TEST EDİLDİ [P18-g]: kapsamsız awk Türkçe uyarı bloklarını da
      okuyordu ve 2 yanlış pozitif verdi; bölüm sınırıyla 0.
   ⭐ "hull" yalnız S5 I2V, G6, S6 I2V ve G7'de geçer (4 blok) [DERS 33].
⛔ YEDEK: S5 tutmazsa KAPSAM DARALIR — G5'e gövdenin alt ucu üst kenarda girer, gölge vuruşu düşer.
   S6 tutmazsa film düşer: final, gövdenin halkaya oturmasıdır.
```

---

## 3. ⭐ DEFTER KAPISI — HALKANIN ÖN ÜST KENARI + TAÇ

```
TAÇ (bedel tanığı)  G0 138 × 47 px (x 471 → 609 · üstten 1106 → 1153) → G1 0 px
  ⛔ G1'den sonra hiçbir karede tepenin üstünde kaya kümesi YOKTUR. Kırığı rampadır ve rampa KALIR.

HALKA ÖN ÜST KENARI (üstten px · eksen kesiti, d 510)
  kare      G0   G1   G2     G3    G4    G5    G6    G7
  hedef     —    —    1146   799   799   799   799   799
  tolerans  —    —    ±4     ±2    ±2    ±2    ±2    ±2
  ⭐ G2 → G3 tek klipte +347 px. Halka TEK PARÇA yükselir: 12 segmentin hiçbiri ayrılmaz, eğilmez.
⛔ DÜŞME ① halka herhangi bir karede bir öncekinden ALÇAKTA ise o kare düşer.
⛔ DÜŞME ② S2 klibinin herhangi bir anında halka eğik (sol ve sağ ucu arasında > 4 px fark) ise klip düşer.
⛔ DÜŞME ③ G3'ten sonra halka hareket ederse kare düşer — yapı biter, defter DONAR.
⭐ HALKA ELİPSİNİN DÖNÜŞÜ (S2): halka kamera yüksekliğini (120 m) geçerken üstten görülen yassı elipsten
   alttan görülen ince banda döner. G2'de elips 1146 → 1090 px arası (üst yüzü görünür), G3'te 799 → 876
   px arası (alt yüzü görünür). Elipsin dönmemesi = halka kamera kotunu geçmemiş demektir.
```

---

## 4. ⭐ IŞIK KAPISI — iki ayrı saat

```
BİRİNCİ YARI (G0–G3) — güneş ve GEZEGENİN AYDINLIK ORANI
  kare   azimut    yükseklik  gölge yönü     gezegen aydınlık   taç / kule gölgesi
  G0    298,92°    63,29°    +24,5° sağa        %55,1          taç 12 m
  G1    286,19°    47,96°    +11,7°             %69,3          —
  G2    279,68°    31,83°     +5,2°             %81,8          halka gölgesi tepede bant
  G3    275,34°    15,44°     +0,9°             %91,6          kule 543 m
  ⛔ DÜŞME ① gölgeler hiçbir karede KISALMAZ ve yönü sağdan düze döner, geri dönmez.
  ⛔ DÜŞME ② gezegenin aydınlık oranı hiçbir karede AZALMAZ; aydınlık taraf HEP YUKARIDADIR
     (konum açısı 348°). Karanlık kısım alttan incelir. Aydınlık taraf yön değiştirirse kare düşer.
  ⛔ DÜŞME ③ C kliplerinde gölgeler DONMAZ [DERS 47]: makine bulanıksa gölge süpürür (≈ 17° saat açısı).

İKİNCİ YARI (G4–G7) — ⭐ GECE ÇİZGİSİ ve IŞIK GRUBU SAYISI
  kare   gece cephesi                          ışık grubu   kule ışığı (ayak + galeri)
  G4     x −490 m — kadrajın alt kenarı           0              0
  G5     x −175 m — plato yakın kenarı            3              0
  G6     ön-orta kule 55,7 m (eksen 31,0 m)        7              4 (3 ayak + 1 galeri)
  G7     ön-orta kule 121,3 m (eksen 97,4 m)      22             18 (6 ayak + 12 galeri)
  S4 zamanlaması: cephe ikiz kayayı ≈ 4,4 sn, hangarları 5,9 sn, rampayı 7,4 sn'de geçer
  S6 zamanlaması: son lamba 6,86 sn (ön-orta kule, 112 m)
  ⛔ DÜŞME ④ gece cephesi YUMUŞAK ise klip düşer. Havasızlıkta yarı gölge yoktur: cephe bir KESİKTİR ve
     geçtiği yer TEK KADEMEDE kararır.
  ⛔ DÜŞME ⑤ gece cephesi hiçbir anda GERİ çekilmez; ışık grubu sayısı hiçbir karede azalmaz.
  ⛔ DÜŞME ⑥ bir ışık grubu gece cephesi ona ULAŞMADAN yanarsa (halka çemberi hariç — o kelepçeyle yanar)
     sıra bozulmuştur; klip düşer.
  ⭐ DÜŞME ⑦ G7'de gövdenin üst yarısı ve halka GÜNEŞTE olmalı [DERS 45]. Gece halkaya ulaştıysa
     final karanlıktır ve film düşer.
⛔ GÜNEŞ HİÇBİR KAREDE KADRAJDA DEĞİL (azimut 299° → 274°, bakış 94°). Kadrajda parlak nokta, disk ya da
   huzme görünürse istasyon yanlıştır [DERS 32 · 39].
```

---

## 5. ⛔ G6 = G7 KİMLİĞİ — kapak kanıtının kendisi

```
ARADA ON DAKİKA VAR. Altı şey BİREBİR aynı olmalı:
  ① altı kule, halka (551 ± 2 px), dört galeri katı, iki hangar (197 × 85 ± 2 px), rampa
  ② gövdenin biçimi ve boyu (473 ± 4 px) — yalnız KOTU değişir
  ③ istif bandı, tepedeki toz halkası, rampadaki izler, kraterin tabanındaki izler
  ④ hangar ışıkları ve rampa lambaları
  ⑤ ÜÇ ÇAPA ±2 px: ikiz kaya · uzak sırt + çentik · gezegen (konum ve boy)
  ⑥ gezegenin aydınlık oranı (%93,6 → %93,8 — gözle SIFIR fark)
İZİN VERİLEN DÖRT FARK — başka hiçbiri değil:
  ⓐ gövde 30 m iner: yaka 775 → 834 px (üstten), tepe 460 → 519 px
  ⓑ kelepçeler kapanır ve halkanın ışık çemberi yanar
  ⓒ iki biniş kolu açılır ve yakaya değer
  ⓓ gece çizgisi tırmanır; kule ışığı 4 → 18; iki rover rampadan tepeye çıkar
⛔ Beşinci bir fark varsa kapak kanıtı düşer [DERS 30].
⭐ KOŞ:  bash araclar/zincir_kontrol.sh g7_kaynak.jpg kapak.png   → çıkış 0 olmalı
```

---

## 6. KADRAJ KİLİTLERİ — ±2 px [sahip kararı 19.09.2026]

```
⭐ SIRA ÖNEMLİ: önce ÜÇ ÇAPAYA bak. Üçü tutmuyorsa geri kalanı ölçme, İSTASYON oynamıştır.
  ① İKİZ KAYA          x 734 → 819 · üstten 1371 → 1426 (85 × 54 px)
  ② UZAK SIRT          %62,02 (üstten 729 px) · kenardan kenara · EĞİM SIFIR · V çentiği x ≈ 800
  ③ GEZEGEN            merkez x 360 · üstten 565 · gövde 186 px · halka elipsi 428 × 90 px
     ⚠️ Zincir kontrolünde gezegenin KENARI ölçülür, parlaklığı değil (aydınlık oranı G0–G3'te değişir).
SONRA yapı kilitleri:
  ufuk (krater tabanı)    %50,00 (960 px)
  ön-orta kule            taban 1199 · tepe 833 · 24 px en
  ön-sol / ön-sağ kule    x 304 / 776 · taban 1174 · tepe 847
  halka (tepede)          ön alt 829 · ön üst 799 · arka alt 876 · arka üst 856 · x 264 → 816
  hangarlar               x 277 → 474 · 606 → 803 · üstten 1269 → 1354
  istif bandı             x 129 → 250 · üstten 1302 → 1326 (yükseklik C kliplerinde AZALIR)
⛔ GÜVENLİ ALAN: kanıt nesnelerinin hiçbiri y 1436'nın altına ya da x 838'in sağına geçmez.
   ⚠️ İkiz kaya alt sınıra 10 px, halkanın sağ ucu sağ sınıra 22 px uzaklıktadır — kadraj 2 px'ten
   fazla kayarsa ikisi de ilk taşan olur.
⛔ BİLİNÇLİ KABUL: gezegenin halka açıklığı (12°) sekiz karede SABİTTİR (plan Tasarım ③). Açıklık
   değişirse kare düşer — fizik değil, plan beyanı ölçülür.
```

---

## 7. HAVASIZLIK VE YÜK YOLU KAPISI

```
⭐ HAVASIZ SAHA — dört zorunlu davranış:
  ① ATILAN TOZ ASILI KALMAZ. S0'da tamburlardan, S5–S6'da itişten kalkan toz TEMİZ YAY çizer ve düşer.
     ⛔ Toz bulutu, pus, sis = kare düşer [MALZEME_VE_DOKU §5].
  ② GÖLGE KENARI KESKİN, gölge KAPKARA — yalnız lambalar onu aydınlatır.
  ③ IŞIK HALESİ YOK. Lambaların, halka çemberinin, rover pencerelerinin çevresinde glow YOK.
  ④ GÖK SİYAH VE YILDIZSIZ (gündüz pozlaması). ⛔ Yıldız alanı, nebula, ikinci ay = kare düşer.
  ⛔ SU/ÇAMUR: prompt metninde geçmez ve kadrajda görünmez.
     Koşulacak:  grep -icE "\b(mud|muddy|puddles?|rain|slush|standing water)\b" <plan.md>  → 0
     ⚠️ DESEN DARALTILDI [P18-g]: THE FIRST GUEST'ten devralınan "\bmud|puddle|rain" biçimi bu filmin
        korpus cümlesindeki "grain" kelimesini yakaladı (9 yanlış pozitif); kelime sınırlı hâli 0 verir.

YÜK YOLU [FIZIK_VE_AGIRLIK · DERS 8 · 46 · 57]
  ⛔ VİNÇ YOK. Hiçbir karede kanca, bom ucu, havada taşınan yük YOKTUR.
  S1   segment → taşıyıcı platformun kaldırılmış yatağı → iki kule başı → kriko çerçevesi → plato kayası
  S2   halka → altı kule başı → kule gövdesi → kriko çerçevesi → temel → plato kayası; her yeni bölüm
       kulenin ALTINDAN girer — üstten hiçbir şey eklenmez
  S3   panel → kısa gergin sapan → manipülatör kol → paletler → regolit
  G7   gövde → yaka → halka → altı kule → temel → plato kayası
  ⛔ Her karede en az ÜÇ temas cümlesi. Asılı her cisim tek bir SAPANA bağlıdır.
  ⛔ S3'ten sonra kule ayaklarında kriko çerçevesi YOKTUR — istifte yatık durur (söküm satırı).
```

---

## 8. SAYIM KAPISI [DERS 55]

```
Sekiz karenin sekizinde de kadrajda ŞUNLAR VARDIR:
  ① krater tabanı ② ortadaki alçak tepe ③ uzak krater duvarı ve çentiği ④ siyah gök ve TEK gezegen
  ⑤ ikiz kaya ⑥ sol öndeki istif
Sekiz karenin hiçbirinde kadrajda ŞUNLAR YOKTUR:
  ⛔ ikinci halka · ikinci kule grubu · kubbe · uzakta üs ya da şehir ışığı
  ⛔ gökte ikinci gezegen ya da ay · yıldız alanı · kadrajda güneş
  ⛔ uçan küçük araçlar · G6'dan önce herhangi bir gövde
  ⛔ yürüyen insan · kabinli/camlı inşaat makinesi (rover'lar HARİÇ: basınçlı, ışıklı pencereli, S4'ten sonra)
⚠️ EN OLASI MODEL ARIZASI: konsept bilim-kurgudur; model "port + ringed planet" görünce yukarıdaki listenin
   tamamını eklemeye çalışır. Her kare bu listeye karşı okunur.
```

---

## 9. ⭐ REJİM KAPISI — YAVAŞLAYAN SAAT (ÖLÇÜLMEDİ)

```
  S0–S2  rejim C · 9 sa / 8 sn = 4050× · makineler YOĞUN BULANIK İZ · gölgeler ≈ 17° süpürür
  S3     rejim B · 2 sa / 8 sn =  900× · makineler hızlı yumuşak bulanık · gölgeler uzar
  S4–S6  rejim A · 10 dk / 8 sn =  75× · ⭐ rover'lar TANINIR hızda · gölgeler NEREDEYSE DURUR,
                                         gece çizgisi YÜRÜR
  ⛔ C kliplerinde keskin, gerçek zamanlı hareket eden makine = rejim kaçağı [DERS 15 · 50].
  ⛔ A kliplerinde bulutlu/akan gök = fizik kaçağı (havasız).
  ⛔ Gövde A kliplerinde YAVAŞ iner (10 dk'da ~30 m – birkaç yüz m); hızlı "uçuş" = rejim kaçağı.
⭐ ÖLÇÜLMEDİ: depoda ilk kez sıkıştırma film içinde iki kademede düşüyor. ⑥ merceği S3 → S4 dikişini
   ritim mi, kopukluk mu okuyacak? ③ merceği "tek ay öğleden sonrası, 29,5 sa" mertebesini okuyabilecek mi?
   İlk üretimden sonra SANTIYE_HAREKETI §1'e ve KURGU_VE_TESLIM §2.4'e birer satır iner — ya da düşer.
```

---

## 10. ⭐ SES KAPISI — TEMAS İLETİMLİ

```
⛔ MÜZİK YOK. ⭐ VE DİEGETİK YATAK DA YOK: havasız sahada dışarıda ses yoktur. Yatak, direğin ayağındaki
   temas mikrofonudur; KASK YOK, NEFES YOK.
  ① Havadan gelen hiçbir ses duyulmaz. ⛔ Motor kükremesi, gemi uğultusu, bip = bant düşer.
  ② Duyulan her şey zeminden ve direkten İLETİLMİŞTİR: alçak geçiren, rezonanslı, yumuşak saldırılı.
  ③ ⭐ 16,0 – 24,0 kriko kursları: filmin TEK ritmik sesi; vuruşlar kuleler yükseldikçe HAFİFLER.
  ④ ⭐ 32,0 – 40,0 neredeyse sessizlik: ışıklar yanar ve ışığın sesi yoktur. ⛔ Buraya vurgu efekti konmaz.
  ⑤ ⭐ 52,0 – 53,0 kelepçeler: filmin EN YÜKSEK sesi. Ölçüm: bu 1,0 saniyenin RMS'i filmin geri kalanının
     RMS'inden en az 10 dB yüksek ve enerjisinin %80'i 120 Hz'in ALTINDA.
  ⑥ ⭐ SES KANITI: ilk ses bir KIRILMA (taç, 0,0–8,0), son ses bir KAPANMA (kelepçe); 53,0'ten sonra zemin susar.
```

---

## 11. ZAMAN VE IŞIK GÜNÜ

```
REJİM      3 × C (9 sa) + 1 × B (2 sa) + 3 × A (10 dk) = 29,5 sa
PENCERE    ay öğlesi +12,4 sa → +41,9 sa · 11,5° güney · güneş deklinasyonu +2,0° · gelgit kilidi
AY GÜNÜ    192 sa (8 Dünya günü) · gündüz 96 sa · batışa 6,1 sa kalır
⛔ Dünya ışık günü tavanı (14 sa) BU SAHADA GEÇERLİ DEĞİL; amacı korunur — gece yok, film tek ay öğleden
   sonrasının içinde. Final aydınlık (güneş 10,9°) [DERS 45].
⭐ MERTEBE BEYANI [HAVA_VE_ATMOSFER §5 · P1-c]: "bir ay öğleden sonrası, yaklaşık bir buçuk Dünya günü".
   ③ merceğinin "TIME READ FROM THE FILM ALONE" satırı bununla karşılaştırılır; "aylar" ya da "yıllar"
   okunursa film kendi süresini anlatamıyor demektir.
```

---

## 12. ⚠️ BİLİNEN RİSKLER — üretimden önce oku

```
① ⭐ EN BÜYÜK RİSK — GÖVDE (§2). Pilot S6, ikinci pilot S5. ⛔ Üçlü pilot geçmeden kalan klipler üretilmez.
② ⭐ İKİNCİ RİSK — KAVRAM SANATI ÇUKURU. Halkalı gezegen + dev gövde modeli render estetiğine çeker.
   ① SURFACE TRUTH ilk karede okunur; düşerse korpus cümlesi (Apollo 70 mm) TEK BAŞINA yetmiyor demektir.
③ GÖVDENİN ERKEN GELMESİ. Model G0–G5'e gökte bir gemi ekleyebilir. Sayım kapısı yakalar (§8).
④ YUMUŞAK GECE CEPHESİ (§4 ④) · ⑤ ASILI TOZ (§7 ①) · ⑥ IŞIK HALESİ (§7 ③)
⑦ HALKANIN PARÇALI YÜKSELMESİ. S2'de model segmentleri ayrı ayrı yükseltebilir ya da halkayı eğebilir (§3 ②).
⑧ GEZEGENİN KIMILDAMASI. Gelgit kilidi fiziktir ama model gezegeni "uzay sahnesi" refleksiyle kaydırabilir
   ya da büyütebilir. Çapa ③ ±2 px.
⑨ BİLİMKURGU HIZI. 29,5 saatte bir liman — beyanlı bedel; ④ / ⑧ "bu kadar hızlı olmaz" derse kusur değildir.
⑩ ⭐ KAPAKTA SPOİLER. Kapak gemiyi gösterir (sahip kuralı: kapak = GN). Beyanlıdır [KAPAK §1].
```
