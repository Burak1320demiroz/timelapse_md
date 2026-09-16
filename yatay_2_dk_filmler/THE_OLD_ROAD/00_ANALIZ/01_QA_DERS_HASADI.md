# 🧾 THE_OLD_ROAD — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — her satırı `04_UYARI_NOTLARI.md` ile `00_SAHNE_TABLOSU.md`
> içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 57 ölçülmüş ders, 11 ölçülmüş film
> kaydı ve devralınan/dış okuma varsayımları var; hiçbir konsept bunların hiçbirini tetiklemez
> diyen hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — `kilavuzlar/DERSLER.md` ölçülmüş derslerden bu filme düşenler

| DERS | ne ölçüldü | BU FİLMDE KİLİT |
|:--:|---|---|
| 1 | değişmezlere geçici ekipman yazıldı, sökülünce blok kırıldı | SITE/BACKGROUND'a yalnız vadi · yamaç · eski yol · taş köprü · şapel · kaya kulesi · zirve girer; kalıp, hangar, burun, destek, geçici geçiş ACTIVITY/SITE TEXTURE'da |
| 3 | ters açılış kancayı sabote etti | S0 ileri yönlü: bitmiş köprü hiçbir karede erken görünmez |
| 4 | kart sahne sanıldı | kart 120,0–125,0 · PLAN ve SPEC künyesinde ayrı beyan |
| 5 · 25 | zincir koşulmayınca her klip başka yapı | 16 kare ters ve zincirli; kanıt nesnesi taş köprü + viraj geometrisi ELLE |
| 6 | "no zoom" tutmadı | ölçülebilir çapa: "the stone arch bridge occupies exactly the same width of the frame" |
| 7 · 21 · 26 | kar tek klipte başlayıp bitti | kar VADİYE yağmaz; kar çizgisi S6'da iner (G7 en düşük), S7'de erir → sel |
| 8 · 22 · 46 · 57 | kanca boş sarktı, uzun rijit yük havada taşınmadı | tabliye KALDIRILMAZ, İTİLİR; vinç yalnız döküm alanında ve nehir düzlüğünde, kanca hep yüklü ve alçak |
| 12 | yazılı kural kapı değildir | itme kuralı hem prompt cümlesi hem günlük §0 ⑨ araç testi |
| 13 · 24 · 31 · 44 | düz ızgara METRONOM · varyanslı kurgu RHYTHM | düz 15 × 8,0 sahip beyanı; karşı kayıt PLAN'da; kurgu SÜRE sütunundan kesilir (kesme_kontrol.sh) |
| 14 · 15 · 18 · 47 | mevsim taşıyıcısı yok / gökyüzü hızlı, yer gerçek zamanlı / gölge donuk | her karede taşıyıcı (melez rengi · kar çizgisi · nehir · beton yaşı); TIME RATE tek cümle; B kliplerinde gölge süpürür |
| 19 · 36 | sayısız bible · tam hâl ara hâlden uzun | STRUCTURE tek cümle, sayılar QA_SPEC §3'te; AT THIS STAGE her zaman daha uzun |
| 20 | blok etiketi nesre döndü | sekiz blok etiketi birebir; kapı klasör modunda koşar |
| 23 · 32 | kutu seti ve gölge aracın özelliği | günlük §0 sekiz ölçüm + ⑨ İTME testi; 8,0 s için kutu ≥ 9,0 |
| 28 · 29 | günlüksüz üretim QA'yı kör etti (dört kez) | günlük §0 doldurulmadan tek kare üretilmez; qa_paket.sh durur |
| 30 | kapak filmden ayrı üretildi | kapak G15'ten türer; kapak kanıtı zincir_kontrol ile |
| 33 · 35 | olmayan özne yazınca geldi | "no X" yok; boşluk pozitif yazılır; metin yasağı yüzeye göre |
| 34 · 42 | korpussuz saha CGI'ye düştü · yapı adı korpusu değiştirdi | "concrete box-girder viaduct pushed from one side" + gerçek şantiye fotoğrafı korpusu; otoyol dizisi korpusuna karşı §55 cümlesi |
| 37 | ara hâl silueti değiştirmeliydi | her itme gövdenin ucunu bir sonraki ayağa taşır — siluet değişir |
| 38 | tek mesafeyle yüzde yanlış çıktı | D_eksen 380 m · D_kenar 190 m ayrı yazıldı |
| 39 | güneş diski anılınca kadraja girdi | LIGHTING yalnız açı · gölge yönü · gök rengi |
| 40 | gölgesiz klip en uzun klipti | rejim C yok; bütün klipler eşit |
| 43 | ACTIVITY'de nesnesiz fiil → makine daire çizdi | her ACTIVITY'de geçişli fiil + büyüyen eleman nesne olarak |
| 45 | final zifiri karanlıkta bitti | G15 güneş −1°, gök aydınlık, yapı ve eski yol okunur |
| 48 · 49 | malzeme yoktan var oldu / saydamlıktan belirdi | her kesit döküm alanında doğar; hiçbir parça gövdenin ÖNÜNDE belirmez |
| 50 | araçlar cam gibi net kaldı | B kliplerinde ağır motion blur, A kliplerinde hafif iz |
| 51 · 53 | makine hazır yüzeye kaçtı · dar yüzeyde iki araç | iş yüzeyi adıyla ve yüzdesiyle; taş köprü pozitif boş; tabliye üstünde aynı anda tek makine |
| 52 | istasyon değişen kesmede yapı da değişti | tek istasyon, 16 kare |
| 54 | ıslak beton + su = havuz okundu | ayak kaideleri ve döküm yatağı "dry, matte, formed concrete"; sel karesinde su kahverengi ve AKAR |
| 55 | tekil yazılan yapı çoğaldı | "exactly one new elevated crossing and one existing stone arch bridge" |
| 56 | montajda hareket fiili yapıya sıçradı | "only the deck slides; the piers stand still"; ışıklar yalnız S13'te yanar |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `QA/RAPORLAR/` + `QA/00_INDEX.md`

| kayıt | hüküm | bu filmde önlem |
|---|---|---|
| OVER THE WALL · EMPTY RIDGE | günlüksüz üretim → 11/12 mercek RUN INCOMPLETE | günlük §0 kapısı; qa_paket.sh günlüksüz açılmaz |
| OVER THE WALL | ⑤ A SET REBUILT · ⑧ APPEARED 0/4 · ⑩ MAGIC | zincir + kanıt nesnesi elle + her kesitin döküm alanında doğması |
| EMPTY RIDGE | ⑩ MAGIC ×3 (kaldırma), ① C1 CRANE 2/10 | kaldırma yerine İTME; vinç yalnız alçak ve yüklü |
| EMPTY RIDGE | ② hayalet kuleler (korpus çoğalması) | "exactly one … one …" cümlesi + günlükte sayım |
| THE LONG DAY · CLOSING SPAN · NARROW LOT | ⑥ METRONOM (düz ızgara) | sahip beyanı + müzik katmanlarıyla telafi (⑥ riski kabul) |
| THE DUST YEAR | ⑦ PARKED · rejim C gölgesiz doruk | rejim C yok; her karede iki hareket eden + yüzey kanıtı |
| OVER THE WALL | ⑫ dar yüzeyde araçlar birbirinin içinden geçti | tabliye ve taş köprü üstünde aynı anda tek araç kuralı |
| THE CROSSING | ③ 10,0 — mevsim taşıyıcısı güçlüydü | aynı yordam: dört taşıyıcı her karede |

---

## 3. 📎 DEVRALINAN / DIŞ OKUMA VARSAYIMLARI — `DERSLER.md` D-x · A/P-x

```
A1-a  süre bandı çelişkisi → 125,0 sn yatay hat; ölçüm yayından sonra (izlemeye devam · ortalama izlenme)
A1-b  kart KONUMU beyan edilir → 120,0–125,0
A2-a  izokronik dizi öngörüsel kodlamaya yenilir → düz ızgaranın bilinen bedeli, sahip kararı
A2-e  kesme vuruşun ÜSTÜNDE → 120 BPM · 4 ölçü/sahne · kesmeler 8,0'ın katlarında
A5-a  her merdiven satırı ELEMAN + ARA HÂL taşır → §2 tablosu
A6-a  rejim beyanı → A/B karışık, gerekçesi 02 §5'te
A6-d  iki hareket eden + yüzey kanıtı → her ACTIVITY bloğunda
A7-b  üretim süresi = teslim + 1,00 sn → 9,0 üret, baştan 1,0 kırp
A9-d  bant kuralı → 3,37 px/m'de nesne değil BANT yazılır (çamur çizgisi · toz bandı · pas akıntısı)
A10-i PHYSICS üç satır → taşınan · asılı + taşıyıcı · hareket eden
A11-k kesir cümlesi ölçülen pikselden → taş köprü 64 px = kadraj eninin ~1/30'u (usta karede doğrulanır)
A12-i iki kare arası gök farkı → G(n) ve G(n+1) LIGHTING satırları farklı yazılır
P1-b  direncin EKRANDA NASIL alanı → 02 §2
P1-h  final hiyerarşi → PLAN §Final hiyerarşi
P2-a  zincir = edit → günlük §2 "master'dan ne kaldırıldı/eklendi"
P2-g  gizli iş + görünür vekil → priz süresi, kaynak, gerdirme kadrajda değil; vekil: kesit sayısı ve itme
```

---

## 📌 HASAT ÖZETİ

```
Bu film ÜÇ ölçülmüş arızayı doğrudan hedefliyor:
  ① kaldırma/pop (DERS 57) → yöntem değişti: kaldırma yok, itme var
  ② çoğalma (DERS 55)      → iki yapı ADIYLA sayıldı, gerisi pozitif boş
  ③ günlüksüzlük (DERS 28) → üretim günlüğü kapısı açık
Ve BİR ölçülmüş riski bilerek kabul ediyor: düz ızgara (DERS 13 · 44) — sahip beyanı.
