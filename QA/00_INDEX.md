# 📊 00_INDEX — PROJEDEKİ TEK SAYAÇ

> ⛔ Sayılar buraya ELLE yazılır ama `bash araclar/sayac.sh` ile
> KARŞILAŞTIRILIR. Betik uyuşmazlığı ekrana basar. Bir sayıyı iki yerde
> tutmak, birini yanlış tutmaktır.

---

## SAYIM

```
TOPLAM FİLM       7
ÖLÇÜLEN FİLM      6
TAM ÖLÇÜLEN       0     (8 merceğin 8'i de koşulmuş — ⑦ ⑧ 07.09.2026'da açıldı)
SEKİZ MERCEKLE    2     (THE LONG DAY · THE DUST YEAR — ikisi de RUN INCOMPLETE)
ALTI MERCEKLE TAM 3     (⑦ ⑧ öncesi tamlık)
ÜRETİLEN FİLM     6
YAZILDI, ÜRETİLMEDİ 1   (BEFORE NIGHTFALL — plan + SPEC hazır, araç kapısı koşulmadı)
```

## TAMLIK MATRİSİ

Bir film "tam ölçüldü" sayılmak için sekiz merceğin sekizini de görmelidir.
⑦ ve ⑧ 07.09.2026'da açıldı; önceki dört filmin hiçbiri bu ikisiyle ölçülmedi.

| Film | ① KARE | ② İNŞA | ③ ZAMAN | ④ TESLİM | ⑤ DEVAM | ⑥ GEÇİŞ | ⑦ İŞ | ⑧ YÖNTEM | Tam |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **THE LONG DAY** | Ⓥ 6,4 karesiz | ⛔ belgesiz | **7,0** | ⛔ belgesiz | Ⓥ 5,8 karesiz | ⛔ belgesiz | Ⓥ 4,4 karesiz | ⛔ belgesiz | **8/8** · 8'i de RUN INCOMPLETE |
| **THE MOUNTAIN DOOR** | Ⓥ 1,1 | ⛔ belgesiz | **3,6** | ⛔ belgesiz | Ⓥ 0,2 | ⛔ belgesiz | ❌ | ❌ | **6/8** |
| **THE NARROW LOT** | Ⓥ 6,0 | ⛔ belgesiz | **4,2** | ⛔ belgesiz | Ⓥ 5,6 | ⛔ belgesiz | ❌ | ❌ | **6/8** |
| THE LONG SHADOW v1 | Ⓥ 3,3 | Ⓥ 0,4 | Ⓥ 4,3 | Ⓥ 2,7 | ❌ | ❌ | ❌ | ❌ | **4/8** |
| THE CLOSING SPAN | 1,0 | Ⓥ 0,0 | 1,3 | Ⓥ 5,4 | Ⓥ 0,0 | Ⓥ 1,6 | ❌ | ❌ | **6/8** |
| **THE DUST YEAR** | Ⓥ 1,3 karesiz | ⛔ belgesiz 0,9 | 4,0 | ⛔ belgesiz 2,1 | Ⓥ 4,0 karesiz | ⛔ belgesiz 6,6 | Ⓥ 1,3 karesiz | ⛔ belgesiz **0,0** | **8/8** · 7'si RUN INCOMPLETE |
| BEFORE NIGHTFALL | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ |

```
⚠️ THE LONG SHADOW v1'in ⑤ ve ⑥'sı KOŞULMADI çünkü o iki mercek film
   ölçüldükten SONRA açıldı. v1 arşivdir ve yeniden ölçülmeyecek — ama
   raporlarında ikisinin de malzemesi zaten var:
     ⑤'in konusu: "crane switches from grey flat-top to blue saddle jib"
                   (② kat.7) · "materials and vehicles morph" (① kat.8)
     ⑥'nın konusu: "cut 1 to cut 2 reverses time entirely" (③ kat.7)
   İki mercek de v1'de ayrı ayrı sorulsaydı bu bulgular DAHA ERKEN ve
   DAHA NET çıkardı. Açılma sebepleri budur.

⚠️ ⑦ İŞ ve ⑧ YÖNTEM dört filmin dördünde de KOŞULMADI — 07.09.2026'da,
   proje sahibinin isteğiyle açıldılar: "durmadan inşa" ve "her parça
   sıfırdan, yapımı görünerek". Malzemeleri eski raporlarda zaten var:
     ⑦'nin konusu: "workers hold frozen poses for the whole clip" (① kat.8)
     ⑧'in konusu: ② APPEARING hükmü dört filmde dört kez — ama hangi PARÇA
                  belirdi, hiçbir rapor adıyla yazmadı. ⑧ onu adıyla yazar.
```

```
⭐ THE NARROW LOT — DEPONUN İLK GEÇEN HÜKÜMLERİ
   ① TIMELAPSE ✅ · ③ PASSES ✅ · ⑤ SAME WORLD ✅ + kanıt nesnesi BULUNDU ·
   ⑥ TIME ✅.  Üç filmde ilk kez kadraj, dünya ve kesme aynı anda tuttu.
   ⛔ Düşen: ② DIFFERENT · APPEARING (üçüncü kez) · ⑥ METRONOM (ikinci kez) ·
      ④ NONE FOUND (üçüncü kez) · ③ TIME RATE 0/10 (gökyüzü ve gölge DONDU).
   ⭐ TAM KOŞAN TEK MERCEK ③'TÜR ve hükmü GEÇTİ. Beş mercek eksik girdiyle
      koştu: ① ve ⑤'e kare grabı, ② ④ ⑥'ya belge verilmedi.
```

```
🔴 THE DUST YEAR — ALTINCI FİLM · İLK MARS SAHASI · ⑧ DEPONUN EN DÜŞÜK SKORU
   ⛔ Film ARAÇ KAPISI KOŞULMADAN üretildi; üretim günlüğü hâlâ "DURUM ⛔ BOŞ".
      İzi ölçülebilir: ① dört istasyon grubu (tek istasyon beyan edilmişti) ·
      teslim ızgarası 6·8·4·4·6·4·10·4·6·10 = 62,0 sn, plan 60,0 idi
      (S1↔S2 yer değiştirmiş, S9 8,0 → 10,0).
   ⛔ Düşen: ⑧ APPEARED 0,0/10 — SEKİZ elemanın SEKİZİ "INCOMPLETE at NEVER".
      Yeni INSAAT_YONTEMI kılavuzunun bütün amacı buydu ve plan ona uymuştu;
      sonuç THE LONG DAY'den (1/9 MADE) DAHA KÖTÜ → DERS 36.
      ② DIFFERENT·APPEARING (altıncı kez) · ⑦ PARKED (on klibin sekizi %100
      boş) · ⑤ A SET REBUILT EACH TIME · ⑥ METRONOM (BEŞİNCİ kez — ızgara
      varyanslı olduğu hâlde → DERS 44) · ④ COST/FINAL BEAT FAIL.
   ⭐ Tutan: ⑥ TEXT AND BRANDING 10/10 · ⑤ VEGETATION AND WATER 10/10 ·
      ⑥ CUT MECHANICS 10/10 · DIRECTION 10/10 · ③ "About one year" —
      filmden okunan süre plandaki 1 Mars yılını TUTTU.
   ⭐ Kimse yürüyen insan bildirmedi: DERS 33'ün pozitif yarısı ("No people
      are present.") TUTTU. İnsan makinenin içinden geldi → DERS 41.
   → DERSLER.md: DERS 35-44 · DERS 34'ün kilidi ölçüldü ve düştü.
```

```
✅  koşuldu, skor tabloda
Ⓥ   koşuldu ama mod V (ön koşu) — tamlık için sayılır, skor bağlayıcı değil
❌  koşulmadı
—   üretim yapılmadı, koşulamaz
```

## DURUM

```
BEFORE NIGHTFALL — YEDİNCİ FİLM · ⛔ HENÜZ ÜRETİLMEDİ
   ızgara 6 × 8,0 = 48,0 sn + kapak 5,0 · ⛔ DÜZ IZGARA (proje sahibi kilidi)
   ⭐ İLK KARA DELİK SAHASI · havasız kayaç ova · saha kartı YOK
   ⭐ FORMATI İLK KOŞAN FİLM: İKİ KEYFRAME ZİNCİRİ — 7 görsel · 6 klip · her
     klip iki onaylı kareye kilitli; dikişin iki yakası AYNI KARE.
     08.09.2026'da bu yöntem DEPONUN FORMATI oldu [KILAVUZ_REHBERI §2.7];
     bu film onun ilk uygulamasıdır. Kesme artık zaman sıçraması değil:
     film TEK GÜNDÜR (12,0 yerel saat).
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ · üretim günlüğü ⛔ AÇILMADI (üretim günü açılır)
   ⛔ KAPI: BLOCK ×1 (süre eşitliği — BİLİNÇLİ, plan §1.2) + FIX ×8
     (7'si prompt_kontrol §9 ↔ DERS 35 çelişkisi · 1'i ölçülmemiş kutu seti)
   ⛔ ÜRETİM AÇILMAZ: araç kapısı yedi ölçümü koşulmadı [ARAC_KARTLARI §4].
     İlk ölçüm bu filmde VAR/YOK sorusudur — kutu seti {4,6,8} çıkarsa 8,0 sn
     tek klipte teslim edilemez (tavan 7,00 sn) ve ızgara yeniden açılır.
     ⭐ SEKİZİNCİ SORU ARTIK KILAVUZDA [ARAC_KARTLARI §4 ölçüm 8]: araç İKİ
     KAREYLE (ilk+son) çalışıyor mu? Çalışmıyorsa bu FORMAT o araçta
     üretilmez — plan düşürülmez, araç değişir.
   ⭐ BU FİLM ÜÇ ÖLÇÜLMEMİŞ ŞEYİ İLK KEZ SINAR: DERS 36'nın oran kapısı
     (tam hâl/ara hâl < 1) · zincirin GEOMETRİ kanalı [A3-d] · DERS 44'ün
     tersi (kusursuz dikişte düz ızgara ⑥'yı düşürür mü).
   → dikey_shorts/BEFORE_NIGHTFALL/ · ölçüm yok, satır yok: mercek tablolarına
     film ÜRETİLMEDEN satır yazılmaz [kart Q ön koşulu].

THE LONG DAY
   ızgara 10 sahne · plan 6·4·6·4·6·6·8·4·6·10 · ⛔ KURGU 10 × 6,0 DÜZ kesildi
   ⭐ İLK UZAY SAHASI · İLK SEKİZ MERCEKLİ ÖLÇÜM · kapı üretimden ÖNCE ✅ GO
   ÜRETİLDİ ✅ · 8/8 mercek koşuldu ✅ · ⛔ SEKİZİ DE RUN INCOMPLETE (karesiz/belgesiz)
   ⛔ ÜRETİM GÜNLÜĞÜ YOK — plan ile film ayrıştı (astronot · güneş kadrajda ·
     dikey habitat · ikiz kule) ve sebebi kayıtta değil [DERS 28]
   ⭐ GEÇEN: ① TIMELAPSE (kamera·kadraj·çapa·istasyon 10/10) · ⑤ SAME WORLD +
     kanıt nesnesi BULUNDU (kaya + krater) · ④ ONE THING ilk kez bulundu ·
     ③ SEASON CARRIER 10 mevsimsiz sahada · ⑥ TIME
   ⛔ DÜŞEN: ② DIFFERENT·APPEARING (5.) · ③ NOT IN ONE DIRECTION (güneş
     kadrajda, gölge donuk) · ⑥ METRONOM (4.) · ⑦ PARKED · ⑧ APPEARED 1/9 ·
     ① PEOPLE 0 · SURFACE 0 · beş mercekte END CARD DIFFERENT
   → KARAR: yayınlanmaz · yeniden üretilmez · Dersler 28-34 ·
     RAPORLAR/THE_LONG_DAY.md §5

THE MOUNTAIN DOOR
   ızgara 5 × 6,0 (DÜZ — proje sahibi kilidi) · depo İÇİNDE yazıldı, GPT yok
   ⭐ KAPI ÜRETİMDEN ÖNCE KOŞULDU: ✅ GO — deponun dört filminde İLK KEZ
   ÜRETİLDİ ✅ · 6/6 mercek koşuldu ✅ · kapak kartı VAR
   ⛔ ALTI HÜKMÜN ALTISI DA DÜŞTÜ:
        ① SIX SEPARATE SHOTS   ② DIFFERENT · APPEARING (4. kez)
        ③ PASSES BUT NOT IN ONE DIRECTION
        ④ ENDS · NONE FOUND (4. kez)
        ⑤ A SET REBUILT EACH TIME · kanıt NONE FOUND
        ⑥ NEXT · METRONOM (3. kez)
   ⭐ GEÇEN: ③ SEASON CARRIER 10/10 · VEGETATION 10/10 · SHADOW/SUN 8/10 ·
     zaman tahmini "9-12 ay" — plan 12 ay, İKİNCİ KEZ TUTTU.
   ⛔ KÖK SEBEP DEĞİŞTİ — artık prompt mimarisi DEĞİL, ÜRETİM AKIŞI:
     ① CAMERA LOCK 0/10 · beş klipte de push-in. Ölçülebilir çapa cümlesi
     beş I2V'de de VARDI; NARROW LOT'ta aynı cümle 10/10 almıştı → araç
     ön ayarı [DERS 23]. Zincir tutmadı: 4/4 dikişte kusur, plana kasten
     konan kanıt nesnesi İLK dikişte kayboldu [DERS 25].
   ⛔ ÖLÇÜLEN HİPOTEZ DÜŞTÜ: klip içi vuruş varyansı metronomu kırmadı —
     ⑥ RHYTHM 0/10, deponun en düşüğü [DERS 24].
   ⛔ DERS 17 İKİNCİ KEZ: SPEC üretimden ÖNCE hazırdı ve mercekler yine
     belgesiz koştu (6'nın 5'i eksik girdi). Eksik olan belge değil,
     koşu YORDAMI [DERS 27].
   → KARAR: yayınlanmaz. Yeniden ÜRETİLMEZ — önce ARAÇ KAPISI ve ZİNCİR.
     Dersler 23-27 · RAPORLAR/THE_MOUNTAIN_DOOR.md §8

THE NARROW LOT
   ızgara 5 × 6,0 · MOTOR_5_SAHNE'nin ilk koşusu · harici GPT
   promptlar ✅ · ⛔ KAPI KOŞULMADI (üretimden sonra koşuldu: 25 madde BLOCK)
   ÜRETİLDİ ✅ · 6/6 mercek koşuldu ✅ · kapak kartı ÜRETİLMEDİ
   ⭐ DÖRT HÜKÜM İLK KEZ GEÇTİ: ① TIMELAPSE · ③ PASSES · ⑤ SAME WORLD · ⑥ TIME
     ⑤ "THE OBJECT THAT PROVES IT IS THE SAME PLACE: coiled hose" — bu satır
     iki filmde de NONE FOUND'du ve deponun en ağır satırıydı.
     ③ zaman tahmini "about one year" — plan ~12 ay. İlk kez TUTTU.
   ⛔ KÖK SEBEP DEĞİŞTİ: artık üretim sırası değil, PROMPT MİMARİSİ.
     Hareketle ilgili her kural GÖRSEL promptta kaldı, I2V'ye hiç girmedi:
     TIME RATE 5/5 görselde · 0/5 I2V'de → ③ TIME RATE · CLOUD · SUN = 0/10.
     Ve YAPI BIBLE sayısız yazıldı ("regular structural bays", oturum yok)
     → ② STRUCTURE IDENTITY 2/10. Aynı filmde SAYILI çapa bloğu 10/10 aldı.
   ⚠️ ⑥ METRONOM: kesmeler 6,0 · 6,0 · 6,0 · 6,0. Brief bunu ÖNCEDEN
     uyarmıştı; ritim varyantı artık varsayılan.
   → KARAR: yayınlanmaz. Yeniden ÜRETİLMEZ, yeniden YAZILIR.
     Dersler 18-22 · RAPORLAR/THE_NARROW_LOT.md §11

THE CLOSING SPAN
   promptlar ✅ · kapı GO ✅ · ÜRETİLDİ ✅ · 6/6 mercek koşuldu ✅
   ⛔ ALTI HÜKMÜN BEŞİ DÜŞTÜ:
        ① AYRI AYRI GÖRÜNTÜLER   ② FARKLI · APPEARING
        ③ YANLIŞ YÖNDE GEÇİYOR   ⑤ HER ÇEKİMDE YENİDEN KURULMUŞ · NONE FOUND
        ⑥ SIRADAKİ · METRONOM    ④ BİTİYOR (tek geçen) ama NONE FOUND
   ⭐ TEK BÜYÜK KAZANIM: ① CAMERA LOCK 10/10 (v1'de 4/10) — DERS 6 tuttu.
   ⛔ KÖK SEBEP YİNE AYNI: ters inşa zinciri koşulmadı → 8 ayrı vantaj,
     9/9 dikiş DEFECT. DERS 5 yazılıydı ve KAPI ilan edilmişti; yazılı
     kural kapı değildir [DERS 12].
   ⚠️ ② ④ ⑥ BELGESİZ koşuldu (mod V) — sözleşme sorusu hiç sorulmadı [DERS 17].

THE LONG SHADOW v1
   promptlar yazıldı ✅ · prompt kapısı GO ✅ · ÜRETİLDİ ✅ · 4/4 mercek koşuldu ✅
   ⛔ DÖRT HÜKMÜN DÖRDÜ DE DÜŞTÜ:
        ① ALTI AYRI GÖRÜNTÜ   ② FARKLI · APPEARING
        ③ GEÇİYOR (yön kırık)  ④ DURUYOR · NONE FOUND
   → KARAR: v1 YAYINLANMAZ. Yeniden planlanıp yeniden üretilir.
     Sebepler ve dersler: RAPORLAR/THE_LONG_SHADOW.md · DERSLER 3-9
   ⭐ ÖLÇÜMÜN DEĞERİ: dört mercek de dokümansız (mod V) koştu ve
     dördü de birbirinden bağımsız olarak AYNI kök sebebe işaret etti —
     ters inşa üretim sırası koşulmadı. Varsayım ölçüme dönüştü [DERS 5].
```

## KURAL

```
· Bir film ÜRETİLMEDEN hiçbir mercek koşulmaz. Rubrik promptu değil VİDEOYU
  eleştirir; plana koşulan bir rubrik prompt kapısının işini tekrar eder.
· ③ ve ④ TAM KURGU ister. Tek klibe koşulmuş bir ③ raporu GEÇERSİZDİR.
· ① · ③ · ⑤'e doküman VERİLMEZ (QA/00_README §1).
· ⑥ SESLİ kurgu ister — ölçü hizasını sessiz bir dosyada denetleyemez.
· ASGARİ SET: ① + ② + ⑤. Bu üçü koşulmadan film yayınlanmaz.
· VERDICT satırı skor ortalamasından bağımsızdır ve çeliştiğinde KAZANIR.
```
