# 📐 THE_IRON_BRIDGE — SAHNE SIRALAMASI

> Kart Y2 §00_ANALIZ adım 03.
> İnşa sırası köprü kartından (§3) türer. Sıkıştırma + Σ rejim burada hesaplanır.

---

## 1. İNŞA SIRASI → SAHNE EŞLEMESİ

Köprü kartı §3 inşa adımları → 12 sahneye indirildi:

| Sahne | Köprü kartı adımı | Eleman | Yüzde |
|:-:|---|---|:-:|
| S0 | Arazi hazırlığı | Ağaç kesimi + geçici yol + kutu perde | — |
| S1 | Kesonlar/kazıklar suya-zemine iner | Ankraj kazısı açık, donatı görünür | 0% |
| S2 | Ankraj blokları | Betonarme ankraj döküldü, kalıp sökülüyor | 5% |
| S3 | Destek kuleleri kuruldu | 2 geçici çelik kule nehir kenarında, vinç geldi | 10% |
| S4 | Kemer ②: iki yakadan konsol büyüyor | Kemer %40 ilerlemiş her iki yakada | 40% |
| S5 | Kemer ③: sonbahar/kış direnci | Kemer %65 — yapraklar dökülmüş, nehir yüksek | 65% |
| S6 | DİRENÇ: kış taşkını, iş durdu | Kemer %80 — nehir taşmış, geçici bariyer sualtı | 80% |
| S7 | Kemer ④: son konsol ilerliyor | Kemer %95 — boşluk 2 m, iki yarım neredeyse değiyor | 95% |
| S8 ⭐ | Orta açıklık KAPANIR | Kemer %100 — son parça kaynaklandı | 100% |
| S9 | Tabliye döşeniyor + askı çubukları | Tabliye %60 + çelik askı çubukları yerinde | — |
| S10 | Korkuluk + patika + söküm | Tabliye %100 · destek kuleleri söküldü · patika bitti | — |
| S11 | TESLİM | Köprü eksiksiz · altın saat · yeni filizler · boş köprü | — |

---

## 2. Σ REJİM HESABI

```
S0   rejim B  (genel ormanlık açılış)
S1   rejim B  (kazı · toprağa yakın)
S2   rejim B  (döküm · beton kalıp)
S3   rejim B  (kule kurulumu · vinç)
S4   rejim B  (kemer kaburga büyüyor)
S5   rejim B  (sonbahar · nehir yükseliyor)
S6   rejim A  (taşkın yakın detay · su bariyeri yalıyor)
S7   rejim B  (2 m boşluk · gerilim)
S8   rejim B  (orta açıklık kapanışı)
S9   rejim B  (tabliye döşeme)
S10  rejim A  (söküm + altın saat öncesi)
S11  rejim A  (teslim · gün batımı)

Σ rejim B: 9 sahne × ~20 dk = ~180 dk
Σ rejim A: 3 sahne × ~10 dk = ~30 dk
TOPLAM: ~210 dk = ~3,5 saat (takvim ~15 ay içinde) ✅ ≤ 14 h sınırı
```

---

## 3. BÖLÜM SINIRI KARESI

```
BOLUM_1   S0–S5  (G0–G5 görsel + S0–S5 I2V)
BOLUM_2   S6–S11 (G6–G11 görsel + S6–S11 I2V + G12 USTA KARE)

BÖLÜM SINIRI: G6 — Ocak kışı, nehir taşkın, kemer %80
KILAVUZ GEREKSİNİMİ: G6 karesi ışık + yapı yüzdesi BOLUM_1 son ≈ BOLUM_2 başı (atlamaz)

G6 KONTROL:
  saat    → 09:00 (her iki dosyada aynı)
  yapı    → kemer %80 (her iki dosyada aynı)
  mevsim  → Ocak çıplak dal, nehir taşkın (her iki dosyada aynı)
  ışık    → sabah gri gökyüzü (her iki dosyada aynı) ✅
```

---

## 4. DÖNGÜ TASARIMI (LOOP)

```
G0   Nisan sabahı 08:00 · meşe KOYU YEŞİL · nehir MAVİ DÜŞÜK · iki yakada sık orman · boş nehir
G12  Temmuz akşamı 17:30 · meşe KOYU YEŞİL · nehir MAVİ DÜŞÜK · iki yakada genç filiz · köprü var

ÇAPALAR her ikisinde: meşe (%x 12–20) · kayalık (%x 78–88) · nehir bandı (%y 38–48)
IŞIK: BİLİNÇLİ FARKLI — G0 bahar sabah ışığı (serin mavi) / G12 yaz akşam ışığı (altın)
KOST GÖRÜNÜR: G12'de köprünün her iki yanında kesim açıklığı (eski orman yoğunluğu gelmemiş)
```

---

## 5. SÖKÜM SATIRI

```
ELEMAN             GİRİŞ  ÇIKIŞ  SAHNE
Kutu perde         G0     G7     S7'den önce kalkar (su çekilince)
Geçici kule ①②   G3     G10    S10'da sökülür → F/G10 arası I2V'de görünür
Mobil vinç        G3     G10    S10'da ayrılır
Kalıp (ankraj)    G2     G2     döküm biter bitmez aynı sahne sonu
İnşaat malzeme deposu  G3  G10  S10'da temizlenir
```
