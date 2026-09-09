# 🖼️ ORBITAL SCAFFOLD — Kapak Kartı

> Bu kart videonun **SON 5 SANİYESİDİR**. Sahne değildir, kurguya sonradan eklenir [DERS 4].
> ⛔ **Kapak, S9 usta karesinden (GN) TÜRETİLİR.** Sıfırdan üretilmez [DERS 30].

---

## 1. KAYNAK KARE VE İŞLEM

1. Film teslim dosyasının (`teslim.mp4`) en sonundaki **S9 klibinden**, ışıkların yandığı uygun bir kare `ffmpeg` ile alınır.
   *(Tercihen GN usta karesi üretimde zaten hazırdır ve doğrudan kullanılabilir).*
2. `s9_kaynak.jpg` üzerine aşağıdaki görsel işlem (başlık dizimi) uygulanır.
3. KAPAK KANITI koşulur: `bash araclar/zincir_kontrol.sh s9_kaynak.jpg kapak.png` (Çıkış 0 olmalıdır).

---

## 2. BAŞLIK VE METİN TASARIMI

**Metin:** `BUILT FROM DUST` (İngilizce, 3 kelime)
**Konum:**
- Çerçeve yüksekliğinin %40 ile %70'i arasındaki boş alana yerleştirilir.
- Sağdan 242 px, soldan 122 px güvenli sınırlarının **içinde** kalır. (Metin arayüz butonlarının altında kalmamalıdır).

**Tipografi:**
- Yükseklik: ≥154 px (kare yüksekliğinin %8'i).
- Renk: Beyaz veya çok açık gri, yüksek kontrastlı. Gerekirse arkasına ince, yarı saydam koyu bir bant (gradyan değil, düz renk) atılır.
- Yazı Tipi: Tek ağırlık, geniş harf aralığı (tracking). Gölge, kontur veya parlama **YOK**.

---

## 3. KAPAK PROMPTU İSKELETİ (Yedek)

Eğer kapak GN karesinden bağımsız olarak üretilmek *zorunda* kalınırsa (kesinlikle önerilmez), GN promptunun sonuna şu ek satır konur:

```text
Leave the upper middle third of the frame visually simple and low-contrast so that a title can be set over it: no structural detail, no strong edge and no bright object between roughly forty and seventy percent of frame height on the left two thirds of the picture.
Output: 9:16, 4K, no text, no watermark.
```

*(Prompt hâlâ `no text` der; başlık her zaman kurguda/görsel düzenleyicide elle dizilir).*

---

## 4. 120 PX POSTA PULU TESTİ

Kapak dosyası hazırlandığında:
`sips -Z 120 kapak.png --out test_120.png`

Aranan **İKİ** şey:
1. **Siluet:** Mars gökyüzüne (veya gece karanlığına) karşı net bir dikey kütle (habitat + direk) ve sağında/solunda alçak bir kütle (çapalar) okunuyor mu?
2. **Başlık:** "BUILT FROM DUST" kelimeleri 120 pikselde harf harf okunmasa da **kelime şekli** olarak seçilebiliyor mu?

Eğer ① kayboluyorsa, sahne **yeniden üretilir.**
Eğer ② kayboluyorsa, punto **büyütülür.** "Bence okunuyor" demek testi geçmek sayılmaz.
