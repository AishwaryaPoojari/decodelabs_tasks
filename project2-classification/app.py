
from flask import Flask, render_template, request
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

app = Flask(__name__)

iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

models = {
    "K-Nearest Neighbors": make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    ),
    "Decision Tree": DecisionTreeClassifier(random_state=42)
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    results[name] = round(accuracy_score(y_test, predictions) * 100, 1)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    measurements = ["5.1", "3.5", "1.4", "0.2"]
    selected_model = "K-Nearest Neighbors"

    if request.method == "POST":
        try:
            measurements = [
                request.form["sepal_length"],
                request.form["sepal_width"],
                request.form["petal_length"],
                request.form["petal_width"]
            ]
            values = [float(value) for value in measurements]

            if any(value <= 0 or value > 10 for value in values):
                raise ValueError

            selected_model = request.form.get(
                "model", "K-Nearest Neighbors"
            )
            if selected_model not in models:
                selected_model = "K-Nearest Neighbors"

            predicted_class = models[selected_model].predict([values])[0]
            prediction = class_names[predicted_class].title()

        except (ValueError, KeyError):
            error = "Enter four valid measurements greater than 0 and at most 10 cm."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        measurements=measurements,
        models=results,
        selected_model=selected_model,
        sample_count=len(X),
        train_count=len(X_train),
        test_count=len(X_test)
    )

if __name__ == "__main__":
    app.run(debug=True)
