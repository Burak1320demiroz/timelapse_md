# 🗂️ FİLM KLASÖRÜ ŞABLONU — yatay timelapse · kopyala, doldur

> **Kural metni burada DEĞİL.** Format kartı `KILAVUZ_REHBERI.md` **§2.8** (yatay merdiven),
> zincir §2.7, değişmezler §3, merdiven §4, konsept kapısı §6, negatif çekirdek §7, üretim
> akışı §8. Bu klasör o kuralların **kopyalanabilir hâlidir** — çelişkide kılavuz kazanır.
>
> İskelet kardeş depo `film_md`'nin `FILM_KLASOR_SABLONU/`'ndan devralındı (14.09.2026 · sahip
> kararı: "aynı film klasörü şablonu, bu deponun kılavuzları ve dersleri"). Oradaki tema / novum /
> kurulum yayı / karakter kapıları BURADA YOKTUR: timelapse'te kamera sabittir, kesme zaman
> sıçramasıdır, özne yapıdır (`KILAVUZ_REHBERI` §1.2). D-numaralı ders atfı geçmez; atıf
> `DERSLER.md`'nin DERS n'idir.

```bash
bash araclar/film_klasoru_ac.sh <FORMAT_KLASORU> <FILM_ADI> [SAHNE_SAYISI]
#   FORMAT_KLASORU ∈ yatay_2_dk_filmler (12) · yatay_4_dk_filmler (24) ·
#                    yatay_6_dk_filmler (36) · yatay_8_dk_filmler (48)
#   SAHNE_SAYISI formattan gelir; farklı verilirse bandın dışıdır (sahip izni + PLAN'a gerekçe)
```

⛔ **ELLE `cp -r` YAPILMAZ.** Betik dört işi birden yapar: şablonu kopyalar · dosyaları
`<FILM>_<ROL>.md` yapar · yer tutucuları doldurur (`<FILM_ADI>` · `<N>` · `<K>` · `<KESMELER>` …) ·
sahne satırlarını damgalar (`00_HIKAYE_ONAYI` · `03_SAHNE_SIRALAMASI` · `00_SAHNE_TABLOSU` ·
`BOLUM_1/2` sahne blokları · `URETIM_GUNLUGU` zincir ve I2V satırları) ve `00_OKUMA_CIZELGESI.md`'yi
dosya sisteminden üretir. Elle kopyada bu damgalar kaçar ve prompt kapısı ilk koşuda BLOCK verir.

---

## Neden şablon bir KLASÖR, tarif değil

`film_md` bu dersi iki kez ödedi ve bu depo da aynı kalıbı ölçtü: **DERS 28** — üretim
günlüğü "yazılır" diye AGENTS'ta duruyordu, dört filmde dört kez tutulmadı; şablon dosyası
`dikey_shorts/URETIM_GUNLUGU_SABLONU.md` olarak ayrılınca kapı (`qa_paket.sh`) ona bağlanabildi.
**DERS 12** — yazılı kural kapı değildir. Nesre yazılmış yapı uygulanmıyor, kopyalanabilir yapı
uygulanıyor.

---

## Dosyalar ve sahipleri

| Dosya | Ne zaman yazılır | Kaynak kılavuz |
|---|---|---|
| `00_ANALIZ/` | 🔬 yazımdan ÖNCE, sırayla — `00_HIKAYE_ONAYI` sahip onayı olmadan hiçbir dosya yazılmaz | kendi README'si |
| `<FILM>_PLAN.md` | kart A adım 1-7 · 9 (müzik/kapak taslağı) | `KILAVUZ_REHBERI` §3 · §4 · §5 · §6 · `YAPI_TIPI_KARTLARI` · `SAHA_VE_IKLIM_KARTLARI` · `KAMERA_ISTASYONU` §3 · `ZAMAN_VE_ISIK` |
| `<FILM>_BOLUM_1.md` | kart A adım 8 — S0…S<K−1> görsel + I2V | `PROMPT_SABLONU` §1-§2 · `INSAAT_YONTEMI` §5 · `SANTIYE_HAREKETI` §2 · `KILAVUZ_REHBERI` §7 |
| `<FILM>_BOLUM_2.md` | kart A adım 8 — S<K>…S<N−1> + ⭐ USTA KARE G<N> | aynı |
| `<FILM>_KAPAK.md` | adım 9 (usta kare promptu + başlık bandı satırı) | `MUZIK_VE_KAPAK` §2 |
| `<FILM>_MUZIK.md` | adım 9 | `MUZIK_VE_KAPAK` §1 |
| `<FILM>_YAYIN_PAKETI.md` | adım 10 · ⭐ İNGİLİZCE | `MUZIK_VE_KAPAK` §3 · `apexait/<platform>/PAKETLEME_SABLONU.md` · `apexait/CAPRAZ_YAYIN.md` |
| `<FILM>_QA_SPEC.md` | adım 11 — yazım paketinin SON parçası | `QA/00_README.md` mod sistemi · `KURGU_VE_TESLIM` §5-§6 |
| `<FILM>_URETIM_GUNLUGU.md` | ⛔ YAZIMDA DEĞİL — üretim sırasında (kart B); klip başına bir satır | `ARAC_KARTLARI` §4-§6 · `AGENTS` kart B · DERS 28 |

⛔ **Boş bırakılan dosya silinmez, `⬜ BEKLİYOR` satırıyla durur.** Var olan boş dosya görünür
borçtur; olmayan dosya borç değil, unutmadır.

---

## Şablonun kendisi denetime girmez

`araclar/prompt_kontrol.py` yolunda `SABLON` geçen dosyayı atlar (çıkış 0, "şablon — atlandı").
`araclar/sayac.sh` yalnız format klasörlerinin köklerini sayar; bu klasör `kilavuzlar/` altındadır
ve film sayılmaz. Kopyası (film klasörü) denetime girer.
