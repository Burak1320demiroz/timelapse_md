# 🔍 OVER THE WALL — QA RAPORU

```
FİLM          OVER THE WALL — Boğazda RCC Baraj · Nehir Duvarı Aşar
TARİH         14.09.2026
DURUM         ⛔ ÜRETİLDİ VE ON İKİ MERCEKLE ÖLÇÜLDÜ — ama ÜRETİM GÜNLÜĞÜ TUTULMADI (DURUM ⛔ BOŞ)
              ⛔ 12 merceğin 11'i RUN INCOMPLETE (belgesiz ve/veya karesiz); yalnız ① kare aldı (69 kare)
              ⛔ Kurgu hiçbir plan sürümüne oturmuyor: 7 klip · 7,8·8,0·10,7·10,0·8,0·13,0·6,0 = 63,5 sn
                 + kart 4,5 sn = 68,0 sn. Plan (14.09.2026): 8 × 8,0 = 64,0 + 5,0 = 69,0.
                 Eski plan (12.09.2026): 10 × (3,0…9,0) = 60,0 + 5,0. Hangisinden üretildiği BİLİNMİYOR [DERS 28].
HAM           QA/HAM_RAPORLAR/OVER_THE_WALL/ — 12 dosya, dokunulmaz
```

---

## 1. 📊 MERCEK BAZLI ÖZET VE SKORLAR

| Mercek | Mod | Skor | VERDICT | Durum |
|---|:---:|:---:|---|---|
| **① KARE** | V (69 kare) | **5,8**/10 Ⓥ | ⛔ SIX SEPARATE SHOTS | CAMERA LOCK 9 · ANCHOR IDENTITY 2 · SURFACE TRUTH 1 · **ikinci istasyon** (klip 5, ufuk %92 vs %73) plan dışı |
| **② İNŞA** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 3,8) | ⛔ DIFFERENT · APPEARING (8. kez) | 00:19,0 "basamaklı beton havuz" → 00:27,0 bambaşka ayak izli kemer duvar |
| **③ ZAMAN** | V | **6,0**/10 Ⓥ | ⛔ PASSES BUT NOT IN ONE DIRECTION | SEASON ORDER 2 · kar 4 kez gidip geldi · okunan süre "1,5–2 yıl" (plan 1 yıl) TUTMADI · SEASON CARRIER 10 |
| **④ TESLİM** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 5,3) | ⚠️ ENDS · COST/FINAL BEAT PASS (7/10) | ONE THING BULUNDU ("kanyon → iki katlı çağlayan") · LOOP 3 · kapak verilmedi · müziksiz pencere yok (8) |
| **⑤ DEVAMLILIK** | ⛔ V karesiz | *karesiz — TEKRARLANACAK* (ham 3,0) | ⛔ A SET REBUILT EACH TIME | 6/6 dikiş DEFECT · kanıt nesnesi BULUNDU: taş köprü · üç istasyon grubu saydı |
| **⑥ GEÇİŞ** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 7,0) | ✅ TIME · ⭐ **RHYTHM** | CUT MECHANICS 10 · MUSIC 9 · DIRECTION 3 (mevsim geri) · JUMP SIZING 6 (00:36,5) — ⑤ REBUILT iken RHYTHM: ilk kez |
| **⑦ İŞ** | ⛔ V karesiz | *karesiz — TEKRARLANACAK* (ham 3,8) | ⛔ PARKED | CAUSE AND EFFECT **0** · WORKING FRONT 3: "Clip 4: lower bridge roadway — NONE on main dam wall" · THE GROWTH NOBODY MADE: 0:26,5 duvar |
| **⑧ YÖNTEM** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham **0,0**) | ⛔ APPEARED · 0/4 MADE | dört elemanın dördü "INCOMPLETE NEVER · COMPLETE 00:26,6" · THE FIRST PIECE: Concrete Dam Wall |
| **⑨ FAALİYET** | ⛔ V karesiz | ham 7,5 Ⓥ | ✅ PRODUCTIVE WORK | ama en amaçsız hareket: yükleyiciler "su basmış temel plakasında" ileri geri (00:22,5) · köprüde ping-pong (00:18,0) |
| **⑩ SEBEP** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 1,3) | ⛔ MAGICAL APPEARANCE | 4 elemanın 3'ü MAGIC · PROXIMITY WITHOUT WORK 2 · SCALE OF LABOUR 1 — "trucks on the bridge as visual proximity cover" |
| **⑪ ENVANTER** | ⛔ V | *belgesiz — TEKRARLANACAK* (ham 9,3) | ⛔ INTRUDERS | iki davetsiz: dikdörtgen su havuzu (00:19,0) · çelik derrick kule (00:37,5 → 00:40,0'da yok) · gelmeyen davetli: YOK |
| **⑫ KATILIK** | ⛔ V karesiz | ham 6,8 Ⓥ | ⛔ MELTING | eriyen her gövde bir ARAÇ, hepsi köprü/platform gibi dar yüzeyde çift: pass-through ×4 · fade-in · dönmeyen teker; duvar · köprü · su HOLDS |

```
⛔ MOD DENETİMİ [DERS 17]: ② ④ ⑥ ⑧ ⑩ ⑪ belgesiz koştu — skorları tabloya YAZILMADI, satırlar
   "belgesiz koşuldu — TEKRARLANACAK" diye açıldı. ⑤ ⑦ ⑨ ⑫ karesiz koştu (kare_al.sh yalnız ① için).
   qa_paket.sh koşulmadı; koşulamazdı da — üretim günlüğü boş [DERS 28 · 29].
⭐ END CARD: on iki merceğin on ikisi de "SAME" dedi — DERS 30 (kapak kanıtı) İLK KEZ bütün
   merceklerde tuttu. Kart filmin son karesinden türemiş.
```

## 2. ⛔ HÜKÜM OKUMA SIRASI — film "zincir koşulmadı" diye kapanır [kart R 6a]

```
⑤ A SET REBUILT EACH TIME  +  ⑧ APPEARED (0/4)  →  diğer merceklerin SKORU yorumlanmaz.
Bu format (İKİ KEYFRAME ZİNCİRİ, §2.7) doğru koşulsaydı 6 dikişin 6'sında iki yaka AYNI KARE
olurdu; ⑤ 6/6 DEFECT saydı (ekskavatör yok olur, kulübeler yok olur, nehir bir karede kurur,
havuz bir karede duvara döner). Üç olasılık var ve günlük olmadığı için AYIRT EDİLEMEZ [DERS 28]:
   (a) zincir hiç koşulmadı (her klip tek kareli I2V ya da T2V)
   (b) zincir koşuldu, araç SON KAREYİ tutmadı (araç kapısı ⑧ sorusu — ölçülmedi)
   (c) klipler başka bir plandan / plansız üretildi (kurgu 7 klip; iki plan sürümü de 8 ve 10)
⭐ Bunun bedeli: aşağıdaki dört yeni dersin hiçbiri "prompt böyle yazılmıştı, tutmadı" diye
   yazılamıyor — yalnız "ekranda bu oldu, plandaki cümle şuydu" diye yazılıyor.
```

## 3. 🚨 EN AĞIR ÜÇ BULGU

1. **[⑦ ⑧ ⑩ ② — 00:26,5 · duvar bir kesmede doğdu]** Baraj gövdesi ilk kez %100 hâliyle görüldü (⑧ "INCOMPLETE NEVER"); onu yapan tek makine ekranda yok (⑦ CAUSE AND EFFECT 0/10, ⑩ MAGIC). Plandaki S3 BÜYÜR (8 → 45 m, 8,0 sn) klibi filmde YOK — büyüme kesmenin içine düştü. Bu, deponun ② APPEARING hükmünün **sekizinci** gelişi; POLAR HABITAT ve THE CROSSING'in BUILT'inden sonra geri düşüş.
2. **[⑦ ⑩ ⑨ ⑤ ① — makineler köprüde, duvarda değil]** Beş mercek birbirinden bağımsız aynı şeyi yazdı: damper, yükleyici ve tanker eski taş köprünün ÜSTÜNDE dolaşıyor (⑨ 00:18,0 ping-pong · ⑤ 00:44,6 köprüde park · ① 0:06,0 iki yükleyici köprüde), baraj gövdesinde çalışma cephesi yok (⑦ "NONE on main dam wall"). Planın ACTIVITY bloğu makineyi sekiz sahnenin altısında **"the deck"** üstüne yazıyor; kadrajda ikinci bir deck var — köprü tabliyesi → **DERS 51**.
3. **[③ ⑥ ⑤ ⑪ — 00:36,5 · istasyon değişti VE duvar sıçradı]** Plan tek istasyon beyan etti ("eight locked-off shots from one camera"); filmde 00:36,5–00:44,5 yüksek açılı ikinci bir istasyon var (① ufuk %92). Aynı kesmede duvar yarımdan tam krete sıçradı (③ 7, ⑥ 3), portal geometrisi kaydı (⑤ C2) ve klipte plana yazılmamış bir çelik derrick kule belirip kayboldu (⑪ en zararlı davetsiz) → **DERS 52**.

## 4. 🎞️ KURGU ↔ PLAN EŞLEMESİ — günlük yok, eşleme TAHMİNİDİR

| Film klibi | Süre | Ekranda | Plandaki en yakın sahne | Not |
|:-:|---:|---|---|---|
| 1 | 0:00,0–0:07,8 | tünel deşarjı, yatakta damperler, kar iner | S0 DÖNER (Ekim→Kasım, kar yalnız çentikte) | kar TABANA indi — plan dışı |
| 2 | 0:07,8–0:15,8 | yeşil nehir, kıyı kazısı, ekskavatör | S1 AÇAR (Kasım→Şubat, kar birikir) | KIŞ ① yok; yaz okundu |
| 3 | 0:15,8–0:26,5 | kar, "beton havuz" 0:19,0 | S2 DOĞAR (Şubat→Nisan, 8 m platform) | platform HAVUZ okundu → DERS 54 |
| — | — | — | **S3 BÜYÜR (8 → 45 m)** | **filmde YOK — kesmenin içinde** |
| 4 | 0:26,5–0:36,5 | tam kemer duvar, fırtına 0:29, sel | S4 KABARIR (45→52 m, fırtına) | duvar zaten tam; fırtına altında SERT gölge (③ tablo) |
| 5 | 0:36,5–0:44,5 | ⛔ ikinci istasyon, kret, derrick | S5 KAPANIR (52→72 m kret) | plan dışı istasyon → DERS 52 |
| 6 | 0:44,5–0:57,5 | kuru portal, tanker + damper köprüde | S6 SÖNER (Eylül→Ekim, tanker sekide) | kar lekeleri geri geldi — plan dışı |
| 7 | 0:57,5–1:03,5 | dudaktan aşan su, köprü köpükte | S7 AŞAR (usta kare G8) | ✅ omurganın sonu ekranda; köprü "ikinci dolusavak"a dönüştü (① 3) |

## 5. ⏱️ ZAMAN TAHMİNİ [kart R 6]

```
③ "TIME READ FROM THE FILM ALONE: about 1.5 to 2 years" — taşıyıcı: "multiple winter snow cycles".
PLAN: 1 yıl (Ekim → Ekim · TEMSİL 1 g + 13 + 8 + 16 + 4 + 5 + 3 hf + 1 g ≈ 50 hafta) · ③ hedefi
"yaklaşık bir yıl" [P1-c]. TUTMADI — sebebi kar: plan tek kışı iki karede (G2 birikme · G3 erime)
taşır; film karı 1 · 3 · 4 · 6. kliplerde getirip 2 · 5 · 7'de kaldırdı, mercek İKİ kış saydı.
Mevsim TAŞIYICISI 10/10: film mevsimi anlatabiliyor, yalnız sırasını tutamıyor [DERS 26 · 3. kez].
```

## 6. ❓ DOKÜMAN SORULARININ CEVAPLARI

### ① KARE
1. **İstasyon koordinatları, lens, ufuk (Grup A ve B)?** — Plan TEK istasyon: doğu duvarındaki kaya sekisine cıvatalı tripod, mercek tabandan 15,0 m, baraj eksenine 120 m, bakış 350°, tilt 0°, roll 0°, 24 mm · f/8 · ISO 100; ufuk tam %50'de (tünel çıkış kemerinin tacı). **Grup B (klip 5, ufuk %92) planda YOK.** Filmin ölçtüğü %73 ufuk da plandaki %50 kilidine oturmuyor.
2. **Havuz (0:19,0) ve duvar (0:27,0) kademeli mi planlandı?** — Evet: S2 ilk yük klibin İÇİNDE dökülür → 8 m platform (G3 %46) · S3 8 → 45 m (G4 %67) · S4 45 → 52 (G5 %71) · S5 52 → 72 kret (G6 %82). Filmde S3 klibi yok; 8 → 72 m'nin tamamı iki kesmenin içine düştü.
3. **Araçlar bulanık aktif eleman mı, keskin dekor mu?** — İkisi de, BEYANLI: rejim B'de "every moving machine is smeared into a blur" + her ACTIVITY'de "a parked truck stays sharp" (tek park hâlinde araç keskin). Köprüde 9 sn keskin duran tanker + damper (① 7, 0:48,0) planın S6'sındaki "tanker sekide durur"un köprüye taşınmış hâli — yüzey yanlış [DERS 51].
4. **Köprünün ikinci dolusavak kretine dönüşmesi (1:02,0) planlı mı?** — Hayır. Köprü sabit çapadır (NEGATIVE: "never change shape"); S7'de su köprüyü YUTAR ("churns white around the drowned bridge"), köprüyü DEĞİŞTİRMEZ. Plan dışı.

### ③ ZAMAN
1. **Toplam takvim ve program?** — 1 yıl, Ekim → Ekim; temsil süreleri yukarıda (§5). Güneş yayı tek gün 08:00 → 16:20 (azimut 113° → 247°), mevsim YERDEN okunur.
2. **Klip başına mevsim ve güneş açısı?** — G0 Ekim 113°/15° · G1 Kasım 127°/25° · G2 Şubat 144°/34° (KIŞ ① kar tabana kadar) · G3 Nisan 162°/40° (KIŞ ② slush) · G4 Temmuz 183°/42° (fırtına, gölgesiz) · G5 Ağustos 203°/39° · G6 Eylül sonu 220°/31° · G7 Ekim 235°/21° · G8 Ekim 247°/10°. TEK kış, S1–S3 arasında.
3. **Klip 6 bitiş sonrası ikinci kış mı?** — Hayır. S6 SÖNER Eylül → Ekim, KURU, karsız; klip 6'daki kar lekeleri plan dışı.

### ⑤ DEVAMLILIK
1. **0:19,0'daki havuz geçici batardo mu?** — Planda havuz yok. En yakın nesne G3'teki 8 m ilk kaldırma platformu — barajın KENDİ alt katmanları, kalıcı, hiç sökülmez (NEGATIVE: "only ever gains material"). Batardo = G0'daki kaya dolgu kapatma seddi; memba tarafında kalır, S3'te duvarın arkasında gizlenir.
2. **Köprüye çıkan taşıma yolu?** — YOK. Köprü hiçbir planda trafik taşımaz; taşıma yolu doğu duvarına kesilen yol sekisidir (S1'de ilk yara → seki → kret kotu %81,7).
3. **Kulübeler?** — Planda şantiye kulübesi yok (⑪ de yazmadı ama davetsizdir).

### ⑦ İŞ
1. **Duvarın betonu kliplerin arasında (kamera dışı) mı planlandı?** — Hayır. S3 BÜYÜR 8,0 sn'lik EKRANDA büyüme klibidir: damper "tips a fresh load … onto the deck", dozer "spreads", silindir "packs" — her katman ekranda. S4–S5 aynı fiillerle 72 m'ye çıkar.
2. **Havuzun sökümü planda var mı?** — Havuz yok; ilk kaldırma barajın kendisidir ve yalnız malzeme kazanır.
3. **Mikser/pompa/vinç kasten dışarıda mı?** — Evet, yöntem RCC: platodaki santralden (kadraj DIŞI) damperle gelen karışım dök → ser → ez. Vinç, pompa, mikser, kalıp planda hiç yok; "eksilen istif yerine gelen kamyon" [plan §Malzeme kaynağı · DERS 48]. ⑦'nin "no concrete supply line" bulgusu bu yüzden geçerlidir: gelen kamyon akışı da ekranda yoktu.

### ⑨ FAALİYET
1. **Köprü ana taşıma yolu mu?** — Hayır (⑤ 2 ile aynı cevap). 
2. **00:22,5'teki yükleyicilerin işi?** — Planda yükleyici yok; S2'nin makineleri damper (tips) · dozer (spreads) · silindir (packs), KURU kaldırma yüzeyinde.
3. **00:51,0'daki park araçları tünel işini mi destekliyor?** — Hayır. S6 SÖNER: tanker kret yolunu sular, park hâlinde damper ve silindir son makinelerdir (SÖKÜM satırı); tünel memba kapağıyla kapanır, vekili jetin sönmesidir. Bu sahne bilinçli olarak filmin en sakin sahnesidir (48–56 sn "near silence"); ⑦'nin %22,5 boşluğu planla uyumlu, yeri (köprü) değil.

### ⑫ KATILIK
1. **Kareler kasten mi verilmedi?** — Hayır; kare_al.sh / qa_paket.sh koşulmadı [DERS 29 · üçüncü film]. ① 69 kare aldı, ⑤ ⑦ ⑨ ⑫ almadı.
2. **Damperler ayrı rijit gövde mi?** — Plan her sahnede "the same yellow dump truck" + PHYSICS bloğunda teker/palet temas cümleleri yazar; ama dar yüzeyde İKİ hareketli araç yazar (S3: damper + ikinci damper + dozer + silindir aynı döşekte) → DERS 53.
3. **Tanker tam gövde mi?** — Planda tek, tam, beyaz tanker ("comes down the bench and stops beside the east shoulder"). Eksik gövde üretim kusuru; yeri de yanlış (sekide değil köprüde).

## 7. 🥁 IZGARA NOTU — proje sahibine ⚠️

```
Kurgu VARYANSLI kesildi: 7,8 · 8,0 · 10,7 · 10,0 · 8,0 · 13,0 · 6,0. ⑥ hükmü: TIME · RHYTHM · MUSIC 9/10.
Bu, ⑤ "A SET REBUILT EACH TIME" hükmü gelen bir filmde ⑥'nın İLK KEZ RHYTHM demesidir — DERS 44'ün
tam tersi ölçüm: orada varyanslı ızgara + kırık dünya → METRONOM; burada varyanslı kurgu + kırık dünya
→ RHYTHM. ⑥'nın gerekçesi kesmelerin ANLAM taşımasına dayanıyor (mevsim · sel · kret · taşkın).
THE CROSSING (7·7·19·7·8·16) ile birlikte ikinci kez: anlam taşıyan kesme + varyanslı süre = RHYTHM.
⚠️ Plan 14.09.2026'da 8 × 8,0 DÜZ ızgaraya kilitlendi ve ⑥ METRONOM riski kabul edildi. Bu ölçüm
   o kilide karşı kanıttır. Karar proje sahibinindir; plan DEĞİŞTİRİLMEDİ, yalnız not düşüldü.
```

## 8. 📚 DERSLER — yeni ve tekrar

```
YENİ  [kart D → DERSLER.md]
  DERS 51  ⭐ İki "deck" varsa makine HAZIR olana gider — iş yüzeyi eleman adı + yüzdeyle kilitlenir
  DERS 52  ⭐ Kesme iki şeyi birden değiştiremez — istasyon değişen kesmede yapı yüzdesi sabittir
  DERS 53  Dar yüzeyde iki hareketli araç birbirinin içinden geçer — ⑫ ilk koşu, A10-g "zayıf" ölçüldü
  DERS 54  Nehir yatağındaki ilk kaldırma SU HAVUZU okundu — ıslak beton + nehir = havuz korpusu
  DERS 44  tersi ölçüldü (§7) — hüküm notu DERS 44'ün altına düşüldü

TEKRAR (sayaç arttı, yeni ders yok)
  DERS 26  mevsim sırası geri gitti — 3. kez (MOUNTAIN DOOR · DUST YEAR · OVER THE WALL)
  DERS 28  günlüksüz üretim — 3. kez (LONG DAY · DUST YEAR · OVER THE WALL): arıza ADLANDIRILAMIYOR
  DERS 29  qa_paket.sh koşulmadı — 11/12 RUN INCOMPLETE
  DERS 17 · 27  ② ④ ⑥ ⑧ ⑩ ⑪ belgesiz; SPEC ve plan üretimden ÖNCE hazırdı
  DERS 35  metin: beyaz kamyon · sarı damper · tanker gövdesinde okunmaz yazı (① 6)
  DERS 49  opacity fade: damperler 00:18,0'de saydamlıktan belirdi (⑫ 6)
  DERS 50  keskin araç: köprüde 9 sn keskin tanker + damper (① 7)
  DERS 5 · 12  ters inşa / zincir koşulmadı — kanıt ⑤ 6/6 DEFECT
TUTAN
  DERS 30  kapak kanıtı: 12/12 END CARD SAME ✅ (ilk kez bütün merceklerde)
  DERS 11  kamera kilidi: CAMERA LOCK 9/10, FRAME IDENTITY 9/10 ✅ (ikinci istasyon hariç)
  ③ SEASON CARRIER 10/10 · C4 VEGETATION 8/10 ✅ — taşıyıcılar yerde okunuyor
```

## 9. 🎯 KARAR VE EYLEM PLANI

```
1. YAYINLANMAZ. ⑤ REBUILT + ⑧ APPEARED + ② APPEARING: zincir hükümleri düştü.
2. YENİDEN ÜRETİLMEZ — önce ARAÇ KAPISI (ARAC_KARTLARI §4, sekiz ölçüm, ⑧ iki kare sorusu dâhil)
   ve ÜRETİM GÜNLÜĞÜ. Günlüksüz bir sonraki üretim de aynı satıra düşer [DERS 28].
3. Yeniden üretilecek sahneler (⑦ "GROWTH NOBODY MADE" 0:26,5 · ⑧ "FIRST PIECE" Concrete Dam Wall):
   S2 DOĞAR (kuru katlı platform, DERS 54) · S3 BÜYÜR (8 → 45 m, filmde hiç yok) · S4–S5 (döşekte
   makine, köprü boş — DERS 51) · tek istasyon (DERS 52) · dar yüzeyde tek araç (DERS 53).
4. Belgeli TEKRAR: ② ⑧ ⑩ ← QA_SPEC · ④ ⑥ ⑪ ← plan (+ kapak, + ses) · ⑤ ⑦ ⑨ ⑫ ← kare_al.sh çıktısı.
   Hepsi qa_paket.sh ile [DERS 29] — günlük açılmadan koşmaz.
5. Izgara kararı (§7) proje sahibine: 8 × 8,0 düz kilit mi, ⑥'nın iki kez RHYTHM dediği varyanslı
   kurgu mu. Plan bu raporla DEĞİŞTİRİLMEDİ.
6. Kabul edilen kusur: YOK — hiçbir bulgu "kabul edildi" diye kapatılmadı; film bir sonraki
   üretimde sıfırdan zincirle üretilir.
```
