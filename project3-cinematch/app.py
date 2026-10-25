from flask import Flask, render_template, request
import pandas as pd
from recommender import recommend_movies

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    genres = [
        "Action", "Adventure", "Animation", "Comedy",
        "Crime", "Drama", "Family", "Horror",
        "Mystery", "Romance", "Sci-Fi", "Thriller",
        "Musical", "Biography"
    ]

    recommendations = []
    selected_genres = []

    if request.method == "POST":
        selected_genres = request.form.getlist("genres")

        if selected_genres:
            recommendations = recommend_movies(
                selected_genres,
                number_of_recommendations=6
            )

    movies = pd.read_csv("movies.csv")

    return render_template(
        "index.html",
        genres=genres,
        selected_genres=selected_genres,
        recommendations=recommendations,
        movie_count=len(movies)
    )


if __name__ == "__main__":
    app.run(debug=True)