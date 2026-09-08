# ⚖️ A10 — FİZİK VE AĞIRLIK

```
AMAÇ      Yerçekimi, temas ve yük yolu gerçekliğini kurmak: her nesnenin neye
          dayandığı, neyin onu taşıdığı, havada asılı hiçbir şeyin olmaması.
KARŞILIĞI ⑧ YÖNTEM ⛔ APPEARED — altı filmin ALTISINDA yapı elemanları havadan belirdi
          ② İNŞA  "morphing, warping, breathing geometry" 0/10
          DERS 37 (siluet değişmezse ara hâl değildir)
          DERS 41 (açık kabinli makine = insansız sahada imkânsız)
          DERS 43 (makine nesneye dokunmuyorsa iş yok)
DÖNÜŞÜ    kilavuzlar/FIZIK_VE_AGIRLIK_KILAVUZU.md (HENÜZ YOK — bu prompt onu
          yazdıracak) · PROMPT_SABLONU PHYSICS bloğu · prompt_kontrol.py
KOŞU      ⛔ koşulmadı — 08.09.2026 yazıldı
```

⛔ **PHYSICS bloğu her promptta tek cümle: "Everything rests on the ground."**
Altı filmde de elemanlar havada asılı kaldı, zemine gömüldü veya bir kareden
diğerine ışınlandı. Yük yolu, temas noktası ve destek koşulu hiç yazılmadı.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen yapı statiği, geçici yapı tasarımı (temporary works) ve şantiye güvenliği üzerine çalışan bir araştırmacısın; benim ürünüm 9:16 dikey, sessiz, yapay zekâ ile üretilmiş bir inşaat timelapse filmi: 10 sahne, her sahne yaklaşık 6 saniye, kamera sabit, ve bağımsız bir denetçi altı filmin altısında yapı elemanlarının "bir kareden diğerine tamamlanmış hâlde belirdiğini, havada asılı kaldığını, zemine gömüldüğünü veya geometrisinin kaynayıp eğrildiğini (boil, warp, breathe)" ölçtü — PHYSICS bloğum tek cümle ("everything rests on the ground") ve hiçbir promptta yük yolu, temas noktası veya destek koşulu tarif edilmedi.

Birinci görevin: şu yapı elemanlarının her biri için — temel kazığı, radye döşeme, kolon, kiriş, döşeme, perde/çekirdek, çelik kolon-kiriş, çatı makası, cephe paneli, iskele, kalıp, vinç, direk/kule, berm/dolgu, boru hattı, kablo/gergi, anten/çanak — GERÇEKTE neyin üstüne oturduğunu, neyin onu taşıdığını ve yük yolunu (load path) tablo hâlinde yaz: "eleman → temas noktası → destek elemanı → zemin" zinciri; ve her eleman için inşaat sırasında GEÇİCİ DESTEK gerekip gerekmediğini (şoring, iskele, geçici bağlantı, kızak, sapan, kaldırma traversi), destek ne zaman kurulur ve ne zaman sökülür, bu desteğin sökülmeden önceki SON KAREDE hâlâ GÖRÜNÜR olması gerektiğini ayrıca belirt.

İkinci görevin: makine ve ekipmanın zemin ile temas kurallarını yaz — paletli ekskavatörün palet genişliği ve iz derinliği, lastik tekerlekli yükleyicinin tekerlek izi paterni, mobil vincin krikolarının yayılma alanı, kule vincinin temel bloku boyutu, insansız/robotik aracın (paletli rover, mafsallı manipülatör) ayak plakası veya palet izi — her birinin ~40 m'den kadrajda kaç piksel kapladığını ve GERÇEK şantiye fotoğraflarında görünen zemin bozulmasını (rut depth, bearing failure, mud displacement, track pattern) tablo hâlinde ver; ayrıca insansız/robotik sahada (Ay/Mars üssü) kabinsiz makine gövdesinin nasıl göründüğünü — kabin yok, cam yok, basamak yok, korkuluk yok, operatör koltuğu yok — ve bu makinelerin Dünya'daki adlarından (dozer, loader, excavator) FARKLI şekilde nasıl adlandırılması gerektiğini açıkla.

Üçüncü görevin: AI görüntü üretiminde en sık karşılaşılan FİZİK İHLALLERİNİ — havada asılı nesne (floating object), zemine gömülü nesne (clipping), parçaların birbirine geçmesi (interpenetration), morfolojik kararsızlık (geometry warping/boiling/breathing/swimming), gölgesiz nesne (shadowless object), ağırlıksız görüntü (weightless appearance), yapısal olarak imkânsız konsol (unsupported cantilever) — ve her birinin prompt düzeyinde nasıl engellendiğini (hangi POZİTİF cümleler yazılır: rigid, bolted, welded, resting on, bearing on, braced by) tablo hâlinde ve İngilizce örneklerle yaz; bu bilgiyi hem gerçek şantiye fotoğrafı analizi kaynaklarından hem de text-to-image/video prompt mühendisliği kaynaklarından topla.

Rapor Türkçe olsun, eleman ve parametre adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] · [İDDİA] · [VARSAYIM]) ve KAYNAK SINIFI (akademik · standart/şartname · yüklenici/ekipman belgesi · pazarlama blogu) yaz, çelişen kaynakları ikisi birden yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz; en sonda her eleman için üretim promptuna doğrudan yapıştırılacak, İngilizce ve POZİTİF birer PHYSICS cümlesi ver, örneğin "the steel beam rests on its two column brackets with both end plates bolted; the crane hook hangs slack above it and the sling lies coiled on the flange; nothing is suspended".

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A10_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A10-a, A10-b…
3. KILAVUZ     kilavuzlar/FIZIK_VE_AGIRLIK_KILAVUZU.md bu rapordan yazılır
4. KAPI        prompt_kontrol.py: PHYSICS bloğunda ≥3 temas cümlesi + yük yolu beyanı
```
