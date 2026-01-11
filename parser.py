import streamlit as st
import requests
import json
import re

# =============================
# Config
# =============================
API_URL = "https://leptophyllous-cachectic-colleen.ngrok-free.dev/parse_cv"
API_KEY = "secret123"

st.set_page_config(
    page_title="CV Parser",
    page_icon="📄",
    layout="centered"
)

# =============================
# Styles (RED THEME)
# =============================
st.markdown("""
<style>
body, .main {
    background-color: #0d1117;
    color: white;
}

.container {
    max-width: 600px;
    margin: auto;
    padding: 40px;
    background: #111827;
    border-radius: 16px;
    border: 1px solid #7f1d1d;
    text-align: center;
}

.title {
    font-size: 44px;
    font-weight: 900;
    color: #ef4444;
}

.subtitle {
    color: #fca5a5;
    margin-bottom: 30px;
}

.stButton > button {
    background: linear-gradient(135deg, #ef4444, #b91c1c);
    color: white;
    font-weight: 700;
    border-radius: 10px;
    padding: 10px 30px;
    border: none;
    font-size: 16px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #f87171, #dc2626);
}

.label {
    margin-top: 30px;
    font-size: 20px;
    font-weight: 700;
    color: #f87171;
    text-align: left;
}

/* 🔴 Skills Grid */
.skills-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 12px;
}

.skill-chip {
    background: linear-gradient(135deg, #ef4444, #b91c1c);
    color: white;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    box-shadow: 0 4px 10px rgba(239, 68, 68, 0.35);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.skill-chip:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(239, 68, 68, 0.5);
}
</style>
""", unsafe_allow_html=True)

# =============================
# Helper
# =============================
def extract_and_clean_json(text):
    match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()

# =============================
# UI
# =============================
st.markdown("""
<div class="container">
    <div class="title">📄 CV Parser</div>
    <div class="subtitle">Upload your CV and get structured data instantly</div>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload CV (PDF)", type=["pdf"])
parse_btn = st.button("Parse CV")

# =============================
# Logic
# =============================
if uploaded_file and parse_btn:
    with st.spinner("Parsing CV..."):
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }
        headers = {"Authorization": f"Bearer {API_KEY}"}

        response = requests.post(API_URL, files=files, headers=headers, timeout=600)
        response.raise_for_status()

        clean_json = extract_and_clean_json(response.json()["parsed_cv"])
        parsed = json.loads(clean_json)

    st.success("✅ CV Parsed Successfully")

    st.markdown("<div class='label'>👤 Full Name</div>", unsafe_allow_html=True)
    st.write(parsed.get("full_name", "N/A"))

    st.markdown("<div class='label'>📧 Email</div>", unsafe_allow_html=True)
    st.write(parsed.get("email", "N/A"))

    st.markdown("<div class='label'>🎓 Education</div>", unsafe_allow_html=True)
    st.write(parsed.get("education", "N/A"))

    st.markdown("<div class='label'>🛠 Skills</div>", unsafe_allow_html=True)
    skills = parsed.get("skills", [])
    if isinstance(skills, str):
        skills = [s.strip() for s in skills.split(",")]

    skills_html = "<div class='skills-grid'>"
    for skill in skills:
        skills_html += f"<div class='skill-chip'>{skill}</div>"
    skills_html += "</div>"
    st.markdown(skills_html, unsafe_allow_html=True)

    st.markdown("<div class='label'>💼 Experience</div>", unsafe_allow_html=True)
    st.write(parsed.get("experience", "N/A"))
