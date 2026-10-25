
# Project 2: Data Classification Using AI
# DecodeLabs AI Internship

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# 1. Load and explore the dataset
iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names

print("=== IRIS DATASET ===")
print("Samples:", X.shape[0])
print("Features:", X.shape[1])
print("Feature names:", iris.feature_names)
print("Classes:", class_names)

# 2. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 3. Define two classification models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    )
}

# 4. Train, evaluate, and compare models
for model_name, model in models.items():
    print(f"\n=== {model_name} ===")

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print("Test accuracy:", f"{accuracy * 100:.2f}%")

    print("\nClassification report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=class_names,
            zero_division=0
        )
    )

    print("Confusion matrix (rows = actual, columns = predicted):")
    print(confusion_matrix(y_test, predictions))

    # Cross-validation is performed on the training data only
    cv_scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=5,
        scoring="accuracy"
    )
    print("5-fold training cross-validation scores:", cv_scores.round(3))
    print("Mean cross-validation accuracy:", f"{cv_scores.mean() * 100:.2f}%")

# 5. Demonstrate prediction with new flower measurements
print("\n=== NEW FLOWER PREDICTION ===")
print("Enter four measurements in this order:")
print("Sepal length, sepal width, petal length, petal width (cm)")

try:
    measurements = [
        float(input("Sepal length (cm): ")),
        float(input("Sepal width (cm): ")),
        float(input("Petal length (cm): ")),
        float(input("Petal width (cm): "))
    ]

    # Use the Decision Tree model for this demonstration
    decision_tree = models["Decision Tree"]
    predicted_class = decision_tree.predict([measurements])[0]

    print("Predicted flower species:", class_names[predicted_class])

except ValueError:
    print("Please enter valid numeric measurements.")
