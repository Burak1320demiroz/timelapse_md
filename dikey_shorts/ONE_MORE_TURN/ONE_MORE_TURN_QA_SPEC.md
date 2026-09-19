# 🔍 ONE MORE TURN — QA SPEC

> Kilit listesi. Mercekler bu dosyayı GÖRMEZ (mod V: ① ③ ⑤ ⑦).
> Plan: `ONE_MORE_TURN_DIKEY_TIMELAPSE.md` · Günlük: `..._URETIM_GUNLUGU.md`

```
FİLM      ONE MORE TURN · 6 × 8,0 = 48,0 sn · KAPAK KARTI YOK · LOGO YOK
SCENE BLOCK / END CARD    48,0 sn / yok
FORMAT    İKİ KEYFRAME ZİNCİRİ · 7 görsel (G0…G6) + 6 I2V · T2V yok
REJİM     S0–S3 B (2 sa) · S4–S5 ⭐ G gerçek zaman 1× — depoda İLK, ölçülmedi
```

---

## 1. ⛔ FİNAL KARE KANITI

```
ffmpeg -ss 46.0 -i teslim.mp4 -frames:v 1 kanit.jpg

O KAREDE ÜÇÜ DE GÖRÜNMELİ, BU SIRAYLA [P1-h]:
  ① DÖNEN çark — 8 kol, 2 halka, 24 kova; sol yarı ISLAK, sağ yarı kuru
  ② ağızdan kovaya dökülen su — kaynak (oluk ağzı, saat 11) ve hedef (kova) birlikte
  ③ beyaz çıkış oluğu — çukurdan basamakların yanından dereye

⛔ Üçünden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
⛔ 46,0'ta çark HAREKET HÂLİNDE olmalı: 46,0 ve 47,0 karelerinde işaretli kol
   farklı açıda (≈ 45°). Duran çark = S5 atılır.
⛔ 48,0'da film çark DÖNERKEN kesilir; sonrasında kart, logo, fade YOK.
```

## 2. Kadraj kilitleri — her karede ölçülür

| ne | beklenen | tolerans |
|---|---|---|
| ufuk | %50,0 | ±0,5 puan |
| mil merkezi (y) | %54,4 | ±0,5 puan · YEDİ KAREDE DE |
| mil merkezi (x) | %46,1 | ±0,5 puan · YEDİ KAREDE DE |
| ⭐ duvar köşesi (x) | %82,4 | ±0,5 puan · YEDİ KAREDE DE (I2V çapası) |
| çark tepe (G0 üst-sağ · G3–G6) | %73,0 | ±1,5 puan |
| çark alt (G0 · G3–G6) | %35,9 | ±1,5 puan |
| çark çapı (G3–G6) | 711 px | ±25 px |
| oluk hattı | %75,9 | ±1 puan |
| saçak / mahya | %62,6 / %80,2 | ±1 puan |
| kaya (dere, sol alt) | %29,5 | ±1 puan · hiç kıpırdamaz |
| çıkış oluğu bandı | %28–36 | alt %25 UI bandının ÜSTÜNDE |
| figür (G4–G6) | 236 px · x ≈ %13 · baş %54 | ±20 px |

## 3. ⭐ ÇARKIN İLERLEYİŞİ — sahne sahne, elle sayılır

```
G0  ESKİ çark · kol 6/8 · halka üst-sol çeyrekte YOK · kova 18/24 · sarmaşık alt-sol üçte bir
    · halat GERGİN · işaretli kol saat 12 · römork BOŞ, sol kenarda kesik
G1  kol 0 · halka 0 · kova 0 — YALNIZ demir göbek + mil, iki dikme · sehpa solda ·
    römork DOLU (gri ahşap + sarmaşık) · ⛔ göbekte hayalet kol YOK
G2  kol 8 (yeni, pale) · halka 0 · kova 0 · yatak ayağı taze harçla · sehpada halka parçası
    · römorkta 16 parça + kova demeti + 3 tahta
G3  kol 8 · halka 2 (KAPALI) · kova 24 · KURU · halat BAĞI halkadan ayağa ·
    römorkta yalnız 3 tahta · oluk hâlâ birikintili
G4  TAM çark · kuru · SERBEST (bağ yok, dikme yok, sehpa yok, römork yok) · oluk YENİ ·
    kapak KAPALI · figür çıkrıkta, iki el, sırtı dönük · işaretli kol 12
G5  kapak AÇIK · su oluğun tamamında ve ağızda · 3 kova dolu · ⭐ işaretli kol 11 ·
    ilk sızıntı çıkış oluğunda · figür tek el
G6  DÖNÜYOR · sol yarı ıslak · sağ alt kovalar boşalıyor · ⭐ işaretli kol YİNE 11 ·
    çıkış oluğu beyaz · figür bir adım geri

⛔ GERİ GİDİŞ YOK: bir karede inen eski parça sonraki karede görünmez; bir karede
   takılan yeni parça sonraki karede eksilmez.
⛔ IŞINLANMA YOK: römork yalnız S1 (gidiş-dönüş) ve S3 (çıkış) kliplerinin İÇİNDE yer
   değiştirir; G1→G2 arası "dolu → yeni yük" geçişi S1 klibinde GÖRÜNÜR.
```

## 4. ⭐ SU KAPISI — S4 ve S5 [P3-d benzeri]

```
① KAYNAK GÖRÜNÜR    su, oluğun sol ucundaki kapak tahtasının altından çıkar; su cephesi
                    oluğu %8 → %30 KOŞAR (S4 1,0–3,0 sn) — birden dolu oluk YOK
② HEDEF GÖRÜNÜR     su ağızdan (saat 11) kovaya düşer; ağız ve kova aynı kadrajda
③ ZİNCİR            ağız → kova → çukur → çıkış oluğu → dere: G6'da beşi de tek çizgi
⛔ Su duvardan, çatıdan, boşluktan ya da çarkın kendisinden GELMEZ.
⛔ Kapak açılmadan oluğa su gelmez; S4'te ÖNCE çıkrık ve kapak, SONRA su.
④ ISLAKLIK YÖNLÜDÜR: inen (sol) yarı ıslak, çıkan (sağ) yarı kuru — ilk turda sağ yarı
   ıslanmaz. G6'da sağ yarı pale meşe kalır.
```

## 5. ⭐ RİJİT DÖNÜŞ KAPISI — S4 ve S5 [günlük §0 ⑯]

```
① SAYIM          0 · 4 · 8 sn karelerinde kol 8, halka 2 daire, kova 24 — sayı DEĞİŞMEZ
② YÖN            saat yönünün TERSİ (su soldan, iniş solda, boşalma sağ altta)
③ AÇI            S4: işaretli kol 12 → 11 (35–45°) · S5: 11 → 11 (360° ± 30°)
④ HIZ            S5'te sabit; ivmelenme yalnız 0,0–2,0 sn'de
⑤ MİL SABİT      göbek merkezi yedi karede ve klip boyunca aynı piksel (≤ 2 px)
⛔ Kolların bükülmesi, halkanın yumurtalaşması, kovaların birbirine karışması,
   çarkın sağa-sola sallanması = KLİP ATILIR, prompt değil ARAÇ sorgulanır.
⚠️ G5 ≈ G6 (bir tam tur) → model S5'i DURGUN verebilir. Kanıt: §1'deki 46,0/47,0 açı farkı.
```

## 6. ⭐ TEK ÇARK KAPISI [DERS 55]

```
SAYIM   göbek 1 · mil 1 · oluk 1 · ağız 1 · kapak tahtası 1 · çıkış oluğu 1 — YEDİ KAREDE DE
⛔ İkinci çark, ikinci oluk, çift ağız, duvarın öbür yüzünde çark = KARE ATILIR.
⛔ G1'de göbek ÇIPLAK (sekiz boş yuva): göbekte kol, halka parçası, hayalet çember = KARE ATILIR.
⛔ Bu, araç kapısının ⑨ SAYIM TESTİ'yle ÖNCEDEN ölçülür; kapıda çıkarsa ARAÇ DEĞİŞİR.
```

## 7. ⭐ REJİM G KAPISI — S4 · S5 [SANTIYE_HAREKETI §1 · ölçülmedi]

```
① GÖLGE SABİT     G4 · G5 · G6'da çarkın duvardaki gölgesi aynı açıda (0° fark)
② DERE DALGALI    ipek/bulanık dere = rejim ihlali; kaya çevresinde dalga okunmalı
③ İZ YOK          motion streak, bulanık ekip, hayalet nesne YOK
④ FİGÜR           tek · sırtı kameraya · yüz okunmaz · G4 iki el, G5 tek el, G6 adım geri
⑤ HIZ             1×: kapak 0,4 m / 1,5 sn · çark 1 tur / 8 sn (7,5 d/dk — hesap)
⛔ Bunlardan biri düşerse S4/S5 yeniden üretilir; rejim G'nin depo notu günlük §6'ya
   ölçüm olarak yazılır [DERSLER adayı].
```

## 8. Zaman ve ışık

```
IŞIK GÜNÜ   10:10 → 18:10 = 8 sa 00 dk · 4×B + 2×G (G ışık gününe 0 dk) ≤ 14 sa
GÜNEŞ       kadrajda HİÇ görünmez (bakış 30°, kadraj az 7°–53°) · disk anılmaz [DERS 39]
GÖLGE       10:10 sola · 12:10 kısa · 14:10 sağa · 16:10 uzun sağa · 18:10 turuncu sıyırıcı
G4–G6       IŞIK AYNI — LIGHTING bloğu üç karede birebir; gölge kıpırdamaz
MEVSİM      geç yaz · tek gün · yamaç koyu yeşil · dere alçak
⛔ KIŞ YOK — tek günlük film [DERS 7 · 26]
```

## 9. Bilinen riskler — mercek bunu bulursa BEKLENEN

```
⑥ METRONOM        süreler eşit (6 × 8,0) — proje sahibinin kesin kuralı, beyanlı
① / ③ DERE DİKİŞİ 32,0 kesmesinde dere ipekten dalgaya döner (B → G) — beyanlı [plan ⑩];
                  müziksiz 30,0–32,0 penceresi bunu taşır; yeniden üretim sebebi DEĞİLDİR
⑦ S5 "İŞSİZ"      S5'te iş yoktur, ÖDÜL vardır — usta kare kasıtlı [plan §KONSEPT KAPISI ④]
⚠️ ÇOĞUL ÇARK     beklenen DEĞİL — çıkarsa §6 gereği araç değişir
⚠️ DURGUN S5      beklenen DEĞİL — çıkarsa §5 gereği klip atılır
```
