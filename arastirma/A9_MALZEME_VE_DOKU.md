# 🧱 A9 — MALZEME VE DOKU

```
AMAÇ      Yüzey gerçekliğini kurmak: yapı malzemelerinin GERÇEK fotoğraftaki
          görünümü — leke, çizik, yaşlanma, ıslak-kuru farkı, kirlilik katmanı.
          SITE TEXTURE bloğu bir cümlelik → malzeme kartlarıyla doldurulacak.
KARŞILIĞI ① KARE  ⛔ SURFACE TRUTH 0/10 (iki filmde) · 3/10 (POLAR HABITAT: lazer,
                    bloom, "CGI rendering, miniature appearance, clean uniform textures")
          ② İNŞA  GEOMETRIC STABILITY 0/10 · "boil, warp, breathe"
          DERS 34 (fotoğrafik korpus yok → render estetiğine düşüş)
          DERS 42 (yapı adının korpusu geometriyi değiştiriyor)
          A4-a (beton kürlenmesi — deponun hiç kullanmadığı taşıyıcı)
          A5-c ÖLÇTÜM (kadraj 33,7 × 60,0 m · 32 px/m · okunabilirlik eşiği 0,5 m)
DÖNÜŞÜ    kilavuzlar/MALZEME_VE_DOKU_KILAVUZU.md (HENÜZ YOK — bu prompt onu
          yazdıracak) · PROMPT_SABLONU SITE TEXTURE bloğu · prompt_kontrol.py
KOŞU      ⛔ koşulmadı — v1 08.09.2026 · v2 11.09.2026
SÜRÜM v2  altı cümleye tamamlandı (A5 kalıbı) · yeni ölçümler eklendi (POLAR
          HABITAT · BUILT FROM DUST) · havasız saha ve buz/permafrost eklendi ·
          tek günlük zaman yayı eklendi · A5–A8 denetimi gereği ÇÖZÜMLENEBİLİR
          KAYNAK şartı ve "çelişenler" başlığı eklendi
```

⛔ **Beş filmin dördünde model "photorealistic" denildi ve CGI üretti.** Eksik
olan kelime değil, o kelimenin bağlandığı YÜZEY BİLGİSİ. Beton, çelik, toprak,
regolit, membranın GERÇEK fotoğraftaki izi prompt düzeyinde hiç tarif edilmedi;
SITE TEXTURE bloğu her filmde aynı tek cümleydi — Ay yüzeyinde ve buz
gezegeninde bile.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen yapı malzemeleri, şantiye fotoğrafçılığı ve fotogerçekçi görüntü sentezi üzerine çalışan bir araştırmacısın; benim ürünüm 9:16 dikey, konuşmasız, yapay zekâ ile üretilmiş bir inşaat timelapse filmi: 10 sahne, her sahne yaklaşık 6 saniye, kamera on sahnede aynı noktada sabit (24 mm eşdeğeri, yapıya ~40 m mesafe, tilt 0°, kadraj yaklaşık 34 × 60 m, yani 1080×1920 karede ~32 piksel/metre), her klip iki onaylı SABİT görsel arasında image-to-video ile üretiliyor (ilk kare ve son kare birer fotoğraf, video ikisini bağlıyor) ve her film bağımsız bir denetçi tarafından zaman damgalı rubriklerle puanlanıyor.

Ölçülmüş arıza şu: denetçi beş filmin dördünde yüzey gerçekliğini 0-3/10 puanladı — "the entire site is a CGI rendering displaying miniature appearance, artificial architectural visualization lighting, and completely clean, uniform textures rather than a photographic working site" — oysa promptlarda "photorealistic documentary construction photograph" yazıyordu; ayrıca yapı elemanı ADLARI modelin eğitim külliyatındaki tipik görünümü çağırdı ("regolith bags" kum torbası mevzisine, "inflatable cylinder" kubbeye, "lattice mast" sondaj kulesine döndü) ve "a hard-mounted engineering camera" gibi var olmayan bir fotoğraf külliyatına atıf yapan korpus cümlesi 0/10 aldı; yani eksik olan kelime değil, o kelimenin bağlandığı yüzey ve malzeme bilgisi — SITE TEXTURE bloğum her filmde aynı tek cümleydi ("mud, tyre ruts, standing puddles, stacked material, offcuts, tarpaulins and untidy clutter"), Ay yüzeyinde ve buz gezegeninde bile.

Birinci görevin: şu malzemelerin her biri için — taze dökülmüş beton, 7 ve 28 günlük kürlenen beton, yıllanmış beton, yapısal çelik (boyasız / astarlı / boyalı / paslı), kalıp panosu (yeni / kullanılmış), cam ve alüminyum giydirme, kazılmış toprak ve şev, Ay ve Mars regoliti, sıkışmış kar ve permafrost buzu, membran ve şişirilebilir kumaş (yeni / tozlanmış), taze ve soğumuş asfalt, tuğla ve harç, ahşap — GERÇEK şantiye fotoğrafında o malzemenin tanımlayıcı yüzey özelliklerini (renk tonu, pürüz, desen, parlaklık/matlık, leke tipi, yaşlanma izi, ıslak-kuru farkı) tablo hâlinde yaz; her satırın yanına o malzemenin AI görüntü/video üretiminde ve mimari görselleştirmede tipik olarak NASIL YANLIŞ üretildiğini (çok pürüzsüz, çok homojen, çok parlak, çok doygun, aynı dokunun tekrarı) ve gerçek fotoğraftan somut farkını koy; ayrıca her malzeme için hangi GERÇEK fotoğraf külliyatının (belgesel şantiye fotoğrafı, uzay ajansı yüzey fotoğrafı, kutup istasyonu arşivi gibi) o görünümü taşıdığını, külliyatın adıyla ve aletiyle (film/sensör, lens, tipik ışık) belirt.

İkinci görevin: bir şantiyenin "kirli ve gerçek" görünmesini sağlayan SOMUT kirlilik ve kullanım katmanlarını saha tipine göre (şehir içi, kırsal, kıyı, dağ/kar, çöl, Ay/Mars yüzeyi, buzul/permafrost) tablo hâlinde yaz — çamur sıçraması, lastik ve palet izi derinliği, beton döküntüsü, su birikintisi, toz filmi, yağ lekesi, pas akıntısı, kür örtüsü altındaki renk farkı, kaynak yanığı, halat aşınması, paletli malzeme üstündeki naylon örtü, regolit üzerindeki tekerlek izi ve ejecta yelpazesi, buz üstünde kir bantları — ve her katmanın benim kadrajımda (24 mm, 40 m, ~32 piksel/metre) kaç piksel kapladığını ve tek bakışta AYIRT EDİLİP EDİLEMEYECEĞİNİ belirt; 0,5 metrenin altındaki detayın bu kadrajda okunmadığını varsay ve buna göre "uzaktan okunan" ile "yalnız yakın planda var olan" katmanları ayır.

Üçüncü görevin: malzemenin FİLM SÜRESİ boyunca nasıl yaşlandığını zaman çizelgesiyle ver — beton kürlenmesinin gün gün renk değişimi (koyu ıslak griden açık kemik rengine kaç günde, hangi tona; ardışık iki dökümün renk farkı aradaki zamanı ekranda gösterir mi), çeliğin pas ilerleme hızı iklime göre, membran ve kumaşın solması ve tozlanması, camda toz katmanı, rüzgârsız bir dünyada regolit üzerindeki toz birikiminin yalnız faaliyetle (araç geçişi, kazı, ejecta) oluşması — ve bu yaşlanmanın üç zaman yayına nasıl eşleneceğini ayrı ayrı yaz: 1-3 yıllık bir inşaat, birkaç aylık bir inşaat ve TEK BİR GÜN içinde geçen bir film; her yay için hangi malzeme değişimlerinin gözle görülür, hangilerinin ayırt edilemez olduğunu belirt.

Rapor Türkçe olsun, malzeme ve parametre adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı, şartname ya da saha kaydı var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · standart/şartname · yüklenici/ekipman belgesi · uzay ajansı belgesi · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI ya da belge adı + bölüm; kaynağı gösterilemeyen sayı ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç ve yukarıda yanlış bulduğun her şeyi orada topla; en sonda her malzeme ve her saha tipi için üretim promptuna doğrudan yapıştırılacak, İngilizce ve POZİTİF (yasak cümlesi değil, ölçülebilir betimleme) birer SITE TEXTURE cümlesi ver, örneğin "the cured slab is pale grey with dark wet patches where ponded water has not yet dried, tyre ruts indent the mud beside it and a chalky white curing-compound residue streaks the nearest bay".

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A9_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A9-a, A9-b…
3. KILAVUZ     kilavuzlar/MALZEME_VE_DOKU_KILAVUZU.md bu rapordan yazılır
4. KAPI        prompt_kontrol.py: SITE TEXTURE bloğunda ≥5 somut nesne yoksa FIX ·
               saha kartıyla çelişen nesne (havasız sahada "puddles") BLOCK
```
