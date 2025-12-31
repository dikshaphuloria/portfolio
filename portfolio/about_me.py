import streamlit as st
from PIL import Image 
import streamlit.components.v1 as components
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
            Beyond data and code, I enjoy photography, exploring mountains, seas and traveling.
            These experiences connect me to the world, broaden my perspective, and help me better understand
            real-world problems and how thoughtful solutions can be developed.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:
        image = Image.open("images/me.jpg")
        st.image(image)

st.write("")


images = [
    ("images/p1.jpg", "Intricate Architecture"),
    ("images/p2.jpg", "Intricate Architecture"),
    ("images/p3.jpg", "Christmas Lights"),
    ("images/p4.jpg", "Golden Hour"),
    ("images/p5.jpg", "Calm by the Sea"),
    ("images/p6.jpg", "Moments in Motion"),
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
