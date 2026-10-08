# 🔍 THE STONE DRAGON — QA RAPORU

```
FİLM          THE STONE DRAGON — tek taş bloktan ejderha çeşmesi yontumu (7 × 8,0 sn = 56,0 sn)
TARİH         24.09.2026
DURUM         ⭐ ÜRETİLDİ VE TÜM RAPORLAR TAMAMLANDI!
              ⭐ BAŞARILI ALANLAR (İNŞAAT VE FİZİK):
                 ② İNŞA 9,2/10 (Mod D) — SAME · BUILT (11 nirengide ölçek sapması tam 0 px / %0,0)
                 ⑫ KATILIK 9,5/10 Ⓥ (Mod V) — SOLID (Taş kütlesi yalnızca eksilerek şekil aldı, erime: SIFIR)
                 ⑥ GEÇİŞ 9,4/10 (Mod D) — TIME · RHYTHM (00:46.0 Rejim B→G canlı su geçişi doruk kesmesi)
                 ⑩ SEBEP 9,25/10 (Mod D) — CAUSED BY LABOUR (Taş işleme ve montaj usta emeğiyle gerçekleşti)
                 ③ ZAMAN 9,1/10 Ⓥ (Mod V) — PASSES (12-14 saatlik güneş yayı 07:00-19:30 dakikası dakikasına tuttu)
                 ⑨ KONTROL CHECKLIST — ONAYLANDI (ŞARTLI) (Taş hareket etmedi, eksiltme monoton, müzik yok)
              🚨 AĞIR KUSURLAR VE DÜŞÜŞLER (DİKİŞ, ÇAPA VE ENVANTER):
                 ⑤ DEVAMLILIK 3,9/10 Ⓥ (Mod V) — ⛔ A SET REBUILT EACH TIME (10/12 dikiş kusurlu!)
                 ⑪ ENVANTER 5,5/10 Ⓥ (Mod V) — ⛔ INTRUDERS (İzinsiz testere makinesi, kompresör, kayıp vinç)
                 ④ TESLİM 5,7/10 Ⓥ (Mod D) — ⚠️ ENDS · FINAL BEAT FAIL (4/10 Ⓥ) (Bitiş kartı vaadi kırdı)
                 ① KARE 6,0/10 Ⓥ (Mod V) — ⛔ SIX SEPARATE SHOTS (Servi formu kayması, vinç/su katmanı zaafı)
                 ⑧ DENETİM AUDIT — 🔴 RED / REJECTED (Gantry vinç kaybolması, moloz sıfırlanması, sahte kart)
                 ⑦ TESLİMAT V2 6,5/10 Ⓥ (Mod V) — ENDS (Final Beat Pass 7/10 Ⓥ, Kapak 2/10)
              🚨 ORTAK KRİTİK HATA:
                 Tüm merceklerin ortak uyarısı: 00:55.5 sonrasına eklenen statik bitiş kartındaki heykel modeli
                 (çift devasa açık kanatlı, cephe duruşlu), ana filmde yontulan heykelle (tek kanatlı, profil)
                 tamamen farklı bir AI konsept görselidir (`END CARD: DIFFERENT`).
HAM           QA/HAM_RAPORLAR/THE_STONE_DRAGON/ — 12 dosya
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|---:|---|---|
| **① KARE** | V | **6,0**/10 Ⓥ | ⛔ **SIX SEPARATE SHOTS** | Kamera kilidi 7 · İstasyon 8 · Çapa kimliği 4 (Klip 3'te arka servi ağaçlarının form değiştirmesi, %2,5 yayılım) · Vinç 3 · Yüzey gerçeği 4 (suyun dijital katman hissi) · Bitiş Kartı DIFFERENT |
| **② İNŞA** | D | **9,2**/10 | ✅ **SAME · BUILT** | Yapı kimliği 9 · Monoton büyüme 10 · İnşa sırası 10 · Yük yolu 10 · Su 9 · ⭐ **Ölçek Kilidi Tablosu:** Ufuk %50, blok en/boy (394 × 716 px), ham kesim bandı (76 px), banker (489 px), su düşüşü (296 px) **tam 0 px sapmayla** tuttu |
| **③ ZAMAN** | V | **9,1**/10 Ⓥ | ✅ **PASSES** | **Zaman tahmini tam tuttu:** Ekrandan okunan ~12–14 saat (07:00–19:30), plandaki 12 sa 0 dk 8 sn ile birebir örtüştü · 180° gölge süpürmesi tam uyumlu · Rejim G su akışı fiziksel hızında |
| **④ TESLİM** | D | **5,7**/10 Ⓥ | ⚠️ **ENDS · FINAL BEAT: FAIL** | 00:54.0'te ağızdan su akışı mevcut; ancak bitiş kartında tamamen farklı bir heykel gösterildiği için teslimat vaadi çöktü (Kapak ve İçerik 3/10, Final Beat 4/10) · Kuru/ıslak renk ayrımı netleşmedi |
| **⑤ DEVAMLILIK** | V | **3,9**/10 Ⓥ | ⛔ **A SET REBUILT EACH TIME** | **10/12 dikiş kusurlu:** Moloz yığınının dikişlerde sıfırlanıp tekrar belirmesi (00:03, 00:07, 00:46), gantry vincin 00:43'te aniden yok olması, dikey kesim ünitesinin ışınlanması · Kanıt: Arka taş duvar ve servi ağaçları |
| **⑥ GEÇİŞ** | D | **9,4**/10 | ✅ **TIME · ⭐ RHYTHM** | 7/7 sert kesim (`HARD`, 10/10) · Nirengi dayanımı 10/10 · Süreler 6,0–9,5 sn arasında değişse de eksiltme adımları güçlü bir ritim kuruyor · ⭐ **THE CUT THAT CARRIES: 00:46.0 Kesmesi** (Rejim B→G canlı su geçişi) |
| **⑦ TESLİMAT V2** | V | **6,5**/10 Ⓥ | ⚠️ **ENDS · FINAL BEAT: PASS Ⓥ** | Mod V ön koşusu · 00:50–00:55 su akışı gözlemlendi (Final Beat 7/10 Ⓥ) · Bitiş kartındaki görsel uyuşmazlığı nedeniyle Kapak 2/10, Döngü 5/10 |
| **⑧ DENETİM AUDIT** | D | 🔴 **RED** | ⛔ **REJECTED** | Şartnameye göre detaylı hata analizi: Portal vinç kaybolması (00:43), moloz yığını sıfırlanması (00:03, 00:07, 00:46), ham kesim bandı dokusunun kaybolması, bitiş kartı uyuşmazlığı |
| **⑨ KONTROL CHECKLIST** | D | ✅ **ONAY** | ⚠️ **ONAYLANDI (ŞARTLI)** | Teknik sert kapılar tam: Heykel taş kaldı (canlanma yok), tek bloktan eksiltildi (ekleme yok), su akışı sağlandı, müzik sızıntısı yok · Tek kritik arıza: Kapak kartı görseli |
| **⑩ SEBEP** | D | **9,25**/10 | ✅ **CAUSED BY LABOUR** | 7 ana yapı elemanının tamamı ustalar ve el aletleriyle üretildi · Taşın kendiliğinden şekil alması yok · Kısa geçişler: Karot delme ünitesi (00:16.8) ve su pompası (00:39.0) |
| **⑪ ENVANTER** | V | **5,5**/10 Ⓥ | ⛔ **INTRUDERS** | İnsanlar 8 · Işık 7 · Kurallar 6 · ⭐ **Davetsiz Misafirler:** Son karttaki çift kanatlı AI ejderha görseli, 00:16'daki raylı testere makinesi, 00:39'daki kompresör tankı, 00:44'te kaybolan portal vinç |
| **⑫ KATILIK** | V | **9,5**/10 Ⓥ | ✅ **SOLID** | **Mükemmele yakın fiziksel katılık:** Blok kenarları keskin (9.5), hayalet nesne yok (10), hacim daralması eksiltmeyle uyumlu (10), sıvı fiziği yerçekimine uygun (9.5) · En çok eriyen gövde: NONE FOUND |

---

## 2. ⛔ HÜKÜM VE KALİTE ANALİZİ

```
ÇELİŞKİLİ TABLO — İKİ AYRI DÜNYA:
1. HEYKELİN OYULMASI VE MİMARİ ANATOMİ GEÇTİ (② 9,2 · ⑫ 9,5 · ⑩ 9,25 · ③ 9,1 · ⑥ 9,4):
   - Heykel tek bir taş bloktan eksiltilerek yontuldu. Hiçbir karede taş eklenmedi veya canlanmadı.
   - Ölçek kilidi tablosu 11 nirengide 0 px fark verdi (deponun en hassas ölçek uyumlarından biri).
   - Zaman süpürmesi 07:00'den 19:30'a kesintisiz aktı; 00:46'da Rejim G su akışına başarıyla bağlandı.
2. ŞANTİYE DİKİŞLERİ VE GÖRSEL DEVAMLILIK ÇÖKTÜ (⑤ 3,9 · ⑪ 5,5 · ① 6,0 · ⑧ RED):
   - 10 dikişte arıza var. Model sahadaki moloz yığınını sahneler arası aktaramayıp sıfırladı ve yeniden oluşturdu.
   - Filmin ana taşıyıcısı olan çelik portal vinç 00:43.8'de hiçbir söküm adımı olmadan sahneden buharlaştı.
   - Klip 3'te vincin kirişine raylı sulu testere ünitesi ışınlandı.
3. EN AĞIR YIKIM: BİTİŞ KARTI (END CARD: DIFFERENT):
   - Tüm 12 raporun 12'sinde de tespit edilen ortak arıza: Kurgu sonuna yapıştırılan 4 saniyelik statik karttaki
     ejderha modeli, film boyunca işlenen heykelle hiçbir benzerlik taşımamaktadır (simetrik iki açık dev kanat,
     farklı kafa ve çanak).
```

---

## 3. 🚨 EYLEM PLANI VE REVİZYON YOLU

1. **[Bitiş Kartı — DERHAL KESİLECEK]:**
   - 00:55.5 sonrasındaki 4 saniyelik statik başlık kartı kurgudan tamamen silinmelidir. Film tam 00:55.5'te çeşmeden su akarken ve usta sırtı dönük beklerken sert kesilmelidir (SPEC §1 gereği).
2. **[Kapak Görseli]:**
   - Kanal kapak görseli bağımsız bir AI görselinden değil, teslim videosunun 00:54.0 karesinden (G7 dondurulmuş kare) üretilmelidir.
3. **[İkinci Üretim / Re-render Gereklilikleri]:**
   - Eğer film tam olarak onaylatılmak isteniyorsa:
     - Portal vinç G0'dan G7'ye kadar kadrajda kilitlenmeli veya S5 kesmesinde sökümü adım adım gösterilmelidir.
     - Moloz yığını promptlarda her sahnede kümülatif olarak tanımlanmalı; dikişlerde sıfırlanması engellenmelidir.
     - Klip 3'teki raylı testere aparatının prompta sızması önlenmeli; yalnızca karot ve el aletleri kilitlenmelidir.

---

## 4. ⏱️ ZAMAN TAHMİNİ

```
③ "TIME READ FROM THE FILM ALONE: Yaklaşık 12 ila 14 saatlik tek bir güneş günü (~07:00 - 19:30)"
Taşıyıcı: Gölgelerin 180 derece kesintisiz süpürmesi (1:1.8 → 1:0.4 → 1:2.5), gökyüzü renk değişimi ve taş kütlesinin eksilmesi.
PLAN: 12 sa 0 dk 8 sn (07:00 G0 → 19:00 G6/G7 + 8 sn).
✅ DAKİKASINA KADAR TAM TUTTU.
```

---

## 5. ❓ DOKÜMAN SORULARININ CEVAPLARI

### ① KARE & ⑤ DEVAMLILIK
1. **Bitiş Kartındaki Farklı Model:** Şartname dışı üretilmiş bağımsız bir AI görselidir; teslim kriterini ihlal etmektedir. Kurgudan atılacaktır.
2. **Klip 3 Testere Ünitesi:** Şartnamede tanımlanmamıştır; model sızıntısıdır.
3. **Portal Vincin Kaybolması:** SPEC §5'e göre gantry S5'ten S6'ya geçerken sahadan kaldırılır; ancak klip içinde (00:43) aniden yok olması model zaafıdır.
4. **Moloz Yığını Sıfırlanması:** SPEC §4 (Eksiltme Kapısı) açıkça ihlal edilmiştir; moloz monoton büyümek zorundayken dikişlerde sıfırlanmıştır.

### ③ ZAMAN
1. **00:46 Rejim B → Rejim G Geçişi:** Tamamen planlı ve beyanlıdır (SPEC §8: Bulut stribi durur, su gerçek 1× hızında akar).
2. **Kapak Kartı Uyuşmazlığı:** Şartname ihlalidir; revize edilecektir.

### ⑩ SEBEP & ⑪ ENVANTER & ⑫ KATILIK
1. **Ekipmanların Durumu:** Palanga ve el aletleri tam nedenseldir; kompresör ve testere aparatının ışınlanması envanter sızıntısıdır.
2. **Fiziksel Katılık:** Taş bloğu rijit kütlesini korumuş, erime veya deformasyon yaşanmamıştır. Heykel S7 boyunca tamamen taş kalmıştır.
