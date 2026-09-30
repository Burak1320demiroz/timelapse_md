# 🎯 THE_IRON_BRIDGE — KONSEPT VE RİSK

> Kart Y2 §00_ANALIZ adım 02.
> Bu dosya teknik + üretim dili kullanır (sahip değil, ajan okur).

---

## 1. KONSEPT KAPISI (KILAVUZ_REHBERI §6)

```
VAAT     Ormanlık vadide nehrin iki yakası çelik kemer yaya köprüsüyle birleşir
DİRENÇ  ① Nehir taşkını (S5–S6) ② Orta açıklık boşluğu (S7–S8) ③ Orman kesimi (saha)
BEDEL    G0'daki kesintisiz yoğun orman — G12'de kesim açıklığı + genç filizler
```

**Konsept kapısı testleri:**
- ✅ TEK KARE: herhangi bir karede "köprü yapılıyor" okunabilir
- ✅ KİNETİK BAĞIMSIZLIK: 10 sn sabit planda kemer büyür, yaprak rengi değişir, nehir seviyesi değişir
- ✅ BAŞLIK ŞEMASI: "The Iron Bridge" → 3 kelime, vaadi söyler
- ✅ OMURGA: keser → kazar → döker → diker → kaynar → direnir → bekler → uzanır → **KAPANIR** → döşer → söker → teslim

---

## 2. YAPI + SAHA KARTI

```
TİP           Tek açıklıklı çelik kemer yaya köprüsü
AÇIKLIK       40 m (nehir ~25 m + her yakada 7,5 m yaklaşım)
KEMER H       8 m (nehir yüzeyinden, tepede)
TABLİYE       genişlik 2,4 m · ahşap kaplama, çelik stringerler üzerine
KORKULUK      çelik boru korkuluk H 1,1 m
AYAK / ANKRAJ iki yakada betonarme ankraj bloğu 3,0 × 4,0 × 2,0 m
MALZEME       çelik kemer (ağırlıklı olarak IPE-400 profil) · çelik askı çubukları
              · meşe ahşap tabliye · galvaniz korkuluk borusu
GEÇİCİ       ① 2 adet geçici çelik destek kulesi (nehir kenarında, her yakada 1 adet)
              ② kutu perde (şantiye yatağı çevre bariyeri, su + çamur kesici)
              ③ 15 m mobil vinç (yük taşıma) — S3'te gelir, S10'da ayrılır

SAHA          Ilıman iklim ormanlık dağ vadisi · nem yüksek · nehir mevsimsel
EĞIM          0° (düz nehir tabanı) — kıyılar hafif yüksek (~2 m)
YÖNELME       kamera nehir EKSENİNE DİK · bakış 350° (kuzeye)
```

---

## 3. 16:9 KAMERA HESABI (MAIN STATION)

```
MAIN STATION   sağ (güney) kıyısı · kayalık platform · h = 3,50 m · D = 55,0 m (köprü merkezine)
BAKIŞ          350° · tilt 0° · f = 24 mm
               16:9 · yatay FoV ≈ 73° → 55 m mesafede: genişlik ≈ 77 m (köprü 40 m → kadrajın %52)

ÇAPALAR
  ① büyük meşe ağacı (SOL kıyı · kuzey yakası)  %x 12–20 · ≈200 px boy · KANIT NESNESİ
  ② kayalık çıkıntı (SAĞ kenar · güney yakası)   %x 78–88 · ≈160 px geniş
  ③ nehir yüzey bandı (kadraj ortası)             %y 38–48

KADRAJ HESABI (tilt 0 · h=3,50 · f=24)
  ufuk çizgisi          %y 50,0
  nehir tabanı (0 m)    %y ≈ 43,7
  tabliye (2,0 m yüzey) %y ≈ 48,7
  kemer tepe (8,0 m)    %y ≈ 66,7   ← G12'de tam orada
  kemer inşaat ara (4m) %y ≈ 57,7   ← G4–G7 arası
  geçici kule tepesi (10 m) %y ≈ 70,0

VİNÇ BOM BAŞI  h ≈ 14 m → %y ≈ 82,7 → GÖKYÜZÜNDE (bom arka planda ağaç önünde okunur)
```

---

## 4. IŞIK GÜNÜ VE MEVSİM

```
TEK GÜN PENCERE   08:00–18:00 (Σ 10 h · gölge ışık taşıyıcı)
SAHNE SAATLERI    S0 08:00 · S1 09:00 · S2 10:00 · S3 10:30 · S4 11:00 · S5 09:30
                  S6 09:00 · S7 10:00 · S8 11:00 · S9 10:30 · S10 16:00 · S11 17:30
REJIM             S0–S4, S7–S11 → rejim B (genel)   S6 → rejim A (yakın detay taşkın)
TAKVİM            Nisan(S0)→Temmuz(S4)→Kasım(S5)→Ocak(S6)→Mart(S7)→Nisan(S8)→Temmuz(S11)
                  = ~15 ay · film "about a year" der [P1-c]

MEVSİM TAŞIYICISI (bu filmin en güçlü silahı)
  S0–S4   Bahar–Yaz      meşe KOYU YEŞİL yaprak · nehir MAVİ düşük · gökyüzü açık
  S5      Sonbahar       yapraklar SARI-TURUNCU · nehir YÜKSELIYOR · gökyüzü gri
  S6      Kış            dallar ÇIPLAK · nehir TAŞKIN KAHVERENGİ · gri gökyüzü · çamur
  S7      Erken bahar    ilk TOMURCUKLAR · su çekilmiş · zemin ıslak kahverengi
  S8–S10  Bahar–Yaz      yeniden KOYU YEŞİL — ama kesim açıklığında GENÇ FİLİZ
  S11     Geç Yaz akşamı altın saat · nehir mavi düşük · ağaçlar tam yapraklı
```

---

## 5. ÜRETİM RİSKLERİ

```
R1 KÖPRÜ ÇOĞALIYOR   "bridge" → model ikinci köprü / viyadük üretir [DERS 55]
   ÇÖZÜM             "one single pedestrian footbridge spanning a 40-metre river gap …
                      the only crossing visible, every other reach of river is bare"

R2 KONSOL HAVADA YÜZÜYOR  model IPE kemer parçasını havada asılı çizer [DERS 57]
   ÇÖZÜM             Her I2V'de: "the partially assembled arch rests continuously on
                      the temporary steel support tower below — not suspended in air"

R3 NEHİR YATAĞı SU HAVUZU OKUNUYOR  düz + ıslak + taşlı nehir yatağı = "basin" [DERS 54]
   ÇÖZÜM             G0–G2 görsel: "the riverbed is dry and sandy, scattered cobblestones,
                      no standing water — temporary coffer dam not yet installed"

R4 YAPRAK DEĞİŞİMİ ANIDEN ATLADI  mevsim tek sahnede değişemez [DERS 7 prensip]
   ÇÖZÜM             S4 son saniyelerinde sararmaya başlar; S5 tam sarı-turuncu

R5 İŞÇİ GÖRÜNMÜYOR / NETLEŞİYOR  "no workers" yazmak işçi doğurur; netleşme = CGI [DERS 33]
   ÇÖZÜM             "workers move as blurred motion traces only, never sharp"

R6 ORTA AÇIKLIK SAHNESINE BAŞKA ŞEY SIKILMADI  S8 yalnız kapanış anı [köprü kartı §3 risk]
   ÇÖZÜM             S8 prompta yalnız son kaynaklanma yazılır; başka ilerleme eklenmez
```
