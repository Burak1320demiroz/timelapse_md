# 📐 A22 — RUBRİK TASARIMI VE PUAN BİRLEŞTİRME

```
AMAÇ      Rubriği ölçüm aracı olarak yeniden kurmak: kategori sayısı ve
          ağırlığı, puan çapaları, 10'un kanıtla kazanılması, koşullu
          kategori (müzik · kart · hız), öldürücü kategori ile ortalama
          ilişkisi, hüküm ↔ puan çelişkisi ve mercekler arası çift sayım.
KARŞILIĞI 06.10.2026 QA denetimi:
          · ⑨ ⑩ 4 kategori · ⑪ 6 · diğerleri 8 — ortalamaya eşit girer
          · ortalama formülü rubriklerde yok — 5 raporda yazılan ≠ hesaplanan
          · son 15 filmin 177 mercek raporunun 55'i (%31) tam 10,0, çoğu kanıtsız
          · rapor hükmü "ENDS", aynı raporun final vuruşu 3/10
          · bir boşta ekskavatör ⑦ ⑧ ⑨ ⑩'da dört kez puan kırdırıyor
          · rubrikler hâlâ müzik (BPM, ölçü), son kart ve "six shots" varsayıyor
DÖNÜŞÜ    kilavuzlar/RUBRIK_YAZIM_KILAVUZU.md (✅ 06.10.2026 yazıldı) · QA/1…12 rubrikleri ·
          QA/00_README §4-§5 · T tabloları
          ⚠️ Sınır: A23 = değerlendiricinin GÜVENİLİRLİĞİ · burası = ÖLÇEĞİN kendisi
KOŞU      ✅ 06.10.2026 yazıldı ve koşuldu · SONUCLAR/A22_GEMINI_HAM.md · denetim A20-A24_DENETIM.md
```

⛔ **README §5 kuralı yeni şablona da uyar:** rubrik içi salt İngilizce,
tarihsiz, film adsız. Raporun önereceği şablon buna göre istenmiştir.

⚠️ Bu dosyanın uzun sürümü YOKTUR.

---

## ⛔ BURADAN AŞAĞISI YAPIŞTIRILIR — kesmeden, altı cümle

Sen ölçme ve değerlendirme (psikometri), puanlama rubriği tasarımı ve büyük dil modelinin hakem olarak kullanıldığı değerlendirmeler (LLM-as-a-judge) üzerine çalışan bir araştırmacısın; benim ürünüm konuşmasız, yapay zekâ ile üretilmiş inşaat timelapse filmleri — dikey (9:16) filmler 7 klip × 8,0 sn olarak üretilip 2 kat hızda yayımlanıyor, yatay (16:9) filmler 12–18 klip olarak normal hızda; bazı filmlerde müzik ya da son kart var, çoğunda yok — ve her film bir çok kipli model (Gemini) tarafından 12 ayrı İngilizce rubrikle puanlanıyor: her rubrik tek bir soruya bakıyor (kamera sabit mi, aynı yapı mı, zaman geçiyor mu, vaat teslim edildi mi, dünya sürekli mi, kesmeler, şantiye çalışıyor mu, her parça görünerek mi yapıldı, faaliyet, sebep, envanter, katılık), 4 ile 8 arası kategoriyi 0–10 puanlıyor, bazı kategoriler koşullu ("NOT TRIGGERED" olabilir), her rubrik ayrıca kategorilerden bağımsız tek satırlık bir hüküm (VERDICT) veriyor ve kuralımız "hüküm ile kategoriler çelişirse hüküm kazanır"; film başına 12 rubriğin ortalaması karşılaştırma için kullanılıyor.

Ölçülmüş arıza şu: rubriklerden ikisi 4, biri 6, dokuzu 8 kategori taşıyor ve hepsi film ortalamasına eşit ağırlıkla giriyor, ortalamanın formülü (koşullu kategoriler dâhil mi) rubriklerde tanımlı olmadığı için beş raporda yazılan ortalama hesapla tutmuyor, son 15 filmin 177 rubrik raporunun 55'i (%31) tam 10,0 ve bunların çoğu "kusur tespit edilmedi" dışında kanıt göstermiyor, bir raporun hükmü "film bitiyor" derken aynı raporun final kategorisi 3/10, aynı tek kusur (büyüyen bir yapının yanında boşta duran bir ekskavatör) dört farklı rubrikte ayrı ayrı puan kırdırıyor ve filmin ortalaması dört kez düşüyor, ve rubrikler format değiştiği hâlde eski varsayımları taşıyor (müzik temposu ve ölçü uzunluğu soruyor, "dosya statik bir son kartla biter" diyor, "altı ayrı çekim" diyor) — yani ölçek, ölçtüğü şeyden bağımsız olarak puan üretiyor.

Birinci görevin: rubrik ve puan ölçeği tasarımı üzerine ölçülmüş bilgiyi yaz — analitik ve bütüncül rubrik, davranışsal çapalı derecelendirme ölçekleri (BARS), 0–10 ile 1–5 ile geçti/kaldı kontrol listesi arasındaki güvenilirlik farkı, özellikle LLM hakemlerde ölçek inceliğinin ve çapa metninin etkisi (G-Eval, Prometheus, CheckEval, TICK, FLASK, "rubric-based" ve "checklist-based" değerlendirme çalışmaları), tavan etkisi ve puan şişmesinin (leniency) nasıl ölçüldüğü ve önlendiği — örneğin yüksek puanı zaman damgalı kanıt şartına bağlamak ("kanıt yoksa en fazla 7") — ve hangi yaklaşımın insan yargısıyla uyumu ne kadar artırdığını sayıyla tablo hâlinde ver.

İkinci görevin: puan BİRLEŞTİRME üzerine yaz — kategori ağırlıklandırma, telafi edici (ortalama) ile telafi etmeyen (öldürücü kategori, eşik, kapı) puanlamanın farkı ve ne zaman hangisi, koşullu/ tetiklenmeyen kategorilerin ortalamaya nasıl girdiği, hüküm ile kategori puanı çeliştiğinde profesyonel sistemlerin ne yaptığı, farklı sayıda kategori taşıyan alt ölçeklerin bir toplamda nasıl dengelendiği, ve birbirine yakın kavramları ölçen birden çok alt ölçekte aynı kusurun ÇİFT SAYILMASININ (construct overlap, multitrait-multimethod matrisi, ayırt edici geçerlilik) nasıl tespit edilip önlendiği — yayın teknik QC'si, oyun sertifikasyonu (TRC/lotcheck), festival jürisi ve hakemli spor puanlaması (en yüksek/en düşük atma, öldürücü hata kesintisi) gibi gerçek sistemlerden belgelenmiş örneklerle karşılaştır.

Üçüncü görevin: formata göre koşullanan rubriği tasarla — oynatma hızı, klip sayısı, müzik var/yok, kart var/yok gibi beyan edilen parametrelerin rubriğin başında değişken bloğu olarak verilip kategorilerin bunlara göre "NOT TRIGGERED" olmasının mı, ayrı rubrik sürümleri yazmanın mı daha güvenilir olduğunu ölçülmüş verilerle yaz; LLM hakemde yapılandırılmış çıktının (JSON şeması, kategori başına zorunlu alan) eksik kategori ve aritmetik hatasını ne kadar azalttığını, ortalamanın modelde değil kodda hesaplanmasının etkisini ve kanıt alanını zorunlu kılmanın puan şişmesine etkisini belgelenmiş örneklerle ver.

Rapor Türkçe olsun, psikometri ve değerlendirme terimleri İngilizce kalsın, tablo ağırlıklı yaz; her bulgunun yanına ETİKET ([ÖLÇÜLDÜ] sayı ya da deney var · [İDDİA] kaynak söylüyor kanıt yok · [VARSAYIM] senin çıkarımın), KAYNAK SINIFI (akademik · araç dokümanı · bağımsız karşılaştırma · pazarlama blogu) ve ÇÖZÜMLENEBİLİR KAYNAK (URL, DOI, arXiv numarası ya da belge adı + bölüm; kaynağı gösterilemeyen sayı ÖLÇÜLDÜ etiketi alamaz) yaz, iki kaynak çelişiyorsa ikisini de yaz ve ORTALAMA ALMA, bilmediğine "BİLİNMİYOR" yaz, raporun sonuna "BENİM VARSAYIMLARIMLA ÇELİŞENLER" başlığı aç (özellikle "hüküm kategorileri yener" ve "12 rubriğin eşit ortalaması" kurallarımı değerlendir); en sonda (a) Türkçe not, tarih ve proje adı içermeyen, doğrudan yapıştırılacak İngilizce bir RUBRİK İSKELETİ (format değişkenleri bloğu · çapaları 0/3/5/7/10 olarak yazılmış ve 10 için zaman damgalı kanıt şartı taşıyan tek bir örnek kategori · NOT TRIGGERED kuralı · öldürücü kategori satırı · VERDICT satırı · JSON çıktı şeması) ve (b) kategori → rubrik → film puanı birleştirme formülünü ağırlıklarıyla ve çift sayımı önleyen "bu kusuru hangi rubrik sahiplenir" kuralıyla bir tablo olarak ver.

---

## 📥 SONUÇ GELDİĞİNDE

```
1. HAM KAYIT   arastirma/SONUCLAR/A22_<BOT>_HAM.md — dokunulmadan [kart S]
2. KOD         VARSAYIMLAR.md · kuşak bölümüne (+ DİZİN satırı)  A22-a, A22-b…
3. KILAVUZ     kilavuzlar/RUBRIK_YAZIM_KILAVUZU.md bu rapordan yazılır
4. KAPI        12 rubrik iskelete göre yeniden yazılır (README §5 korunur) ·
               ortalama KODDA hesaplanır · "kusur sahipliği" tablosu README §1'e
```
