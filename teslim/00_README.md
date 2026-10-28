# 📦 TESLİM — yayın dosyalarının yeri (git dışı)

> Ajan ölçümünün (kart R 2b) ve araçların okuyacağı yer. Bu klasörde **yalnız bu README**
> izlenir; içine konan her şey `.gitignore` ile depo dışında kalır.
>
> NEDEN (28.10.2026): dosyalar `~/Downloads`'ta duruyordu. Üç film kaydında "AJAN OKUYAMADI"
> yazdı, oysa dosyalar yereldeydi. SKY VAULT'ta dosya izin yüzünden okunamadı (DERS 106 ①).
> Aynı klasördeki beş dosyanın ihraç kareleri de birbirinin üstüne yazıldı
> [QA/DENETIM_2026-10-28.md · K4 · A4].

## Adlandırma

```
teslim/<FILM>.mp4          paylaşılacak dosya (dikey: 2x · 1080×1920)
teslim/<FILM>_1x.mp4       1x master (varsa — ❸ ❹ onunla koşar)
teslim/<FILM>_kapak.png    kapak (❺ ve kapak provası)
```

`<FILM>` film klasörünün adıdır (`dikey_shorts/<FILM>/`). Yeniden kesilen dosya **aynı adla**
konur. `kare_al.sh` sha256'yı `QA_KARELER/<FILM>/KAYNAK.txt`'ye yazar; `qa_paket.sh` eski kesimin
karelerini bu yüzden kullanmaz.

## Sıra

```
1. bash araclar/ihrac_kontrol.sh dikey_shorts/<FILM> teslim/<FILM>.mp4 --hiz 2
      ⛔ çıkış 2 → kurgu düzeltilir, bu adım tekrarlanır (çıkış üretim günlüğü §4'e)
2. bash araclar/qa_paket.sh --hiz 2 [--master teslim/<FILM>_1x.mp4] \
        dikey_shorts/<FILM> teslim/<FILM>.mp4 teslim/<FILM>_kapak.png
      → QA/KOSU/<FILM>/ · ihraç kapısını kendisi de koşar
3. beş mercek paketle koşulur → HAM → python3 araclar/kayit_kontrol.py <FILM> → kayıt
```

Kareler `teslim/IHRAC_KARELER/<FILM>/` ve `teslim/QA_KARELER/<FILM>/` altına düşer (git dışı).
