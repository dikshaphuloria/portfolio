import streamlit as st
from PIL import Image 
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import base64


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap');

    .playfair-title {
        font-family: 'Playfair Display', serif;
        font-size: 42px;
        font-style: italic;
        font-weight: 600;
        color: #FFF3E6; 
        margin-bottom: 30px;
    }
    </style>

    <div class="playfair-title">
        Hi there, I’m Diksha Phuloria. Great to have you here!
    </div>
    """,
    unsafe_allow_html=True
)



st.write("")
my_container = st.container()

#background to the container
st.markdown(
    """
    <style>
    .cream-box {
        background-color: #f5f1e8; /* cream */
        color: #000000;           /* black text */
        padding: 20px;
        border-radius: 12px;
    }

    .cream-box h2,
    .cream-box p {
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with my_container:
    col1, col2 = st.columns([2.5, 1.5])

    with col1:
        st.markdown(
            """
            <div class="cream-box";>
            <p style="font-size:28px";>
            <b>
            I am a Data Science graduate student with a strong academic foundation exploring the world of data one dataset at a time.
            </b>
            </p>
            </div>
            <br>

            <div class="cream-box"; style="font-size:22px; line-height:1.6;">
            <p>
            What I bring to the table is a deep curiosity to learn, the ability to adapt to evolving technologies,
            and a strong respect for fundamental concepts. I enjoy understanding how systems work from the scratch
            and applying that knowledge to solve meaningful problems.
            </p>

            <p>
            My interests lie in artificial intelligence, large language models, data analysis, and building applications</b>,
            particularly in building solutions that are both effective and responsible.
            </p>
            </div>
            <br>

            <div div class="cream-box"; style="font-size:22px; line-height:1.6;">
            <p>
            Beyond data and code, I enjoy puzzles, photography, exploring mountains, seas and traveling.
            These experiences connect me to the world, broaden my perspective, and help me better understand
            real-world problems and how thoughtful solutions can be developed.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.write("")


    with col2:
        image = Image.open("portfolio/images/me.jpg")
        st.image(image)

st.write("")


images = [
    ("portfolio/images/p1.jpg", "Intricate Architecture"),
    ("portfolio/images/p2.jpg", "Intricate Architecture"),
    ("portfolio/images/p3.jpg", "Christmas Lights"),
    ("portfolio/images/p4.jpg", "Golden Hour"),
    ("portfolio/images/p5.jpg", "Calm by the Sea"),
    ("portfolio/images/p6.jpg", "Moments in Motion"),
]

def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def render_image_carousel(images):
    html = """
    <style>
    .carousel-container {
        display: flex;
        overflow-x: auto;
        gap: 16px;
        padding: 10px;
        scroll-behavior: smooth;
    }

    .carousel-container::-webkit-scrollbar {
        height: 10px;
    }

    .carousel-container::-webkit-scrollbar-thumb {
        background-color: #666;
        border-radius: 10px;
    }

    .carousel-item {
        flex: 0 0 auto;
        width: 300px;
        height: 380px;
        border-radius: 12px;
        overflow: hidden;
        position: relative;
        box-shadow: 0 4px 12px rgba(0,0,0,0.35);
        transition: transform 0.25s ease;
    }

    .carousel-item:hover {
        transform: scale(1.05);
    }

    .carousel-item img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .carousel-caption {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 8px;
        background: linear-gradient(
            180deg,
            rgba(0,0,0,0.0),
            rgba(0,0,0,0.7)
        );
        color: #fff;
        font-size: 14px;
        text-align: center;
    }
    </style>

    <div class="carousel-container">
    """

    for img_path, caption in images:
        img_base64 = image_to_base64(img_path)
        html += f"""
        <div class="carousel-item">
            <img src="data:image/jpeg;base64,{img_base64}" alt="{caption}">
            <div class="carousel-caption">{caption}</div>
        </div>
        """

    html += "</div>"
    return html

st.write(" ")

with st.container(border=True):
    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital@1&display=swap');

    .playfair-title2 {
        font-family: 'Playfair Display', serif;
        font-size: 35px;
        font-style: italic;
        font-weight: 400;
        margin-bottom: 20px;
        text-align: center;   
        width: 100%;         
    }
    </style>

    <div class="playfair-title2">
        📸 A Glimpse Beyond Data
    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .subheader-align {
            text-align: center;   
            width: 100%;  
        }
        </style>

        <div class="subheader-align";>
            Photography and travel help me explore different perspectives and inspire how I approach things.
        </div>
        """,
        unsafe_allow_html=True
    )

    components.html(render_image_carousel(images), height=400, scrolling=False)


#------------------------------------------------------------------------------
#Game Section
#------------------------------------------------------------------------------
st.write("")
st.markdown(
            """
            <div class="cream-box";>
            <p style="font-size:20px";>
            <b>
            I enjoy games that begin with random guessing, but gradually reveal how a few simple rules make the solution feel natural, just like the one below. Give it a try!
            </b>
            </p>
            </div>""", unsafe_allow_html=True
)

# Initialize session state
if "answer" not in st.session_state:
    st.session_state.answer = np.random.randint(1, 101)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "won" not in st.session_state:
    st.session_state.won = False

def restart_game():
    st.session_state.answer = np.random.randint(1, 101)
    st.session_state.attempts = 0
    st.session_state.won = False

# --- CSS FIXES FOR DARK BACKGROUNDS ---
st.markdown(f"""
    <style>

    /* Title & Text Colors */
    .game-title {{
        font-family: 'Serif';
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0px;
    }}
    
    .game-subtitle {{
        text-align: center;
        font-size: 1.1rem;
    }}

    /* Attempt Badge */
    .attempt-badge {{
        background: #814141;
        color: #FFF3E6;
        padding: 8px 20px;
        border-radius: 50px;
        font-weight: bold;
        text-align: center;
        width: 160px;
        margin: 0 auto 1rem auto;
    }}

    /* Fix for the "Higher/Lower" feedback boxes */
    .stAlert {{
        background-color: rgba(200, 159, 143, 0.2) !important;
        color: #814141 !important;
        border: 1px solid #C89F8F !important;
    }}

    /* Make the input text dark so it's visible on the cream input */
    /* Dark input field */

    input[type="number"] {{
    background-color: #3d1f1f !important;
    color: #ffffff !important;
    border: 1px solid #6b3a3a !important;
    border-radius: 8px !important;
    }}

    /* Remove number input arrows if desired */

    input[type="number"]::-webkit-inner-spin-button,

    input[type="number"]::-webkit-outer-spin-button {{
    opacity: 0.5;
    }}


    /* Placeholder text color */

    input[type="number"]::placeholder {{
    color: #aaaaaa !important;
    }}
            
    .win-message {{
        text-align: center;
        font-style: italic;
        color: #ccc;
        padding: 0.5rem 0 1rem 0;
        font-size: 0.95rem;
    }}
    </style>
""", unsafe_allow_html=True)

# --- UI STRUCTURE ---
# We wrap everything in a div called "game-card" so the CSS above can find it

with st.container(border=True):

    st.markdown('<div class="game-title">✨ Mystery Number</div>', unsafe_allow_html=True)
    st.markdown('<div class="game-subtitle">A game of intuition.</div>', unsafe_allow_html=True)

    # Attempt Counter
    st.markdown(f'<div class="attempt-badge">🎯 Attempt : {st.session_state.attempts}</div>', unsafe_allow_html=True)

    # Guessing Area
    col1, col2 = st.columns([3, 1])
    with col1:
        user_input = st.number_input(
                    "Your guess",
                    min_value=1, max_value=100, step=1,
                    label_visibility="collapsed",
                    placeholder="Enter your guess..."
                    )
    with col2:
        check = st.button("Guess", use_container_width=True, type="primary")

    # Logic
    if check and not st.session_state.won:
        st.session_state.attempts += 1
        if user_input == st.session_state.answer:
            st.session_state.won = True
            st.balloons()
            st.success(f"🏆 Correct! It was {st.session_state.answer}.")
            st.markdown(
                '<div class="win-message">A systematic approach leads to victory in just few attempts 😄</div>',
                unsafe_allow_html=True

                )
        elif user_input < st.session_state.answer:
            st.info("🔼 **Higher!** Keep climbing.")
        else:
            st.warning("🔽 **Lower!** Bring it down.")

    st.markdown('</div>', unsafe_allow_html=True)

    # Footer (Outside the card)
    st.button("🎮 Play Again", on_click=restart_game, type="primary", use_container_width=True)