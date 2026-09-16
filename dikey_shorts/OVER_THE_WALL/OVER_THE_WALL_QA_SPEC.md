# 🔍 OVER THE WALL — QA SPEC

> Rubriğe **mod D** koşularında verilir (② İNŞA · ④ TESLİM · ⑥ GEÇİŞ · ⑧ YÖNTEM).
> ⛔ ① KARE · ③ ZAMAN · ⑤ DEVAMLILIK · ⑦ İŞ merceklerine **VERİLMEZ** — o dördü dokümansız koşar
> [AGENTS değişmez ⑦]. Yorum yok, yalnız ölçülebilir kilitler. Sayıya çevrilemeyen kilit, kilit
> değildir; tariftir.

---

## 0. KÜNYE

```
FİLM          OVER THE WALL — boğazda beton ağırlık barajı, mansaptan
FORMAT        9:16 dikey · 1080×1920 · 30 fps

TESLİM YAPISI ⭐ SAHNE BLOĞU  8 sahne × 8,0 sn = 64,0 sn                  ← merceklerin konusu
              ⭐ KAPAK KARTI  1 × 5,0 sn        =  5,0 sn                  ← SAHNE DEĞİL
                 TOPLAM                           69,0 sn
              ⛔ Kart sahne bloğunun devamı DEĞİLDİR ve devamlılık karşılaştırmalarına GİRMEZ.
                 Ayrı denetlenir: "kart, S7'nin sonundaki barajın AYNISINI mı gösteriyor?"

SAHNE SAATLERİ  S0 0,0–8,0 · S1 8,0–16,0 · S2 16,0–24,0 · S3 24,0–32,0
                S4 32,0–40,0 · S5 40,0–48,0 · S6 48,0–56,0 · S7 56,0–64,0
                KART 64,0–69,0
                (120 BPM · ölçü 2,0 sn · 4 ölçü/sahne · her kesme ölçü başında)
⛔ DÜZ IZGARA   proje sahibinin kilidi (14.09.2026). ⑥ METRONOM hükmü BEKLENEN ve KABUL EDİLMİŞ
                risktir (plan §AŞAMA MERDİVENİ · DERS 24); hüküm gelirse "beklenen" diye kaydedilir,
                yeniden üretim sebebi sayılmaz. Ritim isteniyorsa SÜRE sütunu değişir, prompt değil.
⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [DERS 23 · D-d]:
   ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
   ARAÇ KUTU SETİ: ⛔ ÖLÇÜLMEDİ — ölçülünce buraya ve plana yazılır; her sahne 8,0 sn teslim
   → en büyük kutu ≥ 9,0 gerekir; {4,6,8} çıkarsa sekiz sahnenin sekizi iki zincirli klip
   (plan §DEĞİŞMEZLER · ARAÇ KUTU SETİ satırı).

YAPI          beton ağırlık barajı (silindirle sıkıştırılmış beton) · 72 m · kret 90 m · basamaklı mansap yüzü
SAHA          dağ / boğaz (SAHA_VE_IKLIM §3.4 + §3.5)
ZAMAN YAYI    ~12 ay (Ekim → Ekim) · film mertebe anlatır: "yaklaşık bir yıl" [P1-c]
KAMERA        MAIN STATION — tek istasyon, 8 sahne + usta kare · h 15,0 m · D_eksen 120 m · 350° · tilt 0°
ÜRETİM SIRASI ⛔ ters ve ZİNCİRLİ: G8 usta kare → G7 → … → G0 · her kare zincir_kontrol.sh
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S7
SANİYE      1:02,5   (S7'nin 6,5. saniyesi — son ≥2,0 sn'lik TUTUŞUN içi [P2-i])
GÖRÜLMESİ GEREKEN ŞEY (üçü de, bu sırayla — FİNAL HİYERARŞİ [P1-h]):
   ① Kadrajın ortasını dolduran BEYAZ ÇAĞLAYAN: iki KURU omuz arasındaki orta bölümün yuvarlak
      dudağından tabana kadar basamaklı yüzü örter (y ≈ %81 → %42). Omuzlar ve sağdaki yol
      sekisi KURU.
   ② Solda, orta yükseklikte SİYAH ve KURU derivasyon çıkış kemeri (tacı ufuk çizgisinde, %50).
   ③ Alt-orta bantta (y %36–42) üç kemerli köprü beyaz köpük ve suyun altında; en fazla
      parapet çizgisi görünür.
   + kret sağ duvardaki yol sekisiyle AYNI HİZADA (%81,7 ± 1,5).

KOMUT
   ffmpeg -ss 62.5 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ O karede çağlayan ORTA BÖLÜMDE değilse, omuzlar ıslaksa, kemer akıyorsa ya da köprü kuru
   duruyorsa film TESLİM EDİLMEMİŞTİR — klip sayısı ve süre tutsa bile.

⭐ KANIT ÇİFTİ — LOOP
   ffmpeg -ss 0.3  -i teslim.mp4 -frames:v 1 kanit_g0.jpg
   ffmpeg -ss 62.5 -i teslim.mp4 -frames:v 1 kanit_g8.jpg
   İki karede: çıkış kemeri (x ≈ %29 · y %43–50), köprü (x 309–771 px · y %36–42) ve çentikli
   silüet tam aynı yerde. Işık aynı DEĞİLDİR (08:00 → 16:20, bilinçli — plan LOOP satırı).
```

---

## 2. KADRAJ KİLİTLERİ — MAIN STATION (f=24 · h=15 · tilt 0 · yüzde = 50 + 0,667·(y−15)/D)

| Ne | Beklenen (kare yüksekliği) | Tol. | Hangi sahnelerde |
|---|---|---|---|
| ufuk çizgisi = portal kemerinin TACI | %50,0 | ±%1,0 | G0–G8 (hepsi) |
| portal kemeri (eşik → taç) | %43–50 · x ≈ %29 soldan | ±%1,5 | G0–G8 |
| köprü (taban → parapet) | %35,7–42,4 · x 309–771 px (≈460 px) | ±%1,0 · ±15 px | G0–G7 (G8'de su altında, konumu aynı) |
| yol sekisi (doğu duvar, kret kotu) | %81,7 | ±%1,5 | G2–G8 |
| duvar tepesi G3 (8 m) | %46,1 | ±%1,5 | G3 |
| duvar tepesi G4 (45 m) | %66,7 — ufkun ÜSTÜNDE | ±%1,5 | G4 |
| duvar tepesi G5 (52 m) | %70,6 | ±%1,5 | G5 |
| kret / omuzlar (72 m) | %81,7 = yol sekisi | ±%1,5 | G6–G8 |
| taşkın dudağı (70 m) | %80,6 | ±%1,5 | G6–G8 |
| çağlayan | %81 → %42 arası orta bölüm | — | G8 |

```
⛔ ÜST SINIR   hiçbir yapı parçası %87,5'in üstünde olamaz (kret %81,7 — 5,8 puan pay)
⛔ ALT SINIR   ilerlemeyi kanıtlayan hiçbir şey %25'in altında olamaz (köprü %35,7'de başlar)
⛔ SAĞ ŞERİT   kanıt nesnesi kare genişliğinin sağ %13'ünde (x > 838 px) duramaz
⛔ D_kenar     40 m'den yakın taban kadrajın alt %25'indedir (UI) — oraya hiçbir kanıt konmaz
⭐ PİKSEL      köprü ve kemer genişliği USTA KARE onaylanınca ölçülür, buraya ve plana yazılır
               [PERSPEKTIF §4]; yukarıdaki sayılar formül tahminidir.
⚠️ S3 tek klipte %46 → %67 tırmanır (8 → 45 m) — filmin en büyük tek-klip değişimi; ① merceği
   bu klipte köprü genişliğini (460 px) ÖZELLİKLE ölçer: duvar büyürken köprü küçülmüş mü?
```

---

## 3. YAPI BIBLE — sayılar (promptta yok, burada var) [P2-b · DERS 36]

```
duvar          düz beton ağırlık barajı · 72,0 m (taban kayası → omuz kreti) · kret 90 m · kret genişliği 8 m
               taban genişliği 54 m (0,75 H) · memba yüzü düşey · mansap yüzü 0,75:1, 3,0 m'lik 24 basamak
taşkın         orta bölüm 40 m geniş · dudak kotu 70,0 m (omuzlardan 2 m alçak) · yuvarlak dudak · kapaksız
omuzlar        iki uçta 25'er m · 72,0 m · korkuluk 1,1 m · kret yolu doğu omuzdan sekiye bağlanır
yol sekisi     6 m geniş · kot 72,0 m · doğu duvarı boyunca (G2'de tamam)
derivasyon     10 m çaplı tünel · GİRİŞ memba, batı duvar (uzak, küçük; G4'ten itibaren duvarın arkasında)
               ÇIKIŞ topuktan 25 m mansap, batı duvar · eşik +5 m · taç +15 m (= kamera yüksekliği = ufuk)
kapatma seddi  40 m · 10 m kaya dolgu · memba · G0 %75 → G1 %100 · gömülür, sökülmez
eski köprü     30 m · 3 × 8 m kemer · tabliye +6 m · parapet +7 m · genişlik 4 m · gri kesme taş
kamera         h 15,0 m · D_eksen 120 m · D_kenar 20 m · 350° · tilt 0° · roll 0° · 24 mm
makineler      sarı belden kırma damper (ölçek çapası, aynı model) · paletli ekskavatör (S0 sonu–S1) ·
               paletli dozer · titreşimli silindir · su tankeri (S6 sonu–G8) · VİNÇ YOK · kalıp YOK
```

### Duvar yüksekliği ve su durumu — sahne sahne (② İNŞA · ④ TESLİM için)

| G | duvar | kret/dudak | çıkış kemeri | yatak (köprü altı) | gözle görülmesi gereken ilerleme |
|:-:|---:|---|---|---|---|
| G0 | 0 | — | KURU (giriş de kuru) | vahşi nehir | sed ¾, dozer ucunda |
| G1 | 0 | — | JET güçlü | portal suyu | sed tamam; uzak yatak kuru; ilk seki yarası |
| G2 | 0 | — | jet | portal suyu | seki TAMAM (kret kotunda çizgi); taban duvardan duvara kaya; dozer + silindir + damper batı dayanağında; kar tabana kadar |
| G3 | 8 m | — | jet kahve | portal suyu, kabarık | platform iki damper boyu; sulu kar |
| G4 | 45 m | — | ŞİŞKİN torrent | SEL köprü direklerinde | tepe ⅔'te, ufkun ÜSTÜNDE; renk sınırı ⅔'te; duvar kuru; yamaç ıslak yeşil |
| G5 | 52 m | — | jet orta | portal suyu, köprüde sel çizgisi | tepe ¾'te |
| G6 | 72 m | kret + dudak TAMAM | jet YARIM | ince akış | kret = seki; omuzlar + dudak; döşek boş |
| G7 | 72 m | tamam | KURU, siyah | KURU taş | tanker sekide |
| G8 | 72 m | ÇAĞLAYAN | KURU, siyah | beyaz su, köprü gömülü | final |

⛔ Monoton büyüme: G(n) ≤ G(n+1) her satırda. Tek istisna yok — sökülen ekipman da yok.

---

## 4. "AYNI YER" NESNESİ VE ÇAPA KONTROLÜ [DERS 25]

```
NESNE        derivasyon ÇIKIŞ KEMERİ — batı duvar, 10 m geniş yarım daire, tacı %50'de, içi siyah
KONTROL      her zincir_kontrol.sh koşusunda ELLE: iki karede de aynı yerde, aynı boyutta mı? ✓/✗
             ✗ ise kare ATILIR — betik geçse bile.
İKİNCİ       köprü (G0–G7) · üçüncü: çentikli silüet · dördüncü (G2+): yol sekisi
⛔ NONE FOUND gelirse film aynı yerde geçmiyor demektir — yeniden üretim sebebi (kart R 6b).
```

---

## 5. ⑧ YÖNTEM DEFTERİ — her eleman: kaynağı · geçici desteği · ilk EKSİK görüldüğü kare [DERS 48 · FIZIK §2]

| Eleman | Hammaddesi nereden/nasıl geldi | Geçici destek / ara hâl kanıtı | İlk EKSİK görüldüğü kare | Tamam |
|---|---|---|---|:-:|
| kapatma seddi | damperle taşınan patlatılmış kaya (G0'da damper sedde) | gevşek dolgu, dozer bıçağı | G0 (%75) | G1 |
| yol sekisi | kaya KESİLİR (malzeme çıkar, girmez); pasa konisi altta büyür | raw cut scar · spoil cone | G1 (%10) | G2 |
| temel kazısı | çakıl sıyrılır, damperle sekiden çıkar (S1'in içinde, sekiyle aynı klipte) | bucket teeth marks · spoil pile | G1 (%0 — yatak çakıl) | G2 |
| duvar (katmanlar) | damper → dozer → silindir; her katman EKRANDA dökülür-serilir-ezilir; İLK yük S2'nin içinde düşer (G2'de damper kasası inik bekler) | ıslak koyu şerit · silindir izi · basamak kenarı | G2 (kaya taban, makineler hazır) | G6 |
| taşkın dudağı + omuzlar | son katmanlar yalnız iki uca; orta 1 katman eksik | koyu taze beton (G6) | G5 (tepe ¾) | G6 |
| çağlayan | rezervuar (kadraj dışı) — vekil: portalın sönmesi (S6) | ince perde → tam çağlayan (S7 içinde) | G7 (kuru dudak) | G8 |

```
GİZLİ İŞ + GÖRÜNÜR VEKİL [P2-g]
  tünel deldirme (G0'dan önce)   → G0'da iki kuru kemer
  memba kapağının inmesi (S6)    → çıkış jetinin sönmesi
  göletin dolması (S6→S7, memba) → S7'de dudaktan aşan su
⛔ Sahada kaynağı olmayan parça "APPEARED" hükmü yer; yukarıdaki altı satır kaynak beyanıdır.
⚠️ S1 iki elemanı aynı klipte taşır (seki + taban) — düz ızgaranın katlama bedeli, plan §AŞAMA
   MERDİVENİ (c). ⑧ ikisini de ayrı ayrı sorar: seki uzarken KESİLİYOR mu, taban KAZILIYOR mu.
```

---

## 6. ⑥ GEÇİŞ — kesme listesi ve ses

```
PLAN KESMELERİ (sn)  8,0 · 16,0 · 24,0 · 32,0 · 40,0 · 48,0 · 56,0   (7 kesme, hepsi ölçü başı — DÜZ)
KESME KANITI         bash araclar/kesme_kontrol.sh teslim.mp4 dikey_shorts/OVER_THE_WALL/OVER_THE_WALL_DIKEY_TIMELAPSE.md
                     tolerans kesme başına ±0,25 sn · çıkış 1 = SÜRE sütunundan yeniden kes
                     betik "PLANIN KENDİSİ DÜZ" uyarısını basar — beklenen, kabul edilmiş (künye)
DİKİŞ                zincirli format: dikişin iki yakası AYNI KARE (G1…G7); kesmede ışık, gölge, yapı ATLAMAZ
MÜZİK                120 BPM · müziksiz pencere 0,0–2,0 (nehir sesi) · 48,0–56,0 neredeyse sessiz · 56,0 sub swell
                     ⭐ düz ızgarada yay katmanlarla taşınır: her 8 sn'lik blok bir öncekinden farklı sesler
SES HEDEFİ           −14 LUFS ±0,5 · tepe ≤ −1,0 dBTP
```

---

## 7. ÜRETİM ÖNCESİ AÇIK KAPILAR — bu SPEC'in hükmü bunlar koşulmadan yoktur

```
⛔ ARAÇ KAPISI    sekiz ölçüm (ARAC_KARTLARI §4) · sonuç OVER_THE_WALL_URETIM_GUNLUGU.md §0'a
                  ⑧ iki kare (ilk+son) alınmıyorsa BU FORMAT O ARAÇTA ÜRETİLMEZ; araç değişir
⛔ KUTU SETİ      her sahne 8,0 sn → en büyük kutu ≥ 9,0; değilse iki-klip hükmü SEKİZ sahneye (plan)
⛔ USTA KARE      G8 önce; kapı: çağlayan · siyah kemer · gömülü köprü bu sırayla okunuyor mu
⛔ ZİNCİR         her karede zincir_kontrol.sh + kemer ELLE
⛔ GÜNLÜK         klip başına satır; günlüksüz filme qa_paket.sh açılmaz [DERS 28]
⛔ YEDİ ÖLÇÜM     KURGU_VE_TESLIM §6 → günlük §4
⛔ KAPAK KANITI   ffmpeg -ss 62.5 -i teslim.mp4 -frames:v 1 g8_kaynak.jpg
                  bash araclar/zincir_kontrol.sh g8_kaynak.jpg kapak.png  → çıkış 2 = TESLİM YOK
```
