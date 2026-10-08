# MERCEK 2 — YAPI: TEK BİNA, SIRASIYLA İNŞA EDİLMİŞ

## GİRİŞ KONTROLÜ

ŞARTNAME DOKÜMANI SUPPLIED (`THE_IRON_BRIDGE — QA SPEC` sunuldu). Şartnamede değişken değerlerin bir kısmı taslak (`⬜`) olarak yer aldığından, tanımlı ilkeler dışındaki ölçümlerde iç tutarlılık esasına (Mod D / İç Tutarlılık Destekli) göre değerlendirme yapılmıştır.

---

## KÜNYE (SLATE)

```
FİLM BAŞLIĞI          THE_IRON_BRIDGE
ŞARTNAME              TEDARİK EDİLDİ (SUPPLIED) → Mod D
YAPI TİPİ             Kemer Köprü (Arch Bridge)
KLİP SAYISI           12 Sahne Klipi + 1 Kapak Kartı
SAHNE BLOĞU           00:00 - 02:00 (12 Klip × 10,0 sn = 120,0 sn)
KAPAK KARTI           MEVCUT (02:00 - 02:05 / Video süresi: 02:16 - 02:20)
BEYAN EDİLEN AŞAMALAR Şartnamede taslak (⬜)
GÖZLEMLENEN AŞAMALAR  S00: Saha temizliği ve kazı
                      S01: Geçici ahşap servis köprüsü ve sağ ayak donatısı
                      S02: Beton kenar ayağı dökümü ve çelik destek kuleleri
                      S03-S04: Çelik kemer segmentlerinin vinçle montajı
                      S05: Kış dönemi / Kemerin aniden kaybolması ve yeniden başlanması
                      S06: Kemerin tepe birleşimi ve askı halatlarının montajı
                      S07: Tabliye kaplaması ve korkuluklar
                      S08: Yaklaşım yolu kilit taşı kaplaması ve söküm
                      S09-S11: Tamamlanmış köprü, peyzaj ve çevre düzenlemesi
AŞAMA UYUŞMAZLIĞI     S04'te (00:40-00:50) monte edilen çelik kemer, S05'te (00:51-00:54) aniden kaybolmuş, 00:55'te tekrar monte edilmeye başlanmıştır.
```

---

## SKORLAR (SCORES)

```
1 YAPI KİMLİĞİ (STRUCTURE IDENTITY)    8/10
2 MONOTONIK BÜYÜME (MONOTONIC GROWTH)  2/10
3 ÖLÇEK KİLİDİ (SCALE LOCK)            7/10
4 İNŞA SIRASI (BUILD SEQUENCE)         5/10
5 YÜK YOLU VE DESTEK (LOAD PATH)       6/10
6 GEÇİCİ EKİPMAN (TEMPORARY EQUIPMENT) 5/10
7 MAKİNE VE YÖNTEM (MACHINERY/METHOD)  7/10
8 GEOMETRİK STABİLİTE (STABILITY)      7/10
C1 İKİNCİL AÇI (SECONDARY VANTAGE)     UYGULANMADI (NOT TRIGGERED)
C2 KAZI (EXCAVATION)                   8/10
C3 SAHADA SU VARLIĞI (WATER)           7/10
ORTALAMA PUAN                          6.0 / 10
```

---

## BULGULAR (FINDINGS)

* **[2 MONOTONİK BÜYÜME] [00:51.0]** *Şartname İlkesi: "İşlenmiş imalat geri alınamaz / yok olamaz."* — S03 ve S04 (00:30–00:50) boyunca monte edilen ana çelik kemer strüktürü, S05 klip açılışında (00:51–00:54) aniden tamamen yok olmuş, nehir yatağında sadece geçici kafes kuleler kalmıştır.


* **[4 İNŞA SIRASI] [00:55.0]** *Şartname İlkesi: "Yapım sırası mantıksal mühendislik adımlarını takip etmelidir."* — 00:55 zaman damgasında sepetli vinç ve ana vinç ile çelik kemer segmentleri, daha önce S04'te bitirilme aşamasına gelmiş olmasına rağmen sıfırdan tekrar monte edilmektedir.


* **[6 GEÇİCİ EKİPMAN] [00:20.0]** *Şartname İlkesi: "Geçici ekipman söküm süreci kadrajda görünmeli veya tutarlı geçmelidir."* — S01'de (00:10–00:20) nehri geçen geçici ahşap servis köprüsü, S02 (00:20) başlangıcında herhangi bir söküm işlemi gösterilmeksizin klip arasında aniden kaybolmuştur.


* **[8 GEOMETRİK STABİLİTE] [00:52.0]** *Şartname İlkesi: "Kare içi yapılar zaman geçtikçe formunu korumalıdır."* — S05 kış sahnesinde nehir akıntısı ve arka plandaki ağaç dokularında hafif kadraj kayması ve yüzey yüzmesi ("swimming") gözlemlenmektedir.



---

## ÖLÇEK KİLİDİ TABLOSU (SCALE LOCK TABLE)

| Milat / Aşama | Stated % (Şartname) | Observed % (Gözlemlenen) | Difference (Fark) |
| --- | --- | --- | --- |
| Arazi / Kazı Hazırlığı | ⬜ | %0 (00:00 / S00) | Belirtilmedi |
| Beton Kenar Ayağı Tamamlanma | ⬜ | %20 (00:25 / S02) | Belirtilmedi |
| Çelik Kemer Birleşimi (1. İmalat) | ⬜ | %65 (00:48 / S04) | Belirtilmedi |
| Kemer Yeniden Birleşimi (Final) | ⬜ | %100 (01:05 / S06) | Belirtilmedi |
| Tabliye ve Yol Tamamlanma | ⬜ | %100 (01:25 / S08) | Belirtilmedi |

---

## KARAR (VERDICT)

```
IS IT THE SAME BUILDING?    SAME (AYNI BİNA)
IS IT BEING BUILT?          BUILT (İNŞA EDİLİYOR)
```

Film genel hatlarıyla aynı çelik kemer köprünün sahadaki aşamalı inşasını ve montaj yöntemini başarıyla temsil etmektedir. Ancak 00:51–00:54 (S05) arasında daha önce yükselmiş olan ana çelik kemerin aniden yok olması ve 00:55'te tekrar monte edilmeye başlanması ciddi bir monotonik büyüme hatası oluşturmaktadır. Bu kritik kesinti dışında köprü geometrisi, beton ayaklar ve çevre peyzajı tutarlıdır.

```
END CARD: does it show the same building as the last scene?  SAME (AYNI)
```

(02:16–02:20 arasındaki statik kapak kartı, S11'deki tamamlanmış köprü strüktürü ve peyzaj ile birebir aynı yapıyı göstermektedir.)
