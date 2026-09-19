# 🪜 THE BORROWED HILL — SAHNE SIRALAMASI

> Tam merdiven (24 satır, bütün sütunlarıyla) `THE_BORROWED_HILL_PLAN.md` §AŞAMA MERDİVENİ'ndedir.
> Burada yalnız SIRANIN GEREKÇESİ ve toplamlar durur.

## 1. İnşa sırası neden bu

```
Sıra uydurulmadı; gömülü kemer sığınağın kendi mühendislik sırasıdır:
  ocak açılır → yol ve pad yapılır (ocaktan gelen malzemeyle) → güç ve haberleşme
  kurulur (yapı işi durmadan önce) → hendek kazılır → temel → kaburga → kabuk →
  kapatma → ÖRTÜ → işletme
⭐ GÜÇ VE ANTEN YAPIDAN ÖNCE: şantiyenin kendisi enerji ister; ayrıca bu ikisi
   sonraya kalırsa doruktan SONRA montaj işi açılır ve final dağılır [P4-f].
⭐ ÖRTÜ EN SONA: örtü yapının hem amacı hem bedelidir; tepe onunla biter.
```

## 2. Monoton büyüme — iki ters sayaç

```
ARTAN     sığınak · örtü (%0 → %100) · tümsek yüksekliği (0 → 7,5 m)
AZALAN    ⭐ tepecik (16,0 m → 3,0 m) · ⭐ Dünya malzemesi yığını (%100 → %0)
⛔ HİÇBİRİ GERİ GİTMEZ. Bir karede alınan malzeme geri gelmez; bir karede eksilen
   sandık geri dolmaz; örtülen kabuk açılmaz.
```

## 3. Rejim toplamı [SANTIYE_HAREKETI §1 · §2.8]

```
5 × B (2 sa) = 10 sa      19 × A (10 dk) = 3 sa 10 dk      Σ = 13 sa 10 dk ≤ 14 ✅
B NEREYE  S0 ilk yara · S2 pad sıyrılır · S7 hendek · S14 ilk örtü · S21 son örtü
NEDEN     beşi de ya büyük bir yüzey değişimi ya da doruk taşıyor; gölge süpürmesi
          bu beş klipte okunur. Rejim A kliplerinde gölge klip içinde fark edilmez,
          iş YÜZEYLE ve makineyle kanıtlanır.
⛔ DERS 40 kapısı açılmaz: bütün süreler eşit olduğu için "en uzun klip" yoktur.
```

## 4. Bölüm sınırı — G12 [DERS 52]

```
BOLUM_1  S0–S11  (G0…G11 + 12 I2V)  0,0–120,0 sn
BOLUM_2  S12–S23 (G12…G24 + 12 I2V) 120,0–240,0 sn
SINIR    G12 TEK KAREDİR: kaburga dizisi ayakta, hendek açık, örtü yok.
         S11'in I2V'si G12'de biter; G12 BOLUM_2'nin ilk görselidir.
         ⛔ Işık (13:40 · az 199° · el 53°), gölge açısı, tepe yüksekliği (12,6 m ·
            %61,2) ve yığın (%30) orada ATLAMAZ.
⭐ SINIR NEDEN BURADA: yapının siluetinin ilk kez tam okunduğu kare. Bölüm 1 "yer",
   bölüm 2 "örtü" — ikisi arasındaki eşik açık çelik iskelettir.
```

## 5. Mevsim taşıyıcıları — takvim sahadan okunur [P1-c]

```
① İZ DOLMASI      Mars'ta iz BİRİKMEZ, SİLİNİR [F1-a]: taze iz keskin, eski iz yumuşak.
                  S1'de "ilk izler keskin" → S14'te "izler dolmuş" → S22'de "silinmiş"
② PANEL TOZU      S5 temiz → S17 grileşiyor → S18 matte → S19 silinir → S20 parlak
③ KIRAĞI          S15 · S16 — iki sahne [DERS 7] · ⛔ kırağı, su birikintisi DEĞİL
④ TOZ FIRTINASI   S18 · S19 — görüş düşer, iş durur, temizlikten sonra başlar
⚠️ Filmin yayı ~iki Mars yılıdır ve bunu IŞIK SÖYLEMEZ; bu dört taşıyıcı söyler.
```

## 6. Üç zorunlu satır

```
KANIT   uzak krater sırtı — 25 karede %51,6 · bazalt kümesi 120 px
LOOP    G0 ↔ G24 aynı kadraj · ⛔ KAVRAM döngüsü, durum döngüsü değil
SÖKÜM   S22 BOŞALIR — geçici işler, örtüler, file, bearer ve makineler çekilir
```
