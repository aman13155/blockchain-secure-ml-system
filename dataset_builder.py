import os
import pandas as pd
import random

from encryption import generate_hash

UPLOAD_FOLDER = "uploads"

def build_dataset_from_uploads():
    rows = []

    files = [
        f for f in os.listdir(UPLOAD_FOLDER)
        if f.endswith((".aes", ".des", ".bf", ".rsa"))
        and not f.startswith(("temp_", "ml_"))
    ]

    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file)

        # original hash
        original_hash = generate_hash(path)

        with open(path, "rb") as f:
            data = f.read()

        original_size = len(data)

        # -----------------------
        # 🔥 Simulate tampering
        # -----------------------
        tampered = random.choice([True, False])

        if tampered:
            # add random bytes (realistic tampering)
            extra = os.urandom(random.randint(5, 50))
            new_data = data + extra
            label = 1   # Tampered
        else:
            new_data = data
            label = 0   # Secure

        # -----------------------
        # Compute features
        # -----------------------
        current_hash = generate_hash_bytes(new_data)

        hash_match = 1 if current_hash == original_hash else 0

        new_size = len(new_data)
        size_diff = abs(new_size - original_size)

        time_diff = random.uniform(0, 5)  # more realistic

        rows.append([hash_match, size_diff, time_diff, label])

    df = pd.DataFrame(rows, columns=[
        "hash_match", "size_diff", "time_diff", "label"
    ])

    df.to_csv("dataset.csv", index=False)

    return df


# -----------------------
# Helper function (NEW)
# -----------------------
def generate_hash_bytes(data):
    import hashlib
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()