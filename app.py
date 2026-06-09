import streamlit as st
import pandas as pd
from recommender import recommend

# Page Config
st.set_page_config(
    page_title="Netflix Style Recommender",
    page_icon="🎬",
    layout="wide"
)

# Dark Theme CSS
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #ff4b4b;
}

.movie-card {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    margin-top: 10px;
}

.movie-card:hover {
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# Load Movies
movies = pd.read_csv("movies.csv")

# Header
st.markdown(
    "<h1 class='main-title'>🎬 Netflix Style Movie Recommender</h1>",
    unsafe_allow_html=True
)

st.write("")

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎥 Movies", len(movies))

with col2:
    st.metric("📂 Genres", 20)

with col3:
    st.metric("⭐ Recommendations", 5)

st.divider()

# Better Search
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

# Genre Filter
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

# Movie Selection
selected_movie = st.selectbox(
    "Choose Movie",
    filtered_movies["title"].values
)

# Recommend
if st.button("🍿 Recommend"):

    recommendations = recommend(
        selected_movie
    )

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i, movie in enumerate(recommendations):

        with cols[i]:

            st.markdown(
                f"""
                <div class="movie-card">
                    <h4>{movie}</h4>
                    <p>⭐ IMDb: N/A</p>
                </div>
                """,
                unsafe_allow_html=True
            )
