# 🃏 SAHNE PLAN KARTI — BEŞ SORU, prompttan ÖNCE

> **Bu kart promptun kendisi değildir.** Prompt yazılmadan önce, klip başına
> beş sorunun cevabı yazılır. Cevabı olmayan sahnenin promptu yazılmaz — çünkü
> cevabı olmayan sahne modelde de yoktur; model boşluğu "sihirle" doldurur.
>
> Kaynak: 15 filmin 132 raporunun çapraz analizi (`QA/QA_CAPRAZ_ANALIZ/`,
> 18.09.2026) ve dış değerlendirme. Depoda ÖLÇÜLMEDİ; `DERSLER.md` ÇAPRAZ ANALİZ
> bölümünde **VARSAYIM** olarak durur [C1-a]. İlk pilot üretimden sonra ya
> derse döner ya düşer.
>
> Neden doğdu: ② İNŞA merceğinde 15 filmin 9'u, ⑩ SEBEP'te 5 filmin 4'ü 4,0
> altında (sayılar: `python3 araclar/capraz_sayim.py`). En ağır üç arıza (F01
> nedensiz montaj · F05 sıvı büyüme · F08 bağsız yük) aynı sorunun üç yüzü:
> **malzemenin nereden geldiği, kimin taşıdığı ve nereye oturduğu planda yazılı
> değildi.** OVER_THE_WALL en öğretici örnek — ⑪ ENVANTER 9,3 (ekipman sahada),
> ⑧ YÖNTEM 0,0 (yapıyı o ekipman yapmadı). Araç eklemek işi göstermiyor.

---

# 1. 🃏 BEŞ SORU

```
① MALZEME BAŞLANGIÇTA NEREDE?          → kaynak görselde (G(n)) GÖRÜNÜR olmalı:
                                           istif · pad · kamyon kasası · vinç kancası
② ONU HANGİ ARAÇ VEYA KİŞİ HAREKET      → TEK ana iş, TEK taşıyıcı; taşıyıcının
   ETTİRİYOR?                              yükle bağı görünür (kablo · sapan · çatal)
③ NEREYE TEMAS EDİYOR / OTURUYOR?       → destek noktası KADRAJ ÖLÇEĞİNDE okunur
                                           (≥ okunabilirlik eşiği · INSAAT_YONTEMI §1)
④ KLİP BİTTİĞİNDE NE DEĞİŞMİŞ OLUYOR?   → hedef görselde (G(n+1)) görünür fark;
                                           bir öncekinden FARKLI bir sonuç
⑤ SABİT KALACAKLAR NELER?               → kamera · üç çapa · çevre geometrisi ·
                                           daha önce yapılmış her şey
```

Her sorunun üç yüzü vardır ve üçü de ayrı denetlenir — birinci aşama (plan)
geçmek ikinciyi (görüntü) geçmiş saymaz:

| soru | kaynak görselde | promptta hangi blok | çıktıda kanıt |
|---|---|---|---|
| ① nerede | G(n)'de istif/yük görünür | görsel `AT THIS STAGE` + I2V `MOTION FOCUS` "from …" | klibin ilk saniyesinde malzeme o yerde |
| ② taşıyıcı | taşıyıcı G(n)'de yükün yanında/üstünde | görsel `ACTIVITY` (DERS 43 fiil + NESNE) + `PHYSICS` (asılı → taşıyıcı) | yük taşıyıcıyla birlikte hareket eder, tek başına süzülmez |
| ③ oturma | hedef yüzey G(n)'de boş ve görünür | I2V `MOTION FOCUS` "onto/into …" + `PHYSICS` temas cümlesi | oturma anı kadrajda; parça boyunu korur |
| ④ fark | G(n+1) ≠ G(n) — tek elemanla | I2V son kare kilidi ("ends exactly on the second provided image") | ⑧ YÖNTEM "yapımı görünerek" · ⑦ İŞ büyüme sebepli |
| ⑤ sabit | üç çapa G(n) ve G(n+1)'de aynı px'te | I2V "DEĞİŞMEYECEKLER" paragrafı | `zincir_kontrol.sh` + 3 nirengi (KAMERA_ISTASYONU §7) |

---

# 2. 📋 KART NEREDE DOLAR

```
YATAY (16:9)   00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md — BEŞ SORU sütunu.
               ② → "İKİ HAREKET EDEN" sütunu · ③ → "KALDIRMA / FİZİK" · ⑤ → "KANIT
               NESNESİ · ÇAPALAR" zaten var; BEŞ SORU sütununa ① ve ④ yazılır
               ("istiften · yol %40→%60" gibi) ve beşi tamsa ✅.
               Satırın KAPI'sı ✅ olmadan prompt yazılmaz — tablo zaten bunu ister.

DİKEY (9:16)   plan dosyasının KARE TABLOSU'na ① ve ④ tek hücrede; üretim günlüğü
               §3 klip satırında "beş soru ✓" hücresi.
```

⛔ **Beş sorusu cevaplı olmayan sahnenin promptu yazılmaz.**
KALDIRDIĞI: "sahne bu aşamada şöyle görünür" diye yalnız SONUCU tarif edip
süreci modele bırakma imkânı. Karşılığı, ⑧ YÖNTEM'in "THE FIRST PIECE THAT
APPEARED" satırının NONE dönmesidir — 15 filmin 3'ünde ⑧ sıfırdı.

---

# 3. 🚫 RED SEBEPLERİ — kart geçmez

| durum | neden red | ne yapılır |
|---|---|---|
| bir cevap "—" | model boşluğu doldurur; F01 tam olarak budur | sahne ya bölünür ya sıralamadan çıkar |
| ② iki ana iş (temel + kolon + çatı aynı klipte) | tek klipte tek montaj okunur; ikincisi sıvı büyümeye döner (F05) | iki sahneye böl; ızgara sahne SAYISI ile oynar, süreyle değil |
| ③ temas noktası okunabilirlik eşiğinin altında | cıvata · harç · kaynak dikişi kadraja inmez; prompta yazmak token yer (INSAAT_YONTEMI §1 · `prompt_kontrol.py` KÜÇÜK NESNE kapısı) | temas cümlesi ELEMAN ölçeğinde yazılır: "segment seats on the flange" |
| ④ = G(n) ile aynı | klip bilgi taşımıyor; ritim değil tekrar (F03'ün gerçek sebebi) | eleman yüzdesi bir öncekinden farklı olsun |
| ④ ile ⑤ çelişiyor (değişen şey sabit listesinde) | zincir kırılır; ⑤ DEVAMLILIK "A SET REBUILT" | ⑤'ten çıkar ya da ④'ü değiştir |
| ② taşıyıcı G(n)'de yok | yük "havada belirir" (F08) | taşıyıcı bir önceki kareye girer ya da klip ikiye bölünür |

---

# 4. 🎥 KARTTAN PROMPTA — MOTION FOCUS

Kartın ①②③④ cevabı I2V'nin `MOTION FOCUS:` paragrafına iner (PROMPT_SABLONU §2):

```
MOTION FOCUS: The crawler crane lifts the second tower segment from the
stacked pile on the north pad and seats it onto the flange of the first
segment; by the last frame the segment stands bolted and the sling hangs
empty.
```

Kurallar:
- **Tek cümle dizisi, tek nesne, "from … onto/into …"** kalıbı. Kapı bu kalıbı
  arar (`prompt_kontrol.py` §10e).
- Üç ve daha fazla yapı elemanı adı geçiyorsa kapı "birden fazla ana iş" der.
- `column grid` · `bay spacing` · `footprint` bu paragrafa girmez — kapı bunları
  "yapıyı yeniden tarif" sayar (`prompt_kontrol.py` I2V kuralı). Yapı görsel
  prompttadır; I2V yalnız HAREKETİ yazar [P2-d].
- ⑤ ayrı paragraftır (DEĞİŞMEYECEKLER) — MOTION FOCUS'a karışmaz.

---

# 5. ⚠️ KARTIN SINIRI

- Kart PLANLAMA kontrolüdür. Beş cevabın yazılması görüntüde doğru eylemin
  oluştuğunu garanti etmez; ikinci aşama (klip başı-orta-son elle bakış +
  `zincir_kontrol.sh`) ayrı koşulur → `QA/00_README.md` ÜÇ AŞAMA.
- Kart pilot filmde ölçülmedi. ② İNŞA ve ⑩ SEBEP'te ilk ölçüm gelene kadar
  buradaki her kural VARSAYIMDIR — kapıdaki karşılığı bu yüzden FIX, BLOCK değil.
