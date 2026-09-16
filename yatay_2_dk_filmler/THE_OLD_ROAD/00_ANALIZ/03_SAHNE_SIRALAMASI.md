# 🎞️ THE_OLD_ROAD — SAHNE SIRALAMASI (aşama merdiveninin türetildiği yer)

> **Bu dosya sıranın TÜRETİLDİĞİ ve DENETLENDİĞİ yerdir.** Sonuç `THE_OLD_ROAD_PLAN.md` §AŞAMA MERDİVENİ
> ve §KARE TABLOSU'na taşınır — orası sonucu taşır, burası hesabı.
> ⛔ Burada `## 🎬 SAHNE <n>` başlığı yoktur; sahneler TABLO satırıdır.
> Girdi: `02_KONSEPT_VE_RISK.md` (yapı kartı · kamera · ışık günü · risk) + onaylı sahne satırları.

---

## 1. 🧱 İNŞA SIRASI → 15 SATIR [YAPI_TIPI_KARTLARI · INSAAT_YONTEMI §2-§3]

```
KARTIN SIRASI      İTMELİ (incremental launching) VİYADÜK — gerçek sıra:
                   ① güzergâh kesisi + yaklaşımlar ② kazık/temel ③ ayaklar (tırmanır kalıp) + başlıklar
                   ④ döküm alanı + itme yatağı + çelik burun ⑤ kesit dök → priz → İT (döngü)
                   ⑥ geçici destek (uzun açıklıkta) ⑦ burun teması → beton gövdenin son konumu
                   ⑧ burun ve geçici desteğin sökümü + kalıcı mesnetlere indirme
                   ⑨ kaplama · korkuluk · yaklaşım bağlantıları · aydınlatma ⑩ trafiğin geçmesi
15 SATIRA AÇMA     ① → S0–S1 · ② → S1 · ③ → S2 · ④ → S3 · ⑤ → S4 · S5 · S6 · S7 · S10 · S11
                   ⑥ → S6 · (sel S8, onarım S9 — itme yalnız BU İKİ sahnede durur) · ⑦ → S10 (burun teması) + S11
                   (beton hat) · ⑧ → S12 · ⑨ → S13 · ⑩ → S14
MONOTON BÜYÜME     ✓ hiçbir satır öncekinden az yapı göstermez; tabliye yalnız UZAR, hiç kısalmaz.
                   Ara hâl silueti değiştirir [DERS 37]: her itmede gövdenin ucu bir sonraki ayağa geçer.
KIŞ                kar VADİYE yağmaz: kar çizgisi S6'da yamaçta iner (G7'de en düşük), S7'de erir ve seli
                   doğurur — iki kare, iki sahne [DERS 7 · 21]; çıplak melezler ikinci taşıyıcı.
DORUK              S11 — boşluğun kapanması. Düz ızgarada süreyle değil, KATMANLA (müzik) ve klip içi
                   hareketin iki adımlı kurgusuyla vurgulanır (burun teması → beton gövdenin ilerlemesi).
SÖKÜM              S12 (burun + geçici destek) · S13 (döküm hangarı + şantiye yolu) — ekranda FİİLLE gider.
TERS AÇILIŞ YOK    S0 ileri yönlü kanca [DERS 3]: bitmiş köprü gösterilmez; kanca eski yolun trafiğidir.
```

## 2. 🗺️ SIRALAMA — 15 sahne, sırayla

| S | SÜRE (sn) | AŞAMA FİİLİ | ELEMAN + ARA HÂL (%) | TEMSİL SÜRE | REJİM | SAAT | AZ/EL | İSTASYON | KANIT NESNESİ (px) | onaylı satırla aynı mı |
|:-:|:-:|---|---|---|:-:|:-:|:-:|:-:|---|:-:|
| S00 | 8,0 | **AÇAR** | YENİ GÜZERGÂH 0 → ilk kesi (%2) | 1 gün | A | 05:05→05:15 | 75° / −5° | ANA | sol yamaçta taze toprak kesisi (≈40 px bant) | ✅ |
| S01 | 8,0 | **KAZAR** | YAKLAŞIM + TEMELLER 0 → %100 · geçici geçiş kurulur | 8 hf | B | 05:15→07:15 | 98° / 18° | ANA | iki yakada kenar ayağı basamakları (%45 kotunda iki çentik) | ✅ |
| S02 | 8,0 | **YÜKSELİR** | AYAKLAR %0 → %100 + başlıklar | 16 hf | A | 07:15→07:25 | 99° / 20° | ANA | P3 ayağı 202 px — tepesi tabliye kotunda (%43,8) | ✅ |
| S03 | 8,0 | **KURAR** | DÖKÜM ALANI 0 → %100 · ilk kesit + çelik burun | 8 hf | B | 07:25→09:25 | 127° / 39° | ANA | çelik burun ucu A1'in 20 m ötesinde (%17) | ✅ |
| S04 | 8,0 | **İTER** | TABLİYE %0 → %14 (A1 → P1) | 3 hf | A | 09:25→09:35 | 129° / 41° | ANA | tabliye ucu P1'de (%23,7) · burun %31,5 | ✅ |
| S05 | 8,0 | **EKLER** | TABLİYE %14 → %32 (P1 → P2) | 4 hf | A | 09:35→09:45 | 131° / 42° | ANA | tabliye ucu P2'de (%36,8) · burun %44,7 | ✅ |
| S06 | 8,0 | **UZANIR** | TABLİYE %32 → %50 (P2 → P3) · geçici destek kurulur | 19 hf | B | 09:45→11:45 | 172° / 52° | ANA | tabliye ucu P3'te (%50) · geçici destek %56,6 | ✅ |
| S07 | 8,0 | **ZORLAR** | TABLİYE %50 → %63 (P3 → P4) · su yükselirken itme sürer | 3 hf | B | 11:45→13:45 | 219° / 46° | ANA | tabliye ucu P4'te (%63,2) · burun %71,1 · su çizgisi ayak dibinde | ✅ |
| S08 | 8,0 | **TAŞAR** | HAT KOPAR — geçici geçiş ve berm gider | 2 gün | A | 13:45→13:55 | 222° / 45° | ANA | geçici geçiş YOK (%46,9 boş) · sürüntü matı geçici destekte · berm aşılmış | ✅ |
| S09 | 8,0 | **ONARIR** | HAT YENİDEN KURULUR · döküm alanı iki kesit biriktirir | 4 hf | B | 13:55→15:55 | 252° / 27° | ANA | yeni menfez + yeni çapraz + temizlenmiş pabuç · hangarda 2 hazır kesit | ✅ |
| S10 | 8,0 | **SÜRER** | TABLİYE %63 → %76 (P4 → P5) · burun KARŞI KENARA DEĞER | 6 hf | A | 15:55→16:05 | 254° / 25° | ANA | tabliye ucu P5'te (%76,3) · ⭐ burun ucu A2'de (%86,9) | ✅ |
| S11 | 8,0 | **KAVUŞUR** | TABLİYE %76 → %100 — beton hat tamam | 4 hf | A | 16:05→16:15 | 256° / 23° | ANA | kesintisiz beton çizgi A1 → A2 (%13,1 → %86,9) | ✅ |
| S12 | 8,0 | **SÖKER** | BURUN + DESTEK + HANGAR → 0 · kalıcı mesnetler | 6 hf | B | 16:15→18:15 | 278° / 2° | ANA | burun yok · destek yok · hangar yok · tabliye mesnetlerde | ✅ |
| S13 | 8,0 | **DÖŞER** | ÜST YAPI %0 → %100 · şantiye toplanır | 8 hf | A | 18:15→18:25 | 279° / 1° | ANA | su yalıtımı + asfalt + korkuluk + lamba (%48,8) · yol izi | ✅ |
| S14 | 8,0 | **AKAR** | TRAFİK ESKİ YOL → YENİ YOL | 1 gün | A | 18:25→18:35 | 281° / −1° | ANA | viyadükte far izi çizgisi (%45) ↔ virajlarda son araç | ✅ |

## 3. 📐 DİKİŞ DENETİMİ — mekanik, göz kararı değil [§2.7 · DERS 52]

> Zincirli formatta dikiş bir KAREDİR: G(n+1) hem S(n)'in son karesi hem S(n+1)'in ilk karesi.
> Her dikişte yapı yüzdesi, gölge açısı, gök, çapalar AYNIDIR; değişen yalnız klibin içindedir.

| dikiş | kare | yapı yüzdesi | gölge açısı | gök | istasyon aynı mı | not |
|---|:-:|:-:|:-:|:-:|:-:|---|
| S0→S1 | G1 | temeller | 98° | sabah kümülüs | ✓ |  |
| S1→S2 | G2 | ayaklar tam | 99° | açık | ✓ |  |
| S2→S3 | G3 | burun %17 | 127° | açık | ✓ |  |
| S3→S4 | G4 | tabliye P1 | 129° | açık | ✓ |  |
| S4→S5 | G5 | tabliye P2 | 131° | yüksek sirrus | ✓ |  |
| S5→S6 | G6 | tabliye P3 | 172° | kapalı gri tavan | ✓ |  |
| S6→S7 | G7 | tabliye P3 (sabit) | 219° | alçak yağmur bulutu | ✓ |  |
| S7→S8 | G8 ⭐ bölüm sınırı | tabliye P4 | 222° | yırtılan bulut | ✓ | iki dosya, tek kare |
| S8→S9 | G9 | tabliye P4 (sabit) | 252° | açılan gök | ✓ | tabliye İKİ YAKADA da aynı ayakta |
| S9→S10 | G10 | tabliye %68,4 | 254° | açık | ✓ | tabliye İKİ YAKADA da aynı ayakta |
| S10→S11 | G11 | tabliye A2 | 256° | açık, sıcak | ✓ |  |
| S11→S12 | G12 | burun/destek yok | 278° | altın batı | ✓ |  |
| S12→S13 | G13 | üst yapı tam | 279° | alacakaranlık | ✓ |  |
| S13→S14 | G14 | — | 281° | — | ✓ |  |

## 4. ☀️ IŞIK GÜNÜ TOPLAMI — rejim sütunu TOPLANIR

```
A × 9 = 90 dk = 1,5 h · B × 6 = 12,0 h · C × 0 = 0   →  Σ = 13,5 saat   (≤ 14 ✓ · gece YOK)
SAAT SÜTUNU   S0 05:05 → S14 18:35 — monoton artar ✓ · her G'nin azimut/yükseklik değeri KARE TABLOSU'nda
REJİM DAĞILIMI  B: S1 · S3 · S6 · S7 · S9 · S12   ·   A: S0 · S2 · S4 · S5 · S8 · S10 · S11 · S13 · S14
REJİM C       kullanılmıyor — gölgesiz klip yok [DERS 40 tetiklenmez]
⚠️ A dizisi: S4–S5 (2) · S10–S11 (2) · S13–S14 (2, alacakaranlık) — üçten uzun dizi yok; gölge donukluğuna
   karşı her A karesinde mevsim taşıyıcısı ve eski yol trafiği zorunlu [DERS 47]
```

## 5. ⭐ ÜÇ ZORUNLU SATIR — PLAN'a taşınacak

```
① KANIT NESNESİ   her satırda tabloda (yukarıda). ⭐ "AYNI YER" NESNESİ = ESKİ TAŞ KEMER KÖPRÜ (vadi tabanı,
                  %34,2 · x %44,4 · 64 × 21 px) + ESKİ YOLUN VİRAJ GEOMETRİSİ. zincir_kontrol.sh'in her
                  koşusunda iki karede de aynı yerde, aynı boyda mı — ELLE ✓/✗ [DERS 25].
                  ⭐ İKİNCİ KANIT (yalnız itme sahnelerinde): İLK DÖKÜLEN KESİT — koyu döküm derzi ve kalıp
                  izleriyle tanınır, 16 karede aynı kesittir ve hep en öndedir; her itmede sağa kayar.
② LOOP SATIRI     ⚠️ LOOP DEĞİL, AÇILIŞ–KAPANIŞ KAFİYESİ: G0'da virajlarda far izleri zikzak, G15'te
                  viyadükte tek düz çizgi. Kadraj ve çapalar aynı; ışık ve trafik yön değiştirir.
③ SÖKÜM SATIRI    geçici menfez geçişi (S1 kurulur → S8 SEL GÖTÜRÜR → S9 yeniden serilir → S13 kaldırılır) ·
                  tırmanır kalıplar (S2 sonunda iner) · çelik burun (S3 kurulur → S12 sökülür) · geçici
                  çelik destek (S6 kurulur → S12 sökülür) · döküm hangarı + itme yatağı (S3 → S13) ·
                  şantiye yolu (S1 → S13, İZİ KALIR). Hiçbiri kaybolmaz; hepsi bir FİİLLE gider [P2-h].
```

## 6. 🔁 ONAYLI HİKÂYEYLE FARK

```
Onaylı hikâye metni (00_HIKAYE_ONAYI §SAHNELER) ile bu sıralama BİREBİR aynıdır (15/15 satır ✅).
Fark yok; olursa buraya tarih ve gerekçeyle yazılır ve hikâye onayına da işlenir.
```
