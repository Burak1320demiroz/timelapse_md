# 🗒️ THE DUST YEAR — ÜRETİM GÜNLÜĞÜ

```
DURUM  ⛔ FİLM ÜRETİLDİ, BU GÜNLÜK TUTULMADI.  ⭐ 08.09.2026

       Teslim: 11 klip · 1:07,2 · sekiz mercekle ölçüldü (ham raporlar
       QA/HAM_RAPORLAR/THE_DUST_YEAR_*_HAM.md).

       Aşağıdaki §0-§4'ün hiçbiri doldurulmadı. Yani araç kutu seti
       ölçülmedi, geriye zincir kurulmadı, yedi teslim ölçümü koşmadı.
       ⛔ BU DOSYA GERİYE DÖNÜK DOLDURULMAZ [şablon: "her satır ÜRETİRKEN
          yazılır, sonradan hatırlanarak değil"]. Boş kalır ve boş kalması
          ölçümün bir parçasıdır.

       ⭐ EKSİKLİĞİN ÖLÇÜLEBİLİR İZİ — QA raporlarından okunuyor:
         · ① VANTAGE GROUPS = 4  (A: 7 klip · B: klip 1 · C: klip 3 · D: klip 5)
           Plan TEK istasyon beyan etmişti [§2]. Dört grup = zincir yok.
         · teslim ızgarası 6·8·4·4·6·4·10·4·6·10 = 62,0 sn
           plan ızgarası    6·4·8·4·6·4·10·4·6· 8 = 60,0 sn
           S1↔S2 yer değiştirmiş · S9 8,0 → 10,0 uzamış.
           kesme_kontrol.sh koşsaydı 2. kesmeyi (beklenen 10,00 · bulunan
           14,00) toleransın 16 katı sapmayla düşürürdü.
         · ⑧ 0,0/10 · sekiz elemanın sekizi "first seen INCOMPLETE at NEVER"

       → Bu filmden çıkan dersler: kilavuzlar/DERSLER.md · DERS 35-44
         ⛔ Bu film DÜZELTİLMEZ. Dersler YENİ filmler içindir.
```

> ⛔ Üretirken doldur. Bu dosya yoksa `araclar/qa_paket.sh` durur [DERS 28]: günlüksüz
> filmde QA, "prompt tutmadı" ile "prompt kullanılmadı" ve "araç görmezden
> geldi"yi AYIRAMAZ. THE LONG DAY'de beş ders bu yüzden tek mekanizmaya inemedi.
>
> Kural: her satır ÜRETİRKEN yazılır, sonradan hatırlanarak değil.

---

## 0. ARAÇ KAPISI — plandan önce, TEK PROMPT · BEŞ KLİP [DERS 23 · 32 · A7-d]

> ⭐ 08.09.2026: üç soru YEDİYE çıktı. Yordam ve test promptu:
> `kilavuzlar/ARAC_KARTLARI.md` §4-§5. Kart doldurulmadan tek kare üretilmez.

```
ARAÇ            [ad + sürüm/mod]
ÖLÇÜM TARİHİ    [üretim günü — ⛔ araştırma raporundan alınmaz, A7-X2]
① KUTU SETİ     ffprobe: ____ / ____ / ____ sn   beş klip aynı mı: evet/hayır
   SAHNE TAVANI (en büyük kutu − 1,00) = ____ sn  → plandaki en uzun sahne: ____
② KAMERA        ilk/son kare kayması: ____ px    (>2 px ise ÜRETİLMEZ)
   GEOMETRİ KANALI [static mode · start/end frame · yok]
③ GÖLGE         ilk/son kare açı farkı: ____°    (0° ise ÜRETİLMEZ)
④ NEGATİF       metin içi: __/5 klipte sızdı · ayrı alan: __/5 · ayrı alan var mı: __
⑤ PROMPT TAVANI ____ karakter · promptun son nesnesi göründü mü: __/5
⑥ İLK KARE      zincir_kontrol.sh çıkışı: ____   (2 ise zincir bu araçta yürümez)
⑦ EN BÜYÜK KUTU isteniyor mu / geliyor mu: __
KARAR           bu araçla üretilir / üretilmez — sebep
```

## 1. USTA KARE

```
SAHNE   S9
ARAÇ    [görsel model + ayar]
PROMPT  birebir plandan / değiştirildi: [ne değişti, neden]
SEED    [varsa]
KAPI    çapalar okunuyor mu · taç %'si · güvenli alan · Dünya/yıldız yok mu → geçti/düştü
FİNAL HİYERARŞİ  [plandaki üç şey bu sırayla okunuyor mu — P1-h]
DOSYA   [kare dosya adı]
```

## 2. GERİYE ZİNCİR — klip başına TEK satır, sıra: S8 → S0

| S | araç + ayar | kaynak kare (dosya) | master'dan ne KALDIRILDI / EKLENDİ [P2-a] | prompt birebir mi (değilse ne) | zincir_kontrol | kanıt nesnesi elle | ⭐ ara hâl elle [A5-a] | dosya |
|:-:|---|---|---|---|:---:|:---:|:---:|---|
| 8 | | | | | geçti/düştü | ✓/✗ | ✓/✗ | |
| 7 | | | | | | | | |
| 6 | | | | | | | | |
| 5 | | | | | | | | |
| 4 | | | | | | | | |
| 3 | | | | | | | | |
| 2 | | | | | | | | |
| 1 | | | | | | | | |
| 0 | | | | | | | | |

```
⛔ zincir_kontrol "düştü" yazan satırın ALTINDAKİ satırlar boş kalır — o
   kare atılır, yeniden türetilir, satır yeniden yazılır. Düşen kareden
   türetilmiş bir alt kare bu tabloya giremez [DERS 12 · 25].
```

## 3. VİDEO — I2V, klip başına TEK satır

> ⭐ ÜRETİM SÜRESİ = TESLİM SÜRESİ + 1,00 sn [A7-b]. Kutu setinden ÜST kutuyu
> iste, kurguda kırp. REJİM sütunu boş bırakılamaz [A6-a].

| S | araç + ayar | rejim (A/B/C) | kaynak kare | hedef kare (sonraki onaylı) | prompt birebir mi | ffprobe süre | kırpma (baş/son, kare) | teslim süre | yüzey kanıtı ✓/✗ | dosya |
|:-:|---|:-:|---|---|---|---:|---|---:|:---:|---|
| 0 | | | | S1 ilk kare | | | | | | |
| 1 | | | | | | | | | | |
| 2 | | | | | | | | | | |
| 3 | | | | | | | | | | |
| 4 | | | | | | | | | | |
| 5 | | | | | | | | | | |
| 6 | | | | | | | | | | |
| 7 | | | | | | | | | | |
| 8 | | | | | | | | | | |
| 9 | | | | — (loop → S0) | | | | | | |

## 4. KURGU VE TESLİM — YEDİ ÖLÇÜM [KURGU_VE_TESLIM_KILAVUZU §6]

> ⛔ Yedisi de koşmadan yayın yok. Boş satır = koşulmamış sayılır.

```
① BİÇİM         ffprobe stream=width,height,r_frame_rate,codec_name → ____
                beklenen 1080,1920,30/1,h264 · tolerans SIFIR
② SÜRE          ffprobe format=duration → ____ sn   (sahne bloğu + kart 5,0)
③ KESME KANITI  bash araclar/kesme_kontrol.sh teslim.mp4 <plan>   → çıkış: __
                ⭐ betik top-N ile çalışır; AYIRIM marjı ____ kat çıktı
④ SES           ffmpeg -af ebur128=peak=true ... | grep -A8 Summary
                I: ____ LUFS (hedef −14 ±0,5) · Peak: ____ dBFS (≤ −1,0)
                müzik BPM ____
⑤ AÇILIŞ        müziksiz pencere 0,0-1,5 plana uygun mu: evet/hayır
⑥ FLICKER       signalstats,metadata=print:key=lavfi.signalstats.YDIF
                kesme dışında sıçrama var mı: evet/hayır
                ⛔ yalnız "-vf signalstats" HİÇBİR ŞEY BASMAZ [A8-b]
⑦ FİNAL + KAPAK ffmpeg -sseof -0.05 → son_kare.jpg
                SPEC §1'deki şeyler görünüyor mu: __
                KAPAK KAYNAĞI ffmpeg -ss ____ -i TESLİM.mp4 → s9_kaynak.jpg
                ⭐ kaynak TESLİM dosyasından alınır, üretilen klipten DEĞİL
                   (kırpma kareleri kaydırır) [KURGU_VE_TESLIM §2]
                KAPAK KANITI zincir_kontrol.sh s9_kaynak.jpg kapak.png → __
```

## 5. PLANDAN SAPMALAR — üretim sırasında değişen her şey

```
[tarih] [S] [ne değişti] [neden] [plana geri yazıldı mı]
```
