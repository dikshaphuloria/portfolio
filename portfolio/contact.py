import streamlit as st

# --- CUSTOM CSS FOR ANIMATED CONTACT CARDS ---
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

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    .contact-card {
        background-color: #FFF3E6;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        transition: all 0.4s ease;
        text-decoration: none !important;
        display: block;
        border: 2px solid transparent;
        animation: float 3s ease-in-out infinite;
        height: 130px; 
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .card-1 { animation-delay: 0s; }
    .card-2 { animation-delay: 0.3s; }
    .card-3 { animation-delay: 0.6s; }
    .card-4 { animation-delay: 0.9s; }

    .contact-card:hover {
        transform: scale(1.1) rotate(-2deg) !important;
        animation: none;
        background-color: white;
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
    }

    /* Instagram specific hover: Gradient Background + White Text/Icon */
    .insta-hover:hover { 
        background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%,#d6249f 60%,#285AEB 90%);
        border-color: transparent;
    }
    
    .insta-hover:hover .contact-label {
        color: white !important;
    }

    /* Adjusting icon size for the images */
    .contact-icon-img {
        width: 40px;
        height: 40px;
        margin-bottom: 10px;
        object-fit: contain;
    }

    .contact-label {
        color: #814141;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 0.75rem;
        transition: color 0.3s;
    }
    </style>

    <div class="playfair-title2";>
        🚀 Let's Connect!
    </div>
    """,
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <a href="mailto:dikshaphuloria@gmail.com" class="contact-card card-1 email-hover">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" class="contact-icon-img">
            <span class="contact-label">Email</span>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.write("")

with col2:
    st.markdown(
        """
        <a href="https://in.linkedin.com/in/diksha-phuloria-b4a0ab192" target="_blank" class="contact-card card-2 linkedin-hover">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" class="contact-icon-img">
            <span class="contact-label">LinkedIn</span>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.write("")

with col3:
    st.markdown(
        """
        <a href="https://github.com/dikshaphuloria" target="_blank" class="contact-card card-3 github-hover">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" class="contact-icon-img">
            <span class="contact-label">GitHub</span>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.write("")
