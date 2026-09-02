import textwrap

import streamlit as st

LINKEDIN_URL = "https://www.linkedin.com/in/gowthamganesanambikapathy/"
EMAIL_ADDRESS = "gowthamganesanambikapathy@gmail.com"

st.set_page_config(
    page_title="Gowtham Ganesan | TPM & RM Portfolio",
    page_icon="⚡",
    layout="wide",
)

st.markdown(
    textwrap.dedent(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        :root {
            --page-bg: #07070d;
            --glass-bg: rgba(18, 22, 34, 0.58);
            --glass-border: rgba(255, 255, 255, 0.14);
            --text: #eef4ff;
            --muted: #a9b8d3;
            --teal: #5eead4;
            --pink: #f0abfc;
            --gold: #fde68a;
            --violet: #c4b5fd;
            --shadow: rgba(0, 0, 0, 0.3);
        }

        html, body, [data-testid="stAppViewContainer"], .stApp {
            background: var(--page-bg) !important;
            color: var(--text);
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
        }

        [data-testid="stHeader"] { background: transparent !important; }
        header { visibility: hidden; }
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        [data-testid="stToolbar"] { visibility: hidden; }
        [data-testid="stDecoration"] { display: none; }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 1100px;
        }

        .ambient-layer { position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }
        .orb { position: absolute; border-radius: 50%; filter: blur(90px); opacity: 0.56; }
        .orb-a { width: 46vw; height: 46vw; min-width: 340px; min-height: 340px; top: -14%; left: -8%; background: #4f46e5; animation: ambientA 22s ease-in-out infinite; }
        .orb-b { width: 40vw; height: 40vw; min-width: 300px; min-height: 300px; top: 18%; right: -10%; background: #0d9488; animation: ambientB 25s ease-in-out infinite; }
        .orb-c { width: 36vw; height: 36vw; min-width: 260px; min-height: 260px; bottom: -18%; left: 28%; background: #db2777; animation: ambientC 28s ease-in-out infinite; }

        @keyframes ambientA { 0%, 100% { background: #4f46e5; transform: translate(0,0) scale(1); } 50% { background: #7c3aed; transform: translate(4%,6%) scale(1.06); } }
        @keyframes ambientB { 0%, 100% { background: #0d9488; transform: translate(0,0) scale(1); } 50% { background: #2563eb; transform: translate(-5%,4%) scale(1.08); } }
        @keyframes ambientC { 0%, 100% { background: #db2777; transform: translate(0,0) scale(1); } 50% { background: #ea580c; transform: translate(3%,-5%) scale(1.04); } }

        .ambient-veil {
            position: fixed; inset: 0; z-index: 1; pointer-events: none;
            background: radial-gradient(ellipse at top, rgba(7,7,12,0.15), transparent 55%), linear-gradient(180deg, rgba(7,7,12,0.30) 0%, rgba(7,7,12,0.6) 100%);
        }

        .ambient-grain {
            position: fixed; inset: 0; z-index: 2; pointer-events: none; opacity: 0.035;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
        }

        .stApp > .main, [data-testid="stAppViewContainer"] > .main { position: relative; z-index: 3; background: transparent !important; }
        [data-testid="stVerticalBlock"] { gap: 0 !important; }

        .hero-container {
            max-width: 980px; margin: 0 auto; text-align: center; padding: 3.2rem 1rem 1rem;
            animation: riseIn 0.8s ease both;
        }

        .hero-kicker {
            display: inline-flex; align-items: center; justify-content: center; padding: 0.42rem 0.95rem; border-radius: 999px;
            border: 1px solid rgba(94, 234, 212, 0.28); background: rgba(94, 234, 212, 0.08); color: var(--teal);
            font-size: 0.76rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 1.4rem;
            backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
        }

        .hero-title {
            font-size: clamp(2.5rem, 6vw, 5.3rem); line-height: 0.95; font-weight: 800; letter-spacing: -0.05em; margin: 0;
            background: linear-gradient(125deg, #eff5ff 10%, #9ad7d5 35%, #d9c3ff 70%, #f5d0ff 100%);
            background-size: 180% 180%; -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
            animation: titleSheen 14s ease-in-out infinite;
        }

        @keyframes titleSheen { 0%, 100% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } }

        .hero-subtitle {
            max-width: 760px; margin: 1.7rem auto 0; color: var(--muted); font-size: clamp(1.08rem, 2vw, 1.5rem); line-height: 1.6;
        }

        .skill-row {
            display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin: 2rem auto 2.5rem; max-width: 900px;
            animation: riseIn 1s ease 0.12s both;
        }

        .skill-pill {
            display: inline-flex; align-items: center; justify-content: center; padding: 0.65rem 1rem; border-radius: 14px;
            border: 1px solid rgba(255,255,255,0.14); background: rgba(255,255,255,0.04); color: var(--text);
            font-size: 0.8rem; font-weight: 700; letter-spacing: 0.04em;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.12), 0 10px 24px rgba(0,0,0,0.18);
        }

        .skill-pill:nth-child(1) { color: var(--teal); border-color: rgba(94,234,212,0.35); }
        .skill-pill:nth-child(2) { color: var(--pink); border-color: rgba(240,171,252,0.35); }
        .skill-pill:nth-child(3) { color: var(--gold); border-color: rgba(253,230,138,0.35); }
        .skill-pill:nth-child(4) { color: var(--violet); border-color: rgba(196,181,253,0.35); }
        .skill-pill:nth-child(5) { color: #a5f3fc; border-color: rgba(103,232,249,0.35); }

        .glass-panel {
            background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 28px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.12), 0 18px 40px var(--shadow);
            backdrop-filter: blur(28px) saturate(160%); -webkit-backdrop-filter: blur(28px) saturate(160%);
            padding: 1.4rem 1.2rem 1.1rem;
        }

        .intro-card {
            background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
            border: 1px solid rgba(255,255,255,0.08); border-radius: 22px;
            padding: 1.35rem 1.2rem; line-height: 1.7; color: var(--text);
        }

        .intro-card h3 {
            margin: 0 0 0.8rem; font-size: 0.9rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--teal);
        }

        .intro-card p { margin: 0 0 1rem; color: #dfe9ff; font-size: 1.02rem; }

        .story-chapters { display: grid; gap: 1rem; margin-top: 1.4rem; }
        .story-chapter { position: relative; padding: 1.25rem 1.2rem 1.1rem; border: 1px solid rgba(255,255,255,0.1); border-radius: 22px; background: rgba(255,255,255,0.035); overflow: hidden; }
        .story-chapter::before { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: linear-gradient(180deg, var(--teal), var(--pink)); }
        .story-badge { color: var(--gold); font-size: 0.68rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; }
        .story-title { margin: 0.45rem 0 0.3rem; color: #fff; font-size: clamp(1.2rem, 2.4vw, 1.75rem); font-weight: 800; }
        .story-meta { color: var(--teal); font-size: 0.88rem; font-weight: 700; margin-bottom: 0.9rem; }
        .story-copy { color: #dfe9ff; line-height: 1.72; margin: 0 0 0.9rem; font-size: 0.96rem; }
        .story-quote { margin: 1rem 0; padding: 0.85rem 1rem; border-left: 3px solid var(--pink); border-radius: 0 14px 14px 0; background: rgba(240,171,252,0.06); color: var(--gold); font-style: italic; line-height: 1.55; }

        .featured-skills-title { margin: 1.5rem 0 0.8rem; color: var(--pink); font-size: 0.82rem; letter-spacing: 0.12em; text-transform: uppercase; }
        .featured-skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 0.75rem; }
        .featured-skill-card { border: 1px solid rgba(255,255,255,0.1); border-radius: 18px; padding: 0.9rem; background: rgba(255,255,255,0.035); }
        .featured-skill-heading { font-weight: 800; color: var(--text); font-size: 0.84rem; margin-bottom: 0.55rem; }
        .featured-skill-list { margin: 0; padding-left: 1rem; color: var(--muted); font-size: 0.78rem; line-height: 1.55; }

        .chip-row { display: flex; flex-wrap: wrap; gap: 0.55rem; margin-top: 0.8rem; }
        .chip {
            font-size: 0.76rem; font-weight: 700; letter-spacing: 0.04em; padding: 0.5rem 0.85rem; border-radius: 999px;
            border: 1px solid rgba(255,255,255,0.12); background: rgba(255,255,255,0.04); color: var(--text);
        }

        .experience-stack { display: grid; gap: 1rem; }

        .experience-card {
            display: grid; grid-template-columns: 88px 1fr; gap: 1rem; align-items: center;
            background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 22px; padding: 1rem 1.1rem;
        }

        .company-logo {
            width: 88px; height: 88px; border-radius: 20px; display: flex; align-items: center; justify-content: center;
            font-size: 1.7rem; font-weight: 800; letter-spacing: -0.06em; color: #fff;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.2), 0 16px 28px rgba(0,0,0,0.2);
        }

        .level-badge { display: inline-block; margin-bottom: 0.45rem; color: var(--gold); font-size: 0.68rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; }

        .company-name { font-size: clamp(1.15rem, 2vw, 1.55rem); font-weight: 800; margin: 0; }
        .company-role { font-size: 0.96rem; color: var(--teal); font-weight: 700; }
        .company-meta { font-size: 0.8rem; color: var(--muted); letter-spacing: 0.05em; text-transform: uppercase; margin: 0.2rem 0 0.75rem; }
        .achievements { margin: 0; padding-left: 1.1rem; color: #dfe9ff; line-height: 1.7; }

        .project-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
        .project-card {
            background: rgba(255,255,255,0.035); border: 1px solid rgba(255,255,255,0.08); border-radius: 22px;
            padding: 1.15rem 1.05rem; min-height: 224px; display: flex; flex-direction: column; justify-content: space-between;
            transition: transform 0.22s ease, border-color 0.22s ease;
        }
        .project-card:hover { transform: translateY(-4px); border-color: rgba(196,181,253,0.34); }
        .project-title { font-size: 1.1rem; font-weight: 800; margin-bottom: 0.6rem; }
        .project-desc { color: var(--muted); line-height: 1.7; font-size: 0.96rem; }
        .project-tag { display: inline-block; margin-top: 1rem; font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase; font-weight: 700; color: var(--violet); }

        .creative-gate { display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; max-width: 1100px; margin: 0 auto 1.2rem; padding: 0.8rem 1rem; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; background: rgba(255,255,255,0.025); color: var(--muted); font-size: 0.78rem; }
        .creative-zone { position: relative; overflow: hidden; margin-top: 1.2rem; padding: 1.4rem; border: 1px solid rgba(240,171,252,0.32); border-radius: 26px; background: linear-gradient(135deg, rgba(12,16,38,0.9), rgba(64,20,77,0.64)); box-shadow: inset 0 1px 0 rgba(255,255,255,0.16), 0 24px 60px rgba(19,5,40,0.38); animation: creativeReveal 0.7s ease both; }
        .creative-zone::before, .creative-zone::after { content: ""; position: absolute; border-radius: 50%; pointer-events: none; border: 1px solid rgba(94,234,212,0.24); animation: orbitPulse 8s ease-in-out infinite; }
        .creative-zone::before { width: 320px; height: 320px; right: -100px; top: -170px; }
        .creative-zone::after { width: 220px; height: 220px; left: -80px; bottom: -130px; border-color: rgba(240,171,252,0.22); animation-delay: -3s; }
        .creative-kicker { position: relative; z-index: 1; color: var(--pink); font-size: 0.72rem; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; }
        .creative-title { position: relative; z-index: 1; margin: 0.5rem 0; font-size: clamp(1.7rem, 4vw, 3.2rem); line-height: 1; font-weight: 800; background: linear-gradient(100deg, #fff, var(--teal), var(--pink)); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
        .creative-copy { position: relative; z-index: 1; max-width: 670px; color: #dfe9ff; line-height: 1.7; margin-bottom: 1.2rem; }
        .creative-orbit-grid { position: relative; z-index: 1; display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.7rem; }
        .creative-orbit-card { min-height: 92px; padding: 0.9rem; border: 1px solid rgba(255,255,255,0.14); border-radius: 18px; background: rgba(255,255,255,0.06); backdrop-filter: blur(12px); transition: transform 0.2s ease, background 0.2s ease; }
        .creative-orbit-card:hover { transform: translateY(-4px) rotate(-1deg); background: rgba(255,255,255,0.1); }
        .creative-orbit-card strong { display: block; color: var(--gold); font-size: 0.86rem; margin-bottom: 0.35rem; }
        .creative-orbit-card span { color: var(--muted); font-size: 0.76rem; line-height: 1.45; }
        @keyframes creativeReveal { from { opacity: 0; transform: translateY(16px) scale(0.98); } to { opacity: 1; transform: translateY(0) scale(1); } }
        @keyframes orbitPulse { 0%, 100% { transform: rotate(0deg) scale(1); opacity: 0.42; } 50% { transform: rotate(24deg) scale(1.08); opacity: 0.82; } }
        @media (prefers-reduced-motion: reduce) { .creative-zone, .creative-zone::before, .creative-zone::after { animation: none; } .creative-orbit-card { transition: none; } }

        .site-footer { margin-top: 2rem; padding: 1.2rem 0 0.3rem; }
        .footer-row { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.9rem; align-items: center; }
        .social-pill {
            display: inline-flex; align-items: center; gap: 0.6rem; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.12);
            color: var(--text); border-radius: 999px; padding: 0.7rem 0.95rem; font-size: 0.83rem; font-weight: 700; text-decoration: none;
            transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease; box-shadow: 0 10px 24px rgba(0,0,0,0.18);
        }
        .social-pill:hover { transform: translateY(-3px) scale(1.01); box-shadow: 0 16px 32px rgba(0,0,0,0.24); border-color: rgba(94,234,212,0.32); }
        .social-pill svg { width: 1rem; height: 1rem; fill: currentColor; }
        .footer-name { text-align: center; color: var(--muted); font-size: 0.8rem; margin-top: 0.9rem; letter-spacing: 0.08em; text-transform: uppercase; }

        @keyframes riseIn { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
        @media (max-width: 640px) { .hero-container { padding-top: 2.4rem; } .orb { filter: blur(70px); opacity: 0.44; } .experience-card { grid-template-columns: 1fr; } .company-logo { width: 70px; height: 70px; } }
        </style>
        """
    ),
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="ambient-layer" aria-hidden="true">
        <div class="orb orb-a"></div>
        <div class="orb orb-b"></div>
        <div class="orb orb-c"></div>
    </div>
    <div class="ambient-veil" aria-hidden="true"></div>
    <div class="ambient-grain" aria-hidden="true"></div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-container">
        <div class="hero-kicker">TPM • Release • AI tooling</div>
        <div class="hero-title">Orchestrating Enterprise Delivery.</div>
        <div class="hero-subtitle">Steering complex systems with precision. Blending 8+ years of robust Program &amp; Release Management governance with high-energy AI vibe-coding.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

skill_stack = [
    "Program Management",
    "Release Governance",
    "Agile Delivery",
    "Stakeholder Strategy",
    "AI Automation",
]

st.markdown(
    """
    <div class="skill-row">
        {skills}
    </div>
    """.format(skills="".join(f'<span class="skill-pill">{skill}</span>' for skill in skill_stack)),
    unsafe_allow_html=True,
)

creative_mode = st.toggle("Creative mode", value=False, key="creative_mode", help="Unlock the private visual portfolio with the magic phrase.")
creative_unlocked = False
if creative_mode:
    magic_phrase = st.text_input("Magic phrase", type="password", placeholder="Enter the phrase to unlock", label_visibility="collapsed")
    creative_unlocked = magic_phrase.strip().casefold() == "orchestrate the impossible"
    st.caption("Private creative layer is locked until the phrase is entered." if not creative_unlocked else "Creative layer unlocked.")

if creative_unlocked:
    st.markdown(
        """
        <div class="creative-zone">
            <div class="creative-kicker">Private creative layer · for friends and curious minds</div>
            <div class="creative-title">Governance, but make it kinetic.</div>
            <div class="creative-copy">This is the playful side of the portfolio: a compact visual signature for experimentation, motion, and imagination. The professional portfolio remains the default experience.</div>
            <div class="creative-orbit-grid">
                <div class="creative-orbit-card"><strong>01 · Imagine</strong><span>Turn a rough idea into a visible system.</span></div>
                <div class="creative-orbit-card"><strong>02 · Compose</strong><span>Shape moving parts into a clear rhythm.</span></div>
                <div class="creative-orbit-card"><strong>03 · Animate</strong><span>Give the work enough energy to be remembered.</span></div>
                <div class="creative-orbit-card"><strong>04 · Deliver</strong><span>Keep the magic useful, focused, and real.</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

intro_options = {
    "First Day at a New Job": (
        "I’m excited to join the team and I like to start by learning the operating rhythm quickly: the stakeholders, the release process, the critical dependencies, and the metrics that define success. I bring a calm, organized approach and I like to earn trust by doing the work reliably before trying to scale it. My strength is turning ambiguity into structure and making teams move with clarity.",
        ["Quick ramp-up", "Stakeholder alignment", "Release discipline", "Delivery momentum"],
    ),
    "Interviewer Intro": (
        "I’m a TPM and Release Management professional with 8+ years of experience in enterprise delivery, governance, and high-risk rollout execution. I’ve led multi-environment programs, release controls, cross-functional coordination, and PMO frameworks across customer-facing and internal transformation work. I combine strong delivery operations with AI-enabled tooling to improve speed, visibility, and decision quality.",
        ["8+ years experience", "Enterprise delivery", "Risk & governance", "AI-assisted PMO"],
    ),
    "Tell Me About Yourself": (
        "I’m a program and release management professional who enjoys building dependable systems in fast-moving environments. My background spans release governance, cross-functional project delivery, PMO architecture, and AI-driven operational tooling. I’ve worked across consulting, enterprise implementations, and digital transformation projects, and I’m energized by work that combines structure, strategy, and practical execution.",
        ["TPM mindset", "Release excellence", "AI-powered tooling", "Business value delivery"],
    ),
}

intro_chapters = [
    {
        "badge": "Level 01 • The Foundation",
        "title": "Controlling the Control Room",
        "role": "Release & Deployment Manager | Cognizant",
        "timeline": "March 2016 – December 2018",
        "story": "Every great production is orchestrated from above. Managing high-stakes multi-environment builds and strict Change Advisory Board (CAB) protocols taught me how to keep every operation airtight. I designed release playbooks used across 15+ Fortune 500 clients, orchestrating parallel tracks of UAT testing, production cutover coordination, and zero-downtime deployments across global data centers.",
        "quote": "Absolute control over underlying release mechanics creates total operational freedom.",
        "story_2": "Standardized core rollout playbooks, securing absolute compliance and zero critical post-release incidents across 15+ enterprise clients.",
        "skills": ["CAB Governance", "ServiceNow", "ITIL Framework", "Release Tracking", "Defect Shielding"],
    },
    {
        "badge": "Level 02 • The Orchestrator",
        "title": "Synchronizing Large-Scale Systems",
        "role": "Technical Project Manager | Guidewire Software",
        "timeline": "June 2020 – September 2024",
        "story": "Scaling up meant handling complex multi-tiered enterprise implementations across full SDLC cycles. Pulling the strings between development, QA, and business stakeholders required tuning a thousand moving parts into perfect alignment. Led large-scale InsuranceSuite implementations managing cross-functional teams, intricate dependency mapping, and regulatory compliance gates for premium-processing systems handling $500M+ in annual claims.",
        "quote": "Great project management pulls all the right technical threads together into a single rhythm.",
        "story_2": "Through disciplined Scrum-of-Scrums alignment and structured Jira deployment gating, I cut lower-environment downtime by 15% and accelerated delivery cycles.",
        "skills": ["Guidewire InsuranceSuite", "Scrum-of-Scrums", "Jira & Confluence", "Go/No-Go Gates", "RCA Analysis"],
    },
    {
        "badge": "Level 03 • The Systems Designer",
        "title": "Designing the Human Operating System",
        "role": "Senior Technology Consultant | Qualtrics",
        "timeline": "September 2024 – March 2025",
        "story": "At Qualtrics, I architected end-to-end SaaS implementation playbooks that bridged enterprise systems with human-centered change management. Centralized Coda resource portals, governance artifacts, and stakeholder cadences gave teams a shared operating system for moving from post-sales handover to client launch.",
        "quote": "The strongest delivery architecture makes complex change feel navigable for the people inside it.",
        "story_2": "Directed full-lifecycle enterprise implementations, engineered a centralized PMO Handbook and execution template library, and balanced out-of-the-box configuration with custom engineering to eliminate scope creep.",
        "skills": ["Qualtrics SaaS", "Coda Portals", "PMO Handbook", "Change Management", "Stakeholder Sync"],
    },
    {
        "badge": "Level 04 • The PMO Architect",
        "title": "Engineering the Delivery Blueprint",
        "role": "Implementation Project Manager | Folens",
        "timeline": "July 2025 – October 2025",
        "story": "At this stage, the mission shifted to building brand-new delivery architectures from scratch. Managing $650K ERP rollouts (Dynamics 365) and centralized Coda resource portals meant establishing governance at scale, designing UAT playbooks, and orchestrating cross-functional alignment. I owned the full PMO transformation roadmap. At Folens, this meant engineering governance models, resource capacity planning systems, and stakeholder communication cadences that could carry a complex implementation from design through delivery.",
        "quote": "A master architect doesn't just manage the pieces; they design how the whole ecosystem moves.",
        "story_2": "Delivered Phase 1 rollouts four weeks ahead of schedule and automated business workflows by 30%, creating reusable playbooks for 3+ future implementations. At Folens, this also reduced early-stage deployment defects by 25% via Model Office Testing and custom AI reporting.",
        "skills": ["Dynamics 365", "PMO Architecture", "Coda Portals", "UAT Mastery", "Stakeholder Sync", "Model Office Testing", "Change Control", "AI Reporting"],
    },
    {
        "badge": "Level 05 • The Self-Directed Builder",
        "title": "AI Vibe-Coding & Rapid Innovation",
        "role": "AI Tooling Specialist | Independent R&D",
        "timeline": "February 2026 – Present",
        "story": "Combining 8 years of solid enterprise governance with modern AI-assisted prototyping tools. I build interactive web apps, dashboards and automated tooling to eliminate manual PMO busywork. Leveraging prompt engineering, model context protocols, and rapid iteration cycles to create living documentation systems, intelligent governance bots, and dynamic portfolio intelligence platforms that empower delivery teams with real-time insights.",
        "quote": "The future belongs to builders who can bridge rigorous governance with rapid, animated execution.",
        "story_2": "Deploying custom Python/Streamlit dashboards, prompt-engineered pipelines, and dynamic micro-apps for enterprise clients seeking modern delivery infrastructure.",
        "skills": ["Vibe Coding", "Streamlit Apps", "MCP Agents", "Python Automation", "LLM Tooling"],
    },
]

experience_cards = [
    {
        "level": "Level 05 · The Self-Directed Builder",
        "company": "AI Tooling & PMO",
        "short": "AI",
        "logo_bg": "linear-gradient(135deg, #00f5d4, #7b2cbf)", # Futuristic Teal to Deep Purple
        "role": "AI Tooling & PMO Orchestrator",
        "period": "January 2026 – Present",
        "highlights": [
            "Pioneered 'vibe coding' workflows using LLMs and MCP servers to automate enterprise governance artifacts.",
            "Built custom Streamlit dashboards to eliminate common PMO operational and data bottlenecks.",
            "Maintained active GitHub repositories showcasing automated report engines and version-controlled workflows."
        ],
    },
    {
        "level": "Level 03 · The Systems Designer",
        "company": "Qualtrics",
        "short": "Q",
        "logo_bg": "linear-gradient(135deg, #14b8a6, #0284c7)", # Deep Cyan to Ocean Blue
        "role": "Senior Technology Consultant",
        "period": "September 2024 – March 2025",
        "highlights": [
            "Directed full-lifecycle enterprise SaaS implementations from post-sales handover to client launch.",
            "Engineered a centralized PMO Handbook and execution template library using Coda.",
            "Balanced Out-of-the-Box configuration with custom engineering to eliminate client scope creep."
        ],
    },
    {
        "level": "Level 04 · The PMO Architect",
        "company": "Folens",
        "short": "F",
        "logo_bg": "linear-gradient(135deg, #ff007f, #7928ca)", # Vibrant Pink to Royal Purple
        "role": "Implementation Project Manager",
        "period": "July 2025 – October 2025",
        "highlights": [
            "Delivered Phase 1 of a $650K Microsoft Dynamics 365 rollout 4 weeks ahead of schedule.",
            "Achieved 30% process automation by architecting strict triage and change control PMO frameworks.",
            "Reduced early-stage deployment defects by 25% via Model Office Testing and custom AI reporting."
        ],
    },
    {
        "level": "Level 02 · The Orchestrator",
        "company": "Guidewire",
        "short": "G",
        "logo_bg": "linear-gradient(135deg, #f59e0b, #e11d48)", # Amber to Crimson Red
        "role": "Project Analyst & Release Coordinator",
        "period": "June 2020 – September 2024",
        "highlights": [
            "Coordinated multi-environment InsuranceSuite deployments across distributed Scrum-of-Scrums teams.",
            "Reduced lower-environment downtime by 15% by implementing daily Jira checklists and Go/No-Go gates.",
            "Optimized delivery stability by facilitating post-release evaluations and Root Cause Analyses (RCA)."
        ],
    },
    {
        "level": "Level 01 · The Foundation",
        "company": "Cognizant",
        "short": "C",
        "logo_bg": "linear-gradient(135deg, #3b82f6, #1d4ed8)", # Tech Blue to Corporate Dark Blue
        "role": "Release & Deployment Manager",
        "period": "March 2016 – December 2018",
        "highlights": [
            "Enforced strict Change Advisory Board (CAB) governance via ServiceNow across Dev, QA, and Prod environments.",
            "Authored the Release Implementation Playbook, achieving zero critical post-deployment incidents.",
            "Accelerated defect resolution by 25% through standardized UAT triaging and post-release routines."
        ],
    }
]

featured_skills = [
    {
        "category": "AI Innovation & Automation",
        "icon": "🤖",
        "gradient": "linear-gradient(135deg, #00f5d4, #7b2cbf)", # Matches your AI Orchestrator card
        "skills": [
            "Prompt Engineering",
            "Vibe Coding / LLM Tools",
            "Model Context Protocol (MCP)",
            "Streamlit Dashboard Development",
            "AI Agent Workflows"
        ]
    },
    {
        "category": "Program & PMO Management",
        "icon": "📊",
        "gradient": "linear-gradient(135deg, #ff007f, #7928ca)", # Matches your Folens card
        "skills": [
            "Enterprise PMO Setup",
            "Agile / Scrum-of-Scrums",
            "Stakeholder Management",
            "Resource Libraries (Coda/Notion)",
            "Governance Frameworks"
        ]
    },
    {
        "category": "Technical Delivery & Validation",
        "icon": "⚙️",
        "gradient": "linear-gradient(135deg, #14b8a6, #0284c7)", # Matches your Qualtrics card
        "skills": [
            "User Acceptance Testing (UAT)",
            "Defect Triage Workflows",
            "Model Office Testing",
            "System Validation",
            "Knowledge Transfer & Onboarding"
        ]
    },
    {
        "category": "Release Management & SDLC",
        "icon": "🚀",
        "gradient": "linear-gradient(135deg, #f59e0b, #e11d48)", # Matches your Guidewire card
        "skills": [
            "Release Coordination",
            "Multi-Environment Deployments",
            "Root Cause Analysis (RCA)",
            "Go/No-Go Gatekeeping",
            "Change Advisory Board (CAB)"
        ]
    },
    {
        "category": "Enterprise Tools & Ecosystems",
        "icon": "💼",
        "gradient": "linear-gradient(135deg, #3b82f6, #1d4ed8)", # Matches your Cognizant card
        "skills": [
            "MS Dynamics 365 Business Central",
            "Guidewire InsuranceSuite",
            "Qualtrics SaaS",
            "Jira & ServiceNow",
            "GitHub & Version Control"
        ]
    }
]

project_cards = [
    {
        "title": "Portfolio Experience Engine",
        "desc": "A polished digital portfolio experience designed to blend enterprise storytelling with AI innovation and a premium glassmorphism interface.",
        "stack": "Python • Streamlit • Responsive UI",
    },
    {
        "title": "PMO Governance Assistants",
        "desc": "AI-assisted operational tooling to synthesize project health metrics, executive summaries, and stakeholder-ready delivery narratives.",
        "stack": "MCP • Prompt design • Automation",
    },
    {
        "title": "Release Intelligence Dashboard",
        "desc": "A powerful view of delivery health, dependency tracking, risk posture, and release readiness across enterprise programs.",
        "stack": "Python • Dashboarding • Analytics",
    },
    {
        "title": "AI Workflow Prototyping",
        "desc": "Rapid prototyping of tools to reduce manual PMO effort, accelerate decision-making, and improve how teams collaborate around execution risk.",
        "stack": "LLMs • Workflow automation • Product thinking",
    },
]

intro_tab, experience_tab, showcase_tab = st.tabs(["Intro", "Experience", "AI Showcase"])

with intro_tab:
    show_intro_variants = st.toggle("Reveal intro variations", value=False, key="intro_toggle")
    selected_intro = "Tell Me About Yourself"
    if show_intro_variants:
        selected_intro = st.selectbox("Choose intro style", list(intro_options.keys()), index=2, label_visibility="collapsed")

    content, skills = intro_options[selected_intro]
    featured_html = "".join(
        """
        <div class="featured-skill-card" style="border-color: {gradient};">
            <div class="featured-skill-heading">{icon} {category}</div>
            <ul class="featured-skill-list">{items}</ul>
        </div>
        """.format(
            gradient=group["gradient"].split(",")[-1].replace(")", ""),
            icon=group["icon"],
            category=group["category"],
            items="".join(f"<li>{skill}</li>" for skill in group["skills"]),
        )
        for group in featured_skills
    )
    st.markdown(
        """
        <div class="glass-panel intro-card">
            <h3>Selected intro</h3>
            <p>{content}</p>
            <div class="chip-row">{chips}</div>
            <div class="featured-skills-title">Featured skills</div>
            <div class="featured-skills-grid">{featured}</div>
        </div>
        """.format(content=content, chips="".join(f'<span class="chip">{value}</span>' for value in skills), featured=featured_html),
        unsafe_allow_html=True,
    )

    chapter_html = "".join(
        """
        <article class="story-chapter">
            <div class="story-badge">{badge}</div>
            <h3 class="story-title">{title}</h3>
            <div class="story-meta">{role} &nbsp;•&nbsp; {timeline}</div>
            <p class="story-copy">{story}</p>
            <div class="story-quote">“{quote}”</div>
            <p class="story-copy">{story_2}</p>
            <div class="chip-row">{chips}</div>
        </article>
        """.format(
            badge=chapter["badge"],
            title=chapter["title"],
            role=chapter["role"],
            timeline=chapter["timeline"],
            story=chapter["story"],
            quote=chapter["quote"],
            story_2=chapter["story_2"],
            chips="".join(f'<span class="chip">{skill}</span>' for skill in chapter["skills"]),
        )
        for chapter in intro_chapters
    )
    st.html(f'<div class="story-chapters">{chapter_html}</div>')

with experience_tab:
    cards_html = "".join(
        """
        <div class="experience-card">
            <div class="company-logo" style="background: {logo_bg};">{short}</div>
            <div>
                <div class="level-badge">{level}</div>
                <div class="company-name">{company}</div>
                <div class="company-role">{role}</div>
                <div class="company-meta">{period}</div>
                <ul class="achievements">{highlights}</ul>
            </div>
        </div>
        """.format(
            logo_bg=card["logo_bg"],
            short=card["short"],
            level=card["level"],
            company=card["company"],
            role=card["role"],
            period=card["period"],
            highlights="".join(f"<li>{item}</li>" for item in card["highlights"]),
        )
        for card in experience_cards
    )
    st.html(f'<div class="glass-panel"><div class="experience-stack">{cards_html}</div></div>')

with showcase_tab:
    project_html = "".join(
        """
        <div class="project-card">
            <div>
                <div class="project-title">{title}</div>
                <div class="project-desc">{desc}</div>
            </div>
            <div class="project-tag">{stack}</div>
        </div>
        """.format(title=card["title"], desc=card["desc"], stack=card["stack"]) for card in project_cards
    )
    st.html(f'<div class="glass-panel"><div class="project-grid">{project_html}</div></div>')

st.markdown(
    """
    <div class="site-footer">
        <div class="footer-row">
            <a class="social-pill" href="mailto:{email}" target="_blank" rel="noopener noreferrer">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4-8 5-8-5V6l8 5 8-5v2Z"/></svg>
                Email
            </a>
            <a class="social-pill" href="{linkedin}" target="_blank" rel="noopener noreferrer">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.94 8.5A1.56 1.56 0 1 1 6.94 5.4a1.56 1.56 0 0 1 0 3.1ZM5.5 9.7h2.9V18H5.5V9.7Zm5.1 0h2.8v1.13h.04c.39-.74 1.35-1.52 2.78-1.52 2.98 0 3.53 1.96 3.53 4.51V18h-2.9v-16.7c0-1.17-.02-2.68-1.63-2.68-1.64 0-1.89 1.28-1.89 2.59V18h-2.9V9.7Z"/></svg>
                LinkedIn
            </a>
        </div>
        <div class="footer-name">Gowtham Ganesan • TPM &amp; Release Management</div>
    </div>
    """.format(email=EMAIL_ADDRESS, linkedin=LINKEDIN_URL),
    unsafe_allow_html=True,
)
