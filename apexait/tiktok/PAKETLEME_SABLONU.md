# 📦 TIKTOK PAKETLEME ŞABLONU

> Paketleme KURALLARI `kilavuzlar/MUZIK_VE_KAPAK.md` §3'tedir. Burası
> TikTok için doldurulmuş hâlidir. Dil: İngilizce — bu bir kanal tercihi
> değil, depo kuralı (`KILAVUZ_REHBERI` §2.3).

---

# 1. ✍️ AÇIKLAMA — tek yüzey, çok az yer

```
TikTok'ta başlık YOK. Açıklama hem başlık, hem kanca, hem bağlam —
ve akışta yalnız İLK SATIRI görünür.

⛔ Bu, üç platform içinde EN SIKIŞIK yüzeydir. YouTube açıklamasını
   buraya kopyalama; kopyalanan uzun metin "daha fazla"nın arkasında
   kalır ve hiç okunmaz.
```

## 1.1 İskelet

```
<İLK SATIR — kanca. Tek cümle, bedeli ima eder, finali vermez.>
<İKİNCİ SATIR — tek teknik dayanak ya da zaman yayı.>
<hashtag satırı — §2>
AI-generated. Not a real project. / Yapay zekâ ile üretildi.
```

```
⛔ Son satır kısaltılmış hâliyle bile DURUR. TikTok'ta yer az ama
   KILAVUZ_REHBERI §9.8 pazarlık kabul etmiyor: beyan görünür olacak.
⛔ AIGC anahtarı bu satırın yerine geçmez (HESAP_KIMLIGI §4).
⛔ "Follow for part 2" yok — filmin ikinci parçası yok, film bitiyor.
   Olmayan bir devamı vaat etmek, ilk yorumda çöken tek şeydir.
```

---

# 2. #️⃣ HASHTAG — en az olan platform

```
3-4 TANE.

SABİT (2)      #timelapse #construction
YAPI ÖZEL (1-2)  #highrise · #bridge · #dam · #windfarm · #stadium …

⛔ #aivideo burada SABİT DEĞİL — çünkü AIGC etiketi ve açıklamadaki
   satır zaten söylüyor, ve TikTok'ta "AI" etiketli akış doygun
   (HESAP_KIMLIGI §7 ②). Etikette dürüstlük, hashtag'de rekabet var;
   ikisi aynı şey değil.
⛔ Hashtag bloğu, "fyp", "viral", "foryou" yok.
```

---

# 3. 🖼️ KAPAK

```
⛔ TikTok'un önerdiği kareyi KABUL ETME.
   Kapak, filmin son 5 saniyesindeki BAŞLIKLI KAPAK KARTINDAN seçilir
   (MUZIK_VE_KAPAK §2.1 · HESAP_KIMLIGI §3.1).

⛔ TikTok'un kapak editöründe METİN EKLEME. Başlık zaten karenin üstünde,
   post-prodüksiyonda dizilmiş hâlde. İkinci bir metin katmanı hem
   çakışır hem 120 px testini geçmez.
```

---

# 4. 📌 SABİT YORUM

```
YouTube'un sabit yorumunun aynısı: o yapının arkasındaki gerçek
mühendislik, tek paragraf, o filme özel.
⛔ TikTok'ta KISALTILIR ama şablonlaştırılmaz — kısaltma başka,
   kopyalama başkadır (youtube/POLITIKA_VE_RISK.md §1.3 ②).

⭐ Sabit yorum burada ikinci bir iş daha yapar: yorumları besler ve
   yorumlar bu hesabın film havuzu girdisidir (HESAP_KIMLIGI §8).
```

## 4.1 Sabit cevaplar

`youtube/PAKETLEME_SABLONU.md` §4.1'deki cevaplar aynen geçerlidir.
TikTok'a özel tek ek:

```
"AI slop" / "another AI channel"
   → Fair. The test is whether it holds: same camera, same building, same
     background in every shot, and the building only ever gains material.
     Watch the block on the right — it never moves.

⛔ Savunmaya geçme, tartışma. Cevap bir İDDİA değil, bir DAVETTİR:
   izleyiciyi kadrajı denetlemeye çağırır. Kanalın tek argümanı disiplindir.
```

---

# 5. ✅ YÜKLEME KONTROL LİSTESİ

```
□ 1  CAPRAZ_YAYIN §6 çapraz liste koşuldu mu (QA · master · filigran · C2PA)
□ 2  ⛔ Teslim süresi ffprobe ile ölçüldü mü — 1 dakikanın üstünde mi
      (HESAP_KIMLIGI §5)
□ 3  NATIVE yükleniyor mu — indirilmiş/filigranlı dosya DEĞİL
□ 4  Açıklama ilk satırı kanca mı (§1)
□ 5  Beyan satırı duruyor mu (§1.1)
□ 6  Hashtag 3-4 tane mi (§2)
□ 7  ⛔ AIGC anahtarı elle açıldı mı (HESAP_KIMLIGI §4)
□ 8  Kapak, başlıklı kart karesinden elle seçildi mi (§3)
□ 9  Paylaş → SABİT YORUM yaz ve sabitle (§4)
□ 10 Önceki video aynı siluet ailesinden mi (YAYIN_PLANI §3) → ise DUR
□ 11 Ölçüm satırı açıldı mı (YAYIN_PLANI §6.1) + yeniden izlenme oranı
```

---

# 6. 📝 DOLDURULMUŞ ÖRNEK — THE LONG SHADOW

```
Eighteen storeys went up. The block across the street lost its afternoon.
Zero clearance to the neighbour, so everything went up on one crane.

#timelapse #construction #highrise

AI-generated. Not a real project. / Yapay zekâ ile üretildi.
```

**Sabit yorum (kısaltılmış):**
```
On a plot this tight there's no lay-down area, so material goes truck → hook →
final position. That means the crane sets the pace, not the concrete. The cycle
you're watching is a formwork cycle: pour, cure, strike, climb — about five days
in summer. In cold weather concrete gains strength more slowly, so you either
heat and protect the slab or you wait. On a plot this size, waiting is usually
cheaper. That's the winter in the middle of the film: nothing goes wrong,
everything just takes longer.
```

```
⛔ SPOILER DENETİMİ (MUZIK_VE_KAPAK §3.3):
   Kapak başlığı + ilk satır + ilk 2 sn yan yana konunca yabancı biri
   dönüm noktasını söyleyebiliyor mu?
   → İlk satır bedeli SÖYLÜYOR. ⚠️ TikTok'ta bu bilinçli bir sapmadır:
     burada merak değil, ilk saniyede TUTMA satın alınıyor (HESAP_KIMLIGI §1).
     YouTube ve Instagram'da bedel saklı kalır; üç yüzey aynı olmak zorunda
     değil, aynı FİLMİ satmak zorunda.
```
