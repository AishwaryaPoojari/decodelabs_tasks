import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_movies():
    return pd.read_csv("movies.csv")


def recommend_movies(selected_genres, number_of_recommendations=6):
    movies = load_movies()

    if not selected_genres:
        return []

    # Combine each movie's genres and description.
    movie_features = (
        movies["genres"].fillna("") + " " +
        movies["description"].fillna("")
    )

    # Convert text into numerical vectors.
    vectorizer = TfidfVectorizer(stop_words="english")
    movie_vectors = vectorizer.fit_transform(movie_features)

    # Convert the user's selected genres into text.
    user_preferences = " ".join(selected_genres)

    user_vector = vectorizer.transform([user_preferences])

    # Calculate similarity between preferences and movies.
    similarities = cosine_similarity(
        user_vector, movie_vectors
    ).flatten()

    # Rank movies by similarity.
    movies = movies.copy()
    movies["similarity"] = similarities

    recommendations = movies.sort_values(
        by=["similarity", "rating"],
        ascending=[False, False]
    )

    # Return only movies with a meaningful genre match.
    recommendations = recommendations[
        recommendations["similarity"] > 0
    ].head(number_of_recommendations)

    results = []

    for _, movie in recommendations.iterrows():
        results.append({
            "title": movie["title"],
            "genres": movie["genres"],
            "description": movie["description"],
            "rating": float(movie["rating"]),
            "similarity": round(
                float(movie["similarity"]) * 100, 1
            )
        })

    return results