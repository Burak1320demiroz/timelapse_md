# 🔍 THE BLUE DOOR — QA RAPORU

```
FİLM          THE BLUE DOOR — terk edilmiş taş dükkân restorasyonu → sokak kafesi (7 × 8,0 sn = 56,0 sn)
TARİH         23.09.2026
DURUM         ⭐ ÜRETİLDİ VE TÜM ON İKİ MERCEK TAMAMLANDI (12/12)!
              ⭐ DÖRT TANE 10/10 TAM PUAN:
                 ③ ZAMAN 10,0/10 Ⓥ (Mod V) — PASSES (12 saatlik güneş yayı firesiz okundu)
                 ⑦ İŞ 10,0/10 Ⓥ (Mod V) — WORKING (En uzun boşluk %0, kimsenin yapmadığı büyüme: NONE)
                 ⑨ FAALİYET 10,0/10 Ⓥ (Mod V) — PRODUCTIVE WORK (Amaçsız aktivite: NONE FOUND)
                 ⑫ KATILIK 10,0/10 (Mod D) — SOLID (Eriyen/şekil değiştiren gövde: NONE FOUND)
              ⭐ BEŞ ADET 9,0+ ÜST DÜZEY SKOR:
                 ② İNŞA 9,7/10 (Mod D) — SAME · BUILT
                 ⑧ YÖNTEM 9,5/10 Ⓥ (Mod V) — MADE (8/8 parça sıfırdan yapıldı, ilk beliren parça: NONE)
                 ⑪ ENVANTER 9,4/10 (Mod D) — INTRUDERS (Klip 3 bom kolu ihlali hariç tam kadro)
                 ⑤ DEVAMLILIK 9,3/10 Ⓥ (Mod V) — SAME WORLD (Sarı konteyner 0:00–0:40.9 sabit çapa)
                 ④ TESLİM 9,2/10 (Mod D) — SONA ERİYOR (ENDS) · ⭐ FINAL BEAT PASS (10/10)
                 ⑥ GEÇİŞ 9,2/10 (Mod D) — TIME · ⭐ RHYTHM (Taşıyıcı kesim: 00:48.0 Rejim G geçişi)
                 ① KARE 8,6/10 Ⓥ (Mod V) — TIME-LAPSE (Kamera/istasyon 10/10, logo ve plaka kaçağı 3/10)
              ⚠️ NEDENSELLİK VE SIZINTI UYARILARI:
                 ⑩ SEBEP 7,0/10 (Mod D) — MAGICAL APPEARANCE (00:14 askıda yüzen pencere kasası, 00:19 gri perde montajı)
                 ⑪ ENVANTER — 00:17.0 sol kenarda dar sokak vinç yasağını delen sepetli bom kolu (boom lift)
              🚨 KRİTİK KURGU HATASI:
                 Tüm merceklerin ortak cezalandırdığı 00:56.0–01:00.0 arasındaki 4 saniyelik sahte "THE BLUE DOOR" bitiş kartı.
                 Şartnamede açıkça yasaklanan bu kart mimari halüsinasyon (çatı pencereleri, sarmaşık) içerdiği için
                 tüm merceklerde "END CARD: DIFFERENT" notu düşülmüştür.
HAM           QA/HAM_RAPORLAR/THE_BLUE_DOOR/ — 12 dosya (1_KARE … 12_KATILIK)
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|---:|---|---|
| **① KARE** | V | **8,6**/10 Ⓥ | ✅ **TIME-LAPSE** | Kamera kilidi 10 · İstasyon 10 · Ankor 10 · Güvenli Alan 10 · Yüzey gerçeği 10 · Vinç 10 · Gece 10 · Metin/Logo 3 (BULK SKIP yazısı, araç plakaları) · İnsan/Araç 3 (1,5 sn sabit kamyon, Rejim G net figür) |
| **② İNŞA** | D | **9,7**/10 | ✅ **SAME · BUILT** | Yapı kimliği 10 · Monoton büyüme 10 · Ölçek kilidi 10 · İnşa sırası 10 · Yük yolu 10 · Yöntem 10 · Su 10 · Geçici ekipman 8/10 ve Geometrik stabilite 9/10 (0:19.0 gri perde pop-in) |
| **③ ZAMAN** | V | **10,0**/10 Ⓥ | ✅ **PASSES** | **Deponun zirve zaman koşusu.** Okunan süre: "1 single day (~12 hours, 08:30 to 20:30)" planla DAKİKASINA KADAR TUTTU · Gölge süpürmesi 1:2.75 → 2.5:1 → 1:5.63 · Alacakaranlık kademeli yapay ışık açılışı kusursuz |
| **④ TESLİM** | D | **9,2**/10 | ✅ **SONA ERİYOR (ENDS)** | ⭐ **FINAL BEAT PROOF: BAŞARILI (PASS — 10/10)**. 00:54.0'te açık mavi kapı, sarı ışık yelpazesi, yanan fenerler/pencereler, tüten fincan ve eşikte tek figür eksiksiz · 4 sn bitiş kartı ve fon müziği sızıntısı kırptı |
| **⑤ DEVAMLILIK** | V | **9,3**/10 Ⓥ | ✅ **SAME WORLD** | Sarı moloz konteyneri (00:00–00:40.9), sokak lambası, komşu balkon ve Arnavut kaldırımı sabit çapa · 2/6 dikiş kusuru (Dikiş 1 iskele aniden belirme, Dikiş 2 iskele ışınlanma) |
| **⑥ GEÇİŞ** | D | **9,2**/10 | ✅ **TIME · ⭐ RHYTHM** | 7/7 sert kesim · Nirengi koruma 10/10 · Sıçrama ölçeği 10/10 · ⭐ **THE CUT THAT CARRIES: 00:48.0 Kesimi** (B hızlandırılmış rejimden G gerçek zamanlı akışa geçiş ritmik doruk noktası) |
| **⑦ İŞ** | V | **10,0**/10 Ⓥ | ✅ **WORKING** | **Kusursuz tam puan.** En uzun boşluk 0,0s (%0) · ⭐ Kimsenin yapmadığı büyüme: NONE · Sahadaki 13 büyüme olayının tamamı doğrudan çalışan işçi ve makinelerle gerçekleşti |
| **⑧ YÖNTEM** | V | **9,5**/10 Ⓥ | ✅ **MADE · 8/8 MADE** | 8 elemanın tamamı sıfırdan yapıldı · ⭐ İlk beliren parça: NONE · En iyi parça: Kemerli Mavi Kapı (söküm → sehpa zımparası → mavi boya → menteşe montajı) |
| **⑨ FAALİYET** | V | **10,0**/10 Ⓥ | ✅ **PRODUCTIVE WORK** | **Kusursuz tam puan.** Rölanti 10 · Amaçsız hareket 10 · Animasyon döngüsü 10 · İnsan emeği 10 · ⭐ En amaçsız aktivite: NONE FOUND |
| **⑩ SEBEP** | D | **7,0**/10 | ⚠️ **MAGICAL APPEARANCE** | 00:14.0 sağ üst pencere kasasının askıda boşlukta durması · 00:19.0 üst katı kaplayan gri perde paneli ardından pencerelerin aniden bitmiş belirmesi · 00:17 sol kenar atıl bom kolu |
| **⑪ ENVANTER** | D | **9,4**/10 | ⚠️ **INTRUDERS** | İnsanlar 10 · Yapılar 10 · Işık 10 · Kurallar 10 · Gece 10 · ⭐ Davetsiz misafir: 00:17.0 sepetli araç bomu (dar sokak vinç yasağı ihlali) · Gelmeyen davetli: Sahada kurulmayan manuel makaralı el vinci |
| **⑫ KATILIK** | D | **10,0**/10 | ✅ **SOLID** | **Kusursuz tam puan.** 11/11 kategori 10/10 · En kötü eriyen gövde: NONE FOUND · İskele, kamyon, konteyner, kapı ve mobilyalar kütle ve rijit kenarlarını milimetrik korudu |

---

## 2. ⛔ HÜKÜM OKUMA SIRASI

```
12 MERCEK HÜKÜMLERİNİN 10'U TAM GEÇTİ, 2'Sİ UYARI ALDI:
⑤ SAME WORLD (9,3/10 Ⓥ) ✅
⑧ MADE 8/8 (9,5/10 Ⓥ) ✅
⑦ WORKING (10,0/10 Ⓥ) ✅
⑨ PRODUCTIVE WORK (10,0/10 Ⓥ) ✅
⑫ SOLID (10,0/10) ✅
② SAME & BUILT (9,7/10) ✅
③ PASSES (10,0/10 Ⓥ) ✅
⑥ TIME · RHYTHM (9,2/10) ✅
④ ENDS (9,2/10 — Final Beat Pass) ✅
① TIME-LAPSE (8,6/10 Ⓥ) ✅
⑩ MAGICAL APPEARANCE (7,0/10 — 00:14 / 00:19 pencere montajı) ⚠️
⑪ INTRUDERS (9,4/10 — 00:17 araç bom kolu sızıntısı) ⚠️

ANALİZ:
1. ŞANTİYE VE FİZİKSEL DÜNYA MUAZZAM (③ 10,0 · ⑦ 10,0 · ⑨ 10,0 · ⑫ 10,0 · ② 9,7 · ⑧ 9,5):
   - ⑦ WORKING: En uzun boşluk %0. Kimsenin yapmadığı büyüme NONE.
   - ⑧ MADE (8/8): Hiçbir yapı elemanı aniden doğmadı. Kapının sehpada boyanıp takılması deponun en iyi imalat sekanslarından biri oldu.
   - ⑫ SOLID: Eriyen, başkalaşan, saydamlaşan gövde NONE FOUND.
   - ③ ZAMAN: Tek bir 12 saatlik yaz günü (08:30 - 20:30) gölge boyları ve yönleriyle ekrandan kusursuz okundu.
2. FİNAL VURUŞU VE REJİM G (④ 9,2 & ⑥ 9,2):
   - 00:48.0'de timelapse hızından 1× doğal hıza geçiş (Rejim G) kurgunun ritmik doruk noktası oldu.
   - 00:54.0 Final Beat Proof (açık mavi kapı, kaldırıma dökülen sarı ışık, fincan ve önlüklü tek figür) 10/10 tam puanla onaylandı.
3. ÇÖZÜLMESİ GEREKEN İKİ ANA KUSUR:
   - 00:56.0–01:00.0 BİTİŞ KARTI: Şartname dışı eklenen bu 4 saniyelik yapay zeka görseli çatı pencereleri ve sarmaşık üreterek tüm merceklerde "END CARD: DIFFERENT" uyarısına yol açtı. Kurgudan atılmalıdır.
   - 00:14.0–00:19.0 PENCERE MONTAJI (⑩ SEBEP & ⑪ ENVANTER): Üst pencereler takılırken askıda yüzen kasa ve 1 saniyelik gri perde paneli nedensellik skorunu 7,0'a düşürdü.
```

---

## 3. 🚨 EN AĞIR BULGULAR VE EYLEM PLANI

1. **[Şartname Dışı Bitiş Kartı — DERHAL KESİLECEK]:**
   - *Bulgu:* 00:56.0–01:00.0 arasına "THE BLUE DOOR" başlıklı statik kart eklenmiş; video süresi 60 sn'ye uzamış ve görselde çatı pencereleri ile sarmaşık halüsinasyonları belirmiştir.
   - *Eylem:* Master video 00:56.0'da (figür eşikteyken) sert kesilmelidir. Bitiş kartı tamamen silinecektir.
2. **[S6 Arka Plan Akustik Müziği — SİLİNECEK]:**
   - *Bulgu:* 00:48.0 itibarıyla diegetik ses yatağının altına hafif akustik bir müzik sızmıştır.
   - *Eylem:* Müzik kanalı atılacak, yalnızca pirinç kapı kolu, menteşe gıcırtısı ve kafe içi diegetik uğultusu bırakılacaktır.
3. **[Üst Pencereler Montaj Kusuru (S2 / 00:14–00:19)]:**
   - *Bulgu:* Kasanın askıda kalması ve gri perde paneli belirmesi (⑩ SEBEP 7,0).
   - *Ders:* Dar sokaklarda makaralı el vinci prompt edilirken ip ve askı sapanının bağlantı noktaları daha sıkı kilitlenmelidir.

---

## 4. ⏱️ ZAMAN TAHMİNİ

```
③ "TIME READ FROM THE FILM ALONE: 1 single day (approximately 12 hours, from 08:30 morning light to 20:30 twilight)"
Taşıyıcı: Taş cephedeki gölge süpürme yönü ve uzunluk oranları (1:2.75 → 2.5:1 → 1:5.63), gün batımında yapay ışıkların sırayla açılması (sokak lambası → fenerler → pencereler) ve restorasyon adımları.
PLAN: 12 saat (08:30 G0 → 20:30 G6/G7).
✅ DAKİKASINA KADAR TAM TUTTU.
```

---

## 5. ❓ DOKÜMAN SORULARININ CEVAPLARI

### ① KARE
1. **Hedef Ufuk %:** Planda %50,0 (±0,5) kilitlidir. Ölçülen %50,0 ile sıfır sapmayla tuttu.
2. **Logo ve Plaka Temizliği:** "BULK SKIP" ve plakalar prompt ihlalidir (`no text, no logos`), model sızıntısıdır.
3. **Rejim G (00:48–00:56):** Tamamen bilinçli ve beyanlıdır (SPEC §0/§7: S0–S5 Rejim B, S6 Rejim G).
4. **Bitiş Kartı (00:56–01:00):** Şartname dışıdır (`KAPAK KARTI YOK · 56,0 sn teslim`), kaldırılacaktır.

### ③ ZAMAN
1. **Güneş Açıları (Azimut / Yükseklik):**
   - G0 (08:30): 88° / 21° | G1 (10:30): 109° / 44° | G2 (12:30): 148° / 62° | G3 (14:30): 212° / 62° | G4 (16:30): 251° / 44° | G5 (18:30): 272° / 21° | G6–G7 (20:30): 291° / −1,4°.
2. **Takvim:** Haftalık iş tek bir güneş yayına sıkıştırılmıştır (SPEC §0 beyanlı).
3. **Sıkıştırma Oranı:** S0–S5 900× (~2 saat / 8 sn), S6 1× doğal hız (8 sn).

### ⑤ DEVAMLILIK
1. **İskele Kurulumu:** S0–S1 arası 2 saatlik zaman atlamasında sokaktan getirilip kurulmuştur.
2. **İskele Taşınması:** Tekerlekli modüler iskele S1–S2 arası 2 saatlik atlamada sağdan sola alınmıştır.
3. **Bitiş Kartı:** Tanıtım kartı değil, kurgu hatasıdır; kaldırılacaktır.

### ⑦ İŞ & ⑨ FAALİYET
1. **İş Sıralaması:** Kapı boyama → takma → iskele sökümü → kaldırım döşeme sırası plana tam uygundur.
2. **Teslim Anı:** S6 dükkan açılışı planlanan teslim anıdır; inşaat S5 sonunda biter.
3. **Konteyner Tahliyesi:** S5 saat 18:30'da (gün batımı) kanca kollu kamyonla yapılmıştır.
4. **Tek Figür:** S6'da sırtı dönük önlüklü tek figür şart koşulmuştur; ikincil figür yasağı korunmuştur.

### ⑫ KATILIK
1. **Pencere ve Kemer Ölçüleri:** Kapı kemeri 108 px ±5 px; üst pencereler x %30–40 ve %61–71 aralığında milimetrik kilitlidir.
2. **Araç Kapasitesi:** Dar sokağa uygun kompakt kanca kollu damper kamyonu kullanılmıştır.
3. **Işık Devreye Girme Sırası:** S5 gün batımında fenerler → lamba → vitrin → üst pencereler kademeli olarak devreye girmiştir.
