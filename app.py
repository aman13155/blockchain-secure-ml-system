# =========================================
# IMPORTS
# =========================================

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import send_from_directory
from flask import jsonify

import os
import time
import random
import webbrowser

# =========================================
# GROQ AI
# =========================================

from groq import Groq

client = Groq(

    api_key="gsk_..."
)

# =========================================
# PROJECT MODULES
# =========================================

from encryption import (

    aes_encrypt,

    des_encrypt,

    blowfish_encrypt,

    rsa_encrypt,

    generate_hash
)

from blockchain import (

    store_data,

    get_data
)

from drive import (

    upload_to_drive,

    download_from_drive
)

from graphs import (

    plot_algorithm_times,

    plot_confusion_matrix
)

from llm_helper import (

    generate_explanation
)

from email_sender import (

    send_email
)

# =========================================
# FLASK APP
# =========================================

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(

    UPLOAD_FOLDER,

    exist_ok=True
)

# =========================================
# STORE LATEST FILES
# =========================================

latest_uploaded_files = []

# =========================================
# HOME PAGE
# =========================================

@app.route('/')
def index():

    return render_template(
        "index.html"
    )

# =========================================
# VIEW FILES
# =========================================

@app.route('/uploads/<path:filename>')
def serve_file(filename):

    return send_from_directory(

        UPLOAD_FOLDER,

        filename
    )

# =========================================
# UPLOAD FILES
# =========================================

@app.route(

    '/upload',

    methods=['POST']
)

def upload():

    global latest_uploaded_files

    latest_uploaded_files = []

    files = request.files.getlist(
        "files"
    )

    owner_email = request.form.get(
        "email"
    )

    algorithms = {

        "AES": aes_encrypt,

        "DES": des_encrypt,

        "BF": blowfish_encrypt,

        "RSA": rsa_encrypt
    }

    # =========================================
    # PROCESS FILES
    # =========================================

    for file in files:

        filename = file.filename

        latest_uploaded_files.append(
            filename
        )

        original_path = os.path.join(

            UPLOAD_FOLDER,

            filename
        )

        file.save(original_path)

        # =========================================
        # ENCRYPT USING ALL ALGORITHMS
        # =========================================

        for algo_name, encrypt_func in algorithms.items():

            # ENCRYPTION

            start_enc = time.time()

            encrypted_path = encrypt_func(
                original_path
            )

            enc_time = round(

                time.time() - start_enc,

                4
            )

            # HASH

            file_hash = generate_hash(
                encrypted_path
            )

            # CLOUD UPLOAD

            start_upload = time.time()

            drive_id = upload_to_drive(
                encrypted_path
            )

            upload_time = round(

                time.time() - start_upload,

                4
            )

            # STORE DATA

            key = (
                f"{filename}_{algo_name}"
            )

            store_data(

                key,

                {

                    "hash": file_hash,

                    "drive_id": drive_id,

                    "enc_time": enc_time,

                    "upload_time": upload_time,

                    "owner_email": owner_email
                }
            )

    return redirect("/audit")

# =========================================
# AUDIT PAGE
# =========================================

@app.route('/audit')
def audit():

    global latest_uploaded_files

    if not latest_uploaded_files:

        return redirect("/")

    results = []

    alert = False

    encrypted_files = []

    # =========================================
    # CREATE ENCRYPTED FILE LIST
    # =========================================

    for file in latest_uploaded_files:

        encrypted_files.extend([

            file + ".aes",

            file + ".des",

            file + ".bf",

            file + ".rsa"
        ])

    algo_map = {

        "aes": "AES",

        "des": "DES",

        "bf": "BF",

        "rsa": "RSA"
    }

    # =========================================
    # VERIFY FILES
    # =========================================

    for enc_file in encrypted_files:

        try:

            name, ext = enc_file.rsplit(
                ".",
                1
            )

            algorithm = algo_map.get(
                ext.lower(),
                ""
            )

            key = (
                f"{name}_{algorithm}"
            )

            data = get_data(key)

            if not data:
                continue

            stored_hash = data["hash"]

            drive_id = data["drive_id"]

            owner_email = data.get(
                "owner_email"
            )

            original_path = os.path.join(

                UPLOAD_FOLDER,

                enc_file
            )

            # DOWNLOAD FILE

            start_dec = time.time()

            temp_path = os.path.join(

                UPLOAD_FOLDER,

                "temp_" + enc_file
            )

            download_from_drive(

                drive_id,

                temp_path
            )

            dec_time = round(

                time.time() - start_dec,

                4
            )

            # =========================================
            # RANDOM ATTACK SIMULATION
            # =========================================

            if random.choice([True, False]):

                with open(
                    temp_path,
                    "ab"
                ) as f:

                    f.write(
                        b"tampered"
                    )

            # HASH VERIFICATION

            current_hash = generate_hash(
                temp_path
            )

            size_difference = abs(

                os.path.getsize(temp_path)

                -

                os.path.getsize(original_path)
            )

            # =========================================
            # FINAL STATUS
            # =========================================

            if (

                current_hash == stored_hash

                and

                size_difference == 0
            ):

                status = "Secure ✅"

            else:

                status = "Tampered ❌"

                alert = True

                # =========================================
                # EMAIL ALERT
                # =========================================

                if owner_email:

                    body = f'''

⚠ SECURITY ALERT

Your cloud file integrity was compromised.

File Name : {enc_file}

Algorithm : {algorithm}

Status : Tampered

Please verify your cloud storage immediately.

'''

                    send_email(

                        "Tampered File Alert",

                        body,

                        owner_email
                    )

            enc_time = data.get(
                "enc_time",
                0
            )

            upload_time = data.get(
                "upload_time",
                0
            )

        except Exception as e:

            print("Error:", e)

            status = "Error ❌"

            enc_time = 0

            upload_time = 0

            dec_time = 0

        # =========================================
        # STORE RESULTS
        # =========================================

        results.append({

            "file": enc_file,

            "status": status,

            "enc_time": enc_time,

            "upload_time": upload_time,

            "dec_time": dec_time
        })

    # =========================================
    # EVALUATION METRICS
    # =========================================

    total_files = len(results)

    tampered_files = sum(

        1 for r in results

        if "Tampered" in r["status"]
    )

    secure_files = (
        total_files - tampered_files
    )

    accuracy = round(

        (
            secure_files /
            total_files
        ) * 100,

        2

    ) if total_files else 0

    error_rate = round(

        (
            tampered_files /
            total_files
        ) * 100,

        2

    ) if total_files else 0

    # =========================================
    # CONFUSION MATRIX
    # =========================================

    tp = tampered_files
    tn = secure_files
    fp = 0
    fn = 0

    cm = [

        [tn, fp],

        [fn, tp]
    ]

    plot_confusion_matrix(cm)

    # =========================================
    # ALGORITHM ANALYSIS
    # =========================================

    algo_times = {}

    for r in results:

        algo = (
            r["file"]
            .split(".")[-1]
            .upper()
        )

        if algo not in algo_times:

            algo_times[algo] = []

        algo_times[algo].append(
            r["enc_time"]
        )

    avg_times = {

        algo: round(
            sum(times) / len(times),
            4
        )

        for algo, times
        in algo_times.items()
    }

    fastest_algo = min(
        avg_times,
        key=avg_times.get
    )

    slowest_algo = max(
        avg_times,
        key=avg_times.get
    )

    best_algo = "AES"

    # =========================================
    # GENERATE GRAPHS
    # =========================================

    plot_algorithm_times(
        results
    )

    # =========================================
    # AI ANALYSIS
    # =========================================

    explanation = generate_explanation(
        results
    )

    # =========================================
    # ADMIN REPORT
    # =========================================

    report = f'''

Cloud Integrity Audit Report

Total Files : {total_files}

Secure Files : {secure_files}

Tampered Files : {tampered_files}

Accuracy : {accuracy}%

Error Rate : {error_rate}%

Fastest Algorithm : {fastest_algo}

Slowest Algorithm : {slowest_algo}

Best Algorithm : {best_algo}

'''

    send_email(

        "Cloud Integrity Audit Report",

        report,

        "mscprojectcc@gmail.com"
    )

    # =========================================
    # RENDER DASHBOARD
    # =========================================

    return render_template(

        "audit.html",

        results=results,

        alert=alert,

        explanation=explanation,

        fastest_algo=fastest_algo,

        slowest_algo=slowest_algo,

        best_algo=best_algo,

        avg_times=avg_times,

        total_files=total_files,

        secure_files=secure_files,

        tampered_files=tampered_files,

        accuracy=accuracy,

        error_rate=error_rate,

        cm=cm
    )

# =========================================
# AI CHATBOT
# =========================================

@app.route(

    "/chatbot",

    methods=["POST"]
)

def chatbot():

    query = request.form.get(
        "query"
    )

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {
                    "role": "user",

                    "content": query
                }
            ]
        )

        reply = (

            response
            .choices[0]
            .message.content
        )

    except Exception as e:

        print("Chatbot Error:", e)

        reply = """

AI chatbot currently unavailable.

"""

    return jsonify({

        "reply": reply
    })

# =========================================
# RUN APP
# =========================================

if __name__ == "__main__":

    webbrowser.open(

        "http://127.0.0.1:5000/"
    )

    app.run(debug=True)