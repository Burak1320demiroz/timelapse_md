# 🔍 ORBITAL SCAFFOLD — QA Spesifikasyonu (Kilit Listesi)

> Bu dosya üretimden **ÖNCE** hazırlanır. Mod D mercekleri (②, ④, ⑥, ⑧) koşulurken QA uzmanının bakacağı **TEK** belgedir. Planın kendisi QA'ya verilmez [DERS 17].

---

## 1. ⛔ FİNAL KARE KANITI (ZORUNLU)

Film bitiminde yapının tamamlandığının ve teslimin gerçekleştiğinin reddedilemez fiziksel kanıtı.

**FİNAL KARE (S9'un son saniyesi) ŞUNLARI GÖSTERMEK ZORUNDADIR:**
1. **Habitat Aydınlatması:** Habitat silindirinin dar dikey pencerelerinden net, parlak iç mekân ışığı dışarı vurmalıdır. Bu ışık, dışarıdaki regolit üzerine sert havuzlanmış ışık düşürmelidir.
2. **Karanlık Mars Gökyüzü:** Gökyüzü koyu alacakaranlık mavisi/siyahı olmalı (pre-dawn), güneş diski veya aydınlık bir gökyüzü görünmemelidir.
3. **Panel Dizileri:** İki sıra güneş paneli dizisi (her biri 12 panel) tam olarak yerinde ve bozulmamış formda olmalıdır.
4. **İletişim Direği:** 6 bölümlük direk ve çanak yerinde durmalıdır.
5. **İnsansız Çalışma:** Ortamda dış mekân aydınlatması olmasına rağmen, net veya odaklanmış tek bir insan/astronot figürü dahi görünmemelidir.

Bu beş maddeden BİRİ BİLE görünmüyorsa, film **TESLİM EDİLMEMİŞ** sayılır ve ④ TESLİM merceğinden FİNAL BEAT FAIL alır.

---

## 2. AŞAMA BÜYÜME KİLİTLERİ (⑧ YÖNTEM İçin)

Her elemanın ekranda DOĞDUĞU (belirdiği değil, ara hâlde yapıldığı) anlar. ⑧ YÖNTEM merceği burayı arar:

*   **İniş Pedi:** %25'i S0'da ham bıçak izleriyle başlar. S1'de karolar sinterlenir. S0'dan S1'e alan DOĞARAK büyür.
*   **Temel:** S2'de çukur olarak başlar ve derinliği artar.
*   **Habitat:** S3'te derin kumaş kırışıklıklarıyla yarı şişmiş olarak belirir. S4'te tam şişmiş formunu alır.
*   **Radyasyon Siperi (Berm):** S4'te 4 sıra tüp yüksekliğindedir.
*   **Güneş Panelleri:** S4'te dizilmeye başlar. S5 fırtınasında kararır ve iki panel eksilir. S6'da onarılıp çerçeveye 20 panel tamamlanır.
*   **İletişim Direği:** S7'de alt 3 bölümü ve yerde yatan gergi telleriyle görünür.
*   **Bağlantı Tüpü:** S8'de şişerek belirir ve gerginleşir.

*(Bu adımlar dışındaki ani belirmeler, ⑧ APPEARED cezasını tetikler).*

---

## 3. İSTASYON KİLİTLERİ (② İNŞA İçin)

Bu film **TEK BİR İSTASYON GRUBUNDAN (ANA İSTASYON)** çekilmiştir. Detay istasyonu yoktur.
Tüm klipler (10 klip) A İstasyon grubuna aittir.

**Çapalar:**
- **Sağda:** 4m boyunda, düz üst yüzeyli yarı gömülü koyu bazalt blok. (Her sahnenin THE TIME MOMENT ölçümü buna göredir).
- **Solda:** Üzeri tozlu ince yatay kaya sırtı.
- **Arkada (Ufukta):** Üç sivri mesa silüeti.

*Eğer herhangi bir sahnede (S0-S9) bu üç çapa aynı boyutta, aynı formda ve aynı konumda görünmüyorsa, film ① ANCHOR IDENTITY ve ② GEOMETRIC STABILITY merceklerinden düşer.*

---

## 4. DÜNYA VE FİZİK (①, ⑤ İçin)

- **Mars Fiziği:** Gökyüzü gündüzleri "butterscotch" (sarı-kahve), geceleri koyu mavidir. Beyaz bulut veya mavi gökyüzü görünemez.
- **Toz Fırtınası (S5):** Işık tamamen düzleşir, gölge kaybolur. Paneller tozla kaplanır.
- **Robotik Makine:** Hiçbir makinenin camlı kabini, koltuğu veya insan için tasarlanmış tırabzanı yoktur. Hepsi kapalı ("sealed") robotik ünitelerdir.

## 5. QA_SPEC KONTROLÜ (Üretim Öncesi)
- [x] Final Kare Kanıtı net ve sayısal mı?
- [x] Aşama kilitleri ara hâlleri tanımlıyor mu?
- [x] Çapalar yerli yerinde mi?
