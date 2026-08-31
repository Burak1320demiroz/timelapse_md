# 📊 00_INDEX — PROJEDEKİ TEK SAYAÇ

> ⛔ Sayılar buraya ELLE yazılır ama `bash araclar/sayac.sh` ile
> KARŞILAŞTIRILIR. Betik uyuşmazlığı ekrana basar. Bir sayıyı iki yerde
> tutmak, birini yanlış tutmaktır.

---

## SAYIM

```
TOPLAM FİLM       3
ÖLÇÜLEN FİLM      3
TAM ÖLÇÜLEN       2     (6 merceğin 6'sı da koşulmuş)
ÜRETİLEN FİLM     3
```

## TAMLIK MATRİSİ

Bir film "tam ölçüldü" sayılmak için altı merceğin altısını da görmelidir.

| Film | ① KARE | ② İNŞA | ③ ZAMAN | ④ TESLİM | ⑤ DEVAM | ⑥ GEÇİŞ | Tam |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **THE NARROW LOT** | Ⓥ 6,0 | ⛔ belgesiz | **4,2** | ⛔ belgesiz | Ⓥ 5,6 | ⛔ belgesiz | **6/6** |
| THE LONG SHADOW v1 | Ⓥ 3,3 | Ⓥ 0,4 | Ⓥ 4,3 | Ⓥ 2,7 | ❌ | ❌ | **4/6** |
| THE CLOSING SPAN | 1,0 | Ⓥ 0,0 | 1,3 | Ⓥ 5,4 | Ⓥ 0,0 | Ⓥ 1,6 | **6/6** |

```
⚠️ THE LONG SHADOW v1'in ⑤ ve ⑥'sı KOŞULMADI çünkü o iki mercek film
   ölçüldükten SONRA açıldı. v1 arşivdir ve yeniden ölçülmeyecek — ama
   raporlarında ikisinin de malzemesi zaten var:
     ⑤'in konusu: "crane switches from grey flat-top to blue saddle jib"
                   (② kat.7) · "materials and vehicles morph" (① kat.8)
     ⑥'nın konusu: "cut 1 to cut 2 reverses time entirely" (③ kat.7)
   İki mercek de v1'de ayrı ayrı sorulsaydı bu bulgular DAHA ERKEN ve
   DAHA NET çıkardı. Açılma sebepleri budur.
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
✅  koşuldu, skor tabloda
Ⓥ   koşuldu ama mod V (ön koşu) — tamlık için sayılır, skor bağlayıcı değil
❌  koşulmadı
—   üretim yapılmadı, koşulamaz
```

## DURUM

```
THE NARROW LOT
   ızgara 5 × 6,0 · BES_SAHNE_GPT_BRIEFI'nin ilk koşusu · harici GPT
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
