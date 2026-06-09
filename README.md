# 🎬 Netflix Style Movie Recommendation System

A **Machine Learning web application** built using **Python, Pandas, Scikit-Learn, and Streamlit** that recommends movies based on content similarity. Users can search for a movie and instantly receive five similar movie recommendations through an interactive Netflix-inspired interface.

---

## ✨ Features

- 🔍 Searchable movie selection
- 🎬 Content-based recommendation engine
- 🧠 Cosine Similarity algorithm
- 🎨 Modern Netflix-style UI
- 📊 Built with Machine Learning concepts
- ⚡ Interactive web application using Streamlit

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- MovieLens Dataset

---

## 📂 Project Structure

```
movie-recommender/
│
├── app.py
├── recommender.py
├── requirements.txt
│
└── data/
    ├── movies.csv
    └── ratings.csv
```

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python -m streamlit run app.py
```

The app will open automatically in your browser.

---

## 🧠 How It Works

1. Loads the MovieLens dataset.
2. Extracts movie genres.
3. Converts genres into numerical vectors using **CountVectorizer**.
4. Computes movie similarity using **Cosine Similarity**.
5. Displays the top 5 most similar movies based on the selected title.

---

## 📸 Preview

```
🎬 Netflix Style Movie Recommender

🔍 Search for a movie:
[ Interstellar ▼ ]

🍿 Recommend

⭐ The Martian
⭐ Gravity
⭐ Arrival
⭐ Moon
⭐ Ad Astra
```

---

## 📊 Dataset

This project uses the **MovieLens Small Dataset** provided by GroupLens Research.

https://grouplens.org/datasets/movielens/

---

## 🔮 Future Improvements

- 🎥 Movie posters using TMDB API
- ⭐ IMDb ratings
- 🎭 Genre badges
- 📅 Release year
- 🔍 Enhanced search experience
- 🚀 Deployment with Streamlit Cloud

---

## 👨‍💻 Author

**Jasmin Pucchakayala**

AI & Data Science Student

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

## 🚀 Live Demo

👉 (https://movie-recommendergit-j7n5r8mncp5hxa3kr2kdaf.streamlit.app/) 

Try the application online without installing anything.
