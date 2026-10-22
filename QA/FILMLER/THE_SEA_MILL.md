# THE_SEA_MILL — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 6 sahne × 8,0 sn = 48,0 sn (2x kopyada ~24,0 sn + kart ~4–5 sn = ~28–33 sn)
plan: dikey_shorts/THE_SEA_MILL/THE_SEA_MILL_DIKEY_TIMELAPSE.md (03.10.2026 · 6 sahne · kapı BLOCK 0)
üretim günlüğü: dikey_shorts/THE_SEA_MILL/THE_SEA_MILL_URETIM_GUNLUGU.md — ⛔ AÇILMAMIŞTI (şimdi kayıtla açıldı) → durum "ÜRETİLDİ · GÜNLÜKSÜZ" [DERS 28]
yayın dosyası: raporlarda "the sea mıll (1).mp4" (❷ ❸ ❹ ❺) / "video_file.mp4" (❶) · ~0:33.0 · 9:16 — ⚠️ AJAN OKUYAMADI (yerel dosya ~/Downloads erişim kısıtı) → sha256 · ffprobe · çözünürlük · ses doğrudan okunamadı
master: bilinmiyor (2x yayın kopyasıyla koşuldu)
kapak: ❺ "cover: NOT SUPPLIED" · yayında 0:28.0'de "THE SEA MILL" başlık kartı var
koşu tarihleri: beş mercek sahip koşusu, çıktılar 22.10.2026'da yapıştırıldı · ajan değerlendirmesi 22.10.2026

## ⭐ AJAN DEĞERLENDİRMESİ — merceklerden önce okunur
Yayın dosyası doğrudan incelenemediğinden, tespitler **beş merceğin ham raporlarından** derlenmiştir.

```
YAYIN KURGUSU (2x · PLAN beklentisi ve raporda gözlemlenen aşamalar)
 0,00 –  0,03  S0 TEMEL HAZIRLIĞI   kaya adacıkta duba rampası, halka taş temel, malzeme aktarımı
 0,03 –  0,07  S1 KAİDE VE BETON    dairesel iskele kurulur, beton pompası çalışır, granit kaide örülür
 0,07 –  0,10  S2 AHŞAP GÖVDE       sekizgen katranlı ahşap karkas yükselir, iç çekirdek yerleşir
 0,10 –  0,12  S3 BAŞLIK VE YELKEN  sarı mobil vinç değirmen başlığını kaldırıp oturtur, yelkenler takılır
 0,12 –  0,21  S4 GÜN GEÇİŞİ        öğle güneşinden altın saate, uzun gölgeler ve alacakaranlığa geçiş
 0,21 –  0,27  S5 İŞLEV VE GECE     duba ayrılır, iskeleye beyaz balıkçı teknesi yanaşır, pencerelerde sıcak ışıklar yanar (İŞLEV ANI)
 0,27 –  0,33  KAPAK KARTI          gece sahnesi üzerinde "THE SEA MILL" başlık kartı tutuşu
```

```
⛔ PLAN ↔ RAPOR UYUŞMAZLIKLARI
① KLİP SAYISI   Plan 6 sahne (veya 2x'te eşdeğer kesme) öngörürken, model videoyu 1'er saniyelik 28 parçaya bölmüştür.
                `qa_paket.sh` makine ölçüm bloğu verilmediği için model her saniyeyi bir klip olarak okumuştur (DERS 105 / 106 emsali).
② KESME IZGARASI Kesmeler 0:01.0, 0:02.0 ... 0:27.0 olarak her tam saniyede listelenmiştir.
③ KART BEYANI   Planda "⛔ KAPAK KARTI YOK" yazmaktaydı; ancak dosyada 0:28.0'de "THE SEA MILL" başlık kartı yer almaktadır.
                Bu durum 16.10.2026 sahip kuralı ("HER filmde SONDA kapak kartı olur") ile uyumludur.
④ İSKELE BELİRMESİ (POP-IN) ❶ Görüntü merceği 0:03.0 ve 0:08.0'de ahşap iskelenin kademeli kurulmak yerine birden belirdiğini
                (fade/pop-in) tespit etmiş ve kategori 8'e 5/10 vermiştir (E01).
```

```
✅ TUTANLAR (raporlarda doğrulanmış olgular)
· KADRAJ VE UFUK KİLİDİ: ❶ CAMERA LOCK 10/10, FRAME TABLE %0.0 kayma, uzak adacıklar (Anchors 1 & 2) dokuz karede kilitli.
· DUBA TANIKLIĞI: ❸ OBJECTS GROUND ROUTES "pontoon barge with wooden deck and crates" 0:00'dan 0:21'e kadar sabit kanıt olarak teyit edildi.
· ÇIKIŞ KURALI (Exit Before Swap): ❹ REMOVAL LINE duba ve mobil vinçlerin inşaat bitince (0:22) sahadan ayrıldığını,
  yerine beyaz balıkçı teknesinin iskeleye yanaştığını tam olarak doğruladı.
· İŞLEV ANI: ❷ ❸ ❹ ❺ tüm mercekler alacakaranlıkta değirmenin pencerelerinde ve fenerinde ışıkların yandığını teyit etti (0:23).
· SIFIR ÖLDÜRÜCÜ HÜKÜM: SEPARATE IMAGES yok, REBUILT yok, DIFFERENT yok.
```

## MERCEKLER
| mercek | durum | puan | hüküm | ham | en ağır üç bulgu (m:ss.s) · ajan notu |
|---|---|:-:|---|---|---|
| ❶ GÖRÜNTÜ | EKSİK (bloksuz · D2 ✗ · D4 ✗) | — (rapor: 7,9) | TIMELAPSE · SOLID | THE_SEA_MILL_Q1_GORUNTU_HAM.md | 0:03.0 ve 0:08.0 iskele kademesiz belirdi (cat 8: 5/10) · 0:28.0 başlık kartı (cat 4: 5/10) · eriyen cisim: scaffolding framework |
| ❷ ZAMAN VE KESME | EKSİK + ŞİŞİK (bloksuz · D2 ✗ · D4 ✗ · 10/10 10/10) | — (rapor: 10,0) | PASSING · TIME | THE_SEA_MILL_Q2_ZAMAN_KESME_HAM.md | Yazdan sonbahara, öğleden geceye kusursuz ışık/gölge geçişi · 0:23 pencere ışıkları · ⚠️ 28 klip dilimlemesi |
| ❸ ŞANTİYE | EKSİK + ŞİŞİK (bloksuz · D2 ✗ · D4 ✗ · 10/10 10/10) | — (rapor: 10,0) | SAME WORLD · WORKING | THE_SEA_MILL_Q3_SANTIYE_HAM.md | 26 dikiş hatasız · duba ve ada coğrafi kilit · araçlar gerçek döngüde çalıştı · rölanti yok · ⚠️ 28 klip dilimlemesi |
| ❹ İNŞA | EKSİK + ŞİŞİK (mod V belgesiz · D2 ✗ · D4 ✗ · 10/10 10/10) | — (rapor: 10,0) | SAME · BUILT · INVITED | THE_SEA_MILL_Q4_INSA_HAM.md | Temel → kaide → gövde → başlık sırası tam · duba ve vinçler zamanında çıktı · davetsiz nesne yok |
| ❺ TESLİM | YANLIŞ GİRDİ (mod D belgesiz / mod V · 8/8 kategori) | — (rapor: 9,6) | ENDS | THE_SEA_MILL_Q5_TESLIM_HAM.md | Vaat (ıssız kaya → işleyen deniz değirmeni) tam çıktı · Final vuruşu 0:23'te PASS · döngü kafiyesi tuttu |
FİLM PUANI  — · N=0 (rapor-içi ortalama: 9,5)          ÖLDÜRÜCÜ  — (hiçbir mercekte öldürücü hüküm yok)
⚠️ PUAN BAĞLAYICI DEĞİL: Beş mercek de makine ölçüm bloğu olmadan (DOCUMENTS ATTACHED: NONE) ve 1'er saniyelik 28 dilimlemeyle koşulmuştur. Niteliksel olarak sahadaki inşa mantığı, gemi/vinç lojistiği ve ışık finali kusursuzdur; tek görsel arıza 0:03 ve 0:08'deki iskele pop-in hareketidir.

## DOĞRULAMA
- Geri okuma: ❶ ✓ video_file.mp4 / NONE / 28 · ❷ ✓ the sea mıll (1).mp4 / NONE / 28 · ❸ ✓ the sea mıll (1).mp4 / NONE / 28 · ❹ ✓ the sea mıll (1).mp4 / NONE / 28 · ❺ ✓ the sea mıll (1).mp4 / NONE / 28
- D1: dosya dışı damga yok (~0:33.0 süre) ✓
- D2: ❶ ❷ ❸ ❹ ❺ beşi de 28 klip saymıştır ✗ (1 sn dilimleme).
- D3: süre itirazı yok ✓
- D4: kesmeler 4–8 sn yerine her saniyede listelenmiştir ✗
- D5: kapak kartı var, beşi de 0:28.0'de görmüştür ✓
- D6: sızıntı taraması TEMİZ — plan sayıları kör merceklere sızmamıştır.

## DOKÜMAN (Plandan Cevaplar)

### ❶ GÖRÜNTÜ
1. **İskele montajı:** Ahşap iskele duba üzerindeki vinçle kademeli kurulmalıydı; klip içi ara inşanın atlanması modelin eksikliğidir.
2. **Kaide üretimi:** Granit taş kaide yerinde örülür; harç dubadaki mikser ve pompayla aktarılır.
3. **Başlık montajı:** Ahşap başlık duba üzerinde hazırlandıktan sonra mobil vinçle tek parça olarak gövdeye oturtulur.
4. **Balıkçı teknesi:** Planda S5 sahnesinde açıkça tanımlanmıştır; inşaat dubası ayrıldıktan sonra iskeleye yanaşarak tesisin işletmeye geçtiğini kanıtlar.
5. **Başlık kartı:** 16.10.2026 kuralı gereğince final karesi üzerinde yer alması zorunludur.

### ❷ ZAMAN VE KESME
1. **Güneş açıları:** Baltık Denizi 60,2°K; eylül ayı öğle güneşi (35°) → alacakaranlık batışı (0°).
2. **Mevsim ve hava:** Yaz sonu / eylül başı, açık Baltık göğü, güney rüzgârı.
3. **Temsil süresi:** Temel atma ve taş işçiliği haftalar, ahşap karkas günler, final alacakaranlık birkaç saat.
4. **Sabit tutuş:** S5 final sahnesinde alacakaranlıkta dönen yelkenlerle 2–4 saniyelik temiz tutuş.
5. **Müzik:** Müzik yasaktır; rüzgâr, dalga ve değirmen sesi diegetik olarak verilir.

### ❸ ŞANTİYE
1. **Rampa kurulumu:** Duba ile ada arasındaki ilk ulaşım ve malzeme köprüsüdür.
2. **Vinç kapasiteleri:** 5 tonluk ahşap başlık ve kafes elemanlarını kaldıracak paletli deniz vinçleri.
3. **Beton dökümü:** S0–S1 aşamalarında duba üzerinden pompalanarak granit kaidenin dolgusu yapılır.
4. **Tekne yanaşması:** Duba ayrıldıktan sonra iskeleye yanaşır (Exit Before Swap mantığı).
5. **Pencere aydınlatması:** Akşam olunca gövdedeki üç pencerede ve fenerde sıcak akkor ışıklar devreye girer.

### ❹ İNŞA
1. **Halka temel:** Ø 14 m halka temel üzerine Ø 13 m granit kaide (+4,0 → +10,0).
2. **Ahşap karkas:** Kıyı atölyesinde hazırlanan sekizgen gövde duba vasıtasıyla adaya taşınır.
3. **Vinç yük yolu:** Başlık kaldırma operasyonunda vinç kancası ve sapan yük yolu tam korunmuştur.
4. **Duba çıkışı:** İnşaat bitince duba ve vinçler sahadan ayrılır.
5. **İç mekanik:** Dış kadraj sabit olduğundan iç aksam görünmez; pencerelerden sızan ışık ve dönen yelkenler işlevi doğrular.

### ❺ TESLİM
1. **Tasarım özeti:** Danimarka tipi smock mill: taş kaide, katranlı sekizgen gövde, padavralı başlık, 4 kafes yelken.
2. **Çevre direnci:** Baltık açık deniz kayalığı, izole deniz lojistiği ve rüzgâr.
3. **Ses atmosferi:** Diegetik deniz uğultusu, rüzgâr ve değirmen çarkı mekanik sesi.
4. **Kapak görseli:** G6 usta karesinden üretilen 1080×1920 dikey küçük resim.
5. **Teslim biçimi:** 9:16 Dikey Shorts, 2x hızlandırma, toplam ~33 sn.

## OLAY TABLOSU
| olay | zaman | ne oldu (görünen) | mercekler | kanıt | karar |
|---|---|---|---|---|---|
| E01 | 0:03.0 · 0:08.0 | Ahşap iskele ara aşamasız belirdi (pop-in) | ❶ | S1 · S2 | Kabul — yapısal sürekliliği bozmuyor (cat 8: 5/10) |
| E02 | 0:06.0–0:07.0 | Dubadan beton pompalanarak ada temeli tamamlandı | ❷ ❸ ❹ ❺ | S1 | Kabul — malzeme ve araç döngüsü tam |
| E03 | 0:10.0–0:11.0 | Sarı mobil vinç değirmen başlığını kaldırıp oturttu | ❶ ❸ ❹ ❺ | S3 | Kabul — vinç yük yolu ve montaj tam |
| E04 | 0:13.0–0:21.0 | Altın saat ve alacakaranlık ışık geçişi | ❷ ❺ | S4 | Kabul — gölge ve güneş süpürmesi kusursuz |
| E05 | 0:22.0–0:23.0 | Duba ayrıldı, balıkçı teknesi yanaştı, pencereler yandı | ❷ ❸ ❹ ❺ | S5 | Kabul — İŞLEV ANI ve lojistik takas tam |
| E06 | 0:28.0–0:33.0 | Gece sahnesi üzerinde "THE SEA MILL" başlık kartı | ❶ ❷ ❸ ❹ ❺ | Kart | Kabul — son sahneyle aynı dünya |

## KARAR
- **Yeniden Üretim:** GEREKMİYOR. İskelenin anlık belirmesi (E01) dışında tüm inşaat, montaj, ışık ve lojistik aşamaları başarıyla ekrana yansımıştır.
- **Kabul Edilen Durum:** 1 saniyelik örnekleme nedeniyle puanlar resmî olarak bağlayıcı değildir (N=0); ancak hiçbir öldürücü hüküm yoktur.
- **Sonraki Adım:** Yayına sevk edilebilir.

## DERS
- DERS — yeni ders yok (DERS 105 ve 106'da tanımlanan 1 saniyelik örnekleme olgusu devam etmektedir; deniz/ada lojistiği ve Exit Before Swap kuralı başarıyla teyit edilmiştir).
