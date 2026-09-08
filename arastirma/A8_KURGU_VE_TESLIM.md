# ✂️ A8 — KURGU VE TESLİM

```
AMAÇ      Kliplerden mp4'e giden adımı yazılı hâle getirmek: kesme yeri,
          uç kırpması, dikiş eşleme, final tutuşu, loop, kapak türetme,
          dışa aktarım ve yayından ÖNCEKİ kontrol listesi.
KARŞILIĞI ⑥ GEÇİŞ  ⛔ METRONOM — DÖRDÜNCÜ kez; plan 6·4·6·4·6·6·8·4·6·10
                    yazdı, kurgu 10 × 6,0 DÜZ kesildi
          BEŞ MERCEK  "END CARD DIFFERENT" — kart filmden kopuk
          KAPAK   S9 karesinden türetilmedi (KAPAK.md tersini yazmıştı)
          SES     müziksiz pencere ve LUFS hiç doğrulanmadı
DÖNÜŞÜ    kilavuzlar/KURGU_VE_TESLIM_KILAVUZU.md (HENÜZ YOK) ·
          araclar/kesme_kontrol.sh eşik kalibrasyonu [DERS 31] ·
          MUZIK_VE_KAPAK · üretim günlüğü §4 · kart Y
KOŞU      ⛔ koşulmadı — 07.09.2026 yazıldı
```

⚠️ **A2'den farkı:** A2 "hangi ritim tutturur" diye sordu, yani NEDEN.
A8 "o ritim teslim dosyasına nasıl kesilir ve nasıl kanıtlanır" diye soruyor,
yani NASIL. Metronom dört kez A2'nin bilgi eksikliğinden değil, kurgu adımının
yazılı olmamasından geldi.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen dikey kısa filmlerin son işlem (post-production, finishing) ve teslim aşaması üzerine çalışan bir araştırmacısın; ürün 9:16 dikey, konuşmasız, yapay zekâ ile üretilmiş bir inşaat timelapse filmi: on ayrı klip, hepsi aynı sabit kameradan, kurguda arka arkaya sert kesilip tek bir dosya olarak yayımlanıyor.

Ölçülmüş arıza şu: plan klip sürelerini 6-4-6-4-6-6-8-4-6-10 saniye olarak yazdığı hâlde kurgu on klibi de 6,0 saniyede düz kesti ve bağımsız denetçi dördüncü kez "METRONOME" hükmü verdi, beş ayrı denetim son karttaki görüntünün filmden farklı olduğunu yazdı, kapak son karenin görüntüsünden türetilmedi, açılıştaki müziksiz pencere ve ses yüksekliği hiç ölçülmedi — ve bunların hiçbiri yakalanmadı çünkü teslim dosyasını planla karşılaştıran hiçbir adım yoktu.

Birinci görevin: profesyonel kurgunun bir timelapse dizisini gerçekte nasıl kestiğini yaz — kesme, çekim içindeki harekete göre nereye düşer (hareketin üstüne mi, duruşa mı), üretilen bir klibin başından ve sonundan kaç kare atılır ve neden, aynı sabit kameradan alınmış iki çekimin dikişi nasıl eşlenir (pozlama, parlaklık, renk, nesne konumu), titreme (flicker) nasıl ölçülür ve giderilir, ve editörler/renkçiler bunu hangi araç ve hangi ölçümle kontrol eder.

İkinci görevin: dikey kısa video platformlarında SON hakkında ölçülmüş ne var — son karenin ekranda kaç saniye tutulması, son kartın (end card) izlenme ve tekrar oynatma üzerindeki ölçülmüş etkisi, kusursuz döngü (seamless loop) noktasının nasıl kurulduğu, ve kapak/küçük resmin filmin ilk ve son karesiyle ilişkisi hakkında bağımsız veri.

Üçüncü görevin: teslim teknik şartlarını platform başına yaz — çözünürlük, kare hızı, kodek ve profil, bit oranı, renk uzayı ve aktarım fonksiyonu, ses için hedef LUFS ve tepe değeri, dosya boyutu tavanı — ve yayından önce koşulan profesyonel bir teslim kontrol listesi (QC checklist) çıkar: hangi madde, hangi sırayla, hangi araçla ölçülür ve kabul edilen tolerans nedir.

Rapor Türkçe olsun, araç ve parametre adları İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] bağımsız veri, platform dokümanı ya da ölçüm var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın) ve KAYNAK SINIFI (akademik · platform/araç dokümanı · bağımsız karşılaştırma · pazarlama blogu) yaz, çelişen iki kaynağı ikisi birden yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz; en sonda kontrol listesinin her maddesini ölçen, kopyalanıp çalıştırılabilir ffmpeg ve ffprobe komut satırlarını ver (kesme yerlerini bulan sahne algılama komutu, klip süresi, kare hızı, LUFS ölçümü, iki kare arası parlaklık farkı, son karenin dışa aktarımı) ve her komutun çıktısının nasıl okunacağını bir cümleyle açıkla.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A8_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         DERSLER.md · DEVRALINAN bölümüne  A8-a, A8-b…
3. KILAVUZ     kilavuzlar/KURGU_VE_TESLIM_KILAVUZU.md bu rapordan yazılır
4. KAPI        kesme_kontrol.sh eşiği bu raporla KALİBRE edilir (şu an 0.30,
               ölçülmedi) · dört kanıt satırı günlük §4'e yazılmadan kart Y açılmaz
```
