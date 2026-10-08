# 📋 THE CLOSING SPAN — QA KAYDI

```
KÜNYE      11 segment · 1:04,2 · sahne bloğu 10 klip 1:00,0 · kart 4,2 sn
           altı mercek koşuldu (6/6) — deponun ilk TAM ölçümü
KARAR      ⛔ YAYINLANMAZ.
```

---

## 1. ALTI HÜKÜM

| Mercek | Skor | HÜKÜM |
|---|---:|---|
| ① KARE | 1,0/10 | ⛔ **AYRI AYRI GÖRÜNTÜLER** |
| ② İNŞA | 0,0/10 Ⓥ | ⛔ **FARKLI** · ⛔ **APPEARING** |
| ③ ZAMAN | 1,3/10 | ⛔ **YANLIŞ YÖNDE GEÇİYOR** |
| ④ TESLİM | 5,4/10 Ⓥ | ⚠️ BİTİYOR — ama **NONE FOUND** |
| ⑤ DEVAMLILIK | 0,0/10 Ⓥ | ⛔ **HER ÇEKİMDE YENİDEN KURULMUŞ** · **NONE FOUND** |
| ⑥ GEÇİŞ | 1,6/10 Ⓥ | ⛔ **SIRADAKİ** · ⛔ **METRONOM** |

```
v1 ile karşılaştırma:  3,3 / 0,4 / 4,3 / 2,7   →   1,0 / 0,0 / 1,3 / 5,4
⛔ DÜRÜST KAYIT: v2 v1'den DAHA KÖTÜ ölçüldü. Plan iyileşti, teslim kötüleşti.
```

---

## 2. ⭐ TEK BÜYÜK KAZANIM — DERS 6 TUTTU

```
① CAMERA LOCK   v1: 4/10  →  v2: 10/10
   Rapor on klibin onunda da "MOVEMENT: none" yazdı.
   v1'de bütün klip boyunca push-in vardı.
DEĞİŞEN ŞEY: kamera kilidi yasak cümlesinden ("no zoom") POZİTİF VE
ÖLÇÜLEBİLİR çapaya çevrilmişti ("the buttress occupies exactly the same
width of the frame at both ends"). ⭐ Ölçülmüş bir düzelme.
```

---

## 3. KÖK SEBEP — aynı sebep, ikinci kez

**Ters inşa zinciri yine koşulmadı.**

```
KANIT      ① VANTAGE GROUPS = 8      (plan 2 diyordu: ANA + PİLON)
             A=1,3 · B=2 · C=4 · D=5 · E=6,7 · F=8 · G=9 · H=10
           ⑤ 9 dikişin 9'u da DEFECT
           ⑤ "THE OBJECT THAT PROVES IT IS THE SAME PLACE: NONE FOUND"
           ② "structural design, load paths and scale continuously change
              between every cut"

MEKANİZMA  Kamera her klibin İÇİNDE sabit (10/10) ama klipler ARASINDA
           istasyon her seferinde yeniden doğuyor. Yani kareler bağımsız
           üretildi — tıpkı v1'deki gibi.

⛔ VE BU SEFER KURAL YAZILIYDI. DERS 5 "ters inşa bir öneri değil KAPIDIR"
   diyordu ve KILAVUZ_REHBERI §8'e kapı olarak yazılmıştı.
   → Yazılı kural kapı değildir. Kapı KOŞULAN bir şeydir [DERS 12].
   → prompt_kontrol.py METNİ denetler; ÜRETİM SIRASINI denetleyemez.
     Eksik olan araç: ÜRETİM ARASI kapı.
```

---

## 4. ⭐ "HÂLÂ YAVAŞ" — ölçümün cevabı

Proje sahibinin okuması: *"bence hâlâ yavaş."* Halbuki kesme aralığı 10 sn'den
6 sn'ye indirilmişti. ⑥ merceği sebebi adlandırdı:

```
KESME ARALIKLARI  6,0 · 5,8 · 6,2 · 6,0 · 5,9 · 5,9 · 6,0 · 6,2 · 6,0
⑥ RHYTHM AND PATTERN            0/10
⑥ VERDICT                        METRONOM
⑥ THE CUT THAT CARRIES THE FILM  NONE

"cutting mechanically every ~6.0 seconds without variation, arcs, or
 response to the on-screen action, making every shot feel interchangeable"
```

⭐ **HIZ, KESME SIKLIĞI DEĞİL, KESME VARYANSIDIR.** Eşit aralıklı on kesme
tempo üretmez, nabız üretir; izleyici sürprizsiz bir diziyi yavaş algılar.
6 saniyeye inmek filmi hızlandırmadı çünkü değişen tek şey sabitin kendisiydi.
→ [DERS 13] ve aşama merdivenine RİTİM sütunu.

---

## 5. EN AĞIR BEŞ BULGU (kamera kilidi dışında)

```
⑤ 9/9      Her dikişte dünya yeniden kuruluyor: dağ silueti, yol güzergâhı,
           ağaçlar, istif alanı. "NONE FOUND" — aynı yeri kanıtlayan tek bir
           nesne bile yok.

③ 0:48,0   Mevsim GERİ gidiyor: kış (0:29,9) → yemyeşil yaz (0:48,0).
           ③ zaman tahmini: 34 ay yerine "yaklaşık bir yıl".

③ 0:24,0   ⭐ HIZ KARIŞIMI: "clouds race in time-lapse while the workers move
  0:35,8   at near real-time speeds" · "trucks move at normal video speed".
           Model GÖKYÜZÜNÜ hızlandırıyor, YERİ hızlandırmıyor [DERS 15].

③ 0:18,0   İki sahnede mevsim OKUNAMIYOR ("Indeterminate — bare rock").
  0:41,8   Kaya vadisinde S3/S4'te ne bitki ne kar vardı. Plan hatası:
           mevsim taşıyıcısı bu iki sahneye hiç konmamıştı [DERS 14].

① C4       Gece: "static pinpoint stars with no trails". Benim negatifim
           "no star trails" diyordu — o madde ŞEHİR kartından gelmişti.
           Dağ vadisinde izsiz yıldız SAHTEDİR [DERS 16].
```

---

## 6. ⚠️ ÜÇ MERCEK YANLIŞ MODDA KOŞULDU

```
② İNŞA    QA_SPEC verilmedi   → mod V
④ TESLİM  plan + kapak verilmedi → mod V
⑥ GEÇİŞ   plan + ses verilmedi   → mod V · MUSIC ALIGNMENT "NOT TRIGGERED"

SONUÇ: üçünün de skoru Ⓥ ön koşudur ve BAĞLAYICI DEĞİLDİR.
⭐ Bunun somut bedeli: ④ mod V'de FINAL BEAT'e PASS verdi — çünkü mod V'de
   o kategori "bir sonu var mı"ya dönüşüyor. Planın GERÇEK final vuruşu
   (0:57,5 · vadi karanlık, köprü aydınlık) HİÇ DENETLENMEDİ.
   Bulgular geçerli; sözleşme sorusu sorulmamış [DERS 17].
```

---

## 7. ①/③/⑤'İN "QUESTIONS FOR THE DOCUMENT" CEVAPLARI

```
①-1  HAYIR. Vantaj A'nın arka plan jeolojisi DEĞİŞMEZLER tablosunda kilitliydi
     (çentikli kaya burnu · üç çam · ikiz zirveli sırt). Değişmesi planlı değil.
①-2  ANA istasyon: 24 mm · tabliye kotunun +34 m üstü · yakın pilondan 120 m ·
     bakış 095° · tilt 0°. Sekiz sahnede de aynı olmalıydı.
①-3  İnsan ve araç BULANIK hareket izi olarak planlanmıştı; net figür yok.
①-4  HAYIR. Kadraj defteri çalışma seviyesini %31-45,6 bandına koyuyordu.
③-1  34 ay · Tem→Eyl→Eki→Kas→Ara→Şub→Nis→May→Haz→Ağu (tek yönlü).
③-2  Plan aralık vermedi — yalnız "everything moves at accelerated speed"
     yazmadı. Bu eksik [DERS 15].
③-3  EVET, on sahnenin onunda azimut ve yükseklik dereceyle yazılıydı.
⑤-1  HAYIR. Yol ve güzergâh DEĞİŞMEZ; eski yol filmin BEDELİNİ taşıyan çapaydı.
⑤-2  Hayır — istif alanı planda hiç yoktu.
⑤-3  S6 kar birikir, S7 kar ERİR ve çamura döner. Erime hiç üretilmedi.
```

---

## 8. KARAR

```
⛔ YAYINLANMAZ. Yeniden kurgu / renk / müzik BUNU KURTARMAZ.

v3 İÇİN ZORUNLU — ve bu sefer ARAÇLA bağlanıyor:
  ① ⭐ ZİNCİR KAPISI KURULUR — araclar/zincir_kontrol.sh. Her sahne
     üretildikten sonra, BİR SONRAKİNE GEÇMEDEN ÖNCE koşulur. Ufuk yüzdesi
     ve çapa genişliği bir öncekiyle tutmuyorsa üretim DURUR. [DERS 12]
  ② RİTİM SÜTUNU — sahne süreleri eşit olmaz; ölçüye oturan varyans. [DERS 13]
  ③ MEVSİM TAŞIYICISI SÜTUNU — boş bırakılamaz. [DERS 14]
  ④ TEK HIZ CÜMLESİ — bulut, gölge, makine, insan, araç AYNI hızda. [DERS 15]
  ⑤ NEGATİF ÇEKİRDEK SAHA KARTINA KARŞI OKUNUR — yıldız izi dağda meşru. [DERS 16]
  ⑥ MOD KAYDI — mercek yanlış modda koşulduysa skor tabloya yazılmaz. [DERS 17]
```

## 9. BU FİLMDEN ÇIKAN DERSLER

`kilavuzlar/DERSLER.md` → **DERS 11 · 12 · 13 · 14 · 15 · 16 · 17**
