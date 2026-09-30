# 📊 00_INDEX — PROJEDEKİ TEK SAYAÇ

> ⛔ Sayılar buraya ELLE yazılır ama `bash araclar/sayac.sh` ile
> KARŞILAŞTIRILIR. Betik uyuşmazlığı ekrana basar. Bir sayıyı iki yerde
> tutmak, birini yanlış tutmaktır.

---

## SAYIM

```
TOPLAM FİLM       41
ÖLÇÜLEN FİLM      27
TAM ÖLÇÜLEN       0     (8 merceğin 8'i de koşulmuş — ⑦ ⑧ 07.09.2026'da açıldı)
SEKİZ MERCEKLE    22    (THE LONG DAY · THE DUST YEAR · BUILT FROM DUST · POLAR HABITAT · THE CROSSING · OVER THE WALL · THE EMPTY RIDGE · THE DARK ROCK · BACK TO WATER · THE QUIET FIELD · THE EMPTY LOCK · THE BROKEN CLIMB · THE BLUE DOOR · THE DEEP END · THE VANISHING ROOM · THE GLASS CROSSING · THE FIRST GUEST · THE LAST HARBOR · THE MOUNTAIN CROWN · THE LAST LIFT · THE LAST FIRING · BACK TO PLUMB)
ON İKİ MERCEKLE   18    (OVER THE WALL · THE EMPTY RIDGE · THE DARK ROCK · BACK TO WATER · THE QUIET FIELD · THE EMPTY LOCK · THE BROKEN CLIMB · THE BLUE DOOR · THE DEEP END · THE STONE DRAGON · THE VANISHING ROOM · THE GLASS CROSSING · THE FIRST GUEST · THE LAST HARBOR · THE MOUNTAIN CROWN · THE LAST LIFT · THE LAST FIRING · BACK TO PLUMB — ⑨ ⑩ ⑪ ⑫ dâhil)
ALTI MERCEKLE TAM 8     (⑦ ⑧ öncesi / alternatif tamlık · THE MOUNTAIN DOOR · THE NARROW LOT · THE CLOSING SPAN · THE QUIET FIELD · THE EMPTY LOCK · THE STONE DRAGON · THE VANISHING ROOM · THE LAST FIRING)
ÜRETİLEN FİLM     26
YAZILDI, ÜRETİLMEDİ 15  (BEFORE NIGHTFALL · THE OLD ROAD · THE HIDDEN OASIS · THE NARROW GORGE · THE LAST CIRCLE · THE BORROWED HILL · ONE MORE TURN · THE SWALLOWED BUS · ORBITAL_SCAFFOLD · THE TIDE GATE · THE LONG SHADOW v2 · THE GLASS WALL · THE STONE TOWER · THE IRON BRIDGE · THE DEEP STEP)
```

```
⚠️ 28.09.2026 — KAYIT AÇIĞI, BACK TO PLUMB yazılırken tespit edildi (sayaç 38 diyordu, INDEX 37):
   ⛔ THE GLASS WALL (yatay_2_dk_filmler/THE_GLASS_WALL/) bu INDEX'e HİÇ GİRMEMİŞTİ.
   Klasör tam: PLAN · BÖLÜM 1 · BÖLÜM 2 · QA_SPEC · KAPAK · MÜZİK · YAYIN PAKETİ · ÜRETİM GÜNLÜĞÜ
   · 00_ANALIZ. 16:9 · 12 × 10,0 = 120,0 sn + 5,0 sn kapak kartı · YATAY ailesi · 28.09.2026.
   Durumu KENDİ günlüğünden okundu: '⛔ BOŞ — araç kapısı KOŞULMADI' → YAZILDI, ÜRETİLMEDİ.
   ⛔ Başka hiçbir alanı buraya yazılmadı: bu film bu oturumda YAZILMADI, yalnız SAYILDI.
   ⚠️ Ayrıca kendi planı 'Havuz kaydı: YAYIN_PLANI §5 #5 THE GLASS WALL' diyor ama §5 satır 5
      THE EMPTY RIDGE'dir; film YAYIN_PLANI'nda da kayıtlı DEĞİL. İki açık da sahibin kararını bekler.
   ⚠️ İkinci kez oluyor: THE LAST LIFT de (35. film) YAYIN_PLANI §3/§4'te hâlâ kayıtlı değil.
```

## TAMLIK MATRİSİ

Bir film "tam ölçüldü" sayılmak için sekiz merceğin sekizini de görmelidir.
⑦ ve ⑧ 07.09.2026'da açıldı; önceki dört filmin hiçbiri bu ikisiyle ölçülmedi.

> ⭐ **INC sözleşmesi (18.09.2026 · QA/QA_CAPRAZ_ANALIZ/01 ile aynı):** koşu başladı ama
> dosya açılamadığı için puan üretemediyse hücreye **INC** yazılır, 0 yazılmaz;
> INC ortalamaya girmez. "⛔ belgesiz" = mod D merceği belgesiz koştu (RUN INCOMPLETE,
> puan Ⓥ). İkisi farklı şeydir: INC puan yok, belgesiz puan var ama körlüğü bozuk.

| Film | ① KARE | ② İNŞA | ③ ZAMAN | ④ TESLİM | ⑤ DEVAM | ⑥ GEÇİŞ | ⑦ İŞ | ⑧ YÖNTEM | Tam |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **THE LONG DAY** | Ⓥ 6,4 karesiz | ⛔ belgesiz | **7,0** | ⛔ belgesiz | Ⓥ 5,8 karesiz | ⛔ belgesiz | Ⓥ 4,4 karesiz | ⛔ belgesiz | **8/8** · 8'i de RUN INCOMPLETE |
| **THE MOUNTAIN DOOR** | Ⓥ 1,1 | ⛔ belgesiz | **3,6** | ⛔ belgesiz | Ⓥ 0,2 | ⛔ belgesiz | ❌ | ❌ | **6/8** |
| **THE NARROW LOT** | Ⓥ 6,0 | ⛔ belgesiz | **4,2** | ⛔ belgesiz | Ⓥ 5,6 | ⛔ belgesiz | ❌ | ❌ | **6/8** |
| THE LONG SHADOW v1 | Ⓥ 3,3 | Ⓥ 0,4 | Ⓥ 4,3 | Ⓥ 2,7 | ❌ | ❌ | ❌ | ❌ | **4/8** |
| THE CLOSING SPAN | 1,0 | Ⓥ 0,0 | 1,3 | Ⓥ 5,4 | Ⓥ 0,0 | Ⓥ 1,6 | ❌ | ❌ | **6/8** |
| **THE DUST YEAR** | Ⓥ 1,3 karesiz | ⛔ belgesiz 0,9 | 4,0 | ⛔ belgesiz 2,1 | Ⓥ 4,0 karesiz | ⛔ belgesiz 6,6 | Ⓥ 1,3 karesiz | ⛔ belgesiz **0,0** | **8/8** · 7'si RUN INCOMPLETE |
| **BUILT FROM DUST** | Ⓥ 1,1 karesiz | ⛔ belgesiz 2,8 | Ⓥ 3,3 | ⛔ belgesiz 2,5 | Ⓥ 1,6 karesiz | ⛔ belgesiz 4,5 | Ⓥ 1,8 karesiz | ⛔ belgesiz **0,0** | **8/8** · 8'i de RUN INCOMPLETE |
| **THE CROSSING** | Ⓥ 8,4 | ⛔ belgesiz 6,4 | **10,0** | ⛔ belgesiz 7,9 | Ⓥ 5,8 karesiz | ⛔ belgesiz **10,0** | Ⓥ 8,8 karesiz | ⛔ belgesiz **2,8** | **8/8** · 4'ü RUN INCOMPLETE |
| BEFORE NIGHTFALL | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ |
| THE OLD ROAD ⭐ yatay | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 16.09.2026 · ilk 16:9 film) |
| THE HIDDEN OASIS | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 16.09.2026 · ilk restorasyon) |
| THE NARROW GORGE | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 16.09.2026 · ilk kurgu yakınlaşması) |
| THE LAST CIRCLE | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 17.09.2026 · ilk kayar kalıp · tek hareket S6'da) |
| THE BORROWED HILL ⭐ yatay 4 dk | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 17.09.2026 · 24 × 10,0 · ilk 4 dk · ikinci Mars sahası) |
| ONE MORE TURN | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 18.09.2026 · 6 × 8,0 · ilk su çarkı · ⭐ ilk rejim G gerçek zaman) |
| THE SWALLOWED BUS | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 19.09.2026 · 7 × 8,0 · ilk şehir içi altyapı onarımı · ⭐ ikinci aşağı bakış · ikinci rejim G) |
| THE TIDE GATE | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 22.09.2026 · 7 × 8,0 · ilk fırtına seddi · ⭐ dikey havuzun ilk YATAY filmi · üçüncü rejim G · üçüncü müziksiz) |
| **THE GLASS CROSSING** | Ⓥ 8,9 | **8,1** | Ⓥ 10,0 | Ⓥ 8,5 | Ⓥ 8,7 | Ⓥ 10,0 | Ⓥ 9,1 | **9,2** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · DÖRT TANE 10/10 · ASGARİ SET TAM (① 8,9 · ② 8,1 · ⑤ 8,7) · ⛔ VİNÇ İHLALİ |
| **THE MOUNTAIN CROWN** | Ⓥ 8,1 | **7,3** | Ⓥ 5,7 | Ⓥ 6,9 | Ⓥ 5,6 | Ⓥ 6,4 | Ⓥ 7,0 | ⛔ belgesiz 6,0 | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · ASGARİ SET DÜŞTÜ (② 7,3 · ⑤ 5,6) · ⛔ BİTİŞ KARTI İHLALİ · ⛔ SİHİRLİ OYMA |
| **THE LAST HARBOR** | Ⓥ 9,8 | **10,0** | Ⓥ 9,8 | **9,5** | Ⓥ 10,0 | Ⓥ 9,4 | Ⓥ 10,0 | **10,0** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · ALTI TANE 10/10 · ASGARİ SET TAM (① 9,8 · ② 10,0 · ⑤ 10,0) · ORTALAMA 9,79 |
| **THE FIRST GUEST** | Ⓥ 9,3 | **9,3** | **10,0** | **9,6** | Ⓥ 9,4 | **10,0** | Ⓥ 10,0 | **10,0** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · ALTI TANE 10/10 · ASGARİ SET TAM (① 9,3 · ② 9,3 · ⑤ 9,4) |
| **THE LAST FIRING** | Ⓥ 9,4 (33 kare) | **10,0** | Ⓥ 8,9 | **8,0** | Ⓥ 10,0 | **9,7** | Ⓥ 8,8 | **10,0** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · YEDİ TANE 10/10 · ASGARİ SET TAM (① 9,4 · ② 10,0 · ⑤ 10,0) · ORTALAMA 9,57 (8 mercek: 9,35) |
| **THE LAST LIFT** | Ⓥ 9,7 | **9,9** | Ⓥ 9,8 | Ⓥ 9,6 | Ⓥ 10,0 | **10,0** | Ⓥ 9,6 | **10,0** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · YEDİ TANE 10/10 · ASGARİ SET TAM (① 9,7 · ② 9,9 · ⑤ 10,0) · 🏆 REKOR ORTALAMA 9,83 |
| THE LONG SHADOW v2 | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 28.09.2026 · 7 × 8,0 · ⭐ ilk GÖLGE filmi · ⭐ ilk BİRİMSİZ defter (ORAN · beşinci tür) · ⭐ tarihi hesaptan çıkan ilk film (ekinoks sabiti 4,1413 m) · ⭐ son yükseklik türetilmiş (11,34 m) · konu ajandan, üç öneriden ajanın önerisi seçildi · dokuzuncu DİKEY · ⭐ v1'in YENİDEN PLANI: v1 üretildi, 4/4 mercek düştü, yayınlanmadı) |
| **BACK TO PLUMB** | Ⓥ 6,8 (32 kare) | **8,4** | Ⓥ 9,1 | **6,1** | Ⓥ 8,3 karesiz | **9,6** | Ⓥ 8,2 | **9,3** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · ASGARİ SET TAM (① 6,8 · ② 8,4 · ⑤ 8,3) · ORTALAMA 8,80 (8 mercek: 8,23) · ⛔ FINAL BEAT FAIL · ⛔ §3 ÇATLAK SIVANMASI |
| THE GLASS WALL ⭐ yatay | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 28.09.2026 · 12 × 10,0 · YATAY ailesi) |
| THE STONE TOWER | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 30.09.2026 · 7 × 8,0 · DİKEY ailesi · kuru taş gözetleme kulesi) |
| THE IRON BRIDGE ⭐ yatay | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 30.09.2026 · 12 × 10,0 · YATAY ailesi · tek açıklıklı çelik kemer yaya köprüsü) |
| THE DEEP STEP | — | — | — | — | — | — | — | — | **0/8** · ⛔ ÜRETİLMEDİ (plan 30.09.2026 · 7 × 8,0 · ZEMİN ailesi · yeraltı basamaklı su kuyusu / stepwell) |
| **THE DEEP END** | Ⓥ 9,6 (21 kare) | **10,0** | Ⓥ 10,0 | **9,9** | Ⓥ 10,0 | **9,4** | Ⓥ 9,3 karesiz | **10,0** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · YEDİ TANE 10/10 · ASGARİ SET TAM |
| **THE STONE DRAGON** | Ⓥ 6,0 | **9,2** | Ⓥ 9,1 | Ⓥ 5,7 | Ⓥ 3,9 | **9,4** | *V2 Ⓥ 6,5* | 🔴 RED (audit) | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM (⑦/⑧ denetim formatında) · ASGARİ SET DÜŞTÜ (⑤ 3,9) · ⛔ BİTİŞ KARTI İHLALİ |
| **THE VANISHING ROOM** | Ⓥ 8,9 | **10,0** | Ⓥ 10,0 | Ⓥ 9,5 | **9,9** | Ⓥ 9,6 | Ⓥ 8,4 | **9,9** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · BEŞ TANE 10/10 · ASGARİ SET TAM (① 8,9 · ② 10,0 · ⑤ 9,9) |
| **THE BLUE DOOR** | Ⓥ 8,6 | **9,7** | Ⓥ 10,0 | **9,2** | Ⓥ 9,3 | **9,2** | Ⓥ 10,0 karesiz | ⛔ belgesiz 9,5 | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · DÖRT TANE 10/10 · ASGARİ SET TAM |
| **THE EMPTY LOCK** | Ⓥ 7,5 (60 kare) | **10,0** | Ⓥ 10,0 | ⛔ belgesiz 6,8 | Ⓥ 7,0 | ⛔ belgesiz 9,5 | Ⓥ 9,9 karesiz | **10,0** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · YEDİ TANE 10/10 · ASGARİ SET TAM |
| **THE BROKEN CLIMB** | Ⓥ 4,1 (33 kare) | **10,0** | Ⓥ 9,9 | ⛔ kapaksız 5,1 | Ⓥ 10,0 | **9,9** | Ⓥ 10,0 karesiz | **10,0** | **8/8** + ⑨⑩⑪⑫ · ⭐ 12 MERCEK TAM · SEKİZ TANE 10/10 · ASGARİ SET TAM |
| **THE QUIET FIELD** | Ⓥ 9,8 (58 kare) | **10,0** | Ⓥ 10,0 | ⛔ belgesiz 8,4 | Ⓥ 10,0 karesiz | ⛔ belgesiz **10,0** | Ⓥ 9,0 karesiz | **10,0** | **8/8** + ⑨⑩⑪⑫ · ⭐ DEPONUN EN İYİ FİLMİ · 12 MERCEK TAMAMLANDI |
| **BACK TO WATER** | Ⓥ 5,8 (33 kare) | **9,3** | Ⓥ 9,4 | ⛔ belgesiz 7,1 | Ⓥ 9,7 karesiz | ⛔ belgesiz 9,9 | Ⓥ 10,0 karesiz | ⛔ belgesiz 9,2 | **8/8** + ⑨⑩⑪⑫ · 4'ü RUN INCOMPLETE |
| **THE DARK ROCK** | ⛔ V karesiz 4,9 | ⛔ belgesiz 3,8 | Ⓥ 2,8 | ⛔ belgesiz 6,1 | Ⓥ 3,1 karesiz | ⛔ belgesiz 2,9 | ⛔ karesiz 5,1 | ⛔ belgesiz 4,5 | **8/8** + ⑨⑩⑪⑫ · 12'si de RUN INCOMPLETE |
| **THE EMPTY RIDGE** | Ⓥ 2,8 | ⛔ belgesiz 5,2 | **5,4** | ⛔ belgesiz 3,4 | Ⓥ 7,2 karesiz | ⛔ belgesiz 7,6 | Ⓥ 7,0 karesiz | ⛔ belgesiz **9,1** | **8/8** + ⑨⑩⑪⑫ · 11'i RUN INCOMPLETE · ⛔ günlüksüz üretim |
| **OVER THE WALL** | Ⓥ 5,8 | ⛔ belgesiz 3,8 | Ⓥ 6,0 | ⛔ belgesiz 5,3 | Ⓥ 3,0 karesiz | ⛔ belgesiz 7,0 | Ⓥ 3,8 karesiz | ⛔ belgesiz **0,0** | **8/8** + ⑨⑩⑪⑫ · 11'i RUN INCOMPLETE · ⛔ günlüksüz üretim |
| **POLAR HABITAT** | Ⓥ 7,7 | ⛔ belgesiz | Ⓥ 9,8 | ⛔ belgesiz | Ⓥ 10,0 | ⛔ belgesiz | Ⓥ 7,9 | Ⓥ 8,2 | **8/8** |

```
⚠️ THE LONG SHADOW v1'in ⑤ ve ⑥'sı KOŞULMADI çünkü o iki mercek film
   ölçüldükten SONRA açıldı. v1 arşivdir ve yeniden ölçülmeyecek — ama
   raporlarında ikisinin de malzemesi zaten var:
     ⑤'in konusu: "crane switches from grey flat-top to blue saddle jib"
                   (② kat.7) · "materials and vehicles morph" (① kat.8)
     ⑥'nın konusu: "cut 1 to cut 2 reverses time entirely" (③ kat.7)
   İki mercek de v1'de ayrı ayrı sorulsaydı bu bulgular DAHA ERKEN ve
   DAHA NET çıkardı. Açılma sebepleri budur.

⚠️ ⑦ İŞ ve ⑧ YÖNTEM dört filmin dördünde de KOŞULMADI — 07.09.2026'da,
   proje sahibinin isteğiyle açıldılar: "durmadan inşa" ve "her parça
   sıfırdan, yapımı görünerek". Malzemeleri eski raporlarda zaten var:
     ⑦'nin konusu: "workers hold frozen poses for the whole clip" (① kat.8)
     ⑧'in konusu: ② APPEARING hükmü dört filmde dört kez — ama hangi PARÇA
                  belirdi, hiçbir rapor adıyla yazmadı. ⑧ onu adıyla yazar.
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
🔴 THE DUST YEAR — ALTINCI FİLM · İLK MARS SAHASI · ⑧ DEPONUN EN DÜŞÜK SKORU
   ⛔ Film ARAÇ KAPISI KOŞULMADAN üretildi; üretim günlüğü hâlâ "DURUM ⛔ BOŞ".
      İzi ölçülebilir: ① dört istasyon grubu (tek istasyon beyan edilmişti) ·
      teslim ızgarası 6·8·4·4·6·4·10·4·6·10 = 62,0 sn, plan 60,0 idi
      (S1↔S2 yer değiştirmiş, S9 8,0 → 10,0).
   ⛔ Düşen: ⑧ APPEARED 0,0/10 — SEKİZ elemanın SEKİZİ "INCOMPLETE at NEVER".
      Yeni INSAAT_YONTEMI kılavuzunun bütün amacı buydu ve plan ona uymuştu;
      sonuç THE LONG DAY'den (1/9 MADE) DAHA KÖTÜ → DERS 36.
      ② DIFFERENT·APPEARING (altıncı kez) · ⑦ PARKED (on klibin sekizi %100
      boş) · ⑤ A SET REBUILT EACH TIME · ⑥ METRONOM (BEŞİNCİ kez — ızgara
      varyanslı olduğu hâlde → DERS 44) · ④ COST/FINAL BEAT FAIL.
   ⭐ Tutan: ⑥ TEXT AND BRANDING 10/10 · ⑤ VEGETATION AND WATER 10/10 ·
      ⑥ CUT MECHANICS 10/10 · DIRECTION 10/10 · ③ "About one year" —
      filmden okunan süre plandaki 1 Mars yılını TUTTU.
   ⭐ Kimse yürüyen insan bildirmedi: DERS 33'ün pozitif yarısı ("No people
      are present.") TUTTU. İnsan makinenin içinden geldi → DERS 41.
   → DERSLER.md: DERS 35-44 · DERS 34'ün kilidi ölçüldü ve düştü.
```

```
🔴 OVER THE WALL — DOKUZUNCU ÜRETİLEN FİLM · İLK BARAJ · 14.09.2026 · ON İKİ MERCEK
   ⛔ Film ÜRETİM GÜNLÜĞÜ TUTULMADAN üretildi (günlük "DURUM ⛔ BOŞ" — DUST YEAR
      ve LONG DAY'den sonra ÜÇÜNCÜ kez [DERS 28]). Kurgu 7 klip · 7,8·8,0·10,7·
      10,0·8,0·13,0·6,0 = 63,5 + kart 4,5 = 68,0 sn; ne 14.09 planına (8 × 8,0)
      ne 12.09 planına (10 sahne) oturuyor. Hangi promptlardan üretildiği
      bilinmiyor. 12 merceğin 11'i RUN INCOMPLETE; yalnız ① kare aldı (69).
   ⛔ Düşen: ⑤ A SET REBUILT EACH TIME (6/6 dikiş) + ⑧ APPEARED 0/4 → film
      "zincir koşulmadı" diye kapanır [kart R 6a]. ② DIFFERENT · APPEARING
      (SEKİZİNCİ kez; POLAR ve CROSSING'in BUILT'inden sonra geri düşüş) ·
      ① SIX SEPARATE SHOTS (plan dışı İKİNCİ İSTASYON, klip 5) · ③ NOT IN ONE
      DIRECTION (kar 4 kez gidip geldi; okunan süre 1,5–2 yıl, plan 1 yıl) ·
      ⑦ PARKED · CAUSE AND EFFECT 0 (duvarda çalışma cephesi YOK, makineler
      köprüde) · ⑩ MAGICAL APPEARANCE · ⑪ INTRUDERS (havuz · derrick kule) ·
      ⑫ MELTING (köprüde çift araç birbirinin içinden geçti).
   ⭐ Tutan: 12/12 END CARD SAME (DERS 30 ilk kez bütün merceklerde) · ① CAMERA
      LOCK 9 · ③ SEASON CARRIER 10 · ④ ENDS + FINAL BEAT PASS + ONE THING
      BULUNDU · ⑥ TIME · ⭐ RHYTHM — ⑤ REBUILT iken İLK KEZ; kurgu varyanslıydı.
      DERS 44'ün tersi ölçüldü; 8 × 8,0 düz kilide karşı kanıt (RAPORLAR §7).
   → DERSLER.md: DERS 51-54 · RAPORLAR/OVER_THE_WALL.md · HAM_RAPORLAR/OVER_THE_WALL/
```

```
⭐ THE EMPTY RIDGE — ONUNCU ÜRETİLEN FİLM · İLK TÜRBİN · 14.09.2026 · ON İKİ MERCEK · DEPONUN EN İYİ ÖLÇÜMÜ
   ⛔ Plan ve üretim aynı gün; günlük TUTULMADI (dördüncü film [DERS 28]). Kurgu 8 klip, varyanslı
      (4,9·3,6·6,3·7,0·10,0·8,1·7,9·8,0); plan 7 × 8,0. ① dört istasyon grubu + klip 1–2 push-in;
      plan tek sabit istasyon. 12 merceğin 11'i RUN INCOMPLETE; ③ tam girdiyle koştu.
   ⭐ İLK KEZ AYNI ANDA: ⑤ SAME WORLD (kanıt = plana konan yalnız meşe — planlı çapa ilk kez bulundu)
      · ⑧ MADE 6/6 · 9,1 (deponun en yüksek ⑧; ilk beliren parça YOK) · ⑫ SOLID (ilk SOLID) ·
      ⑥ TIME · RHYTHM (varyanslı kurgu, 3. kez) · ③ PASSES + süre tahmini "2–3 ay" TUTTU (plan 9,5 hf)
      · ⑨ PRODUCTIVE · 12/12 END CARD SAME.
   ⛔ Düşen: ① SIX SEPARATE SHOTS (kamera hareketi, dört istasyon, SURFACE 1) · ② DIFFERENT (yapı BUILT,
      ama 0:21 ve 0:39'da HAYALET KULE kopyaları) · ⑩ MAGICAL APPEARANCE (segment · nasel · kanat kancasız
      pop; dağ arka planı halatı kurtarmadı) · ⑪ INTRUDERS · ④ NONE FOUND (5.) · RESISTANCE 2 (rüzgâr
      bekleyişi okunmadı) · rotor montajda döndü.
   → DERSLER.md: DERS 55 (çoğul korpus) · 56 (göbek döndürme → rotor döner) · 57 (yük havada taşınmaz;
      DERS 22 mekanizması düştü) · DERS 25 ✅ tuttu · DERS 44 tersi 3. kez · RAPORLAR/THE_EMPTY_RIDGE.md
```

```
⭐ THE QUIET FIELD — ON ÜÇÜNCÜ ÜRETİLEN FİLM · İLK RADYO TELESKOPU · 21.09.2026 · ON İKİ MERCEK (12/12) · DEPONUN EN İYİ FİLMİ
   ⭐ TARİHİ SONUÇ: ① KARE 9,8 · ② İNŞA 10,0 · ③ ZAMAN 10,0 · ④ TESLİM 8,4 · ⑤ DEVAMLILIK 10,0 · ⑥ GEÇİŞ 10,0 · ⑦ İŞ 9,0 · ⑧ YÖNTEM 10,0 · ⑨ FAALİYET 10,0 · ⑩ SEBEP 9,5 · ⑪ ENVANTER 10,0 · ⑫ KATILIK 10,0.
      · ASGARİ SET EKSİKSİZ TAMAM: Kamera kilidi tam (10/10), yapı sıfırdan ve ölçek kilitli (%0,0 sapma, 10/10),
        dünya devamlılığı kusursuz (0/6 kusur, taş ambar 0:00 ve 0:56 kanıtı tuttu, 10/10).
      · FİZİK VE NEDENSELLİK KUSURSUZ: 8/8 eleman sıfırdan yapıldı (⑧ 10/10 MADE); hiçbir sihirli belirme yok
        (⑩ 9,5 CAUSED BY LABOUR); davetsiz nesne yok (⑪ 10/10 INVITED); eriyen/bozulan gövde yok (⑫ 10/10 SOLID).
      · ZAMAN & GEÇİŞ KUSURSUZ: Filmden okunan süre "about one year" plandaki 1 yılla birebir örtüştü; kurgu eşit
        aralıklara (8,0 sn) rağmen Cut 2'deki dramatik mevsim/gece sıçramasıyla RHYTHM hükmünü kazandı.
      · FINAL BEAT PASS: 0:54.0 çanağın 50° güneşe devrilme ödülü ekranda doğrulandı (ENDS).
   ⚠️ Tek kusur: 0:48–0:56 arasında planda olmayan başlık bindirmesi ("THE QUIET FIELD") ekranın üst %40'ına girmiş (Safe Area 8/10).
      Kurguda bu metin katmanı kaldırılmalıdır.
   → RAPORLAR/THE_QUIET_FIELD.md · HAM_RAPORLAR/THE_QUIET_FIELD/
```

```
⭐ THE EMPTY LOCK — ON DÖRDÜNCÜ ÜRETİLEN FİLM · İLK KANAL KİLİDİ · 21.09.2026 · ON İKİ MERCEK (12/12 TAM KOŞU)
   ⭐ ASGARİ SET EKSİKSİZ TAMAMLANDI (① KARE 7,5 · ② İNŞA 10,0 · ⑤ DEVAMLILIK 7,0 — SAME WORLD, Kanıt: White lockkeeper cottage).
   ⭐ YEDİ TANE 10/10 TAM PUAN: ② İNŞA 10,0 · ③ ZAMAN 10,0 · ⑧ YÖNTEM 10,0 · ⑨ FAALİYET 10,0 · ⑩ SEBEP 10,0 · ⑪ ENVANTER 10,0 · ⑫ KATILIK 10,0.
      · İNŞA, YÖNTEM & FİZİK KUSURSUZ: 5/5 eleman yapıldı (⑧ 10/10 MADE); hiçbir sihirli belirme yok (⑩ 10/10 CAUSED);
        davetsiz misafir yok (⑪ 10/10 INVITED); eriyen/bozulan gövde yok (⑫ 10/10 SOLID); 7 nirengide ölçek sapması %0,0 (② 10/10 BUILT).
      · İŞ & FAALİYET ZİRVEDE: ⑦ İŞ 9,9 (en uzun boşluk %0, büyüme yok: NONE) · ⑨ FAALİYET 10,0 (amaçsız aktivite: NONE).
      · ZAMAN KUSURSUZ: Filmden okunan süre "about 10 to 11 hours (one single working day)" plandaki 10 sa 20 dk ile birebir tuttu.
      · ⑥ RİTİM 9,5: 8,0 sn düz ızgaraya rağmen Cut 4'teki meşe kapı montajı, müzik girişi ve Rejim A hız değişimiyle RHYTHM kazanıldı.
      · ④ FINAL BEAT PASS: Yeni kapının suyu tutması ve teknenin geçişi doğrulandı (ENDS).
      · ① TIMELAPSE 7,5: Kamera, nirengi ve istasyon 10/10 kilitli; ufuksuz kadraj (-38° eğim) ZEMİN ailesine tam uydu.
   ⚠️ Üretim kusurları: 0:56.0'da planda olmayan üst %35 başlık bindirmesi (Safe Area 4/10) · Vinçte ve teknede "PAB" harfleri (Text 2/10)
      · 0:40 ve 0:54'te motion blur'suz donuk insan figürleri (People 6/10) · Loop 5/10 (döngü süreksizliği).
   → RAPORLAR/THE_EMPTY_LOCK.md · HAM_RAPORLAR/THE_EMPTY_LOCK/
```

```
✅  koşuldu, skor tabloda
Ⓥ   koşuldu ama mod V (ön koşu) — tamlık için sayılır, skor bağlayıcı değil
❌  koşulmadı
—   üretim yapılmadı, koşulamaz
```

## DURUM

```
BACK TO PLUMB — OTUZ YEDİNCİ FİLM · ⭐ DEPONUN İLK DÜZELTME FİLMİ · ⭐ İLK SAPMA DEFTERİ · ⭐ İLK 'DEĞİŞMEMESİ GEREKEN' ÖLÇÜM · ÖNERİ 28.09.2026 · YAZILDI 28.09.2026 · ÜRETİLDİ VE 12 MERCEKLE ÖLÇÜLDÜ ⭐
   ⭐ 12/12 MERCEK TAMAMLANDI · ÜÇ TANE 10/10 TAM PUAN (⑨ 10,0 · ⑩ 10,0 · ⑫ 10,0) · ASGARİ SET TAM (① 6,8 · ② 8,4 · ⑤ 8,3) · 8 MERCEK ORTALAMASI: 8,23/10 · 12 MERCEK: 8,80/10 · ⛔ §5 FINAL BEAT FAIL (STOPS) · ⛔ §3 ÇATLAK SIVANMASI
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare (G0..G7) + 7 I2V
   YAPI: bir ova çiftliğinin avlusunda YATIK YUVARLAK TUĞLA TAHIL KULESİ — h 9,60 m, dış çap 3,20 m,
      duvar 0,35 m, konik kiremit şapka, gövde 30,08 m³ = 57,2 t. Yatıklık 5,00°, tepe taban
      ekseninden 0,837 m kaçık. Sebep kadrajda görünür: tek sıra DONATISIZ tuğla ayak halkası.
      ⭐ HİÇBİR ŞEY İNŞA EDİLMEZ, HİÇBİR ŞEY YIKILMAZ — altı kuyu, iki parça çelik taban kirişi,
      altı 20 t kriko, kademeli kaldırma. ⭐ KALKIŞ TÜRETİLDİ: 0,2800 m = 3,20 × tan 5,00°.
      ⛔ Vinç yok, iskele yok, kuleye hiçbir şey eklenmez — bütün iş taban kotunun ALTINDADIR.
   KAYNAK: Sahip "dikey 3 yeni konu öner" dedi. Ajan üç DİKEY konsept sundu (BACK TO PLUMB (SAPMA) ·
      THE GAP CLOSES (UZUNLUK) · THE LAST CAIRN (HACİM)) ve ①'i önerdi; sahip "senin önerine başla"
      dedi, ajan sahne sahne öneriyi sundu, sahip "hazırla" dedi. ⭐ Konu ajandan.
   ⭐ DEFTER (SAPMA · altıncı tür): konik şapkanın ucunun x'i − taban halkası merkezinden inen düşeyin x'i.
      64,6 → 55,0 → 46,0 → 37,0 → 27,0 → 18,0 → 9,0 → 0,0 px. Yedi adım: 9,6 · 9 · 9 · 10 · 9 · 9 · 9.
      ⛔ Kesinlikle azalan, eksiye geçmez, G7 = 0,0 ± 2 px filmin TANIMIDIR.
   ⭐ ÜÇ ÖLÇÜM: ① defter AZALIR ② yeni tuğla kaması BÜYÜR (0 → 26 px) ③ eski çatlak HİÇ DEĞİŞMEZ (4,6 px).
      ③ deponun ilk 'sabit kalması gereken' ölçümüdür: kule doğrulmuş ama yarılmışsa film düşer.
   ⛔ ROLL KAPISI: şapkanın ucu kadraj merkezinin 563 px üstünde → roll 0,2° tek başına 1,97 px yalancı
      kaçıklık üretir (bir adımın beşte biri). Ölçüm kuleden değil, iki DIŞ düşeyden yapılır (ahşap direk
      x% 10,0 · ahır köşesi x% 82,0; taban 778 px → eğim farkı ≤ 2,71 px). ⛔ Döndürerek kurtarma YOK,
      ⛔ yazılım stabilizasyonu YASAK. Bu deponun ilk 'kadrajın kendisi ölçü aletidir' filmidir.
   SAHA: 41°K · ekim başı (δ −5°) · gün 11 sa 25 dk · pencere 07:00 → 15:30 · ışık günü 8 sa 30 dk
      istasyon h +1,60 m · d 14,00 m · bearing 340° · tilt 6° yukarı · roll ⛔ 0 · 24 mm
      ⛔ güneş azimutu 104° → 240°, kadraj 313,4° … 6,6° — hiçbir karede kadraja girmez
   REJİM: B × 4 + A × 3 (iki rejim) · ⛔ rejim G yok · ⭐ ikinci saat: kulenin kendi gölgesi
      (69,2 → 10,4 → 22,0 m; sabah kadrajın solundan, öğlen tam arkadan, ikindi sağından)
   ⚠️ BEYAN EDİLEN ZAYIFLIK: final görsel olarak deponun en sessiz karesidir ('düz bir kule').
      120 px küçük resimde kama 2,9 px kalır. ⛔ Kırpma, kontrast itmesi ve ikinci açı ile
      kurtarılmaz; kapak dosyası §1 bunu ölçerek kaydeder.
   DOSYALAR: dikey_shorts/BACK_TO_PLUMB/ — PLAN (992 satır) · QA_SPEC (304) · KAPAK (130)
   KAPI: prompt_kontrol.py → ⚠️ FIX 2 (ikisi de beyanlı: ARAÇ KUTU SETİ ölçülmedi · ⑥ METRONOM) · BLOCK 0
   ⭐ ÜRETİLDİ: 12 mercek raporlandı (QA/RAPORLAR/BACK_TO_PLUMB.md) · asgari set tam · defter G0→G7 tuttu · ⛔ §3 çatlak sıvanması ve §10 müzik ihlali tespit edildi
   ⛔ YAYIN: LONG SHADOW v2 (DİKEY) ile ARDIŞIK YAYINLANAMAZ — araya DİKEY olmayan bir film girmeli.

THE LONG SHADOW v2 — OTUZ ALTINCI FİLM · ⭐ DEPONUN İLK GÖLGE FİLMİ · ⭐ İLK BİRİMSİZ DEFTER (ORAN) · ⭐ TARİHİ HESAPTAN ÇIKAN İLK FİLM · ÖNERİ 27.09.2026 · YAZILDI 28.09.2026 · ⛔ ÜRETİLMEDİ
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare (G0..G7) + 7 I2V
   YAPI: eski bir tepe kasabasında 3,60 m'lik aralık sokağa sıkışmış ÜÇ KATLI DOLGU EV — parsel
      12,00 × 6,40 m, iki yanında tek katlı taş depo (saçak 3,60 m), iki blok ayırma duvarı,
      prekast merdiven çekirdeği (tek kaldırma), iki CLT kat kaseti, çatı kaseti, taş harpuşta.
      ⭐ SON YÜKSEKLİK SEÇİLMEDİ, TÜRETİLDİ: 11,34 m = 7,20 + 3,60 × cot 41° = 7,20 + 4,1413.
      ⛔ Dış iskele YOK, vinç kadrajda YOK (sokak 3,60 m) — ağır parçalar meydandaki bomdan tek zincirle iner.
   KAYNAK: Sahip "yeni 3 öneride bulun" dedi. Ajan üç DİKEY konsept sundu (LONG SHADOW · GAP CLOSES ·
      LAST MAST), her birinin defter cinsini ve ÖLÇÜLMÜŞ riskini yazdı ve ①'i önerdi. Sahip
      "önerini hazırla" dedi; sahne sahne öneri sunuldu; sahip "hazırla" dedi.
   KAMERA: h +1,60 m · d 18,00 m (parsel merkezi) · bearing 270° (batı) · tilt 6° YUKARI · roll 0 · 24 mm.
      Ufuk %42,993 = 825 px — ⭐ GÖRÜNMEZ: gökte değil, iki saçak hattının birleşeceği noktada.
   ⭐ DEFTER (beşinci tür · ORAN · BİRİMSİZ): gölge çizgisinin karşı duvardaki yüksekliği ÷ o duvarın
      kendi yüksekliği, aynı karede aynı sütunda iki px uzunluk:
      0,000 · 0,094 · 0,323 · 0,546 · 0,698 · 0,848 · 0,955 · 1,000  (±0,006) — kesinlikle artan.
      ⭐ Ham px defteri sahnelerin SIRASINI değiştirirdi (S4 180 px ile en büyük görünür, oysa duvar
      en çok S1'de kaybeder: 0,228). Bant 27,50 m'den 13,40 m derinliğe kayar, px/m 46,3 → 93,7.
   ⭐ EKİNOKS: δ = 0'da doğu-batı bir duvara düşen gölge çizgisinin düşüşü GÜN BOYU SABİTTİR ve yalnız
      enlemden gelir: 3,60 × cot 41° = 4,1413 m (06:02'de de 17:58'de de aynı; min = maks, ölçüldü).
      Güneş deftere hiçbir şey katmaz; çizgiyi yalnız inşaat yükseltir. Ekinoks MENTEŞE GÜNÜDÜR:
      o günden 21 Mart'a kadar karşı duvar hiçbir saatte güneş almaz (mevsim tablosu planda).
   IŞIK: 41°K · ekinoks · gün 12 sa · pencere 08:00 → 14:40 = 6 sa 40 dk · rejim B × 3 + A × 4.
      Güneş azimut 111° → 232°, kadraj 243,4° … 296,6° → hiçbir karede kadrajda değil (pay 51 dk).
   SES: ⛔ müzik yok · tam diegetik · ⭐ 3,60 m'lik sokağın 21 ms'lik tek yankısı filmin imzası.
   SİLUET: DİKEY (dokuzuncu) · ızgara DİKEY 9 · ZEMİN 6 · KÜTLE 7 · YATAY 2 · LAST LIFT KÜTLE'den sonra ✅
   DOSYALAR: dikey_shorts/THE_LONG_SHADOW_V2/ → _DIKEY_TIMELAPSE.md (961 satır) · _QA_SPEC.md (263) · _KAPAK.md (132)
   KAPI: prompt_kontrol.py → FIX 2 (ikisi de beyanlı: düz ızgara [DERS 13], araç kutu seti ölçülmedi) · BLOCK 0
   ⛔ ÜRETİLMEDİ: araç kapısı koşulmadı · tek kare üretilmedi · pilot görsel test edilmedi
   ⭐ PİLOT: G7 (defter 1,000 · |pay − payda| ≤ 2 px — tutmazsa BÜTÜN PLAN yeniden yazılır) +
      S0 klibi (defter 7,45. sn'de açılıyor mu) + G2/G4 (20 dakikada gölge yönü değişmemeli)
   ⭐ v1 BAĞI: bu film deponun İLK FİLMİNİN yeniden planıdır. v1 üretildi, dört merceğin dördü de
      düştü (① 3,3 ALTI AYRI GÖRÜNTÜ · ② 0,4 FARKLI/APPEARING · ③ 4,3 yön kırık · ④ 2,7 DURUYOR)
      ve karar 'yeniden planlanıp yeniden üretilir' idi. Planın §v1'İN CEVABI bölümü v1'in yedi
      arızasını tek tek karşılar. Havuz satırı 1'in bedeli korundu, ölçülebilir hâle getirildi.
      ⛔ v1'in QA kaydı ayrıdır (matriste 'THE LONG SHADOW v1'); klasör adı bu yüzden _V2'dir.
   ⚠️ v1'in plan dosyası (dikey_shorts/THE_LONG_SHADOW/, 791 satır) KANIT OLARAK YERİNDE DURUYOR ve
      dokunulmadı. v2 ayrı klasördedir (_V2). ⛔ v1'in kendi içindeki 'v2 şöyle yazılacak' notu
      (10 sahne × 6 sn + 5 sn kapak kartı = 65 sn) ARTIK GEÇERSİZDİR: sahne süresi 8,0 sn ve
      video içi kapak kartı yok — ikisi de sonraki sahip kuralları (19.09.2026 · 21.09.2026).
   ⭐ DERS: P20-a…g [kilavuzlar/DERSLER.md]

THE LAST LIFT — OTUZ BEŞİNCİ FİLM · ⭐ DEPONUN İLK STADYUM FİLMİ · ⭐ İLK 260M ÇELİK UZAY KAFES ÇATI VE STRAND JACK LİFTİ · ⭐ ÜRETİLDİ VE ÖLÇÜLDÜ (12/12 QA) — 28.09.2026
   🏆 DEPO REKORU: 9,83 / 10 GENEL ORTALAMA · YEDİ MERCEKTE TAM 10/10 (⑤ ⑥ ⑧ ⑨ ⑩ ⑫ + ⑥ 120 BPM senkronu) · RAPOR: QA/RAPORLAR/THE_LAST_LIFT.md
   dikey_shorts · ızgara 10 × 6,0 = 60,0 sn · hızlandırılmış 44,0 sn master · 120 BPM müzik · zincirli · 11 kare (G0..G10) + 10 I2V
   YAPI: 60.000 kişilik stadyum çanağı + 260m çelik uzay kafes çatı (strand jack ile 4 geçici kafes kuleden kaldırılır).
   KAYNAK: Sahip "viral bir timelapse dikey shorst planlarmısın" dedi. Ajan 3 konsept sundu (stadyum seçildi), kullanıcı başlığı "THE LAST LIFT" olarak seçti.
   KAMERA: h +45,0m · D_kenar 120,0m · D_eksen 220,0m · bearing 315° (KB) · tilt -25° (aşağı) · roll 0° · 24mm. Ufuk tabandan 1557 px (%81,09), üstte 363 px dağ sırtı ve açık gök.
   DEFTER: Çatının yükseliş defteri (S0-S4 zemin/çanak, S5 çatı montajı zemin kotunda +3,0m, S6 kaldırma başlar +18,0m, S7 kaldırma biter +54,0m, S8 kilit + membran, S9 zemin/çim, S10 tamamlandı).
   DOSYALAR: THE_LAST_LIFT_DIKEY_TIMELAPSE.md (791 satır) · _QA_SPEC.md (260 satır) · _KAPAK.md (180 satır)
   KAPI: prompt_kontrol.py -> FIX 2 (beyanlı: düz ızgara [DERS 13], araç kutu seti ölçülmedi) · BLOCK 0
   ⭐ PİLOT: G10 (usta kare) + G6 (kaldırma anı) + G5 (zemin montajı)

THE LAST FIRING — OTUZ DÖRDÜNCÜ FİLM · ⭐ İLK YANMA FİLMİ · ⭐ İLK TAM EL İŞİ YAPIMI · ⭐ DEFTERİ KADRAJIN DIŞINA KAPANAN İLK FİLM · ⭐ İLK İKİ YÖNLÜ DEFTER · YAZILDI 26.09.2026 · ÜRETİLDİ VE 12 MERCEKLE ÖLÇÜLDÜ ⭐
   ⭐ 12/12 MERCEK TAMAMLANDI · YEDİ TANE 10/10 TAM PUAN (② 10,0 · ⑤ 10,0 · ⑧ 10,0 · ⑨ 10,0 · ⑩ 10,0 · ⑪ 10,0 · ⑫ 10,0) · ASGARİ SET TAM (① 9,4 · ② 10,0 · ⑤ 10,0) · FINAL BEAT PASS (8/10) · ORTALAMA: 9,57/10
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare + 7 I2V
   YAPI: elle örülen TARLA TİPİ KİREÇ OCAĞI — dış Ø 3,40 m · tepe +2,20 m · korbelli taş kubbe ·
      iç yanma odası Ø 2,40 × 1,60 m · ateş ağzı 0,60 × 0,80 m · tepede Ø 0,55 m baca gözü ·
      kil + saman sıva 0,10 m (23,50 m² → 2,35 m³). ⭐ Kemer KUM KALIBIN üstüne örülür ve kum ateş
      ağzından kürekle çıkarılır (3,00 → 3,45 m³ kabarmış; kadrajda ÖNLÜK olarak kalır, geri dönmez).
      YÜK 8,98 m³ dizili kireçtaşı = 15,8 t. ⭐ CaCO3 15,8 t → CaO 8,83 t + CO2 6,93 t (%43,97 GAZ).
      İş: serilir → kalıplanır → örülür → yüklenir → tutuşur → yanar → açılır.
   KAYNAK: sahip "yeni bir konu bulalım öneride bulun 3 tane" dedi. Ajan üç KÜTLE konusu sundu —
      ① THE LAST TERRACE (denklik defteri · su saati) ② AWAY FROM THE EDGE (mesafe defteri · ⛔ ana
      yapı kımıldıyor, RİSKLİ işaretlendi) ③ THE LAST FIRING (görünmez defter · ateş saati). Sahip
      "the last fırıng olsun" dedi; ajan sahne sahne öneri sundu; sahip "onay" dedi.
   KAMERA: ısı paravanının gerisinde sabit sehpa · h +2,00 m · d 8,50 m (kubbe merkezi) · d 6,80 m
      (ön yüz) · bearing 340° · ⭐ TİLT 6° AŞAĞI · roll 0 · 24 mm · KAMERA_DILI §3.
      ⭐ UFUK KADRAJDA VE CETVEL: %57,007 = tabandan 1095 px · üstte 825 px açık gök.
      kare dibi d 2,15 m · optik eksen d 19,03 m · kadraj eni = d = 8,50 m → yatay 127,06 px/m ·
      dikey ocakta 148,9 px/m → ⭐ ayrıntı tabanı 0,23 m (DEPONUN EN YAKIN İSTASYONU).
      ⭐ h SEÇİLMEDİ, HESAPLANDI: kubbenin kapanmadan önceki son yüksekliğine EŞİT → G3 defteri TAM SIFIR.
   ⭐ DEFTER (dördüncü tür · İŞARETLİ MESAFE · iki yönlü): ocağın tepesi ile ufuk arasındaki fark
      G0 −246 · G1 −165 · G2 −83 · G3 ⭐0 · G4 ⭐+31 · G5 +18 · G6 −33 · G7 −36 px (±2 px)
      ⛔ G0→G4 KESİN ARTAR (örülüyor) · ⛔ G4→G7 KESİN AZALIR (yanıyor) · dönüm G4 = ateşin verildiği kare
      ⭐ Defterin biçimi ile filmin biçimi aynı biçimdir. Toplam oturma 0,44 m = 67 px (tam yanmanın %71'i).
      ÇAPRAZ DEFTER: kum önlüğü 831 × 132 px — G2'de belirir, hiçbir karede küçülmez.
   KADRAJ: kubbe 432 × 328 px (%40,0 en · taban 797 px) · yaşlı incir 234 × 488 px (%x 9,17–30,83,
      tacı ufkun 276 px üstünde) · ateş ağzı 95 × 145 px · ham bant 143 × 90 px (sol etek, G4→G7) ·
      baca gözü 87 px (⛔ küçük resimde 9,7 px, okunmaz — beyanlı) · taş yığını 576 × 199 px (G0–G2).
   IŞIK: 43°K · δ +12° · gün 13 sa 32 dk (05:14 → 18:46) · pencere 06:00 → 18:10 = 12 sa 10 dk ≤ 14 ✅
      rejim B × 6 + ⭐ A × 1 (iki rejim) · ⛔ REJİM G YOK [P16-g]
      yakın yüz katsayısı 0,192 · 0,460 · 0,567 · 0,484 · 0,233 · 0,000 · 0,000 · 0,000
      ⭐ ocağın kendi saati (kor) 0,00 · 0,00 · 0,00 · 0,00 · 0,02 · 0,30 · 0,80 · 1,00
      ⭐ İKİ SAAT S4'ün 3,32. saniyesinde KESİŞİR (≈14:50) · güneş yakın yüzü 5,41. saniyede terk eder (15:21)
      ⛔ Güneş hiçbir karede kadraja girmez (kadraj 313,4°…6,6°, azimut 81° → 281°).
   SES: ⭐ TAM DİEGETİK (hava var) — taş, kürek, mala, çalının tutuşması, çekiş uğultusu, kilin çatlaması.
      Ölçülebilir iddia: 51,0–53,5'te RMS, 40,0–48,0 ortalamasının ≥ 6 dB üstünde, enerjinin ≥ %70'i < 200 Hz.
   SİLUET: KÜTLE (altıncı) · FIRST GUEST ⭐ZEMİN → LAST FIRING KÜTLE ardışık yayınlanabilir
      ⛔ NARROW GORGE · ONE MORE TURN · BACK TO WATER · BLUE DOOR · MOUNTAIN CROWN ile olmaz
      Izgara DİKEY 8 · ZEMİN 6 · KÜTLE 6 · YATAY 2
   DOSYALAR: THE_LAST_FIRING_DIKEY_TIMELAPSE.md (892 satır) · _QA_SPEC.md (238) · _KAPAK.md (123)
   KAPI: prompt_kontrol.py → ⚠️ FIX 2 (ikisi de BEYANLI: ⛔ kutu seti ölçülmedi · ⑥ METRONOM) ·
      ⛔ BLOCK 0 · MOTION FOCUS FIX 0 · prompt uzunlukları 4 980 – 5 143
   ⭐ ÜRETİLDİ: 12 mercek raporlandı (QA/RAPORLAR/THE_LAST_FIRING.md) · asgari set tam · defter sıfır sapmayla tuttu · 8 mercek ortalaması: 9,35 / 10 · 12 mercek ortalaması: 9,57 / 10
   ⭐ PİLOT: G3 + G4 (|defter(G3)| ≤ 2 px) — tuttu (|defter(G3)| = 0 px, |defter(G4)| = +31 px)
   DERSLER: P19-a…g

THE FIRST GUEST — OTUZ ÜÇÜNCÜ FİLM · İLK HAVASIZ SAHA FİLMİ (GÜNCEL KONTRATLA) · ⭐ ÖLÇEĞİ BİLEREK SAKLAYAN İLK FİLM · ⭐ İLK TEK REJİMLİ FİLM · ⭐ FİKİR SAHİPTEN · YAZILDI 26.09.2026 · ÜRETİLDİ VE 12 MERCEKLE ÖLÇÜLDÜ ⭐
   ⭐ 12/12 MERCEK TAMAMLANDI · ALTI TANE 10/10 TAM PUAN (③ 10,0 · ⑥ 10,0 · ⑦ 10,0 · ⑧ 10,0 · ⑩ 10,0 · ⑫ 10,0) · ASGARİ SET TAM (① 9,3 · ② 9,3 · ⑤ 9,4) · FINAL BEAT PASS (9/10) · ORTALAMA: 9,66/10 · ⚠️ HAVASIZ SAHADA ASILI TOZ SAPMASI (⑪ 8,5)
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare + 7 I2V
   YAPI: havasız bir ayda, BAŞKASININ YAPTIĞI 160,00 m'lik kesme kaya kapısının önüne kurulan 4,50 m'lik
      İNSAN GEÇİŞ KİLİDİ — iki tarafın kıyafet çıkarmadan buluşabileceği tek oda. Pad 14,00 × 10,00 m,
      0,60 m kazılıp SİNTERLENMİŞ cam taban · 6 kavisli kaburga · panel + gergin dış örtü · gövde
      6,00 × 5,00 m, kapısı 2,40 × 2,60 m ve KARŞI KAPIYA BAKAR · gemiden 3 sehpalı göbek bağı.
      Karşısında 12,00 × 12,00 m'lik KARE SERVİS GEÇİDİ (kadrajda 216 × 315 px — insan kilidinin 2,08 KATI).
      ⛔ KAPININ TEPESİ HİÇBİR KAREDE GÖRÜNMEZ: d 60,00'da kadrajın üst kenarı yalnız y = +17,01 m'ye ulaşır.
   KAYNAK: sahibin yapıştırdığı 4 dakikalık, iki karakterli, anlatılı bilim-kurgu fikri ("İLK MİSAFİR":
      genç keşifçi, dev muhafız, ritimle kurulan selamlaşma, ayın iç yüzeyindeki şehir). Ajan ÜÇ ÇARPIŞMA
      bildirdi: ① 4 dk anlatı · iki kostüm · mekân değiştiren kesme · kamera hareketi — dördü de formatın
      kendisine aykırı ② ⛔ FİKİRDE İNŞAAT YOK (üst üste üçüncü kez) ③ dev şehir reveal'ı tek kadrajda
      gösterilemez. Ajan fikrin TEK timelapse'lik görüntüsünü aldı — ⭐ ÖLÇEK YANILGISI ("sütun sandığımız
      şey bir bacak") — ve altına gerçek bir yapım işi koydu: misafirin BAŞKASININ KAPISININ ÖNÜNE
      KENDİ KAPISINI kurması. Muhafız GÖVDE olarak değil, GÖLGE olarak kaldı (aşağıda).
      Sahip 26.09.2026'da "oney" dedi.
   KAMERA: iniş gemisinin direğinde sabit tripod · h +14,00 m · d_yüz 60,00 m · ⭐ D_eksen 39,00 m ·
      d_sütun 44,00 m [DERS 38] · bearing 270° · ⭐ TİLT 34° AŞAĞI · roll 0 · 24 mm · KAMERA_DILI §3.
      ⛔ KADRAJDA GÖK YOK, UFUK YOK, KARA YOK. Kadrajı kapatan şey kapının KENDİSİDİR (%75,41'den yukarısı).
      kare dibi d 4,86 m · kum bandı %0 → %75,41 = 1 448 px · px/m yatay d38 28,42 · d60 18,00 · dikey 31,9
   BEDEL: ⭐ DOKUNULMAMIŞ KUM. G0'da alt 1 448 pikselin TAMAMI milyonlarca yıllık, rüzgârsız, izsiz
      orijinal dalgalı dokudadır. ⭐ Havasız bir ayda hiçbir şey izi SİLMEZ — misafirin ilk yıktığı şey,
      buraya kimsenin gelmemiş olmasıdır.
   DEFTER: ⭐ TEMİZ KUM ALANI (yüzde) 100 · 92 · 71 · 55 · 44 · 38 · 35 · 35 — monoton azalan, G6'da DONAR.
      ⭐ ÜÇÜNCÜ TÜR DEFTER: MOUNTAIN CROWN bir KENAR ölçtü, LAST HARBOR bir SAYI saydı, bu film bir ALAN
      ölçüyor [P18-d]. HACİM: 84,0 m³ katı × 1,20 = 100,8 m³ gevşek → solda 2,25 m yüksek (72 px) yığın;
      hiçbir şey kadrajı terk etmez.
   TANIK: ① ⭐ 11,00 m'lik SERBEST TAŞ SÜTUN (367 × 61 px · %x 15,34 → 21,02) — fikrin "sütunu" budur ve
      hiç dokunulmaz; ilk yarıda GÖLGESİ saattir (182,1 → 63,1 → 41,4 → 34,6 m) ② kapı tabanı çizgisi
      (%75,41 · 1 448 px) ③ dört nervür (%x 5,00 · 35,00 · 50,00 · 58,33)
   ÖDÜL: ⭐ bir nesne değil, bir TEMAS — karşı tarafın ışığının bizim kapımıza ULAŞMASI. G7'de 225 piksellik
      turuncu kama padı geçer ve küçük beyaz kabuğun yakın yüzünü yıkar. Kimse konuşmaz, kimse görünmez.
   ⭐ MUHAFIZ = GÖLGE: G7'de turuncu kamayı baştan sona kesen, ≈120 px eninde, DÜZ KENARLI, AYRINTISIZ
      tek koyu bant. Gövde yok, uzuv yok, yüz yok. Sebep hesaplandı: 12 m'lik bir figür bu kadrajda
      ≈380 px olur ve filmin ÖZNESİ hâline gelir; timelapse ölür, yaratık filmi başlar.
      ⛔ Sekiz görselin ve yedi I2V'nin hiçbirinde yaratık kelimesi GEÇMEZ (tarandı, 0) [P18-g].
   IŞIK: 72° kuzey · δ 0 · ay günü 32 saat · gündüz 16,00 sa · doğuş 04:00 · batış 20:00
      ışık günü 05:00 → 19:00 = ⭐ 7 × 2,00 = 14,00 sa — TAVANIN TAM ÜSTÜNDE, sıfır israf
      kaya yüzü katsayısı 0,981 → 0,831 → 0,556 → 0,195 → 0,000 · kum katsayısı 0,060 → 0,303 → 0,000
      ⭐ İKİ EĞRİ FİLMİN ORTASINDA KESİŞİR: ışık duvardan yere, sonra yerden hiçbir yere gider.
      ⭐ GÖLGE BIÇAĞI: S3 klibinin 4,00 → 6,32. saniyeleri arasında 160 m'lik kayanın gölge kenarı bütün
      kadrajı 2,32 saniyede süpürür ve geçtiği her ışıklı kum sırtı SIRAYLA söner. Havasız → yarı gölge YOK.
      İkinci yarının saati IŞIK KAYNAĞI SAYISI (3 → 4 → 5 → ⭐ 6) ve SIÇRAMA MESAFESİDİR (103 → 2 603 m).
      ⛔ Güneş hiçbir karede kadrajda değil, iki ayrı sebeple: 05:00–12:00 kameranın ARKASINDA,
      13:00–19:00 kayanın ARKASINDA.
   ⭐ SES: deponun ilk DİEGETİK OLMAYAN yatağı. Havasız sahada dışarıda ses yoktur; yatak tamamen kaskın
      içidir (nefes · kumanda · TEMASLA iletilen titreşim). Filmin en büyük görsel olayı (28,0'deki bıçak)
      filmin EN SESSİZ anıdır; en yüksek sesi ise 50,0–53,5'te taş kanadın KUMDAN gelen titreşimidir [P18-e].
   SİLUET: ⭐ ZEMİN (altıncı · HIDDEN OASIS · SWALLOWED BUS · EMPTY LOCK · DEEP END · VANISHING ROOM'dan sonra)
      Izgara DİKEY 8 · ZEMİN 6 · KÜTLE 5 · YATAY 2. LAST HARBOR YATAY → FIRST GUEST ZEMİN ardışık OK.
      ⚠️ KÜTLE bilerek seçilmedi: kadrajı kaplayan bir kaya yüzü MOUNTAIN CROWN'ı tekrarlardı [P18-c].
   DOSYALAR: THE_FIRST_GUEST_DIKEY_TIMELAPSE.md (994 satır) · THE_FIRST_GUEST_QA_SPEC.md (266) ·
      THE_FIRST_GUEST_KAPAK.md (132)
   ⛔ KAPI: prompt_kontrol.py → FIX ×2 (ARAÇ KUTU SETİ ölçülmedi · yedi sahne de 8,0 → ⑥ METRONOM),
      ikisi de BEYANLI · BLOCK 0 · MOTION FOCUS FIX 0 · prompt uzunlukları 5 292 – 5 651
   AÇIK: platform başlığı · ⛔ ses üretim yolu (standart yol YOK — temas iletimli yatak) ·
      ⛔ ARAÇ KUTU SETİ ölçülmedi (üretimi BLOKE ediyor) · kapak varyantı (⭐ bu filmde ⓑ BAŞLIKSIZ
      ÖNERİLMİYOR, kare çok koyu; ⓒ alt başlık "DAY ONE" ciddi aday) · yayın aralığı
   EN BÜYÜK RİSK: ⭐ KOYU BANT (QA_SPEC §1). Model onu bir yaratığa çevirirse film düşer; hiç üretmezse
      final ölür. ⛔ YEDEK PLAN YOK — bandı çıkarmak finali yok eder. Bu yüzden pilot S6'dır.
   PİLOT: G6 → G7 → S6 (koyu bant · deponun modele verdiği en zor tek talimat) → S3 (2,32 saniyede
      bütün kadrajı karartan sert gölge bıçağı) → G0 → G1 → kalanlar
   ⭐ REJİM: 7 × B, TEK REJİM. ⛔ G kullanılmadı [P16-g], A kullanılmadı [P17-d]. Gerekçe: 12 m'lik taş
      kanat dakikalarca kayar; rejim G burada YALAN SÖYLERDİ. ÖLÇÜLMEDİ: yedi eşit sıkıştırma ⑥ merceğinde
      "tekdüze" okunur mu, yoksa ışık eğrisi tek başına yeter mi? [P18-f]

THE LAST HARBOR — OTUZ İKİNCİ FİLM · İLK KAYSON · ⭐ ANA YAPISI İLK KAREDE ZATEN TAM OLAN İLK FİLM · ⭐ İLK REJİM-A FİNALİ · ⭐ FİKİR SAHİPTEN · ⭐ ÜRETİLDİ VE ÖLÇÜLDÜ (12/12 QA) — 28.09.2026
   ⭐ 12 MERCEK TAMAMLANDI · ALTI TANE 10/10 TAM PUAN (② ⑤ ⑦ ⑧ ⑨ ⑩) · GENEL ORTALAMA 9,79 / 10 · FİNAL BEAT PASS 10/10 · RAPOR: QA/RAPORLAR/THE_LAST_HARBOR.md
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare + 7 I2V
   YAPI: adı verilmeyen bir kuzey kıyısında, eski limanın ağzının DIŞINDA, 36,00 × 16,00 × 22,00 m'lik
      hücreli betonarme YÜZER KAYSON → liman kolunun başı. 2 115,2 m³ beton = 5 182 t; 9,00 m su çekiminde
      deplasman 5 314 t (fark +132 t = donatı ve teçhizat payı). Yüzerken fribord 13,00 m; hazır kaya
      yatağının üstü −16,00 m; oturduğunda tepe +6,00 m, kumla 1,00 m gömülür; 1,50 m başlık plağı →
      kret +6,50 m; deniz yüzünde 2,50 m parapet → +9,00 m. 5 baba · sol başta 6,00 m fener direği ·
      sağ uçta geçici kaya bermi. Hücrelere 9 600 m³ kum (3 mavna × 3 200 m³).
      ⛔ KADRAJDA KARA YOKTUR — kıyı kameranın ARKASINDADIR.
   KAYNAK: sahibin yapıştırdığı 4 dakikalık, anlatılı, bilim-kurgu fikri ("SON LİMAN — THE LAST HARBOR":
      fırtınalı gezegen, dev liman, muhafız, limanın aslında bir göç gemisi olduğu ve havalandığı finali).
      Ajan ÜÇ ÇARPIŞMA bildirdi: ① 4 dk anlatı · karakter · mekân değiştiren kesme · kamera hareketi ·
      hava değişimi — beşi de formatın kendisine aykırı ② ⛔ FİKİRDE İNŞAAT YOK: hiçbir şey yapılmıyor,
      eski bir makine uyanıyor; aşama merdiveni, geçici ekipman defteri ve kanıt nesnesi boş kalır
      ③ finalin "kalkış"ı BACK TO WATER'ın (18. film) iskeletini tekrarlar: su yükselir, gövde takozdan
      kalkar, gövde gider. Ajan fikri REDDETMEDİ; bir TERSİNE ÇEVİRME ve bir EKLEME yaptı:
      ⭐ TERSİNE ÇEVİRME — liman gemi çıkıp KALKMAZ; gemi liman çıkıp BİR DAHA HİÇ KIMILDAMAZ.
         BACK TO WATER'da nesne giderek kurtulur; burada nesne KALARAK TÜKENİR.
      ⭐ EKLEME — fikrin şaşkınlığını taşıyan GERÇEK bir yapım işi arandı ve bulundu: kaysonun batırılması.
      Sahip 26.09.2026'da "okeydirr y yap bunu" dedi.
   KAMERA: eski mendireğin başında sabit tripod · h +18,50 m (ortalama deniz seviyesinden) ·
      d_yakın 52,00 m · ⭐ D_eksen 60,00 m · d_uzak 68,00 m [DERS 38] · bearing 310° · ⭐ TİLT 15° AŞAĞI ·
      roll 0 · 24 mm · tilt formülü KAMERA_DILI §3.
      ⭐ İSTASYON SEÇİLMEDİ, ÜÇ SINIRIN KESİŞİMİNDEN ÇIKTI: 36 m'lik kolun iki başıyla kadraja girmesi
      ENİ (d 52,00 → 748 px · %69,23), 7,00 m'lik batmanın en az 150 px okunması YÜKSEKLİĞİ
      (h 18,50 → 169 px), göğün kadrajın üçte birini geçmemesi de TİLTİ (15° → %32,14) belirledi.
      ⛔ TİLT SIFIR OLAMAZDI: denizde tilt 0 demek ufkun HER ZAMAN tam %50'de durması, yani göğün
      kadrajın YARISI olması demektir — geometrik zorunluluk, tercih değil [P17-b].
   BEDEL: ⭐ GEMİLİK — kutunun yüzer olmasına ait ne varsa kadrajda tek tek yok olur:
      ① fribord 13,00 m (304 px) → 6,00 m (136 px) → kumla 5,00 m (113 px)
      ② ⭐ KIRMIZI ZEHİRLİ BOYA BANDI 4,00 m (90 px) — S1'in ilk iki saniyesinde denize girer, BİR DAHA GÖRÜNMEZ
      ③ iki çekme köstek gözü (41 px · %x 26,92 / 73,08) — G7'de durur ama İŞLEVSİZDİR
      ④ iki römorkör — S2'de sağdan çıkar ve DÖNMEZ   ⑤ dört sarı şamandıra — S5'te toplanır
   DEFTER: ⭐ TEK DEFTER — kolun İÇ yakasındaki (kadrajın alt 857 pikseli) kırılan beyaz köpük sayısı:
      G0 7 · G1 7 · G2 5 · G3 4 · G4 2 · G5 1 · G6 0 · G7 0. Hiçbir karede ARTMAZ.
      ÇAPRAZ KONTROL dış bantta: kırılma çizgisi S4'te DIŞARI yürür ve açık deniz bandı 231 → 185 px'e iner.
      ⭐ Enerji yok olmaz, YER DEĞİŞTİRİR — iki bandın ters yönde gitmesi bu filmin fiziğidir.
      ⛔ MOUNTAIN CROWN'ın "iki defter" numarası BİLEREK TEKRARLANMADI [P17-d].
   TANIK: ① eski mendirek başı (%x 10,00 → 90,00 · %y 1,63 → 10,04 · 161 px · kameranın üstünde durduğu taş)
      ② kaya adacığı (x −30,00 · d 66,00 · %x 4,55 · 73 px) ③ ufuk çizgisi (%67,86 · 1303 px)
      ⭐ Bu filmde çapa sorunu deponun en zorudur: kadrajda kara yoktur ve suyun kendisi çapa olamaz.
   ÖDÜL: kolun kendisi değil, KOLUN YAPTIĞI ŞEY — kadrajın alt 857 pikseli dümdüz kararır ve oraya bir
      tekne gelir. ⭐ Ödül bir NESNE değil, bir YOKLUKTUR: dalganın yokluğu.
   IŞIK: 52° kuzey · geç ağustos (δ +10°) · gündüz 13 sa 44 dk · doğuş 05:08 · batış 18:52
      ışık günü 06:00 → 18:10 = 12 sa 10 dk (6 × B + 1 × A · tavan 14,00 · pay 52 + 42 dk)
      iç yüz normali 130° · katsayı 0,686 → 0,834 → 0,740 → 0,430 → 0,000 → 0,000 → 0,000
      ⭐ IŞIK FİLMİN İKİNCİ YARISINDA YÜZÜ TERK EDER VE BU KURGUDUR: son üç karede beton SİLUET,
      arkasındaki deniz GÜMÜŞ PARILTI. Film bir İNŞAAT fotoğrafı olarak başlar, bir DENİZ fotoğrafı
      olarak biter. Güneş hiçbir karede kadrajda değil (pay 5,29°).
   SİLUET: YATAY (ikinci · TIDE GATE'ten sonra) — 748 piksellik tek alçak bant, üstünde 185 px açık deniz.
      ⭐ BEŞ FİLMDİR AÇ KALAN YATAY YUVASI DOLDU. Izgara DİKEY 8 · ZEMİN 5 · KÜTLE 5 · YATAY 2.
      ⚠️ THE TIDE GATE ile araya EN AZ İKİ film girmeli (aynı aile, aynı saha tipi, aynı görsel cümle).
   DOSYALAR: THE_LAST_HARBOR_DIKEY_TIMELAPSE.md (1008 satır) · THE_LAST_HARBOR_QA_SPEC.md (240) ·
      THE_LAST_HARBOR_KAPAK.md (134)
   ⛔ KAPI: prompt_kontrol.py → FIX ×2 (ARAÇ KUTU SETİ ölçülmedi · yedi sahne de 8,0 → ⑥ METRONOM),
      ikisi de BEYANLI · BLOCK 0 · MOTION FOCUS FIX 0 · prompt uzunlukları 5 504 – 5 902
   AÇIK: platform başlığı · ses üretim yolu · ⛔ ARAÇ KUTU SETİ ölçülmedi (üretimi BLOKE ediyor) ·
      kapak varyantı (⭐ ⓑ başlıksız ciddi aday, iki filmdir üst üste) · TIDE GATE ile yayın aralığı
   EN BÜYÜK RİSK: ⭐ filmin bilim-kurguya kaçması. Kaynak metin anlatılı bilim-kurgudur ve "liman"
      kelimesi modelde kule, dev vinç, gökdelen gemi ve şehir çağırır. Kadrajda ALTI nesne vardır ve
      altısı da QA_SPEC §7'de sayılıdır; her kare o listeye karşı okunur.
   PİLOT: G6 → G7 → S1 (batma · modelin "gövde büyür" alışkanlığına ters tek sahne) → S3 (ışığın yüzü
      terk ettiği ve aynı anda yeni malzeme eklenen tek klip) → G0 → G2 → kalanlar
   ⭐ REJİM: 6 × B + 1 × A. ⛔ REJİM G KULLANILMADI — P16-g'nin kendi kaydına uyuldu. Deponun İLK
      rejim-A finali ve ÖLÇÜLMEDİ: 100×'te teknenin çizgisi ve fenerin tek boncuğa dönüşmesi modelde
      sınanmadı; ilk üretimden sonra SANTIYE_HAREKETI §1'e tek satır iner [P17-g · QA_SPEC §8].

THE MOUNTAIN CROWN — OTUZ BİRİNCİ FİLM · İLK KAYA OYMA CEPHE · ⭐ AYNI MADDEYİ İKİ DEFTERDE SAYAN İLK FİLM · ⭐ FİKİR SAHİPTEN · ⭐ ÜRETİLDİ VE ÖLÇÜLDÜ (12/12 QA) — 28.09.2026
   ⭐ 12 MERCEK TAMAMLANDI · DİFÜZYON MODELİNİN EKSİLTMELİ OYMA SINIRLARI · GENEL ORTALAMA 6,15 / 10 · ASGARİ SET DÜŞTÜ (② 7,3 · ⑤ 5,6) · ⛔ BİTİŞ KARTI İHLALİ · RAPOR: QA/RAPORLAR/THE_MOUNTAIN_CROWN.md
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare + 7 I2V
   YAPI: adı verilmeyen bir bazalt kayalığında (vadi tabanından +118,00 m) 42,00 × 30,00 m'lik KAYA OYMA SU SARAYI.
         cepheden 6,00 m içeri · 6 tek parça sütun (Ø 3,00 × 22,00 m · eksenler x = ±10,50 · ±15,00 · ±19,50) ·
         ortada tek kemer (12,00 m açıklık · 30,00 m boy) · arkada üç teras (+40,00 · +47,50 · +55,00) ·
         arşitrav +62,00→+68,00 · ⭐ TAÇ: 14 dişli parapet +68,00→+72,00 · iki köşede 3,00 m öne taşan konsol
         oluk ağzı · eşikten (+112,00) inen iki kesme oluk
   KAYNAK: sahibin yapıştırdığı 50 sn / 7 satır fikri ("THE MOUNTAIN CROWN") → ajan DÖRT BULGU bildirdi
         (① fikir THE STONE DRAGON'ın hem ödül mekanizmasını hem BEDEL nesnesini tekrarlıyordu [P16-a]
          ② 40 katta moloz defteri kapanmıyordu: 600 000 m³ gevşek, 35° şevde 53 m yüksek · 76 m ileri, ya da
             21 000 kamyon seferi [P16-b]  ③ 40 kat işçiyi 15 piksele indiriyordu  ④ konu YATAY yuvasını dolduramaz)
         → ÜÇ TERSİNE ÇEVİRME önerdi (su ödül değil DİRENÇ · 40 kat → 8 kat · defter kapalı) → sahip "onay" dedi.
   KAMERA: karşı yamaçtaki kaya sekisi · h +52,00 m · d 78,00 m · bearing 15° · ⭐ TİLT 0 · roll 0 · 24 mm
         kadraj 78,00 m en × 138,67 m boy · 13,846 px/m · cephe normali 195° · 44°K · δ +8°
         ⭐ İSTASYON SEÇİLMEDİ, İKİ SINIRIN KESİŞİMİNDEN ÇIKTI: şelalelerin %x 25/75'e oturması ENİ,
            vadi tabanı + eşik + kaya tepesinin aynı kadraja girmesi BOYU belirledi; 9:16'nın 1,778 oranı
            ikisini tek bir d = 78,00 m'de buluşturdu.
   BEDEL: ⭐ ISLAK KARA YÜZ — G0'da kayalık siyah, ıslak ve parlaktır; iki doğal şelale x = ±19,50'den
         (%x 25/75) 118,00 m (1634 px) düşer; ortasında 4,00 m'lik (55 px) yeşil yosun bandı; dibinde iki dip
         havuzu. S0'da iki akış eşikteki çelik oluğa alınır ve %93,59'a atılır; S1'de yüz SİYAHTAN SOLUK GRİYE
         döner ve yosun kesilip atılır — yerinde yalnız açık renk bir SIYRIK kalır. Geri dönmez.
   ⭐ İKİ DEFTER, AYNI KAYA (deponun ilki):
         ① toplayan — APRON ÜST KENARI, monoton artan: 240 · 240 · 286 · 330 · 376 · 420 · 420 · 420 px
         ② eksilen  — DÜŞEN SU İPLİĞİ: G0 2 (%x 25/75) → G1–G6 1 (%x 93,59, kahverengi) → G7 2 (%x 21,33/78,67)
         hacim: çıkan 10 228 m³ katı × 1,25 = 12 785 m³ gevşek · apron net 12 783 m³ · ⭐ FARK −2 m³ (%0,02)
         ⛔ Hiçbir kamyon kadrajdan taş çıkarmaz, hiçbir kamyon kadraja taş getirmez. ⛔ VİNÇ YOK: taş DÜŞER.
   TANIK: ① x −26,00 · d 70,00 · %x 12,86'da iki kaya bloğu (93 px · 77 px) — G0'da yeşil suyun içinde,
             G7'de AYNI PİKSELDE kuru, apron saçağıyla yarı gömülü
          ② kesilen yosun bandının yatay SIYRIĞI (G2 → G7, cephe dışında da sürer)
          ③ iki doğal kaya payandası %x 7,69 / 92,31, tepeden dibe
   ÖDÜL: dağın suyu geri gelir — ama artık kayaya değil, KESME TAŞA iner. Ödül YENİ değil, GERİ VERİLEN şeydir.
         final rejim G: kapak düşer · su iki oluğu doldurur · 61,00 m serbest düşüş = √(2·61/9,81) = 3,53 sn
         (⭐ uydurulmuş değil HESAPLANMIŞ süre · çarpma 34,60 m/s · 878 px) · iki şelale kurulur
   IŞIK: 6 × rejim B + 1 × rejim G = 12,00 sa (tavan 14,00) · 06:00 → 18:00 · gündüz 13 sa 02 dk · pay 31+31 dk
         cephe aydınlık katsayısı: 0,000 → 0,014 → 0,351 → 0,568 → 0,607 ⭐ → 0,457 → 0,160
         ⭐ IŞIK EĞRİSİ İLE KURUMA EĞRİSİ AYNI EĞRİ: ışık yüze tam olarak su kesildiği saatte ulaşır [P16-f]
   SİLUET: KÜTLE (beşinci) · GLASS CROSSING DİKEY → MOUNTAIN CROWN KÜTLE ardışık yayınlanabilir
         ⚠️ STONE DRAGON ile aile farklı ama İŞ aynı (oyma): araya en az iki film
         ⚠️ IZGARA: DİKEY 8 · ZEMİN 5 · KÜTLE 5 · YATAY 1 — YATAY dördüncü kez aç kaldı, sahip bilerek onayladı
   DOSYALAR: THE_MOUNTAIN_CROWN_DIKEY_TIMELAPSE.md (958 satır) · _QA_SPEC.md (255) · _KAPAK.md (133)
   ⛔ KAPI: ⚠️ FIX × 2 (ikisi de BEYANLI: ARAÇ KUTU SETİ ölçülmedi · yedi sahne de 8,0 sn = ⑥ METRONOM) ·
         ⛔ BLOCK 0 · MOTION FOCUS FIX 0 · prompt uzunlukları 5 790 – 5 996 (band 2 000–6 000) · "crane" YOK
   AÇIK: platform başlığı · SES üretim yolu · ⛔ ARAÇ KUTU SETİ ölçülmedi (üretimi BLOKE eder) ·
         kapak varyantı (ⓑ başlıksız ciddi aday) · yayın aralığı (STONE DRAGON ile araya iki film)
   EN BÜYÜK RİSK: ⭐ "KEŞİF FİLMİ"NE DÖNME — model kaya oyma bir cepheyi ANTİK HARABE olarak boyamaya
         çok yatkındır (Petra/Ellora refleksi) ve o anda film YAPIM filmi olmaktan çıkar. Savunma:
         taze kesik ≥ 1,8 × yıllanmış kaya renk oranı (QA_SPEC §2 ①) + cephe ile apronun AYNI RENK olması.
         PİLOT: S4 (G4 → G5) · ikinci pilot S2 (G2 → G3, modelin "yapı büyür" alışkanlığına ters tek sahne).
   ⚠️ REJİM G BEŞİNCİ KEZ FİNAL — bir sonraki filmin finali G olmamalı [P16-g, sahip onayı 25.09.2026].

THE GLASS CROSSING — OTUZUNCU FİLM · İLK CAM DÖŞEME · ⭐ ŞEFFAFLIĞI ÖLÇÜLEBİLİR YAPAN İLK FİLM · ⭐ FİKİR SAHİPTEN · YAZILDI 24.09.2026 · ÜRETİLDİ VE 12 MERCEKLE ÖLÇÜLDÜ ⭐
   ⭐ 12/12 MERCEK TAMAMLANDI · DÖRT TANE 10/10 TAM PUAN (③ 10,0 · ⑥ 10,0 · ⑨ 10,0 · ⑫ 10,0) · ASGARİ SET TAM (① 8,9 · ② 8,1 · ⑤ 8,7) · FINAL BEAT PASS (9/10) · ORTALAMA: 9,04/10 · ⛔ KANYON ÜSTÜ VİNÇ İHLALİ (⑪ 6,5 · ② 8,1)
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare + 7 I2V
   YAPI: adı verilmeyen bir kaya boğazında 27,00 m'lik çürümüş kalas köprünün CAM ZEMİNLİ GEÇİDE dönüşmesi.
         eski hâl: iki paslı çelik kiriş + çürük meşe kaplama + halat korkuluk →
         söküm (kaplama · korkuluk · kirişler 4,50 m'lik parçalara kesilir) → yeni çelik ızgara (iki kenar rayı +
         3,00 m'de bir çapraz taşıyıcı = 9 göz) → beyaz koruyucu filmli 9 cam ünite (2,40 × 3,00 × 0,040 m · 720 kg)
         neopren üstüne oturur ve alüminyum bastırma çerçevesiyle kenetlenir → cam korkuluk → ⭐ FİLMLER SOYULUR
   KAYNAK: sahibin yapıştırdığı 50 sn / 7 satır fikri ("THE GLASS CROSSING") → 7 × 8,0'a katlandı. SEKİZ KARAR
         değiştirildi, ikisi YAPISAL: ① soyma yönü TERS çevrildi (uzak uçtan yakına — dereyi gösteren tek göz
         yakın gözdür ve sona saklandı) ② son iki filmi FİGÜRÜN KENDİSİ söküyor (VANISHING ROOM iskeletini
         kırmak için: figür gelen konuk değil, örtüyü kaldıran kişi). Diğer altısı: derinlik 18,00 m'de
         kilitlendi (güvenli alan) · açıklık 27,00 m · eski köprüye çelik kiriş eklendi · ⛔ vinç kaldırıldı,
         geçici tel kondu · başlık değiştirildi · aile DİKEY yazıldı (YATAY satın alınamadı).
   KAMERA: güney kenarın üst kaya terası · h +20,00 m · d0 11,00 m · D_eksen 24,50 m · bearing 0° · tilt 33° · roll 0
         ufuk %93,29 (KADRAJDA · üstte 129 px gök) · kare altı d 7,33 m · d_50 30,80 m
         ⭐ camdan görme: görülen = d × (1 + 18,00/20,00) = d × 1,90 — tilt GİRMEZ [P14-c]
         ⭐ istasyon ARANMADI, ÇÖZÜLDÜ: tan(tilt + 36,87°) ≥ 2 · derinlik / açıklık [P15-d]
   BEDEL: eski köprünün kendisi — 3,24 m³ çürük meşe (≈2,43 t) + 4,50 m'lik parçalara kesilmiş iki paslı kiriş
         (≈2,97 t) boğaz TABANINA iner, orada kalır, hiçbir karede küçülmez.
         ⭐ Yığın 8,00 m eninde kurulur; köprü taban düzleminde 4,56 m'lik şerit örter →
            G1 ~70 px · G2–G6 134 px · G7 223 px. KİMSE DOKUNMADAN genişler; genişleten şey CAMDIR.
   TANIK: ① dere bandı %20,05 · 106 px · kadrajı soldan sağa keser; döşeme onu d 12,89'da 201 px kara barla keser
            → KESİK: G0 · G1 · G4 · G5 · G6   ·   KESİNTİSİZ: G2 · G3 · G7
          ② güney kayadaki eski ankraj yuvaları (d 8,50 · 28 px) — G0 dolu, G2'den sonra boş, yeri sabit
          ③ çentikli kret + tek çam, ufkun hemen altında
   ÖDÜL: tek figür cam zeminin üstünde, 18,00 m suyun DOĞRUDAN üstünde, aşağı bakıyor — ve o zemini
         kaldıran kişi kendisi (elinde son film tomarı, arkasında 209 px'lik beyaz iz).
   ⭐ GÖRÜNÜRLÜK EĞRİSİ: 0 → 12 020 → 104 863 → 100 401 → 0 → 0 → 53 298 → 111 556 px²
         Deponun diğer 29 filmi BÜYÜMEYİ ölçer; bu film İKİ KEZ kapanıp İKİ KEZ açılan bir eğriyi ölçer [P15-e].
   IŞIK GÜNÜ: 6 × 2 sa = 12,00 sa ≤ 14 sa · 44°K · δ +8° · gündüz 13 sa 02 dk (05:29–18:31) · iki uçta 31'er dk pay
         gölge süpürmesi 191,5° · güneş hiçbir karede kadrajda değil (yatay yarı açı 26,57°)
         ⭐ boğaz tabanı gün boyu AÇIK GÖLGEDE (yalnız G3'te öğle güneşi iner) — hata değil, kontrast bütçesi [P15-f]
   SİLUET: DİKEY (sekizinci) — G7'den okundu: 236 px'ten 68 px'e daralan kama. VANISHING ROOM ZEMİN → GLASS
         CROSSING DİKEY ardışık yayınlanabilir. ⚠️ Ama ÖDÜL MEKANİZMASI aynı; araya film girmeli [P15-a].
         ⚠️ Izgara: DİKEY 8 · ZEMİN 5 · KÜTLE 4 · YATAY 1 — YATAY üçüncü kez aç kaldı [P15-b].
   DOSYALAR: dikey_shorts/THE_GLASS_CROSSING/ — _DIKEY_TIMELAPSE.md (907 satır) · _QA_SPEC.md (235) · _KAPAK.md (128)
   ⛔ KAPI: python3 araclar/prompt_kontrol.py … → ⚠️ FIX ×2 (ikisi de BEYANLI: ARAÇ KUTU SETİ ölçülmedi ·
         yedi sahnenin yedisi de 8,0 sn → ⑥ METRONOM) · BLOCK 0 · MOTION FOCUS FIX 0
   AÇIK: platform başlığı ("A Rotten Plank Bridge Becomes a Glass Crossing | AI Timelapse") · SES üretim yolu ·
         ⛔ ARAÇ KUTU SETİ ÖLÇÜLMEDİ (üretim açılamaz) · S6'da yürünen mesafe (6,00 m önerilen) · yayın aralığı
   EN BÜYÜK RİSK: modelin camı İKİNCİ BİR OPAK YÜZEY sanması. Pilot klip S5 — kadrajdan bir şey ÇIKARAN tek klip;
         modelin ölçülmüş eğilimi EKLEMEKTİR [P14-h]. Üretim sırası: G6 → G7 → S5 → G3-G4 → G0 → kalanlar.
   ⛔ DEVAM EDEN AÇIK [P13-h]: prompt_kontrol.py §9 metin yasağı kapsam denetimi "…annotated by anyone" arıyor,
         ev yazımı "…included." ile bitiyor; sekiz yüzey sayımı hiçbir filmde ateşlenmedi. Sahip kararı olarak taşınıyor.

THE VANISHING ROOM — YİRMİ DOKUZUNCU FİLM · İLK GÖMÜLÜ BAHÇE ODASI · ⭐ DORUĞU BOŞLUK OLAN İLK FİLM · ⭐ FİKİR SAHİPTEN · YAZILDI 23.09.2026 · ÜRETİLDİ VE 12 MERCEKLE ÖLÇÜLDÜ ⭐
   ⭐ 12/12 MERCEK TAMAMLANDI · BEŞ TANE 10/10 TAM PUAN (② 10,0 · ③ 10,0 · ⑩ 10,0 · ⑪ 10,0 · ⑫ 10,0) · ASGARİ SET TAM (① 8,9 · ② 10,0 · ⑤ 9,9) · FINAL BEAT PASS (10/10) · 0/6 dikiş kusuru · ORTALAMA: 9,65/10
   ⭐ DEPO REKORLARI: THE GROWTH NOBODY MADE: NONE · THE FIRST PIECE THAT APPEARED: NONE · THE MOST PURPOSELESS ACTIVITY: NONE · THE MOST DAMAGING INTRUDER: NONE · THE BODY THAT MELTED WORST: NONE
   ⭐ BİTİŞ KARTI: Tüm merceklerde "AYNI" (SAME) onaylandı.
   → RAPORLAR/THE_VANISHING_ROOM.md · HAM_RAPORLAR/THE_VANISHING_ROOM/
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare + 7 I2V
   YAPI: adı verilmeyen bir evin duvarlı arka bahçesinde çimin ALTINA gömülen tek oda (iç 3,00 × 4,20 × 2,60 m,
         taban −2,90 m, tavan üstü −0,30 m): çim 18 ruloda kaldırılır → 3,80 × 5,00 × 2,90 m çukur açılır →
         taban + dört duvar + düz merdiven dökülür → ⭐ ODA ÜSTÜ AÇIKKEN DÖŞENİR (ahşap kaplama, uzun bank, raf,
         halı, lineer armatür yanar) → tavan 2,20 × 2,60 m ağız bırakılarak dökülür, ray + zincir + dişli tahrik
         takılır, 300 mm toprak ve çim geri serilir → ⭐ KENDİ ÇİMİNİ TAŞIYAN 550 kg'lık KAPAK kapanır ve oda
         kadrajdan tamamen silinir → 8 gerçek saniyede kapak 1,80 m kayar, yerden sıcak ışık çıkar, tek figür
         üç basamak iner. Hacim kapalı: ÇUKUR 55,1 m³ = ODA 40,7 + GERİ DOLGU 14,4; net dışarı 36,0 m³.
   KAYNAK: sahibin yapıştırdığı 50 sn / 8 satır fikri ("THE VANISHING ROOM") → 7 × 8,0'a katlandı. ON KARAR
         (plan §TASARIM KARARLARI); ikisi yapısal: ① iç döşeme TAVANDAN ÖNCEYE alındı — bir delikten görülen
         taban ağzın boyu × (1 + derinlik/h) kadardır ve DUVARLAR GÖRÜNMEZ, yani kitaplık ve bank tavan
         takılıyken sabit dış istasyondan okunamaz; ② mevsim geç yaza (δ +8°) kaydı — altı rejim B klibi 12 saat
         eder ve bu pencere ekinoksta sıfır payla, erken sonbaharda hiç kapanmaz.
   KAMERA: HOME · bahçe deposunun düz çatısı · h 7,00 m · d_yakın 5,00 m / d_eksen 7,50 m · bearing 0° ·
         ⭐ tilt 40° AŞAĞI · roll 0 · 24 mm f/8 · ufuk %105,94 (KADRAJIN DIŞINDA — gök YOK) · formül KAMERA_DILI §3.
         h 7,00 tilt değil YÜKSEKLİK olarak seçildi: görünür oda tabanını açan tek değişken h'dir (h 4,60 → 0,40 m,
         h 7,00 → 3,68 m).
   BEDEL: ⭐ TOPRAK SETİ — çukurdan çıkan 36,0 m³'ün 8,8 m³'ü bahçenin solunda dikili bir sırt olarak kalır
         (G1 2,00 m → G4 5,00 m · x %14,2–26,6 · 88–103 px). Hiçbir karede küçülmez. Oda kaybolmaz, biçim
         değiştirip bahçenin kenarında ayakta durur.
   TANIK ①: 18 ÇİM RULOSU — S1'de kalkan çim S5–S6'da odanın üstüne geri iner (18 → 11 → 2). ⭐ KAPANAN DEFTER.
   TANIK ②: DİKİŞ — kapağın çevresinde 2,4 px'lik kapanmayan çizgi, G5→G7 kilitli piksellerde. Bilerek okunurluk
         eşiğinin ALTINDA: okunur olsaydı gizlenme başarısız olurdu [P14-f].
   ÖDÜL: rejim G · 48,0–56,0 · kapak 0,225 m/sn ile 1,80 m kayar, 186 px'lik yarık açılır, ⭐ IŞIK AŞAĞIDAN
         YUKARI çıkar (filmin tek yukarı doğru hareketi), tek figür sırtı kameraya üç basamak iner.
   IŞIK GÜNÜ: 06:00 → 18:00 + 8 sn = 12 sa 0 dk 8 sn ≤ 14 sa · 40°K · δ +8° · doğuş 05:33 · batış 18:27 ·
         gölge süpürmesi 20,0 / 28,1 / 48,1 / 48,1 / 28,1 / 20,0 derece · güneş hiçbir karede kadrajda değil.
   SİLUET: ⭐ ZEMİN (G7'den okundu) · beşinci ZEMİN · STONE DRAGON DİKEY'den sonra ardışık yayınlanabilir ·
         ⛔ HIDDEN OASIS · SWALLOWED BUS · EMPTY LOCK · DEEP END ile yayınlanamaz.
         ⚠️ Izgara DİKEY 7 · ZEMİN 5 · KÜTLE 4 · YATAY 1 — YATAY daha da aç kalıyor ve bu konu o yuvayı dolduramaz.
   DOSYALAR: dikey_shorts/THE_VANISHING_ROOM/{_DIKEY_TIMELAPSE.md · _QA_SPEC.md · _KAPAK.md}
   ⛔ KAPI: prompt_kontrol.py → FIX ×2, ikisi de BEYANLI (araç kutu seti ölçülmedi · 7 sahne süresi eşit → ⑥ METRONOM).
         BLOCK 0 · MOTION FOCUS FIX 0 · promptlar 5875–5995 karakter · "crane" hiçbir promptta yok.
   AÇIK: platform başlığı · ses üretim yolu · ⛔ ARAÇ KUTU SETİ ÖLÇÜLMEDİ (üretim açılamaz) · kapağın G7'deki
         yolu (1,80 m önerildi) · ızgaranın YATAY açığı · üretim sırası (G6 → G7 → pilot S5 → G3-G4-G5 → S6 → kalanlar).
   ⚠️ EN BÜYÜK RİSK: G6'da kadrajda ölçülecek YAPI YOKTUR — yalnız çim vardır ve 2 px eşiği tamamen üç saha
         çapasına yaslanır [P14-b]. İkinci risk: modelin eğilimi EKLEMEKTİR, S5 ise sekiz saniyede sekiz şeyi
         ÇIKARIR [P14-h]. Pilot bu yüzden S5'tir.
   ⚠️ P13-h DEVAM EDİYOR: kapının §9 metin yasağı kapsam kontrolü bu korpusun NEGATIVE yazımında hiç koşmuyor;
         bu film de ev standardıyla yazıldı. Sahip kararı bekliyor.

THE STONE DRAGON — YİRMİ SEKİZİNCİ FİLM · İLK TAŞ OYMA · ⭐ DEPONUN İLK EKSİLTMELİ FİLMİ · ⭐ FİKİR SAHİPTEN · YAZILDI 23.09.2026 · ÜRETİLDİ VE 12 MERCEKLE ÖLÇÜLDÜ ⭐
   ⭐ 12/12 MERCEK TAMAMLANDI · İNŞAAT VE FİZİK GEÇTİ (② 9,2 · ⑫ 9,5 · ⑩ 9,25 · ③ 9,1 · ⑥ 9,4) · 11 nirengide ölçek sapması 0 px (%0,0) · Rejim G 00:46 canlı su doruk kesmesi · 12-14 saatlik güneş yayı tam tuttu
   🚨 ŞANTİYE DİKİŞLERİ VE GÖRSEL DEVAMLILIK DÜŞTÜ: ⑤ 3,9 Ⓥ (10/12 dikiş kusurlu: moloz sıfırlanması, vinç buharlaşması 00:43) · ⑪ ENVANTER 5,5 Ⓥ (izinsiz testere aparatı 00:16, kompresör) · ⑧ DENETİM RED / REJECTED
   🚨 ORTAK KRİTİK HATA: BİTİŞ KARTI (00:55.5–01:00.0) tamamen farklı bir AI ejderha modeli (çift dev kanatlı) göstermektedir (`END CARD: DIFFERENT`). Kurgudan derhal 4 sn kesilecek.
   → RAPORLAR/THE_STONE_DRAGON.md · HAM_RAPORLAR/THE_STONE_DRAGON/
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare + 7 I2V
   YAPI: taş atölyesinin açık avlusunda tek ham ocak bloğu 1,25 × 1,05 × 2,35 m, 0,45 m taş banker üstünde iki meşe
         takozda: köşeler düşer, kütle düz keski düzlemlerine iner → BAŞ çıkar (iki kısa boynuz, sağa kıvrılan boyun)
         → karot matkabı boynun arkasından dikey delik açar, çıkan taş silindir banker'ın sağına dikilir → gözler,
         oyuk ağız (tabanında delik), gövdeye yatık kanat, kuyruk, kaba hazne → pullar + kanat çizgileri + eğe +
         hortumla yıkama (taşın gerçek rengi) → bronz boru ağza, pompa çukura, saha avlu kapısından çıkar →
         rejim G: pompa çalışır, su ağızdan hazneye 296 px düşer, göğüs ıslanıp koyulaşır, işçi geri çekilir
   ⭐ KAYNAK: sahibin yapıştırdığı 50 sn / 7 bölüm fikri ("THE STONE DRAGON") → 7 × 8,0'a katlandı (3 değişiklik:
      süre 50→56,0 · tesisat YANDAN → TAŞIN İÇİNDEN (karot deliği, S2'ye alındı) · hazne ayrı tekne → AYNI BLOKTAN)
      + fikrin kendi 6 sınırı sert kilit hâline getirildi (hacim · kısa boynuz · yatık kanat · yalnız aletin
      çalıştığı yerde eksilme · sabit ön çapraz kamera · heykel finalde de TAŞ)
   KAMERA: HOME tek istasyon · avlu döşemesinde · h +1,70 m · D_ön 4,20 m · D_banker 5,00 m · bearing 0° (KUZEY) ·
      ⭐ TİLT 0 · ufuk %50 · ölçek 257 px/m · tiltli formül borcu YOK
   ⭐ BEDEL: MOLOZ YIĞINI — G0'da yok, G5'te 1,70 × 0,68 m (367 × 174 px), banker'ın solunda; hiçbir karede küçülmez
   ⭐ TANIK ①: HAM OCAK KESİMİ BANDI — bloğun dibinde hiç oyulmayan 0,25 m, %30,16–34,13 · 76 px · G0→G7 AYNI PİKSEL
   ⭐ TANIK ②: KAROT — Ø0,09 × 1,40 m taş silindir (22 × 407 px · x %73,86), G3→G7 kadrajda
   ÖDÜL: rejim G'de su (296 px düşüş) + iki renkli taş (ağzın üstü kuru/soluk, altı ıslak/koyu)
   IŞIK GÜNÜ: 07:00 → 19:00 + 8 sn = 12 sa 0 dk 8 sn (6 × B + 1 × G) ≤ 14 sa ✅ · 40°K · δ +21° (erken yaz) ·
      güneş 82°/24° → 295°/+2,6° · hiçbir karede kadrajda değil · takvim ~5 hafta, IŞIKTAN değil YIĞINDAN okunur
   SİLUET: ⭐ DİKEY (aile G7'den okundu) · DEEP END ZEMİN → STONE DRAGON DİKEY ardışık yayınlanabilir ·
      ⛔ LONG SHADOW · EMPTY RIDGE · LAST CIRCLE · DARK ROCK · QUIET FIELD · BROKEN CLIMB ile ardışık YAYINLANAMAZ
   DOSYALAR: dikey_shorts/THE_STONE_DRAGON/ → plan (922 satır) · QA_SPEC (203) · KAPAK (110)
   ⛔ KAPI: prompt_kontrol.py → FIX ×2 (kutu seti ÖLÇÜLMEDİ · 7 sahnenin süresi eşit = ⑥ METRONOM, ikisi de
      BEYANLI) · BLOCK 0 · MOTION FOCUS FIX 0 · görsel promptlar 5628–5942 karakter · "crane" hiçbir promptta yok
   AÇIK: platform başlığı ("A Rough Stone Becomes a Dragon Fountain | AI Timelapse") · ses üretim yolu (SFX
      üreteci mi kütüphane mi) · ARAÇ KUTU SETİ ölçülmedi → ⛔ üretim açılamaz · üretim sırası (G7 → pilot S1 →
      G2-G3-G4 üçlüsü → S6 → kalanlar)
   ⚠️ EN BÜYÜK RİSK: serbest geometri — ejderha sekiz bağımsız karede farklı çizilebilir. Azaltma: blok zarfı
      px kilitli (394 × 716) · ham kesim bandı çapa · beş maddelik ejderha cümlesi G2→G7 birebir · ⭐ PİLOT S1
      (geometri sahnesi değil KİMLİK sahnesi — deponun ilk kez pilotu en zor geometriden başka bir yere koyması)
   ⚠️ P13-h: kapının §9 metin yasağı 8-yüzey kontrolü bu depodaki negatif çekirdek yazımıyla FİİLEN KOŞMUYOR
      (kontrol "…annotated by anyone" arıyor, çekirdek "…included." ile bitiyor) — 27 filmin hepsini ilgilendirir,
      sahip kararı bekliyor

THE DEEP END — YİRMİ YEDİNCİ FİLM · İLK HAVUZ → GİZLİ AÇIK HAVA SİNEMASI · ⭐ FİKİR SAHİPTEN · İLK KADEMELİ GÜVERTE · YAZILDI 23.09.2026 · ÜRETİLDİ VE 12 MERCEKLE ÖLÇÜLDÜ ⭐
   ⭐ 12/12 MERCEK TAMAMLANDI · YEDİ TANE 10/10 TAM PUAN (② 10,0 · ③ 10,0 · ⑤ 10,0 · ⑧ 10,0 · ⑩ 10,0 · ⑪ 10,0 · ⑫ 10,0) · ASGARİ SET TAM (① 9,6 · ② 10,0 · ⑤ 10,0) · FINAL BEAT PASS (10/10) · Rejim G 00:48 doruk vuruşu · ORTALAMA: 9,83/10
   ⚠️ 00:56–01:00 bitiş kartı kurguda kesilecek · 00:44.5–00:48.0 teslimat geçişi 3.5 sn boşluk (⑦ İŞ 9,3)
   → RAPORLAR/THE_DEEP_END.md · HAM_RAPORLAR/THE_DEEP_END/
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · ⛔ öncesi/sonrası YOK · zincirli · 8 kare + 7 I2V
   YAPI: duvarlı bahçede 10,0 × 4,0 m terk edilmiş havuz (sığ uç −1,0 · derin uç −2,0): pompa suyu çeker + tramplen
         sökülür → yaprak + silt çıkar, basınçlı yıkama başlar → kabuk onarılır (çatlak · yalıtım · paslanmaz ızgara) →
         4 kademeli larch güverte kameradan uzağa kapanır → 4 bank + krem minder + SÖNÜK pirinç armatürler →
         beyaz perde uzak duvara + projektör, saha boşalır → rejim G: armatürler sırayla yanar, huzme havuzu geçer,
         perdede deniz, tek figür koridordan inip oturur
   ⭐ KAYNAK: sahibin yapıştırdığı 50 sn / 8 bölüm fikri ("THE HIDDEN CINEMA") → 7 × 8,0'a katlandı (8 değişiklik:
      süre · bedel eklendi (tramplen) · düz taban → 4 kademe · iki figür → tek figür · ışık rejim G'ye · gök kaldırıldı
      (ZEMİN) · vinç yok (rampa) · derinlik rakamı çıkarıldı (metin yasağı))
   ⭐ KAMERA: havuz evi terası h +5,0 · D_kenar 2,5 · D_eksen 7,5 · tilt −38° · ufuk %102,1 (KADRAJ DIŞI) ·
      perde 208 px (KESİR) · ZEMİN ailesi (dördüncü)
   BEDEL: tramplen (G0'da derin ucun üstünde, perde tam o duvara gelir) · TANIK: tramplen çimende (G1→G7, 215 px) +
      kesintisiz turkuaz fayans bandı + krom korkuluk · ÖDÜL: S6'da ışık, huzme ve perdedeki deniz
   Işık tek gün 08:30 → 20:30 + 8 sn (6×B + G) · güneş 100°/11° → 280°/−11,4° · takvim yok, mevsim taşıyıcısı
      erken sonbahar (çınar + düşen yapraklar)
   plan ✅ (BEŞ SORU + her I2V'de MOTION FOCUS) · QA_SPEC ✅ (§4 YÜK YOLU · §6 SAYIM · §7 REJİM G) · KAPAK ✅ (YALNIZ G7 ·
   THE DEEP END · bantsız, karaçam bandında) · günlük ⛔ AÇILMADI
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0 · MOTION FOCUS FIX 0
   ⚠️ AÇIK: kapak başlığı (sahip) · SES üretim yolu (sahip) · yüzdeler TÜRETİLMİŞ · ⛔ THE HIDDEN OASIS ile ARDIŞIK
      YAYINLANAMAZ (aynı aile VE aynı konu) · gece finali riski (bahçe aydınlanırsa "gizli oda" kaybolur) ·
      BROKEN CLIMB ④ dersi: teslim 56,0 sn, kart BASILMAZ
   → dikey_shorts/THE_DEEP_END/

THE BLUE DOOR — YİRMİ ALTINCI FİLM · İLK CEPHE RESTORASYONU (DÜKKÂN → KAFE) · ⭐ SENARYO SAHİPTEN · İLK YAPAY IŞIKLI FİNAL · YAZILDI 22.09.2026 · ÜRETİLDİ VE 12 MERCEKLE ÖLÇÜLDÜ ⭐
   ⭐ 12/12 MERCEK TAMAMLANDI · DÖRT TANE 10/10 TAM PUAN (③ 10,0 · ⑦ 10,0 · ⑨ 10,0 · ⑫ 10,0) · ASGARİ SET TAM (① 8,6 · ② 9,7 · ⑤ 9,3) · FINAL BEAT PASS (10/10) · Rejim G 00:48 doruk vuruşu
   ⚠️ 00:56-01:00 bitiş kartı ve fon müziği sızıntısı kurguda kesilecek · ⑩ SEBEP 7,0 (00:14 kasanın askıda kalması) · ⑪ ENVANTER 9,4 (00:17 sepetli araç bomu)
   → RAPORLAR/THE_BLUE_DOOR.md · HAM_RAPORLAR/THE_BLUE_DOOR/

THE TIDE GATE — YİRMİ BEŞİNCİ FİLM · İLK FIRTINA KABARMASI SEDDİ · ⭐ DİKEY HAVUZUN İLK YATAY FİLMİ · ÜÇÜNCÜ REJİM G · YAZILDI 22.09.2026 · ÜRETİLMEDİ ⛔
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · zincirli · 8 kare + 7 I2V
   YAPI: Atlantik haliç limanının 60 m'lik ağzına 3 gri beton kule (+22) + 2 kavisli çelik segment kapak (24 m):
         taşkın çekilir, jack-up gelir → 3 palplanş batardo kurutulur → kuleler yükselir → kapak 1 (sheerleg, dışarıdan) →
         kapak 2 + silindirler, kapaklar KALKAR → fırtına: kapaklar İNER → rejim G: dalga kapalı kapaklara çarpar
   ⭐ KAYNAK: sahibin taslağı + ajanın dört fizik düzeltmesi (fiyort → makrogelgitli haliç · gelgit "dalgası" → kabarma ·
      final A → B + G · "ayna" iç su → rüzgâr pürüzü) → sahip "başla"
   ⭐ KAMERA: kilise avlusu h +25 · D_eksen 160 · tilt −8° · ufuk %59,4 — kule kabinleri (+28) ufku keser (bedel)
   BEDEL: açık ağız + içeri giren dalga · TANIK: evlerde kahverengi taşkın çizgisi (G1→G7 aynı) · ÖDÜL: S6 patlama, içerisi düz
   Işık tek gün 06:15 → 18:15 + 8 sn (6×B + G) · takvim bir yıl (burun bitkileri) · su kotu her G karesinde kilitli
   plan ✅ (BEŞ SORU + her I2V'de MOTION FOCUS) · QA_SPEC ✅ (§4 YÜK YOLU · §6 SAYIM · §7 REJİM G) · KAPAK ✅ (YALNIZ G7 ·
   THE TIDE / GATE · alternatif THE LAST WAVE) · günlük ⛔ AÇILMADI
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0 · MOTION FOCUS FIX 0
   ⚠️ AÇIK: kapak başlığı (sahip) · SES üretim yolu (sahip) · yüzdeler TÜRETİLMİŞ · kot farkı 27 px (kanıt doku) ·
      BROKEN CLIMB ④ dersi: teslim 56,0 sn, kart BASILMAZ
   → dikey_shorts/THE_TIDE_GATE/

THE BROKEN CLIMB — YİRMİ DÖRDÜNCÜ FİLM · İLK FÜNİKÜLER ONARIMI · ⭐ İKİNCİ MÜZİKSİZ FİLM · ÜRETİLDİ ✅ · ⭐ ON İKİ MERCEK TAMAMLANDI (12/12) (① 4,1 Ⓥ · ② 10,0 · ③ 9,9 Ⓥ · ④ 5,1 Ⓥ · ⑤ 10,0 Ⓥ · ⑥ 9,9 · ⑦ 10,0 Ⓥ · ⑧ 10,0 · ⑨ 10,0 Ⓥ · ⑩ 10,0 · ⑪ 10,0 Ⓥ · ⑫ 10,0) · ⭐ SEKİZ TANE 10/10 TAM PUAN
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · zincirli · 8 kare + 7 I2V
   YAPI: yamaç FÜNİKÜLERİ onarımı (120 m hat, 35° eğim, 40 m yarık): 12 mikrokazık + 8 prekast panel istinat (5 × 9 m) + 4 ray paneli + tek sarı yeni vagon + halat
   ⭐ SEKİZ TANE 10/10 TAM PUAN: ② İNŞA 10,0 · ⑤ DEVAMLILIK 10,0 (0/6 dikiş) · ⑦ İŞ 10,0 (boşluk %0, büyüme: NONE) · ⑧ YÖNTEM 10,0 (4/4 MADE) · ⑨ FAALİYET 10,0 · ⑩ SEBEP 10,0 · ⑪ ENVANTER 10,0 Ⓥ · ⑫ KATILIK 10,0
   ⭐ ZAMAN VE GEÇİŞ ZİRVEDE: ③ ZAMAN 9,9/10 (okunan süre 07:30–17:50 tam tuttu) · ⑥ GEÇİŞ 9,9/10 (TIME · RHYTHM, 00:20.3 tırmanış vuruşu)
   ⛔ DÜŞEN: ① KARE 4,1/10 Ⓥ (ALTI AYRI ÇEKİM · 4 istasyon grubu · Klip 4 ve 6 push-in/kayma · kilise mimari mutasyonu 0:11 · vagon metinleri)
   ⚠️ KURGU VE TESLİM İHLALİ: ④ TESLİM 5,1/10 Ⓥ (ENDS, Final Beat Fail) · 56,0 sn plan yerine 32,0 sn kesilmiş · şartname dışı "IT CLIMBED AGAIN" kapanış kartı
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ · RAPORLAR/THE_BROKEN_CLIMB.md ✅
   → dikey_shorts/THE_BROKEN_CLIMB/

THE QUIET FIELD — YİRMİ ÜÇÜNCÜ FİLM · İLK RADYO TELESKOPU (SIFIRDAN) · ⭐ İLK GECE-GÜNDÜZ ÇEMBERİ · ⭐ İLK MÜZİKSİZ FİLM · ⭐ ON İKİ MERCEK TAMAMLANDI (12/12) (① 9,8 · ② 10,0 · ③ 10,0 · ④ 8,4 · ⑤ 10,0 · ⑥ 10,0 · ⑦ 9,0 · ⑧ 10,0 · ⑨ 10,0 · ⑩ 9,5 · ⑪ 10,0 · ⑫ 10,0) · DEPONUN EN İYİ FİLMİ ✅
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · ⛔ MÜZİK YOK · zincirli · 8 kare + 7 I2V
   YAPI: Lovell tipi TEK radyo teleskopu (ray halkası Ø 96 · 2 kafes kule 50 m · 80 m beşik · Ø 76 m çanak · zenitte 90 m):
         çayırda halka hendek → beton halka + ray, ilk bölüm sapanda → iki kule (günbatımı, projektörler yanar) → beşik
         tandem kaldırma (gece, kar) → kaburgalar + rim (gecenin dibi → şafak) → paneller (projektörler söner, güneş
         doğar, vinç gider) → çanak 50° kameraya döner (A)
   ⭐ VAAT: "çanak bitecek mi?" değil, "bu şey HAREKET EDECEK mi?" — S6 rejim A: çanak zenitten 50° devrilir, içi
      güneşlenir; bedel (çayır + kret) kadrajda: kret orta yarısı çanağın arkasında, ambar kulenin dibinde (P8-f)
   ⭐ IŞIK ÇEMBERİ: 17:20 → 05:30 (6×B + A = 12 sa 10 dk) · 53°K haziran sonu (karanlık 5 sa) · günbatımı S2 içinde,
      gece S3–S4 (yıldız yayı 30°/2 sa · projektör havuz gölge · far izi · kuzey alacakaranlık bandı), gündoğumu S5
      içinde · final güneşli [DERS 45] · takvim yerden bir yıl, kar yalnız gece karelerinde (P8-a/b/c/d)
   ⭐ KAMERA: güney tepecik h 20 m · D_eksen 160 m · bearing 10° (güneş diskinden kaçmak için, P8-h) · tilt 0 ·
      ufuk %50 · DİKEY ailesi. ⛔ ön görselleştirme usta kareden önce zorunlu.
   ⭐ SES: müzik yok — diegetik yatak tek taşıyıcı (A1-c ilk sınav · P8-e); üretim yolu (SFX promptu / cue) sahip kararı
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ · RAPORLAR/THE_QUIET_FIELD.md ✅ (① KARE 9,8 · ② İNŞA 10,0 · ③ ZAMAN 10,0)
   ⚠️ AÇIK: Kurgudaki izinsiz başlık bindirmesi (0:48–0:56) kaldırılmalı · Asgari set için ⑤ DEVAMLILIK koşulmalı
   → dikey_shorts/THE_QUIET_FIELD/

THE EMPTY LOCK — YİRMİ İKİNCİ FİLM · İLK KANAL KİLİDİ · ⭐ ÜÇÜNCÜ AŞAĞI BAKIŞ · FİNAL REJİM A (makinesiz) · ⭐ ON İKİ MERCEK TAMAMLANDI (12/12) (① 7,5 · ② 10,0 · ③ 10,0 · ④ 6,8 · ⑤ 7,0 · ⑥ 9,5 · ⑦ 9,9 · ⑧ 10,0 · ⑨ 10,0 · ⑩ 10,0 · ⑪ 10,0 · ⑫ 10,0) · ⭐ ASGARİ SET TAMAMLANDI
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · zincirli · 8 kare + 7 I2V
   YAPI: TEK taş kanal kilidi (hazne 5 × 30 × 4,5 m · düşü 3 m): kırık kara meşe alt kapı → tahtalar + pompa, hazne
         boşalır → iki eski kanat vinçle çekek yoluna → eşik + çanaklar temizlenir → iki sarı kanat çanağa, mitre kapanır
         → tahtalar çıkar, su alt seviyeye, vinç gider, tekne gelir → tekne hazneye girer (A) → hazne dolar, tekne 3 m
         yükselir, yeni kapının güney yüzü KURU (A)
   ⭐ VAAT: "kapı değişecek mi?" değil, "yeni kapı YÜKÜ tutacak mı?" — S6 rejim A: su basamak 1→5, tekne coping
      hizasına; bedel (eski kanatlar) G7'de yolda YATAR, kadrajdan çıkmaz (P7-d)
   ⭐ KAMERA: değirmen çatı parapeti h 16 m · D_eksen 20 m · eksenden 4,5 m doğu · bearing 353° · tilt −38° (tanjantlı
      formül KAMERA_DILI §3, pinhole izdüşüm) — ufuk %102, gök YOK, ZEMİN ailesi. Aile bandı (−15…−30) dışında,
      bedeli plana yazıldı (P7-f). ⛔ ön görselleştirme usta kareden önce zorunlu.
   BEDEL: eski meşe kapı (yolda kalır) · ÖDÜL: S6 doluş, tekne yükselir, kapı kuru
   Işık tek gün 07:20 → 17:40 (5×B + 2×A = 10 sa 20 dk) · G6 → G7 ışığı 10 dk ilerler · her G karesi tek saat/tek durum
   plan ✅ (BEŞ SORU tablosu + her I2V'de MOTION FOCUS + KARAR CÜMLESİ) · QA_SPEC ✅ (§4 YÜK YOLU/DERS 57 · §5 SU
   CETVELİ/KURU YÜZ · §7 REJİM A) · KAPAK ✅ (kart yok; ⭐ YALNIZ G7 + THE EMPTY / LOCK — öncesi/sonrası YOK) ·
   RAPORLAR/THE_EMPTY_LOCK.md ✅ (12/12 TAM KOŞU · YEDİ TANE 10/10)
   ⚠️ AÇIK: Kurgudaki izinsiz başlık bindirmesi (0:56.0) kaldırılmalı · Safe Area 4/10 · Text 2/10
   → dikey_shorts/THE_EMPTY_LOCK/

BACK TO WATER — YİRMİ BİRİNCİ FİLM · İLK KURU HAVUZ / TEKNE · ⭐ İLK KIYI SAHASI · ÜÇÜNCÜ REJİM G · YAZILDI 19.09.2026 · ÜRETİLMEDİ ⛔
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK · zincirli · 8 kare + 7 I2V
   YAPI: TEK kuru havuzda (26 × 12 × 6 m) TEK çelik balıkçı teknesi (14 m): jet kabuğu soyar → kumlama + iki delik kare
         kesilir → iki levha sapanla iner, kaynak → kırmızı/lacivert boya → kabin krem + 5 cam, ekipman çıkar → havuz dolar,
         tekne takozdan kalkar, keson kayar → tekne kendi motoruyla kapıdan çıkar
   ⭐ SENARYO SAHİPTEN (S1–S7 · "Suya Dönüş") → depo formatına çevrildi (S0–S6 · tek ışık günü · S0 rejim A · kapı G6'da ·
      tekne 14 m · kapak SON KAREDEN) → sahip onayı 19.09.2026; yedi değişiklik plana §KONSEPT KAPISI altına yazıldı
   ⭐ KAMERA: batı rıhtımı başı projektör platformu h 12 m · D_eksen 16 m · bearing 20° · tilt −22° — ufuk %80, gök %20
      (kapak başlığı için); iskele bordası + güverte + taban + kapı + deniz tek kadrajda. ⛔ ön görselleştirme zorunlu.
   BEDEL: kesilip atılan iki gövde parçası (S2'de kamyon kasasında sağdan gider) + havuzun kendisi (S5'te su altında; G7'de
      dolu ve BOŞ) · ÖDÜL: S6 çıkış, iz kapıdan içeri
   Işık tek gün 07:00 → 17:10 (A + 5×B = 10 sa 10 dk · G 0 dk) · G6 = G7 ışığı birebir · her G karesi tek saat/tek durum
   plan ✅ (BEŞ SORU tablosu + her I2V'de MOTION FOCUS) · QA_SPEC ✅ (§4 YÜK YOLU · §5 SU SAATİ/KAPI · §7 REJİM G) ·
   KAPAK ✅ (kart yok; ⭐ YALNIZ G7 + BACK TO / WATER gök bandında — öncesi/sonrası YOK) · günlük açıldı ⛔ BOŞ
   (⑪ aşağı bakış + ufuk · ⑫ sapan · ⑬ su · ⑭ kapı · ⑮ geçiş)
   ⛔ KAPI: FIX ×3 (kutu seti ölçülmedi · süreler eşit · S6 ACTIVITY tek hareket eden — üçü de beyanlı) · BLOCK 0
   ⚠️ AÇIK: yüzdeler TÜRETİLMİŞ, ön görselleştirmede ölçülecek · S6 hızı (kıç 18 m / 8 sn ≈ 4,4 knot; yavaşsa ikinci kabul
      SPEC §1) · kıçın sancak köşesi %94 (UI bandı) · yapı tipi kartı YOK (liman kartı §7 uymaz — yeni kart adayı)
   → dikey_shorts/BACK_TO_WATER/

THE SWALLOWED BUS — YİRMİNCİ FİLM · İLK ŞEHİR İÇİ ALTYAPI ONARIMI · ⭐ İKİNCİ AŞAĞI BAKIŞ · İKİNCİ REJİM G · YAZILDI 19.09.2026 · ÜRETİLMEDİ ⛔
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK (varsayım — ONE MORE TURN kararı gibi) · zincirli · 8 kare + 7 I2V
   YAPI: caddede TEK çöküntü (8 × 6 m · 3,5 m): otobüs vinçle çıkar → palplanş iksa + pompa → eski hattın iki ucuna
         2 × 3,0 m Ø 1,2 boru (bilezik) → pompa gider → üç katman dolgu → söküm + son katman → asfalt + çizgi → otobüs geçer
   ⭐ VAAT: "otobüs kurtulacak mı?" değil, "bu yol yeniden otobüs taşıyabilecek mi?" — S6 rejim G: ikinci otobüs
      yürüme temposunda geçer, arka teker dikişi aşar, yama arkasında BÜTÜN (dış değerlendirme yedi düzeltmesi plana yazıldı)
   ⭐ KAMERA: karşı çatı parapeti h 18 m · D_eksen 18 m · tilt −40° (HIDDEN OASIS formülü, ikinci koşu) — gök YOK, ZEMİN ailesi;
      22 m / 7 m yatay istasyon atıldı (taban görünmüyordu). ⛔ ön görselleştirme usta kareden önce zorunlu.
   BEDEL: otobüsün kendisi (S1'de soldan gider) + kapalı cadde · ÖDÜL: S6 geçiş, yama bütün
   Işık tek gün 07:20 → 17:30 (A + 5×B = 10 sa 10 dk · G 0 dk) · G6 = G7 ışığı birebir · her G karesi tek saat/tek durum
   plan ✅ (BEŞ SORU tablosu + her I2V'de MOTION FOCUS) · QA_SPEC ✅ (§4 YÜK YOLU · §5 KATMAN/CETVEL · §7 REJİM G) ·
   KAPAK ✅ (kart yok; ⭐ YALNIZ G7 + THE SWALLOWED / BUS — öncesi/sonrası bölme 19.09.2026'da sahip kararıyla KALDIRILDI) ·
   günlük açıldı ⛔ BOŞ (⑪ aşağı bakış · ⑫ sapan · ⑬ katman · ⑭ bağlı söküm · ⑮ geçiş)
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0 · MOTION FOCUS FIX 0
   ⚠️ AÇIK: kapak kartı var mı yok mu (sahip) · başlık metni (sahip) · yüzdeler TÜRETİLMİŞ, ön görselleştirmede ölçülecek ·
      S6'da otobüs sağ UI bandından girer (kanıt yama, otobüs değil) · yapı kartı §6b yeni, ilk uygulama
   → dikey_shorts/THE_SWALLOWED_BUS/

ONE MORE TURN — ON DOKUZUNCU FİLM · İLK SU ÇARKI · ⭐ İLK REJİM G · YAZILDI 18.09.2026 · ÜRETİLMEDİ ⛔
   dikey_shorts · ızgara 6 × 8,0 = 48,0 sn · ⛔ KAPAK KARTI YOK · LOGO YOK (sahip şartı) · zincirli · 7 kare + 6 I2V
   YAPI: eski taş değirmenin yan duvarında TEK üstten beslemeli ahşap su çarkı (Ø 5,0 · 8 kol · 2 halka · 24 kova);
         demir göbek + mil duvarda KALIR, eski çark parça parça iner, yenisi aynı mile kurulur
   ⭐⭐ DEPONUN İLK GERÇEK ZAMAN SAHNELERİ — REJİM G (1×), S4–S5 (proje sahibinin onayı, 18.09.2026):
      çarkın 8 sn'de bir tur atması A/B sıkıştırmasında gösterilemez → SANTIYE_HAREKETI §1'e dördüncü rejim,
      prompt_kontrol.py'ye "moves at natural speed · eight seconds pass" imzası ve insan kuralı eklendi.
      ⚠️ ÖLÇÜLMEDİ. Gölge kıpırdamaz · dere ipek değil dalga · tek figür sırtı dönük · iz yok.
   ⭐ Sahip konsepti 12 × 10 yataydı; sahip kararıyla 6 × 8,0 dikeye çevrildi — on bir sapma sohbette
     onaylandı, plan §KONSEPT KAPISI'nda listelendi (cephe/çatı yok · dönüş saat tersi, kapak solda ·
     çark %66 en · söküm S0'da · rejim G · sırtı dönük figür · çark bağı · işaretli kol · kamera 2,0 m ·
     dere dikişi 32,0 beyanlı · vinç kelimesi yok — sehpa + çıkrık)
   BEDEL: eski çark (römork kasasında gider) · ÖDÜL: S5 bir tam tur, ıslak sol yarı / kuru sağ yarı aynı karede
   Işık tek gün 10:10 → 18:10 (4 × B = 8,0 sa · G ışık gününe 0 dk) · G4 = G5 = G6 ışığı birebir
   plan ✅ · QA_SPEC ✅ (§4 SU · §5 RİJİT DÖNÜŞ · §7 REJİM G) · KAPAK ✅ (kart yok; mil dikeyinde bölünmüş G0 | G6) ·
   günlük açıldı ⛔ BOŞ (⑭ SU · ⑮ SABİT ÇARK · ⑯ RİJİT DÖNÜŞ eklendi; ⑩ çözünürlük uygulanmaz — kurgu yok)
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0
   ⚠️ AÇIK: rejim G araçta var mı (⑭ ⑯) · G5 ≈ G6 olduğundan S5 durgun gelebilir · su kapağı tahtası sol 122 px bandında
   → dikey_shorts/ONE_MORE_TURN/

THE NARROW GORGE — ON ALTINCI FİLM · İLK BARAJ · YAZILDI 16.09.2026 · ÜRETİLMEDİ ⛔
   dikey_shorts · ızgara 7 × 8,0 = 56,0 sn · ⛔ KAPAK KARTI YOK (sahip kararı) · zincirli · 8 kare + 7 I2V
   YAPI: dar boğazda çift eğrilikli beton KEMER BARAJI · kapaklı dolusavak · dip savak · enerji kırıcı havuz
   ⭐ İKİNCİ VİNÇSİZ PLAN: beton BANT KONVEYÖRLE gelir ve OLUKTAN düşer; havada asılı yük yok [DERS 8 · 22 · 46 · 57]
   ⭐⭐ DEPONUN İLK KAMERA HAREKETİ — KURGU YAKINLAŞMASI (proje sahibinin kararı, 16.09.2026):
      HOME ana kadraj · S0 1,55× · S1 2,0× · S3 1,7× · S6 2,0× · S2/S4/S5 sabit · her sahne HOME'da başlar ve biter
      ⛔ KILAVUZ_REHBERI §1.2 ("format kimliği sabit kameradır") ve DERSLER P2-l ② ("crop push-in ALINMADI")
         AÇIKÇA GEÇERSİZ KILINDI. Karar sahibindir, ÖLÇÜLMEMİŞTİR; ① KARE ve ⑤ DEVAMLILIK hükümleri
         BEKLENEN sayılacak. Promptlar sabit kamera ister; yakınlaşma yalnız KURGUDA.
      ⛔ FORMAT ŞARTI: kaynak klipler ≥ 2160 × 3840 (2,0× için). Araç vermiyorsa tavan düşer — araç kapısı ⑨.
   ⭐ Eleştiri turundan sekiz düzeltme işlendi: ilk saniyede kırıcı kayada · bedel "denetime alınan akış +
     söğütlü kıyının kaybı" · üç su sistemi ayrıldı (geçici tünel ÇIKIŞI köprünün aşağısında · dip savak ·
     kapaklı dolusavak) · S3 kanıtı GÖZ ÇİZGİSİ (%50) oldu (köprü hizası kadrajda gerçekleşmiyordu) ·
     final "ilk kontrollü salım" (kapak S4'te yerleşir, S6'da açılır; hazne dolumu S5→S6 kesmesinde) ·
     S4 TAMAMLAR · kart kaldırıldı · finalde krette doğrudan altın ışık istenmiyor (mavi saat)
   BEDEL: dolaşan doğal akış + söğütlü çakıl bariyerleri + değirmen arkının suyu · AYNI YER: tek gözlü taş köprü
   Işık tek gün 05:30 → 19:30 (7 × rejim B = 14,0 saat ⚠️ üst sınırın TAM üstünde) · takvim KESMELERDE geçer
   plan ✅ · QA_SPEC ✅ (§7 KURGU KAPISI) · KAPAK ✅ (kart yok; bölünmüş küçük resim G0 + G7) · günlük açıldı ⛔ BOŞ
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0
   ⚠️ AÇIK KARARLAR: ışık günü 14,0 saat mi 12,5 mi · GİZLİ VAHA'nın kartı da kalksın mı · S6 fiziksel
     hareket denemesi üretilsin mi · siluet ailesi KÜTLE
   → dikey_shorts/THE_NARROW_GORGE/

THE HIDDEN OASIS — ON BEŞİNCİ FİLM · İLK RESTORASYON · YAZILDI 16.09.2026 · ÜRETİLMEDİ ⛔
   dikey_shorts · ızgara 7 × 8,0 = 56,0 + kart 5,0 = 61,0 sn · ⛔ DÜZ IZGARA (sahip kilidi) · zincirli · 8 kare + 7 I2V
   ⛔ ARA KARE YOK: her sahne tek 8,0 sn klip
   ⭐ İLK YIKIM-DEĞİL-DÖNÜŞTÜRME: yapı sıfırdan kurulmaz, VAR OLAN havuz başka bir şeye çevrilir
   ⭐ İLK AŞAĞI BAKAN İSTASYON: tilt −40° · KAMERA_ISTASYONU §3 formülü GEÇMEZ, plan kendi formülünü yazar
     (yüzde(d) = (76,87° − atan(6,0/d)) / 73,74°) · ufuk ve gök kadrajda YOK → kılavuza yeni alt kart borcu
   ⭐ KİNETİK PAKET: THE DARK ROCK'tan dokuz araç devralındı (kenar geçişi · dikey süpürme · gölge süpürmesi ·
     bulut gölgesi · üç vuruş · ödülün gecikmesi · yüzey sınırı · iz bırakan araç · ekip lekesi) + onuncu olarak
     YANSIMA. ⛔ Kamera hareketi DEVRALINMADI — DARK ROCK'ta da yoktur (sahip düzeltmesi, 16.09.2026)
   BEDEL: havuzun havuz olması (açık mavi seramik + merdiven + hacim) · AYNI YER: kemerli niş (≈99 × 134 px)
   Işık tek gün 06:20 → 18:30 · 6 × B + 1 × A = 12 sa 10 dk ≤ 14 · takvim YOK (film BİR GÜN anlatır, beyanlı)
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ (bölünmüş ızgara kapağı + G7 kartı) · üretim günlüğü açıldı ⛔ BOŞ
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0
   ⚠️ AJAN KARARLARI sahibin onayına açık: kapak kartı eklendi (dış plan kartsızdı) · rejim B+A · S1 yükü ·
     siluet ailesi "ZEMİN" önerildi (yeni aile) · tilt kartı ölçülmedi
   → dikey_shorts/THE_HIDDEN_OASIS/

THE OLD ROAD — ⭐ DEPONUN İLK YATAY (16:9) FİLMİ · YAZILDI 16.09.2026 · ÜRETİLMEDİ ⛔
   yatay_2_dk_filmler · ızgara 15 × 8,0 = 120,0 + kart 5,0 = 125,0 sn · ⛔ DÜZ IZGARA (sahip beyanı, modül 12 × 10,0)
   zincirli · 16 kare (G0…G15) + 15 I2V · ara kare YOK · bölüm sınırı G8 · QA birimi FİLM
   YAPI: itmeli beton viyadük — 420 m, 7 açıklık, 5 ayak; ⭐ tabliye KALDIRILMAZ, İTİLİR → DERS 8 · 22 · 46 · 57
     devre dışı kalır; 1 numaralı risk gövdenin sıçraması, araç kapısına ⑨ İTME TESTİ eklendi
   BEDEL: eski yolun trafiği — G0'da 14 virajda far izleri, G15'te viyadükte tek düz çizgi, virajlar boş ama OKUNUR
   DİRENÇ: kar erimesi seli — S7'de su yükselirken itme sürer ve kaya bermi dökülür, S8'de sel geçişi ve bermi
     götürür (itme DURUR), S9'da hat yeniden kurulur: çalışan hat → kopuk hat → yeniden kurulan hat
   IŞIK: tek gün 05:05 → 18:35 · 9 A + 6 B = 13,5 h ≤ 14 · ⚠️ üsluplu sıkıştırma beyanı (tek günde çekilmedi)
   TAKVİM: 627 gün ≈ 20,6 ay · iki kış, iki yaz · kar YALNIZ kar çizgisiyle (vadiye kar yağmaz)
   00_ANALIZ altı dosya ✅ · PLAN ✅ · BOLUM_1/2 ✅ · KAPAK ✅ · MUZIK ✅ · YAYIN_PAKETI ✅ · QA_SPEC ✅ · günlük ⛔ BOŞ
   ⛔ KAPI (klasör modu): BLOCK 0 · FIX 2 — kutu seti ölçülmedi · süreler eşit (ikisi de beyanlı)
   ⭐ YATAY (16:9) ilk kez: kadraj formülü, güvenli alan ve ışık günü toplamı ÖLÇÜLMEDİ — bu film onların ilk ölçümü
   ⭐ Siluet ailesi YATAY (EMPTY RIDGE · DARK ROCK DİKEY'den sonra sıradaki aile) · havuz #4
   → yatay_2_dk_filmler/THE_OLD_ROAD/

THE DARK ROCK — ON ÜÇÜNCÜ FİLM · İLK FENER · YAZILDI 15.09.2026 · ÜRETİLMEDİ ⛔
   ızgara 6 × 8,0 = 48,0 sn + kapak 5,0 · ⛔ DÜZ IZGARA (proje sahibi kilidi) · zincirli · 7 kare + 6 I2V
   ⛔ ARA KARE YOK (proje sahibi, 15.09.2026): her sahne tek 8,0 sn klip · S3'te kopan hat yalnız klip ortasında — kabul edilen risk
   ⭐ İLK VİNÇSİZ PLAN: tek düşey taşıyıcı raylı asansör kabini; uzun rijit yük havada taşınmaz [DERS 8 · 22 · 46 · 57]
   ⭐ Eleştiri turundan yedi düzeltme işlendi: fırtına = iniş hattı arızası (rampa kayar → yeniden oturur) · gövde
     fırtınadan önce biter · 900× dili (köpük ALANI, ıslak BANT) · üst iskele sökümü S4 sonunda tepeden · martı
     yalnız atmosfer · ödül ilk ışığın BELİRMESİ (huzme yok) · loop iddiası yok, 7,0 sn sonuç ekranı riski beyanlı
   BEDEL: kayanın çentikli tacı (%39 → kaide %34,5) · AYNI YER: THE NEEDLE (tek sütun, ≈200 px)
   Işık tek gün 07:00 → 19:00 (6 × rejim B = 12 saat) · takvim tarladan + deniz renginden (~6 ay) · kış yok
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ (başlık iki satır, alt bantta — ⚠️ sahip kararı) · üretim günlüğü açıldı ⛔ BOŞ
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı) · BLOCK 0
   ⚠️ DİKEY siluet ailesi — THE EMPTY RIDGE ile ARDIŞIK yayınlanamaz (YAYIN_PLANI §3) · havuz #11
   → dikey_shorts/THE_DARK_ROCK/

THE EMPTY RIDGE — ON İKİNCİ FİLM · İLK TÜRBİN · ÜRETİLDİ ✅ (günlüksüz ⛔) · 12/12 mercek ✅ · 11'i RUN INCOMPLETE ⛔
   ızgara 7 × 8,0 = 56,0 sn + kapak 5,0 · ⛔ DÜZ IZGARA (proje sahibi kilidi) · zincirli · 8 kare + 7 I2V
   ⛔ Kurgu 8 klip varyanslı, plana oturmuyor; kesme_kontrol.sh koşulamadı (teslim.mp4 depoda yok)
   ⭐ GEÇEN: ⑤ SAME WORLD (meşe) · ⑧ MADE 9,1 · ⑫ SOLID · ⑥ RHYTHM · ③ PASSES (tahmin tuttu) · ⑨ · 12/12 kart SAME
   ⛔ DÜŞEN: ① SIX SEPARATE SHOTS (push-in + 4 istasyon) · ② DIFFERENT (hayalet kuleler) · ⑩ MAGIC · ⑪ · ④
   → KARAR: yayınlanmaz · YENİDEN ÜRETİLİR (yeniden yazılmaz): plan tutuyor, üç cümle düzeltilir
     (DERS 55 · 56 · 57) — önce ARAÇ KAPISI (⑨ vinç testi) + ÖN GÖRSELLEŞTİRME + GÜNLÜK · tek istasyon.
     RAPORLAR/THE_EMPTY_RIDGE.md §9 · kapak başlığı üst %12,5'te → KAPAK.md bandına çekilir
   ⭐ DİKEY siluet ailesi (YAYIN_PLANI §3 sırası: OVER THE WALL KÜTLE → DİKEY) · havuz #5
   ⭐ DERS 22'yi İSTASYONLA çözen ilk vinçli plan: kamera pad'in +100 m üstünde, göz çizgisi = göbek (%50),
     bom başı %55 < uzak sıradağ silueti %57 → bütün kaldırmalar DAĞA karşı; SAHA ŞARTI (+6°) ve ön
     görselleştirme adımı plana yazıldı. DERS 51 (iş yüzeyi adı + yüzde) · 52 (tek istasyon) · 53 (dar
     yüzeyde tek araç) · 54 (kuru katlı ilk hâl) bu planın doğduğu gün kılavuza indi ve uygulandı.
   ⭐ Işık tek gün 06:00 → 20:00 (7 × rejim B 2 saat = 14 saat, TUTARLI) · takvim tarladan (9,5 hafta) ·
     bilinçli sıkıştırma beyanlı. Kış yok.
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ · üretim günlüğü açıldı ⛔ BOŞ
   ⛔ KAPI: FIX ×2 (kutu seti ölçülmedi · süreler eşit — ikisi de beyanlı)
   ⚠️ Plan bu ölçümden sonra DÜZELTİLMEDİ — üç cümle (S5 göbek · SITE "only turbine" · S2–S5 kaldırma
     yolu) yeniden üretimden önce plana yazılır; kart A adım 8 yeniden koşulur.
   → dikey_shorts/THE_EMPTY_RIDGE/

OVER THE WALL — DOKUZUNCU ÜRETİLEN FİLM · İLK BARAJ · 14.09.2026
   plan 8 × 8,0 = 64,0 + kapak 5,0 (14.09 · ⛔ DÜZ · proje sahibi kilidi) · zincirli · 9 kare + 8 I2V
   ÜRETİLDİ ✅ (günlüksüz ⛔) · 12/12 mercek koşuldu ✅ · 11'i RUN INCOMPLETE ⛔ · kapak kartı VAR
   ⛔ Kurgu 7 klip, hiçbir plan sürümüne oturmuyor; kesme_kontrol.sh koşulamadı (teslim.mp4 depoda yok)
   ⛔ Zincir hükümleri düştü: ⑤ REBUILT 6/6 · ⑧ APPEARED 0/4 · ② APPEARING (8.) · ⑦ PARKED · ⑩ MAGIC
   ⭐ GEÇEN: ⑥ TIME · RHYTHM (varyanslı kurgu) · 12/12 END CARD SAME · ① CAMERA LOCK 9 · ③ CARRIER 10
   → KARAR: yayınlanmaz · yeniden ÜRETİLMEZ — önce ARAÇ KAPISI + GÜNLÜK + ZİNCİR.
     Yeniden üretilecek: S2 (kuru katlı platform) · S3 BÜYÜR (filmde yok) · S4–S5 (döşekte makine) ·
     tek istasyon · dar yüzeyde tek araç. Dersler 51-54 · RAPORLAR/OVER_THE_WALL.md §9
   ⚠️ IZGARA: ⑥ varyanslı kurguda RHYTHM dedi (CROSSING'den sonra 2. kez) — 8 × 8,0 düz kilit
     proje sahibine geri soruldu; plan DEĞİŞTİRİLMEDİ.

BEFORE NIGHTFALL — YEDİNCİ FİLM · ⛔ HENÜZ ÜRETİLMEDİ
   ızgara 6 × 8,0 = 48,0 sn + kapak 5,0 · ⛔ DÜZ IZGARA (proje sahibi kilidi)
   ⭐ İLK KARA DELİK SAHASI · havasız kayaç ova · saha kartı YOK
   ⭐ FORMATI İLK KOŞAN FİLM: İKİ KEYFRAME ZİNCİRİ — 7 görsel · 6 klip · her
     klip iki onaylı kareye kilitli; dikişin iki yakası AYNI KARE.
     08.09.2026'da bu yöntem DEPONUN FORMATI oldu [KILAVUZ_REHBERI §2.7];
     bu film onun ilk uygulamasıdır. Kesme artık zaman sıçraması değil:
     film TEK GÜNDÜR (12,0 yerel saat).
   plan ✅ · QA_SPEC ✅ · KAPAK ✅ · üretim günlüğü ⛔ AÇILMADI (üretim günü açılır)
   ⛔ KAPI: BLOCK ×1 (süre eşitliği — BİLİNÇLİ, plan §1.2) + FIX ×8
     (7'si prompt_kontrol §9 ↔ DERS 35 çelişkisi · 1'i ölçülmemiş kutu seti)
   ⛔ ÜRETİM AÇILMAZ: araç kapısı yedi ölçümü koşulmadı [ARAC_KARTLARI §4].
     İlk ölçüm bu filmde VAR/YOK sorusudur — kutu seti {4,6,8} çıkarsa 8,0 sn
     tek klipte teslim edilemez (tavan 7,00 sn) ve ızgara yeniden açılır.
     ⭐ SEKİZİNCİ SORU ARTIK KILAVUZDA [ARAC_KARTLARI §4 ölçüm 8]: araç İKİ
     KAREYLE (ilk+son) çalışıyor mu? Çalışmıyorsa bu FORMAT o araçta
     üretilmez — plan düşürülmez, araç değişir.
   ⭐ BU FİLM ÜÇ ÖLÇÜLMEMİŞ ŞEYİ İLK KEZ SINAR: DERS 36'nın oran kapısı
     (tam hâl/ara hâl < 1) · zincirin GEOMETRİ kanalı [A3-d] · DERS 44'ün
     tersi (kusursuz dikişte düz ızgara ⑥'yı düşürür mü).
   → dikey_shorts/BEFORE_NIGHTFALL/ · ölçüm yok, satır yok: mercek tablolarına
     film ÜRETİLMEDEN satır yazılmaz [kart Q ön koşulu].

THE LONG DAY
   ızgara 10 sahne · plan 6·4·6·4·6·6·8·4·6·10 · ⛔ KURGU 10 × 6,0 DÜZ kesildi
   ⭐ İLK UZAY SAHASI · İLK SEKİZ MERCEKLİ ÖLÇÜM · kapı üretimden ÖNCE ✅ GO
   ÜRETİLDİ ✅ · 8/8 mercek koşuldu ✅ · ⛔ SEKİZİ DE RUN INCOMPLETE (karesiz/belgesiz)
   ⛔ ÜRETİM GÜNLÜĞÜ YOK — plan ile film ayrıştı (astronot · güneş kadrajda ·
     dikey habitat · ikiz kule) ve sebebi kayıtta değil [DERS 28]
   ⭐ GEÇEN: ① TIMELAPSE (kamera·kadraj·çapa·istasyon 10/10) · ⑤ SAME WORLD +
     kanıt nesnesi BULUNDU (kaya + krater) · ④ ONE THING ilk kez bulundu ·
     ③ SEASON CARRIER 10 mevsimsiz sahada · ⑥ TIME
   ⛔ DÜŞEN: ② DIFFERENT·APPEARING (5.) · ③ NOT IN ONE DIRECTION (güneş
     kadrajda, gölge donuk) · ⑥ METRONOM (4.) · ⑦ PARKED · ⑧ APPEARED 1/9 ·
     ① PEOPLE 0 · SURFACE 0 · beş mercekte END CARD DIFFERENT
   → KARAR: yayınlanmaz · yeniden üretilmez · Dersler 28-34 ·
     RAPORLAR/THE_LONG_DAY.md §5

THE MOUNTAIN DOOR
   ızgara 5 × 6,0 (DÜZ — proje sahibi kilidi) · depo İÇİNDE yazıldı, GPT yok
   ⭐ KAPI ÜRETİMDEN ÖNCE KOŞULDU: ✅ GO — deponun dört filminde İLK KEZ
   ÜRETİLDİ ✅ · 6/6 mercek koşuldu ✅ · kapak kartı VAR
   ⛔ ALTI HÜKMÜN ALTISI DA DÜŞTÜ:
        ① SIX SEPARATE SHOTS   ② DIFFERENT · APPEARING (4. kez)
        ③ PASSES BUT NOT IN ONE DIRECTION
        ④ ENDS · NONE FOUND (4. kez)
        ⑤ A SET REBUILT EACH TIME · kanıt NONE FOUND
        ⑥ NEXT · METRONOM (3. kez)
   ⭐ GEÇEN: ③ SEASON CARRIER 10/10 · VEGETATION 10/10 · SHADOW/SUN 8/10 ·
     zaman tahmini "9-12 ay" — plan 12 ay, İKİNCİ KEZ TUTTU.
   ⛔ KÖK SEBEP DEĞİŞTİ — artık prompt mimarisi DEĞİL, ÜRETİM AKIŞI:
     ① CAMERA LOCK 0/10 · beş klipte de push-in. Ölçülebilir çapa cümlesi
     beş I2V'de de VARDI; NARROW LOT'ta aynı cümle 10/10 almıştı → araç
     ön ayarı [DERS 23]. Zincir tutmadı: 4/4 dikişte kusur, plana kasten
     konan kanıt nesnesi İLK dikişte kayboldu [DERS 25].
   ⛔ ÖLÇÜLEN HİPOTEZ DÜŞTÜ: klip içi vuruş varyansı metronomu kırmadı —
     ⑥ RHYTHM 0/10, deponun en düşüğü [DERS 24].
   ⛔ DERS 17 İKİNCİ KEZ: SPEC üretimden ÖNCE hazırdı ve mercekler yine
     belgesiz koştu (6'nın 5'i eksik girdi). Eksik olan belge değil,
     koşu YORDAMI [DERS 27].
   → KARAR: yayınlanmaz. Yeniden ÜRETİLMEZ — önce ARAÇ KAPISI ve ZİNCİR.
     Dersler 23-27 · RAPORLAR/THE_MOUNTAIN_DOOR.md §8

THE NARROW LOT
   ızgara 5 × 6,0 · MOTOR_5_SAHNE'nin ilk koşusu · harici GPT
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
