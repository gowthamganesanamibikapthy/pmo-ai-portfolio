import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Gowtham Ganesan | Cinematic Portfolio", page_icon="🍏", layout="wide")

# 2. Cinematic CSS & Apple Scroll-Driven Keyframes
st.markdown("""
    <style>
    /* Global Apple Dark Mode Aesthetics */
    .stApp {
        background-color: #000000;
        color: #f5f5f7;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Hero Section */
    .hero-container {
        padding: 8rem 2rem 4rem 2rem;
        text-align: center;
        max-width: 1000px;
        margin: 0 auto;
    }
    
    .hero-title {
        font-size: 5.5rem;
        font-weight: 700;
        letter-spacing: -0.03em;
        line-height: 1.05;
        background: linear-gradient(180deg, #ffffff 0%, #a1a1a6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.8rem;
        color: #86868b;
        font-weight: 400;
        line-height: 1.4;
        letter-spacing: -0.01em;
    }

    /* Apple-Style Cinematic Story Chapters */
    .story-chapter {
        background: rgba(28, 28, 30, 0.6);
        backdrop-filter: blur(40px);
        -webkit-backdrop-filter: blur(40px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 36px;
        padding: 4.5rem;
        margin: 0 auto 8rem auto;
        max-width: 1100px;
        box-shadow: 0 30px 60px rgba(0,0,0,0.6);
        
        /* Native Browser Scroll-Driven Animations */
        opacity: 0;
        transform: translateY(100px) scale(0.94);
        animation: appleCinematicReveal linear forwards;
        animation-timeline: view();
        animation-range: entry 5% cover 30%;
    }
    
    @keyframes appleCinematicReveal {
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    .chapter-eyebrow {
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #2997ff;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .chapter-title {
        font-size: 2.8rem;
        font-weight: 600;
        color: #f5f5f7;
        letter-spacing: -0.02em;
        margin-bottom: 0.5rem;
    }

    .chapter-timeline {
        font-size: 1.15rem;
        color: #86868b;
        font-weight: 500;
        margin-bottom: 3rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 1.5rem;
    }

    /* Immersive Story Paragraphs */
    .story-prose {
        font-size: 1.25rem;
        color: #d2d2d7;
        line-height: 1.8;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    .story-prose strong {
        color: #ffffff;
        font-weight: 600;
    }

    /* Highlight Pull-Quotes */
    .story-quote {
        font-size: 1.4rem;
        color: #2997ff;
        font-style: italic;
        border-left: 3px solid #2997ff;
        padding-left: 1.5rem;
        margin: 2.5rem 0;
        line-height: 1.5;
    }

    /* Skill Badge Grid */
    .badge-wrap {
        display: flex;
        flex-wrap: wrap;
        gap: 0.75rem;
        margin-top: 2.5rem;
    }
    
    .apple-pill {
        background: rgba(255, 255, 255, 0.05);
        color: #f5f5f7;
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 0.6rem 1.4rem;
        border-radius: 30px;
        font-size: 0.95rem;
        font-weight: 500;
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
    }
    
    .apple-pill:hover {
        background: rgba(41, 151, 255, 0.15);
        border-color: rgba(41, 151, 255, 0.4);
        color: #2997ff;
        transform: translateY(-3px);
    }

    /* AI Vibe Coding Grid Section */
    .ai-section-title {
        font-size: 4rem;
        font-weight: 700;
        text-align: center;
        margin: 8rem 0 1.5rem 0;
        letter-spacing: -0.02em;
        background: linear-gradient(180deg, #fff 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .ai-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2.5rem;
        max-width: 1100px;
        margin: 0 auto;
    }

    .ai-card {
        background: linear-gradient(145deg, rgba(28,28,30,0.7) 0%, rgba(15,15,18,0.9) 100%);
        border: 1px solid rgba(168, 85, 247, 0.25);
        border-radius: 30px;
        padding: 3rem;
        transition: all 0.4s ease;
    }
    
    .ai-card:hover {
        transform: translateY(-8px);
        border-color: rgba(168, 85, 247, 0.8);
        box-shadow: 0 20px 40px rgba(168, 85, 247, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">The Evolution of Delivery.</div>
        <div class="hero-subtitle">An immersive, cinematic journey through 8+ years of engineering enterprise scale, program governance, and AI-driven automation.</div>
    </div>
""", unsafe_allow_html=True)

# 4. Cinematic Story Chapters Data
chapters = [
    {
        "eyebrow": "Chapter 01 • The Genesis",
        "title": "The Foundation of Discipline",
        "role": "Release & Deployment Manager | Cognizant",
        "timeline": "March 2016 – December 2018",
        "prose_1": "My career started in the engine room of enterprise IT operations. Managing high-stakes multi-environment builds and strict Change Advisory Board (CAB) workflows across ServiceNow taught me a foundational truth: <strong>zero-incident releases are never a matter of luck</strong>—they are the direct byproduct of ruthless procedural discipline.",
        "quote": "Standardizing deployment playbooks taught me that rigid processes create the freedom to scale securely.",
        "prose_2": "By authoring comprehensive release implementation guides and orchestrating rigorous pre-deployment validations, I gained the operational rigor needed to eliminate critical post-implementation downtime entirely, setting the stage for larger enterprise responsibilities.",
        "skills": ["CAB Governance", "ServiceNow", "ITIL Framework", "Environment Management", "Defect Triaging"]
    },
    {
        "eyebrow": "Chapter 02 • The Orchestrator",
        "title": "Synchronizing Chaos at Scale",
        "role": "Technical Project Manager | Guidewire Software",
        "timeline": "June 2020 – September 2024",
        "prose_1": "Stepping into enterprise InsuranceSuite implementations meant zooming out from individual release windows to manage the entire Software Development Life Cycle (SDLC). Cross-functional friction between development, QA, and business workstreams was constant—and solving it required structural harmonization.",
        "quote": "True program management isn't just tracking tasks; it's aligning human intent across complex technical dependencies.",
        "prose_2": "By facilitating Scrum-of-Scrums and embedding structured deployment checklists directly into Jira, I learned how to transform chaotic cross-team dependencies into predictable release trains. This systemic alignment successfully drove down lower-environment downtime by 15%.",
        "skills": ["Guidewire InsuranceSuite", "Scrum-of-Scrums", "Jira & Confluence", "Go/No-Go Gates", "Root Cause Analysis"]
    },
    {
        "eyebrow": "Chapter 03 • The Architect",
        "title": "Engineering Frameworks from Scratch",
        "role": "Senior PMO & Implementation Lead | Folens & Qualtrics",
        "timeline": "October 2024 – January 2026",
        "prose_1": "With delivery mechanics mastered, the frontier shifted to architectural design. At Folens and Qualtrics, I was tasked with engineering centralized PMO frameworks from the ground up—balancing strict Out-of-the-Box SaaS configurations with custom ERP solutions like Microsoft Dynamics 365 Business Central.",
        "quote": "Building custom PMO frameworks transformed how executives view delivery: shifting it from a reactive cost center to a predictive engine.",
        "prose_2": "By optimizing milestone execution and driving centralized documentation portals via Coda, I led Phase 1 rollouts for 80+ users four weeks ahead of schedule while achieving a 30% boost in overall business process automation.",
        "skills": ["Dynamics 365", "PMO Architecture", "Coda", "UAT Orchestration", "Stakeholder Alignment"]
    },
    {
        "eyebrow": "Chapter 04 • The Horizon",
        "title": "AI-Powered Program Management",
        "role": "AI Tooling Specialist & Vibe Coder | Independent R&D",
        "timeline": "February 2026 – Present",
        "prose_1": "The modern PMO cannot run on spreadsheets and manual status reports alone. Today, I combine my 8 years of foundational delivery governance with advanced AI vibe-coding and natural language prompt architecture.",
        "quote": "The future belongs to builders who can bridge rigorous enterprise governance with rapid AI prototyping.",
        "prose_2": "By designing custom Streamlit web dashboards, experimenting with Model Context Protocol (MCP) servers, and deploying autonomous LLM agents, I eliminate manual PMO reporting overhead in real time.",
        "skills": ["Vibe Coding", "Streamlit Dev", "MCP Agents", "Python Automation", "LLM Integration"]
    }
]

# Render Cinematic Chapters
for ch in chapters:
    badges_html = "".join([f'<span class="apple-pill">{skill}</span>' for skill in ch["skills"]])
    
    st.markdown(f"""
    <div class="story-chapter">
        <div class="chapter-eyebrow">{ch["eyebrow"]}</div>
        <div class="chapter-title">{ch["title"]}</div>
        <div class="chapter-timeline">{ch["role"]} &nbsp;|&nbsp; {ch["timeline"]}</div>
        
        <div class="story-prose">{ch["prose_1"]}</div>
        
        <div class="story-quote">"{ch["quote"]}"</div>
        
        <div class="story-prose">{ch["prose_2"]}</div>
        
        <div class="badge-wrap">
            {badges_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# 5. AI & Vibe Coding Showcase Section
st.markdown('<div class="ai-section-title">Applied AI & Vibe Coding.</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #86868b; max-width: 750px; margin: 0 auto 5rem auto; font-size: 1.3rem; line-height: 1.5;">Showcasing active applications built by merging enterprise delivery experience with cutting-edge AI prototyping workflows.</p>', unsafe_allow_html=True)

ai_projects = [
    {
        "title": "Interactive Streamlit Portfolios",
        "desc": "Engineered this very web application using Python and Streamlit, featuring custom CSS keyframe animations, glassmorphism design layouts, and dynamic state transitions.",
        "tech": "Python • Streamlit • CSS3"
    },
    {
        "title": "Automated PMO Governance Agents",
        "desc": "Built workflow helpers using Model Context Protocol (MCP) to instantly parse raw project metrics, log defects, and auto-generate executive status report documents.",
        "tech": "MCP Servers • LLMs • Automation"
    },
    {
        "title": "Agile Defect Triage Simulators",
        "desc": "Created localized prototype tools leveraging prompt engineering to streamline root-cause analysis reporting and accelerate lower-environment release validation.",
        "tech": "Prompt Engineering • Python Scripting"
    }
]

st.markdown('<div class="ai-grid">', unsafe_allow_html=True)
for proj in ai_projects:
    st.markdown(f"""
    <div class="ai-card">
        <div style="font-size: 1.6rem; font-weight: 600; color: #ffffff; margin-bottom: 1rem;">{proj["title"]}</div>
        <div style="font-size: 1.1rem; color: #94a3b8; line-height: 1.6; margin-bottom: 2rem;">{proj["desc"]}</div>
        <div style="font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; color: #a855f7; font-weight: 600; margin-bottom: 0.5rem;">Tech Stack</div>
        <div style="color: #f5f5f7; font-weight: 500; font-size: 1rem;">{proj["tech"]}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer Spacing
st.markdown('<div style="height: 180px;"></div>', unsafe_allow_html=True)