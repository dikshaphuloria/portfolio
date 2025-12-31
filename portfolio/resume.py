import streamlit as st

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap');

    /* Title Styling */
    .playfair-title2 {{
        font-family: 'Playfair Display', serif;
        font-size: 42px;
        font-style: italic;
        font-weight: 600;
        color: #FFF3E6;
        text-align: center;   
        margin-bottom: 30px;
    }}

    /* Card Styling */
    .custom-card {{
        background-color: rgba(255, 243, 230, 0.1); /* Semi-transparent cream */
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #C89F8F;
        margin-bottom: 20px;
        color: white;
    }}

    .school-name {{
        color: #C89F8F;
        font-size: 20px;
        font-weight: bold;
    }}

    .job-date {{
        float: right;
        font-style: italic;
        font-size: 0.9em;
        color: #FFF3E6;
    }}
    </style>

    <div class="playfair-title2">
        Education & Experience
    </div>
    """,
    unsafe_allow_html=True
)

# ---- EDUCATION SECTION ----
st.subheader("🎓 Education")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="custom-card">
            <div class="school-name">Rutgers University, New Brunswick, NJ, USA </div>
            <i>MS in Data Science</i><br>
            <b>GPA:</b> 3.83 / 4.0<br>
            <span style="font-size:0.8em;">2024 – May 2026</span>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="custom-card">
            <div class="school-name">Manipal University Jaipur, Rajasthan, India </div>
            <i>B.Tech in Information Technology</i><br>
            <b>GPA:</b> 8.07 / 10<br>
            <span style="font-size:0.8em;">2017 – 2021</span>
        </div>
    """, unsafe_allow_html=True)


# ---- EXPERIENCE SECTION ----
st.subheader("💼 Professional Experience")

st.markdown("""
    <div class="custom-card">
        <span class="job-date">May 2021 – July 2023</span>
        <div class="school-name">Accenture, Gurugram</div>
        <b>Analyst – Custom Software Engineering</b>
        <ul style="margin-top:10px; font-size:0.95em;">
            <li>Supported enterprise analytics platforms (<b>Tableau, IBM Cognos</b>), improving reporting reliability.</li>
            <li>Resolved <b>100+ client issues</b> by debugging pipelines using <b>ServiceNow</b>.</li>
            <li>Monitored lifecycle metrics to ensure <b>SLA compliance</b>.</li>
            <li>Performed system maintenance and upgrades for platform stability.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)


# ---- CERTIFICATIONS & DOWNLOAD ----
c1, c2 = st.columns([1.5, 1])

with c1:
    st.subheader("📜 Certifications")
    st.markdown("""
        <style>
        .cert-link {
            color: #C89F8F; /* Using your warm brown primary color */
            text-decoration: none;
            font-weight: bold;
        }
        .cert-link:hover {
            color: #FFF3E6; /* Lightens on hover */
            text-decoration: underline;
        }
        </style>
        
        <div style="background: rgba(200, 159, 143, 0.2); padding: 15px; border-radius: 10px; border: 1px solid rgba(200, 159, 143, 0.3);">
            <a class="cert-link" href="https://achieve.snowflake.com/f93aa466-1e48-4236-a287-fbfb880b7dd8#acc.TD4Uz15Z" target="_blank">
                ❄️ SnowPro Core Certification
            </a><br>
            <span style="font-size:0.8em; color: #FFF3E6;">Snowflake | Valid: Aug 2025 – 2027</span>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.subheader("⬇️ Resume")
    # Centering the button slightly
    st.write("") 
    try:
        with open("portfolio/Resume_DikshaPhuloria.pdf", "rb") as file:
            st.download_button(
                label="📥 Download PDF",
                data=file,
                file_name="Resume_DikshaPhuloria.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        st.error("Resume PDF not found.")
