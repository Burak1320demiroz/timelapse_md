# 📦 PAKETLEME ŞABLONU — @apexait

> **Kurallar burada değil.** Başlık uzunluğu, hashtag sayısı, spoiler bütçesi
> ve sabit yorum zorunluluğu `kilavuzlar/MUZIK_VE_KAPAK.md` §3'tedir.
> Bu dosya o kuralların **kanal için doldurulmuş hâlini** tutar: sabit metinler,
> sabit altbilgi, sabit cevaplar.
>
> Dil kararı ve gerekçesi: `KANAL_KIMLIGI.md` §6. Türkçeye çevirmek istersen
> ⛔ **yalnız bu dosya** düzenlenir.

---

# 1. 🧾 BAŞLIK — üç kalıp

Üçü de yazılır, biri seçilir. Uzunluk sınırı: `MUZIK_VE_KAPAK` §3.

```
① SORU KALIBI      merakı bedelin üstüne kurar, cevabı vermez
   "Whose sunlight did it take?"
   "What was here before?"

② KAYIP KALIBI     ne kaybolduğunu söyler, nasıl olduğunu söylemez
   "The ferry stopped running"
   "The terraces went under"

③ İŞ KALIBI        yalnız işi söyler — en sade, en dayanıklı
   "18 floors on a plot this narrow"
   "A dam across this valley"

⛔ YASAK: sayı yemi ("99% don't know"), büyük harf bağırma, "SATISFYING",
   "you won't believe". Kapak ve başlık kanalın verdiği tek sözdür; yem
   verirse filmin ödeyeceği bir şey kalmaz.
⛔ YASAK: başlıkta gerçek proje/şehir adı (POLITIKA_VE_RISK §3).
```

---

# 2. 📄 AÇIKLAMA — iskelet

İlk satır kancadır (`MUZIK_VE_KAPAK` §3). Alt blok **her videoda birebir aynıdır.**

```
<KANCA — tek cümle, bedeli ima eder, finali vermez>

<2-3 cümle: yapı ne, saha ne, hangi direnç. Teknik dayanak TEK satır:
 kat döngüsü / açıklık / dolgu hacmi gibi tek bir gerçek mühendislik ölçüsü.>

<TEK SATIR: zaman yayı — "14 months in 60 seconds">

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration, no text on screen.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real site, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

<HASHTAG SATIRI — §3>
```

```
⛔ Son iki satır (İngilizce + Türkçe beyan) SİLİNMEZ, KISALTILMAZ, YER
   DEĞİŞTİRMEZ. Türkçe satır KILAVUZ_REHBERI §9.8'nın şart koştuğu cümledir;
   İngilizce satır izleyicinin fiilen okuduğu cümledir. İkisi de gerekir.
⛔ Açıklamadaki beyan, Studio'daki "Altered content" kutusunun YERİNE GEÇMEZ
   (POLITIKA_VE_RISK §2).
```

---

# 3. #️⃣ HASHTAG — sabit + değişken

Sayılar (kaç geniş / kaç niş / kaç yapı-özel): `MUZIK_VE_KAPAK` §3.

```
GENİŞ (sabit, her videoda)
   #timelapse #construction #architecture

NİŞ (sabit, her videoda)
   #civilengineering #buildingprocess #aivideo #shorts #constructionsite

YAPI ÖZEL (her videoda değişir — 2-4 tane)
   kule      → #highrise #concrete #towercrane
   köprü     → #bridge #cablestayed #engineering
   baraj     → #dam #hydropower #rcc
   yol/tünel → #roadconstruction #mountainroad
   liman     → #port #landreclamation
   stadyum   → #stadium #roofstructure
   türbin    → #windfarm #renewables

⭐ #aivideo SABİTTİR ve kaldırılmaz. Ne saklıyoruz ne özür diliyoruz;
   kanalın adı zaten söylüyor (KANAL_KIMLIGI §1).
```

---

# 4. 📌 SABİT YORUM — ⭐ kanalın en önemli 120 kelimesi

`POLITIKA_VE_RISK` §1.3: bu paragraf, kanalın "özgün ve otantik değer"
kanıtıdır. Paketleme kalemi değil, hayati organ.

```
İÇERİK: o yapının arkasındaki GERÇEK mühendislik — tek paragraf.
   · neden bu sıra (kazı → çekirdek → kat döngüsü → cephe)
   · o yapı tipinin gerçek zorluğu nedir ve sahada nasıl çözülür
   · filmdeki bir kararın gerçek karşılığı ("kışın kat döngüsünün
     uzaması betonun priz süresindendir")

⛔ ŞABLONLAŞTIRMA. Her videoda YENİ ve O YAPIYA ÖZEL yazılır.
   Şablonlaştığı gün kanalın tek özgünlük kanıtı kapanır ve
   POLITIKA_VE_RISK §1 kapısı bize döner.
⛔ Sabit yorumda gerçek proje adı, firma adı, "bu şuna benziyor" yok.
```

## 4.1 Sabit cevaplar — yorumlara

```
"Is this real?" / "Which project is this?"
   → It isn't one. Every frame is AI-generated. The building type and the
     construction sequence are real; the project, the company and the site
     are not.

"Why is the camera not moving?"
   → That's the whole point. A time-lapse is a fixed camera — if the frame
     moves, you can't see what changed.

"Why no music at the start?"
   → The first seconds are the site's own sound. The score builds one layer
     per stage and pulls out completely at the end.

"Can you do <real project>?"
   → No real projects here — see the description. But the building TYPE,
     yes: tell me which one.
```

---

# 5. ✅ YÜKLEME KONTROL LİSTESİ — Studio'da sırayla

```
□ 0  ⛔ QA DÖRT MERCEK koşuldu mu?       (QA/00_README — yayından ÖNCE)
□ 1  FİNAL KARE KANITI koşuldu mu?      (KILAVUZ_REHBERI §8 adım 9)
     ⛔ Koşulmadıysa film teslim edilmemiştir. Yükleme başlamaz.
□ 2  120 px posta pulu testi geçti mi?  (MUZIK_VE_KAPAK §2.5)
□ 3  Başlık — üç kalıptan biri (§1)
□ 4  Açıklama — iskelet + iki dilli beyan altbloğu (§2)
□ 5  Hashtag — sabitler + yapı özel (§3)
□ 6  ⛔ Ayrıntılar → "Altered content" → EVET   (POLITIKA_VE_RISK §2)
□ 7  Oynatma listesi — yapı tipine göre        (YAYIN_PLANI §7)
□ 8  Kapak / ilk kare kontrolü
□ 9  Yayınla → SABİT YORUM yaz ve sabitle (§4)
□ 10 Sıralama kuralı ihlal edildi mi? Bir önceki video aynı siluet
     ailesindense ⛔ YAYINLAMA, sırayı değiştir (YAYIN_PLANI §3)
□ 11 Ölçüm satırını aç (YAYIN_PLANI §6.1)
```

---

# 6. 📝 DOLDURULMUŞ ÖRNEK — THE LONG SHADOW

> Filmin planı: `dikey_shorts/THE_LONG_SHADOW/`. Aşağısı yalnız paketlemedir;
> plandaki bedel satırından türetilmiştir, uydurulmamıştır.

**Başlık (② kayıp kalıbı):**
```
Whose sunlight did it take?
```

**Açıklama:**
```
A narrow plot between two blocks, and one crane that everything had to pass through.

Eighteen storeys on a 24 by 18 metre footprint, zero clearance to the neighbour,
so every slab, every prop and every panel goes up on a single tower crane. Then
a winter arrives and the floor cycle stretches from five days to nine. Watch the
five-storey brick block on the right: in the first frame its face is in full
afternoon light.

14 months in 60 seconds.

──────────────────────────────────
Locked-off camera. No cuts inside a shot. No narration, no text on screen.
Every frame is generated with AI. This is not a record of a real project:
no real company, no real site, no real building is depicted.

Bu video yapay zekâ ile üretilmiştir. Gerçek bir projeyi belgelemez.
──────────────────────────────────

#timelapse #construction #architecture #civilengineering #buildingprocess
#aivideo #shorts #constructionsite #highrise #concrete #towercrane
```

**Sabit yorum:**
```
The reason a tight urban plot changes everything is logistics, not structure.
With no room for a lay-down area, material can't wait on the ground — it goes
from the truck to the hook to its final position, which means the crane, not
the concrete, sets the pace of the build. The floor cycle you're watching is a
formwork cycle: pour, cure, strike, climb. In summer that's about five days.
In cold weather concrete gains strength more slowly, so you either wait longer
before striking the formwork or you heat and protect the slab — and on a plot
this size, waiting is usually cheaper than heating. That's the winter you see
in the middle of the film: nothing goes wrong, everything just takes longer.
```

```
⛔ SPOILER DENETİMİ (MUZIK_VE_KAPAK §3.2 tek cümle testi):
   Başlık + kapak + ilk 2 sn + açıklama yan yana konunca yabancı biri filmi
   izlemeden dönüm noktasını söyleyebiliyor mu?
   → Açıklama gölgeyi İMA ediyor ("in the first frame its face is in full
     light") ama S9'da ne olduğunu söylemiyor. ✅ GEÇER.
```
