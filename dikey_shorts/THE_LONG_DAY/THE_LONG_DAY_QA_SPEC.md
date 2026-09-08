# 🔍 THE LONG DAY — QA SPEC

> ⛔ **BU SPEC ÜRETİMDEN ÖNCE YAZILDI.** Buradaki her kilit, plandaki on
> görsel ve on I2V promptunun içinde İngilizce olarak YAZILIDIR. Hiçbir
> satır uydurulmadı; ölçülmemiş olanlar §7'de açıkça AÇIK olarak durur.
>
> ⭐ VE BELGE YETMEZ [DERS 27]: MOUNTAIN DOOR'da SPEC üretimden önce hazırdı
> ve mercekler yine belgesiz koştu. Her koşudan ÖNCE tek satır yazılır ve
> raporun başına yapıştırılır: `verilen girdiler: <dosya adları>` (§8).

---

## 0. KÜNYE

```
FİLM          THE LONG DAY — Uzun Gün
FORMAT        9:16 dikey · 10 sahne = 60,0 sn (6,0 · 4,0 · 6,0 · 4,0 · 6,0 ·
              6,0 · 8,0 · 4,0 · 6,0 · 10,0 — hedef)
KAPAK KARTI   5,0 sn · SAHNE DEĞİL · SON 5 sn · S9'un 0:54,0 karesinden türer
TOPLAM        65,0 sn
YAPI          Ay yüzey üssü · 2 gömülü modül (12,0 × 4,4 m) + tünel + 2 güç
              direği (18,0 m) + iletişim direği (22,0 m) + yol
SAHA          🌕 Ay yüzeyi · mare ovası · 20° kuzey · SAHA KARTI YOK (plan §7)
ZAMAN YAYI    19 Ay günü ≈ 19 ay · gün 0 → gün 19 · MEVSİM YOK
KAMERA        tek istasyon — ANA (10 sahnenin 10'u) · detay istasyonu YOK
ÜRETİM SIRASI ⛔ TERS: S9 usta kare → S8 → … → S0
              her kareden sonra zincir_kontrol.sh + KAYA elle doğrulanır
KAYNAK        depo içi · kilavuzlar/TIMELAPSE_SISTEM_PROMPTU.md
KAPI          python3 araclar/prompt_kontrol.py → ✅ GO (üretimden ÖNCE · 07.09.2026)
⛔ KLİP SÜRESİ ffprobe ile HENÜZ ÖLÇÜLMEDİ [D-d]. 6,0 hedeftir, ölçüm değil.
⛔ ARAÇ KAPISI HENÜZ KOŞULMADI [DERS 23]. Hangi araçla üretileceği ve
   aracın 10 sn klip verip vermediği (S6 · S9) bilinmiyor.
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S9
SANİYE      0:59,6   (S9 klibinin son 0,4 saniyesi · sahne bloğu 0:50,0–1:00,0)
GÖRÜLMESİ GEREKEN ŞEY — beşinin BEŞİ birden:
   ① İKİ düz tepeli regolit tümseği, ikisi de aynı yükseklikte, aralarında
      alçak tünel tümseği; öndekinin güney ucunda torba duvar içinde
      yuvarlak kapak + lumboz. Hiçbir geçici ekipman YOK (paletli araç,
      yığın, torba istifi, ambalaj çerçevesi).
   ② ÜÇ direk: solda 22 m iletişim direği, ÇANAĞI SOL ÜSTE ÇEVRİLMİŞ VE
      KİLİTLİ (klibin ~7. saniyesinde döndü); sağda iki 18 m güç direği,
      panelleri güneşe (kameranın arkasına, sağa) dönük.
   ③ GÜNDÜZ IŞIĞI · S0 ile AYNI: azimut 100° · yükseklik 15° — kayanın
      gölgesi SOLA uzun, gökyüzü siyah, yıldız YOK, projektör ve lumboz
      gündüzde sönük. Bu kare S0'ın ilk karesiyle yan yana konur: LOOP.
   ④ ⭐ BEDEL ①: iniş aracı ile kaya arasındaki ova BAŞTAN BAŞA İZ YUMAĞI;
      yol düz ve koyu; S0'da izsiz olan yüzeyde tek bir temiz alan yok.
   ⑤ ⭐ BEDEL ②: sağ kenardaki iniş aracı TEPEYE KADAR TOZ GRİSİ (S0'da
      bembeyazdı); yerinde, silueti aynı.
   + basınçlı rover hava kilidine yanaşık, hareketsiz.

KOMUT
   ffmpeg -ss 59.6 -i teslim.mp4 -frames:v 1 kanit.jpg
   ffmpeg -ss 0.0  -i teslim.mp4 -frames:v 1 s0_kare0.jpg     ← LOOP çifti

⛔ Beşinden biri o karede görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR — klip
   sayısı ve süre tutsa bile [D-e].
⭐ ④ merceğinin "THE ONE THING THIS FILM DOES" satırının cevabı ④ ve ⑤'tir.
   Dört filmde de bu satır NONE FOUND geldi; sebebi BEDELİN YAZILMAMASIYDI.
```

---

## 2. KADRAJ KİLİTLERİ — ANA istasyon (10 sahnenin 10'u)

Formül (`KAMERA_ISTASYONU §3`): `kare yüzdesi = %50 + f × (y − h) / (36 × D)`
Bu filmde `f = 24`, `h = 3,0`, `D = 40` → **kare yüzdesi = %50 + (y − 3,0) × 1,667**
Tolerans **± %2**. Uzak sırt için açı formülü: `%50 + 66,7 × tan(θ)`.

| Ne | y (m) | Beklenen | Hangi sahnelerde |
|---|---:|---:|---|
| ufuk çizgisi | 3,0 | **%50,0** | 10 sahnede de |
| ova / pad yüzeyi (üs derinliğinde) | 0 | %45,0 | 10 sahnede de |
| yığın sırtı tepesi (S3) | 3,0 | %50,0 | S3 · S4 |
| modül gövde tepesi (ayaklarda) | 5,2 | %53,7 | S4 (klip sonu) · S5 |
| iniş aracı gövde tepesi | 5,2 | %53,7 | 10 sahnede de |
| kaya tepesi ⭐ | 6,0 | %55,0 | 10 sahnede de |
| tümsek tacı (S6 başı) | 6,0 | %55,0 | S6 ilk kare |
| tümsek tacı (tamam) | 6,9 | %56,5 | S6 sonu · S7 · S8 · S9 |
| katlı güç direği (S2 başı) | 6,0 | %55,0 | S2 ilk kare |
| iletişim direği (S7 başı) | 10,0 | %61,7 | S7 ilk kare |
| krater sırtı (θ = 11,8°) | — | %64,2 | 10 sahnede de |
| güç direği tepesi | 18,0 | %75,0 | S2 sonu → S9 |
| iletişim direği tepesi | 22,0 | %81,7 | S7 sonu → S9 |

```
⛔ ÜST SINIR: hiçbir yapı parçası %87,5'in üstünde olamaz (üst 1/8 = arayüz).
              İletişim direği tacı %81,7 ile sınırın altındadır.
⛔ ALT SINIR: ilerlemeyi kanıtlayan hiçbir şey %25'in altında olamaz.
              Ova %45,0 — geniş pay var. Taze krater (%38-44) KANIT DEĞİL,
              ÇAPADIR; alt %25'e girmez.
⛔ SAĞ ŞERİT: kanıt nesnesi kare genişliğinin sağ %12,5'inde duramaz.
              İniş aracı sağ %16'da (x ≈ %84) ama o bir ÇAPADIR. Güç
              direkleri x %64 ve %74 — kanıt oldukları S2-S3'te şeridin
              dışındadır.
⚠️ NARROW LOT'ta ① SAFE AREA 4/10 geldi; COMPOSITION bloğu yoktu [DERS 20].
   Bu filmde COMPOSITION bloğu on promptun ONUNDA da birebir vardır.
```

---

## 3. DEĞİŞMEZLİK KİLİTLERİ — sahneler arası

```
① KAMERA        10 sahnenin 10'unda da kamera hareketi = 0 kare.
                Pan/tilt/zoom/kayma/sarsıntı: 1 karede bile yok.
                ⛔ MOUNTAIN DOOR'da beş klipte push-in: ARAÇ ön ayarıydı
                   [DERS 23]. Araç kapısı koşulmadan bu satır ölçülemez.

② ANA İSTASYON  10 sahnede de: lens 24 mm · yükseklik 3,0 m · mesafe 40 m ·
                bakış 350° · tilt 0° · roll 0°. Onu BİREBİR aynı cümle.

③ ÇAPA ① ARKADA Krater sırtı: kesintisiz tek çizgi · TAM BİR V çentiği
                merkezin solunda · TAM BİR yuvarlak tepe merkezin sağında.
                ⛔ Çentik/tepe sayısı ya da yeri değişirse BLOCK.
                ⭐ S7'nin kanıtı: direk tepesi çentiğin ÜSTÜNE çıkar.

④ ÇAPA ② SOLDA  Ev boyunda gri KAYA · 6,0 m yüksek · 9,0 m geniş · x ≈ %26.
                ⭐ ⑤ merceğinin "aynı yer" KANIT NESNESİ budur VE filmin
                   saat ibresidir (gölgesi her klipte süpürür).
                ⛔ 10 sahnenin 10'unda da aynı yerde ve aynı boyutta.
                ⛔ ZİNCİR KAPISI MADDESİ [DERS 25]: her zincir_kontrol
                   koşusunda ELLE bakılır. Kaybolduysa kare ATILIR.

⑤ ÇAPA ③ SAĞ ÖN Taze krater · 14 m çap · parlak ejekta halkalı yüksek kenar ·
                18 m'de. Hiçbir araç içine girmez; kenarı hiçbir sahnede
                ezilmez. İkinci "aynı yer" nesnesi.

⑥ ÇAPA ④ SAĞDA  İlk iniş aracının iniş kademesi · sekizgen · 5,2 m · dört
                ayak 8,0 m · x ≈ %84. Silueti 10 sahnede aynı.
                ⚠️ RENGİ DEĞİŞİR ve değişmek ZORUNDADIR (zaman nesnesi):
                   S0-S2 bembeyaz → S3 ayaklar gri → S6 ayaklara kadar gri,
                   üstü çizgili → S7-S9 tepeye kadar gri. GERİ BEYAZLAMAZ.
                   Bu ayrım ⑤'te denetlenir: silüet sabit, renk monoton.

⑦ UFUK          %50,0 · sapma ± %2 · 10 sahnede de.

⑧ YAPI GEOMETRİSİ  modül 12,0 × 4,4 m · 6 ayak 0,8 m · merkezden 12,0 m ·
                ikinci modül 8,0 m geri + 10,0 m sağ · tünel 6,0 × 2,0 m ·
                tümsek 2,5 m / 17,0 × 9,4 m / taç 6,9 m · torba duvar 5,0 m ·
                kapak 1,2 m · lumboz 0,6 m · güç direği 2 × 18,0 m (14 m ara)
                · panel 6,0 × 3,0 m · iletişim direği 22,0 m · çanak 2,4 m ·
                yol 4,0 m.
                ⛔ Bu sayılar on promptun onunda da BİREBİR yazılıdır.

⑨ VİNÇ          ⛔ BU FİLMDE VİNÇ YOKTUR ve "crane" kelimesi hiçbir promptta
                geçmez. Direkler teleskopik, modüller araç kasasıyla iner.
                ⛔ Herhangi bir karede vinç/halat/kanca görünürse kare ATILIR.

⑩ GÖKYÜZÜ       Gündüz karelerinde (S0-S8 + S9'un gündüz bölümü) gökyüzü
                SİYAH: yıldız YOK, Dünya YOK, mavi YOK, bulut YOK.
                ⛔ Dev Dünya çizen kare ATILIR — çapa değildir, plan onu
                   kadraj dışına koydu (batı-güneybatı, kamera arkası).
```

---

## 4. GÜNEŞ SAATİ KİLİDİ — Ay günü

| S | An | Başlangıç azimut · yükseklik | Bitiş azimut · yükseklik | Kayanın gölgesi |
|:-:|---|---|---|---|
| 0 | gün 0 sabah → akşam | 100° · 15° | 260° · 15° | sola uzun → uzağa kısa → sağa uzun |
| 1 | gün 2 geç sabah → akşam | 130° · 40° | 250° · 25° | sol-uzak orta → sağ-uzak uzun |
| 2 | gün 3 sabah → akşam | 100° · 15° | 260° · 15° | tam süpürme |
| 3 | gün 5 öğleden sonra → akşam | 150° · 55° | 265° · 12° | uzağa kısa → sağa uzun |
| 4 | gün 8 erken sabah → akşam | 95° · 10° | 255° · 20° | sola çok uzun → sağa uzun |
| 5 | gün 10 geç sabah → akşam | 120° · 32° | 262° · 13° | sol-uzak → sağa uzun |
| 6 | gün 14 sabah → akşam | 100° · 15° | 262° · 13° | tam süpürme (8,0 sn) |
| 7 | gün 15 öğleden sonra → akşam | 160° · 62° | 258° · 18° | uzağa kısa → sağa uzun |
| 8 | gün 18 sabah → akşam | 105° · 22° | 262° · 13° | sola uzun → sağa uzun |
| 9 | gün 19 GECE → sabah | 85° · 6° ufkun altında | **100° · 15°** | (gece: yok) → sola uzun |

```
⭐ S9'un BİTİŞİ = S0'ın BAŞLANGICI (100° · 15°). LOOP kapısı budur.
⛔ KLİP İÇİ: her klipte gölge kadrajı SÜPÜRÜR ve açı değişimi 0° OLAMAZ.
   NARROW LOT'ta beş klibin beşinde de 0° ölçüldü; açılar yalnız görselde
   vardı [DERS 18]. Bu filmde on I2V'nin onunda da başlangıç VE bitiş
   açısı dereceyle yazılıdır.
⛔ GÜNEŞ HİÇBİR KAREDE KADRAJDA DEĞİL (kamera kuzeye bakar, güneş güneyden
   geçer). Kadrajda güneş diski / parlama görünen kare ATILIR.
⛔ MEVSİM YOK, YÖN VAR: her klipte gölge SOLDAN SAĞA döner (sabah → akşam),
   asla ters yöne. Sahneler arası mevsim sırası sorusu bu filmde yoktur;
   ③'ün SEASON ORDER kategorisi "not applicable" okumalıdır.
⭐ ③ "TIME READ FROM THE FILM ALONE": beklenen cevap "many lunar days /
   one to two years" — mevsim taşıyıcısı olmadığı için planın 19 ay
   iddiasını yalnız iz yoğunluğu ve toz taşır (§5).
```

---

## 5. ZAMAN NESNESİ (mevsim taşıyıcısı yerine) VE GİRİŞ HAZIRLIĞI

```
Bu sahada MEVSİM YOKTUR [DERS 14 · seçenek b]. Zamanı taşıyan iki nesne
MONOTON birikir ve geri gitmez — Ay'da rüzgâr yoktur:

İZ YOĞUNLUĞU (beton kürlenmesinin bu sahadaki karşılığı [A4-a])
  S0  izsiz ova (ilk kare) → klip sonunda TEK ÇİFT iz (rampa → kaya)
  S1  ilk çift + paletli araç izleri, bıçak izleri
  S3  pad baştan başa iz
  S6  araç–kaya arası iz YUMAĞI, pad gri churned
  S8  yol dışında her yer iz; yol düz ve koyu
  S9  iz yumağı + bot izleri; İLK ÇİFT ALTTA HÂLÂ VAR (kanıt satırı)
  ⛔ Hiçbir sahnede iz AZALMAZ. Azalan iz = zincir kırıldı.

TOZ GRİLEŞMESİ (iniş aracı)
  S0-S2 bembeyaz → S3 ayaklar gri → S4-S5 ayaklar gri, üst beyaz →
  S6 ayaklara kadar gri + üstü çizgili → S7-S9 tepeye kadar gri
  ⛔ Geri beyazlayan araç = zincir kırıldı.

YIĞIN (geçici — kurulur ve tükenir, söküm satırı)
  S1 alçak sırt → S2 1,5 m → S3 3,0 m → S5 1,0 m → S6 bitti
  ⭐ Yığın küçülürken tümsek büyür: aynı malzeme yer değiştiriyor.
     ② merceği "malzeme nereden geldi" sorusuna bununla cevap bulur.

⛔ GİRİŞ HAZIRLIĞI [DERS 21] BU FİLMDE TEK YERDE VAR: S8 → S9 kesmesi
   gündüzden GECEYE geçer. Hazırlık S8'in I2V'sinde YOK — çünkü Ay'da
   alacakaranlık yoktur; güneş battığı anda gecedir. Bu bilinçli bir
   karardır: S8 akşam ışığında (262° · 13°) biter, S9 gecede başlar.
   ⑥ C2 bunu "hazırlıksız geçiş" okuyabilir; §7'de AÇIK olarak durur.
```

---

## 6. MONOTON BÜYÜME VE SÖKÜM TAKVİMİ

```
S0  izsiz ova + beyaz iniş aracı + rampada rover     EKLENEN: İLK İZ (klip içi)
S1  + 20 × 12 m pad + alçak yığın sırtı               EKLENEN: PAD
S2  + güç direği ① (6 → 18 m) + kablo                  EKLENEN: DİREK ①
S3  + güç direği ② + yığın 3,0 m                       EKLENEN: DİREK ② · YIĞIN
S4  + modül A (kasada → ayaklarda) + 6 temel pedi     EKLENEN: MODÜL A
S5  + yan regolit 2,6 m + torba duvar 5,0 m + kapak    EKLENEN: YARIM TÜMSEK
S6  + tümsek tacı 6,0 → 6,9 m                          EKLENEN: TAM TÜMSEK · yığın BİTTİ
S7  + iletişim direği (10 → 22 m)                      EKLENEN: DİREK ③
S8  + modül B + tünel + B tümseği (2,6 → 6,9 m) + yol  EKLENEN: MODÜL B · YOL
S9  + basınçlı rover + lumboz/projektör + çanak döner  SÖKÜLEN: bütün geçici ekipman

SÖKÜM TAKVİMİ (hepsi S9'dan ÖNCE)
  açık rover              S0 iner → S8'e kadar park → S9'da YOK
  paletli araç            S1 belirir → S8 → S9'da YOK
  regolit yığını          S1 → S6'da tükenir (tümseğe girer)
  torba istifi + ambalaj  S1 → S8 → S9'da YOK
  son regolit tümseği     S6 klip içinde sıfırlanır

⛔ SÖKÜLMEYEN — BEDELDİR, kalır:
  iniş aracı kademesi     S0 → S9 (grileşir, yerinde)
  tekerlek izleri         S0 → S9 (birikir, ilk çift altta)
  kablo hatları           S2 → S9 (yarı gömülü)
  temel pedleri           S4 → S9 (tümseğin altında, görünmez ama var)
```

---

## 7. ⛔ BU SPEC'İN KENDİ AÇIKLARI — üretimden önce bilinen

```
⛔ SAHA KARTI YOK. §3 ⑩ ve §4'ün gökyüzü/gölge kilitleri bu planın kendi
   fiziğidir; hiçbiri bu depoda ölçülmedi.
⛔ KLİP SÜRESİ ÖLÇÜLMEDİ [D-d]. S6 (8,0) ve S9 (10,0) aracın 10 sn ayarını
   varsayar. Araç vermiyorsa §0, §1 ve plandaki bütün zaman kodları
   yeniden yazılır.
⛔ 4,0'lık sahneler (S1 · S3 · S7) 6,0 klipten SONDAN kırpılır: I2V'de
   yazılan bitiş açısı o üç sahnede EKRANA GELMEZ. §4'teki bitiş sütunu
   o sahnelerde klibin bitişidir, kesmenin değil. ③ SUN DIRECTION bunu
   okuyabilir.
⛔ S8 → S9 GÜNDÜZ → GECE kesmesi hazırlıksızdır (§5). ⑥ C2 düşebilir.
⛔ S9'UN IŞIK YAYI FARKLI (gece → şafak). Loop'un bedelidir.
⛔ İNSAN YOK. ① PEOPLE AND VEHICLES kategorisi yalnız araçları ölçebilir.
⛔ 1/6 g FİZİĞİ: fırlayan regolitin temiz parabolü, asılı toz yokluğu ve
   aracın yavaşlığı I2V'de yazılı; modelin Dünya fiziğiyle çizmesi beklenir.
⛔ DÜNYA VE YILDIZ: model "uzay" deyince ikisini de çizer. Negatif çekirdek
   adıyla yasaklıyor; tutmazsa bu filmin ilk aday dersidir.
⛔ TERS İNŞA bu depoda hâlâ hiç koşulmadı [AGENTS §6]; A3-a'nın hata
   birikimi iddiası ilk kez bu filmde sınanır.
```

---

## 8. KOŞULACAK MERCEKLER

```
⛔ 0. GİRDİ SATIRI — HER KOŞUDAN ÖNCE, TEK SATIR [DERS 27]
      "verilen girdiler: <dosya adları>"  → raporun başına yapıştırılır.
      bash araclar/kare_al.sh teslim.mp4 10   ① ve ⑤'ten ÖNCE koşulur.

ASGARİ SET  ① KARE + ② İNŞA + ⑤ DEVAMLILIK — bu üçü koşulmadan YAYINLANMAZ.
SIRA        ① · ③ · ⑤ · ⑦ ÖNCE (mod V · doküman verilmez)
            sonra ② (bu SPEC) · ④ (plan + kapak) · ⑥ (plan + SESLİ kurgu) · ⑧ (bu SPEC)

GİRDİ TABLOSU — koşuyu yapan kişi satırı kopyalar, başka hiçbir şey vermez:
  ①  verilen girdiler: teslim.mp4 · kareler/ (30 kare) · QA/1_KARE_QA.md
  ③  verilen girdiler: teslim.mp4 (TAM KURGU) · QA/3_ZAMAN_QA.md
  ⑤  verilen girdiler: teslim.mp4 · kareler/ (30 kare) · QA/5_DEVAMLILIK_QA.md
  ②  verilen girdiler: teslim.mp4 · THE_LONG_DAY_QA_SPEC.md · QA/2_INSA_QA.md
  ④  verilen girdiler: teslim.mp4 · THE_LONG_DAY_DIKEY_TIMELAPSE.md · kapak.png · QA/4_TESLIM_QA.md
  ⑥  verilen girdiler: teslim.mp4 (SESLİ) · THE_LONG_DAY_DIKEY_TIMELAPSE.md · QA/6_GECIS_QA.md
  ⑦  verilen girdiler: teslim.mp4 · kareler/ (30 kare) · QA/7_IS_QA.md
  ⑧  verilen girdiler: teslim.mp4 · THE_LONG_DAY_QA_SPEC.md · QA/8_YONTEM_QA.md

⭐ ⑧ İÇİN ELEMAN LİSTESİ bu SPEC'in §6'sıdır: pad · direk ① · direk ② ·
   yığın · modül A · torba duvar · tümsek A · iletişim direği · modül B ·
   tünel · tümsek B · yol · çanak. Her biri için "ilk EKSİK görüldüğü an"
   raporda olmalı; olmayan parça ADIYLA "APPEARED" yazılır.
⭐ ⑦ İÇİN: her klipte tek iş adımı klibin İLK YARISINA yazıldı (plan §2);
   boş aralık klibin ikinci yarısında çıkabilir. 4,0'lık sahnelerde kuyruk
   kırpıldığı için boş aralık kısalır; 8,0 ve 10,0'da uzar. ⑦'nin IDLE
   TABLE'ı bunu ölçer.```
