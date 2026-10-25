# CineMatch — Movie Recommendation System

## Project Overview
CineMatch is a content-based movie recommendation system developed as part of the DecodeLabs AI Internship, Week 3 project.

The application recommends movies based on users' selected genres and interests. It uses text-processing and similarity techniques to rank movies according to their relevance to the selected preferences.

## Objectives
- Collect movie preferences from users.
- Analyse movie genres and descriptions.
- Calculate similarity between user preferences and movie information.
- Display ranked movie recommendations.
- Provide an interactive web interface.

## Technologies Used
- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSS
- JavaScript

## Recommendation Method
The system uses TF-IDF to convert movie information into numerical vectors and cosine similarity to compare user preferences with movie data.

Movies are ranked according to their calculated similarity scores.

## Project Structure

```text
DecodeLabs_Project3/
├── app.py
├── recommender.py
├── movies.csv
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Installation

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal in the project directory.
3. Run the application:

```bash
python app.py
```

4. Open your browser and visit:

```text
http://127.0.0.1:5000
```

5. Select your preferred movie genres.
6. Click **Find my movies** to view recommendations.

## Dataset
The project uses a local CSV dataset named `movies.csv`, containing movie titles, genres, descriptions, and ratings.

## Project Outcome
CineMatch demonstrates the fundamental concepts of content-based recommendation, text processing, similarity calculation, and web application development.

## Internship
**Organisation:** DecodeLabs  
**Project:** Project 3 — AI Recommendation Logic