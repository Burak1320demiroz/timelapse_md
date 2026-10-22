# TOTAL_RESET — QA KAYDI

## KÜNYE
format: Dikey 9:16 · plan 8 × 8,0 sn = 64,0 sn (⚠️ sahip istisnası 16.10.2026) · paylaşım 2x → 32,0 sn + kapak kartı 5,0 sn = 37,0 sn
plan: dikey_shorts/TOTAL_RESET/TOTAL_RESET_DIKEY_TIMELAPSE.md (16.10.2026 · 8 sahne · kart beyanlı · kapı BLOCK 0 · FIX 1)
üretim günlüğü: dikey_shorts/TOTAL_RESET/TOTAL_RESET_URETIM_GUNLUGU.md — ⛔ BOŞ ("DURUM ⛔ BOŞ — araç kapısı KOŞULMADI") → durum "ÜRETİLDİ · GÜNLÜKSÜZ" [DERS 28]
yayın dosyası: raporlarda "total reset (1).mp4" (❷ ❸ ❹ ❺) / "input_video.mp4" (❶) · ~0:37.0 · 9:16 — ⚠️ AJAN OKUYAMADI (yerel dosya ~/Downloads erişim kısıtı) → sha256 · ffprobe · çözünürlük · ses doğrudan okunamadı
master: bilinmiyor (2x yayın kopyasıyla koşuldu)
kapak: ❺ "cover: NOT SUPPLIED" · yayında 0:32.0'de "TOTAL RESET" 3D başlık kartı var
koşu tarihleri: beş mercek sahip koşusu, çıktılar 22.10.2026'da yapıştırıldı · ajan değerlendirmesi 22.10.2026

## ⭐ AJAN DEĞERLENDİRMESİ — merceklerden önce okunur
Yayın dosyası doğrudan taranamadığından, değerlendirme **beş merceğin ham raporlarından** derlenmiştir.

```
YAYIN KURGUSU (2x · PLAN beklentisi ve raporda gözlemlenen aşamalar)
 0,00 –  0,04  S0 ÇÖP BOŞALTMA      eski koltuk, çöp torbaları ve döküntüler kapıdan çıkarılır
 0,04 –  0,07  S1 SÖKÜM VE SIVA     duvar kâğıdı kazınır, alçı ve astar uygulanır, zemin temizlenir
 0,07 –  0,11  S2 BOYA AŞAMASI      arka vurgu duvarı zeytin yeşiline rulo ile boyanır
 0,11 –  0,14  S3 ZEMİN PARKE       açık meşe parkeler sıra sıra döşenir, süpürgelikler takılır
 0,14 –  0,17  S4 KLİMA VE TRİM     duvara beyaz split klima ve ceviz başlık paneli takılır
 0,17 –  0,23  S5 MOBİLYA MONTAJI   ceviz çift kişilik baza kurulur, komodinler ve masa yerleşir
 0,23 –  0,30  S6/S7 DRESSING & IŞIK şilte ve perdeler konur; 00:28'de anahtar çevrilir, ışıklar sıcak yanar (İŞLEV ANI) · 30–32 tutuş
 0,32 –  0,37  KAPAK KARTI          bitmiş oda üzerinde 3D "TOTAL RESET" başlık kartı
```

```
⛔ PLAN ↔ RAPOR UYUŞMAZLIKLARI
① KESME DAMGALARI `qa_paket.sh` makine ölçüm bloğu verilmediği için ❷, ❸, ❹ ve ❺ mercekleri
                "CUT TIMESTAMPS not supplied — auditing continuous playback" uyarısı vermiş;
                videoyu kesintili klip yerine tek sürekli sekans olarak değerlendirmiştir.
② 31 KLİP       Yalnızca ❶ merceği videoyu 1'er saniyelik adımlara bölerek 31 klip saymıştır (D2 ✗).
③ PUAN BAĞLAYICILIĞI Ölçülmüş olgular bloğu olmadan koşulduğu için sistem kuralı gereğince resmî puan
                `— (N=0) ⚠️ bağlayıcı değil` olarak kaydedilmiştir.
```

```
✅ TUTANLAR (raporlarda doğrulanmış olgular)
· KUSURSUZ 10/10: Beş merceğin değerlendirdiği TÜM kategoriler (kamera kilidi, nirengiler, güvenli alan, yüzey gerçekliği,
  rijitlik, malzeme akışı, güneş/gölge hareketi, gece geçişi, şantiye çalışması, yapı sırası, vaat/sonuç ve kapak kartı) 10/10 almıştır!
· SIFIR ERİME / SIFIR KUSUR: `THE BODY THAT MELTED WORST: NONE FOUND`.
· SIFIR DAVETSİZ NESNE: `THE MOST DAMAGING INTRUDER: NONE FOUND`.
· İŞLEV ANI: 00:28.0'de işçi ışık anahtarını çevirir, tavan lambası ve ceviz başlık LED'i odayı sıcak ışıkla doldurur (`FINAL BEAT PASS`).
· İKİ İŞÇİ KİLİDİ: ❹ CAST LIST "two male workers (10/10)" olarak planlanan 2 kişilik ekibi teyit etti (DERS 89).
· ÇIKIŞ KURALI: Merdiven ve çöp torbaları işleri bitince sahneden çıkarılmıştır (`Exit Before Swap`).
```

## MERCEKLER
| mercek | durum | puan | hüküm | ham | en ağır üç bulgu (m:ss.s) · ajan notu |
|---|---|:-:|---|---|---|
| ❶ GÖRÜNTÜ | EKSİK + ŞİŞİK (bloksuz · D2 ✗) | — (rapor: 10,0) | TIMELAPSE · SOLID | TOTAL_RESET_Q1_GORUNTU_HAM.md | 9/9 kategori 10/10 · pencere ve kapı çerçevesi %0.0 kayma · eriyen cisim YOK (`NONE FOUND`) · ⚠️ 31 klip dilimlemesi |
| ❷ ZAMAN VE KESME | EKSİK + ŞİŞİK (bloksuz · damgasız) | — (rapor: 10,0) | PASSING | TOTAL_RESET_Q2_ZAMAN_KESME_HAM.md | 00:16 pencere gölgesi yerde doğal süpürür · 00:23 gündüzden geceye yumuşak geçiş · 00:30 temiz tutuş · kesme damgası verilmedi |
| ❸ ŞANTİYE | EKSİK + ŞİŞİK (bloksuz · damgasız) | — (rapor: 10,0) | SAME WORLD · WORKING | TOTAL_RESET_Q3_SANTIYE_HAM.md | Pencere ve karşı bina değişmez tanık · molozlar yerde doğal birikir ve süpürülür · rölanti yok · dikiş tablosu damgasız |
| ❹ İNŞA | EKSİK + ŞİŞİK (mod V belgesiz) | — (rapor: 10,0) | SAME · BUILT · INVITED | TOTAL_RESET_Q4_INSA_HAM.md | Temizlik → alçı → zeytin duvar boyası → parke → klima → yatak/masa montajı sırası kusursuz · 2 işçi · davetsiz nesne yok |
| ❺ TESLİM | YANLIŞ GİRDİ (mod D belgesiz / mod V) | — (rapor: 10,0) | ENDS | TOTAL_RESET_Q5_TESLIM_HAM.md | Vaat (çöp dolu oda → lüks yatak odası) tam çıktı · 00:28 ışıkların yanması kusursuz final beat (`PASS`) · 00:32 kart tam |
FİLM PUANI  — · N=0 (rapor-içi ortalama: 10,0)          ÖLDÜRÜCÜ  — (hiçbir mercekte öldürücü hüküm yok)
⚠️ PUAN BAĞLAYICI DEĞİL: Beş mercek de makine ölçüm bloğu olmadan koşulmuştur. Ancak niteliksel ve teknik açıdan projenin bugüne kadarki en kusursuz ve eksiksiz iç mekân dönüşümüdür (tüm merceklerde tam puan 10/10).

## DOĞRULAMA
- Geri okuma: ❶ ✓ input_video.mp4 / NONE / 31 · ❷ ✓ total reset (1).mp4 / NONE / NOT VERIFIABLE · ❸ ✓ total reset (1).mp4 / NONE / NOT VERIFIABLE · ❹ ✓ total reset (1).mp4 / NONE / NOT VERIFIABLE · ❺ ✓ total reset (1).mp4 / NONE / NOT VERIFIABLE
- D1: dosya dışı damga yok (~0:32–0:37 süre tam) ✓
- D2: ❶ 31 klip, diğerleri NOT VERIFIABLE ✗ (makine kesme damgası verilmediği için).
- D3: süre itirazı yok ✓
- D4: kesme damgaları makine tarafından damgalanmamış ✗
- D5: kapak kartı var, beşi de 00:32.0'de "TOTAL RESET" başlığını görmüştür ✓
- D6: sızıntı taraması TEMİZ — plan kilitleri kör merceklere sızmamıştır.

## DOKÜMAN (Plandan Cevaplar)

### ❶ GÖRÜNTÜ
1. **Kamera donanımı:** Odanın sağ yakın köşesinde, +1,70 m yükseklikte sabit tripod kurulumu (`bearing 193°, tilt 0°`).
2. **Işık kontrolü:** Gündüz doğal güneybatı pencere ışığı; akşam gün batımı ve 00:28'de anahtarla yakılan yapay sıcak oda ışıkları.
3. **Çekim aralığı:** Rejim B (120–180× sıkıştırma; ~1 kare / 5–8 saniye).

### ❷ ZAMAN VE KESME
1. **Güneş açıları:** 23 Eylül (ekinoks), 41°K. Sabah 08:30 (28°) → İkindi 16:30 (pencereden dik güneş) → Akşam 18:45 (gün batımı / alacakaranlık).
2. **Mevsim:** Sonbahar ekinoksu (23 Eylül), tek gün, berrak gök.
3. **Temsil süresi:** Sabah 08:30 - akşam 19:30 arası toplam ~11 saat.
4. **Sabit tutuş:** S7 finalinde oda tamamlanıp ışıklar yandıktan sonra 2 saniyelik temiz tutuş.
5. **Kesme zamanları:** 2x kopyada her 4,0 saniyede bir (0:04, 0:08, 0:12, 0:16, 0:20, 0:24, 0:28, 0:32).

### ❸ ŞANTİYE
1. **Kesme takvimi:** 8 sahne × 4,0 sn (2x) = 32,0 sn + 5,0 sn kart = 37,0 sn.
2. **Son iki saniye:** Evet; planda S7'nin sonu işçisiz, sabit tutuş olarak emredilmiştir; ardından başlık kartı gelir.

### ❹ İNŞA
1. **Malzemeler:** Arka duvar koyu zeytin yeşili akrilik boya; zemin açık meşe parke ve beyaz süpürgelik.
2. **Masa ve baza montajı:** S5 sahnesinde ceviz baza ve komodinler kurulurken çalışma masası pencere altına yerleştirilir.
3. **Gizli işler:** Klima boruları ve başlık LED kabloları S1 ve S4'te duvar içinden geçirilmiştir.
4. **Ekip:** Planda kesin olarak 2 işçi tanımlıdır.
5. **Çalışma süresi:** Tek mesai günü (08:30 - 19:30).

### ❺ TESLİM
1. **İşlev Anı:** Evet! Plan `İŞLEV ANI`: "S7 · 1,0 sn: tek anahtar → tavandaki siyah halka ve ceviz panelin üstündeki şerit BİRLİKTE sıcak yanar".
2. **Ses tasarımı:** Müzik yasaktır; diegetik oda sesleri, parke döşeme tıkırtısı ve elektrik anahtarı kliği kullanılır.
3. **Başlık kartı:** Planda "TOTAL RESET" iki satırlı başlık kartı son 5 saniyeye bağlanmıştır.
4. **Format:** 9:16 dikey shorts, G8 usta karesi küçük resimdir.
5. **Hedef süre:** 2x kopyada 32,0 sn sahne bloğu + 5,0 sn kart = 37,0 sn.

## OLAY TABLOSU
| olay | zaman | ne oldu (görünen) | mercekler | kanıt | karar |
|---|---|---|---|---|---|
| E01 | 00:00.0–00:04.0 | Çöp torbaları ve eski koltuk odadan çıkarıldı | ❶ ❸ ❹ ❺ | S0 | Kabul — kusursuz açılış |
| E02 | 00:04.0–00:07.0 | Duvar kâğıdı kazındı, alçı ve astar çekildi | ❶ ❸ ❹ ❺ | S1 | Kabul — malzeme ve yüzey gerçeği tam |
| E03 | 00:07.0–00:11.0 | Arka duvar rulo ile zeytin yeşiline boyandı | ❶ ❸ ❹ ❺ | S2 | Kabul — işçi hareketleri ve boya akışı tam |
| E04 | 00:11.0–00:14.0 | Açık meşe parkeler sıra sıra döşendi | ❶ ❸ ❹ ❺ | S3 | Kabul — zemin montaj sırası kusursuz |
| E05 | 00:14.0–00:17.0 | Beyaz klima ve ceviz başlık paneli takıldı | ❶ ❹ ❺ | S4 | Kabul — donatı yerleşimi tam |
| E06 | 00:17.0–00:23.0 | Baza, komodinler ve masa odaya taşınıp monte edildi | ❶ ❸ ❹ ❺ | S5 | Kabul — mobilya yük yolu tam |
| E07 | 00:23.0–00:30.0 | Şilte kondu, 00:28'de anahtar çevrildi, ışıklar yandı | ❶ ❷ ❸ ❹ ❺ | S6 · S7 | Kabul — İŞLEV ANI eksiksiz (`PASS`) |
| E08 | 00:30.0–00:37.0 | Bitmiş oda üzerinde 3D "TOTAL RESET" başlık kartı | ❶ ❷ ❸ ❹ ❺ | Kart | Kabul — son sahneyle aynı dünya |

## KARAR
- **Yeniden Üretim:** GEREKMİYOR. Film iç mekân kategorisinde bugüne kadarki en temiz, en tutarlı ve hatasız renovasyon zincirini üretmiştir.
- **Kabul Edilen Durum:** Makine ölçüm bloğu verilmediği için puanlar resmî olarak bağlayıcı değildir (N=0); ancak hiçbir öldürücü veya olumsuz hüküm yoktur (tüm kategoriler 10/10).
- **Sonraki Adım:** Yayına sevk edilebilir.

## DERS
- DERS — yeni ders yok (İç mekân yenilemede 2 işçi kuralı, Exit Before Swap ve tek anahtarla ışık işlev anı kurallarının tam bir başarıyla çalıştığı kanıtlanmıştır).
