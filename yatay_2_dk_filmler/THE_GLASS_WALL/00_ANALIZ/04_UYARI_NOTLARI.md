# ⚠️ THE_GLASS_WALL — UYARI NOTLARI

> Girdi: `01_QA_DERS_HASADI.md §HASAT ÖZETİ` — EN PAHALI ÜÇÜ + QA arızaları.
> Her satır promptta veya PLAN DEĞİŞMEZLER'de karşılık bulacak.
> ⛔ Bu dosya boş geçilemez; boş geçen satır, görülmemiş arızadır.

---

## ⛔ YÜKSEK ÖNCELİK — bu filmde görülme olasılığı yüksek

| # | Arıza | Tetikleyen sahne | Önlem | Ölçen mercek |
|---|---|---|---|---|
| 1 | **ÇOK SERA** [DERS 55] — "greenhouse" modelde çiftlik çoğulur, birden fazla sera üretilir | S5–S11 tüm sera sahneleri | "one greenhouse … the only greenhouse on this hillside, every other slope is bare scrubland" her görsel + I2V | ⑪ ENVANTER |
| 2 | **CAM PANEL KALDIRMA POP** [DERS 57] — panel havada kancasız belirir, vakum tutuşu görünmez | S6·S7·S8 cam montaj | Panel palete yaslanır, vakum kaldırıcı tutuşu görünür, klip SONUNDA panel yerleşmiş — havada asılı sahne YOK | ⑩ SEBEP |
| 3 | **MALZEMEYİ KAYNAK YOK** [DERS 48] — cam paleti nereden geldiği belirsiz, model doğuruyor | G5'ten itibaren | G5 görsel: "a flat pallet of glass panels lies on the right edge of the terrace" — palet G8'de boşalır | ⑩ SEBEP · ⑧ YÖNTEM |

---

## ⚠️ ORTA ÖNCELİK — ölçülmüş tekrarlayan arızalar

| # | Arıza | Neden bu filmde | Önlem |
|---|---|---|---|
| 4 | **ÇERÇEVESİZ CAM** — model çelik çerçeveyi atlayarak saf cam duvar üretiyor | Cam paneller büyük → çerçeve küçük → model atlar | Her promptta: "dark-green painted steel arched frames visible between every panel, frames are 80 mm wide" |
| 5 | **CAM AYNA YANSIMA** — cam yüzeyi mirror render ediyor, içi görünmüyor | Cam yüzey modelin doğal eğilimi | "partly translucent glass, green plants and growing benches visible inside, no mirror reflections" |
| 6 | **DENİZ UFUKU KAYAR** [§3.3 RISK] — model deniz seviyesini sahne sahne değiştiriyor | Tilt 0 garantisi yazıyla yetmiyor | Her promptta sayıyla: "the sea horizon stays at exactly 50.00% frame height (540 px from top)" |
| 7 | **İSKELE DEĞİŞMEZLER'E GİRER** [DERS 1] — koruma iskelesi kalıcı sanılır | Geçici/kalıcı karışıklığı | İskele SITE TEXTURE bloğuna; DEĞİŞMEZLER'e girmiyor; SÖKÜM satırı S8'de zorunlu |
| 8 | **KOPYA KARE** [DERS 5] — ters inşa yapılmazsa her klip başka yapı | Bu türün 1 numaralı ölüm sebebi | G12 usta kare ÖNCE → image-to-image geriye G11→G0; zincir kırılırsa üretim durur |
| 9 | **KAPAK KARTI SAHNE SAYILIR** [DERS 4] | Belgesiz kapak → ① ② ④ mercek düşüyor | QA_SPEC künyesinde SCENE BLOCK 120,0 s / END CARD 5,0 s ayrı · prompta konmaz |
| 10 | **METİN SIZMA** [DERS 35] — iskele borusu, cam etiketi, patika tabelası | Akdeniz saha metin yoğun | Negatif çekirdek son satırı: "no text, no labels, no signs, no numbers on any surface in frame" |

---

## 📌 TEKRAR EDEN ARIZA TABLOSU [KILAVUZ_REHBERI §2.8 Y2 adım 4]

Bu depoda kaç kez görüldü:

| Arıza sınıfı | Kaç filmde | Son görüldüğü |
|---|---|---|
| ② DIFFERENT · APPEARING (yapı beliriyor) | 8 film | THE EMPTY RIDGE |
| ⑥ METRONOM (düz ızgara ritim sorunu) | 5 film | THE DUST YEAR |
| ⑧ APPEARED (eleman yapılmadan doğuyor) | 4 film | OVER THE WALL |
| ⑪ INTRUDERS (davetsiz yapı / araç) | 4 film | THE EMPTY RIDGE |
| ⑤ A SET REBUILT (istasyon değişiyor) | 4 film | OVER THE WALL |
| ⑩ MAGICAL APPEARANCE (fizik ihlali) | 3 film | THE MOUNTAIN CROWN |

**Bu filmde hangisi tetiklenebilir:**
- ② APPEARING: cam paneller → vakum lifter + palet kaynağı ile baskılanıyor
- ⑥ METRONOM: DÜZ IZGARA (sahip beyanı) → ritmi klip İÇİ değişim büyüklüğü taşımalı; her sahne bir öncekinden görünür biçimde farklı sonuç taşır
- ⑧ APPEARED: teras taşları, ev duvarı, çelik çerçeve → her birinin ara hâli (%25/%50/%75) aşama merdiveninde
- ⑪ INTRUDERS: çoğalan sera → "only one greenhouse" savunması
- ⑩ MAGICAL: cam panel pop → havada asılı sahne YOK; panel palete yaslanır

---

## 🔑 AÇIK KAPILARINA NOT

```
⛔ ARAÇ KUTU SETİ ÖLÇÜLMEDİ — ızgara 10,0 s ön varsayım; üretim öncesi araç kapısı ①'de ölçülür
⛔ KAMERA HESABI KISMI — D = 45 m göz kararı; ilk pilot G12'de taban/taç/çapa yüzdeleri kontrol edilir
⭐ DÜZGÜN IZGARA BEYANI — PLAN §DÜZ IZGARA BEYANI: 12 × 10,0 düz ızgara sahip beyanıdır;
   karşı kayıt (DERS 13 · 24 · 44) ve kabul edilen risk plana yazılır; ritim klip içi değişimle taşınır
⛔ KORUMA İSKELESİ TİPİ — çelik boru mu, geçici kaplama mı? Araç kapısında gözlemlenecek
```
