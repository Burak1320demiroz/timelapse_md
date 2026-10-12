# 🎶 THE_FIRST_LIGHT — MÜZİK + SES

**Kaynak:** sahip senaryosu TUR 3, 10.10.2026 ("vinç, metal, motor ve dağ rüzgârı önde; altında düşük seviyeli, sözsüz
sinematik müzik" · ses planı 00:00–02:40 · "müzik klip üretimlerinin içinde ayrı ayrı üretilmez; 160 saniyelik bütünün
üzerine kurgu aşamasında yerleştirilir") · hikâye SAPMA ⑮ · `MUZIK_VE_KAPAK.md` §1 · ses hedefi `KURGU_VE_TESLIM` §4

```
KARAR         ✅ MÜZİK VAR — düşük seviyeli, sözsüz, melodi hattı yok. ⭐ DİEGETİK YATAK ÖNDE, müzik altta [§1.3 · A1-c]:
              her sahnenin kendi makine/malzeme sesi önce duyulur; müzik zemin ve nabızdır, taşıyıcı değildir.
              Sahip senaryosu TUR 3'te müziği açıkça yazdı (TUR 2'deki "varsayıldı" notu kapandı).
TEMPO         120 BPM · ölçü 2,0 sn · ⭐ 8,0 sn = 4 ölçü/sahne · 20 sahne = 80 ölçü · BPM = 240 × 4 ÷ 8,0 = 120 [§1.1]
KESMELER      8,0 · 16,0 · … · 152,0 (19 kesme) — her kesme bir ölçünün 1. VURUŞUNDA [A2-e] · istasyon kesmeleri (136,0 ·
              144,0) aynı vuruşta, ses mekânı değişir (dış ↔ kubbenin içi), seviye değişmez · 88,0 (kubbe asılı) kesmesinde
              ses KESİLMEZ: vinç motoru iki klipte aynı sürer (tek olay)
MÜZİKSİZ      0,0–1,5 sn: yalnız saha sesi (vinç motoru, rüzgâr) — kanca diegetik sesle açılır [§1.3]; uzun sessiz giriş YOK
              (sahip senaryosu)
SÜRE          160,0 s = sahne bloğu (kart YOK) · son 4 sn müzik çözülür, rüzgâr ve bulut denizinin sesi kalır, ANİ KESİLME YOK
KAYNAK        her saha sesi bir GÖRÜNEN kaynaktan gelir (diegetik): görünmeyen makinenin sesi konmaz [A1-c] · kapak, teleskop ve
              kubbe motoru yalnız hareket ettikleri saniyelerde · ⛔ görüntüde olmayan sert çarpışma efekti YOK · ⛔ "uzaydan
              gelen ses" YOK (senaryo kuralı)
TELEFON       missing fundamental: "Every sub-bass element below 150 Hz is doubled by its own upper harmonics at roughly
              100, 150 and 200 Hz so the fundamental is implied rather than required; the low end is never the only
              carrier of the weight." [§1.3]
SES HEDEFİ    −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP · mono uyumlu · vinç motoru ve kubbe motoru merkezde
LİSANS        ⬜ müzik kaynağı ve lisansı + ses efekti kütüphanesi (kullanılırsa) günlük §5'e, yayından ÖNCE
              (POLITIKA_VE_RISK §1 · telif)
```

---

## 🎚️ KATMAN = KAT — 20 sahnede beş katman [§1.2]

> Katman eklenir, hiçbiri çıkmaz — aşama merdiveninin monoton büyümesinin sesteki karşılığı. Sahibin ses planına oturur:
> bakımda alçak ritim, kubbede müzik genişler, tamamlamada makine sesi azalır (müzik tutar), kullanımda açılır.

```
S0–S3    ① kuru nabız — her ölçünün 1. vuruşunda alçak, yumuşak bir darbe            1 katman   (kubbe, tüp, temizlik, bakır)
S4–S7    ② alçak bas nota, hareketsiz, uzun                                        2          (ray, zemin, tüp bakımı, tüp geri)
S8–S9    ③ ince metalik doku — tek tek, seyrek çan/plaka vuruşları (hassas makine)  3          (ilk hareket, kapak)
S10–S11  ④ geniş, ılık yaylı yastık — kubbenin dönüşü, müzik GENİŞLER                4          (⭐ kalkış · ⭐ oturuş)
S12–S15  ①–④ tutar, makine sesi azalır, rüzgâr geri gelir                            4          (yol, korkuluk, söküm, vinç gider)
S16–S19  ⑤ yüksek, açık, sakin armoni — ilk ışık                                    5          (yarık · iç · dönüş · tutuş)
SON 4 SN hepsi çözülür ve söner; yalnız rüzgâr ve bulut denizinin hışırtısı
```

## 📝 MÜZİK PROMPTU [§1.4 iskeletinin 160 sn · 20 × 8 sn hâli]

```
Instrumental score for a 160-second horizontal restoration time-lapse: twenty 8-second shots, no end card.
No lyrics, no voice, no melody line, no traditional song structure. Low in the mix: it sits under the site sounds.

Genre: minimal ambient score, warm and patient, slowly opening.
Tempo: 120 BPM, strict and bar-aligned, four bars per 8-second shot.

Layers (added in order, none removed until the final bars):
1. [shots 1-4] a soft dry pulse on the first beat of every bar
2. [shots 5-8] a low sustained bass note
3. [shots 9-10] sparse, delicate metallic tones, one at a time
4. [shots 11-12] a wide warm string pad — the score opens up here
5. [shots 17-20] a high, open, calm chord — the widest and quietest moment

Dynamic map across 160 seconds:
  0.0-1.5      silence — only the site's own sound (crane engine, wind)
  1.5-32.0     layer 1 alone
  32.0-64.0    layer 2 enters
  64.0-80.0    layer 3 enters
  80.0-96.0    layer 4 enters, the score widens
  96.0-128.0   layers 1-4 hold steady and a little lower, leaving room for the wind
  128.0-156.0  layer 5 enters, the stack sits together, softly
  156.0-160.0  everything resolves and decays; the last 1.5 seconds carry only wind

Phone-speaker rule: every sub-bass element below 150 Hz is doubled by its own upper harmonics at roughly 100, 150 and
200 Hz so the fundamental is implied rather than required; the low end is never the only carrier of the weight.
```

> ⛔ Referans besteci adı yazılmadı (alıntı üretme riski — §1.4 "iki gerçek besteci" satırı bilerek boş; sahip isterse ekler).

---

## 🔊 SES TABLOSU — sahne sahne (dört perde: söküm → bakım → kubbe → ilk ışık)

| S | saniye | görünen kaynak | saha sesi (önde → arkada) | müzik katmanı | geçiş |
|:-:|:-:|---|---|:-:|---|
| 0 | 0,0–8,0 | vinç · havadaki kubbe · kamyon | ⭐ açılış: vinç motorunun uğultusu · gerilen sapanların metal gıcırtısı · zirvede rüzgâr · kılavuz ipte ekip | ① (1,5 sn'den) | ilk saniyeler müziksiz |
| 1 | 8,0–16,0 | vinç · tüp · beşik | vincin ağır yük sesi · beşiğe oturan çeliğin tok sesi · zincir ve kayış | ① | söküm |
| 2 | 16,0–24,0 | iskele kuleleri · basınçlı su · kasalar | basınçlı suyun taşta tıslaması · akan su · koparılan sarmaşık · kasaya düşen moloz | ① | temizlik |
| 3 | 24,0–32,0 | yürüme yolu · bakır levhalar · vinç | ince bakır levhanın esneme sesi · çekiç ve perçin tabancası (seyrek) · sökülen panelin istife düşüşü | ① | ⭐ renk dönüşümü |
| 4 | 32,0–40,0 | vinç · ray parçaları · ekip | çeliğin çeliğe oturuşu · darbeli anahtar · eski rayın istife bırakılışı | ①② | yenileme |
| 5 | 40,0–48,0 | vinç · zemin paneli paletleri | panellerin zemine konuşu (tok, ahşap) · eski tahtanın kasaya atılışı · rüzgâr | ①② | zemin |
| 6 | 48,0–56,0 | beşik · tüp panelleri | panel cıvatalarının sökülüşü · yeni panelin yerine oturuşu (yumuşak metal) · vinç motoru | ①② | tüp bakımı |
| 7 | 56,0–64,0 | vinç · tüp + çerçeve | uzun tüpün çatala yatışı (metal sürtünme, yumuşak) · cıvatalar | ①② | ⭐ tüp geri |
| 8 | 64,0–72,0 | teleskop · vinç · kamyon | ⭐ teleskop motorunun uzun, düz vınlaması (tüp dikilirken) · durunca tek tık · uzaklaşan kamyon | ①②③ | ⭐ ilk hareket |
| 9 | 72,0–80,0 | vinç · eski ve yeni kapak | kapağın kızaktan çıkış sürtünmesi · yeni kapağın kızağa oturuşu · cıvatalar | ①②③ | hazırlık |
| 10 | 80,0–88,0 | vinç · kubbe | ⭐ vinç motorunun yükselen gücü · dört sapanın gerilişi · rüzgârda kılavuz ipler | ①②③④ | ⭐ müzik genişler |
| 11 | 88,0–96,0 | vinç · kubbe · kamyon | ⭐ DORUK: inişte motorun yavaşlaması · kubbenin halka raya oturuşu (derin, yumuşak — sert çarpışma YOK) · gevşeyen sapanlar | ①②③④ | ⭐ oturuş |
| 12 | 96,0–104,0 | vinç · taş plakalar · ekip | taş plakanın kuma oturuşu · mala · uzak vinç | ①②③④ | tamamlama |
| 13 | 104,0–112,0 | vinç · korkuluk modülleri | korkuluk direklerinin cıvatası · metal tınısı · rüzgâr belirginleşir | ①②③④ | tamamlama |
| 14 | 112,0–120,0 | kuleler · kamyonlar · vinç | iskele borularının sökülüşü · yüklenen kamyonların motorları, uzaklaşır · akşam rüzgârı | ①②③④ | makine perdesi kapanır |
| 15 | 120,0–128,0 | vinç (bom iner, gider) · küçük kamyon | uzaklaşan paletli vinç · tırmık sesi · yalnız rüzgâr kalır | ①②③④ | ilk sessiz zirve |
| 16 | 128,0–136,0 | servis aracı · kapak · yol lambaları | ⭐ kapak motorunun uzun, düz sesi · kızakta kayan bakır · uzak kapı | ①–⑤ | açılış |
| 17 | 136,0–144,0 | KUBBE İÇİ: teleskop · masa · iki kişi | iç mekân: teleskop servosunun hafif vınlaması (ilk 3 sn) · defterin masaya konuşu · kubbenin içinde rüzgârın uğultusu | ①–⑤ | ⭐ iç ses |
| 18 | 144,0–152,0 | kubbe (döner) · servis aracı | kubbenin halka rayda dönüşünün derin, sürekli gürültüsü · durunca tek tık · uzak rüzgâr | ①–⑤ | dönüş |
| 19 | 152,0–160,0 | iki kişi · bulut denizi | kapının kapanışı (yumuşak) · terastaki adımlar · uzaklaşan araç · son 4 sn yalnız rüzgâr — söner, kesilmez | çözülür | sönüm |

```
VURUŞ NOKTALARI  dört: 0,0–8,0 (havadaki kubbe — vinç motoru) · 64,0–72,0 (tüpün ilk hareketi — ilk motor) · 88,0–96,0
                 (kubbenin halkaya oturuşu — derin, yumuşak) · 128,0–136,0 (kapağın açılışı — makinelerden sonra ilk motor)
                 — az olan güçlüdür
SESSİZLİK        yok; ama S15 (vinç gider) makine sesinin bittiği an ve S19'un son 4 sn'si yalnız rüzgâr
⛔ YASAK         şarkı · söz · trend ses · anlatıcı · insan konuşması · bilimkurgu "uzay" sesi · uzaydan geldiği iddia edilen
                 ses · görüntüde olmayan patlama, darbe ya da sert çarpışma (senaryo ses planı)
```
