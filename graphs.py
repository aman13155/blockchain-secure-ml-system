import matplotlib

# -----------------------
# FIX FOR FLASK
# -----------------------

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from collections import defaultdict

import os

# -----------------------
# PERFORMANCE GRAPHS
# -----------------------

def plot_algorithm_times(results):

    # CREATE STATIC FOLDER

    os.makedirs(
        "static",
        exist_ok=True
    )

    # -----------------------
    # GROUP DATA
    # -----------------------

    data = defaultdict(

        lambda: {

            "enc": [],

            "upload": [],

            "dec": []
        }
    )

    for r in results:

        algo = (
            r["file"]
            .split(".")[-1]
            .upper()
        )

        data[algo]["enc"].append(
            r["enc_time"]
        )

        data[algo]["upload"].append(
            r["upload_time"]
        )

        data[algo]["dec"].append(
            r["dec_time"]
        )

    algos = list(data.keys())

    # -----------------------
    # AVERAGE VALUES
    # -----------------------

    enc_avg = [

        round(

            sum(data[a]["enc"]) /

            len(data[a]["enc"]),

            4
        )

        for a in algos
    ]

    upload_avg = [

        round(

            sum(data[a]["upload"]) /

            len(data[a]["upload"]),

            4
        )

        for a in algos
    ]

    dec_avg = [

        round(

            sum(data[a]["dec"]) /

            len(data[a]["dec"]),

            4
        )

        for a in algos
    ]

    # -----------------------
    # ENCRYPTION GRAPH
    # -----------------------

    plt.figure(figsize=(7,5))

    plt.bar(
        algos,
        enc_avg
    )

    plt.title(
        "Encryption Time Comparison"
    )

    plt.xlabel(
        "Algorithm"
    )

    plt.ylabel(
        "Time (seconds)"
    )

    plt.savefig(
        "static/enc.png"
    )

    plt.close()

    # -----------------------
    # UPLOAD GRAPH
    # -----------------------

    plt.figure(figsize=(7,5))

    plt.bar(
        algos,
        upload_avg
    )

    plt.title(
        "Upload Time Comparison"
    )

    plt.xlabel(
        "Algorithm"
    )

    plt.ylabel(
        "Time (seconds)"
    )

    plt.savefig(
        "static/upload.png"
    )

    plt.close()

    # -----------------------
    # DOWNLOAD GRAPH
    # -----------------------

    plt.figure(figsize=(7,5))

    plt.bar(
        algos,
        dec_avg
    )

    plt.title(
        "Download Time Comparison"
    )

    plt.xlabel(
        "Algorithm"
    )

    plt.ylabel(
        "Time (seconds)"
    )

    plt.savefig(
        "static/dec.png"
    )

    plt.close()

# -----------------------
# CONFUSION MATRIX GRAPH
# -----------------------

def plot_confusion_matrix(cm):

    os.makedirs(
        "static",
        exist_ok=True
    )

    plt.figure(figsize=(5,5))

    plt.imshow(
        cm,
        cmap="Blues"
    )

    plt.title(
        "Confusion Matrix"
    )

    plt.colorbar()

    labels = [

        "Secure",

        "Tampered"
    ]

    plt.xticks(
        [0,1],
        labels
    )

    plt.yticks(
        [0,1],
        labels
    )

    plt.xlabel(
        "Predicted"
    )

    plt.ylabel(
        "Actual"
    )

    # -----------------------
    # MATRIX VALUES
    # -----------------------

    for i in range(2):

        for j in range(2):

            plt.text(

                j,

                i,

                cm[i][j],

                ha="center",

                va="center",

                color="black",

                fontsize=16
            )

    plt.savefig(
        "static/confusion.png"
    )

    plt.close()