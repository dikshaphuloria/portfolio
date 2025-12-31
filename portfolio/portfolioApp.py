import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

if __name__ == '__main__':
    # ---------------- PAGE CONFIG ----------------
    st.set_page_config(
        page_title="Diksha Phuloria",
        page_icon=":woman_technologist:",
        layout="wide")
    
    st.markdown("""
    <style>
    [data-testid="stSidebar"] * {
        color: #3A2F2A !important;  /* dark brown */
    }
    </style>
    """, unsafe_allow_html=True)
    
    pages =[
        st.Page("about_me.py", title="About Me", icon=":material/face_3:"),
        st.Page("resume.py", title="Education & Experience", icon=":material/file_open:"),
        st.Page("skill.py", title="Skills Set", icon=":material/widgets:"),
        st.Page("projects.py", title="Projects", icon=":material/deployed_code:"),
        st.Page("contact.py", title="Contact", icon=":material/contact_page:")
    ]
    
    image = Image.open("images/goal.png")
    st.sidebar.image(image)

    page = st.navigation(pages)
    page.run()
    


