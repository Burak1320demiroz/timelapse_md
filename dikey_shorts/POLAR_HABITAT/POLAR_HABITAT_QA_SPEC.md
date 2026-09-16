# 🔍 POLAR HABITAT — QA SPEC

> ⛔ **BU SPEC ÜRETİMDEN ÖNCE YAZILDI.** Buradaki her kilit, plandaki yedi görsel ve altı I2V promptunun içinde İngilizce olarak YAZILIDIR.
>
> ⭐ VE BELGE YETMEZ [DERS 27 · 29]: her mercek koşusundan ÖNCE tek satır yazılır ve raporun başına yapıştırılır: `verilen girdiler: <dosya adları>`. Koşu `araclar/qa_paket.sh` ile PAKETLENİR.

---

## 0. KÜNYE

```
FİLM          POLAR HABITAT
FORMAT        9:16 dikey · 6 sahne × 8,0 sn = 48,0 sn  ⛔ DÜZ IZGARA
              (proje sahibinin kilidi · plan §1.2)
KAPAK KARTI   5,0 sn · SAHNE DEĞİL · teslimin SON 5 sn'si · G6'dan türer
              ⭐ kaynak kare · kapak promptu · başlığın dizilişi (sayıyla): POLAR_HABITAT_KAPAK.md
TOPLAM        53,0 sn
FORMAT (2)    ⭐ İKİ KEYFRAME ZİNCİRİ — 7 görsel · 6 klip · her klip iki onaylı kareyle kilitli.
              Dikişin iki yakası AYNI KARE. foto–video–foto · deponun formatı [KILAVUZ_REHBERI §2.7]
YAPI          ekstrem kutup yaşam alanı: Ø24,0 m altıgen temel halkası + 6 köşe ankraj pimi +
              12 kolonlu çelik kubbe karkası (14,0 m apex) + çift katmanlı kompozit termal kabuk +
              18,0 m merkez geothermal enerji kulesi (4 radyatör kanatlı) + 3,5 m buz kırıcı koruma duvarı
SAHA          karlı/buzlu gezegen buzul platosu · masif mavi-buz dağ sırtı önü (bearing 320° → 040°)
ZAMAN YAYI     yerel 10,0 saat (güneş azimut 110° → 210° · yükseklik 14° → 22°)
              Zamanın taşıyıcısı GÖLGE AÇISI VE İZ BİRİKİMİDİR.
KAMERA        tek istasyon — MAIN (altı sahnenin altısı) · detay istasyonu YOK
              h 6,5 m · D_eksen 40,0 m · D_kenar 28,0 m · bearing 145° · tilt 12° down · roll 0°
ÜRETİM SIRASI ⛔ TERS: G6 usta kare → G5 → G4 → G3 → G2 → G1 → G0
              her kareden sonra zincir_kontrol.sh + CANLI ÇAPA elle doğrulanır
KAPI          python3 araclar/prompt_kontrol.py → ✅ GO
```

---

## 1. ⛔ FİNAL KARE KANITI — teslimin tek kapısı

```
SAHNE       S5 (sahne bloğu 40,0–48,0)
SANİYE      0:47,6   (S5 klibinin son 0,4 saniyesi)

GÖRÜLMESİ GEREKEN ŞEY — YEDİSİNİN YEDİSİ birden:
   ① TAM KUBBE: 12 kolonlu çelik kubbe karkası ve üzerini %100 kapatan mat beyaz-amber kompozit termal paneller tam görünür.
   ② 18M ENERJİ KULESİ: Kubbe apexini delen 18m merkez geothermal kule dikili, 4 radyatör kanadı açık ve tepesinden cyan enerji parıltısı yükselmektedir.
   ③ İÇ IŞIKLAR: Silindirik çift hava kilidi modülünün porthole pencerelerinden ve ana girişten sıcak turuncu (2700K) iç yaşam ışığı sızmaktadır.
   ④ BUZ KORUMA DUVARI: Rüzgâr tarafındaki 3,5m basamaklı kesme buz blok koruma duvarı eksiksiz tamamlanmıştır.
   ⑤ TEMEL HALKASI: 24m altıgen geothermal temel halkası ve 6 köşe ankraj pimi permafrost tabanına kilitlidir.
   ⑥ ARKA PLAN ÇAPASI: Masif mavi-buz dağ sırtı silueti üst kadrajda pikselce aynı hizada ve yüksekliktedir.
   ⑦ IŞIK & GÖLGE: Gölgeler kuzeydoğuya doğru uzanmış, ikindi kutup güneşinin soğuk mavi gölge kırılmaları beyaz buz yüzeyine düşmektedir.

KOMUT
   ffmpeg -y -sseof -5.4 -i teslim.mp4 -frames:v 1 kanit.jpg
   ⭐ Kare TESLİM dosyasından alınır, üretilen klipten DEĞİL [KURGU_VE_TESLIM §2].
⛔ Yedisinden biri görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR.
```

---

## 2. KADRAJ KİLİTLERİ — MAIN istasyon (altı sahnenin altısı)

```
ufuk                 %50,0 — YEDİ karede de
dağ sırtı silueti    %75,0 — %85,0 arası (üst kadraj kilitli)
temel yakın kenarı   %35,2 (D_kenar = 28,0 m)
kubbe apex yüksekliği %58,2 (14,0 m apex)
18m kule tepesi      %68,0 (18,0 m taç)
kadraj               33,75 m geniş × 60,0 m yüksek · 32,0 px/m

⭐ YÜZDELER D_eksen = 40,0 m'DEN HESAPLANDI, saha kenarından değil [DERS 38].
```

---

## 3. 📋 KİLİT LİSTESİ

```
KİLİT 1 (Kamera):   Sabit istasyon (H=6.5m, D_kenar=28m, D_eksen=40m, Bearing 145°, Tilt 12° down, Roll 0°).
KİLİT 2 (Arka Plan): Masif mavi-buz dağ sırtı silueti 7 görselde de pikselce aynı konumda ve yükseklikte.
KİLİT 3 (Yapı):      24m altıgen temel, 12 kolonlu kubbe karkası, çift katmanlı termal kabuk, 18m kule.
KİLİT 4 (İnsansız):  Şantiyede insan/insansı figür yoktur; tüm işler otonom robotik ünitelerle yürütülür.
```
