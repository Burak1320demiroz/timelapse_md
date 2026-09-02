# 🔍 THE MOUNTAIN DOOR — QA SPEC

> ⛔ **BU SPEC ÜRETİMDEN ÖNCE YAZILDI.** Buradaki her kilit, plandaki beş
> görsel ve beş I2V promptunun içinde İngilizce olarak YAZILIDIR. Hiçbir
> satır uydurulmadı; ölçülmemiş olanlar §7'de açıkça AÇIK olarak durur.
>
> Sebebi süreçtir [DERS 17]: NARROW LOT'ta SPEC hiç üretilmedi, `② İNŞA`,
> `④ TESLİM` ve `⑥ GEÇİŞ` belgesiz koştu ve skorları tabloya yazılamadı.
> Bu dosya o üç merceğin BELGESİDİR ve üretimden önce hazırdır.

---

## 0. KÜNYE

```
FİLM          THE MOUNTAIN DOOR — Dağın Kapısı
FORMAT        9:16 dikey · 5 sahne × 6,0 sn = 30,0 sn (hedef)
KAPAK KARTI   5,0 sn · SAHNE DEĞİL · S4'ün usta karesinden türer
TOPLAM        35,0 sn
YAPI          dağ yol tüneli · 620 m tek tüp · portal + kanopi + yaklaşım
SAHA          dağ/eğim (§3.4) + kar/kış şantiyesi (§3.5)
ZAMAN YAYI    12 ay · Temmuz → Temmuz
KAMERA        tek istasyon — ANA (5 sahnenin 5'i) · detay istasyonu YOK
ÜRETİM SIRASI ⛔ TERS: S4 usta kare → S3 → S2 → S1 → S0
              her kareden sonra zincir_kontrol.sh
KAYNAK        depo içi · kilavuzlar/TIMELAPSE_SISTEM_PROMPTU.md
KAPI          python3 araclar/prompt_kontrol.py → ✅ GO (üretimden ÖNCE)
⛔ KLİP SÜRESİ ffprobe ile HENÜZ ÖLÇÜLMEDİ [D-d]. 6,0 hedeftir, ölçüm değil.
```

---

## 1. ⛔ FİNAL VURUŞ KANITI — teslimin tek kapısı

```
SAHNE       S4
SANİYE      0:29,4
GÖRÜLMESİ GEREKEN ŞEY — dört şeyin DÖRDÜ birden:
   ① Tamamlanmış portal: 21,0 m başlık duvarı + üstünde 6,0 m kanopi;
      ağızda hiçbir geçici ekipman YOK (jumbo, kalıp, kanal, konteyner, çit).
   ② Yol kadrajın SOL ALTINDAN kesintisiz girip aydınlatılmış tüpe giriyor
      ve 62 lambalık TEK SIRA kayaya doğru küçülerek çekiliyor.
   ③ ⭐ BEDEL ①: portalın altındaki AÇIK RENKLİ PASA SEKİSİ duruyor —
      düzeltilmiş ama kaldırılmamış.
   ④ ⭐ BEDEL ②: kaya yüzündeki eski geçit yolunun İKİ VİRAJI da BOŞ ve
      alt virajın ağzını açık renkli bir kum bariyeri kapatıyor.

KOMUT
   ffmpeg -ss 29.4 -i teslim.mp4 -frames:v 1 kanit.jpg

⛔ Dördünden biri o karede görünmüyorsa FİLM TESLİM EDİLMEMİŞTİR — klip
   sayısı ve süre tutsa bile [D-e].
⭐ ④ merceğinin "THE ONE THING THIS FILM DOES" satırının cevabı ③ ve ④'tür.
   Üç filmde de bu satır NONE FOUND geldi; sebebi BEDELİN YAZILMAMASIYDI.
```

---

## 2. KADRAJ KİLİTLERİ — ANA istasyon (5 sahnenin 5'i)

Formül (`KAMERA_ISTASYONU §3`): `kare yüzdesi = %50 + f × (y − h) / (36 × D)`
Bu filmde `f = 24`, `h = 16,0`, `D = 48` → **kare yüzdesi = %50 + (y − 16,0) / 0,72**
Tolerans **± %2**.

| Ne | y (m) | Beklenen | Hangi sahnelerde |
|---|---:|---:|---|
| ufuk çizgisi | 16,0 | **%50,0** | 5 sahnede de |
| yol platformu / kaya yüzü tabanı | 0 | %27,8 | 5 sahnede de |
| istinat duvarı harpuştası | 5,2 | %35,0 | S3 · S4 |
| portal kemer tacı = kaya burnu ALT yarığı | 9,0 | %40,3 | S1 · S2 · S3 · S4 |
| başlık duvarı üst kenarı | 12,5 | %45,1 | S2 · S3 · S4 |
| kaya burnu ÜST yarığı | 20,0 | %55,6 | 5 sahnede de |
| eski geçit yolu ALT virajı | 30,0 | %69,4 | 5 sahnede de |
| eski geçit yolu ÜST virajı | 37,0 | %79,2 | 5 sahnede de |
| kaya yüzü tacı | 40,0 | %83,3 | 5 sahnede de |

```
⛔ ÜST SINIR: hiçbir yapı parçası %87,5'in üstünde olamaz (üst 1/8 = arayüz).
              Kaya yüzü tacı %83,3 ile sınırın altındadır.
⛔ ALT SINIR: ilerlemeyi kanıtlayan hiçbir şey %25'in altında olamaz.
              Yol platformu %27,8 — bant DAR, denetlenecek.
⛔ SAĞ ŞERİT: kanıt nesnesi kare genişliğinin sağ %12,5'inde duramaz.
              Kaya burnu sağdadır ama o bir ÇAPADIR, kanıt değildir.

⚠️ NARROW LOT'ta ① SAFE AREA 4/10 geldi ve iki bulgunun ikisi de alt %25'teydi.
   Sebep: COMPOSITION bloğu promptlarda HİÇ YOKTU (0/5) [DERS 20].
   Bu filmde COMPOSITION bloğu beş promptun BEŞİNDE de birebir vardır.
```

---

## 3. DEĞİŞMEZLİK KİLİTLERİ — sahneler arası

```
① KAMERA        5 sahnenin 5'inde de kamera hareketi = 0 kare.
                Pan/tilt/zoom/kayma/sarsıntı: 1 karede bile yok.

② ANA İSTASYON  5 sahnede de: lens 24 mm · yükseklik 16,0 m · mesafe 48 m ·
                bakış 315° · tilt 0° · roll 0°. Beşi BİREBİR aynı cümle.

③ ÇAPA ① SAĞDA  Kaya burnu: TAM İKİ düşey yarık.
                alt yarık ağzı 9,0 m · üst yarık ağzı 20,0 m.
                ⛔ Yarık sayısı ya da kotu değişirse BLOCK.

④ ÇAPA ② ÜSTTE  Eski geçit yolu: kadrajda TAM İKİ viraj.
                alt viraj 30,0 m · üst viraj 37,0 m · kuru taş korkuluk.
                ⛔ Viraj sayısı değişirse BLOCK.
                ⚠️ Yolun ÜSTÜNDEKİ trafik değişir (S0'da leke, S4'te YOK) —
                   yolun KENDİSİ değişmez. Bu ayrım ⑤'te denetlenir.

⑤ ÇAPA ③ SOLDA  Üstü düz granit kaya · 2,4 m · yol platformunun sol kenarı.
                ⭐ ⑤ merceğinin "aynı yer" KANIT NESNESİ budur.
                ⛔ Beş sahnenin beşinde de aynı yerde ve aynı boyutta.
                   S2'de üstü karla kaplıdır ama YERİ ve BOYU aynıdır.

⑥ ÇAPA ④ ALTTA  Tek kemerli taş köprü (TEK ayak) + örgülü dere.
                Korkuluğu S3'ün kanıt kotudur.

⑦ ÇAPA ⑤ ARKADA Uzak sırt: geniş boyun + sağında TAM BİR kaya boynuzu.
                ⚠️ Boynuzun KARI mevsimle değişir (taşıyıcıdır), SİLUETİ değişmez.

⑧ UFUK          %50,0 · sapma ± %2 · 5 sahnede de.

⑨ YAPI GEOMETRİSİ  tüp 12,4 × 9,0 m · başlık duvarı 21,0 × 12,5 m ·
                kanopi 6,0 m · platform 9,4 m · istinat duvarı 5,2 m ·
                14 panel × 15,0 m · 62 lamba × 10,0 m.
                ⛔ Bu dokuz sayı beş promptun beşinde de BİREBİR yazılıdır.
                   NARROW LOT'ta ② STRUCTURE IDENTITY 2/10'un tek sebebi
                   oturum ve aks sayılarının HİÇ YAZILMAMASIYDI [DERS 19].

⑩ VİNÇ          ⛔ BU FİLMDE VİNÇ YOKTUR. DERS 8 ve DERS 22 aynı arızayı iki
                filmde ölçtü (halat gökyüzüne karşı kopuyor). Arıza yüzeyi
                yasakla değil TASARIMLA kaldırıldı.
                ⛔ Herhangi bir karede kule vinci görünürse o kare ATILIR.
```

---

## 4. GÜNEŞ SAATİ KİLİDİ

| S | Mevsim / an | Başlangıç azimut · yükseklik | Bitiş azimut · yükseklik | Gölge |
|:-:|---|---|---|---|
| 0 | yaz · Temmuz kuşluk | 96° · 30° | 262° · 26° | batı → doğu, soldan sağa |
| 1 | sonbahar · Ekim kuşluk | 136° · 24° | 224° · 18° | kuzeybatı, uzayarak |
| 2 | kış ① · Ocak geç kuşluk | 144° · 14° | 216° · 12° | çok uzun, mavi |
| 3 | kış ② · Mart kuşluk | 132° · 26° | 232° · 20° | uzun, kısalarak |
| 4 | yaz · Temmuz şafak → kuşluk | 72° · 12° | **96° · 30°** | çok uzun → kısalır |

```
⭐ S4'ün BİTİŞİ = S0'ın BAŞLANGICI (96° · 30°). LOOP kapısı budur.
⛔ KLİP İÇİ: her klipte gölge kadrajı SÜPÜRÜR ve açı değişimi 0 DERECE OLAMAZ.
   NARROW LOT'ta beş klibin beşinde de 0° ölçüldü — çünkü açılar yalnız
   GÖRSEL promptta vardı, I2V'de yoktu [DERS 18]. Bu filmde beş I2V'nin
   beşinde de başlangıç VE bitiş açısı dereceyle yazılıdır.
⛔ MEVSİM tek yönlü: yaz → sonbahar → kış① → kış② → yaz = 12 ay.
⛔ ③ merceğinin "TIME READ FROM THE FILM ALONE" satırı ~1 yıl demelidir.
```

---

## 5. MEVSİM TAŞIYICISI VE GİRİŞ HAZIRLIĞI

```
S0  yaz          koyu yeşil alpin çim · kar çizgisi kadrajın ÜSTÜNDE
S1  sonbahar     pas kahvesi çim · uzak sırttaki boynuzda İLK KAR
S2  kış ①        kar çizgisi VADİ TABANINA iner · her iki viraj karlı ·
                 granit kayanın üstü karlı
S3  kış ②        kar çizgisi VİRAJLARA çekilir · altı çıplak ve eriyik sulu
S4  yaz          kar çizgisi yine kadrajın üstünde · koyu yeşil çim

⭐ KAR ÇİZGİSİNİN YAMAÇTA İNİP ÇIKMASI (SAHA §3.4) bu filmin mevsim saatidir
   ve dört farklı kotta okunur: üst (yok) → boynuz → vadi tabanı → virajlar.

⛔ GİRİŞ HAZIRLIĞI GİDEN KLİBİN İÇİNDEDİR [DERS 21]:
   S1'in SON saniyesi: ilk kar istiflenmiş çelik profillerin ve pasa
      bermisinin üst kenarına düşer, zemin hâlâ koyu ve ıslak.
   S3'ün SON saniyesi: gri sulusepken bitmiş, platformdan ilk kuru toz kalkar.
   ⛔ Bu iki cümle yoksa ⑥ C2 SEASON CHANGE düşer (NARROW LOT: 4/10).
```

---

## 6. MONOTON BÜYÜME VE SÖKÜM TAKVİMİ

```
S0  kırılmamış yüz + 12 m ham şev kesiği     EKLENEN: şev kesiği
S1  + ağız (18 m) + püskürtme beton + platform + pasa bermisi
                                             EKLENEN: AĞIZ
S2  + 12,5 m başlık duvarı + kanopi kalıbı   EKLENEN: başlık duvarı
S3  + kanopi + 14 panel istinat duvarı + kaplama halkası
                                             EKLENEN: istinat duvarı
S4  + asfalt + bariyer + 62 lamba            SÖKÜLEN: bütün geçici ekipman

SÖKÜM TAKVİMİ (hepsi S4'ten ÖNCE)
  şantiye çiti + konteyner   kurulum S1 → söküm S4'ten önce
  delici jumbo               kurulum S1 → söküm S4'ten önce
  havalandırma kanalı        kurulum S1 → söküm S4'ten önce
  beton pompası + duvar kalıbı  kurulum S2 → söküm S4'ten önce
  kaplama kalıp arabası      kurulum S3 → söküm S4'ten önce

⛔ SÖKÜLMEYEN — BEDELDİR, kalır:
  pasa bermisi    S1'de doğar → S4'te kalıcı düzeltilmiş SEKİ
  şev yarası      S0'da açılır → hiçbir sahnede kapanmaz

⛔ ZEMİN DURUMU BİRİKİR (NARROW LOT ⑤ WEAR 2/10'da birikmedi):
  S0 kuru scree + kaya tozu → S1 derin çamur + pasa → S2 gri izli kar +
  altında siyah çamur → S3 eriyik su + sulusepken → S4 yeni asfalt +
  kenarda kurumuş açık renkli pasa kabuğu
```

---

## 7. ⛔ BU SPEC'İN KENDİ AÇIKLARI — üretimden önce bilinen

```
⛔ KLİP SÜRESİ ÖLÇÜLMEDİ [D-d]. 6,0 hedeftir. İlk test klibinden sonra
   §0, §1 ve plandaki bütün zaman kodları yeniden yazılır.
⛔ DÜZ IZGARA bilerek seçildi. ⑥ merceğinin METRONOM hükmü VERMESİ
   beklenmelidir; telafi klip içi vuruş yerlerine taşındı (plan §2).
   ⚠️ Makine bunu yakalamaz: prompt_kontrol.py 5 satırlık tabloda süre
      eşitliğini BLOCK edemez (eşik 6 satır).
⛔ TÜNELİN İÇİ GÖRÜNMEZ. ② merceği "yapı büyüyor mu" diye sorduğunda
   büyüyen şey tüp değil, PORTAL ÖNÜ ve PASA BERMİSİDİR. Bu tasarım kararı
   bu depoda hiç sınanmadı.
⛔ S4'ÜN IŞIK YAYI FARKLI (2,5 saat · şafak → kuşluk; diğerleri tam gün).
   Loop'un bedelidir. ③ merceği bunu "tutarsız klip içi zaman" okuyabilir.
⛔ TERS İNŞA bu depoda hâlâ hiç koşulmadı [AGENTS §6].
⛔ ÇAPA KOTLARI kaya burnunun kendi YÜKSEKLİĞİNİ vermiyor (yalnız iki
   yarığın kotu var). Burun kadrajı taşarsa ① ANCHOR IDENTITY etkilenmez
   ama ölçüm satırı yazılamaz.
```

---

## 8. KOŞULACAK MERCEKLER

```
ASGARİ SET  ① KARE + ② İNŞA + ⑤ DEVAMLILIK — bu üçü koşulmadan YAYINLANMAZ.
SIRA        ① · ③ · ⑤ ÖNCE (mod V · doküman verilmez)
            sonra ② (bu SPEC) · ④ (plan + kapak) · ⑥ (plan + SESLİ kurgu)
⭐ Bu film, bu SPEC üretimden ÖNCE hazır olduğu için ② ④ ⑥'nın belgesiz
   koşma riski YOKTUR [DERS 17].
```
