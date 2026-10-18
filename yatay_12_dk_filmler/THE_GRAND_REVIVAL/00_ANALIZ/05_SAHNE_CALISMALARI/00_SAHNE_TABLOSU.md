# 🧮 THE_GRAND_REVIVAL — SAHNE TABLOSU (sahne başına BİR satır · 90 satır + usta kare)

> Betikten üretilir (`grv_gen.py`); elle satır eklenmez. BEŞ SORU [SAHNE_PLAN_KARTI]: ① malzeme başlangıçta nerede ·
> ② taşıyıcı · ③ nereye oturur · ④ klip sonunda ne değişti · ⑤ ne sabit. KAPI ✅ = beşi cevaplı, prompt yazıldı.
> ⭐ Çok istasyon: ⑤ her istasyonun kendi ölçü çapasıdır (COMPOSITION'daki px cümlesi + I2V 'same width').

| S | İST | REJİM · SAAT · AZ/EL | AŞAMA FİİLİ | ① kaynak · ② taşıyıcı · ③ hedef | ④ ne değişti (hedef kare) | ⑤ ne sabit (ölçü çapası) | KİLİT | KAPI |
|:--:|:--:|---|---|---|---|---|---|:--:|
| S00 | A | A · 06:00 · 71°/14° | KANEPE ÇIKAR | eşikte, işçilerin elinde · iki işçi · yoldaki düz araba | Kanepe ve kırık koltuk arabada · sarmaşıklı kemer, kırık pencereler, hasarlı çatı görünür | kuş banyosu 86 px · ufuk %50 | AÇILIŞ NESNESİ · 'from the first frame' · kuşkulu yük yok | ✅ |
| S01 | A | A · 06:10 · 73°/16° | SARMAŞIK GİDER | kemer ve pencere üstünde · iki işçi, merdiven · demetler arabaya | Kemer ve iki pencere açıklığı sarmaşıksız · taş hâlâ kirli gri · İLK BÜYÜK SONUÇ (0:16) | kuş banyosu 86 px · ufuk %50 | İLK BÜYÜK SONUÇ · açıklık sayısı sabit | ✅ |
| S02 | A | A · 06:20 · 74°/18° | CEPHE YIKANIR | arabadaki kovalar · iki işçi, fırça · cephe soldan sağa | Bütün cephe açık bej taş · geometri aynı | kuş banyosu 86 px · ufuk %50 | yalnız renk değişir | ✅ |
| S03 | A | A · 06:30 · 75°/20° | ÇATI SÖKÜLÜR | çatıda kiremit · kova, iskele kulesi · araba | Bütün çatı soyulmuş: gri altlık ve çıtalar aynı eğimde | kuş banyosu 86 px · ufuk %50 | çatı eğimi ve yüksekliği sabit | ✅ |
| S04 | A | A · 06:40 · 77°/22° | ÇATI KAPANIR | paletteki istif · iki işçi, iskele kulesi · çatı altlığı | Çatı yeni, koyu antrasit, aynı siluet çizgisi | kuş banyosu 86 px · ufuk %50 | çatı siluet çizgisi sabit | ✅ |
| S05 | A | A · 06:50 · 78°/24° | SOL PENCERE | araba üstünde cam ünite · iki işçi, sapan · sol açıklık | Sol pencere yeni, sağ eski | kuş banyosu 86 px · ufuk %50 | açıklık ölçüsü sabit | ✅ |
| S06 | A | A · 07:00 · 79°/26° | SAĞ PENCERE | araba üstünde ikinci ünite · iki işçi, sapan · sağ açıklık | İki pencere yeni ve eş | kuş banyosu 86 px · ufuk %50 | iki pencere aynı ölçü | ✅ |
| S07 | A | A · 07:10 · 81°/28° | CEVİZ KAPI | kemer yanındaki sehpa · iki işçi · kemer içi | Ceviz kapı yerinde, kanatlar kapalı · kemer korunur | kuş banyosu 86 px · ufuk %50 | kemer korunur | ✅ |
| S08 | A | A · 07:20 · 82°/29° | TAŞ YOL | paletteki taş istifi · iki işçi · eski yolun çizgisi | Taş yol tamam, aynı genişlik ve çizgi · kenarlarda sönük yol lambaları | kuş banyosu 86 px · ufuk %50 | yol başı, sonu, genişliği sabit | ✅ |
| S09 | A | A · 07:30 · 83°/31° | BAHÇE · ARABA ÇIKAR | çimdeki fide kasaları · iki işçi · iki yatak | Dış cephe ilk tamamlanmış hâlinde · içerisi henüz gösterilmedi | kuş banyosu 86 px · ufuk %50 | ön cephe bölümünün sonu | ✅ |
| S10 | H | A · 07:40 · 85°/33° | HOL BOŞALIR | zemindeki enkaz · iki işçi, el arabası · dışarıdaki araba | Hol boş · kemer, kapı, iki dar pencere sabit | taş kemer 584 px · ufuk %50 | kemer + ceviz kapı = A ile ortak çapa | ✅ |
| S11 | H | A · 07:50 · 86°/35° | DUVAR ONARILIR | arabadaki sıva kovası · iki işçi, mala · çatlak yüzeyler | Duvarlar düz, gri-beyaz, boyasız | taş kemer 584 px · ufuk %50 | — | ✅ |
| S12 | H | A · 08:00 · 88°/37° | TRAVERTEN | kapı içindeki palet · iki işçi · harç yatağı | Açık traverten zemin kesintisiz | taş kemer 584 px · ufuk %50 | — | ✅ |
| S13 | H | A · 08:10 · 89°/39° | BOYA | arabadaki boya · iki işçi, rulo · sıvalı duvarlar | Duvarlar sıcak kırık beyaz · hol aydınlık | taş kemer 584 px · ufuk %50 | — | ✅ |
| S14 | H | A · 08:20 · 91°/41° | AVİZE | arabadaki sandık · iki işçi, merdiven · tavandaki zincir | Avize asılı, sönük | taş kemer 584 px · ufuk %50 | avize kendi zincirinde · ek kaldırma düzeni yok | ✅ |
| S15 | H | A · 08:30 · 92°/43° | KONSOL | arabadaki tabla ve ayaklar · iki işçi · sol duvar | Tek konsol sol duvarda, üstünde tek vazo | taş kemer 584 px · ufuk %50 | tek konsol | ✅ |
| S16 | H | A · 08:40 · 94°/45° | BANK VE TABLO | arabadaki bank, kapı yanındaki tablo · iki işçi · sağ duvar, konsol üstü | Hol tamam: konsol, vazo, tablo, bank, avize | taş kemer 584 px · ufuk %50 | ayna yok — tablo (sahip kararı) | ✅ |
| S17 | L | A · 08:50 · 96°/47° | SALON BOŞALIR | zemindeki eski eşya · iki işçi, el arabası · holdeki araba | Salon boş · açıklıktan bitmiş hol görünür | hol açıklığı 542 px · ufuk %50 | açılış kanepesi geri dönmez · hol = ortak çapa | ✅ |
| S18 | L | A · 09:00 · 98°/49° | FİLDİŞİ | arabadaki boya · iki işçi, rulo · duvarlar | Duvarlar fildişi · pencere, tavan, duvar sınırları aynı | hol açıklığı 542 px · ufuk %50 | — | ✅ |
| S19 | L | A · 09:10 · 99°/51° | MEŞE PARKE | arabadaki tahta istifi · iki işçi, tezgâh · şap | Meşe zemin tek yönde | hol açıklığı 542 px · ufuk %50 | döşeme yönü sabit | ✅ |
| S20 | L | A · 09:20 · 101°/53° | CEVİZ PANEL | arabadaki panel istifi · iki işçi, matkap · uzak duvarın sol bölümü | Ceviz panel yalnız sol bölümde | hol açıklığı 542 px · ufuk %50 | açıklık ve duvarın kalanı değişmez | ✅ |
| S21 | L | A · 09:30 · 104°/55° | TAVAN IŞIĞI | arabadaki sandık · iki işçi, merdiven · tavan göbeği | Halka ışık asılı, sönük · yüksekliği sabit | hol açıklığı 542 px · ufuk %50 | — | ✅ |
| S22 | L | A · 09:40 · 106°/57° | HALI | arabadaki rulo · iki işçi · zeminin ortası | Halı ortada, köşeleri sabit | hol açıklığı 542 px · ufuk %50 | halı köşeleri kilit | ✅ |
| S23 | L | A · 09:50 · 108°/59° | ANA KANEPE | açıklıktaki araba · iki işçi · halının sol kenarı | Tek ana kanepe | hol açıklığı 542 px · ufuk %50 | tek kanepe | ✅ |
| S24 | L | A · 10:00 · 111°/61° | İKİNCİ KANEPE | açıklıktaki araba · iki işçi · halının sağ kenarı | İki kanepe, aralarında geniş geçiş | hol açıklığı 542 px · ufuk %50 | iki kanepe | ✅ |
| S25 | L | A · 10:10 · 114°/62° | BERJERLER | açıklıktaki araba · iki işçi · halının uzak köşeleri | İki berjer · taş sehpa arabada, açıklığın içinde | hol açıklığı 542 px · ufuk %50 | her yük tek berjer · geç teslimat | ✅ |
| S26 | L | G · 10:20 · 117°/64° | TAŞ SEHPA | açıklıktaki araba · dört işçi · halının ortası | Sehpa halının ortasında, ayakları halıya basar, kanepelere değmez | hol açıklığı 542 px · ufuk %50 | GERÇEK ZAMAN · ağırlık yavaş okunur | ✅ |
| S27 | L | A · 10:20 · 117°/64° | CEVİZ KONSOL | açıklıktaki araba · iki işçi · panelin önü | Konsolun ayak izi sabit | hol açıklığı 542 px · ufuk %50 | — | ✅ |
| S28 | L | A · 10:30 · 121°/66° | YAN SEHPALAR | açıklıktaki araba · iki işçi · kanepe uçları | Tam iki yan sehpa | hol açıklığı 542 px · ufuk %50 | sayı 2 | ✅ |
| S29 | L | A · 10:40 · 125°/68° | LAMBADER VE ZEYTİN | açıklıktaki iki araba · iki işçi · sağ kanepe yanı, cam kapılar | Salon tamam — ilk iç mekân zirvesi · BÖLÜM 1 sonu | hol açıklığı 542 px · ufuk %50 | BÖLÜM 1 sonu (240,0 sn) | ✅ |
| S30 | D | A · 10:50 · 129°/69° | YEMEK ODASI BOŞALIR | zemindeki eski eşya · iki işçi · verandadaki araba | Oda boş · mutfak kapısından harap mutfak, camlardan harap veranda | üç cam kapı 918 px · ufuk %50 | yük yolu = cam kapılar (veranda) | ✅ |
| S31 | D | A · 11:00 · 134°/71° | GREJ | arabadaki boya · iki işçi · duvarlar | Duvarlar grej | üç cam kapı 918 px · ufuk %50 | — | ✅ |
| S32 | D | A · 11:10 · 140°/72° | TAŞ ZEMİN | kapıdaki palet · iki işçi · harç yatağı | Taş zemin · desen bundan sonra aynı | üç cam kapı 918 px · ufuk %50 | zemin deseni kilit | ✅ |
| S33 | D | A · 11:20 · 147°/73° | AVİZE | arabadaki sandık · iki işçi, merdiven · tavan kancası | Avize merkez ekseninde · masa arabada, kapının içinde | üç cam kapı 918 px · ufuk %50 | geç teslimat | ✅ |
| S34 | D | G · 11:30 · 154°/74° | MASA | kapıdaki araba · dört işçi · avizenin altı | Tek masa, tek sabit konum | üç cam kapı 918 px · ufuk %50 | GERÇEK ZAMAN · ağırlık yavaş okunur | ✅ |
| S35 | D | A · 11:30 · 154°/74° | BAŞ SANDALYELERİ | kapıdaki araba · iki işçi · masanın iki ucu | Toplam iki sandalye | üç cam kapı 918 px · ufuk %50 | sayı 2 | ✅ |
| S36 | D | A · 11:40 · 162°/75° | BÜFE | kapıdaki araba · iki işçi · sağ duvar | Büfe sağ duvarda · iki sandalye aynı yerde | üç cam kapı 918 px · ufuk %50 | büfe geçişi kapatmaz | ✅ |
| S37 | D | A · 11:50 · 171°/75° | SERGİ DOLABI | kapıdaki araba · iki işçi · büfenin ötesi | Tek yeni dolap | üç cam kapı 918 px · ufuk %50 | tek dolap | ✅ |
| S38 | D | A · 12:00 · 180°/75° | DÖRT SANDALYE · SAYIM PİLOTU | arabadaki sandalye istifi · iki işçi · masanın sol yanı | Toplam altı sandalye: iki baş + solda dört | üç cam kapı 918 px · ufuk %50 | SAYIM PİLOTU · her yük tek sandalye (DERS 89) | ✅ |
| S39 | D | A · 12:10 · 189°/75° | PERDELER | arabadaki perde demeti · iki işçi, merdiven · iki pencere | Perdeler asılı · altı sandalye aynı | üç cam kapı 918 px · ufuk %50 | pencere konumu sabit | ✅ |
| S40 | D | A · 12:20 · 198°/75° | SON DÖRT SANDALYE | arabadaki istif · iki işçi · masanın sağ yanı | Toplam on sandalye: iki baş + iki yanda dörder | üç cam kapı 918 px · ufuk %50 | sayı 10 · her yük tek sandalye | ✅ |
| S41 | D | A · 12:30 · 206°/74° | TABLO VE ÇİÇEK | arabadaki tablo ve kutu · iki işçi · büfe üstü, masa ortası | Masa, on sandalye, büfe, dolap, perde, avize tamam | üç cam kapı 918 px · ufuk %50 | yemek odası sonu | ✅ |
| S42 | K | A · 12:40 · 213°/73° | SÖKÜM | sol duvardaki eski dolaplar · iki işçi · servis kapısındaki araba | Sol duvar çıplak · kapılar aynı | yemek odası kapısı 420 px · ufuk %50 | tesisat duvarı sabit | ✅ |
| S43 | K | A · 12:50 · 220°/72° | DUVAR VE BOYA | arabadaki kova · iki işçi · duvarlar | Duvarlar krem · sınırlar aynı | yemek odası kapısı 420 px · ufuk %50 | — | ✅ |
| S44 | K | A · 13:00 · 226°/71° | TAŞ ZEMİN | kapıdaki palet · iki işçi · harç yatağı | Taş zemin · ada yeri boş | yemek odası kapısı 420 px · ufuk %50 | — | ✅ |
| S45 | K | A · 13:10 · 231°/69° | KİLER DOLAPLARI | kapıdaki araba · iki işçi · uzak duvar | Yüksek dolaplar tek duvarda | yemek odası kapısı 420 px · ufuk %50 | tek duvar | ✅ |
| S46 | K | A · 13:20 · 235°/68° | ALT DOLAPLAR | kapıdaki araba · iki işçi · sol duvar | Alt dolaplar ve tezgâh sol duvarda | yemek odası kapısı 420 px · ufuk %50 | kapak bölümleri kilit | ✅ |
| S47 | K | A · 13:30 · 239°/66° | ADA GÖVDESİ | kapıdaki araba · iki işçi · zeminin ortası | Ada gövdesi ortada, üstü boş · taş tezgâh arabada yanında | yemek odası kapısı 420 px · ufuk %50 | geç teslimat | ✅ |
| S48 | K | G · 13:40 · 243°/64° | TAŞ TEZGÂH · PİLOT | arabadaki taş · dört işçi, sapan · ada gövdesi | Ada tek parça; tezgâh kenarı, kalınlığı, boyu sabit | yemek odası kapısı 420 px · ufuk %50 | GERÇEK ZAMAN · PİLOT | ✅ |
| S49 | K | A · 13:40 · 243°/64° | TAŞ PANELLER | arabadaki istif · iki işçi · tezgâh arası | Taş paneller yerinde | yemek odası kapısı 420 px · ufuk %50 | taş deseni sabit | ✅ |
| S50 | K | A · 13:50 · 246°/62° | BUZDOLABI | kapıdaki araba · iki işçi · sağ duvar nişi | Buzdolabı yerinde · ön yüzü dolap çizgisinde | yemek odası kapısı 420 px · ufuk %50 | dolap çizgisi | ✅ |
| S51 | K | A · 14:00 · 249°/61° | ÇİFT FIRIN | kapıdaki araba · iki işçi · dolap yuvası | Tek fırın ünitesi | yemek odası kapısı 420 px · ufuk %50 | yeni dolap yok | ✅ |
| S52 | K | A · 14:10 · 252°/59° | İKİ TABURE | kapıdaki araba · iki işçi · ada kenarı | Tam iki tabure | yemek odası kapısı 420 px · ufuk %50 | sayı 2 | ✅ |
| S53 | K | A · 14:20 · 254°/57° | DÖRT TABURE · KAHVE | kapıdaki araba · iki işçi · ada kenarı, tezgâh | Dört tabure · ada, kiler, cihazlar, tezgâh tamam | yemek odası kapısı 420 px · ufuk %50 | sayı 4 · mutfak sonu | ✅ |
| S54 | M | A · 14:30 · 256°/55° | ESKİ YATAK ÇIKAR | uzak duvardaki eski yatak · iki işçi · koridor kapısındaki araba | Oda boş · kapı, pencere, giyinme kapısı aynı | koridor kapısı 192 px · ufuk %50 | — | ✅ |
| S55 | M | A · 14:40 · 259°/53° | DUVAR VE GREJ | arabadaki kova · iki işçi · duvarlar | Duvar bitişi tamam | koridor kapısı 192 px · ufuk %50 | — | ✅ |
| S56 | M | A · 14:50 · 261°/51° | MEŞE PARKE | arabadaki istif · iki işçi, tezgâh · şap | Meşe zemin, bu kameraya göre sabit yön | koridor kapısı 192 px · ufuk %50 | döşeme yönü | ✅ |
| S57 | M | A · 15:00 · 262°/49° | BAŞLIK | arabadaki panel · iki işçi · uzak duvar ortası | Başlık duvarı ölçüsü değişmez | koridor kapısı 192 px · ufuk %50 | başlık ortalı | ✅ |
| S58 | M | A · 15:10 · 264°/47° | PERDELER | arabadaki demet · iki işçi, merdiven · pencere | Perdeler asılı | koridor kapısı 192 px · ufuk %50 | pencere ölçüsü sabit | ✅ |
| S59 | M | A · 15:20 · 266°/45° | HALI | arabadaki rulo · iki işçi · başlığın önü | Halı yerinde · yatak gövdesi arabada, kapının içinde · BÖLÜM 2 sonu (480,0 sn) | koridor kapısı 192 px · ufuk %50 | BÖLÜM SINIRI KARESİ G60 · geç teslimat | ✅ |
| S60 | M | G · 15:30 · 268°/43° | KING YATAK | kapıdaki araba · dört işçi · başlığın önü | Yatak gövdesi başlığa ortalı | koridor kapısı 192 px · ufuk %50 | GERÇEK ZAMAN · BÖLÜM 3 ilk sahnesi | ✅ |
| S61 | M | A · 15:30 · 268°/43° | ŞİLTE VE NEVRESİM | kapıdaki araba · iki işçi · yatak gövdesi | Tek yatak, sabit örtü düzeni | koridor kapısı 192 px · ufuk %50 | yatak ölçüsü sabit | ✅ |
| S62 | M | A · 15:40 · 269°/41° | KOMODİNLER | kapıdaki araba · iki işçi · yatak iki yanı | İki komodin, iki abajur | koridor kapısı 192 px · ufuk %50 | sayı 2 + 2 | ✅ |
| S63 | M | A · 15:50 · 271°/39° | YATAK UCU BANKI | kapıdaki araba · iki işçi · yatak ucu | Bank yatak ucunda, geçişler açık | koridor kapısı 192 px · ufuk %50 | — | ✅ |
| S64 | M | A · 16:00 · 272°/37° | ŞEZLONG | kapıdaki araba · iki işçi · pencere yanı | Dinlenme köşesi | koridor kapısı 192 px · ufuk %50 | — | ✅ |
| S65 | M | A · 16:10 · 274°/35° | MAKYAJ KONSOLU | kapıdaki araba · iki işçi · sol duvar | Yatak, komodinler, bank, şezlong, makyaj alanı tamam | koridor kapısı 192 px · ufuk %50 | ayna yok · oda sonu | ✅ |
| S66 | W | A · 16:20 · 275°/33° | RAFLAR SÖKÜLÜR | duvarlardaki raflar · iki işçi · kapıdaki araba | İki uzun duvar boş | yatak odası kapısı 250 px · ufuk %50 | — | ✅ |
| S67 | W | A · 16:30 · 277°/31° | BOYA | arabadaki boya · iki işçi · duvarlar | Duvarlar açık renk | yatak odası kapısı 250 px · ufuk %50 | — | ✅ |
| S68 | W | A · 16:40 · 278°/29° | MEŞE ZEMİN | arabadaki istif · iki işçi · şap | Meşe zemin · ada yeri boş | yatak odası kapısı 250 px · ufuk %50 | — | ✅ |
| S69 | W | A · 16:50 · 279°/28° | SOL GARDIROP | kapıdaki araba · iki işçi · sol duvar | Sol gardırop duvarı tam | yatak odası kapısı 250 px · ufuk %50 | modül sayısı kilit | ✅ |
| S70 | W | A · 17:00 · 281°/26° | SAĞ GARDIROP | kapıdaki araba · iki işçi · sağ duvar | İki gardırop duvarı eş · ayna yok | yatak odası kapısı 250 px · ufuk %50 | ayna yok (sahip kararı) | ✅ |
| S71 | W | A · 17:10 · 282°/24° | ORTA ADA | kapıdaki araba · iki işçi · zeminin ortası | Ada ortada, eşit geçişler | yatak odası kapısı 250 px · ufuk %50 | eşit geçiş | ✅ |
| S72 | W | A · 17:20 · 283°/22° | BANK VE KIYAFETLER | kapıdaki iki araba · iki işçi · ada ucu, açık raflar | Bank ve ada ayrı · raflarda sabit sayıda grup | yatak odası kapısı 250 px · ufuk %50 | raflar çoğalmaz · oda sonu | ✅ |
| S73 | B | A · 17:30 · 285°/20° | MOLOZ ÇIKAR | zemindeki moloz · iki işçi · kapıdaki araba | Zemin temiz · duş nişi yerinde | pencere 512 px · ufuk %50 | duş nişi sabit | ✅ |
| S74 | B | A · 17:40 · 286°/18° | TAŞ DUVARLAR | arabadaki istif · iki işçi · duvarlar | Duvarlar taş · damarlar sabit | pencere 512 px · ufuk %50 | duvar damarları kilit | ✅ |
| S75 | B | A · 17:50 · 287°/16° | TAŞ ZEMİN | arabadaki istif · iki işçi · harç yatağı | Zemin taş · derz yönü kilit | pencere 512 px · ufuk %50 | derz çizgileri | ✅ |
| S76 | B | A · 18:00 · 289°/14° | ÇİFT LAVABO | kapıdaki araba · iki işçi · sağ duvar | Tek dolap bankası, iki lavabo, iki aplik · küvet arabada kapının içinde | pencere 512 px · ufuk %50 | ayna yok — aplik (sahip kararı) · geç teslimat | ✅ |
| S77 | B | G · 18:10 · 290°/12° | KÜVET | kapıdaki araba · dört işçi · pencerenin önü | Tek küvet, sabit yer | pencere 512 px · ufuk %50 | GERÇEK ZAMAN | ✅ |
| S78 | B | A · 18:10 · 290°/12° | BATARYA | arabadaki kutu · iki işçi · zemin çıkışı | Batarya tek ve sabit | pencere 512 px · ufuk %50 | su akışı yok | ✅ |
| S79 | B | A · 18:20 · 292°/10° | BANK VE HAVLULAR | kapıdaki araba · iki işçi · sol duvar | Küvet, dolap, aplikler, bank, duş nişi tamam | pencere 512 px · ufuk %50 | banyo sonu | ✅ |
| S80 | T | A · 18:30 · 293°/9° | AHŞAP DÖŞEME | arabadaki tahta istifi · iki işçi · eski beton | Ahşap veranda · kolonlar ve tavan aynı | 2. kolon 64 px · ufuk %50 | kolon ve tavan sabit | ✅ |
| S81 | T | A · 18:40 · 294°/7° | DIŞ KANEPE | çimdeki araba · iki işçi · verandanın ortası | Tek oturma grubu | 2. kolon 64 px · ufuk %50 | tek grup | ✅ |
| S82 | T | A · 18:50 · 296°/5° | İKİ KOLTUK | çimdeki araba · iki işçi · kanepenin karşısı | Tam iki koltuk | 2. kolon 64 px · ufuk %50 | sayı 2 | ✅ |
| S83 | T | A · 19:00 · 297°/3° | DIŞ SEHPA | çimdeki araba · iki işçi · grubun ortası | Sehpa grubun merkezinde | 2. kolon 64 px · ufuk %50 | — | ✅ |
| S84 | T | A · 19:10 · 299°/2° | UZUN BANK | çimdeki araba · iki işçi · arka duvar | Bank arka duvarda · geçiş açık | 2. kolon 64 px · ufuk %50 | geçiş açık | ✅ |
| S85 | T | A · 19:20 · 300°/0° | SAKSILAR · IŞIKLAR | çimdeki araba · iki işçi · veranda köşeleri | Tamamlanmış veranda, sıcak ışık, bütün mobilya aynı karede | 2. kolon 64 px · ufuk %50 | ışık tek karede yanar (ISIK_FINALI) | ✅ |
| S86 | H | A · 19:30 · 302°/-2° | TESLİM · AVİZE YANAR | holdeki son aletler · iki işçi, iki kişi · dışarıdaki araba | Hol avizesi yanık · kapı kapalı | taş kemer 584 px · ufuk %50 | ışık tek karede yanar · sahip kararı: final ışıklar | ✅ |
| S87 | L | A · 19:40 · 304°/-3° | ÖRTÜLER KALKAR · LAMBALAR | mobilyadaki örtüler · iki işçi · açıklıktaki araba | Salon lambalı · örtü yok | hol açıklığı 542 px · ufuk %50 | ışık tek karede yanar | ✅ |
| S88 | A | A · 19:50 · 305°/-5° | DIŞ CEPHE · MAVİ SAAT | yoldaki merdiven · iki işçi · araba (kadraj dışı) | İki pencere yanık, yol ışıkları yanık · açılışla aynı kadraj, karşıt hâl | kuş banyosu 86 px · ufuk %50 | AÇILIŞ–FİNAL KAFİYESİ · ışık tek karede | ✅ |
| S89 | D | G · 20:00 · 307°/-7° | İLK AKŞAM YEMEĞİ | masa başında ayakta · iki kişi · sandalyeler | USTA KARE G90 — iki kişi sofrada, avize yanık, on sandalye, camların ardında yanık veranda | üç cam kapı 918 px · ufuk %50 | İŞLEV ANI · 4 + 4 · kapak kaynağı | ✅ |
| G90 | D | G · 20:00 · 307°/-7° | USTA KARE | — | USTA KARE G90 — iki kişi sofrada, avize yanık, on sandalye, camların ardında yanık veranda | üç cam kapı 918 px · ufuk %50 | kapak kaynağı | ✅ |
