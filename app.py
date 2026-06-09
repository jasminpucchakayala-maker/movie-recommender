import streamlit as st
import pandas as pd
from recommender import recommend

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Netflix Style Recommender",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

/* Background */

.stApp {
    background: linear-gradient(to bottom, #141414, #000000);
}

/* Title */

.main-title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #E50914;
    margin-bottom: 20px;
}

/* Subtitle */

.subtitle {
    text-align: center;
    color: #bbbbbb;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Metric Cards */

[data-testid="stMetric"] {
    background-color: #1f1f1f;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #333;
}

[data-testid="stMetricLabel"] {
    color: white !important;
}

[data-testid="stMetricValue"] {
    color: #E50914 !important;
    font-size: 35px !important;
}

/* Inputs */

.stTextInput input {
    background-color: #262730;
    color: white !important;
    border-radius: 10px;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #262730;
    border-radius: 10px;
}

/* Button */

.stButton button {
    background-color: #E50914;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 220px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    background-color: #ff1f1f;
}

/* Recommendation Cards */

.movie-card {
    background-color: #1f1f1f;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    min-height: 150px;
    box-shadow: 0px 0px 12px rgba(255,0,0,0.25);
}

.movie-card:hover {
    transform: scale(1.05);
}

/* Headers */

h2, h3 {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# LOAD DATA
# -----------------------------------

movies = pd.read_csv("movies.csv")

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown(
    "<h1 class='main-title'>🎬 Netflix Style Movie Recommender</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Find movies you'll love with AI-powered recommendations</p>",
    unsafe_allow_html=True
)

# -----------------------------------
# DASHBOARD METRICS
# -----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎥 Movies", len(movies))

with col2:
    genres_count = len(
        set("|".join(movies["genres"]).split("|"))
    )
    st.metric("🎭 Genres", genres_count)

with col3:
    st.metric("⭐ Recommendations", 5)

st.divider()

# -----------------------------------
# SEARCH
# -----------------------------------

search = st.text_input(
    "🔍 Search Movie"
)

filtered_movies = movies[
    movies["title"].str.contains(
        search,
        case=False,
        na=False
    )
]

# -----------------------------------
# GENRE FILTER
# -----------------------------------

genre_list = ["All"] + sorted(
    list(
        set(
            "|".join(
                movies["genres"]
            ).split("|")
        )
    )
)

selected_genre = st.selectbox(
    "🎭 Filter by Genre",
    genre_list
)

if selected_genre != "All":

    filtered_movies = filtered_movies[
        filtered_movies["genres"].str.contains(
            selected_genre,
            case=False,
            na=False
        )
    ]

# -----------------------------------
# MOVIE SELECTOR
# -----------------------------------

if len(filtered_movies) > 0:

    selected_movie = st.selectbox(
        "🎬 Choose Movie",
        filtered_movies["title"].values
    )

    if st.button("🍿 Recommend Movies"):

        recommendations = recommend(
            selected_movie
        )

        st.markdown(
            "<h2>🍿 Recommended Movies</h2>",
            unsafe_allow_html=True
        )

        cols = st.columns(5)

        for i, movie in enumerate(recommendations):

            with cols[i]:

                st.markdown(
                    f"""
                    <div class="movie-card">
                        <h4>{movie}</h4>
                        <p>⭐ Similar Movie</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

else:

    st.warning(
        "No movies found. Try another search."
    )
