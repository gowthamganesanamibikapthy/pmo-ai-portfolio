import streamlit as st
import textwrap

st.set_page_config(
    page_title="Gowtham Ganesan | TPM & RM Portfolio",
    page_icon="⚡",
    layout="wide",
)

st.markdown(
    textwrap.dedent("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    :root {
        --glass-bg: rgba(16, 18, 28, 0.55);
        --glass-border: rgba(255, 255, 255, 0.12);
        --glass-highlight: rgba(255, 255, 255, 0.18);
        --text: #f4f6fb;
        --muted: #a8b3c7;
        --accent-teal: #5eead4;
        --accent-pink: #f0abfc;
        --accent-gold: #fde68a;
        --accent-violet: #c4b5fd;
    }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background: #07070c !important;
        color: var(--text);
        font-family: 'Plus Jakarta Sans', sans-serif;
        overflow-x: hidden;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    [data-testid="stDecoration"] {display: none;}

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 4rem;
        max-width: 1080px;
    }

    /* Slow ambient color field — stays in place, no flying particles */
    .ambient-layer {
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        overflow: hidden;
    }

    .orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        opacity: 0.55;
        will-change: transform, background-color;
    }

    .orb-a {
        width: 46vw;
        height: 46vw;
        min-width: 320px;
        min-height: 320px;
        top: -12%;
        left: -8%;
        background: #4f46e5;
        animation: ambientA 22s ease-in-out infinite;
    }

    .orb-b {
        width: 40vw;
        height: 40vw;
        min-width: 280px;
        min-height: 280px;
        top: 18%;
        right: -12%;
        background: #0d9488;
        animation: ambientB 26s ease-in-out infinite;
    }

    .orb-c {
        width: 36vw;
        height: 36vw;
        min-width: 260px;
        min-height: 260px;
        bottom: -16%;
        left: 28%;
        background: #db2777;
        animation: ambientC 30s ease-in-out infinite;
    }

    @keyframes ambientA {
        0%, 100% { background: #4f46e5; transform: translate(0, 0) scale(1); }
        50% { background: #7c3aed; transform: translate(4%, 6%) scale(1.06); }
    }

    @keyframes ambientB {
        0%, 100% { background: #0d9488; transform: translate(0, 0) scale(1); }
        50% { background: #2563eb; transform: translate(-5%, 4%) scale(1.08); }
    }

    @keyframes ambientC {
        0%, 100% { background: #db2777; transform: translate(0, 0) scale(1); }
        50% { background: #ea580c; transform: translate(3%, -5%) scale(1.04); }
    }

    .ambient-veil {
        position: fixed;
        inset: 0;
        z-index: 1;
        pointer-events: none;
        background:
            radial-gradient(ellipse at top, rgba(7, 7, 12, 0.15), transparent 55%),
            linear-gradient(180deg, rgba(7, 7, 12, 0.25) 0%, rgba(7, 7, 12, 0.55) 100%);
    }

    .ambient-grain {
        position: fixed;
        inset: 0;
        z-index: 2;
        pointer-events: none;
        opacity: 0.035;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
    }

    .stApp > .main, [data-testid="stAppViewContainer"] > .main {
        position: relative;
        z-index: 3;
        background: transparent !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }

    .hero-container {
        padding: 4.5rem 1rem 2rem;
        text-align: center;
        max-width: 920px;
        margin: 0 auto;
        animation: riseIn 0.8s ease both;
    }

    .hero-kicker {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.4rem 0.95rem;
        margin-bottom: 1.4rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--accent-teal);
        background: rgba(94, 234, 212, 0.08);
        border: 1px solid rgba(94, 234, 212, 0.22);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
    }

    .hero-title {
        font-size: clamp(2.4rem, 6vw, 4.2rem);
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1.08;
        background: linear-gradient(120deg, #fff 10%, #5eead4 42%, #c4b5fd 68%, #f0abfc 100%);
        background-size: 180% 180%;
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: titleSheen 14s ease-in-out infinite;
        margin-bottom: 1.2rem;
    }

    @keyframes titleSheen {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    .hero-subtitle {
        font-size: clamp(1.05rem, 2vw, 1.35rem);
        color: var(--muted);
        font-weight: 500;
        line-height: 1.65;
        max-width: 680px;
        margin: 0 auto 2.4rem;
    }

    .artefact-stack-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.85rem;
        max-width: 880px;
        margin: 0 auto 4.5rem;
        padding: 0 1rem;
        animation: riseIn 1s ease 0.12s both;
    }

    .stacked-box {
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        font-weight: 600;
        font-size: 0.86rem;
        padding: 0.7rem 1.15rem;
        border-radius: 14px;
        backdrop-filter: blur(18px) saturate(140%);
        -webkit-backdrop-filter: blur(18px) saturate(140%);
        user-select: none;
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        box-shadow:
            inset 0 1px 0 var(--glass-highlight),
            0 10px 24px rgba(0, 0, 0, 0.22);
        transition: transform 0.28s ease, background-color 0.28s ease, border-color 0.28s ease, box-shadow 0.28s ease;
    }

    .box-1 { background: rgba(94, 234, 212, 0.10); border: 1px solid rgba(94, 234, 212, 0.28); color: var(--accent-teal); }
    .box-2 { background: rgba(240, 171, 252, 0.10); border: 1px solid rgba(240, 171, 252, 0.28); color: var(--accent-pink); }
    .box-3 { background: rgba(253, 230, 138, 0.10); border: 1px solid rgba(253, 230, 138, 0.28); color: var(--accent-gold); }
    .box-4 { background: rgba(196, 181, 253, 0.10); border: 1px solid rgba(196, 181, 253, 0.28); color: var(--accent-violet); }

    .stacked-box:hover {
        transform: translateY(-4px);
        box-shadow:
            inset 0 1px 0 var(--glass-highlight),
            0 14px 28px rgba(0, 0, 0, 0.28);
    }

    .box-1:hover { background: rgba(94, 234, 212, 0.18); }
    .box-2:hover { background: rgba(240, 171, 252, 0.18); }
    .box-3:hover { background: rgba(253, 230, 138, 0.18); }
    .box-4:hover { background: rgba(196, 181, 253, 0.18); }

    .fun-chapter-card {
        background: var(--glass-bg);
        backdrop-filter: blur(28px) saturate(160%);
        -webkit-backdrop-filter: blur(28px) saturate(160%);
        border: 1px solid var(--glass-border);
        border-radius: 28px;
        padding: clamp(1.6rem, 4vw, 2.8rem);
        margin: 0 auto 1.6rem;
        max-width: 1050px;
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.12),
            0 18px 40px rgba(0, 0, 0, 0.28);
        animation: riseIn 0.7s ease both;
        transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;
    }

    .fun-chapter-card:nth-of-type(1) { animation-delay: 0.05s; }
    .fun-chapter-card:nth-of-type(2) { animation-delay: 0.1s; }
    .fun-chapter-card:nth-of-type(3) { animation-delay: 0.15s; }
    .fun-chapter-card:nth-of-type(4) { animation-delay: 0.2s; }

    .fun-chapter-card:hover {
        transform: translateY(-3px);
        border-color: rgba(94, 234, 212, 0.28);
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.16),
            0 22px 48px rgba(0, 0, 0, 0.32);
    }

    .card-badge-top {
        display: inline-block;
        background: rgba(255, 255, 255, 0.06);
        color: var(--accent-pink);
        border: 1px solid rgba(240, 171, 252, 0.28);
        padding: 0.35rem 0.95rem;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 1rem;
    }

    .card-main-title {
        font-size: clamp(1.6rem, 3vw, 2.2rem);
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.03em;
        margin-bottom: 0.35rem;
    }

    .card-time-role {
        font-size: 1rem;
        color: var(--accent-teal);
        font-weight: 650;
        margin-bottom: 1.5rem;
    }

    .card-story-text {
        font-size: 1.05rem;
        color: #d5dcea;
        line-height: 1.75;
        margin-bottom: 1.2rem;
    }

    .card-quote-box {
        background: rgba(255, 255, 255, 0.04);
        border-left: 3px solid rgba(240, 171, 252, 0.7);
        padding: 1rem 1.25rem;
        border-radius: 0 14px 14px 0;
        color: var(--accent-gold);
        font-style: italic;
        font-size: 1.08rem;
        margin: 1.4rem 0;
        font-weight: 500;
    }

    .pill-box {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
        margin-top: 1.4rem;
    }

    .fun-pill {
        background: rgba(255, 255, 255, 0.05);
        color: var(--text);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 0.4rem 0.95rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
        transition: background-color 0.25s ease, border-color 0.25s ease, color 0.25s ease;
    }

    .fun-pill:hover {
        background: rgba(94, 234, 212, 0.16);
        border-color: rgba(94, 234, 212, 0.35);
        color: #ecfeff;
    }

    .ai-zone-title {
        font-size: clamp(2rem, 5vw, 3rem);
        font-weight: 800;
        text-align: center;
        margin: 4.5rem 0 0.8rem;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #c4b5fd 0%, #f0abfc 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: riseIn 0.7s ease both;
    }

    .ai-intro-text {
        text-align: center;
        color: var(--muted);
        max-width: 680px;
        margin: 0 auto 2.4rem;
        font-size: 1.08rem;
        line-height: 1.7;
    }

    .ai-cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 1.1rem;
        max-width: 1050px;
        margin: 0 auto;
        padding: 0 0.4rem 3rem;
    }

    .fun-ai-card {
        background: var(--glass-bg);
        backdrop-filter: blur(24px) saturate(160%);
        -webkit-backdrop-filter: blur(24px) saturate(160%);
        border: 1px solid var(--glass-border);
        border-radius: 22px;
        padding: 1.6rem 1.5rem;
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 14px 32px rgba(0, 0, 0, 0.22);
        transition: transform 0.28s ease, border-color 0.28s ease, box-shadow 0.28s ease;
    }

    .fun-ai-card:hover {
        transform: translateY(-4px);
        border-color: rgba(196, 181, 253, 0.38);
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.14),
            0 18px 36px rgba(0, 0, 0, 0.28);
    }

    .ai-card-title {
        font-size: 1.2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.65rem;
        letter-spacing: -0.02em;
    }

    .ai-card-desc {
        font-size: 0.98rem;
        color: var(--muted);
        line-height: 1.65;
        margin-bottom: 1.3rem;
    }

    .ai-card-tech-label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: var(--accent-violet);
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .ai-card-tech {
        color: var(--text);
        font-weight: 600;
        font-size: 0.92rem;
    }

    .site-footer {
        text-align: center;
        color: #7c879c;
        font-size: 0.85rem;
        padding: 1.5rem 1rem 2rem;
    }

    @keyframes riseIn {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @media (prefers-reduced-motion: reduce) {
        .orb, .hero-title, .hero-container, .artefact-stack-container,
        .fun-chapter-card, .ai-zone-title {
            animation: none !important;
        }
        .stacked-box, .fun-chapter-card, .fun-ai-card, .fun-pill {
            transition: none !important;
        }
        .stacked-box:hover, .fun-chapter-card:hover, .fun-ai-card:hover {
            transform: none !important;
        }
    }

    @media (max-width: 640px) {
        .hero-container { padding-top: 2.4rem; }
        .orb { filter: blur(70px); opacity: 0.42; }
    }
    </style>
    """),
    unsafe_allow_html=True,
)

st.markdown(
    textwrap.dedent("""
    <div class="ambient-layer" aria-hidden="true">
        <div class="orb orb-a"></div>
        <div class="orb orb-b"></div>
        <div class="orb orb-c"></div>
    </div>
    <div class="ambient-veil" aria-hidden="true"></div>
    <div class="ambient-grain" aria-hidden="true"></div>
    """),
    unsafe_allow_html=True,
)

st.markdown(
    textwrap.dedent("""
    <div class="hero-container">
        <div class="hero-kicker">TPM · Release · AI tooling</div>
        <div class="hero-title">Orchestrating Enterprise Delivery.</div>
        <div class="hero-subtitle">Steering complex systems with precision. Blending 8+ years of robust Program &amp; Release Management governance with high-energy AI vibe-coding.</div>
    </div>

    <div class="artefact-stack-container">
        <div class="stacked-box box-1">Release_Note_v1.0.pdf</div>
        <div class="stacked-box box-2">Dynamics365_GoLive.pkg</div>
        <div class="stacked-box box-3">PMO_Governance_v2.json</div>
        <div class="stacked-box box-4">Streamlit_App_v4.5.py</div>
    </div>
    """),
    unsafe_allow_html=True,
)

chapters = [
    {
        "badge": "Level 01 • The Foundation",
        "title": "Controlling the Control Room",
        "role": "Release & Deployment Manager | Cognizant",
        "timeline": "March 2016 – December 2018",
        "story": "Every great production is orchestrated from above. Managing high-stakes multi-environment builds and strict Change Advisory Board (CAB) protocols taught me how to keep every operation running smoothly while minimizing risk. I engineered standardized release processes that reduced deployment failures by 40%.",
        "quote": "Absolute control over underlying release mechanics creates total operational freedom.",
        "story_2": "Standardized core rollout playbooks, securing absolute compliance and zero critical post-release incidents across 15+ enterprise clients.",
        "skills": ["CAB Governance", "ServiceNow", "ITIL Framework", "Release Tracking", "Defect Shielding"],
    },
    {
        "badge": "Level 02 • The Orchestrator",
        "title": "Synchronizing Large-Scale Systems",
        "role": "Technical Project Manager | Guidewire Software",
        "timeline": "June 2020 – September 2024",
        "story": "Scaling up meant handling complex multi-tiered enterprise implementations across full SDLC cycles. Pulling the strings between development, QA, and business stakeholders required tuned collaboration, strategic gate management, and disciplined risk assessment. I led Scrum-of-Scrums frameworks for teams spanning 6+ locations.",
        "quote": "Great project management pulls all the right technical threads together into a single rhythm.",
        "story_2": "Through disciplined Scrum-of-Scrums alignment and structured Jira deployment gating, I cut lower-environment downtime by 15% and accelerated delivery cycles.",
        "skills": ["Guidewire InsuranceSuite", "Scrum-of-Scrums", "Jira & Confluence", "Go/No-Go Gates", "RCA Analysis"],
    },
    {
        "badge": "Level 03 • The Architect",
        "title": "Building Custom PMO Frameworks",
        "role": "Senior PMO & Implementation Lead | Folens & Qualtrics",
        "timeline": "October 2024 – January 2026",
        "story": "At this stage, the mission shifted to building brand-new delivery architectures from scratch. Managing $650K ERP rollouts (Dynamics 365) and centralized Coda resource portals meant establishing governance at scale, designing UAT playbooks, and orchestrating cross-functional alignment. I owned the full PMO transformation roadmap.",
        "quote": "A master architect doesn't just manage the pieces; they design how the whole ecosystem moves.",
        "story_2": "Delivered Phase 1 rollouts four weeks ahead of schedule and automated business workflows by 30%, creating reusable playbooks for 3+ future implementations.",
        "skills": ["Dynamics 365", "PMO Architecture", "Coda Portals", "UAT Mastery", "Stakeholder Sync"],
    },
    {
        "badge": "Level 04 • The Sandbox",
        "title": "AI Vibe-Coding & Rapid Innovation",
        "role": "AI Tooling Specialist | Independent R&D",
        "timeline": "February 2026 – Present",
        "story": "Combining 8 years of solid enterprise governance with modern AI-assisted prototyping tools. I build interactive web apps, dashboards and automated tooling to eliminate manual PMO busywork and accelerate delivery. This is where rigor meets rapid iteration, governance meets flow.",
        "quote": "The future belongs to builders who can bridge rigorous governance with rapid, animated execution.",
        "story_2": "Deploying custom Python/Streamlit dashboards, prompt-engineered pipelines, and dynamic micro-apps for enterprise clients seeking modern delivery infrastructure.",
        "skills": ["Vibe Coding", "Streamlit Apps", "MCP Agents", "Python Automation", "LLM Tooling"],
    },
]

for ch in chapters:
    pills_html = "".join([f'<span class="fun-pill">{skill}</span>' for skill in ch["skills"]])
    st.markdown(
        textwrap.dedent(
            f"""
            <div class="fun-chapter-card">
                <div class="card-badge-top">{ch["badge"]}</div>
                <div class="card-main-title">{ch["title"]}</div>
                <div class="card-time-role">{ch["role"]} &nbsp;•&nbsp; {ch["timeline"]}</div>
                <div class="card-story-text">{ch["story"]}</div>
                <div class="card-quote-box">"{ch["quote"]}"</div>
                <div class="card-story-text">{ch["story_2"]}</div>
                <div class="pill-box">{pills_html}</div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

st.markdown(
    textwrap.dedent("""
    <div class="ai-zone-title">AI Vibe-Coding Zone.</div>
    <div class="ai-intro-text">Interactive projects built by combining deep PMO expertise with modern AI tooling. Each piece is engineered to eliminate friction and deliver insight.</div>
    """),
    unsafe_allow_html=True,
)

ai_projects = [
    {
        "title": "Interactive Streamlit Dashboards",
        "desc": "Designed and shipped this high-performance portfolio app featuring custom CSS animations and glassmorphic cards. Built for complex customer onboarding workflows and enterprise toolkit delivery across full project lifecycles.",
        "tech": "Python • Streamlit • Advanced CSS",
    },
    {
        "title": "Automated PMO Governance Bots",
        "desc": "Built smart script assistants utilizing model context protocols to rapidly parse project health metrics, generate executive briefs, and structure governance dashboards for real-time stakeholder visibility.",
        "tech": "MCP Agents • LLM Scripting",
    },
    {
        "title": "Agile Defect Triage Simulators",
        "desc": "Created fast prototype utilities driven by prompt engineering to accelerate lower-environment code validations, automate defect categorization, and track quality gates with AI-assisted insights.",
        "tech": "Prompt Architecture • Automation",
    },
]

cards_html = "".join(
    f"""
    <div class="fun-ai-card">
        <div class="ai-card-title">{proj["title"]}</div>
        <div class="ai-card-desc">{proj["desc"]}</div>
        <div class="ai-card-tech-label">Tech Specs</div>
        <div class="ai-card-tech">{proj["tech"]}</div>
    </div>
    """
    for proj in ai_projects
)

st.markdown(
    textwrap.dedent(
        f"""
        <div class="ai-cards-grid">
            {cards_html}
        </div>
        <div class="site-footer">Gowtham Ganesan · TPM &amp; Release Management</div>
        """
    ),
    unsafe_allow_html=True,
)
