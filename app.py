import streamlit as st
import textwrap

st.set_page_config(
    page_title="Gowtham Ganesan | Executive Portfolio & Hub",
    page_icon="⚡",
    layout="wide"
)

# Advanced CSS with High-End Special Effects & Animations
st.markdown(textwrap.dedent("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% 10%, #111019 0%, #030305 100%);
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
        overflow-x: hidden;
    }
    
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .ambient-glow-1 {
        position: fixed;
        top: 10%;
        left: 15%;
        width: 400px;
        height: 400px;
        background: rgba(168, 85, 247, 0.08);
        filter: blur(120px);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
        animation: orbFloat 10s ease-in-out infinite alternate;
    }

    .ambient-glow-2 {
        position: fixed;
        bottom: 10%;
        right: 15%;
        width: 450px;
        height: 450px;
        background: rgba(78, 205, 196, 0.06);
        filter: blur(140px);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
        animation: orbFloat 14s ease-in-out infinite alternate-reverse;
    }

    @keyframes orbFloat {
        0% { transform: translateY(0px) scale(1); }
        100% { transform: translateY(-30px) scale(1.1); }
    }

    .master-glass-shell {
        background: rgba(14, 14, 22, 0.75);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 36px;
        padding: 3.5rem 3rem;
        max-width: 1200px;
        margin: 2rem auto;
        box-shadow: 0 30px 100px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        position: relative;
        z-index: 1;
    }

    .profile-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 2rem;
        margin-bottom: 3rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        padding-bottom: 2.5rem;
    }
    
    .name-title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -0.03em;
    }

    .linkedin-badge {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.2) 0%, rgba(56, 189, 248, 0.1) 100%);
        border: 1px solid rgba(56, 189, 248, 0.4);
        color: #38bdf8;
        padding: 0.75rem 1.8rem;
        border-radius: 50px;
        font-weight: 700;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 25px rgba(14, 165, 233, 0.2);
    }
    
    .linkedin-badge:hover {
        background: #0ea5e9;
        color: #ffffff;
        box-shadow: 0 15px 35px rgba(14, 165, 233, 0.4);
        transform: translateY(-3px);
    }

    .release-cloud {
        background: linear-gradient(135deg, rgba(20, 20, 32, 0.8) 0%, rgba(10, 10, 18, 0.95) 100%);
        border: 1px solid rgba(78, 205, 196, 0.3);
        border-radius: 28px;
        padding: 2.5rem;
        margin-bottom: 3rem;
        position: relative;
    }

    .cloud-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #4ECDC4;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 1.5rem;
    }

    .artifact-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .artifact-pill {
        background: rgba(78, 205, 196, 0.08);
        border: 1px solid rgba(78, 205, 196, 0.3);
        color: #4ECDC4;
        padding: 0.6rem 1.2rem;
        border-radius: 14px;
        font-family: monospace;
        font-size: 0.92rem;
        font-weight: 600;
    }

    .dark-skill-cloud {
        background: linear-gradient(135deg, rgba(12, 8, 20, 0.95) 0%, rgba(4, 4, 10, 0.99) 100%);
        border: 1px solid rgba(168, 85, 247, 0.4);
        border-radius: 32px;
        padding: 3.5rem;
        margin-bottom: 4rem;
    }

    .dark-cloud-title {
        font-size: 1.6rem;
        font-weight: 800;
        color: #e9d5ff;
        margin-bottom: 2rem;
    }

    .skill-pillars-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
    }

    .skill-pillar-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(168, 85, 247, 0.2);
        border-radius: 24px;
        padding: 2.5rem;
    }

    .pillar-name {
        font-size: 1.25rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1rem;
    }

    .pillar-desc {
        font-size: 0.98rem;
        color: #94a3b8;
        line-height: 1.7;
    }

    .chapter-box {
        background: rgba(18, 18, 28, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 28px;
        padding: 3rem;
        margin-bottom: 2.5rem;
    }

    .chapter-badge {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #f472b6;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .chapter-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.4rem;
    }

    .chapter-role {
        font-size: 1.1rem;
        color: #38bdf8;
        font-weight: 600;
        margin-bottom: 1.8rem;
    }

    .chapter-text {
        font-size: 1.05rem;
        color: #cbd5e1;
        line-height: 1.8;
    }
    </style>

    <div class="ambient-glow-1"></div>
    <div class="ambient-glow-2"></div>
"""), unsafe_allow_html=True)

tab_portfolio, tab_codebase = st.tabs(["✨ Cinematic Portfolio & Journey", "💻 Codebase & GitHub Hub"])

with tab_portfolio:
    st.markdown(textwrap.dedent("""
    <div class="master-glass-shell">
        <div class="profile-header">
            <div>
                <h1 class="name-title">Gowtham Ganesan</h1>
                <p style="color: #94a3b8; font-size: 1.25rem; margin-top: 0.5rem; font-weight: 500;">
                    Master Orchestrator | Technical Program & Release Management Leader | AI Vibe-Coder
                </p>
            </div>
            <div>
                <a href="https://www.linkedin.com/in/gowtham-ganesan" target="_blank" class="linkedin-badge">
                    <span>🔗 Connect on LinkedIn</span>
                </a>
            </div>
        </div>

        <div class="release-cloud">
            <div class="cloud-title">☁️ Active Software Release Atmosphere</div>
            <div class="artifact-grid">
                <span class="artifact-pill">📄 Release_Note_v1.0.pdf</span>
                <span class="artifact-pill">🚀 Dynamics365_GoLive.pkg</span>
                <span class="artifact-pill">💡 PMO_Governance_v2.json</span>
                <span class="artifact-pill">⚡ Streamlit_App_v4.5.py</span>
                <span class="artifact-pill">🛡️ CAB_Change_Advisory.log</span>
            </div>
        </div>

        <div class="dark-skill-cloud">
            <div class="dark-cloud-title">🌩️ Core Expertise Matrix</div>
            <div class="skill-pillars-grid">
                <div class="skill-pillar-card">
                    <div class="pillar-name">01. Enterprise Release Governance</div>
                    <div class="pillar-desc">Mastery over high-stakes multi-environment deployments, strict CAB protocols, ITIL frameworks, and risk mitigation to ensure absolute zero-downtime production releases.</div>
                </div>
                <div class="skill-pillar-card">
                    <div class="pillar-name">02. Large-Scale Systems Orchestration</div>
                    <div class="pillar-desc">Deep leadership across Guidewire InsuranceSuite and Dynamics 365 ERP implementations, aligning complex multi-tiered SDLC cycles and cross-functional engineering teams.</div>
                </div>
                <div class="skill-pillar-card">
                    <div class="pillar-name">03. AI Vibe-Coding & Tooling</div>
                    <div class="pillar-desc">Rapid prototyping of smart web applications, custom Python micro-apps, and model context protocol (MCP) agents to fully automate legacy PMO busywork.</div>
                </div>
            </div>
        </div>

        <div>
            <h2 style="font-size: 2.5rem; font-weight: 800; color: #ffffff; margin-bottom: 2.5rem; text-align: center;">Career Evolution Chapters</h2>
            
            <div class="chapter-box">
                <div class="chapter-badge">Chapter 01 • The Foundation</div>
                <div class="chapter-title">Mastering the Control Room</div>
                <div class="chapter-role">Release & Deployment Manager | Cognizant (March 2016 – December 2018)</div>
                <div class="chapter-text">Governing high-stakes deployment schedules and strict Change Advisory Board protocols, establishing foundational reliability through bulletproof procedural workflows.</div>
            </div>

            <div class="chapter-box">
                <div class="chapter-badge">Chapter 02 • The Orchestrator</div>
                <div class="chapter-title">Synchronizing Large-Scale Systems</div>
                <div class="chapter-role">Technical Project Manager | Guidewire Software (June 2020 – September 2024)</div>
                <div class="chapter-text">Steering multi-tiered enterprise implementations across full SDLC cycles, turning chaotic cross-team dependencies into smooth release cadences and cutting lower-environment downtime by 15%.</div>
            </div>

            <div class="chapter-box">
                <div class="chapter-badge">Chapter 03 • The Architect</div>
                <div class="chapter-title">Building Custom PMO Frameworks</div>
                <div class="chapter-role">Senior PMO & Implementation Lead | Folens & Qualtrics (October 2024 – January 2026)</div>
                <div class="chapter-text">Architecting centralized delivery frameworks from scratch, managing $650K ERP rollouts (Dynamics 365) and unified resource portals that accelerate business automation by 30%.</div>
            </div>

            <div class="chapter-box">
                <div class="chapter-badge">Chapter 04 • The Sandbox</div>
                <div class="chapter-title">AI Vibe-Coding & Rapid Innovation</div>
                <div class="chapter-role">AI Tooling Specialist | Independent R&D (February 2026 – Present)</div>
                <div class="chapter-text">Merging 8 years of enterprise governance with modern AI-assisted prototyping tools to build interactive web apps and automated tooling.</div>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

with tab_codebase:
    st.markdown(textwrap.dedent("""
    <div class="master-glass-shell">
        <h1 style="font-size: 3rem; font-weight: 800; color: #ffffff; margin-bottom: 1.2rem;">Codebase & GitHub Projects Hub</h1>
        <p style="color: #94a3b8; font-size: 1.25rem; margin-bottom: 3.5rem; line-height: 1.6;">
            Explore the underlying source code architecture, repositories, and automated utility scripts that power this portfolio ecosystem.
        </p>

        <div class="skill-pillars-grid" style="margin-bottom: 3.5rem;">
            <div class="skill-pillar-card">
                <div class="pillar-name">📂 Portfolio Repository</div>
                <div class="pillar-desc">The complete Streamlit application source code featuring custom CSS physics, glassmorphic containers, and interactive tabs.</div>
                <div style="margin-top: 1.8rem;">
                    <a href="https://github.com" target="_blank" class="linkedin-badge" style="font-size: 0.9rem; padding: 0.5rem 1.2rem;">View GitHub Repo</a>
                </div>
            </div>
            <div class="skill-pillar-card">
                <div class="pillar-name">⚡ AI Vibe-Coding Scripts</div>
                <div class="pillar-desc">Python utility scripts and automation pipelines designed for PMO metrics tracking and protocol management.</div>
                <div style="margin-top: 1.8rem;">
                    <a href="https://github.com" target="_blank" class="linkedin-badge" style="font-size: 0.9rem; padding: 0.5rem 1.2rem;">Explore Scripts</a>
                </div>
            </div>
            <div class="skill-pillar-card">
                <div class="pillar-name">🛡️ MCP Governance Tools</div>
                <div class="pillar-desc">Experimental model context protocol servers built to parse and evaluate live project health metrics securely.</div>
                <div style="margin-top: 1.8rem;">
                    <a href="https://github.com" target="_blank" class="linkedin-badge" style="font-size: 0.9rem; padding: 0.5rem 1.2rem;">Check MCP Hub</a>
                </div>
            </div>
        </div>

        <div style="background: rgba(18, 18, 28, 0.7); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 24px; padding: 3rem;">
            <h3 style="color: #ffffff; font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem;">Branch Architecture Status</h3>
            <p style="color: #94a3b8; font-size: 1.1rem; line-height: 1.6;">
                This enhanced iteration is isolated within your custom working branch, keeping your core production environment secure while offering maximum visual sophistication and high-end animation physics for your showcase.
            </p>
        </div>
    </div>
    """), unsafe_allow_html=True)