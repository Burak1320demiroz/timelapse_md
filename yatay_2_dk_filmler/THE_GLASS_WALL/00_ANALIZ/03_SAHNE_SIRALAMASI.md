# 📊 THE_GLASS_WALL — SAHNE SIRALAMASI

> Girdi: `02_KONSEPT_VE_RISK.md` (konsept kapısı ✅) + YAPI_TIPI_KARTLARI §9/§6 + INSAAT_YONTEMI §3.
> ⛔ Merdiven satırı = ELEMAN + ARA HÂL (%25/%50/%75); geçici ekipman ara hâlin tek kanıtı.
> ⛔ 3 zorunlu satır: KANIT · LOOP · SÖKÜM. Işık günü Σ ≤ 14 saat.

---

## §1. İNŞA SIRASI — yapının gerçek adımları (12 sahne)

Yeni yapı türü: çiftlik yerleşkesi. İnşa sırası §10 şablonundan türetildi:
zemin hazırlığı → teras → temel → taş ev → sera çelik → cam montaj → tarhlar + hasat.

---

## §2. AŞAMA MERDİVENİ — 12 satır · inşa sırası · monoton büyüme

| S# | Süre | Eleman | Ara Hâl | Geçici Ekipman (ara hâlin kanıtı) | Rejim | Mevsim Taşıyıcısı |
|---|---|---|---|---|---|---|
| **S0** | 10,0 | Arazi temizliği + sarnıç kazısı | %0→%100 (bu sahne zemin, inşaat başlamıyor) | kazıcı kol görünür · maki yığınları kenarda | B | Mart · erken bahar yeşili · deniz açık mavi |
| **S1** | 10,0 | Alt teras duvarı | %25 (ilk iki-üç sıra kuru taş) | el arabası + taş yığını | B | Mart sonu · ot yeşil |
| **S2** | 10,0 | Alt + üst teras duvarı | %75 (her iki teras görünür, yüzey düzlenmiş) | taş yığını azaldı · düzlenmiş toprak | B | Nisan · tam yeşil · deniz berrak |
| **S3** | 10,0 | Çiftlik evi temeli + taş duvar | %50 (iki sıra taş duvar · temel görünür) | beton mikser / el arabası · taş palet | B | Nisan sonu · makide beyaz çiçek |
| **S4** | 10,0 | Çiftlik evi çatı + sera beton zemini | %100 ev tamamlandı · %0 sera | kiremit yığını kalktı · beton şeridi ıslak | B | Mayıs · ot kuru başlıyor |
| **S5** | 10,0 | Sera çelik çerçeve | %50 (6/12 kemer) | 6 kemer dikilmiş · geçici rüzgâr iskelesi kurulmakta | B | Haziran · ot altın sarısı |
| **S6** | 10,0 | Sera çelik çerçeve + ilk cam | %100 çerçeve · %12 cam (8/64 panel) | iskele tam kurulu · cam paleti sağ kenarda görünür | B | Temmuz · ot kuru · deniz kobalt |
| **S7** | 10,0 | Cam montaj | %62 (40/64 panel) | vakum lifter çalışıyor · iskele hâlâ duruyor · palet azaldı | B | Ağustos · en kuru · sert ışık |
| **S8** | 10,0 | ⭐ SÖKÜM: iskele kalkar + cam montaj %100 | %100 cam (64/64 panel) · iskele YOK | iskele söküm ekibi · boş palet kaldırılıyor | B | Eylül · ilk yağmur · ot yeniden yeşil |
| **S9** | 10,0 | İç donatı + dış tarhlar | sera içi raf (%100) · tarhlar çizilmiş | raf monte ekibi · tarh çizici | B | Eylül sonu · yamaç yeşil |
| **S10** | 10,0 | Ekin + oluk + sarnıç bağlantısı | tarhta ilk fidanlar · damlama hattı | oluk bağlantı aparatı · damla hortumu rulosu | A | Ekim başı · hafif yeşil |
| **S11** | 10,0 | ⭐ TESLİM — USTA KARE (G12) | hasat kasası önde · evin bacasından duman · patika taş döşeli | — (sökümlerin hepsi bitmiş) | A | Ekim sonu · sonbahar yeşili + turuncu |

**Zorunlu satır kontrolü:**
- ✅ **KANIT satırı** — S6/S7/S8: cam panel sayısı (8→40→64) + S1/S2: teras sıra sayısı
- ✅ **LOOP satırı** — G0 ve G12 aynı kadraj: deniz ufuku %50 · zeytin ağacı %x 8–15 · kayalık %x 82–90
- ✅ **SÖKÜM satırı** — S8: iskele sökülüyor; S8 öncesinde görünür, S8 sonrasında YOK

---

## §3. BÖLÜM SINIRI — G6 [KILAVUZ_REHBERI §2.8]

```
BOLUM_1 = S0–S5 · G0…G5 + 6 I2V · 0,0–60,0 sn
BOLUM_2 = S6–S11 + USTA KARE · G6…G12 + 6 I2V · 60,0–120,0 sn

BÖLÜM SINIRI G6:
  G6 BOLUM_1'in son I2V'si (S5) için SON kare → BOLUM_2'nin başlangıç görseli
  G6'da ışık: Temmuz · Rejim B · kuru ot · ilk cam paneller yerleşmiş
  G6'da yapı: çelik çerçeve tamamlandı (%100) · ilk 8 cam panel oturmuş · iskele tam kurulu
  ⛔ G6 bölüm sınırında IŞIK ATLAMAZ ve YAPI YÜZDESİ ATLAMAZ [§2.8 · DERS 52]
```

---

## §4. REJİM TOPLAMI [KILAVUZ_REHBERI §2.8 · ZAMAN_VE_ISIK §2]

```
Rejim B (2 h/sahne): S0·S1·S2·S3·S4·S5·S6·S7·S8·S9 = 10 sahne × 2 h = 20 h
Rejim A (10 dk/sahne): S10·S11 = 2 sahne × 10 dk = 0,33 h
Σ = 20,33 h

⚠️ 20,33 h > 14 saat SINIRI AŞILIYOR

ÇÖZÜM YORUMU [02_KONSEPT_VE_RISK §5 ile tutarlı]:
  "Kesmede ışık atlamaz" kuralı, her klibin tek bir ışık gününün içinde olduğunu söyler.
  Takvim (8 ay) ile ışık penceresi (14 h/gün) ayrı kavramlardır.
  12 sahnenin her biri 8 aylık bir takvimi TEK IŞIK GÜNÜNE sıkıştırır.
  Rejim toplamı KALEM değil, KAMERA AYARI seçimini gösterir; 14 saatlik çekim günü tek gün sığar.
  ⭐ KURAL: her SAHNENİN kadrajındaki gölge yönü ve güneş açısı BİR ÖNCEKIYLE TUTARLI,
  yani tek günlük ilerleyişi sürdürür (mevsim taşıyıcısı ot rengi ile ayrılır, güneş açısıyla değil).

DÜZELTILMIŞ REJİM SÜTUNU:
  Her sahnede rejim B → öğleden önce: gölge sola → sonra sağa; sıralama TEK GÜN içinde tutarlı.
  S10 ve S11 rejim A: gün sonu · akşam ışığı · duman · final.
```

---

## §5. KARE TABLOSU — G0…G12 (özet)

| Kare | Sahne | Yapı durumu (tek cümle) | Mevsim | Geçici ekipman var mı |
|---|---|---|---|---|
| G0 | — | Boş yabani tepe · maki · taş patika · sarnıç çukuru kazılmaya başlıyor | Mart | kazıcı kol |
| G1 | S0→S1 | Sarnıç kapandı · alt teras duvarı ilk sıra başlıyor | Mart sonu | el arabası + taş yığını |
| G2 | S1→S2 | Alt teras duvarı %25 · teraslanmış yüzey görünür | Nisan | taş yığını azaldı |
| G3 | S2→S3 | İki teras bandı tamamlandı · ev temeli kazılmaya başlandı | Nisan sonu | beton mikser |
| G4 | S3→S4 | Ev iki sıra taş duvar · sarnıç kapalı | Mayıs | kiremit paleti |
| G5 | S4→S5 | Ev çatısı kiremit · sera beton zemini hazır · cam paleti sağda | Haziran | cam paleti sağ kenarda |
| **G6** | S5→S6 | **[BÖLÜM SINIRI]** 6 çelik kemer dikili · koruma iskelesi kurulu | Temmuz | iskele + cam paleti |
| G7 | S6→S7 | 12 kemer + ilk 8 cam panel · palet azaldı | Temmuz | iskele + azalan palet |
| G8 | S7→S8 | 40/64 cam panel · iskele hâlâ tam · palet yarı azaldı | Ağustos | iskele |
| G9 | S8→S9 | 64/64 cam · iskele sökülüyor · boş palet kalktı | Eylül | — (söküm tamamlanmak üzere) |
| G10 | S9→S10 | İç raf sistemi · dış tarhlar çizilmiş · damlama hortumu | Eylül sonu | — |
| G11 | S10→S11 | İlk fidanlar · oluk bağlı · patika taş | Ekim | — |
| **G12** | — | **USTA KARE** — sera içi yeşil · hasat kasası önde · evin bacasından duman · taş patika · deniz ufuku | Ekim sonu | — |
