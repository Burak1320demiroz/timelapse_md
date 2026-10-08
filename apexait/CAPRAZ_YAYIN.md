# 🔁 ÇAPRAZ YAYIN — bir film, üç hesap

> Üç platformda da aynı film yayınlanır. Bu dosya **üçünde de aynı olan
> işi** tutar: tek master, filigran yasağı, güvenli alan zarfı, metadata.
> Platforma özel olan her şey `youtube/`, `instagram/`, `tiktok/` altındadır.
>
> ⚠️ Bu dosya iki türetilmiş sayının KAYNAĞIDIR (§3.2 ızgara kırpması).
> Başka yerde tekrarlanmaz.

---

# 1. 🎞️ TEK MASTER — ⛔ üç ayrı kurgu yok

```
Kurgudan ÇIKAN tek dosya:
   apexait_<FILM>_master_1080x1920.mp4
   · filigran YOK · platform logosu YOK · gömülü altyazı YOK
   · gömülü başlık/kapak kartı YOK (negatif çekirdek zaten yasaklıyor)
   · ihraç ayarları: KILAVUZ_REHBERI §8 adım 4

Bu dosya ÜÇ PLATFORMA DA AYNEN yüklenir.
```

## 1.1 ⛔ FİLİGRANLI YENİDEN YÜKLEME YASAK

```
⛔ TikTok'tan indirilen (TikTok filigranlı) videoyu Reels'e YÜKLEME.
⛔ Reels'ten indirilen videoyu TikTok'a YÜKLEME.
⛔ Hiçbir platformun "diğerine paylaş" düğmesini kullanma.

SEBEP: her platform rakibinin filigranını taşıyan içeriği geri plana atar
ve bu, kalitesi ne olursa olsun filmi öldürür. Üç yükleme de master
dosyadan, NATIVE (uygulamanın kendi yükleyicisiyle) yapılır.

⭐ Bu bir "algoritma söylentisi" değil, tek yönlü bir bahis: filigranı
   kaldırmanın maliyeti sıfır, filigranlı yüklemenin maliyeti belirsiz
   ama tek yönlü. Bedava olan tarafta dur.

⭐ 07.10.2026 — artık resmî dayanağı var [A31-d]:
   Instagram 31.05.2023: "low-resolution or watermarked reels … or reels that have
   already been posted on Instagram" daha az görünür · 30.04.2024: özgün içerik
   önerilerde yeniden paylaşımın yerini alır, toplayıcı hesaplar öneriden çıkar ·
   30.04.2026: filigran eklemek ya da HIZ değiştirmek özgünlük sayılmaz.
   TikTok: "We also don't recommend duplicated content" · yeniden kullanılmış içerik
   For You'ya girmez. ⇒ Tek master + native yükleme doğru; aynı filmi bir platformda
   İKİ KEZ yükleme (silip yeniden yüklemek dahil) yasağın parçasıdır.
```

---

# 2. 🧬 METADATA VE C2PA — ⛔ temizleme

```
Üretim araçlarının çoğu dosyaya C2PA / IPTC "Content Credentials" gömer.
TikTok ve Meta bu imzayı OKUR ve içeriği kendiliğinden "AI" etiketler.

⛔ BU METADATA SİLİNMEZ. Silmek iki sebeple yanlış:
   ① Kanalın tezi zaten açık (KANAL_KIMLIGI §1): saklayacak bir şey yok.
      Adında "AI" yazan bir hesabın metadata temizlemesi tutarsızlıktır.
   ② TikTok'ta otomatik uygulanan etiket ÜRETİCİ TARAFINDAN KALDIRILAMAZ.
      Yani kaçmayı denemenin sonucu, kontrolü kaybetmiş olmaktır.

⭐ DOĞRU HAMLE: her platformda ÖNCE KENDİN beyan et.
   Kendi beyanın senin cümlendir; otomatik etiket platformun cümlesidir.
   İkisi de olacaksa, önce seninki olsun.

⭐ 07.10.2026 — üç platformda da otomatik etiket RESMÎ [A31 · A32]:
   TikTok   09.05.2024'ten beri Content Credentials okur · "you won't be able to remove the label"
   YouTube  C2PA'lı içeriğe etiketi kendisi koyar, "can not be adjusted" · 27.05.2026'dan beri
            Shorts'ta overlay · etiket öneriyi ve parayı etkilemez (POLITIKA_VE_RISK §2)
   Meta     "AI info" (01.07.2024'ten beri bu ad) · C2PA/IPTC okur
   ⚠️ C2PA ile görünmez filigranı birlikte doğrulayan yaygın bir iş akışı henüz yok (arXiv 2603.02378) —
      etiketin her yüzeyde gelmesi garanti değil; kendi beyanın bu yüzden de gerekir.
   ⚠️ TikTok 11/2025'ten beri izleyiciye yapay zekâ içeriğini AZALTMA kaydırıcısı veriyor: ceza değil,
      izleyici tercihi. Bizim filmin o izleyiciye gitmemesi beklenir ve ölçülemez.
   → youtube/POLITIKA_VE_RISK.md §2 · instagram/HESAP_KIMLIGI.md §4
     · tiktok/HESAP_KIMLIGI.md §4
```

---

# 3. 📐 GÜVENLİ ALAN — ⭐ iyi haber

## 3.1 Zarf: YouTube Shorts üçünü de kapsıyor

Üç platform da 1080×1920 alır ama arayüzleri farklı yerleri kapatır.
`KILAVUZ_REHBERI` §2'deki GÜVENLİ ALAN tablosu **YouTube Shorts'a göre**
yazılmıştı. Üç platformun kenar kenar karşılaştırması:

| Kenar | YouTube Shorts | Instagram Reels | TikTok | ⭐ En dar olan |
|---|---|---|---|---|
| ÜST | §2'deki değer | daha küçük | daha küçük | **YouTube** |
| ALT | §2'deki değer | daha küçük | daha küçük | **YouTube** |
| SAĞ | §2'deki değer | daha küçük | daha küçük | **YouTube** |
| SOL | §2'deki değer | daha küçük | daha küçük | **YouTube** |

```
⭐ SONUÇ: YouTube Shorts güvenli alanı diğer ikisini ZARFLIYOR.
   Yani KILAVUZ_REHBERI §2'ye göre yazılmış bir COMPOSITION satırı
   Reels'te ve TikTok'ta da güvenlidir.

⛔ PROMPTLARDA HİÇBİR DEĞİŞİKLİK GEREKMİYOR. Üç platform için üç ayrı
   kadraj hesabı YAPILMAZ — zaten yapılmış olanın içindeler.
⚠️ Bu tablo ikincil kaynaklardan kuruldu, ölçülmedi. Ölçüm §3.3'te.
```

## 3.2 ⛔ TEK İSTİSNA — Instagram profil ızgarası 4:5 kırpar

Instagram'ın profil ızgarası dikey videoyu **4:5'e ortalayarak kırpar.**
Bu, videonun kendisini değil, **ızgarada görünen kapağı** etkiler — ve
`KANAL_KIMLIGI` §5.4'e göre ızgara kanalın asıl görüntüsüdür.

```
HESAP (bu dosya bu iki sayının kaynağıdır):
   1080 genişlikte 4:5  →  1080 × 1350
   kesilen yükseklik    →  1920 − 1350 = 570
   üstten ve alttan     →  570 / 2 = 285 px

   IZGARADA GÖRÜNEN BANT:  y = 285 … 1635

ÇARPIŞMA:
   KILAVUZ_REHBERI §2.3 yapının TACINI üst şeridin hemen ALTINA koyuyor.
   O taç 285'in ÜSTÜNDE kalırsa videoda görünür ama IZGARADA KESİLİR.
   Aşama kanıtı tarafında sorun yok: §2.3'ün alt sınırı 1635'in üstünde.

⭐ KAPAK BAŞLIĞI GÜVENDE: MUZIK_VE_KAPAK §2.3 başlık metnini y=500-1400
   bandına koyuyor, ızgaranın gördüğü bant y=285-1635. Yani 4:5 kırpması
   başlığa DOKUNMUYOR. Kesilme riski yalnız yapının tacındadır.

⛔ INSTAGRAM KAPAK KURALI: kapak karesi seçilirken yapının TACI
   y = 320'nin altında olmalı (285 + güvenlik payı).
   Bu, VİDEOYU değil yalnız KAPAK KARESİ SEÇİMİNİ bağlar.
   → instagram/HESAP_KIMLIGI.md §3
```

## 3.3 ⭐ ÖLÇÜM — söylentiyle değil, kaplamayla

Depo kuralı: sayı seçilmez, ölçülür (`KILAVUZ_REHBERI` §2 klip süresi
maddesinin aynısı). §3.1 tablosu ilk filmden sonra ölçülerek doğrulanır:

```
1. İlk filmi üç platforma da yükle.
2. Her platformda kendi telefonundan ekran görüntüsü al.
3. Üç görüntüyü 1080×1920'ye ölçekle ve üst üste koy.
4. Arayüzün kapattığı en geniş dikdörtgeni işaretle.
5. Sonuç §3.1 tablosundan DARSA → o platform artık zarfın kendisidir,
   tablo güncellenir ve KILAVUZ_REHBERI §2'ye tek satır ders olarak iner
   (AGENTS.md görev kartı D).
6. Sonuç aynıysa tabloya "ölçüldü · <tarih>" yazılır ve ⚠️ kalkar.
```

---

# 4. 🕐 YÜKLEME SIRASI VE ZAMANI

```
AYNI GÜN, ÜÇÜ BİRDEN, NATIVE.

SIRA (aralarında birkaç saat):
   1. YouTube Shorts    — arama kalıcılığı en uzun olan platform; arşiv orada
   2. TikTok            — ilk 24 saat dağıtımı en sert olan platform
   3. Instagram Reels   — kapak seçimi elle yapılır (§3.2), en son

⛔ Platformlar arası link/CTA koyma ("TikTok'ta da varım"). Her platform
   kendi içinde tutmak ister; dışarı gönderen içeriği geri plana atar.
   Handle zaten üçünde de aynı (@apexait) — arayan bulur.
⚠️ Bu sıra bir varsayımdır, ölçülmedi. Üç film sonra YAYIN_PLANI §6.2'ye
   göre sınanır: aynı film üç platformda hangi sırayla daha iyi açıldı?
⚠️ Aynı gün üç yüklemenin "özgün olmayan" sinyali verdiğine dair resmî bir cümle YOK; resmî
   kurallar FİLİGRAN, YENİDEN PAYLAŞIM ve KOPYA üzerinedir (§1.1) [A31 denetimi].
```

## 4.1 ⭐ Platform araçları — 0 aboneli hesapta ne var, ne yok (okundu 07.10.2026)

| araç | şart | bizde açılışta | kaynak |
|---|---|---|---|
| YouTube Shorts → ilgili video | advanced feature access · bağlanan video kendi kanalımız | ⬜ kanal doğrulaması gerekir (YAYIN_PLANI §4) | 14075157 ✅ |
| YouTube A/B testi (başlık + küçük resim) | yalnız UZUN FORM · masaüstü · advanced features · "not available for Shorts" | yatay filmde ✅ · dikeyde YOK | 16391400 ✅ |
| Instagram Trial Reels | herkese açık hesap · profesyonelde ≥ 200 takipçi · "Share to everyone automatically" ayarı | ⛔ 200 takipçiye kadar yok | Instagram Help ✅ |
| TikTok bio linki | ≥ 1.000 takipçi ya da doğrulanmış işletme hesabı | ⛔ — zaten §4 platformlar arası link yok | TikTok Support ✅ |
| TikTok A/B testi (organik) | resmî araç bulunmadı | YOK | BİLİNMİYOR |
| Instagram hashtag | gönderi başına ≤ 5 (18.12.2025) | şablon 3–5 ✅ | Social Media Today ✅ |

```
⛔ Dikey filmde hiçbir platformda yerleşik A/B testi YOK [A17-c doğrulandı]. Kapak ve başlık
   kararları dikeyde ölçülerek değil, KURAL ile verilir (MUZIK_VE_KAPAK §4 · sahip 19.09.2026).
```

---

# 5. 🧩 NE ORTAK, NE PLATFORMA ÖZEL

| Katman | Ortak mı | Nerede yaşıyor |
|---|---|---|
| Film (master mp4) | ✅ üçünde aynı | `dikey_shorts/<FİLM>/` |
| Tez · bedel · film havuzu | ✅ üçünde aynı | `KANAL_KIMLIGI` · `YAYIN_PLANI` |
| Logo · palet | ✅ üçünde aynı | `KANAL_KIMLIGI` §5.1-5.2 |
| Handle (@apexait) | ✅ üçünde aynı | `KANAL_KIMLIGI` §7.2 |
| Kadans · siluet sırası | ✅ üçünde aynı | `YAYIN_PLANI` §1, §3 |
| Banner / kanal sanatı | ⛔ yalnız YouTube | `KANAL_KIMLIGI` §5.3 |
| Biyografi metni | ⛔ platforma özel | her klasörün `HESAP_KIMLIGI` §2 |
| Başlık / caption / hashtag | ⛔ platforma özel | her klasörün `PAKETLEME_SABLONU` |
| AI beyanı yeri ve adı | ⛔ platforma özel | her klasörün `HESAP_KIMLIGI` §4 |
| Para kazanma eşiği | ⛔ platforma özel | her klasörün `HESAP_KIMLIGI` §5 |
| Kapak karesi seçimi | ⚠️ IG'de farklı | §3.2 |

```
⛔ Bir satır "ortak" sütununda ✅ ise platform klasörüne KOPYALANMAZ.
   Kopyalandığı gün üç kimlik ayrışır ve hangisinin doğru olduğu kaybolur.
```

---

# 6. ✅ ÇAPRAZ YAYIN KONTROL LİSTESİ

```
□ 0  ⛔ QA DÖRT MERCEK koşuldu mu (QA/00_README) — yayından ÖNCE
□ 1  Master dosya filigransız, logosuz mu (başlıklı kapak kartı hariç —
     o filmin parçası, sonraki 5 saniye)
□ 2  C2PA/metadata SİLİNMEDİ mi (§2)
□ 3  Üç platformda da AI beyanı kendi elinle işaretlendi mi
□ 4  Instagram kapak karesi: taç y=320'nin altında mı (§3.2)
□ 5  Üç yükleme de native mi — hiçbiri "diğerine paylaş" ile yapılmadı mı
□ 6  Aynı gün mü yayınlandı
□ 7  Üçünde de caption/açıklama o platformun şablonundan mı yazıldı
□ 8  Platformlar arası link/CTA yok mu
□ 9  ⛔ Metinde etkileşim çağrısı yok mu — "send this to…", "tag a friend", "comment …",
     "find the mistake" (Meta 2017 engagement bait · TikTok FYF "Tricking others into
     increasing engagement") [A33-b]
□ 10 Bu film bu platformda daha önce yüklenmedi mi (silip yeniden yükleme dahil — §1.1)
```
