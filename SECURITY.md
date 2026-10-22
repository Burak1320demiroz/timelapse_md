# Security Policy

## Supported Versions

We provide security updates and patches for the following versions of the `timelapse_md` production pipeline:

| Version | Supported | Status |
|---|:---:|---|
| **2.0.x** (Current Hat v2) | :white_check_mark: | Actively supported and maintained |
| < 2.0.0 (Legacy Pipeline) | :x: | Frozen archive; no security updates |

---

## Reporting a Vulnerability

The `timelapse_md` team and **Apex AI Timelapse** take the security and integrity of our codebase, tools, and developer environments seriously.

If you discover a security vulnerability or sensitive information exposure in this repository, please do **NOT** open a public issue. Instead, report it privately through one of the following channels:

1. **GitHub Private Vulnerability Reporting:**
   Use GitHub's built-in private reporting feature by navigating to **Security** -> **Advisories** -> **Report a vulnerability**.
2. **Direct Contact:**
   Contact the repository maintainer directly via GitHub profile messaging or email at `burakdemirozis16@gmail.com`.

### Scope of Security Concerns
- **API Key & Secret Leaks:** Exposure of LLM provider keys (`ANTHROPIC_API_KEY`, `GEMINI_API_KEY`), video generation platform credentials (Veo, Runway, Luma), social media upload tokens, or cloud access keys.
- **Command Injection & Path Traversal:** Unsanitized arguments or subprocess invocations inside verification scripts (`prompt_kontrol.py`, `zincir_kontrol.sh`, `qa_paket.sh`, `kesme_kontrol.sh`, `ihrac_kontrol.sh`).
- **Filesystem Integrity:** Bypassing workspace isolation, unauthorized media inclusion in commits, or malicious scripts in the pipeline.

### What to Include in Your Report
To help us resolve the issue swiftly, please include:
- A clear description of the vulnerability.
- Steps to reproduce or proof-of-concept (PoC).
- Potential impact and affected files or commands.
- Suggested remediation or patch, if available.

### Response Timeline
- **Initial Acknowledgement:** Within 48 hours.
- **Triage & Status Update:** Within 5 business days.
- **Resolution & Disclosure:** A patch will be published alongside an advisory once verified.

Thank you for responsibly disclosing vulnerabilities and keeping the AI timelapse production ecosystem secure.
