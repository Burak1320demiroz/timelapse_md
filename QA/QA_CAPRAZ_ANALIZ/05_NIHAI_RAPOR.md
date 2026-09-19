# 🏆 QA Çapraz Analiz Nihai Raporu ve Aksiyon Planı

> **Tarih:** 18.09.2026  
> **Kapsam:** Depodaki 15 dikey Shorts filminin 132 ham QA raporunun (130 puanlı + 2 INC) sentezi, çıkarılan dersler ve yapım kalitesini yükseltecek önceliklendirilmiş aksiyon planı.

---

## 1. Yönetici Özeti (Executive Summary)

`QA/HAM_RAPORLAR/` dizininde yer alan 15 dikey Shorts filminin 132 adet ham değerlendirme raporu (130 puanlı + 2 INC; aynı 15 filmin 12 mercekte tekrar okunması, bağımsız deney değil) çapraz analize tabi tutulmuştur. Elde edilen veriler sistem genelinde kaliteyi düşüren **3 ana zafiyet alanını** ortaya koymuştur:

1. **İnşa ve Nedensellik Çöküşü (İnşa %60,0 = 9/15 · Sebep %80,0 = 4/5, yalnız 5 puanlı film):**  
   Filmlerin çoğunda yapı elemanlarının sahadaki araç veya insan müdahalesi gösterilmeden kendiliğinden belirdiği (`MAGIC`), eriyerek genleştiği (`MORPHING`) veya havada süzüldüğü tespit edilmiştir. `② İNŞA` (3.83/10) ve `⑩ SEBEP` (4.24/10) en düşük puanlı merceklerdir.

2. **Durağan Şantiye ve Heykel İnsanlar (⑦ İŞ %54,5 = 6/11 · ⑧ YÖNTEM %54,5 = 6/11):**  
   Promptlarda insan ve araçlar beyan edilmesine rağmen, yapay zeka modelleri araçları "park edilmiş" (`PARKED`), insanları ise "donmuş heykel" olarak üretmektedir.

3. **Otomatik Kapı Betiklerinin Yetersizliği:**  
   Metin düzeyinde kılavuzlarda yer alan kuralların (örneğin %25/%50/%75 ara hâl aşaması veya düz ızgara kuralı) kapı betikleri (`prompt_kontrol.py`) tarafından otomatik denetlenmemesi nedeniyle hatalar üretim aşamasına sızmaktadır.

---

## 2. Önlem Tablosu ve Uygulama (revize · 18.09.2026 dış değerlendirme sonrası)

> [!IMPORTANT]
> İlk sürümün aksiyon planı "prompta etiket koyunca sorun çözülür" varsayımına
> dayanıyordu. Etiket **planlama** kontrolüdür; görüntüde doğru eylemin oluştuğu
> ayrıca doğrulanır (`QA/00_README.md §7 ÜÇ AŞAMA`). Aşağıdaki tablo bu düzeltmeyle
> yeniden yazıldı; §2.2 hangi önerinin neden değiştiğini kayda geçirir.

### 2.1 On arıza kalıbı — üretim öncesi önlem · çıktıda kabul kanıtı

| arıza | üretim öncesi önlem | çıktıda kabul kanıtı | öncelik | nerede |
|---|---|---|---|---|
| **F01 — Nedensiz montaj** | Beş soru kartında malzeme kaynağı ve taşıyıcı yazılır; tek ana iş seçilir; I2V `MOTION FOCUS` paragrafı | Ana parçanın kaynağı ve yerine ulaşması anlaşılır; ⑩ "MAGIC" yok | 🔴 çok yüksek | `SAHNE_PLAN_KARTI` · `PROMPT_SABLONU §2` · `prompt_kontrol.py §10e` |
| **F02 — Atıl şantiye** | Her klibe görünür SONUÇ üreten görev (araç sayısı değil, iş sonucu); yükü tutan vinç beklerken PARKED sayılmaz | Yapıda ya da malzemede görünür değişim var | 🔴 yüksek | `SANTIYE_HAREKETI §4 İŞE BAĞLI HAREKET` |
| **F03 — Eşit kesmeler** | Süre denetimi DEĞİL — klip içi ilerleme ve tekrar denetimi (sahne süresi sahip kuralıyla sabit) | Benzer sürelerde FARKLI sonuçlar / gerilim aşamaları | 🟡 çıktıya bağlı | `KILAVUZ_REHBERI §2.2 karşı kayıt` · `KURGU_VE_TESLIM §2.4` |
| **F04 — Kamera kayması** | Onaylı referans + 3 sabit nirengi + oransal px eşiği; her kare önceki VE ana referansla | Arka plan, yapı köşesi, ufuk beklenen konumda | 🔴 çok yüksek | `KAMERA_ISTASYONU §7` · `zincir_kontrol.sh` (3. argüman) |
| **F05 — Sıvı büyüme** | Parçalar önceden tanımlı; bütün yapı tek dönüşüme yüklenmez (MOTION FOCUS ≥3 eleman → FIX) | Parçalar boyunu korur; ilerleme ekleme/işleme yoluyla | 🔴 çok yüksek | `prompt_kontrol.py §10e` · `INSAAT_YONTEMI §3` |
| **F06 — Donmuş işçiler** | Az sayıda, ana işi destekleyen görevli; kalabalık yok (ACTIVITY >4 hareket eden → INFO) | İşçi hareketi anlaşılır; heykelimsi figür yok | 🟡 sahneye bağlı | `SANTIYE_HAREKETI §4` · `PROMPT_SABLONU ACTIVITY` |
| **F07 — Gölge sıçraması** | Bir gün mü çok gün mü belirlenir; ışık buna göre (rejim beyanı) | Zamanın ilerleyişi anlaşılır; istemsiz yön değişimi yok | 🟡 orta | `SANTIYE_HAREKETI §1-2` · `ZAMAN_VE_ISIK` (değişmedi) |
| **F08 — Bağsız yük** | Yükün taşıyıcıyla ilişkisi başlangıçta kurulur (beş soru ②③); bağlantı kadrajda okunur (≥0,5 m) | Destek ve bağlantı sahne ölçeğinde görünür | 🔴 çok yüksek | `SAHNE_PLAN_KARTI §3` · `FIZIK_VE_AGIRLIK §5` (değişmedi) |
| **F09 — Kapak uyuşmazlığı** | Finalde gösterilecek sonuç senaryoda kesinleşir; açılış-kapak-final yan yana okunur | Kapak/başlıkta vaat edilen dönüşüm filmde gerçekleşir | 🔴 çok yüksek | `MUZIK_VE_KAPAK §5` · `KILAVUZ_REHBERI §8 adım 2b` |
| **F10 — İstenmeyen metin** | Kaynak görsel temiz tutulur; üç durum (uydurma yazı · kaynak izi · hizmet filigranı) ayrı teşhis | Anlamsız yazı ya da marka izi yok | 🟢 görünürlüğe bağlı | `KILAVUZ_REHBERI §7` (F10 notu) |

### 2.2 İlk sürümden vazgeçilen öneriler — ve neden

| ilk sürüm önerisi | ne oldu | gerekçe |
|---|---|---|
| `[CAUSATION]` `[JOINERY]` `[HUMAN MOTION]` üç zorunlu etiket, BLOCK | → `MOTION FOCUS` paragrafı (FIX) + beş soru kartı; joinery yalnız ≥0,5 m ise | Üç etiket aynı soruyu üç yerde sorar; köşeli parantez etiketi kapı zaten BLOCK'lar (`prompt_kontrol.py` §2b); <0,5 m ayrıntı kadraja inmez (`INSAAT_YONTEMI §1`). BLOCK değil FIX: ölçülmedi, 19 film kırılmasın |
| Tüm promptlara kilitlenecek evrensel `NEGATIVE` bloğu | → sahneye özgü 1-3 kısa dışlama; çekirdek kısa | 15 filmde çekirdek her prompta yapıştırıldı, F01/F04/F05 yine geldi; negatif doğru eylemin yerini tutmaz (`KILAVUZ_REHBERI §7`) |
| 5 klipte de süreler eşitse METRONOM BLOCK | → REDDEDİLDİ | Sahip kuralı: dikey shorts sahne süresi sabit; FIX beyanlıdır. Ritim klip içi ilerlemeyle taşınır (`§2.2 karşı kayıt`) |
| "Araçların en az %50'si hareket izi (egzoz · toz) taşısın" | → işe bağlı hareket; toz/egzoz kanıt değil | OVER_THE_WALL: ENVANTER 9,3 · YÖNTEM 0,0 — araç varlığı ≠ yapıyla bağ (`SANTIYE_HAREKETI §3-4`) |
| `zincir_kontrol.sh` "10 px kayma otomatik red" | → oransal eşik (genişlik × oran) + 3 nirengi elle; betik px eşiğini basar | Betik SSIM ölçer, piksel ölçmez; "10 px" depoda hiç yoktu — ölçülmüş kural 2 px @ 1080'di ve dört yerde kopyalanmıştı, tek yere indi (`zincir_kontrol.sh ESIK_KAYMA_ORAN`) |
| `ARAC_KARTLARI`'na "Araç Yük Bağlantı Testi" 9. ölçüm | → alınmadı; beş soru ②③ karşılar | Araç kapısı aracın davranışını ölçer, sahnenin planını değil |
| `INSAAT_YONTEMI`'ne "Malzeme Birleşim Şartı" | → alınmadı; beş soru ③ + `FIZIK_VE_AGIRLIK §5` temas cümlesi zaten ister | Aynı kuralı ikinci yerde tutmak, birini yanlış tutmaktır (AGENTS §3 ①) |
| `qa_paket.sh` günlük şartı korunsun | ✅ korundu (değişiklik yok) | — |

### 2.3 Film bazlı müdahale öncelik sırası

Öncelik en düşük ortalamadan çok **en kritik arızanın yeniden üretim maliyetine** göre.
Yeniden üretim kapsamı (sıfırdan mı, yalnız I2V ve montaj klibi mi) **sahip kararıdır**
(`06 §5`); üretim onay-önce-üretim kuralına tabidir.

| öncelik | film | dikkat çeken bulgu | ilk müdahale |
|:-:|---|---|---|
| 1 | THE_CLOSING_SPAN | İnşa 0,0 · Devamlılık 0,0 | Köprü açıklığı + sabit destekleri yeniden planla; tek birleşim hareketini pilot klipte ÖNCE doğrula (§8 adım 2b) |
| 2 | BUILT_FROM_DUST | Kare 1,1 · Yöntem 0,0 · Devamlılık 1,6 | Ana referansı düzelt (3 nirengi); bütün yapı yerine okunur parça ekleme klibi dene |
| 3 | THE_DUST_YEAR | İnşa 0,9 · Yöntem 0,0 · İş 1,3 | Sıvı büyümeyi ortadan kaldıracak fiziksel parça/işleme düzeni (beş soru ①③) |
| 4 | THE_MOUNTAIN_DOOR | Devamlılık 0,2 · Kare 1,1 | Kaya ve kapı çevresinin kimliğini sabitle (nirengi = kaya köşeleri) |
| 5 | THE_LONG_SHADOW | İnşa 0,4 · yalnız 4 mercek | Ana inşa olayını düzelt; eksik mercekleri tamamla (ortalaması güvenilmez) |
| 6 | BEFORE_NIGHTFALL | İnşa 2,1 · Yöntem 2,5 · Teslim 2,8 | Taşıma-montaj-final ilişkisini sadeleştir (tek ana iş / klip) |
| 7 | OVER_THE_WALL | Envanter 9,3 · Yöntem 0,0 · Sebep 1,3 | **Mevcut ekipmanı yapı değişimine bağla** — yeni araç ekleme öncelik değil |
| 8 | THE_DARK_ROCK | Katılık 2,4 · Zaman 2,8 | Kaya/zemin değişimini açıklanabilir yap |

> `OVER_THE_WALL` en öğretici örnektir: ekipmanın sahada bulunması ≠ oluşan yapıyla
> bağlantısının gösterilmesi. "Daha fazla araç ekle" yaklaşımının neden yeterli
> olmadığını gösteren en net veri.

---

## 3. Sonuç — ölçülecek pilot hedef (sayı vaadi değil)

İlk sürüm "%73-80 başarısızlık %15'in altına düşürülecektir" yazıyordu. Bu iddianın
deneysel dayanağı yoktu ve üst sınırı da yanlıştı (İnşa %73,3 değil %60,0); kaldırıldı.
Yerine **ölçülecek** üç kapı:

```
① PİLOT ÜÇLÜ      bir sonraki filmin ilk teslimi ÜÇ PARÇADIR (KILAVUZ_REHBERI §8 adım 2b):
                  · onaylı sabit referans karesi — 3 nirengi işaretli
                  · pilot klip — en zor montaj hareketi gerçekten oluşuyor (beş soru dolu)
                  · çalışan final — vaat edilen sonuç görülüyor
                  Üçü onaylanmadan kalan senaryo üretilmez.
② İLK ÖLÇÜM       o filmde ② İNŞA ve ⑩ SEBEP 4,0 üstü mü; OLAY TABLOSU'nda F01/F05/F08
                  kaydı var mı. Tek film kural üretmez — üç film aynı yönde (YAYIN_PLANI §6.2).
③ İZLEYİCİ        6 filmlik tek değişkenli dizi ve 7. gün karşılaştırması → 06_IZLEYICI_DENEY_PLANI.
```

Uygulanan kılavuz/betik değişiklikleri `kilavuzlar/DERSLER.md` ÇAPRAZ ANALİZ bölümünde
(C1-a…h) VARSAYIM olarak kayıtlıdır; ilk üretimden sonra ya derse dönerler ya düşerler.

*Yeniden üretim kapsamı, deney dizisinin başlangıcı ve Analytics erişimi için proje
sahibinin kararı beklenmektedir (06 §5).*
