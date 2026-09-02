# 📋 THE MOUNTAIN DOOR — QA KAYDI

```
FİLM        THE MOUNTAIN DOOR — Dağın Kapısı
            teslim başlığı: "THEY CUT A DOOR INTO THE MOUNTAIN"
FORMAT      9:16 · 5 sahne × 6,0 sn = 30,0 sn + kapak kartı = 0:34,0
            ızgara 5 × 6,0 DÜZ (proje sahibi kilidi)
PLAN        dikey_shorts/THE_MOUNTAIN_DOOR/THE_MOUNTAIN_DOOR_DIKEY_TIMELAPSE.md
SPEC        THE_MOUNTAIN_DOOR_QA_SPEC.md — ⭐ ÜRETİMDEN ÖNCE yazıldı
PROMPT KAPISI  ✅ GO — deponun ilk temiz geçişi, üretimden ÖNCE koşuldu
ÖLÇÜM       6/6 mercek koşuldu · ham çıktı QA/HAM_RAPORLAR/THE_MOUNTAIN_DOOR_*
```

⛔ **BU FİLM DEPONUN EN AĞIR ÖLÇÜMÜDÜR VE SEBEBİ ÖĞRETİCİDİR:**
prompt kapısından **GO** alan tek film, altı merceğin **beşinde** düştü.
Kapı biçimi denetler, üretimi denetlemez — ve bu, kapının bir kusuru değil
sınırıdır [AGENTS §6]. Bir filmin kâğıt üstünde doğru olması, üretilirken
doğru üretileceğini garanti etmez.

---

## 1. ALTI HÜKÜM

| Mercek | Mod | Ham ort. | VERDICT |
|---|:---:|---:|---|
| ① KARE | V ⚠️ karesiz | 1,1 | ⛔ **SIX SEPARATE SHOTS** |
| ② İNŞA | ⛔ V belgesiz | 1,5 | ⛔ **DIFFERENT · APPEARING** |
| ③ ZAMAN | ✅ **V tam** | **3,6** | ⛔ **PASSES BUT NOT IN ONE DIRECTION** |
| ④ TESLİM | ⛔ V belgesiz | 4,0 | ⚠️ ENDS · ⛔ **NONE FOUND** |
| ⑤ DEVAMLILIK | V ⚠️ karesiz | 0,2 | ⛔ **A SET REBUILT EACH TIME** · NONE FOUND |
| ⑥ GEÇİŞ | ⛔ V belgesiz | 3,5 | ⛔ **NEXT · METRONOME** |

```
⭐ TEK OLUMLU ÖLÇÜM: ③ SEASON CARRIER 10/10 · VEGETATION 10/10 ·
   SHADOW VS SUN HEIGHT 8/10 · ve zaman tahmini "about 9 to 12 months"
   plandaki 12 ayı TUTTURDU (deponun ikinci tutan tahmini).
⛔ Geri kalan her şey düştü.
```

---

## 2. ⚠️ MOD DENETİMİ — ALTI MERCEĞİN BEŞİ EKSİK GİRDİYLE KOŞTU

```
① KARE        ⛔ kare grabı verilmedi  (kare_al.sh koşulmadı)
② İNŞA        ⛔ QA_SPEC verilmedi     ← SPEC ÜRETİMDEN ÖNCE HAZIRDI
③ ZAMAN       ✅ TAM — girdisi yalnız tam kurgu, eksiksiz verildi
④ TESLİM      ⛔ plan ve kapak verilmedi
⑤ DEVAMLILIK  ⛔ kare grabı verilmedi
⑥ GEÇİŞ       ⛔ plan verilmedi · ⛔ filmde SES YOK
```

⛔ **BU, DERS 17'NİN İKİNCİ ÖLÇÜMÜDÜR VE İLKİNDEN DAHA AĞIRDIR.**
NARROW LOT'ta belge YOKTU — bu yüzden verilemedi. Bu filmde belge **vardı**
ve **üretimden önce özellikle bunun için yazılmıştı.** Yine verilmedi.

```
⭐ Yani DERS 17'nin çözümü "SPEC'i erken yaz" değilmiş. SPEC erken yazıldı
   ve hiçbir şeyi değiştirmedi. Eksik olan BELGE değil, KOŞU YORDAMI.
   → DERS 27
```

② ④ ⑥'nın skorları bu yüzden **tabloya yazılmadı**; bulguları geçerlidir.

---

## 3. ⛔ EN AĞIR ÜÇ BULGU

### ① CAMERA LOCK 0/10 — beş klibin beşinde de push-in

```
"Slow, continuous push-in movement throughout the clip."
0:00,0 · 0:06,0 · 0:12,0 · 0:18,0 · 0:24,0 — beşi de.
```

⭐ **VE ÖLÇÜLEBİLİR ÇAPA CÜMLESİ BEŞ I2V'NİN BEŞİNDE DE YAZILIYDI:**

```
"The framing is identical in the first frame and in the last frame: the
 clefted rock buttress on frame right occupies exactly the same width of the
 frame at both ends of the shot, and the horizon stays at exactly half the
 frame height throughout. The camera does not move at any point."
```

Aynı cümle NARROW LOT'ta `① CAMERA LOCK 10/10 · FRAME IDENTITY 10/10` almıştı.
Aynı cümle, iki farklı araç, iki zıt sonuç → **DERS 23**.

⛔ Ve ufuk hiç %50'de olmadı: ölçülen %62 → %67 (yayılım %5).
Plan %50,0 ± %2 diyordu. Kadraj hesabı (`h=16,0 · D=48`) ekrana hiç ulaşmadı.

### ⑤ KANIT NESNESİ KAYBOLDU — 0,2/10 · NONE FOUND

Plana **kasten** bir kanıt nesnesi yerleştirilmişti (NARROW LOT'un "coiled
hose" kazanımını tekrarlamak için): *"one flat-topped granite boulder 2.4
metres across, too large to move"*, beş görsel promptun beşinde de birebir.

```
⑤ bulgu 6:  [0:05,9] -> [0:06,0]
"A massive rock boulder resting on the gravel to the left of the excavation
 site vanished completely."
```

⛔ **Yani plandaki kanıt nesnesi, filmin İLK dikişinde kaybolan şey oldu.**
Dört dikişin dördü de kusur taşıyor; eski geçit yolu iki kez rota değiştirdi,
taş köprü düz taştan kemere dönüştü → **DERS 25**.

### ③ SEASON ORDER 0/10 — sonbahar hiç gelmedi, erime YAZ oldu

```
PLAN     yaz → sonbahar → kış① → kış②(erime) → yaz          = 12 ay
EKRAN    yaz → yaz      → kış  → yaz          → yaz
```

⛔ S1'in sonbaharı (pas kahvesi çim + boynuzda ilk kar) hiç üretilmedi.
⛔ S3 "kış ② · erime" olarak yazılmıştı; **tamamen yaz olarak üretildi.**
Sonuç: kış tek sahneye düştü (DERS 7 ihlali) ve mevsim GERİ gitti
(③ hükmü: `PASSES BUT NOT IN ONE DIRECTION`).

⭐ Ve DERS 21'in hazırlık cümleleri S1 ve S3 I2V'lerinde YAZILIYDI:
*"In the last second of the shot the first snow begins to settle…"* —
⑥ C2 SEASON CHANGE **0/10** verdi. Cümle yazıldı, üretilmedi → **DERS 26**.

---

## 4. ⛔ RİTİM — METRONOM ÜÇÜNCÜ KEZ, ve telafi DÜŞTÜ

```
⑥ RHYTHM AND PATTERN 0/10 — deponun en düşük ritim skoru
"identical 6-second cut intervals, resulting in a perfectly rigid metronome
 structure with no editorial arc, building tension, or released pacing"
```

Plan §2 bu riski **önceden yazmıştı** ve bir telafi öneriyordu: kesme aralığı
sabit kalsın, varyans klibin İÇİNE taşınsın — iş adımı her klipte başka bir
saniyede patlasın (1,2 · 3,6 · 4,8 · 2,4 · 5,0).

⛔ **TELAFİ ÖLÇÜLDÜ VE DÜŞTÜ.** Üstelik CLOSING SPAN (10 eşit kesme, 0/10) ve
NARROW LOT'tan (4 eşit kesme, 4/10) daha kötü. → **DERS 24**

---

## 5. ⛔ ④ "NONE FOUND" — DÖRDÜNCÜ KEZ, ve bu sefer BEDEL YAZILIYDI

Üç filmde bu satır boş geldi çünkü BEDEL hiç yazılmamıştı. Bu filmde **iki**
bedel plana, SPEC'e ve S4 promptuna yazıldı:

```
① dağın yüzündeki kalıcı açık renkli yara + pasa sekisi
② üstteki eski geçit yolunun boş kalması + ağzını kapatan kum bariyeri
```

⑤'in ölçümü ikisinin de neden ekrana ulaşmadığını açıklıyor: **pasa bermisi
hiç birikmedi** (0:11,9→0:12,0'da yok oldu) ve **eski yol iki kez rota
değiştirdi**, yani "aynı yol, artık boş" karşılaştırması hiç kurulamadı.

⚠️ Bu satır mod V'de geldi (plan verilmedi) — ④ belgeyle TEKRARLANMALI.
Ama ⑤'in kanıtı, tekrarın da NONE FOUND vereceğini söylüyor.

---

## 6. ①'İN "QUESTIONS FOR THE DOCUMENT" CEVAPLARI

```
S1  Kamera tamamen sabit mi olacaktı, yoksa push-in planlı mıydı?
C1  ⛔ TAMAMEN SABİT. Plan §3: "bolted to a rock bench… The camera never
    moves". Push-in beş klipte de PLAN DIŞIDIR.

S2  Ufuk ve en yüksek arka plan nesnesinin hedef yüzdesi neydi?
C2  ufuk %50,0 (tilt 0° geometrisinin sonucu) · kaya yüzü tacı %83,3 ·
    portal kemer tacı %40,3 · yol platformu %27,8. Ölçülen ufuk %62-67.

S3  Klipler arası coğrafya farkları kasıtlı mı?
C3  ⛔ HAYIR. Beş çapa (iki yarıklı kaya burnu · iki virajlı eski yol ·
    2,4 m granit kaya · tek kemerli taş köprü · boyunlu sırt) beş promptta
    da BİREBİR aynı cümleyle yazılıydı. Hepsi üretim hatasıdır.

S4  Araçlar bulanık çizgi olarak mı planlanmıştı?
C4  ⛔ EVET. "Workers appear only as soft motion streaks… vehicles render as
    smeared light and colour trails" beş promptun beşinde de var.
```

## ③'ÜN "QUESTIONS FOR THE DOCUMENT" CEVAPLARI

```
S1  Mevsim takvimi ve toplam süre neydi?
C1  12 ay · Temmuz → Ekim → Ocak → Mart → Temmuz.
    ⭐ ③ filmden "9-12 ay" okudu — TUTTU. Film süresini doğru anlatıyor;
       anlatamadığı şey mevsimlerin SIRASI.

S2  Klip içi zaman sıkışması planlı mıydı?
C2  ⛔ EVET, tam metin beş görselde ve beş I2V'de: "Everything in this frame
    is time-lapsed at the same rate: the clouds, the shadows, the machines,
    the people and the vehicles…" TIME RATE yine 0/10 geldi.

S3  Beyan edilen güneş açıları neydi?
C3  S0 96°/30°→262°/26° · S1 136°/24°→224°/18° · S2 144°/14°→216°/12° ·
    S3 132°/26°→232°/20° · S4 72°/12°→96°/30°.
    ⛔ ③ beş klipte de gölge açı değişimini SIFIR ölçtü ve hepsinde ~45°
       sabit bir güneş gördü. Açılar hem görselde hem I2V'de yazılıydı.
```

## ⑤'İN "QUESTIONS FOR THE DOCUMENT" CEVAPLARI

```
S1  Eski geçit yolunun rotası değişecek miydi?      ⛔ HAYIR — kalıcı çapa ①②
S2  Branda ve malzeme kışa girmeden kaldırılacak mıydı?
    ⛔ HAYIR — söküm takvimi hepsini S4'ten ÖNCE diyordu, S2'den önce değil
S3  Alt köprü yenilenecek miydi?                     ⛔ HAYIR — kalıcı çapa ④
```

---

## 7. ⛔ KÖK SEBEP — üretim sırası, üçüncü kez

Plan §8 ters inşayı ve `zincir_kontrol.sh` kapısını yazıyordu. Ölçüm bu
adımın koşulmadığını güçlü biçimde gösteriyor:

```
⑤ dört dikişin DÖRDÜ de DEFECT  ·  ② STRUCTURE IDENTITY 0/10
① ANCHOR IDENTITY 0/10          ·  ⑥ ANCHOR SURVIVAL 0/10
```

Beş kare bağımsız üretilmiş bir filmin imzası tam olarak budur [DERS 5].
⚠️ Raporlar üretim sırasını göremez; bu bir çıkarımdır ve proje sahibi
tarafından doğrulanmalıdır. Ama zincir koşulduysa `zincir_kontrol.sh` çıkış
kodu 2 vermiş olmalıydı ve üretim durmalıydı.

⭐ **DERS 12 üçüncü kez doğrulandı:** yazılı kural kapı değildir. Bu filmde
kural yazılıydı, kapı da vardı — ama kapı KOŞULMADI.

---

## 8. KARAR

```
⛔ YAYINLANMAZ.
⛔ YENİDEN ÜRETİLMEZ — YENİDEN ÜRETİM YORDAMI DEĞİŞMEDEN bu film tekrar
   üretilirse aynı sonucu verir. Kusur promptta değil, AKIŞTA.

ÖNCE YAPILACAKLAR (v2'den ÖNCE):
1. ⛔ ARAÇ ÖLÇÜMÜ. Tek bir I2V test klibi üretilir ve YALNIZ şu sorulur:
   kamera hareket ediyor mu? Ediyorsa o araçla bu format ÜRETİLMEZ [DERS 23].
2. ⛔ TERS İNŞA + zincir_kontrol.sh FİİLEN koşulur. Kapı koşulmadan
   sonraki kare üretilmez.
3. ⛔ QA koşu yordamı yazılır: hangi merceğe hangi dosya verilecek [DERS 27].
4. Kar/pasa/eski yol: birikme ve boşalma PLANDA sahne sahne yazılır,
   promptta cümle olarak değil [DERS 26].

KABUL EDİLEN KUSURLAR (v2'de de kalacak):
· düz ızgara — proje sahibinin kilidi. ⛔ Ama klip içi telafi ÖLÇÜLDÜ ve
  düştü; v2'de telafi olarak SUNULMAZ, risk olarak yazılır [DERS 24].
· ④ ve ⑥ mod V'de koştu; skorları geçersiz. Belgeyle TEKRARLANACAK.

TEKRARLANACAK KOŞULAR (film değişmeden, yalnız girdi düzelterek):
② İNŞA    + QA_SPEC          ⑥ GEÇİŞ  + plan (ses yok, C7 yine ölçülemez)
④ TESLİM  + plan + kapak     ① ve ⑤   + kare_al.sh çıktısı
```

---

## 9. BU FİLMDEN ÇIKAN DERSLER

```
DERS 23  Ölçülebilir kamera çapası ARACA bağlıdır, prompta değil
DERS 24  Klip İÇİ vuruş varyansı metronomu kırmıyor — ölçüldü, düştü
DERS 25  Kanıt nesnesi YAZMAK yetmiyor; zincirden geçmeyen çapa ilk dikişte ölür
DERS 26  Prompta yazılan MEVSİM, plandaki mevsimi üretmiyor
DERS 27  Belgeyi erken yazmak DERS 17'yi çözmedi — eksik olan koşu YORDAMI
```
