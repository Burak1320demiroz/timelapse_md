# 📁 HAM — modelin ham çıktısı, DOKUNULMAZ

```
YOL     QA/HAM/<FILM>/<FILM>_Q<n>_<AD>_HAM.md
        <n>  1–5 · <AD>  GORUNTU · ZAMAN_KESME · SANTIYE · INSA · TESLIM
        ikinci koşu (test-tekrar · yeniden koşu)  …_HAM_K2.md · _K3
        yarım master bölümü (yatay)                <FILM>_B<b>_Q<n>_<AD>_HAM.md
ÖRNEK   QA/HAM/THE_BLUE_SILO/THE_BLUE_SILO_Q3_SANTIYE_HAM.md
```

```
⛔ Model çıktısı DÜZENLENMEZ, KISALTILMAZ, ÖZETLENMEZ. Ajanın ne anladığı FILMLER/ altındadır.
⭐ KÜNYE — dosyanın en üstünde, `---` çitleri arasında; kaydeden yazar, model çıktısı altına
   olduğu gibi gelir. Paket dosyası taslağı basar (qa_paket.sh); "model" satırını koşuyu
   yapan doldurur. Alanlar ve anlamları: kilavuzlar/QA_KAYIT_KILAVUZU.md §2.1 ·
   QA_KOSU_KILAVUZU.md §5.

---
film:        <FILM>
mercek:      Q<n>_<AD>
dosya:       <ad> · sha256 <ilk 12> · <süre> sn · <G×Y> · <hız>x
belgeler:    <dosya ("ilk satır")> | YOK (kör mercek)
rubrik:      QA/Q<n>_<AD>.md @ <git kısa hash>
model:       Gemini <sürüm> · sohbet | API · proje DIŞI · geçici sohbet ✓
tarih:       gg.aa.yyyy
geri_okuma:  dosya adı ✓/✗ · belge başlığı ✓/✗ · görülen klip <n>
durum:       TAM | EKSİK | YANLIŞ GİRDİ | SIZINTI | TUTARSIZ | BAĞLAYICI DEĞİL
---
<model çıktısı>

⚠️ "durum" künyede ilk kayıtta yazılır. Sonradan değişirse (ör. YERİNE GEÇTİ) ham dosyaya
   DOKUNULMAZ; değişiklik QA/FILMLER/<FILM>.md'nin mercek tablosuna ve TABLO.md'ye yazılır.
```

Eski 12 mercekli ham raporlar: `QA/ARSIV_12_MERCEK/HAM_RAPORLAR/` (393 dosya · durumları
`ARSIV_12_MERCEK/00_ESLEME.tsv`).
