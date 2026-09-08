# 🧱 A9 — MALZEME VE DOKU

```
AMAÇ      Yüzey gerçekliğini kurmak: yapı malzemelerinin GERÇEK fotoğraftaki
          görünümü — leke, çizik, yaşlanma, ıslak-kuru farkı, kirlilik katmanı.
          SITE TEXTURE bloğu bir cümlelik → malzeme kartlarıyla doldurulacak.
KARŞILIĞI ① KARE  ⛔ SURFACE TRUTH 0/10 (iki filmde) · "CGI rendering,
                    miniature appearance, artificial lighting, clean uniform textures"
          ② İNŞA  GEOMETRIC STABILITY 0/10 · "boil, warp, breathe"
          DERS 34 (fotoğrafik korpus yok → render estetiğine düşüş)
          DERS 42 (yapı adının korpusu geometriyi değiştiriyor)
DÖNÜŞÜ    kilavuzlar/MALZEME_VE_DOKU_KILAVUZU.md (HENÜZ YOK — bu prompt onu
          yazdıracak) · PROMPT_SABLONU SITE TEXTURE bloğu · prompt_kontrol.py
KOŞU      ⛔ koşulmadı — 08.09.2026 yazıldı
```

⛔ **Beş filmin dördünde model "photorealistic" denildi ve CGI üretti.** Eksik
olan kelime değil, o kelimenin bağlandığı YÜZEY BİLGİSİ. Beton, çelik, toprak,
membranın GERÇEK fotoğraftaki izi prompt düzeyinde hiç tarif edilmedi.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen yapı malzemeleri, şantiye fotoğrafçılığı ve fotogerçekçi görüntü sentezi üzerine çalışan bir araştırmacısın; benim ürünüm 9:16 dikey, sessiz, yapay zekâ ile üretilmiş bir inşaat timelapse filmi: 10 sahne, her sahne yaklaşık 6 saniye, kamera on sahnede aynı noktada sabit (24 mm, ~40 m mesafe), ve bağımsız bir denetçi beş filmin dördünde yüzey gerçekliğini 0/10 ölçtü — hüküm "CGI rendering, miniature appearance, clean uniform textures" oldu; promptlarda "photorealistic documentary construction photograph" yazıyordu ama model her yüzeyi pürüzsüz, homojen, lekesiz render estetiğiyle üretti.

Birinci görevin: şu malzemelerin her biri için — taze beton, kürlenen beton, yaşlanan beton, yapısal çelik (boyasız/boyalı/paslı), kalıp tahtası (yeni/kullanılmış), cam cephe, toprak/regolit, membran/kumaş (beyaz/kirli), asfalt (taze/soğumuş), tuğla/harç, alüminyum kompozit, ahşap — GERÇEK şantiye fotoğraflarında o malzemenin tanımlayıcı YÜZEY ÖZELLİKLERİNİ (renk tonu, pürüz, desen, parlaklık, leke tipi, yaşlanma izi, ıslak-kuru farkı) tablo hâlinde yaz; her satırda o malzemenin AI render/mimari görselleştirmede tipik olarak NASIL YANLIŞ ÜRETİLDİĞİNİ (çok pürüzsüz, çok homojen, çok parlak, çok doygun) yanına koy ve gerçek fotoğraftaki farkı somut olarak açıkla.

İkinci görevin: bir şantiyenin "kirli ve gerçek" görünmesini sağlayan SOMUT KİRLİLİK KATMANLARINI saha tipine göre (şehir içi, kırsal, kıyı, dağ, çöl/Mars yüzeyi) tablo hâlinde yaz — çamur sıçraması, lastik izi derinliği, beton döküntüsü, su birikintisi, toz filmi, yağ lekesi, pas izi, kür örtüsü altındaki renk farkı, metal talaşı, kaynak yanığı, halat aşınma izi, paletlenmiş malzeme üzerindeki naylon örtü — ve her birinin ~40 m'den 24 mm lensle çekilmiş dikey karede ayırt edilip edilemeyeceğini (piksel karşılığını vererek) belirt.

Üçüncü görevin: malzemenin FİLM SÜRESİ BOYUNCA nasıl yaşlandığını — beton kürlenme renk değişimi (kaç günde, hangi tona), çelik pas ilerleme hızı, toprak/regolit üzerinde toz birikimi, membran solması, cam üzerinde toz katmanı — zaman çizelgesiyle ver ve bu yaşlanmanın bir timelapse filminde SAHNELERİN ZAMAN YAYI ile nasıl eşleştirileceğini açıkla; özellikle 1-3 yıllık bir yayda hangi malzemelerin değişimi GÖZLE GÖRÜLÜR, hangileri ayırt edilemez.

Rapor Türkçe olsun, malzeme ve parametre adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] · [İDDİA] · [VARSAYIM]) ve KAYNAK SINIFI (akademik · standart/şartname · yüklenici/ekipman belgesi · pazarlama blogu) yaz, çelişen kaynakları ikisi birden yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz; en sonda her malzeme için üretim promptuna doğrudan yapıştırılacak, İngilizce ve POZİTİF birer SITE TEXTURE cümlesi ver, örneğin "the cured slab is pale grey with dark wet patches where ponded water has not yet dried, tyre ruts indent the mud beside it and a chalky white curing-compound residue streaks the nearest bay".

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A9_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A9-a, A9-b…
3. KILAVUZ     kilavuzlar/MALZEME_VE_DOKU_KILAVUZU.md bu rapordan yazılır
4. KAPI        prompt_kontrol.py: SITE TEXTURE bloğunda ≥5 somut nesne yoksa FIX
```
