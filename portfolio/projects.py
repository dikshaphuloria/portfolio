import streamlit as st
from PIL import Image 

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
        text-align: center;
        margin-bottom: 30px;
    }
    </style>

    <div class="playfair-title">
       Academic Projects
    </div>
    """,
    unsafe_allow_html=True
)


with st.expander("🌱 Carbon-Aware Fine-Tuning of Language Models", expanded=True):
    st.write(
        """
        **Problem Statement:** When fine-tuning Transformer models, we often focus on accuracy and performance while overlooking the environmental impact, such as electricity consumption and resulting carbon emissions. This project seeks to bring attention to these overlooked costs by making environmental impact measurable, comparable, and transparent.
        
        **Goal:** To evaluate the trade-offs between model performance and carbon emissions across different fine-tuning strategies for question answering tasks.

        **Approach:**
        - Fine-tuned transformer models (DistilBERT, BERT, GPT, RoBERTa) using full fine-tuning, LoRA, and few-shot learning on SQuAD v2.0
        - Integrated CodeCarbon to track energy consumption (GPU/CPU/RAM energy usage) and CO₂ emissions during training.
        - Compared models using F1 score, Exact Match, training time, and emissions efficiency metrics.
        - Analyzed parameter-efficient methods to identify sustainable training strategies.
        """
    )
    st.markdown("**Tech Stack:** Python | Hugging Face | CodeCarbon | NLP | LLMs")
    st.link_button(
        "GitHub Repository",
        "https://github.com/shrutielangovan/CarbonEmissionsinFine-TuningLanguageModelS"
    )

with st.expander("📈 Financial Sentiment Feature Extraction with Sparse Autoencoders"):
    st.write(
        """
        **Problem Statement:** Large language models like GPT-2 act as black boxes, making it difficult to understand how they encode domain-specific information such as financial sentiment. This lack of interpretability reduces trust and control in high-stakes domains like finance.

        **Goal:** Extract interpretable financial sentiment features from GPT-2 internal activations.

        **Approach:**
        - Used GPT-2 to generate intermediate residual stream activations from financial text data (FinancialPhraseBank).
        - Extracted residual stream activations from GPT-2 layer 9
        - Trained Sparse Autoencoders (SAEs) with L1 regularization to enforce sparse, interpretable feature representations.
        - Experimented with multiple dictionary sizes (8× to 128×) to study sparsity and feature specificity.
        - Evaluated extracted features using firing rate analysis, financial relevance scoring, and top-activating token inspection.
        - Identified challenges such as overactive features and limited data diversity to guide future improvements.
        """
    )
    st.markdown("**Tech Stack:** Python | GPT-2 | Sparse Autoencoders | Interpretability | Pandas")
    st.link_button(
        "GitHub Repository",
        "https://github.com/mallick20/financial-interpretability"
    )

with st.expander("Anime & Manga Recommendation Platform"):
    st.write(
        """
        **Problem Statement:** Anime and manga platforms often lack personalized discovery, structured user feedback, and flexible search capabilities, making it difficult for users to find content aligned with their preferences.
        
        **Goal:** To build a data-driven platform that enables users to browse, review, and discover anime and manga content using structured filters, user behavior, and natural language queries.

        **Approach:**
        - Designed a relational PostgreSQL database to store users, content, reviews, and interaction logs.
        - Built a Streamlit-based interface with search, filtering, sorting, and pagination for efficient browsing.
        - Implemented a rule-based shuffle recommender using user preferences, ratings, genres, and popularity.
        - Integrated an OpenAI-powered natural language assistant to parse user queries into structured filters and generate SQL-based recommendations.
        """
    )
    st.markdown("**Tech Stack:** Python | Streamlit | PostgreSQL | SQLAlchemy | OpenAI API")
    
    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital@1&display=swap');

    .playfair-title2 {
        font-family: 'Playfair Display', serif;
        font-size: 30px;
        font-style: italic;
        font-weight: 400;
        margin-bottom: 20px;
        text-align: center;   
        width: 100%;         
    }
    </style>

    <div class="playfair-title2">
        A Glimpse Of the Website
    </div>
    """,
    unsafe_allow_html=True
    )
 
    col1, col2, col3 = st.columns(3)
    with col1:
        image = Image.open("portfolio/images/anime1.png")
        st.image(image)
    with col2:
        image1 = Image.open("portfolio/images/anime2.png")
        st.image(image1)
    with col3:
        image2 = Image.open("portfolio/images/anime3.png")
        st.image(image2)


    st.link_button(
        "GitHub Repository",
        "https://github.com/mallick20/anime-guru"
    )

with st.expander("Renewable Energy Consumption Analysis & Visualization"):
    st.write(
        """
        **Problem Statement:** Understanding global renewable energy adoption trends requires integrating economic, population, and energy datasets, which are often fragmented.
        
        **Goal:** To analyze renewable energy consumption patterns and identify relationships between GDP, electrification, and renewable adoption.

        **Approach:**
        - Cleaned, merged, and analyzed multi-country energy and economic datasets.
        - Enriched datasets using external APIs for population and geospatial data.
        - Performed exploratory data analysis to identify trends and regional patterns.
        - Built interactive visualizations to communicate sustainability insights.
        """
    )
    st.markdown("**Tech Stack:** Python | Pandas | Matplotlib | APIs (Kaggle, Ninja API)")
    st.link_button(
        "Pages Link",
        "https://dikshaphuloria.github.io/Renewable_Energy_Consumption_Analysis/DataVisualization.html"
    )
