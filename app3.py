import streamlit as st
from pathlib import Path
from datetime import datetime
import base64
from PIL import Image
# Color for different project types
PROJECT_TYPE_COLORS = {
    "Research Paper": "#06B6D4",   # cyan
    "Project": "#2563EB",          # bright tech blue
    "Creative Project": "#DB2777"  # neon magenta
}

# ---------------------------
# Basic Config
# ---------------------------
st.set_page_config(page_title="Raghav Goel — Portfolio", page_icon=":briefcase:", layout="wide")

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
RESUME_FILE = BASE_DIR / "MSBA_RAGHAVGOEL_FINAL.pdf"
PROFILE_IMG = ASSETS_DIR / "profile.jpg"

# ---------------------------
# Helper functions
# ---------------------------
def file_download_link(file_path: Path, label="Download"):
    if not file_path.exists():
        return None
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path.name}">{label}</a>'
    return href

# ---------------------------
# Custom CSS Styling
# ---------------------------

st.markdown("""
<style>
:root {
  --bg: #0a0f1c;
  --card: #111827;
  --accent: #60a5fa;
  --gold: #fbbf24;
  --text: #e5e7eb;
  --muted: #9ca3af;
}


            

/* Background and font */
[data-testid="stAppViewContainer"] {
  background-color: var(--bg);
  color: var(--text);
  font-family: 'Segoe UI', sans-serif;
}

/* Headings */
h1,h2,h3 {
  color: var(--gold);
}

/* Cards */
.card {
  background-color: var(--card);
  padding: 20px;
  border-radius: 12px;
  margin: 15px 10px;              /* 🌟 Adds spacing between cards */
  transition: all 0.25s ease;
  box-shadow: 0 8px 20px rgba(0,0,0,0.35);
  height: 100%;                   /* Ensures consistent height */
}
.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.5);
}

/* Tag styling */
.tag {
  background: rgba(96,165,250,0.15);
  color: var(--accent);
  border-radius: 999px;
  padding: 5px 10px;
  margin-right: 6px;
  font-size: 12px;
}

/* CTA button */
.cta {
  background: linear-gradient(90deg, var(--accent), var(--gold));
  color: #0b1020;
  padding: 8px 12px;
  border-radius: 6px;
  font-weight: 700;
  text-decoration: none;
}
.cta:hover {
  opacity: 0.9;
  box-shadow: 0 0 10px rgba(251,191,36,0.4);
}

/* Add top spacing for entire Projects section */
section.projects {
  margin-top: 30px;
}

/* Adjust column spacing for better breathing room */
div[data-testid="column"] {
  padding: 5px 15px;             /* horizontal spacing between columns */
}

/* Footer */
.footer {
  text-align: center;
  color: var(--muted);
  padding: 16px 0;
  font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.image(str(PROFILE_IMG), use_column_width=False, width=160)
st.sidebar.markdown("### Raghav Goel")
st.sidebar.caption("📍 MSc Business Analytics — NTU, Singapore")

st.sidebar.markdown("---")
st.sidebar.markdown("\n**Citizen:** India   \n**Residence:** Singapore   \n**Area:** Jurong West  \n**Email:** raghav010@e.ntu.edu.sg  \n**Phone:** +65 9349 4001")

st.sidebar.markdown("---")
st.sidebar.subheader("Skills")
skills = {
    "Python": 50,
    "SQL": 60,
    "Tableau": 90,
    "Microsoft Office": 90,
    "Canva": 100,     
    "English" : 95
}
for skill, val in skills.items():
    st.sidebar.progress(val/100, text=f"{skill} ({val}%)")

st.sidebar.markdown("---")
resume_link = file_download_link(RESUME_FILE, label="📄 Download Resume")
if resume_link:
    st.sidebar.markdown(resume_link, unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 Raghav Goel")

# ---------------------------
# Hero Section
# ---------------------------
st.markdown("## 👋 Hi, I’m **Raghav Goel**")
st.write("""
I am a  **business analytics** professional pursuing an MSc in Business Analytics at **Nanyang Technological University (NTU)**, Singapore, with a **BBA in Marketing & Management from NMIMS,
Mumbai, India**. I specialize in translating data into actionable insights to optimize operations, improve decision-making, and drive measurable business outcomes., I blend analytical rigor with strategic thinking 
to create sustainable growth opportunities for businesses.
""")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------
# Projects Section
# ---------------------------

# ---------------------------
# PROJECTS SECTION
# ---------------------------

import json

# Load projects from JSON
PROJECTS_FILE = BASE_DIR / "projects.json"

def load_projects():
    if PROJECTS_FILE.exists():
        with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        st.warning("⚠️ projects.json not found — using sample data.")
        return [
            {
                "title": "Car Price Analysis",
                "description": "Performed ANOVA, regression, and EDA to identify key pricing drivers.",
                "tags": ["Python", "EDA"],
                "link": "https://github.com/raghavgoel/car-price-analysis",
                "type": "project"
            },
            {
                "title": "Sustainable Packaging Research",
                "description": "Conducted Primary and Secondary research to reveal brand trust (+148%) and environmental awareness (+64%) as key drivers for sustainable packaging adoption and loyalty.",
                "tags": ["Research", "Sustainability"],
                "link": "https://github.com/raghavgoel9670/CapstoneProject",
                "type": "project"
            },
            {
                "title": "Metaverse Marketing Research Paper",
                "description": "Published IJARESM paper analysing 20 virtual worlds and 100 surveys to develop branding strategies.",
                "tags": ["Marketing", "Analytics"],
                "link": "https://drive.google.com/file/d/your-paper-id/view",
                "type": "paper"
            }
        ]

# Load the data
projects = load_projects()

# Display Projects
st.markdown("### 💼 Projects")



cols = st.columns(3)
for i, proj in enumerate(projects):
    with cols[i % 3]:

        proj_type = proj.get("type", "Project")  # Default to 'Project'
        card_color = PROJECT_TYPE_COLORS.get(proj_type, "#0F172A")

        link = proj.get("link", "#")
        tags_html = "".join([f"<span class='tag'>{t}</span>" for t in proj.get("tags", [])])

        st.markdown(
            f"""
            <div class='card' style="background-color:{card_color};">
                <h4>{proj['title']}</h4>
                <p>{proj['description']}</p>
                {tags_html}
                <br><br>
                <a href="{link}" target="_blank" class="cta">
                    View {proj_type} →
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------
# Internship Section
# ---------------------------
st.markdown("### 🏢 Internship Experience")
st.markdown("""
**Office Sahayogi – Business Analyst Intern (Jul 2024 – Oct 2024)**  
- Improved warehousing & dispatch efficiency by 20%.  
- Reduced order fulfillment time by 15%.  

**LG India – Sales & Operations Intern (Apr 2024 – Jun 2024)**  
- Enhanced regional sales by 5% across 50+ stores.  
- Streamlined workflows reducing turnaround time by 25%.  
- Conducted onboarding sessions for 6 new hires.
""")

# ---------------------------
# Contact Section
# ---------------------------
st.markdown("### 🌐 Connect with Me")
st.markdown("""
[🔗 LinkedIn](https://www.linkedin.com/in/raghavgoel00147/)  
[💻 GitHub](https://github.com/raghavgoel9670)  
[📧 Email](mailto:raghav010@e.ntu.edu.sg)
""")

# ---------------------------
# Footer
# ---------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>© 2025 Raghav Goel — Built with Streamlit</div>", unsafe_allow_html=True)


