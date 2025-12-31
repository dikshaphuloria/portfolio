import streamlit as st

# --- CUSTOM CSS FOR CREAM CARDS ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap');

    .playfair-title2 {
        font-family: 'Playfair Display', serif;
        font-size: 42px;
        font-style: italic;
        font-weight: 600;
        color: #FFF3E6;
        text-align: center;   
        margin-bottom: 30px;
    }

    .skills-card {
        background-color: #FFF3E6; /* Your cream secondary background color */
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #C89F8F; /* Your warm brown accent */
        height: 100%;
    }
    
    .skills-card h3 {
        color: #814141 !important; /* Your main background color used as text color here */
        margin-top: 0;
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
    }

    .skills-card ul {
        color: #333333; /* Darker text for readability on cream background */
        list-style-type: none;
        padding-left: 0;
    }

    .skills-card li {
        margin-bottom: 8px;
        font-size: 1rem;
        padding-left: 1.2rem;
        position: relative;
    }

    /* Custom bullet point */
    .skills-card li::before {
        content: "•";
        color: #C89F8F;
        font-weight: bold;
        position: absolute;
        left: 0;
    }
    </style>

    <div class="playfair-title2">
        Skills & Expertise
    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)

with col1:
    # --- Category 1 ---
    st.markdown("""
        <div class="skills-card">
            <h3>Programming & Querying</h3>
            <ul>
                <li>Python</li>
                <li>SQL</li>
                <li>R</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # --- Category 2 ---
    st.markdown("""
        <div class="skills-card">
            <h3>Data Science & ML</h3>
            <ul>
                <li>Exploratory Data Analysis (EDA)</li>
                <li>Feature Engineering</li>
                <li>Predictive Modeling</li>
                <li>Model Evaluation</li>
                <li>Causal Inference</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # --- Category 3 ---
    st.markdown("""
        <div class="skills-card">
            <h3>NLP & LLMs</h3>
            <ul>
                <li>Transformer Fine-Tuning</li>
                <li>LoRA & Few-shot Learning</li>
                <li>Interpretability</li>
                <li>Hugging Face</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # --- Category 4 ---
    st.markdown("""
        <div class="skills-card">
            <h3>Databases & Platforms</h3>
            <ul>
                <li>PostgreSQL, MySQL, Snowflake</li>
                <li>Streamlit</li>
                <li>ServiceNow</li>
                <li>Git & GitHub</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)