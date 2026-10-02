import os
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

MODEL_FILE = "model.pkl"

def create_basic_model():
    # Only used if no dataset available
    data = {
        "hash_match": [1, 1, 0, 0],
        "size_diff": [0, 0, 10, 20],
        "time_diff": [0, 0, 1, 2],
        "label": [0, 0, 1, 1]
    }

    df = pd.DataFrame(data)

    X = df[["hash_match", "size_diff", "time_diff"]]
    y = df["label"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_FILE)

    return model


def load_or_create_model():
    if not os.path.exists(MODEL_FILE):
        return create_basic_model()
    return joblib.load(MODEL_FILE)