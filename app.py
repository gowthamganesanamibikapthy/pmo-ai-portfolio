import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Gowtham Ganesan |  TPM & RM Portfolio", page_icon="🧶", layout="wide")

# 2. Playful Custom CSS, Puppet-String Pull Physics & Falling Software Artefacts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap');

    .stApp {
        background-color: #08080a;
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
        overflow-x: hidden;
    }
    
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* PUPPET STRINGS & PERSON OF COLOR SYMBOLISM FIXED TO TOP */
    .puppet-master-rig {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 999;
        overflow: hidden;
    }

    /* Vertical Control Strings coming down from above */
    .string-line {
        position: absolute;
        top: 0;
        width: 2px;
        background: linear-gradient(180deg, rgba(244, 114, 182, 0.8) 0%, rgba(78, 205, 196, 0.4) 60%, transparent 100%);
        height: 100vh;
        animation: stringPullEffect 4s ease-in-out infinite alternate;
    }
    .string-1 { left: 15%; animation-delay: 0s; }
    .string-2 { left: 50%; animation-delay: 1.2s; width: 3px; background: linear-gradient(180deg, rgba(168, 85, 247, 0.9) 0%, rgba(255, 230, 109, 0.3) 70%, transparent 100%); }
    .string-3 { left: 85%; animation-delay: 2.4s; }

    @keyframes stringPullEffect {
        0% { transform: scaleY(0.97) translateY(-5px); }
        100% { transform: scaleY(1.03) translateY(5px); }
    }

    /* Puppet Master Silhouette / Hands from Above Symbolizing POC Leadership & Orchestration */
    .puppeteer-silhouette {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 320px;
        height: 110px;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.25) 0%, rgba(244, 114, 182, 0.08) 50%, transparent 80%);
        border-bottom-left-radius: 160px;
        border-bottom-right-radius: 160px;
        display: flex;
        justify-content: center;
        align-items: flex-end;
        padding-bottom: 10px;
        border-bottom: 2px dashed rgba(244, 114, 182, 0.4);
    }
    .puppeteer-hands-icon {
        font-size: 1.8rem;
        animation: handsTug 2s ease-in-out infinite alternate;
        filter: drop-shadow(0 0 10px rgba(244, 114, 182, 0.8));
    }
    @keyframes handsTug {
        0% { transform: translateY(0px) rotate(-2deg); }
        100% { transform: translateY(8px) rotate(2deg); }
    }

    /* FLOATING RELEASING SOFTWARE ARTEFACTS & PAPERS (Simulating PM/RM Release Drops) */
    @keyframes releaseDrift {
        0% { transform: translateY(-50px) rotate(0deg) scale(0.8); opacity: 0; }
        20% { opacity: 0.8; }
        80% { opacity: 0.8; }
        100% { transform: translateY(105vh) rotate(360deg) scale(1.1); opacity: 0; }
    }

    .floating-artefact {
        position: fixed;
        pointer-events: none;
        z-index: 998;
        font-family: monospace;
        font-weight: 700;
        padding: 0.5rem 1rem;
        border-radius: 12px;
        backdrop-filter: blur(8px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        animation: releaseDrift linear infinite;
    }
    .art-1 { top: -10%; left: 8%; background: rgba(78, 205, 196, 0.15); border: 1px solid #4ECDC4; color: #4ECDC4; animation-duration: 9s; animation-delay: 0s; }
    .art-2 { top: -10%; left: 75%; background: rgba(244, 114, 182, 0.15); border: 1px solid #f472b6; color: #f472b6; animation-duration: 12s; animation-delay: 3s; }
    .art-3 { top: -10%; left: 35%; background: rgba(255, 230, 109, 0.15); border: 1px solid #FFE66D; color: #FFE66D; animation-duration: 7s; animation-delay: 5s; }
    .art-4 { top: -10%; left: 88%; background: rgba(168, 85, 247, 0.15); border: 1px solid #a855f7; color: #c084fc; animation-duration: 10s; animation-delay: 1.5s; }

    /* Hero Section */
    .playful-hero-container {
        padding: 9rem 1rem 4rem 1rem;
        text-align: center;
        max-width: 950px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }
    
    .playful-title {
        font-size: 4.5rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.1;
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 40%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: hueShift 8s infinite alternate;
        margin-bottom: 1.5rem;
    }

    @keyframes hueShift {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
    
    .playful-subtitle {
        font-size: 1.5rem;
        color: #94a3b8;
        font-weight: 500;
        line-height: 1.5;
    }

    /* Fun Chapter Cards */
    .fun-chapter-card {
        background: rgba(20, 20, 30, 0.75);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 2px solid rgba(255, 255, 255, 0.08);
        border-radius: 32px;
        padding: 4rem;
        margin: 0 auto 5rem auto;
        max-width: 1050px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        z-index: 2;
        
        opacity: 0;
        transform: translateY(80px) scale(0.95);
        animation: playfulReveal linear forwards;
        animation-timeline: view();
        animation-range: entry 5% cover 30%;
    }
    
    .fun-chapter-card:hover {
        transform: translateY(-8px) scale(1.01);
        border-color: #f472b6;
        box-shadow: 0 30px 70px rgba(244, 114, 182, 0.25);
    }

    @keyframes playfulReveal {
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    .card-badge-top {
        display: inline-block;
        background: rgba(244, 114, 182, 0.15);
        color: #f472b6;
        border: 1px solid rgba(244, 114, 182, 0.4);
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 1.2rem;
    }

    .card-main-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.4rem;
    }

    .card-time-role {
        font-size: 1.15rem;
        color: #4ECDC4;
        font-weight: 700;
        margin-bottom: 2.5rem;
    }

    .card-story-text {
        font-size: 1.2rem;
        color: #cbd5e1;
        line-height: 1.8;
        margin-bottom: 1.8rem;
        font-weight: 400;
    }

    .card-quote-box {
        background: rgba(244, 114, 182, 0.05);
        border-left: 4px solid #f472b6;
        padding: 1.2rem 1.5rem;
        border-radius: 0 16px 16px 0;
        color: #FFE66D;
        font-style: italic;
        font-size: 1.25rem;
        margin: 2rem 0;
        font-weight: 500;
    }

    .pill-box {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        margin-top: 2rem;
    }

    .fun-pill {
        background: rgba(255, 255, 255, 0.04);
        color: #f8fafc;
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 0.6rem 1.3rem;
        border-radius: 50px;
        font-size: 0.95rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .fun-pill:hover {
        background: #f472b6;
        color: #08080a;
        border-color: #f472b6;
        transform: translateY(-4px) rotate(-1deg);
        box-shadow: 0 10px 20px rgba(244, 114, 182, 0.3);
    }

    /* AI Vibe Coding Zone */
    .ai-zone-title {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin: 8rem 0 1rem 0;
        background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
        z-index: 2;
    }

    .ai-cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2.5rem;
        max-width: 1050px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }

    .fun-ai-card {
        background: linear-gradient(145deg, rgba(20,20,30,0.85) 0%, rgba(10,10,15,0.95) 100%);
        border: 2px solid rgba(168, 85, 247, 0.25);
        border-radius: 28px;
        padding: 3rem;
        transition: all 0.4s ease;
    }

    .fun-ai-card:hover {
        transform: translateY(-10px);
        border-color: #a855f7;
        box-shadow: 0 20px 40px rgba(168, 85, 247, 0.3);
    }
    </style>

    <!-- FIXED OVERLAY RIG: Puppet-Strings & POC Puppeteer Symbolism from Above -->
    <div class="puppet-master-rig">
        <div class="puppeteer-silhouette">
            <div class="puppeteer-hands-icon">✊🏽🧵✨</div>
        </div>
        <div class="string-line string-1"></div>
        <div class="string-line string-2"></div>
        <div class="string-line string-3"></div>
    </div>

    <!-- FLOATING SOFTWARE RELEASES & ARTEFACTS FALLING AS WE SCROLL -->
    <div class="floating-artefact art-1">📄 Release_Note_v1.0.pdf</div>
    <div class="floating-artefact art-2">🚀 Dynamics365_GoLive.pkg</div>
    <div class="floating-artefact art-3">💡 PMO_Governance_v2.json</div>
    <div class="floating-artefact art-4">⚡ Streamlit_App_v4.5.py</div>
""", unsafe_allow_html=True)

# 3. Hero Section
st.markdown("""
    <div class="playful-hero-container">
        <div class="playful-title">Pulling the Strings of Enterprise Delivery.</div>
        <div class="playful-subtitle">Steering complex systems from above with precision. Blending 8+ years of robust Program & Release Management governance with high-energy AI vibe-coding.</div>
    </div>
""", unsafe_allow_html=True)

# 4. Content Chapters
chapters = [
    {
        "badge": "Level 01 • The Foundation",
        "title": "Controlling the Control Room",
        "role": "Release & Deployment Manager | Cognizant",
        "timeline": "March 2016 – December 2018",
        "story": "Every great production is orchestrated from above. Managing high-stakes multi-environment builds and strict Change Advisory Board (CAB) protocols taught me how to keep every operational string tightly controlled for zero critical downtime.",
        "quote": "Absolute control over underlying release mechanics creates total operational freedom.",
        "story_2": "Standardized core rollout playbooks, securing absolute compliance and zero critical post-release incidents.",
        "skills": ["CAB Governance", "ServiceNow", "ITIL Framework", "Release Tracking", "Defect Shielding"]
    },
    {
        "badge": "Level 02 • The Orchestrator",
        "title": "Synchronizing Large-Scale Systems",
        "role": "Technical Project Manager | Guidewire Software",
        "timeline": "June 2020 – September 2024",
        "prose": " Scaling up meant handling complex multi-tiered enterprise implementations across full SDLC cycles. Pulling the strings between development, QA, and business stakeholders required turning chaotic dependencies into smooth release cadences.",
        "quote": "Great project management pulls all the right technical threads together into a single rhythm.",
        "story_2": "Through disciplined Scrum-of-Scrums alignment and structured Jira deployment gating, I cut lower-environment downtime by 15%.",
        "skills": ["Guidewire InsuranceSuite", "Scrum-of-Scrums", "Jira & Confluence", "Go/No-Go Gates", "RCA Analysis"]
    },
    {
        "badge": "Level 03 • The Architect",
        "title": "Building Custom PMO Frameworks",
        "role": "Senior PMO & Implementation Lead | Folens & Qualtrics",
        "timeline": "October 2024 – January 2026",
        "prose": "At this stage, the mission shifted to building brand-new delivery architectures from scratch. Managing $650K ERP rollouts (Dynamics 365) and centralized Coda resource portals meant engineering systems that work seamlessly for both users and executives.",
        "quote": "A master architect doesn't just manage the pieces; they design how the whole ecosystem moves.",
        "story_2": "Delivered Phase 1 rollouts four weeks ahead of schedule and automated business workflows by 30%.",
        "skills": ["Dynamics 365", "PMO Architecture", "Coda Portals", "UAT Mastery", "Stakeholder Sync"]
    },
    {
        "badge": "Level 04 • The Sandbox",
        "title": "AI Vibe-Coding & Rapid Innovation",
        "role": "AI Tooling Specialist | Independent R&D",
        "timeline": "February 2026 – Present",
        "prose": "Combining 8 years of solid enterprise governance with modern AI-assisted prototyping tools. I build interactive web apps, dashboards and automated tooling to eliminate manual PMO busywork entirely.",
        "quote": "The future belongs to builders who can bridge rigorous governance with rapid, animated execution.",
        "story_2": "Deploying custom Python/Streamlit dashboards, prompt-engineered pipelines, and dynamic micro-apps.",
        "skills": ["Vibe Coding", "Streamlit Apps", "MCP Agents", "Python Automation", "LLM Tooling"]
    }
]

# Render Chapters
for ch in chapters:
    pills_html = "".join([f'<span class="fun-pill">{skill}</span>' for skill in ch["skills"]])
    
    st.markdown(f"""
    <div class="fun-chapter-card">
        <div class="card-badge-top">{ch["badge"]}</div>
        <div class="card-main-title">{ch["title"]}</div>
        <div class="card-time-role">{ch["role"]} &nbsp;•&nbsp; {ch["timeline"]}</div>
        
        <div class="card-story-text">{ch.get("story", ch.get("prose"))}</div>
        
        <div class="card-quote-box">"{ch["quote"]}"</div>
        
        <div class="card-story-text">{ch["story_2"]}</div>
        
        <div class="pill-box">
            {pills_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# 5. AI Vibe Coding Showcase Section
st.markdown('<div class="ai-zone-title">AI Vibe-Coding Zone.</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #94a3b8; max-width: 750px; margin: 0 auto 5rem auto; font-size: 1.25rem; position: relative; z-index: 2;">Interactive projects built by combining deep delivery management knowledge with fast, playful AI prototyping tools.</p>', unsafe_allow_html=True)

ai_projects = [
    {
        "title": "Interactive Streamlit Dashboards",
        "desc": "Designed and shipped this high-performance app featuring custom CSS layout for projects whiwh revolve  around complex Cusomter onboarding and custom toolkits for the entire cycle of any domains. Leveraged advanced physics, animated text gradients, and smooth scroll triggers majority of the way and trying to be avoind  as  a meat proxy.",
        "tech": "Python • Streamlit • Advanced CSS"
    },
    {
        "title": "Automated PMO Governance Bots",
        "desc": "Built smart script assistants utilizing model context protocols to rapidly parse project health metrics and structure executive briefs.",
        "tech": "MCP Agents • LLM Scripting"
    },
    {
        "title": "Agile Defect Triage Simulators",
        "desc": "Created fast prototype utilities driven by prompt engineering to accelerate lower-environment code validations and tracking.",
        "tech": "Prompt Architecture • Automation"
    }
]

st.markdown('<div class="ai-cards-grid">', unsafe_allow_html=True)
for proj in ai_projects:
    st.markdown(f"""
    <div class="fun-ai-card">
        <div style="font-size: 1.5rem; font-weight: 800; color: #ffffff; margin-bottom: 0.8rem;">{proj["title"]}</div>
        <div style="font-size: 1.05rem; color: #94a3b8; line-height: 1.6; margin-bottom: 2rem;">{proj["desc"]}</div>
        <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px; color: #a855f7; font-weight: 700; margin-bottom: 0.4rem;">Tech Specs</div>
        <div style="color: #f8fafc; font-weight: 600;">{proj["tech"]}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer Spacing
st.markdown('<div style="height: 150px;"></div>', unsafe_allow_html=True)