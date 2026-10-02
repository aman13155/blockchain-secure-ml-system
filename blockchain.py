import json
import os

FILE = "blockchain_data.json"


# -----------------------
# LOAD DATA (SAFE)
# -----------------------
def load_data():
    if not os.path.exists(FILE) or os.path.getsize(FILE) == 0:
        return {}

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}


# -----------------------
# SAVE DATA
# -----------------------
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# -----------------------
# STORE DATA (NEW FORMAT)
# -----------------------
def store_data(filename, data):
    """
    data = {
        "hash": "...",
        "drive_id": "...",
        "enc_time": ...,
        "upload_time": ...
    }
    """
    db = load_data()
    db[filename] = data
    save_data(db)


# -----------------------
# GET DATA
# -----------------------
def get_data(filename):
    db = load_data()
    return db.get(filename)