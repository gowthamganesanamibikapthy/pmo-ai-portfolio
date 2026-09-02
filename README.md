# Gowtham Ganesan | TPM & AI PMO Portfolio

An interactive Streamlit portfolio for 8+ years of enterprise program, release, implementation, and PMO delivery experience, with a professional-first presentation of AI tooling work.

## Production Version

The production application lives on `main` and is intentionally professional by default. It includes:

- Three tabs: Intro, Experience, and AI Showcase.
- Intro storytelling across five chapters: Cognizant, Guidewire, Qualtrics, Folens, and self-directed AI tooling.
- Distinct progression levels from Foundation through Self-Directed Builder.
- Selectable intro copy for a new job, interviews, and general introductions.
- Experience cards with company badges, roles, dates, and achievement highlights.
- Featured skills across AI innovation, PMO management, technical validation, release management, and enterprise tools.
- AI project showcase cards.
- Clickable LinkedIn and email footer links.

## Friends-Only Creative Version

The private creative experience is isolated on `feature/creative-mode`. It is not part of production `main`.

That branch contains:

- Phrase-gated creative mode using `AlthafBabaVegaMagaRaga`.
- Animated orbit telemetry, motion controls, and creative visual lenses.
- A close-friends-only presentation layer.
- A career-only feedback dialog for gathering advice on skills, direction, and next opportunities.

Run it locally without changing the live professional portfolio:

```powershell
git switch feature/creative-mode
streamlit run app.py
```

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501` in a browser.

## Deploy With Streamlit Community Cloud

1. Push the production `main` branch to GitHub.
2. In Streamlit Community Cloud, create or update the app from this repository.
3. Select branch `main` and file `app.py`.
4. Deploy or reboot the app.

The Streamlit deployment will follow future pushes to `main` when connected to this repository.

## Contact

- LinkedIn: <https://www.linkedin.com/in/gowthamganesanambikapathy/>
- Email: <mailto:gowthamganesanambikapathy@gmail.com>

## Digital Change Log

### 2026-09-02

- Merged the approved tabbed portfolio work into `main`.
- Preserved the professional production view without the friends-only creative mode.
- Added the five-chapter storytelling structure and distinct level progression.
- Added company experience badges, featured skills, AI showcase content, and contact actions.
- Kept the animated creative mode, phrase gate, and career feedback prompt isolated on `feature/creative-mode`.
- Fixed visible HTML rendering issues by using Streamlit's HTML renderer for Experience and AI Showcase cards.
- Fixed the creative animation formatting error caused by CSS braces being interpreted as Python format fields.

### Earlier iterations

- Replaced placeholder release-note artifact labels with expertise and skill labels.
- Added conditional intro variations so alternate intro copy is hidden until requested.
- Added and refined the glass ambient visual system, responsive cards, motion, and accessibility-aware reduced-motion handling.