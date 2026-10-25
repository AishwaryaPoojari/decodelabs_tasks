# Project 2: Data Classification Using AI

## DecodeLabs AI Internship

### Project Overview
This project demonstrates a basic supervised machine-learning classification model. It uses the Iris flower dataset to predict the species of a flower from its measurements.

### Dataset
The Iris dataset contains 150 samples, 4 numerical features, and 3 flower species:
- Setosa
- Versicolor
- Virginica

The features are sepal length, sepal width, petal length, and petal width.

### Methodology
1. Load and inspect the Iris dataset.
2. Split the data into training (80%) and testing (20%) sets.
3. Train a Decision Tree classifier.
4. Predict flower species for the test data.
5. Evaluate the model using accuracy and a classification report.
6. Predict the species of a new sample flower.

### Tools and Technologies
- Python
- scikit-learn

### Result
The model achieved **100% accuracy on the 30-sample test set** for the selected train/test split. It predicted the example flower as Setosa.

### How to Run
Install scikit-learn:

```bash
python -m pip install scikit-learn
```

Run the program:

```bash
python classification_model.py
```

### Learning Outcome
This project provides practice in dataset handling, train/test splitting, supervised learning, model training, classification, and evaluation.
