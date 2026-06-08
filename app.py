import streamlit as st
import pandas as pd

from recommender import recommend

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
    color: white;
}

.stSelectbox label {
    color: white !important;
    font-size: 18px;
}

.movie-card{
    background-color:#1c1f26;
    padding:20px;
    border-radius:15px;
    margin:10px;
    text-align:center;
    color:white;
    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Load Data ----------

movies = pd.read_csv("data/movies.csv")

# ---------- Header ----------

st.markdown(
    "<h1>🎬 Netflix Style Movie Recommender</h1>",
    unsafe_allow_html=True
)

st.write("")

st.info(
    "Select your favorite movie and discover similar movies."
)

# ---------- Sidebar ----------

st.sidebar.title("🎥 About")

st.sidebar.write("""
AI & Data Science Mini Project

Built using:
- Python
- Pandas
- Scikit-Learn
- Streamlit
""")

# ---------- Movie Selection ----------

selected_movie = st.selectbox(
    "Choose a Movie",
    movies["title"].values
)

st.write("")

# ---------- Recommendation ----------

if st.button("🍿 Recommend Movies"):

    recommendations = recommend(
        selected_movie
    )

    st.subheader("You may also like")

    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for i in range(len(recommendations)):

        with cols[i]:

            st.markdown(
                f"""
                <div class="movie-card">
                <h3>🎬</h3>
                <p>{recommendations[i]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown(
    """
    <div class="footer">
    Made with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)