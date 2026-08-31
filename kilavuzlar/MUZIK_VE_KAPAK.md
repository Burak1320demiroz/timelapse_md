# 🎶🖼️ MÜZİK, KAPAK VE PAKETLEME

> ⛔ **DİL KURALI:** başlık, açıklama, hashtag, sabitlenecek yorum ve
> **kapak metni İNGİLİZCEDİR.** Türkçe olan yalnız depo belgeleri ve QA
> raporlarıdır. Bu dosyanın anlatımı Türkçe, ürettiği her şey İngilizce.

---

# 1. MÜZİK — tek parça, 65 saniye, ızgaraya oturur

## 1.1 BPM ızgarası (zorunlu)

Sahne süresi 6,0 saniye olduğu için tempo **hesaplanır**, seçilmez:

```
        BPM = 240 × (sahne başına ölçü) ÷ (sahne saniyesi)
        6 saniyelik sahne için:  BPM = 40 × ölçü

   40 BPM  → 1 ölçü/sahne     ⛔ çok ağır, bu ızgarada kullanılmaz
   80 BPM  → 2 ölçü/sahne     ölçülü, belgesel
  120 BPM  → 3 ölçü/sahne     ⭐ VARSAYILAN — nabız var, acele yok
  160 BPM  → 4 ölçü/sahne     hızlı montaj hissi
  200 BPM  → 5 ölçü/sahne     ⛔ 6 saniyede kalabalık

120 BPM'de: her sahne 3 ölçü · sahne bloğu 30 ölçü · kapak kartı 2,5 ölçü.
Izgara dışı bir tempo (örn. 130) on kesmenin onunu da hizasız bırakır.
```

### ⭐ SAHNE SÜRELERİ EŞİT DEĞİL — ölçüye oturan varyans [DERS 13]

```
Ölçü uzunluğu = 240 / BPM saniye
   120 BPM → 2,0 sn → izinli sahne süreleri  4 · 6 · 8 · 10
   160 BPM → 1,5 sn → izinli sahne süreleri  4,5 · 6 · 7,5 · 9

Her sahne TAM SAYIDA ölçü tutar, yani kesmeler hâlâ ölçü başındadır —
ama sahneler artık eşit DEĞİLDİR. Müzik hizası korunur, metronom kırılır.

ÖRNEK (160 BPM · 10 sahne · 60,0 sn):
   6 · 4,5 · 6 · 4,5 · 6 · 7,5 · 6 · 4,5 · 6 · 9
   4    3    4    3    4    5    4    3    4    6   ← ölçü sayısı

⛔ On sahnenin süresi eşitse ⑥ merceği METRONOM hükmü verir ve o hüküm
   skor ortalamasını yener. Ölçülmüş vaka: THE CLOSING SPAN.
```

## 1.2 ⭐ KATMAN = KAT — 10 sahnede beş katman

Her İKİ sahnede bir katman eklenir, hiçbiri çıkmaz. Aşama merdiveninin
monoton büyüme yasasının sesteki karşılığı.

```
S0-S1   ① kuru nabız (her ölçünün 1. vuruşu)              1 katman
S2-S3   ② alçak bas nota, hareketsiz                       2
S4-S5   ③ metalik perküsyon — kalıp/çekiç ritmi            3
S6-S7   ④ sürtünmeli yaylı doku ⭐ KIŞ KATMANI              4
S8-S9   ⑤ geniş sıcak akor yastığı — armoniye zemin        5
KART    hepsi çözülür ve söner; son 1,5 saniye yalnız ortam sesi
```

⭐ **Kış katmanı gelince bir daha gitmez.** Kış filmin direnç sahnesidir
(S6-S7) ve müzik onu hatırlar: bina bittikten sonra da o doku altta durur.

## 1.3 Zorunlu maddeler

```
· SÖZ YOK · melodi hattı yok · geleneksel şarkı yapısı yok
· MÜZİKSİZ PENCERE: 0,0-1,5 sn. Kanca diegetik sesle açılır (uzak trafik,
  rüzgâr, tek makine). Uzun enstrümantal intro ELENİR.
· Diegetik ses yatağı müziğin altında sürer
· TELEFON HOPARLÖRÜ KURALI (missing fundamental):
  "Every sub-bass element below 150 Hz is doubled by its own upper harmonics
   at roughly 100, 150 and 200 Hz so the fundamental is implied rather than
   required; the low end is never the only carrier of the weight."
  Telefon hoparlörü ~300 Hz altını üretemez. Eşlikçi yedek değil, TAŞIYICIDIR.
```

## 1.4 Müzik promptu iskeleti

```
Instrumental score for a 65-second vertical construction time-lapse: a
60-second scene block of ten 6-second shots, followed by a 5-second end card.
No lyrics, no voice, no melody line, no traditional song structure.

Genre: [tür]
Tempo: 120 BPM, strict and bar-aligned, three bars per 6-second shot.

Layers (one added every two shots, none removed until the final bars):
1. [S0-S1]  2. [S2-S3]  3. [S4-S5]  4. [S6-S7 · winter]  5. [S8-S9]

Dynamic map across 65 seconds:
  0.0-1.5    silence — only the site's own ambience
  1.5-12.0   layer 1 alone
  12.0-24.0  layer 2 enters
  24.0-36.0  layer 3 enters
  36.0-48.0  layer 4 enters — the coldest and widest moment
  48.0-60.0  layer 5 enters, the stack sits together
  60.0-65.0  end card: everything resolves and decays; the last 1.5 seconds
             carry only ambience

Reference feel: [iki gerçek besteci — alıntı ÜRETME]
Phone-speaker rule: [missing fundamental cümlesi]
```

---

# 2. KAPAK — ⭐ BAŞLIK METNİ TAŞIR

> ⛔ **KURAL DEĞİŞTİ.** Önceki sürüm metinsiz kapak istiyordu. Artık kapak
> **İngilizce başlık metni taşır** ve videonun son 5 saniyesinde de görünür.
> Sebep: ters açılış kaldırıldığı için vaadi taşıyan yüzey kapaktır [DERS 3].

## 2.1 Kapak iki iş yapar

```
① IZGARA KAPAĞI   kanal ızgarasında ve "izlemeye devam et" kartında
② KAPAK KARTI     teslim dosyasının SON 5 SANİYESİ
                  ⛔ SAHNE DEĞİLDİR — planda ayrı beyan edilir [DERS 4]
İkisi AYNI görüntüdür. Kart hareketsizdir; zoom, kayma, animasyon yok.
```

## 2.2 ⛔ Kapak S9'un usta karesinden TÜRETİLİR

v1'de kapak kartı filmden ayrı üretildi ve **başka bir bina** çıktı
(① ANCHOR IDENTITY 0/10 · ④ FİNAL BEAT FAIL). Artık:

```
S9 usta karesi → aynı kadraj, aynı bina, aynı çapalar → üstüne başlık dizilir
⛔ Kapak sıfırdan üretilmez. Üretilirse kart, filmin bitirdiği binadan
   farklı bir bina gösterir ve film kendi finalini yalanlar.
```

## 2.3 BAŞLIK METNİ — sayılarla

```
DİL          İngilizce
UZUNLUK      en fazla 3 kelime  (kart 5 saniye görünür, okunacak zaman kısa)
YÜKSEKLİK    ⭐ büyük harf yüksekliği ≥ kare yüksekliğinin %8'i (≥154 px)
             Sebep: 120 px'e küçültülünce yaklaşık 10 px kalır — okunma eşiği.
             %7'nin altında ızgarada okunmaz.
KONUM        y = 500-1400 bandı · sağ 242 px'e girmez · sol 122 px'e girmez
             (kart videonun içinde de görünür ve arayüz alt 484 px'i kapatır)
KONTRAST     metin ile arkası arasında en az 4,5:1 · gerekiyorsa metnin
             arkasına düz koyu bir bant konur, gradyan değil
YAZI TİPİ    tek ağırlık, geniş harf aralığı, gölge/kontur/parlama YOK
ANİMASYON    yok. Kart 5 saniye boyunca hareketsizdir.
```

## 2.4 Kapak promptu iskeleti

```
[S9 usta karesinin görsel promptu birebir kopyalanır]
+ ek satır:
Leave the upper middle third of the frame visually simple and low-contrast so
that a title can be set over it: no structural detail, no strong edge and no
bright object between roughly forty and seventy percent of frame height on the
left two thirds of the picture.
Output: 9:16, 4K, no text, no watermark.
```

⛔ **Prompt hâlâ `no text` der.** Başlık kadraja MODELE yazdırılmaz —
post-prodüksiyonda dizilir. Model yazdığı yazıyı bozar; bu türün en sık
metin arızası budur.

## 2.5 ⭐ 120 PX POSTA PULU TESTİ — artık İKİ ŞEY arar

```
İKİ görüntüye birden koşulur:
   ① kapak (başlık dizilmiş hâli)      ② S0'ın 0. karesi
   sips -Z 120 <dosya> --out <test>

KAPAKTA aranan İKİ şey:
   ⓐ SİLUET   gökyüzüne karşı net bir dikey kütle ve sağında alçak bir kütle
   ⓑ BAŞLIK   kelimeler hâlâ ayırt ediliyor mu (harfler değil, KELİME şekli)

⛔ ⓐ kayboluyorsa kapak yeniden ÇERÇEVELENMEZ, SAHNE YENİDEN ÜRETİLİR.
⛔ ⓑ kayboluyorsa punto büyütülür ya da kelime sayısı düşürülür —
     asla "olsun, ızgarada büyük görünür" denmez.
⛔ Elle "bence okunuyor" demek bu testi geçmek sayılmaz.
```

---

# 3. PAKETLEME — İNGİLİZCE

```
3 TITLES        ≤ 40 karakter · merak sorusu · spoiler yok
1 DESCRIPTION   ilk satır kancadır · 2-3 cümle + tek satır teknik dayanak
8-12 HASHTAGS   3 geniş · 5 niş · 2-4 yapı-özel
PINNED COMMENT  yapının arkasındaki gerçek mühendislik, tek paragraf
⛔ AI DISCLOSURE  açıklamanın son satırı
```

## 3.1 İskelet

```
TITLES
1. [≤40 chars]
2. [≤40 chars]
3. [≤40 chars]

DESCRIPTION
[hook line — one sentence, the promise]
[2-3 sentences: what was built, what resisted, one measured fact]
[hashtags]

This video was generated with AI. It does not document a real project.

PINNED COMMENT
[the real engineering behind it, one paragraph, no company names]
```

## 3.2 ⛔ GERÇEKLİK BEYANI

```
· gerçek firma adı, logo, proje adı, parsel/şehir iddiası KULLANILMAZ
· açıklamanın son satırında AI beyanı bulunur (İngilizce)
· platformun kendi "altered content" beyanı AYRICA işaretlenir —
  açıklamadaki cümle onun yerine geçmez, iki ayrı yüzeydir
· gerçek bir yapının birebir kopyası üretilmez
```

## 3.3 Spoiler bütçesi — dört yüzey

| Yüzey | Ne verir | Ne vermez |
|---|---|---|
| Başlık | vaadin sorusunu | cevabı, bedeli, finali |
| Kapak | bitmiş yapının siluetini + başlığı | sürecin nasıl geçtiğini |
| İlk 2 sn | mekânı, ölçeği ve ilk işi | aşamaları, kışı, bedeli |
| Açıklama | ne yapıldığını ve tek teknik dayanağı | dönüm noktasını |

```
TEK CÜMLE TESTİ: dört yüzey yan yana konunca bir yabancı, videoyu izlemeden
sürecin dönüm noktasını söyleyebiliyor mu? → HAYIR olmalı.
```
