# 🗺️ Kılavuz İhlalleri ve Kural Boşluk Haritası

> **Kapsam:** Tarafımızdan tespit edilen TOP 10 Arıza Kalıbı (F01–F10) ile depoda bulunan mevcut kılavuzlar (`kilavuzlar/*.md`) arasındaki ilintilendirme, kılavuzlardaki eksiklikler ve zafiyet nedenlerinin haritasıdır.

---

## 1. Arıza Kalıpları — Kılavuz Eşleşme Matrisi

| Arıza Kodu ve Adı | İlgili Mevcut Kılavuz | Kılavuzdaki Durum | Zafiyet / Boşluk Sebebi |
|---|---|---|---|
| **F01: Sihirli Belirme** | `INSAAT_YONTEMI_KILAVUZU.md`<br>`YAPI_TIPI_KARTLARI.md` | ⚠️ Kural Var (Metin) | Metin bazlı "ara hâl" şartı var ancak promptta mekanik taşıma/montaj nedeni beyanı zorunlu etiketlenmemiş. |
| **F02: Atıl Şantiye** | `SANTIYE_HAREKETI_KILAVUZU.md`<br>`ARAC_KARTLARI.md` | ⚠️ Kural Var (Bölüm) | Şantiye hareketi beyanı isteniyor fakat AI modellerine nesnelerin "hareket izi" (toz, gergin halat, dönen mikser) promptla dikte ettirilmiyor. |
| **F03: Metronom Kesmesi** | `KILAVUZ_REHBERI.md` (§2.6)<br>`KURGU_VE_TESLIM_KILAVUZU.md` | ⚠️ Kural Var (Metin) | Düz ızgara yasağı nesir olarak yazılı ancak `prompt_kontrol.py` 5 klip altında eşit süreyi BLOCK etmiyor. |
| **F04: İstasyon Kayması** | `KAMERA_ISTASYONU_KILAVUZU.md`<br>`PERSPEKTIF_VE_OLCEK_KILAVUZU.md` | ⚠️ Kural Var (Formül) | Kamera açısı ve piksel bazlı nirengi kontrolü var fakat Görsel-Görsel dikişte `zincir_kontrol.sh` piksel eşiği esnek kalıyor. |
| **F05: Geometrik Sıvı Büyüme** | `FIZIK_VE_AGIRLIK_KILAVUZU.md`<br>`INSAAT_YONTEMI_KILAVUZU.md` | 🛑 KURAL EKSİK | Katı malzeme eklenme birleşimi (birleşim elemanı, kaynak, cıvata) prompt şablonunda zorunlu parametre değil. |
| **F06: Heykel İnsan** | `SANTIYE_HAREKETI_KILAVUZU.md` | 🛑 KURAL EKSİK | İnsan figürü prompt yazımında aktif eylem fiili (eğilmiş, taşıyor, yürürken flu) taşıma şartı kılavuzda yok. |
| **F07: Gölge Sıçraması** | `ZAMAN_VE_ISIK_KILAVUZU.md`<br>`HAVA_VE_ATMOSFER_KILAVUZU.md` | ⚠️ Kural Var (Açı) | Güneş açısı derecesi yazılıyor fakat I2V promptunda gölge hareket yönü ("shadow moves clockwise") açıkça beyan edilmiyor. |
| **F08: Yük Yolu İhlali** | `FIZIK_VE_AGIRLIK_KILAVUZU.md`<br>`ARAC_KARTLARI.md` | ⚠️ Kural Var (Fizik) | Yük yolu ilkesi var fakat promptta kanca-halat kilitlenme fiili ("hook tensioned to cable") kilit olarak istenmiyor. |
| **F09: Kapak Uyuşmazlığı** | `MUZIK_VE_KAPAK.md`<br>`PROMPT_SABLONU.md` | ⚠️ Kural Var (Süreç) | Kapak son kareden türetilir deniyor ancak final karesindeki yapının tamamlanma oranı (%100 görünürlük) denetlenmiyor. |
| **F10: Filigran Sızıntısı** | `KAMERA_ISTASYONU_KILAVUZU.md` | 🛑 KURAL EKSİK | Yapay zeka veri seti sızıntılarını engelleyecek negatif prompt standart kelime öbeği kılavuzda merkezi tanımlı değil. |

---

## 2. Kılavuz Zafiyetlerinin 3 Ana Nedeni

### 1. Yazılı Kural var, Otomatik Kapı (Script Door) Yok
- `INSAAT_YONTEMI_KILAVUZU.md` dosyasında %25/%50/%75 ara hâl aşamaları tanımlanmıştır. Ancak `araclar/prompt_kontrol.py` betiği prompt metninde bu ara hâl kelimelerinin (`[STAGE: 50% COMPLETE]`, `AT THIS STAGE`) fiziki anlamını denetlemez; sadece kelimenin varlığına bakar.
- `KILAVUZ_REHBERI.md` §2.6 düz ızgara süresini yasaklar, fakat 5 kliplik filmlerde kapı devre dışı kalmaktadır.

### 2. Prompt Şablonunda Eksik Etiketler (`PROMPT_SABLONU.md`)
- Mevcut prompt şablonu `[SCENE_START_FRAME]`, `[SCENE_END_FRAME]`, `[TIME RATE]`, `[ACTIVITY]` etiketlerini zorunlu kılar.
- Ancak **`[CAUSATION / MEKANİK NEDEN]`**, **`[JOINERY / BİRLEŞİM ELEMANI]`** ve **`[HUMAN MOTION / İNSAN HAREKETİ]`** gibi yapay zekanın sihirli üretmesini engelleyen 3 kritik parametre şablonda yer almamaktadır.

### 3. Nicel (Sayısal) Eşiklerin Yetersizliği
- Gölge dönüşünde derece belirtilse de I2V promptuna güneş saati satırı eklenmemektedir.
- İnsan ve araç hareketlerinde "durağanlık negatif çekirdeği" (`static frozen statue, idle parked truck, unmoved crane`) promptlara otomatik eklenmemektedir.
