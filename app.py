import streamlit as st
import os

# 1. Page Setup for Responsive Design
st.set_page_config(
    page_title="Gowtham Ganesan | TPM & AI PMO Innovator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Advanced CSS Layer for Fluid Styling & Animations
st.markdown("""
    <style>
    /* Global Imports & Animations */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Canvas Padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 95%;
    }

    /* Glassmorphism Hero Section */
    .hero-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.3);
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: #94A3B8;
        margin-bottom: 1.5rem;
    }

    /* Fluid Glass Cards with Hover State */
    .custom-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.5rem;
        height: 100%;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px -3px rgba(37, 99, 235, 0.15);
        border-color: #3B82F6;
    }

    /* Modern Pill Badges */
    .badge {
        display: inline-block;
        background: #EFF6FF;
        color: #1D4ED8;
        font-weight: 600;
        font-size: 0.75rem;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
        border: 1px solid #BFDBFE;
    }
    
    .badge-alt {
        background: #F0FDF4;
        color: #15803D;
        border-color: #BBF7D0;
    }

    /* Metric Cards */
    .metric-box {
        background: #FFFFFF;
        border-left: 4px solid #2563EB;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.markdown("### ⚡ Navigation")
page = st.sidebar.radio("Navigate", ["Executive Dashboard", "AI & PMO Portfolio", "Career Journey"], label_visibility="collapsed")

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="font-size: 0.9rem; line-height: 1.6;">
    <b>Gowtham Ganesan Ambikapathy</b><br>
    📍 Dublin, Ireland<br>
    🛂 <b>Stamp 4 Visa Holder</b><br>
    📧 <a href="mailto:gowthamganesanambikapathy@gmail.com">Email Me</a><br>
    🔗 <a href="https://linkedin.com/in/gowthamganesan" target="_blank">LinkedIn</a> | 
    💻 <a href="https://github.com/gowthamganesan" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Download Resume Button
resume_path = "assets/Gowtham_Ganesan_Resume.pdf"
if os.path.exists(resume_path):
    with open(resume_path, "rb") as pdf_file:
        st.sidebar.download_button(
            label="📄 Download Official Resume",
            data=pdf_file,
            file_name="Gowtham_Ganesan_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# 4. View Routing

if page == "Executive Dashboard":
    # Hero Section
    st.markdown("""
        <div class="hero-card">
            <div class="hero-title">Gowtham Ganesan Ambikapathy</div>
            <div class="hero-subtitle">Technical Program Manager | Enterprise Release Lead | AI PMO Builder</div>
            <span class="badge badge-alt">Stamp 4 Visa (Ireland)</span>
            <span class="badge">8+ Years Experience</span>
            <span class="badge">Dynamics 365 & Guidewire</span>
            <span class="badge">ITIL & SAFe</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Overview & Metrics Grid
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""<div class="metric-box"><span style="color: #64748B; font-size: 0.8rem;">TOTAL EXPERIENCE</span><h2 style="margin:0; color:#0F172A;">8+ Yrs</h2></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="metric-box"><span style="color: #64748B; font-size: 0.8rem;">DOWNTIME REDUCTION</span><h2 style="margin:0; color:#2563EB;">15%</h2></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="metric-box"><span style="color: #64748B; font-size: 0.8rem;">DEFECT RESOLUTION</span><h2 style="margin:0; color:#16A34A;">+25%</h2></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="metric-box"><span style="color: #64748B; font-size: 0.8rem;">ERP BUDGET CONTROL</span><h2 style="margin:0; color:#0F172A;">$650K+</h2></div>""", unsafe_allow_html=True)

    st.markdown("###")
    
    # About Section
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown("#### Executive Summary")
        st.write("""
        Technical Program Manager and Enterprise Release Lead with over 8 years of hands-on experience driving complex ERP (Dynamics 365, Guidewire), 
        SaaS, and infrastructure programs across global teams[cite: 1]. Expert in structured release governance, environment management, and ITIL-aligned 
        production readiness[cite: 1]. 
        
        A modern practitioner combining traditional delivery frameworks (Agile, Waterfall, Hybrid)[cite: 1] with active AI tooling, vibe coding, 
        and custom automation scripts to streamline governance and eliminate delivery bottlenecks[cite: 1].
        """)
    
    with col_b:
        st.markdown("#### Core Technical Stack")
        st.markdown("""
        <span class="badge">Python / Streamlit</span>
        <span class="badge">MCP Agents</span>
        <span class="badge">Jira / Confluence</span>
        <span class="badge">ServiceNow</span>
        <span class="badge">Azure DevOps</span>
        <span class="badge">CI/CD & Jenkins</span>
        """, unsafe_allow_html=True)

elif page == "AI & PMO Portfolio":
    st.markdown("## 📊 AI PMO Applications & Automation")
    st.caption("Self-directed prototypes and operational tools engineered using LLM APIs, Streamlit, and Model Context Protocol (MCP) servers.")
    st.markdown("---")
    
    # Dynamic Card Grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="custom-card">
                <span class="badge">Streamlit + LLM</span>
                <h3 style="margin-top:0.5rem; color:#0F172A;">AI PMO Executive Dashboard</h3>
                <p style="color:#475569; font-size:0.9rem;">
                    An interactive delivery tracking dashboard integrating LLMs to auto-generate executive status updates, calculate sprint burn-down risk, and parse unstructured defect logs.
                </p>
                <span class="badge">Python</span> <span class="badge">Pandas</span> <span class="badge">OpenAI API</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("###")
        if st.button("🚀 View AI PMO Dashboard Details", key="btn1"):
            st.info("Repository Link: `github.com/gowthamganesan/ai-pmo-dashboard` | Features automated document generation via custom LLM prompts.")

    with col2:
        st.markdown("""
            <div class="custom-card">
                <span class="badge badge-alt">Model Context Protocol</span>
                <h3 style="margin-top:0.5rem; color:#0F172A;">MCP Governance & Compliance Agent</h3>
                <p style="color:#475569; font-size:0.9rem;">
                    Custom FastMCP agent pipeline that connects enterprise file repositories to local models to parse compliance files and auto-populate change control logs.
                </p>
                <span class="badge">FastMCP</span> <span class="badge">Python</span> <span class="badge">JSON-RPC</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("###")
        if st.button("🚀 View MCP Agent Details", key="btn2"):
            st.info("Repository Link: `github.com/gowthamganesan/mcp-governance-agent` | Designed for automated audit readiness.")

elif page == "Career Journey":
    st.markdown("## 💼 Professional Experience")
    st.caption("Detailed delivery history across enterprise implementation, release leadership, and technical consulting.")
    st.markdown("---")

    # Interactive Accordion Timeline
    with st.expander("🛠️ **AI PMO Specialist & Tooling Builder** | Independent Venture | *Feb 2026 – Present*", expanded=True):
        st.markdown("""
        * **Vibe Coding & Automation:** Engineered AI-assisted scripts and Streamlit web applications to streamline PMO reporting and release tracking.
        * **MCP Integration:** Architected Model Context Protocol agentic workflows to convert raw release notes into executive status decks.
        * **Code Governance:** Maintained active GitHub repos with full version control and structured documentation.
        """)

    with st.expander("💼 **Senior PMO / Implementation PM (Contract)** | Folens | *Jul 2025 – Jan 2026*"):
        st.markdown("""
        * **Dynamics 365 Rollout:** Delivered Phase 1 of a $650K ERP deployment for 80+ users **4 weeks ahead of schedule**[cite: 1].
        * **Governance Framework:** Established centralized PMO documentation and defect triage workflows, reducing early defects by 25%[cite: 1].
        * **Process Automation:** Streamlined business execution, achieving 30% process automation across business workflows[cite: 1].
        """)

    with st.expander("🤝 **Senior Technology Consultant (Engagement)** | Qualtrics | *Oct 2024 – Mar 2025*"):
        st.markdown("""
        * **Enterprise SaaS Delivery:** Led post-sales implementations from Solution Architecture handover to final deployment[cite: 1].
        * **PMO Architecture:** Engineered a centralized PMO Resource Library in Coda to standardize delivery frameworks[cite: 1].
        """)

    with st.expander("⚡ **Technical PM & Release Coordinator** | Guidewire Software | *Jun 2020 – Sep 2024*"):
        st.markdown("""
        * **Guidewire Implementations:** Coordinated builds, deployments, and Go/No-Go readiness gates across Dev, QA, and UAT environments[cite: 1].
        * **Downtime Reduction:** Designed daily lower-environment checklists in Jira, **reducing system downtime by 15%**[cite: 1].
        """)