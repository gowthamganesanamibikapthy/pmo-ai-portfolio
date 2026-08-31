import streamlit as st
import time

# 1. Page Config
st.set_page_config(
    page_title="Gowtham Ganesan | Interactive Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Comprehensive Animation & Design CSS Engine
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* KEYFRAME ANIMATIONS */
    @keyframes fadeInSlideUp {
        0% { opacity: 0; transform: translateY(25px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.4); }
        70% { box-shadow: 0 0 15px 8px rgba(37, 99, 235, 0); }
        100% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0); }
    }

    @keyframes borderBeam {
        0% { border-color: #2563EB; }
        50% { border-color: #10B981; }
        100% { border-color: #2563EB; }
    }

    /* HERO ANIMATED BANNER */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        border: 2px solid #2563EB;
        animation: borderBeam 6s infinite linear, fadeInSlideUp 0.8s ease-out;
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: 2.6rem;
        font-weight: 700;
        background: linear-gradient(90deg, #3B82F6, #60A5FA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    /* INTERACTIVE HOVER CARDS FOR SKILLS & PROJECTS */
    .anim-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInSlideUp 0.6s ease-out;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }

    .anim-card:hover {
        transform: translateY(-8px) scale(1.01);
        box-shadow: 0 20px 25px -5px rgba(37, 99, 235, 0.15);
        border-color: #2563EB;
    }

    /* ANIMATED BADGES */
    .badge {
        display: inline-block;
        background: #EFF6FF;
        color: #1D4ED8;
        font-weight: 600;
        font-size: 0.8rem;
        padding: 0.3rem 0.8rem;
        border-radius: 9999px;
        margin: 0.2rem;
        border: 1px solid #BFDBFE;
        transition: transform 0.2s ease;
    }
    .badge:hover {
        transform: scale(1.1);
        background: #2563EB;
        color: white;
    }
    
    .badge-ai {
        background: #ECFDF5;
        color: #047857;
        border-color: #A7F3D0;
    }
    .badge-ai:hover {
        background: #10B981;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Setup
st.sidebar.title("⚡ Navigation")
nav = st.sidebar.radio("Go to Section", [
    "1. Executive Overview", 
    "2. Interactive Core Competencies", 
    "3. AI Vibe Coding & Tooling Lab", 
    "4. Career Experience Timeline"
])

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Gowtham Ganesan Ambikapathy**  
📍 Dublin, Ireland  
🛂 **Stamp 4 Visa Holder**  
✉️ [Email Me](mailto:gowthamganesanambikapathy@gmail.com)
""")

# 4. View Routing & Animations

# --- SECTION 1: EXECUTIVE OVERVIEW ---
if nav == "1. Executive Overview":
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Gowtham Ganesan Ambikapathy</div>
            <h3 style="margin-top: 0; color: #94A3B8;">Technical Program Manager | Release & Deployment Lead | AI PMO Builder</h3>
            <span class="badge badge-ai">Stamp 4 Visa (Ireland)</span>
            <span class="badge">8+ Years Experience</span>
            <span class="badge">Dynamics 365 & Guidewire</span>
            <span class="badge">Vibe-Coding Practitioner</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Value Delivered Snapshot")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="Downtime Reduction", value="15%", delta="Guidewire Infrastructure")
    with c2:
        st.metric(label="Process Automation", value="30%", delta="Dynamics 365 Rollout")
    with c3:
        st.metric(label="Defect Resolution", value="25%", delta="Model Office Validation")
    with c4:
        st.metric(label="Post-Release Incidents", value="0", delta="100% Task Completion")

    st.markdown("---")
    st.markdown("### 💡 What I Bring to the Table")
    st.write("""
    I bridge the gap between heavy enterprise delivery frameworks (Agile, SAFe, ITIL) and modern AI automation. 
    By combining 8+ years of hands-on ERP/SaaS release leadership with natural language AI vibe coding, I eliminate 
    reporting overhead, streamline defect triaging, and accelerate go-live timelines.
    """)

# --- SECTION 2: INTERACTIVE CORE COMPETENCIES ---
elif nav == "2. Interactive Core Competencies":
    st.markdown("## 🧠 Core Skill Set & Technical Proficiency")
    st.caption("Select categories below to interactively explore domain mastery and tools.")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Program Governance", 
        "🚀 Release & Operations", 
        "🤖 AI & Technical Stack", 
        "💼 Enterprise Platforms"
    ])

    with tab1:
        st.markdown("""
            <div class="anim-card">
                <h4>Program & Delivery Governance</h4>
                <p>Full lifecycle ownership across hybrid and Agile frameworks.</p>
                <span class="badge">Technical Program Management (TPM)</span>
                <span class="badge">PMO Setup & Frameworks</span>
                <span class="badge">Scope & Dependency Mapping</span>
                <span class="badge">Risk & Issue Mitigation</span>
                <span class="badge">UAT & Business Readiness</span>
            </div>
        """, unsafe_allow_html=True)
        st.write("**Proficiency Index:**")
        st.progress(0.95, text="Program Management & Governance (95%)")
        st.progress(0.90, text="UAT & Business Readiness (90%)")

    with tab2:
        st.markdown("""
            <div class="anim-card">
                <h4>Release & Production Operations</h4>
                <p>ITIL-aligned deployment execution and production controls.</p>
                <span class="badge">Environment Management</span>
                <span class="badge">Change Advisory Board (CAB)</span>
                <span class="badge">Go/No-Go Readiness Gates</span>
                <span class="badge">ITIL Defect & Problem Resolution</span>
            </div>
        """, unsafe_allow_html=True)
        st.write("**Proficiency Index:**")
        st.progress(0.92, text="Release & Environment Management (92%)")
        st.progress(0.88, text="ITIL Incident & Defect Resolution (88%)")

    with tab3:
        st.markdown("""
            <div class="anim-card">
                <h4>AI & Applied Technical Stack</h4>
                <p>Practical AI-assisted prototyping and automated workflow engines.</p>
                <span class="badge badge-ai">Vibe Coding (AI-Assisted Prototyping)</span>
                <span class="badge badge-ai">Model Context Protocol (MCP)</span>
                <span class="badge badge-ai">Streamlit Dashboards</span>
                <span class="badge badge-ai">Python Scripts & LLM APIs</span>
                <span class="badge badge-ai">Git / GitHub & CI/CD Pipelines</span>
            </div>
        """, unsafe_allow_html=True)
        st.write("**Proficiency Index:**")
        st.progress(0.85, text="Applied AI Tooling & Vibe Coding (85%)")
        st.progress(0.80, text="Python & Streamlit Development (80%)")

    with tab4:
        st.markdown("""
            <div class="anim-card">
                <h4>Enterprise Platforms & Tooling</h4>
                <span class="badge">Microsoft Dynamics 365 Business Central</span>
                <span class="badge">Guidewire InsuranceSuite</span>
                <span class="badge">Qualtrics</span>
                <span class="badge">ServiceNow</span>
                <span class="badge">Jira / Confluence</span>
                <span class="badge">Azure DevOps</span>
                <span class="badge">Coda</span>
            </div>
        """, unsafe_allow_html=True)

# --- SECTION 3: AI VIBE CODING & TOOLING LAB ---
elif nav == "3. AI Vibe Coding & Tooling Lab":
    st.markdown("## 🧪 Live AI Tooling & PMO Application Demos")
    st.caption("Interactive simulations of AI tools engineered to automate program management bottlenecks.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="anim-card">
                <span class="badge badge-ai">Live Interactive Simulation</span>
                <h3>📊 AI PMO Status Generator</h3>
                <p>Simulate an AI agent parsing raw defect data into executive summaries.</p>
            </div>
        """, unsafe_allow_html=True)
        
        raw_input = st.text_area("Input Raw Incident Log:", "Defect #409: Dynamics 365 migration timed out during UAT. 12 records unmapped.")
        if st.button("🚀 Run AI Agent Parsing"):
            with st.spinner("AI Agent processing via prompt pipeline..."):
                time.sleep(1)
                st.success("Analysis Complete!")
                st.json({
                    "Root Cause": "Data Mapping Timeout",
                    "Impacted Workstream": "Dynamics 365 Migration",
                    "Executive Summary": "Isolated non-critical defect on 12 unmapped records; UAT target timeline unimpacted.",
                    "Recommended Action": "Trigger automated re-run script."
                })

    with col2:
        st.markdown("""
            <div class="anim-card">
                <span class="badge badge-ai">Protocol Architecture</span>
                <h3>🤖 MCP Governance Server</h3>
                <p>Extracts compliance artifacts directly from project documents.</p>
            </div>
        """, unsafe_allow_html=True)
        
        doc_type = st.selectbox("Select Project Artifact Type:", ["Release Readiness Sign-off", "CAB Deployment Checklist", "UAT Defect Summary"])
        if st.button("⚡ Generate Automated Template"):
            st.info(f"Generated standardized {doc_type} template using LLM Prompt Engineering.")
            st.code(f"""
# {doc_type.upper()}
Status: Approved for Production
Validated By: Technical Program Manager
Automated Verification: 100% Code Promotion Checked
            """, language="markdown")

# --- SECTION 4: CAREER EXPERIENCE TIMELINE ---
elif nav == "4. Career Experience Timeline":
    st.markdown("## 💼 Professional Experience Timeline")
    st.caption("Click any role to expand metrics and full project achievements.")

    with st.expander("🤖 **AI Tooling Specialist & PMO Innovator** | Self-Directed Venture | *Feb 2026 – Present*", expanded=True):
        st.markdown("""
        * Built AI-assisted applications using natural language prompt-engineering ("vibe coding") and LLMs to solve PMO operational bottlenecks.
        * Developed custom Streamlit dashboards and automated status report generators to parse raw project metrics and defect logs.
        * Leveraged Model Context Protocol (MCP) servers and AI agents to auto-generate enterprise governance artifacts.
        """)

    with st.expander("💼 **Senior PMO / Implementation PM (Contract)** | Folens | *Jul 2025 – Jan 2026*"):
        st.markdown("""
        * **Dynamics 365 Rollout:** Led Phase 1 of a $650K rollout for 80+ users, delivering **4 weeks ahead of schedule** with 30% process automation.
        * **PMO Architecture:** Established centralized documentation repositories, defect triage processes, and change control frameworks.
        * **Quality Control:** Directed Model Office Testing, reducing early-stage deployment defects by 25% prior to UAT.
        """)

    with st.expander("🤝 **Senior Technology Consultant (Engagement)** | Qualtrics | *Oct 2024 – Mar 2025*"):
        st.markdown("""
        * **SaaS Implementation:** Directed full-lifecycle enterprise SaaS implementations from Solution Architect handover to client sign-off.
        * **Documentation Standard:** Engineered a centralized PMO Handbook and Resource Library in Coda to standardize delivery templates.
        """)

    with st.expander("⚡ **Technical PM & Release Coordinator** | Guidewire Software | *Jun 2020 – Sep 2024*"):
        st.markdown("""
        * **SDLC Coordination:** Directed end-to-end Guidewire InsuranceSuite implementations across global cross-functional workstreams.
        * **Operational Stability:** Created lower-environment deployment checklists in Jira, **reducing system downtime by 15%**.
        """)

    with st.expander("🌐 **Release & Deployment Manager** | Cognizant | *Mar 2016 – Dec 2018*"):
        st.markdown("""
        * **CAB Governance:** Managed build and rollback cadences, partnering with CAB via ServiceNow for enterprise compliance.
        * **Deployment Success:** Authored the Release Implementation Playbook, achieving 100% release task completion with zero critical incidents.
        """)