import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Gowtham Ganesan | TPM", page_icon="⚡", layout="wide")

# 2. Shared Master Resume Data (Ensures both modes have 100% full content)
resume_data = {
    "summary": "Technical Program Manager and Enterprise Release Lead with 8+ years of experience steering complex ERP (Dynamics 365, Guidewire), SaaS, and enterprise software implementations across global cross-functional teams. Proven track record in structured release governance, environment management, and production readiness within ITIL and Agile/Hybrid environments. Forward-thinking leader adept at leveraging AI tools, vibe-coding, Streamlit, and automated workflows to streamline PMO operations.",
    "competencies": {
        "Program & Delivery Governance": "Technical Program Management (TPM), PMO Setup, Scope & Dependency Mapping, Risk Mitigation, Agile/Scrum/Hybrid Delivery, UAT Execution, Business Readiness.",
        "Release & Production Operations": "Application Release & Deployment, Environment Management, Go/No-Go Gates, CAB (Change Advisory Board), ITIL Incident/Defect Resolution, Production Rollouts.",
        "AI & Applied Technology": "Vibe Coding (AI-Assisted Prototyping), Model Context Protocol (MCP), Streamlit Dashboards, Python Scripts, LLM Tool Integration, Git/GitHub, CI/CD Coordination.",
        "Enterprise Platforms & Tools": "Microsoft Dynamics 365 Business Central, Guidewire InsuranceSuite, Qualtrics, ServiceNow, Jira, Confluence, Azure DevOps, Coda."
    },
    "experience": [
        {
            "title": "AI Tooling Specialist & PMO Innovator (Self-Directed)",
            "company": "Portfolio & Applied AI R&D",
            "date": "February 2026 – Present",
            "bullets": [
                "Built and experimented with AI-assisted applications using natural language prompt-engineering ('vibe coding') and LLM tools to solve common program management operational bottlenecks.",
                "Developed custom Streamlit dashboards and automated report generators to parse raw project metrics, defect logs, and executive status reports.",
                "Leveraged Model Context Protocol (MCP) servers and AI agents to auto-generate enterprise governance artifacts and document templates.",
                "Maintained active GitHub repositories to store project code, manage version control, and document AI tool integration workflows."
            ]
        },
        {
            "title": "Senior PMO / Implementation Project Manager",
            "company": "Folens",
            "date": "July 2025 – January 2026",
            "bullets": [
                "Led Phase 1 of a $650K Microsoft Dynamics 365 Business Central rollout for 80+ users, delivering 4 weeks ahead of schedule by optimizing milestone execution and achieving 30% process automation.",
                "Architected a robust PMO framework—including a centralized documentation repository, strict defect triage workflows, and change control protocols—boosting execution transparency for executive stakeholders.",
                "Directed Model Office Testing and System Validation to verify end-to-end business workflows, successfully reducing early-stage deployment defects by 25% prior to UAT.",
                "Orchestrated comprehensive User Acceptance Testing (UAT) and introduced pre-deployment executive walkthroughs to secure 'fit-for-purpose' sign-offs and mitigate go-live risks.",
                "Governed complex legacy data migrations and deployed custom AI-driven reporting tools, designing targeted knowledge transfer sessions to drive long-term user adoption."
            ]
        },
        {
            "title": "Senior Technology Consultant",
            "company": "Qualtrics",
            "date": "October 2024 – March 2025",
            "bullets": [
                "Directed full-lifecycle enterprise SaaS implementations, managing the post-sales handover from Solution Architects to execute custom technical roadmaps and delivery plans.",
                "Engineered a centralized PMO Handbook and Resource Library using Coda, establishing a single source of truth for delivery templates, governance standards, and cross-team execution.",
                "Managed a hybrid delivery model, successfully balancing Out-of-the-Box (OOTB) configurations with custom-engineered solutions to meet complex enterprise client specifications.",
                "Acted as the primary technical liaison between enterprise clients and product teams, aligning scope, dependencies, and milestone execution to prevent scope creep.",
                "Orchestrated UAT, defect triaging, and go-live readiness gates, delivering targeted knowledge-transfer sessions to accelerate client onboarding and maximize platform adoption."
            ]
        },
        {
            "title": "Technical Project Manager & Release Coordinator",
            "company": "Guidewire Software",
            "date": "June 2020 – September 2024",
            "bullets": [
                "Directed end-to-end Guidewire InsuranceSuite implementations across the full SDLC, balancing technical release coordination with strict program governance for enterprise-scale customers.",
                "Facilitated Scrum-of-Scrums and managed complex cross-functional dependencies, driving technical alignment between development, QA, and business stakeholders.",
                "Orchestrated build and deployment coordination across Dev, QA, and UAT environments, implementing daily deployment checklists in Jira that reduced lower-environment downtime by 15%.",
                "Governed release cadences, Go/No-Go readiness gates, defect triaging, and pre-deployment validation to ensure high-quality code promotion with minimal operational disruption.",
                "Led post-release evaluations and Root Cause Analysis (RCA) sessions, analyzing deployment defect patterns to continuously optimize release efficiency, stability, and delivery processes."
            ]
        },
        {
            "title": "Release & Deployment Manager",
            "company": "Cognizant",
            "date": "March 2016 – December 2018",
            "bullets": [
                "Managed complex, multi-environment builds, deployments, and rollbacks across Development, QA, and Production environments.",
                "Enforced Change Advisory Board (CAB) governance and managed change artifacts via ServiceNow, ensuring strict procedural compliance for high-stakes releases.",
                "Authored the Release Implementation Playbook and standardized deployment checklists, achieving 100% completion of release tasks with zero critical post-deployment incidents.",
                "Directed UAT defect triaging and post-release Root Cause Analysis (RCA), accelerating defect resolution by 25% and reducing repeat incidents by 15%."
            ]
        }
    ]
}

# 3. Sidebar Mode Switch
st.sidebar.markdown("### 🎛️ Portfolio Mode")
is_apple_mode = st.sidebar.toggle("🍏 Enable Cinematic (Apple) Mode", value=False)
st.sidebar.markdown("---")
st.sidebar.markdown("**Gowtham Ganesan Ambikapathy**\n\n📍 Dublin, Ireland | 🛂 Stamp 4")

# ==========================================
# MODE A: CLASSIC / STATIC RESUME
# ==========================================
if not is_apple_mode:
    st.title("Gowtham Ganesan Ambikapathy")
    st.subheader("Technical Program Manager | Enterprise Release & Deployment Lead")
    st.markdown("[LinkedIn Profile] | [GitHub / Portfolio] | gowthamganesanambikapathy@gmail.com")
    st.markdown("---")
    
    st.markdown("### PROFESSIONAL SUMMARY")
    st.write(resume_data["summary"])
    
    st.markdown("### CORE COMPETENCIES")
    for category, skills in resume_data["competencies"].items():
        st.markdown(f"**{category}:** {skills}")
        
    st.markdown("### PROFESSIONAL EXPERIENCE")
    for job in resume_data["experience"]:
        st.markdown(f"#### {job['title']}")
        st.markdown(f"**{job['company']}** | {job['date']}")
        for bullet in job["bullets"]:
            st.markdown(f"- {bullet}")
        st.write("")
        
    st.markdown("### EDUCATION & CERTIFICATIONS")
    st.markdown("- **MSc in Data Analytics** | Dublin Business School, Ireland")
    st.markdown("- **B.E. in Computer Science & Engineering** | Anna University, India")
    st.markdown("- **PMP Candidate** | Project Management Institute (Expected Q4 2026)")
    st.markdown("- **SAFe 6.0 Release Train Engineer (RTE)** | Scaled Agile (In Preparation)")

# ==========================================
# MODE B: CINEMATIC APPLE-STYLE MODE
# ==========================================
else:
    # Injecting CSS for Scroll-Driven Animations
    st.markdown("""
        <style>
        /* Force dark theme aesthetics */
        .stApp {
            background-color: #000000;
            color: #f5f5f7;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        
        /* Typography */
        .apple-hero {
            font-size: 4.5rem;
            font-weight: 700;
            line-height: 1.1;
            letter-spacing: -0.02em;
            background: linear-gradient(180deg, #fff 0%, #a1a1a6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-top: 5rem;
            margin-bottom: 2rem;
        }
        
        .apple-subhero {
            font-size: 1.5rem;
            color: #86868b;
            text-align: center;
            max-width: 800px;
            margin: 0 auto 10rem auto;
            line-height: 1.5;
        }

        /* Scroll-Driven Animation Cards */
        .apple-card {
            background: rgba(28, 28, 30, 0.5);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 30px;
            padding: 4rem;
            margin: 0 auto 8rem auto;
            max-width: 1000px;
            
            /* CSS Scroll Timeline */
            opacity: 0;
            transform: translateY(100px) scale(0.95);
            animation: appleReveal linear forwards;
            animation-timeline: view();
            animation-range: entry 5% cover 25%;
        }
        
        @keyframes appleReveal {
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }
        
        .apple-card-title {
            font-size: 2.5rem;
            font-weight: 600;
            color: #f5f5f7;
            margin-bottom: 0.5rem;
        }
        
        .apple-card-subtitle {
            font-size: 1.2rem;
            color: #2997ff;
            font-weight: 500;
            margin-bottom: 2rem;
        }
        
        .apple-bullet {
            font-size: 1.1rem;
            color: #a1a1a6;
            margin-bottom: 1rem;
            line-height: 1.6;
            display: flex;
        }
        .apple-bullet::before {
            content: "•";
            color: #2997ff;
            font-size: 1.5rem;
            margin-right: 1rem;
            line-height: 1.2;
        }
        </style>
    """, unsafe_allow_html=True)

    # Render Hero Section
    st.markdown('<div class="apple-hero">Engineering Enterprise Delivery.</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="apple-subhero">{resume_data["summary"]}</div>', unsafe_allow_html=True)

    # Loop through experience and generate Apple-style scrolling cards
    for job in resume_data["experience"]:
        bullets_html = "".join([f'<div class="apple-bullet">{bullet}</div>' for bullet in job["bullets"]])
        
        st.markdown(f"""
        <div class="apple-card">
            <div class="apple-card-title">{job["title"]}</div>
            <div class="apple-card-subtitle">{job["company"]} | {job["date"]}</div>
            <div style="margin-top: 2rem;">
                {bullets_html}
            </div>
        </div>
        """, unsafe_allow_html=True)