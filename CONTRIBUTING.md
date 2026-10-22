# Contributing to timelapse_md

Thank you for your interest in contributing to **timelapse_md** (the production system behind **Apex AI Timelapse**)!

`timelapse_md` is an agentic, docs-as-code production pipeline for photoreal AI construction, civil engineering, and infrastructure timelapses. Because this repository acts as a deterministic build engine and verification framework for generative video pipelines, all contributions must respect our strict architectural invariants, mathematical models, and quality assurance contracts.

---

## Invariant Rules (Non-Negotiable)

Before submitting any Pull Request or proposing modifications, you must review and adhere to the contract defined in [`AGENTS.md`](file:///Users/dai/github/apex_md/timelapse_md/AGENTS.md):

1. **No Video/Media in Git (Strictly Text-Only):**
   - Video clips, raw render frames, and master exports **never enter this repository**.
   - All physical media files reside outside the repository in external storage or release caches.
   - `.gitignore` strictly rejects video, audio, and heavy binary assets.
   - *Sole exception:* Essential documentation diagrams and screenshots located in `images/`.

2. **The Two-Keyframe Chain is Absolute (No Text-to-Video):**
   - Pure Text-to-Video (`T2V`) is strictly prohibited. Every clip is generated via Image-to-Video (`I2V`) bounded between two exact keyframe images ($G_n \to G_{n+1}$).
   - The chain must maintain spatial lock ($< 2\text{ px}$ anchor drift) and monotonic forward progress ($dC/dt \ge 0$).

3. **Frozen Archives are Read-Only:**
   - The legacy 12-lens QA archive (`QA/ARSIV_12_MERCEK/`) and historical research outputs are frozen records. Do not modify, reformat, or alter them.

4. **A Defect Does Not Become a Rule Without Measurement:**
   - In-production failures are recorded in the film's `URETIM_GUNLUGU.md`.
   - New pipeline rules and guidelines require documented, reproducible evidence across at least two distinct productions and formal registration in [`kilavuzlar/DERSLER.md`](file:///Users/dai/github/apex_md/timelapse_md/kilavuzlar/DERSLER.md).

5. **Single Source of Truth for Counts:**
   - Never hardcode file or film counts across multiple files. All statistics must match the output of [`bash araclar/sayac.sh`](file:///Users/dai/github/apex_md/timelapse_md/araclar/sayac.sh).

---

## How to Contribute

### 1. Tooling & Verification Scripts
Our CLI tools live in `araclar/` and use **only standard Python 3 and POSIX shell scripts** (plus `ffmpeg`/`ffprobe` for audio-video verification):
- [`prompt_kontrol.py`](file:///Users/dai/github/apex_md/timelapse_md/araclar/prompt_kontrol.py): Strict production linter checking prompt budgets, keyframe locks, forbidden words, and construction phase gates.
- [`sayac.sh`](file:///Users/dai/github/apex_md/timelapse_md/araclar/sayac.sh): Central repository auditor verifying film matrices, QA tables, and documentation invariants.
- [`zincir_kontrol.sh`](file:///Users/dai/github/apex_md/timelapse_md/araclar/zincir_kontrol.sh): Inter-frame pixel drift and anchor alignment validator.
- [`qa_paket.sh`](file:///Users/dai/github/apex_md/timelapse_md/araclar/qa_paket.sh): 5-lens QA evaluation runner generating standardized audit blocks.
- [`kesme_kontrol.sh`](file:///Users/dai/github/apex_md/timelapse_md/araclar/kesme_kontrol.sh) & [`ihrac_kontrol.sh`](file:///Users/dai/github/apex_md/timelapse_md/araclar/ihrac_kontrol.sh): Final cut timing, speed factor (2x/1x), and end-card duration checkers.

### 2. Improving Production Guidelines & Failure Atlases
Contributions to the knowledge base (`kilavuzlar/`) are welcome when addressing:
- Construction methods and sequencing (`INSAAT_YONTEMI_KILAVUZU.md`).
- Site movement, material flow, and compaction regimes (`SANTIYE_HAREKETI_KILAVUZU.md`).
- Monotonic progression and irreversible phase gates (`MONOTONIK_ILERLEME_VE_FAZ_KAPISI_KILAVUZU.md`).
- Spatial isolation and bounding-box quarantine (`MEKANSAL_IZOLASYON_VE_BOLGE_KARANTINASI_KILAVUZU.md`).

### 3. Empirical Research & Model Calibration
Contributions to `arastirma/` must include raw model outputs, verification audits, and formal assumption entries in `kilavuzlar/VARSAYIMLAR.md`.

---

## Development & Verification Workflow

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Burak1320demiroz/timelapse_md.git
   cd timelapse_md
   ```

2. **Verify Repository Health:**
   Before making any change, ensure the repository passes all automated audits:
   ```bash
   bash araclar/sayac.sh
   ```
   *Expected output:* `✅ TABLO tutarlı` with zero unmanaged `.md` files or broken prompt gates.

3. **Branching & Commit Convention:**
   - Create a feature branch: `git checkout -b feat/your-feature-name`
   - Use conventional commit messages:
     - `feat(...)`: New tools, production guidelines, or film projects.
     - `fix(...)`: Bug fixes in linters, scripts, or prompt constraints.
     - `docs(...)`: Documentation updates, lessons, or QA records.
     - `refactor(...)`: Code cleanup with zero behavioral change.

4. **Verify Lint & Prompt Gates:**
   If you modified or added a film plan:
   ```bash
   python3 araclar/prompt_kontrol.py <FORMAT_DIR>/<FILM_DIR>
   ```

5. **Submit a Pull Request:**
   - Ensure `bash araclar/sayac.sh` exits cleanly (code 0).
   - Describe the motivation, rationale, and empirical verification data in your PR description.

---

## Code of Conduct

All contributors are expected to uphold our community standards as described in [`CODE_OF_CONDUCT.md`](file:///Users/dai/github/apex_md/timelapse_md/CODE_OF_CONDUCT.md).
