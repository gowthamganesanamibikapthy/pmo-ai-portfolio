import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Gowtham Ganesan | Day One Portfolio", 
    page_icon="⚡", 
    layout="wide"
)

# 2. Sidebar Feature Toggle for Release Control
st.sidebar.markdown("### 🎛️ Release Control Center")
enable_cinematic = st.sidebar.toggle("✨ Cinematic & Playful Mode", value=True)
st.sidebar.markdown("---")
st.sidebar.info("Flip this toggle to switch between the high-energy cinematic release view and a clean executive layout for your first day.")

if enable_cinematic:
    # ==========================================
    # CINEMATIC / PLAYFUL MODE (ACTIVE)
    # ==========================================
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        .stApp {
            background-color: #060608;
            color: #f8fafc;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
        }
        
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* MASTER ORCHESTRATOR BADGE */
        .master-conductor-badge {
            position: fixed;
            top: 25px;
            right: 30px;
            background: rgba(20, 20, 30, 0.85);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(244, 114, 182, 0.4);
            padding: 0.6rem 1.2rem;
            border-radius: 50px;
            z-index: 9999;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            animation: badgeFloat 3s ease-in-out infinite alternate;
        }
        
        @keyframes badgeFloat {
            0% { transform: translateY(0px); }
            100% { transform: translateY(-4px); }
        }
        
        .conductor-text {
            font-size: 0.85rem;
            font-weight: 700;
            color: #f472b6;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        /* BACKGROUND DRIFTING ARTIFACTS */
        @keyframes subtleDrift {
            0% { transform: translateY(-30px) rotate(0deg); opacity: 0.2; }
            50% { opacity: 0.5; }
            100% { transform: translateY(105vh) rotate(180deg); opacity: 0.2; }
        }

        .drift-item {
            position: fixed;
            pointer-events: none;
            z-index: 1;
            font-family: monospace;
            font-size: 0.8rem;
            padding: 0.4rem 0.8rem;
            border-radius: 8px;
            backdrop-filter: blur(4px);
            animation: subtleDrift linear infinite;
        }
        .d-1 { top: -10%; left: 5%; background: rgba(78, 205, 196, 0.08); border: 1px solid rgba(78,205,196,0.2); color: #4ECDC4; animation-duration: 14s; animation-delay: 0s; }
        .d-2 { top: -10%; left: 82%; background: rgba(244, 114, 182, 0.08); border: 1px solid rgba(244,114,182,0.2); color: #f472b6; animation-duration: 18s; animation-delay: 4s; }
        .d-3 { top: -10%; left: 15%; background: rgba(255, 230, 109, 0.08); border: 1px solid rgba(255,230,109,0.2); color: #FFE66D; animation-duration: 12s; animation-delay: 7s; }

        /* HERO SECTION */
        .hero-box {
            padding: 8rem 1rem 4rem 1rem;
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }
        
        .hero-main-title {
            font-size: 4.2rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            line-height: 1.1;
            background: linear-gradient(135deg, #FFFFFF 0%, #94a3b8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1.2rem;
        }
        
        .hero-desc {
            font-size: 1.35rem;
            color: #94a3b8;
            font-weight: 400;
            line-height: 1.6;
            max-width: 750px;
            margin: 0 auto;
        }

        /* CHAPTER CARDS */
        .chapter-card {
            background: rgba(18, 18, 24, 0.85);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 32px;
            padding: 3.5rem;
            margin: 0 auto 4.5rem auto;
            max-width: 1000px;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
            position: relative;
            z-index: 2;
            transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
            
            opacity: 0;
            transform: translateY(60px) scale(0.97);
            animation: cardReveal linear forwards;
            animation-timeline: view();
            animation-range: entry 5% cover 30%;
        }
        
        .chapter-card:hover {
            border-color: rgba(244, 114, 182, 0.4);
            transform: translateY(-5px) scale(1);
            box-shadow: 0 30px 80px rgba(244, 114, 182, 0.15);
        }

        @keyframes cardReveal {
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        .chapter-eyebrow {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #f472b6;
            font-weight: 700;
            margin-bottom: 1rem;
        }

        .chapter-heading {
            font-size: 2.4rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.3rem;
            letter-spacing: -0.02em;
        }

        .chapter-submeta {
            font-size: 1.1rem;
            color: #4ECDC4;
            font-weight: 600;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        .story-paragraph {
            font-size: 1.15rem;
            color: #cbd5e1;
            line-height: 1.8;
            margin-bottom: 1.5rem;
            font-weight: 400;
        }

        .quote-box {
            background: rgba(244, 114, 182, 0.04);
            border-left: 3px solid #f472b6;
            padding: 1.2rem 1.5rem;
            border-radius: 0 14px 14px 0;
            color: #FFE66D;
            font-style: italic;
            font-size: 1.15rem;
            margin: 2rem 0;
            font-weight: 500;
        }

        .skills-wrapper {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-top: 2rem;
        }

        .skill-chip {
            background: rgba(255, 255, 255, 0.04);
            color: #f8fafc;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 0.5rem 1.1rem;
            border-radius: 30px;
            font-size: 0.9rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .skill-chip:hover {
            background: #f472b6;
            color: #060608;
            border-color: #f472b6;
            transform: translateY(-2px);
        }

        /* AI ZONE */
        .ai-zone-header {
            font-size: 3.2rem;
            font-weight: 800;
            text-align: center;
            margin: 7rem 0 1rem 0;
            background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            z-index: 2;
        }

        .ai-grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1000px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }

        .ai-card-item {
            background: linear-gradient(145deg, rgba(18,18,24,0.9) 0%, rgba(10,10,15,0.98) 100%);
            border: 1px solid rgba(168, 85, 247, 0.25);
            border-radius: 24px;
            padding: 2.5rem;
            transition: all 0.4s ease;
        }

        .ai-card-item:hover {
            transform: translateY(-6px);
            border-color: #a855f7;
            box-shadow: 0 20px 40px rgba(168, 85, 247, 0.2);
        }
        </style>

        <div class="master-conductor-badge">
            <span>🧵✨</span>
            <span class="conductor-text">Gowtham | Day One Showcase</span>
        </div>
        
        <div class="drift-item d-1">📄 Release_v2.4.pkg</div>
        <div class="drift-item d-2">🚀 ERP_GoLive_Pipeline</div>
        <div class="drift-item d-3">💡 PMO_Governance_Agent</div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="hero-box">
            <div class="hero-main-title">Pulling Strings of Enterprise Delivery.</div>
            <div class="hero-desc">Steering Complex system from bottom-up with total procedural rigor, precision and efficiency. By blending 8+ years of project, program & release management experience with high energy AI vibe-coding.</div>
        </div>
    """, unsafe_allow_html=True)

    career_chapters = [
        {
            "eyebrow": "Chapter 01 • The Foundation",
            "title": "Mastering the Release Control Room",
            "role": "Release & Deployment Manager | Cognizant",
            "timeline": "March 2016 – December 2018",
            "story": "Every robust platform begins with strict foundational governance. Managing high-stakes multi-environment builds and rigorous Change Advisory Board (CAB) protocols taught me how to keep every operational dependency tightly controlled to guarantee zero production downtime.",
            "quote": "Absolute control over underlying release mechanisms builds the foundation for secure enterprise scale.",
            "story_two": "By standardizing core deployment guides and enforcing pre-release validations, I eliminated critical post-implementation incidents and secured absolute release compliance.",
            "skills": ["CAB Governance", "ServiceNow", "ITIL Framework", "Release Tracking", "Defect Shielding"]
        },
        {
            "eyebrow": "Chapter 02 • The Orchestrator",
            "title": "Synchronizing Large-Scale Systems",
            "role": "Technical Project Manager | Guidewire Software",
            "timeline": "June 2020 – September 2024",
            "story": "Stepping into enterprise InsuranceSuite ecosystems required managing the full SDLC across distributed teams. Bridging operational gaps between development, QA, and business stakeholders meant turning complex technical dependencies into predictable release cadences.",
            "quote": "True project management pulls all moving technical threads together into a single synchronized rhythm.",
            "story_two": "Through structured Scrum-of-Scrums alignment and rigorous Jira gatekeeping, I successfully reduced lower-environment downtime by 15%.",
            "skills": ["Guidewire InsuranceSuite", "Scrum-of-Scrums", "Jira & Confluence", "Go/No-Go Gates", "Root Cause Analysis"]
        },
        {
            "eyebrow": "Chapter 03 • The Architect",
            "title": "Building Custom PMO Frameworks",
            "role": "Senior PMO & Implementation Lead | Folens & Qualtrics",
            "timeline": "October 2024 – January 2026",
            "story": "At this stage, the mission evolved into architecting centralized delivery frameworks from scratch. Directing complex ERP rollouts (Dynamics 365) and unified resource hubs via Coda meant designing systems that empower both end-users and executive stakeholders.",
            "quote": "A master architect doesn't just manage tasks; they engineer how the entire enterprise workflow moves.",
            "story_two": "Delivered Phase 1 SaaS rollouts four weeks ahead of schedule while increasing business process automation by 30%.",
            "skills": ["Dynamics 365", "PMO Architecture", "Coda Portals", "UAT Mastery", "Stakeholder Sync"]
        },
        {
            "eyebrow": "Chapter 04 • The Horizon",
            "title": "AI Vibe-Coding & Rapid Prototyping",
            "role": "AI Tooling Specialist & Builder | Independent R&D",
            "timeline": "February 2026 – Present",
            "story": "Combining 8 years of rigorous enterprise delivery governance with cutting-edge AI coding workflows. I build modern web applications and automated utilities to eliminate manual PMO reporting bottlenecks instantly.",
            "quote": "The future belongs to builders who can bridge rigorous operational control with rapid AI execution.",
            "story_two": "Deploying custom Python/Streamlit web apps, prompt-engineered pipeline agents, and dynamic workflow micro-tools.",
            "skills": ["Vibe Coding", "Streamlit Apps", "MCP Agents", "Python Automation", "LLM Tooling"]
        }
    ]

    for ch in career_chapters:
        chips_html = "".join([f'<span class="skill-chip">{s}</span>' for s in ch["skills"]])
        st.markdown(f"""
        <div class="chapter-card">
            <div class="chapter-eyebrow">{ch["eyebrow"]}</div>
            <div class="chapter-heading">{ch["title"]}</div>
            <div class="chapter-submeta">{ch["role"]} &nbsp;•&nbsp; {ch["timeline"]}</div>
            <div class="story-paragraph">{ch["story"]}</div>
            <div class="quote-box">"{ch["quote"]}"</div>
            <div class="story-paragraph">{ch["story_two"]}</div>
            <div class="skills-wrapper">{chips_html}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="ai-zone-header">AI Vibe-Coding Zone.</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #94a3b8; max-width: 700px; margin: 0 auto 4rem auto; font-size: 1.2rem; position: relative; z-index: 2;">Showcasing active applications built by combining deep program management experience with fast, modern AI prototyping tools.</p>', unsafe_allow_html=True)

    ai_showcase_projects = [
        {
            "title": "Interactive Streamlit Portfolios",
            "desc": "Engineered this high-performance web app featuring custom CSS layout physics, dynamic glassmorphic depth, and scroll-driven animations.",
            "tech": "Python • Streamlit • CSS3"
        },
        {
            "title": "Automated PMO Governance Agents",
            "desc": "Built smart script assistants utilizing model context protocols (MCP) to instantly parse project metrics and structure executive status summaries.",
            "tech": "MCP Servers • LLM Scripting"
        },
        {
            "title": "Agile Defect Triage Simulators",
            "desc": "Created fast prototype utilities driven by prompt engineering to streamline root-cause analysis tracking and lower-environment testing.",
            "tech": "Prompt Architecture • Python"
        }
    ]

    st.markdown('<div class="ai-grid-container">', unsafe_allow_html=True)
    for proj in ai_showcase_projects:
        st.markdown(f"""
        <div class="ai-card-item">
            <div style="font-size: 1.4rem; font-weight: 700; color: #ffffff; margin-bottom: 0.8rem;">{proj["title"]}</div>
            <div style="font-size: 1.02rem; color: #94a3b8; line-height: 1.6; margin-bottom: 2rem;">{proj["desc"]}</div>
            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; color: #a855f7; font-weight: 700; margin-bottom: 0.4rem;">Tech Specs</div>
            <div style="color: #f8fafc; font-weight: 600; font-size: 0.95rem;">{proj["tech"]}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height: 180px;"></div>', unsafe_allow_html=True)

else:
    # ==========================================
    # EXECUTIVE CLASSIC MODE (FALLBACK)
    # ==========================================
    st.markdown("""
        <div style="padding: 4rem 1rem 2rem 1rem; max-width: 900px; margin: 0 auto;">
            <h1 style="font-size: 3rem; font-weight: 800; color: #ffffff; margin-bottom: 0.5rem;">Gowtham Ganesan</h1>
            <h3 style="font-size: 1.4rem; color: #38bdf8; font-weight: 600; margin-bottom: 2rem;">Technical Program & Release Management Leader</h3>
            <p style="font-size: 1.15rem; color: #94a3b8; line-height: 1.6;">
                Executive portfolio view optimized for corporate review, structured governance analysis, and standard evaluation metrics.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Core Professional Summary")
    st.write("8+ years of expertise spanning enterprise SaaS implementations, rigorous PMO framework design, ITIL release governance, and AI-driven workflow automation across Cognizant, Guidewire, Folens, and Qualtrics.")
    
    st.subheader("Active Roles & Milestones")
    st.markdown("""
    * **Senior PMO & Implementation Lead | Folens & Qualtrics (2024–2026):** Managed $650K ERP rollouts and custom Coda portals, driving a 30% increase in process automation.
    * **Technical Project Manager | Guidewire Software (2020–2024):** Orchestrated enterprise InsuranceSuite SDLC builds, cutting lower-environment downtime by 15% through Scrum-of-Scrums harmonization.
    * **Release & Deployment Manager | Cognizant (2016–2018):** Enforced CAB governance and multi-environment build discipline to eliminate critical post-deployment incidents entirely.
    """)
    
    st.subheader("AI Vibe-Coding Initiatives")
    st.markdown("""
    * Building custom Python/Streamlit dashboards for automated metrics tracking.
    * Experimenting with Model Context Protocol (MCP) servers for autonomous defect triage assistance.
    """)