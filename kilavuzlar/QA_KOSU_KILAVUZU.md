# 🧪 QA KOŞU KILAVUZU — değerlendiriciye NE gittiği kanıtlı olur

> `QA/00_README §2` merceklerin **sırasını** söyler. Bu kılavuz bir koşunun **nasıl
> yalıtıldığını ve kaydedildiğini** söyler: kör merceğin oturumu, belge isteyen merceğin
> belgesi, ön uçuş geri okuması, son uçuş sızıntı taraması, bozuk koşuda tek eylem.
>
> Kaynak: A20 · 06.10.2026 (`arastirma/SONUCLAR/A20_GEMINI_HAM.md`) · denetim
> `A20-A24_DENETIM.md` · tetikleyen: 06.10.2026 QA denetimi.
> ⭐ Rapordan inen: Gem/proje bilgi dosyalarının o Gem'in BÜTÜN sohbetlerine girmesi
> (Google yardım sayfası, çekildi ✅) · geçici sohbetin kişiselleştirmeyi kapatması ✅ ·
> sızıntı kelimesi ve kanarya terimi · fail-closed eylem tablosu · koşu manifestosu.
> ⛔ İnmeyen: "temperature 0 deterministik" (Google: "çoğunlukla") · "kule" için
> "önceki videonun tensörleri kaldı" teşhisi (kanıtsız) · süre geri okumasını kapı
> yapmak (model süre ölçemiyor — QA_OLCUM_ZEMINI §1) · James/Bang körlük endeksi
> (kör merceğe "plan gördün mü" sorulmaz; sızıntı METİNDEN ölçülür).

---

# 0. 🚪 KURAL

```
Koşu, değerlendiricinin ne gördüğü KANITLANABİLİYORSA koşudur.
  · kör mercek (❶ ❷ ❸) belge görebilecek bir oturumda koşmaz
  · belge isteyen mercek (❹ ❺) belgesiz koşmaz — koşarsa puanı yoktur
  · her ham rapor künyesiyle kaydedilir: dosya · belge · rubrik · oturum [QA_KAYIT §2.1]
Kanıtlanamayan koşunun BULGUSU okunur, PUANI hiçbir tabloya girmez.
```

Ölçülmüş bedeli (06.10.2026 denetimi · 393 ham · 37 film · 12 mercekli arşiv):

| arıza | ne oldu |
|---|---|
| kör mercek plan biliyor | 6 filmde ① ③ ⑤ ⑦ plandan alıntı: "şartnamedeki akifer su aynası" · "G7" · "56,0 sn hedefi" · "KAPAK KARTI YOK" |
| belge isteyen mercek belgesiz | en az 11 koşu; LAST LIFT ④ plansız + kapaksız final vuruşuna 10/10 → "REKOR 9,83" |
| başka filmin belgesi | STAR DOCK ⑧ ← DEEP STEP SPEC · DEEP STEP ⑧ ← STONE TOWER SPEC (iki puan da ortalamada) |
| muhtemelen başka video | POLAR HABITAT: sekiz mercek 1…21 klip saydı, ② ⑧ filmde olmayan bir "kule" anlattı |
| eksik koşu puanlandı | RUN INCOMPLETE ile başlayan raporlar tabloya puanla girdi |
| girdi kaydı yok | ham raporların çoğunda hangi video, belge, rubrik sürümü yazmıyor; QA/KOSU/ hiç oluşmadı |

---

# 1. 🔒 YALITIM — kör mercek nerede koşar

Gemini sohbet arayüzünde (06.10.2026'da çekilen yardım sayfaları ve Google duyuruları):

| özellik | ne yapar | kör merceğe etkisi |
|---|---|---|
| **Gem bilgi dosyaları** | Gem'e eklenen dosya o Gem'le açılan **her sohbete** girer ✅ | Gem'de SPEC/plan varsa o Gem'deki her kör koşu **belgelidir** |
| **proje / not defteri** dosyaları | projeye eklenen dosyalar projedeki sohbetlerde paylaşılır ✅ | aynı — proje içindeki kör koşu belgeli |
| **kişisel bağlam** (geçmiş sohbet belleği) · **kayıtlı bilgi** | önceki sohbetlerden bilgi taşır; kişisel hesapta varsayılan AÇIK ✅ | önceki filmin planı/rubriği yeni sohbete sızabilir |
| **geçici sohbet** | kişiselleştirmeyi ve geçmişi kapatır ✅ | kör koşunun tek güvenli yeri (sohbet arayüzünde) |

```
⇒ Bugünkü düzen "Gemini (sohbet arayüzü) · proje" — kör sızıntının EN OLASI sebebi
   budur: plan ve SPEC aynı projeye/Gem'e yüklüyse kör mercek onları görür.
   (Kanıtlanmadı: projenin içeriğini sahip bilir. ⚠️ İlk iş: projede hangi dosyalar var?)

KURAL   KÖR MERCEK  → proje/Gem DIŞINDA, GEÇİCİ SOHBETTE, yalnız video + kareler.
        BELGELİ MERCEK → yine geçici sohbette; belge o sohbete ELLE eklenir —
                         projenin bilgi tabanından değil (yanlış film belgesi
                         riskini de kaldırır: ne eklendiyse künyededir).
        Her mercek AYRI sohbet. İki filmi aynı sohbette koşma.
⚠️ Gem'ler kişisel hesaplarda Kasım 2026'dan itibaren "skill"e dönüşüyor (yardım
   sayfası) — davranış değişirse bu tablo yeniden çekilir.
```

---

# 2. 🛫 ÖN UÇUŞ — koşudan önce

## 2.1 Paket kontrolü (ajan · makine)

```
□ video dosyasının sha256'sı alındı (künyeye ilk 12 hane)   shasum -a 256 f.mp4
□ ÖLÇÜLMÜŞ OLGULAR bloğu dolduruldu ve rubriğin İÇİNDE [QA_OLCUM_ZEMINI §2]
□ belge isteyen mercekte belgenin İLK SATIRI film adını taşıyor (ör. "# 🔒 THE BLUE SILO — QA SPEC")
□ kör mercek paketinde belge YOK
□ rubrik dosyasının git kısa hash'i künyede
```

## 2.2 Geri okuma — rubriğin ilk talimatı (İngilizce · README §5'e uyar)

```
BEFORE YOU SCORE — write these three lines first, then stop and wait if any is wrong:
FILE NAME AS SHOWN:     <the name of the video file you were given>
DOCUMENTS ATTACHED:     <first line of each attached document, or NONE>
CLIPS YOU CAN SEE:      <your count — this is a check, the measured count is above>
```

| geri okuma | beklenen | tutmazsa |
|---|---|---|
| dosya adı | künyedeki ad | KOŞMA — yanlış video (POLAR HABITAT) |
| belgeler (kör mercek) | NONE | KOŞMA — oturum sızdırıyor (§1) |
| belgeler (belgeli mercek) | doğru filmin başlığı | KOŞMA — yanlış belge (DEEP STEP ⑧) |
| klip sayısı | ÖLÇÜLMÜŞ CLIP COUNT | koşu SÜRER; sayı modelin zayıflığıdır, kapı değildir · künyeye yazılır |

```
⛔ Süre geri okuması KAPI DEĞİLDİR: model süreyi ölçmüyor (2x kopyaya "32 sn" dedi).
   Kapı yalnız OKUNABİLEN şeydir: dosya adı ve belgenin ilk satırı.
```

---

# 3. 🛬 SON UÇUŞ — rapor geldikten sonra

## 3.1 Sızıntı taraması — kör mercekler

```
SIZINTI LİSTESİ (film başına, plan + SPEC'ten):
   · genel: "spec" · "specification" · "şartname" · "plan" · "G0"…"G7" · "S0"…"S6" ·
     "keyframe" · "prompt" · "MOTION FOCUS" · "regime" · "rejim"
   · filme özel: plandaki sayılar (56,0 · 61,0 · −21,60 m) ve yalnız planda geçen adlar
     (ör. "akifer su aynası")
   ⚠️ "spec not supplied / no document" cümlesi SIZINTI DEĞİLDİR — kör merceğin
      doğru tepkisidir; sızıntı, belgenin İÇERİĞİNİN raporda görünmesidir.
KANARYA (öneri · kapı adımı): her QA_SPEC'in künyesine bir uydurma terim
   ("KANARYA: <tek kelime>"). Üretim promptlarına GİRMEZ (prompt_kontrol denetler).
   Kör raporda geçerse sızıntı %100 kanıtlıdır.
```

## 3.2 Diğerleri

```
□ ilk satır RUN INCOMPLETE mı → durum EKSİK
□ VERDICT ve her kategori satırı var mı → yoksa EKSİK
□ D1–D5 [QA_OLCUM_ZEMINI §5] — dosya dışı damga · klip sayısı · süre itirazı · kesme · kart
□ hüküm ↔ sahip kategori çelişkisi [RUBRIK_YAZIM §4.3] → TUTARSIZ
```

---

# 4. 🛑 TEK EYLEM — fail closed

| durum | eylem | puan |
|---|---|---|
| sha/ad tutmuyor · yanlış belge · kör merceğe belge gitmiş | **KOŞMA** (başladıysa iptal) | yok |
| sızıntı listesi ya da kanarya kör raporda | **YENİDEN KOŞ** — geçici sohbette, proje dışında | SIZINTI · bulgular okunur |
| RUN INCOMPLETE · eksik kategori · hüküm yok | **YENİDEN KOŞ** — eksik girdi tamamlanarak | EKSİK |
| D1 dosya dışı damga · iki ya da daha çok D-kaldısı | **YENİDEN KOŞ** | bağlayıcı değil |
| hüküm iyi, sahip kategori ≤ 3 | **YENİDEN KOŞ** | TUTARSIZ |
| deneme · stres testi · serbest denetim | **BAĞLAYICI SAYMA** | yok — `QA_KAYIT` BAĞLAYICI DEĞİL |

```
⛔ Eksik koşunun puanı 0 ile de, 10 ile de DOLDURULMAZ; o mercek film puanının
   paydasından çıkar ve film puanı "N=…" taşır [RUBRIK_YAZIM §4.2].
⭐ Yeniden koşu eskisini silmez: yeni dosya _K2 ekiyle kaydedilir, eskisi
   YERİNE GEÇTİ olur [QA_KAYIT §3].
```

---

# 5. 🧾 KOŞU MANİFESTOSU = HAM RAPOR KÜNYESİ

Biçim `QA_KAYIT_KILAVUZU §2.1`'dedir; alanların kaynağı:

| alan | kim doldurur | nereden |
|---|---|---|
| film · mercek | ajan | paket |
| dosya (ad · sha256 · süre · çözünürlük · hız) | ajan | ffprobe · shasum · plan |
| belgeler (ad + ilk satır) | ajan | pakete konan dosya |
| rubrik @ git hash | ajan | `git log -1 --format=%h -- QA/<rubrik>` |
| model · arayüz · proje dışı · geçici sohbet | **sahip** | koşuyu yapan bilir |
| geri okuma | ajan | raporun ilk üç satırı (§2.2) |

```
⭐ Paket dosyası (QA/KOSU/<FILM>/Q<n>_<AD>_paket.md) künye taslağını en üste basar;
   sahip "model · arayüz" satırını doldurup raporla birlikte geri verir.
⛔ QA/KOSU/ bugüne dek hiç oluşmadı — paket hep elle kuruldu. Paket kullanılmadan
   koşulan raporun künyesini ajan sonradan YAZMAZ; "künye yok" yazılır.
```

---

# 6. 🔀 SOHBET Mİ API Mİ — sahip kararı

| | sohbet arayüzü (bugün) | Gemini API (betik) |
|---|---|---|
| yalıtım | geçici sohbet + proje dışı ile **elle** | her çağrı durumsuz — **yapı gereği** |
| girdi kaydı | künye elle | betik dosya özetini, model sürümünü, ayarları yazar |
| video örnekleme | belgelenmemiş | 1 fps varsayılan · fps ayarlanabilir (2x kopyada 2 fps → klip başına 8 kare) |
| çıktı biçimi | serbest metin; SCORES satırları elle okunur | yapılandırılmış çıktı (şema) — ajan doğrudan okur |
| sıcaklık | ayarlanamaz | ayarlanır — ama determinizm yine ÖLÇÜLÜR [QA_KALIBRASYON §1] |
| maliyet | abonelik | token başına (kare başına ~70 token; 28 sn'lik dosya küçük) · API anahtarı |
| kurulum | yok | bir Python betiği + anahtar |

```
ÖNERİ: kısa vadede sohbet + §1 kuralları (bugün uygulanabilir, bedava).
       Orta vadede API betiği — test-tekrar (QA_KALIBRASYON §1) 36 koşu ister ve elle
       36 geçici sohbet hem yorucu hem kayıt açığıdır.
⚠️ Karar sahibindir: API anahtarı, maliyet ve "QA'yı kim koşar" sorusu.
```
