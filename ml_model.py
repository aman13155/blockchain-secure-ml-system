import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

from dataset_builder import build_dataset_from_uploads

MODEL_FILE = "model.pkl"


def train_model():
    df = build_dataset_from_uploads()

    X = df[["hash_match", "size_diff", "time_diff"]]
    y = df["label"]

    # ✅ Split data (IMPORTANT FIX)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # ✅ Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # ✅ Test on unseen data
    preds = model.predict(X_test)

    accuracy = accuracy_score(y_test, preds)
    cm = confusion_matrix(y_test, preds)

    joblib.dump(model, MODEL_FILE)

    return model, accuracy, cm


def load_model():
    return joblib.load(MODEL_FILE)


def predict_status(hash_match, size_diff, time_diff):
    model = load_model()

    input_data = pd.DataFrame(
        [[hash_match, size_diff, time_diff]],
        columns=["hash_match", "size_diff", "time_diff"]
    )

    pred = model.predict(input_data)

    return "Secure ✅" if pred[0] == 0 else "Tampered ❌"