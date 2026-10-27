# 📥 A43 — HAM SONUÇ (dokunulmadı)

```
KÜNYE
BOT        Claude Sonnet 5.5 alt ajan (Claude Code · effort medium · web arama + özetleyici sayfa okuyucu)
TARİH      25.10.2026 (sahip isteğiyle koşuldu: "alt agent sonnet 5.5 medium çalıştırıp araştırma yapabilirsin")
PROMPT     arastirma/A43_DIKEY_KAPAK_STILI.md — prompt bu depoda yazıldı
KESİLDİ Mİ hayır — ajan raporu tek dosya olarak yazdı; aşağısı o dosyanın birebir kopyası
SÜRE       ≈ 2 dk 13 sn · 27 araç çağrısı
DENETİM    ayrı denetim dosyası YOK · URL'ler ajanın beyanıdır; sayfalar ÖZETLEYİCİ okuyucuyla okundu (ajanın notu) —
           sayılar birebir alıntı değil, okuyucunun aktardığıdır. Kılavuza inen her madde A43-x koduyla ⬜ açık.
```

> ⛔ Bu dosya HAM kayıttır: tek karakter düzeltilmez [kart S]. Aşağısı ajanın yazdığı raporun birebir kopyasıdır.

---

# Vertical cover style research (Reels / Shorts, 1080x1920) - 2026-10-25

Tags: [PRIMARY] official/named method; [SECONDARY] reputable design/marketing article; [UNVERIFIED] listicle, no method.
Scope note: web search tool only; I read pages via a summarizing fetcher, so numbers quoted from pages are as reported by it. No repository files edited.

## 1. UI overlay safe zones (1080x1920)

- Meta's own Reels *ad* spec gives margins as percentages: avoid placing text/logos/key elements in top >=14%, bottom >=35%, sides >=6%. On 1080x1920 that is ~269 px top, ~672 px bottom, ~65 px each side. Page fetched in Turkish locale; it states the purpose is avoiding cropping, profile icon/CTA overlap and taller-than-9:16 screens. [PRIMARY, but ADS only] https://www.facebook.com/business/ads-guide/update/video/instagram-reels
- Same numbers repeated by third-party tools (Socialync etc.), which also note platforms publish safe zones for ads, not organic. [SECONDARY] https://www.socialync.io/tools/safe-zones/instagram-reels
- Google Ads help says vertical 1080x1920 ads have a safe-zone graphic (red rectangle, pixel measurements are only in the image, not in text) and that "overlays, call-to-actions, and buttons may appear in different places depending on the format, campaign type, and screen". It also says 9:16 image safe zones are similar to Shorts video. [PRIMARY, ADS] https://support.google.com/google-ads/answer/13547298?hl=en
- Third-party sites attribute to that Google image: top 288, bottom 672, left 48, right 192 px. I could NOT verify these against the image. [SECONDARY/UNVERIFIED] https://www.socialync.io/tools/safe-zones/youtube-shorts , https://explore.picc.co/safe-zone-templates-social-media-videos/
- Another tool reports ad-preview measurements (Mar 2026): top 241, bottom 381, right 201, left 60 px. Conflicts with the above. [UNVERIFIED] https://www.aicarousels.com/free-tools/youtube-safe-zone-checker
- Organic guesses vary widely: right rail 120-230 px wide (~x > 850-960), bottom 250-450 px, top 220-290 px. Reap states its 10-15% side / 25-35% bottom / ~15% top figures are its own "conservative editorial recommendation", not official organic specs. [SECONDARY, self-declared non-official] https://reap.video/blog/short-form-video-safe-zones
- Vertical extent of the right rail: I found only ONE source with a range - rail occupies roughly y 800-1500 (lower-right quadrant) on Reels. Single third-party estimate. [UNVERIFIED] (aggregated via search of https://houseofmarketers.com/guide-to-safe-zones-tiktok-facebook-instagram-stories-reels/ and similar). Socialync/Reap give no rail height.
- Answer to "does rail intrude y 860-1380 at x > ~840?" Could not confirm officially. Every source places the rail (like/comment/share/save) on the right edge in the lower half, and the widest estimates (rail ~190-230 px wide, i.e. x > ~850-890) overlap your y 860-1380 band. Treat x > ~840 in that band as at-risk; the centered core (x 150-930) edge at 930 is inside the widest estimates. Title centered with margin to x ~ 840 is safe under all sources. (Inference, not measured.)
- Wide-screen note: Meta says margins also guard devices taller than 9:16. [PRIMARY ads page above]
- Instagram grid: profile grid is now taller (reports: 3:4 tile, 1080x1440 for Reels covers; others say 4:5/1013x1350). Sources conflict; all third-party. [SECONDARY] https://buffer.com/resources/instagram-grid/ , https://planoly.com/blog/guide-to-instagrams-new-vertical-grid , https://help.hopperhq.com/en/articles/10907941-instagram-s-vertical-grid . Your already-settled 4:5 / 1:1 crop math stands; 3:4 (y 240-1680) is looser than 4:5, so it is covered.

## 2. Title typography

- Fonts: Anton - OFL 1.1 verified in Google Fonts repo (Copyright 2020 The Anton Project Authors). [PRIMARY] https://raw.githubusercontent.com/google/fonts/main/ofl/anton/OFL.txt
- Google Fonts FAQ: fonts usable commercially; ~99% are OFL, rest Apache; per-font license in fonts.google.com/attribution. I did NOT individually confirm Bebas Neue, Archivo Black, Montserrat, Oswald, Inter (all expected OFL; verify). [PRIMARY] https://developers.google.com/fonts/faq
- OFL restriction: cannot sell font alone; modified versions can't use the Reserved Font Name. [SECONDARY] https://v2.4over4.com/guide/are-google-fonts-free-for-commercial-and-print-use
- Common viral-cover faces: Impact, Anton, Bebas Neue (tall, bold, dominate frame); Montserrat/Poppins/Oswald for cleaner looks; heavier weight survives small sizes; 3-4 words max. No data or method cited. [UNVERIFIED] https://1of10.com/blog/youtube-thumbnail-fonts-text/
- Thin fonts lose shape after compression; use bold/extra-bold. Test at ~168x94 px. [UNVERIFIED] https://blog.autonolab.com/blog/2025-09-22-typography-in-thumbnails-text-that-converts/ , https://vloggingpro.com/tools/thumbnail-legibility/
- Stroke/shadow: sources agree on contrast outline or subtle shadow over busy images; stroke ~2-4% of font size, thicker looks cramped. Pure practitioner rules. [UNVERIFIED]. Same pages.
- YouTube's own thumbnail guidance (as quoted by SEJ): fewer words can be impactful, too much text hard to process while scrolling; use high contrast so subject stands out in light and dark mode. [PRIMARY-ish, secondhand quote] https://searchenginejournal.com/youtube-rolls-out-thumbnail-a-b-testing-to-all-channels/519281
- Condensed vs wide, letter-spacing, line count, cap-height % of frame: NOT FOUND with evidence. Also NOT FOUND: any study on outline/glow effects and clickbait perception, or two-colour (accent word) titles. Do not claim support.
- Generic accessibility floor: 3:1 contrast for large text (WCAG; cited by thumbnail guides). [SECONDARY]

## 3. Lighting that reads small

- No thumbnail-specific study (eye tracking / A/B) found for luminance vs hue, blue-hour/warm-window, rim light, or architecture/timelapse. Say plainly: gap.
- Complementary warm/cool is widely asserted to boost subject separation and "vivid" look (film grading), with the caveat that teal-orange is overused. Practitioner explanation, not measured. [SECONDARY/UNVERIFIED] https://morphic.com/ai-glossary/teal-and-orange , https://www.expertphotography.com/orange-and-blue
- Adjacent complements give highest contrast; hue alone is not enough, value/saturation matter. [UNVERIFIED] same.
- YouTube guidance: high contrast between subject and background (see section 2). [secondhand PRIMARY]
- Everything else (single brightest focal point, saturation level) is my judgment, see recommendations.

## 4. AI relighting with geometry locked

- Google's Gemini image docs: edits via text prompts "add, remove, or modify elements, change the style, or adjust the color grading"; pattern "state the change, then what must stay": e.g. "Do not change any other elements of the image." Multi-turn recommended for iteration. [PRIMARY] https://ai.google.dev/gemini-api/docs/image-generation
- Google dev blog templates: "Keep everything else in the image exactly the same, preserving the original style, lighting, and composition."; "change only the [element]"; state that input aspect ratio must not change. Note "preserving lighting" - in a relight prompt, omit lighting from the keep list. Listed limits: may need several iterations; complex typography needs follow-ups; character drift after many edits (restart conversation). [PRIMARY] https://developers.googleblog.com/en/how-to-prompt-gemini-2-5-flash-image-generation-for-the-best-results/
- Adobe (Photoshop with Nano Banana): include lighting and time of day in the prompt (example "golden hour sunset"); each new prompt references the original image, not the previous result; model can alter pose unprompted, so say "keep the same pose" - analogous: name what must not move. [SECONDARY, vendor tutorial] https://www.adobe.com/learn/photoshop/web/nano-banana-generative-edits
- Practitioner blogs: one change per pass, concrete "stays the same" list. [UNVERIFIED] https://storista.io/blog/nano-banana-prompts
- IC-Light: research comparisons report inconsistent highlights/cast shadows and higher geometric drift than newer methods (point-cloud metric, video paper). [SECONDARY, arXiv] https://arxiv.org/pdf/2512.05115 , https://arxiv.org/pdf/2406.07520
- Magnific Relight: manual up to 3 lights or light-transfer from reference image, text prompt or light map; 2024 beta note of unwanted face changes (portraits, not architecture). [SECONDARY] https://www.magnific.com/ai/docs/relight , https://the-decoder.com/magnific-ais-relight-uses-prompts-to-transform-image-lighting-and-backgrounds/
- Krea relight, Photoshop Harmonize, Lightroom relight: nothing reliable found. Gap.
- No systematic data on how often Nano Banana shifts composition, adds/removes objects, or garbles text when relighting. Failure modes listed above are from vendor docs, not measured. Mitigation (my judgment): diff the output against the final frame (overlay/blink compare), reject any structural change, and since cover must be the film's actual final frame, prefer grading/relight only if pixel-structure check passes.

## 5. Cover choice and performance

- YouTube (blog, 24 Jul 2026): YPP creators can upload custom Shorts thumbnails, expanding over time; desktop offers 3 suggested frames; mobile can still pick any frame. Explicitly no performance data, only "helps viewers know what to expect". [PRIMARY] https://blog.youtube/news-and-events/making-thumbnails-easier-on-youtube/ (Engadget/AlternativeTo confirm: https://engadget.com/2223150/youtube-new-tools-thumbnails)
- Instagram: no official statement or Mosseri quote found on cover effect on reach. Whether a cover can be changed after posting is disputed (Planoly: "Adjust Preview"; Superprofile: Help Center says no). Verify in app. [SECONDARY] https://planoly.com/blog/guide-to-instagrams-new-vertical-grid
- Hype flag: "thumbnail A/B testing raises CTR 37-110% / 300%" is a vendor claim, no method. [UNVERIFIED] https://air.io/en/youtube-hacks/how-to-split-test-your-thumbnails-and-choose-the-best-one
- Measured evidence that a Shorts/Reels cover raises performance: none found. Note that Shorts and Reels are primarily feed-swiped, so cover mainly matters on profile grid / search / shared link.

## Recommendations for the guide (max 12)

Supported:
1. Use Meta's ad percentages (14% top / 35% bottom / 6% sides) only as a worst-case reference; they are for ads, not organic. Your core (y 540-1380) exceeds the 35% bottom line (y 1248) at its lower edge, so the lower-mid band (y 1170-1380) is the riskiest in the live feed. [PRIMARY ads]
2. Keep title text at x <= ~840 (or at least centered with >= 240 px side margins) when it sits in y 860-1380; no source shows an official right-rail number, and estimates reach x ~850-890. [partly supported; rail size unverified]
3. Fonts: Anton and others are OFL, commercial use OK; verify each of Bebas Neue, Archivo Black, Montserrat, Oswald, Inter at fonts.google.com/attribution before listing. [PRIMARY for Anton/FAQ]
4. Max 3 words, bold/heavy weight (YouTube also says fewer words, high contrast). [PRIMARY-ish + practitioner]
5. Do not market any specific outline % or shadow as proven; say "practitioner rule". 
6. Say in the guide that Shorts custom thumbnails are YPP-only and Reels cover edit-after-post is unverified, so the baked-in final frame stays the canonical cover.
7. For relight prompts use Google's template pattern: state the lighting change, then "Keep composition, camera, and every object identical; do not add or remove anything; keep the aspect ratio" and drop "preserve lighting" from the keep list. [PRIMARY phrasing]

Judgment (no evidence found):
8. Title band choice: prefer mid (y 860-1060) - furthest from top bar and the 35% bottom line; upper-mid second; lower-mid only for short titles.
9. Condensed heavy sans (Anton / Bebas Neue), all caps, tracking slightly positive (+2-5%), 1 line, cap-height ~4-6% of frame (~80-115 px) - test at 120-160 px width; no source gives these numbers.
10. Prefer a restrained dark (#101315 at 35-50%) soft scrim or very soft shadow over a hard heavy outline, to avoid a clickbait look; two-colour titles (amber accent word) untested - allow at most one amber word.
11. Lighting: single brightest focal point plus warm window glow against blue-hour dark is consistent with practitioner complement theory, but there is no thumbnail-specific data; validate by shrinking covers to 120-160 px and ranking squint-test luminance.
12. Run an A/B check yourself: YouTube Test & Compare (desktop, long-form only per sources; Shorts unconfirmed) cannot be assumed for Shorts.
