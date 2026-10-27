# 🧪 A43 — DİKEY KAPAK STİLİ: GÜVENLİ ALAN · BAŞLIK TİPOGRAFİSİ · IŞIK · YENİDEN IŞIKLANDIRMA

```
AMAÇ      Dikey (9:16 · 1080×1920) kapakta başlığın ORTA bantlarda nereye oturacağını, hangi yazı stiliyle
          küçük önizlemede okunacağını, hangi ışığın küçükte okunduğunu ve son kareyi (GN) geometrisi kilitli
          biçimde yeniden ışıklandırmanın yolunu bulmak.
KARŞILIĞI Sahip isteği 25.10.2026: "her film için viral kapak kılavuzu · safe area · Insta + YouTube · film adı
          ortada · viral ışık ve başlık stilleri" + sahip kararları: başlık en üstte/en altta OLMAZ · kapak = son
          kare sabit · farklı ışık serbest · yatay kapak KAPSAM DIŞI.
          Ölçülmüş zemin: DERS 94 (üst bantta başlık kırpıldı) · DERS 99 (usta kare başlık kutusunu yuttu) ·
          DERS 30 · 85 (ayrı üretilen kapak başka dünya oldu).
DÖNÜŞÜ    kilavuzlar/KAPAK_STIL_KILAVUZU.md
KOŞU      ✅ 25.10.2026 · Claude Sonnet 5.5 alt ajan (effort medium) · ham: SONUCLAR/A43_SONNET_HAM.md
```

---

## ⛔ BURADAN AŞAĞISI — ajana verilen prompt, birebir

You are doing web research for a vertical-video (9:16, 1080×1920) cover/thumbnail style guide for an AI-generated construction/transformation TIMELAPSE channel that posts to Instagram Reels and YouTube Shorts (TikTok secondary). The cover is ALWAYS the film's final frame (same camera, same composition) with an English film title (1–3 words) overlaid in post. We do NOT need horizontal 16:9 YouTube thumbnails — skip them entirely.

Context already settled (do not re-research): centered crop math (4:5 grid shows y 285–1635, 1:1 shows y 420–1500); our "content core" is x 150–930, y 540–1380; title will be horizontally centered and placed in one of three bands inside the core (upper-mid ~y 560–770, mid ~y 860–1060, lower-mid ~y 1170–1380), never at the very top or bottom. Palette is fixed: #101315, #E8E4DC, #2B3136, single accent amber #F2A03D.

Research these questions. For each claim, give the source URL and tag it: [PRIMARY] (official platform help/docs/creator blog, or a named study with method), [SECONDARY] (reputable design/marketing article), [UNVERIFIED] (blog listicle, no method). Say plainly when you could not find something; do not fill gaps with guesses.

1. UI overlay safe zones on 1080×1920 for Reels and Shorts (organic, not ads if possible): where the right-side action rail (like/comment/share) sits in px (x range, y range), bottom caption/channel area height, top bar height. Especially: does the right rail intrude into y ≈ 860–1380 at x > ~840? Official numbers if any exist (Meta, YouTube); otherwise the most-cited templates, noting they are third-party.
2. Title typography that stays legible at 120–160 px wide thumbnails: font families commonly used for viral Shorts/Reels covers (prefer free/open licenses — Google Fonts: e.g. Anton, Bebas Neue, Archivo Black, Montserrat, Oswald, Inter — confirm licenses), weight, condensed vs wide, letter-spacing, line count, cap-height as % of frame height. Any evidence on text shadow / outline / stroke / glow helping or hurting legibility and perceived quality (clickbait perception)? Any evidence about two-color titles (one accent word)?
3. Lighting in thumbnails/covers: evidence or strong practitioner consensus on what lighting reads well small — blue hour with warm windows (complementary contrast), golden-hour rim light, single brightest focal point, luminance contrast between subject and background, saturation levels. Anything specific to architecture/construction/transformation/timelapse content.
4. AI relighting while preserving geometry: current (2025–2026) methods to relight an existing image without changing composition/objects — e.g., Google Gemini image editing ("Nano Banana"), IC-Light, Photoshop/Lightroom relight, Krea, Magnific relight. What prompt phrasing best keeps geometry locked ("keep composition, camera and every object identical; change only time of day/lighting")? Known failure modes (objects added/removed, structure drift, text artifacts).
5. Anything measured about cover choice affecting Reels/Shorts performance (e.g., YouTube's own statements on Shorts thumbnails, Instagram statements on cover/grid). Keep it short; flag hype.

Output: a single Markdown report written to <scratchpad>/kapak_stil_arastirma.md with sections 1–5, each a compact list of claims with tags and URLs, then a final "Recommendations for the guide" list (max 12 bullets) that separates what is supported vs. your judgment. Write the report in English. Then return to me a ~300-word summary of the strongest findings and the file path. Do not edit any files in the repository.
