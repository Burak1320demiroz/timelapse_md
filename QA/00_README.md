# 🔍 QA — ALTI MERCEK

> Bu klasör **rubrikleri** (girdi) ve **skor tablolarını** (çıktı) tutar.
> Rubrik üretilmiş işi eleştirir; tablo sonucu saklar. İkisi karışmaz.

---

## 1. ALTI MERCEK

| | Dosya | Tek soru | Girdi | Mod |
|:-:|---|---|---|:-:|
| ① | `1_KARE_QA.md` | Bu bir timelapse mi, ayrı ayrı görüntüler mi? | yalnız video + kare grabları | **V** |
| ② | `2_INSA_QA.md` | Aynı yapı mı? Gerçekten inşa ediliyor mu? | video + QA_SPEC | **D** |
| ③ | `3_ZAMAN_QA.md` | Zaman geçiyor mu, yoksa sadece ışık mı değişiyor? | yalnız tam kurgu | **V** |
| ④ | `4_TESLIM_QA.md` | Bitiyor mu, duruyor mu? | tam kurgu + plan + kapak | **D** |
| ⑤ | `5_DEVAMLILIK_QA.md` | Aynı dünya mı, her çekimde yeniden mi kuruldu? | yalnız video + kare grabları | **V** |
| ⑥ | `6_GECIS_QA.md` | Kesme ZAMAN mı demek, SIRADAKİ mi? | tam kurgu + plan + ses | **D** |

### Eksenler nasıl ayrıldı — çakışma yok

```
① kamera ve kare        kadraj oynadı mı, kare temiz mi
② yapı ve inşa mantığı  aynı yapı mı, yöntemi gerçek mi
③ ışık ve akış          zaman geçiyor mu, tek yönde mi
④ vaat ve teslim        söz verilen şey ekrana çıktı mı
⑤ DÜNYA                 yapı ve ışık DIŞINDA kalan her şey kesmeyi karşıya
                        geçebiliyor mu — makine · konteyner · çamur · yol ·
                        ağaç · su · yıpranma
⑥ KESMENİN KENDİSİ      sıçrama boyu · yön · ritim · ölçü hizası · karta devir

⛔ ①-④ sahneleri BÜTÜN olarak inceler. Hiçbiri DİKİŞE bakmaz: sahne N'in
   SON karesi ile N+1'in İLK karesi. Onu ⑤ alır; rubriğinin çekirdeği odur.
⛔ ③'ün 7. kategorisi bu yüzden daraltıldı: kesmenin YÖNÜ ve VARLIĞI ③'te
   kalır, BOYU · RİTMİ · MEKANİĞİ ⑥'ya geçti. İki kez puanlanan şey iki
   skoru birden anlamsızlaştırır.
```

```
⭐ 3-3 BÖLÜNMESİ KASITLIDIR.
   ① · ③ · ⑤'e DOKÜMAN VERİLMEZ. Üçünün de ölçtüğü şey planı hiç görmemiş bir
   izleyicinin gözüdür. Doküman verilirse değerlendirici filmi kendi içinde
   değil plana karşı okur ve filmin KENDİ KENDİSİYLE çeliştiğini kaçırır.
   Bunun yerine üçü de sonunda "QUESTIONS FOR THE DOCUMENT" listesi çıkarır;
   o soruları ajan plandan cevaplar. Rubriğin ikinci yarısı o adımdır.

   ② · ④ · ⑥ sözleşmeye karşı denetimdir; plan olmadan yalnız ön koşu olur.
```

```
⛔ ASGARİ SET — hepsini koşamıyorsan
   ① + ② + ⑤  bu türün öldürücü üç arızasını yakalar:
   kadraj oynadı mı · aynı yapı mı · aynı dünya mı.
   Kalan üçü olmadan film yayınlanabilir; bu üçü olmadan yayınlanmamalı.
```

## 2. ÇALIŞTIRMA

⭐ **Koşu sırası numara sırası DEĞİLDİR.** Doküman körlüğü isteyen ikisi (① ve
③) önce koşulur: önce SPEC'i okuyup sonra "mod V koşuyorum" demek, körlüğü
zaten kaybetmiş olmaktır.

```
0. MAKİNE   bash araclar/kare_al.sh <teslim.mp4> 6
            → 18 kare (her klibin ilk/orta/son karesi)
            → ①'in en zor sorusu bir MODELE değil bir SAYIYA sorulur

1. ① KARE       rubrik + tam kurgu + kare grabları   ⛔ DOKÜMAN VERME
2. ③ ZAMAN      rubrik + TAM KURGU                    ⛔ DOKÜMAN VERME
                ⛔ tek klibe koşulmaz — ölçtüğü şeyin çoğu kesmelerin ARASINDA yaşar
3. ⑤ DEVAMLILIK rubrik + tam kurgu + kare grabları    ⛔ DOKÜMAN VERME
                ⭐ kare_al.sh'ın ürettiği "son kare / ilk kare" çiftleri
                   doğrudan bu merceğin DİKİŞ DENETİMİ içindir
4. ② İNŞA       rubrik + tam kurgu + <FILM>_QA_SPEC.md
5. ④ TESLİM     rubrik + tam kurgu + plan dosyası + kapak görseli
6. ⑥ GEÇİŞ      rubrik + tam kurgu + SESLİ + plan dosyası
```

Her koşuda **başka hiçbir şey verilmez** — medya + rubrik + (mod D ise) tek belge.

### ⛔ GİRDİ SATIRI — koşudan ÖNCE doldurulur [DERS 27]

```
Her koşunun başına, koşmadan ÖNCE tek satır yazılır ve rapora yapıştırılır:
    verilen girdiler: <dosya adları>

⭐ NEDEN BU SATIR VAR — ölçüldü, iki kez:
   NARROW LOT   6 merceğin 5'i eksik girdiyle koştu → SPEC yoktu
   MOUNTAIN DOOR 6 merceğin 5'i eksik girdiyle koştu → SPEC ÜRETİMDEN
                 ÖNCE hazırdı ve yine verilmedi.
   Yani eksik olan BELGE değildi, koşudan önce bakılan bir KONTROL
   SATIRIYDI. Yukarıdaki liste yazılıydı; liste koşturmuyor [DERS 12].

⛔ kare_al.sh dört filmin dördünde de koşulmadı. ① ve ⑤ o yüzden hiç
   tam koşmadı: dikiş denetimi "son kare / ilk kare" çiftlerini hiç görmedi.
⛔ Raporun ilk satırı RUN INCOMPLETE diyorsa skoru tabloya YAZMA, koşuyu
   girdiyi tamamlayıp TEKRARLA [DERS 17].
```

## 3. SKOR TABLOLARI

```
T1_KARE · T2_INSA · T3_ZAMAN · T4_TESLIM · T5_DEVAMLILIK · T6_GECIS  ← satır buraya
00_INDEX.md                                            ⭐ PROJEDEKİ TEK SAYAÇ
RAPORLAR/<FILM>.md                                     film başına kalıcı kayıt
HAM_RAPORLAR/<FILM>_<MERCEK>_HAM.md                    modelin ham çıktısı, dokunulmaz
```

```
Ⓥ İŞARETİ: mod V koşulan skor Ⓥ ile işaretlenir. Ⓥ bir ÖN KOŞUDUR ve
tabloda bağlayıcı sayılmaz — ama VERDICT satırı her modda bağlayıcıdır.
```

```
⛔ YANLIŞ MODDA KOŞULAN MERCEK [DERS 17]
   ② ④ ⑥ mod D merceğidir. Belgesi verilmeden koşulduysa:
     · skoru T tablosuna SKOR OLARAK yazılmaz
     · satır "belgesiz koşuldu — TEKRARLANACAK" diye açılır
     · bulguları geçerlidir ve rapora işlenir
   Ölçülmüş bedeli: ④ mod V'de FINAL BEAT'e PASS verdi, çünkü mod V'de o
   kategori "bir sonu var mı"ya dönüşüyor. Planın gerçek final vuruşu hiç
   denetlenmedi. Ⓥ "kabul edildi" demek değildir.
```

## 4. ⭐ VERDICT KATEGORİLERİ YENER

Her rubrik 8 kategoriyi puanlar **ve** kategorilerden bağımsız tek satırlık bir
hüküm verir. İkisi çelişirse **hüküm kazanır.**

```
① BU BİR TIMELAPSE Mİ?        TIMELAPSE / AYRI AYRI GÖRÜNTÜLER
② AYNI YAPI MI?               AYNI / FARKLI  ·  BUILT / APPEARING
③ ZAMAN GEÇİYOR MU?           GEÇİYOR / YANLIŞ YÖNDE GEÇİYOR / SADECE IŞIK
④ BİTİYOR MU, DURUYOR MU?     BİTİYOR / DURUYOR  ·  + NONE FOUND satırı
⑤ AYNI DÜNYA MI?              AYNI DÜNYA / HER ÇEKİMDE YENİDEN KURULMUŞ
                              + "aynı yeri KANITLAYAN nesne" satırı
⑥ KESME ZAMAN MI DEMEK?       ZAMAN / SIRADAKİ  ·  RİTİM / METRONOM
```

⭐ **⑥'nın METRONOM hükmü yeni ızgaranın kendi riskidir:** on eşit kesme
teknik olarak kusursuz olabilir ve film yine de düz durur. Hiçbir kategori
bunu yakalamaz — hüküm satırı yakalar.

Sebep: kardeş depoda 18 dikey film teknik kategorilerde iyi puan aldı ve
izlenince anlamsızdı. Kategoriler ortalamaya gider; hüküm gitmez.

## 5. RUBRİK YAZIM KURALI

```
Rubrik dosyalarının İÇİ SALT İNGİLİZCE PROMPTTUR.
İçine YAZILMAZ: Türkçe not · tarih · film adı · ders numarası · depo yolu.
Ders GÖVDEYE KURAL olarak girer; numarası bu README'de ve DERSLER.md'de durur.
Sebep: rubrik yapıştırılıp koşulacak bir metindir, bir belge değil.
```

## 6. AJAN AKIŞI

```
Rapor geldi  → AGENTS.md §2 kart R (rapor işleme)
Yeni bozulma → kilavuzlar/DERSLER.md kart D
Skor         → T tablosuna satır + RAPORLAR/<FILM>.md + 00_INDEX güncelle
Ham çıktı    → HAM_RAPORLAR/ (dokunulmaz)
```
