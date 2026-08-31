# 🔍 THE LONG SHADOW — QA SPEC

> Bu dosya rubriğe/denetime **doküman olarak** verilir (mod D). İçinde yorum
> yoktur, yalnız **ölçülebilir kilitler** vardır. Bir kilit sayıyla yazılamıyorsa
> kilit değildir, tariftir.

---

## 0. KÜNYE

```
FİLM          THE LONG SHADOW — Uzayan Gölge
FORMAT        9:16 dikey · 6 sahne · sahne başına 10 sn · toplam 60 sn
              ⛔ Bu ızgara ARAÇTAN ölçülmeden kesinleşmez [D-d]:
                 ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
                 Ölçülen değer buraya yazılır: __________
YAPI          18 katlı betonarme kule · 24×18 m · 58,7 m taç
SAHA          şehir içi dar parsel + kış (SAHA_VE_IKLIM §3.1 + §3.5)
ZAMAN YAYI    14 ay
KAMERA        hibrit — ANA (4 sahne) + ÇUKUR (S1) + VİNÇ (S2)
ÜRETİM SIRASI ters inşa: S5 usta kare → S4 → S3 → S0 · S1/S2 ayrı
```

---

## 1. ⛔ FİNAL VURUŞ KANITI — teslimin tek kapısı

```
SAHNE       S5
SANİYE      0:57,5
GÖRÜLMESİ GEREKEN ŞEY:
   Kulenin gölgesi, kadrajın sağındaki BEŞ KATLI KIRMIZI TUĞLA BLOĞUN
   güneybatı yüzünü KALDIRIMDAN ÇATI SIRTINA KADAR baştan sona kaplıyor,
   ve arkasındaki gökyüzü hâlâ aydınlık.

KOMUT
   ffmpeg -ss 57.5 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ Bu karede gölge tuğla bloğun üstünde DEĞİLSE film TESLİM EDİLMEMİŞTİR —
   klip sayısı 6, süre 60 sn ve kadraj sabitliği tutsa bile kurgu kapısı DÜŞER.
   Sebep: bu filmin BEDELİ tek bir karede yaşıyor ve kapı klip sayar,
   vuruş saymaz [D-e].
```

---

## 2. KADRAJ KİLİTLERİ — ana istasyon (S0 · S3 · S4 · S5)

Formül: `kare yüzdesi = %50 + (y − 24) / 108`  ·  tolerans **± %2**

| Ne | y (m) | Beklenen | Hangi sahnelerde |
|---|---:|---:|---|
| ufuk çizgisi | 24,0 | %50,0 | 4 sahnede de |
| yapı tabanı | 0 | %27,8 | 4 sahnede de |
| tuğla blok çatı sırtı | 15,5 | %42,1 | 4 sahnede de |
| servi tepesi | 19,0 | %45,4 | 4 sahnede de |
| taç (parapet) | 58,7 | %82,1 | S0 · S4 · S5 |
| 7. döşeme | 22,4 | %48,5 | S3 başlangıç |
| 8. döşeme | 25,6 | %51,5 | S3 · ufku geçiş anı |
| 18. döşeme | 57,6 | %81,1 | S3 bitiş · S4 |

```
⛔ ÜST SINIR: hiçbir yapı parçası %87,5'in üstünde olamaz (üst 1/8 = arayüz).
⛔ ALT SINIR: ilerlemeyi kanıtlayan hiçbir şey %25'in altında olamaz.
⛔ SAĞ ŞERİT: kanıt nesnesi kare genişliğinin sağ %13'ünde duramaz.
```

---

## 3. DEĞİŞMEZLİK KİLİTLERİ — sahneler arası

```
① KAMERA        6 sahnenin 6'sında da kamera hareketi = 0 kare.
                Pan/tilt/zoom/kayma/sarsıntı: hiçbiri 1 karede bile yok.
② ANA İSTASYON  S0 · S3 · S4 · S5'te lens 24 mm · yükseklik 24,0 m ·
                mesafe 72 m · bakış 035° · tilt 0°. Dördü BİREBİR aynı.
③ ÇAPA ①        tuğla blok: 6 sahnenin 6'sında da BEŞ katlı, çatısında
                İKİ baca, çatı sırtı %42,1 (± %2). Kat sayısı değişirse BLOCK.
④ ÇAPA ②        servi: TEK ağaç, eğik gövde, tepe %45,4 (± %2). ANA istasyon
                sahnelerinde (S0·S3·S4·S5) her karede var.
⑤ ÇAPA ③        sırt hattı silueti aynı tepe dizilimi, ~%47.
⑥ UFUK          %50,0 · sapma ± %2 · 4 ana sahnede de
⑦ YAPI GEOMETRİSİ  kat yüksekliği 3,20 m sabit · oturum 24×18 m sabit ·
                aks 4,0 m sabit · cephe rengi antrasit + açık gri sabit
```

---

## 4. MONOTON BÜYÜME KİLİDİ

| Geçiş | Kat sayısı | İzin verilen | Yasak |
|---|---|---|---|
| S0 → S1 | — → 0 (çukur) | ters açılış · S0 kurgu sırasında ilk sahnedir | — |
| S1 → S2 | 0 → 5 | temel + 5 kat | çukurun kaybolması |
| S2 → S3 | 5 → 7 | S2 içinde 5→7 | 7'nin altına inmek |
| S3 → S4 | 7 → 18 | S3 içinde 7→18 | kat yüksekliğinin değişmesi |
| S4 → S5 | 18 (cephe 0→18) | S4 içinde cephe tırmanışı | kule boyunun artması |

```
⛔ YAPILMIŞ İŞ GERİ ALINMAZ. Tek istisna GEÇİCİ EKİPMANDIR ve söküm anı
   burada yazılıdır:
     şantiye çiti   S0 (var) → S4 (var) → S5 (YOK)   söküm: S4 ile S5 ARASINDA
     kule vinci     S2 (kurulur) → S4 (var) → S5 (YOK)  söküm: S4 ile S5 ARASINDA
     konteynerler   S0 (var) → S4 (var) → S5 (YOK)   söküm: S4 ile S5 ARASINDA
⛔ Hiçbiri bir klibin İÇİNDE kaybolmaz. Klip ortasında yok olan ekipman = BLOCK.
```

---

## 5. GÜNEŞ KİLİTLERİ

| S | Mevsim | Azimut | Yükseklik | Gölge yönü |
|:-:|---|---:|---:|---|
| 0 | Temmuz (öğle → ikindi) | 178° → 258° | 68° → 22° | kuzey → doğu-kuzeydoğu |
| 1 | Eylül | 218° | 44° | kuzeydoğu |
| 2 | Aralık | 226° | 17° | doğu-kuzeydoğu |
| 3 | Şubat | 232° | 16° | doğu-kuzeydoğu |
| 4 | Haziran | 248° | 38° | doğu-kuzeydoğu |
| 5 | Eylül (sabah → ikindi → akşam) | 112° → 258° | 30° → 20° | batı-kuzeybatı → doğu-kuzeydoğu |

```
⛔ MEVSİM TEK YÖNDE: Temmuz → Eylül → Aralık → Şubat → Haziran → Eylül ✅
⛔ KLİP İÇİNDE GÜNEŞ TEK YÖNDE: doğudan batıya. Geri dönen gölge = BLOCK.
⭐ S0'ın SON karesi ile S5 · 0:57,5'in ışığı AYNI olmak zorunda
   (Eylül/Temmuz ikindisi · elevation ~20-22° · gölge doğu-kuzeydoğu).
   Farklıysa kanıt çifti geçersizdir ve filmin bedeli okunmaz.
```

---

## 6. METİN VE İNSAN KİLİTLERİ

```
EKRAN METNİ          0,0 saniye. Hiçbir karede okunabilir harf/rakam/sembol yok.
YÜZEY YÜZEY SAYIM    çit · tabela · vinç · makine · konteyner · yelek · kask ·
                     kamyon · iskele · kalıp · cephe · dükkân · pano · sokak
                     levhası · plaka — on beş yüzeyin on beşi de temiz [D-b]
İNSAN                okunabilir yüz 0 kare. Bütün insanlar bulanık hareket
                     çizgisi. Net duran insan = FIX.
ARAÇ                 net duran araç yok; hepsi leke/iz
```

---

## 7. RENDER ÇUKURU KİLİDİ

```
Her ana sahnede kadrajda AYNI ANDA bulunması gereken en az dört şey:
   ① çamur veya lastik izi   ② su birikintisi veya ıslak leke
   ③ istiflenmiş malzeme     ④ branda / örtü / kesme artığı
S3'te ayrıca: kar GRİ, izli, yığılmış ve kısmen erimiş — temiz beyaz kar = FIX.
⛔ Temiz, düzenli, boş bir şantiye = emlak render'ı = BLOCK.
```

---

## 8. KURGU KAPISI

```
a) klip sayısı        6
b) toplam süre        6 × ölçülen klip süresi (± 0,5 sn)
c) kesme içi          her klipte 0 kesme · geçiş efekti 0
d) sahne sırası       S0 · S1 · S2 · S3 · S4 · S5
e) ekran metni        0,0 sn (jenerik kartı dahil)
f) ⛔ FİNAL VURUŞ     §1 — ffmpeg ile kanıtlanır
g) 120 PX TESTİ       kapak + S0'ın 0. karesi (sips -Z 120)
h) ihraç              1440p+ · BT.709 · 48 kHz · −14 LUFS · −1,0 dBTP
i) müzik hizası       96 BPM · sahne geçişleri ölçü başına denk geliyor mu
j) gerçeklik beyanı   açıklamanın son satırında var mı
```
