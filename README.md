blockchain-secure-ml-system








A Flask-based cloud security application for file encryption, cloud storage, integrity verification, tamper detection, audit reporting, and AI-assisted security analysis.

The system encrypts uploaded files using multiple cryptographic algorithms, stores encrypted copies in Google Drive, records integrity metadata in a local JSON-based ledger, and later verifies whether the stored files have been modified.

Project type: Academic / MCA Project
Primary stack: Python, Flask, Google Drive API, PyCryptodome, Scikit-learn, Matplotlib, Groq LLM

📌 Overview

Cloud-stored files can be modified, corrupted, or tampered with after upload. This project provides a security workflow that combines:

🔒 Multi-algorithm file encryption

#️⃣ SHA-256 integrity hashing

☁️ Google Drive cloud storage

⛓️ Blockchain-style metadata ledger

🛡️ Tamper detection

📧 Email security alerts

📊 Audit dashboard and performance graphs

🤖 Machine-learning based integrity classification

🧠 LLM-powered security analysis and chatbot

The application provides a web interface where a user can upload one or more files and provide an owner email address. Each file is encrypted using AES, DES, Blowfish, and RSA, uploaded to Google Drive, and associated with integrity metadata.

✨ Key Features

🔒 1. Multi-Algorithm Encryption

The system supports four encryption methods:

Algorithm

Purpose

AES

Symmetric encryption

DES

Symmetric encryption comparison

Blowfish

Symmetric encryption comparison

RSA

Public-key encryption demonstration

Each uploaded file is processed with all four algorithms.

#️⃣ 2. SHA-256 Integrity Verification

A SHA-256 hash is generated for every encrypted file.

During an audit:

The encrypted file is downloaded from Google Drive.

A new SHA-256 hash is calculated.

The downloaded file size is compared with the stored file size.

The current hash and size are compared with the original values.

The file is classified as Secure or Tampered.

☁️ 3. Google Drive Integration

Encrypted files are uploaded to Google Drive using PyDrive.

The application records the Google Drive file ID along with:

SHA-256 hash

Encryption time

Upload time

Owner email

⛓️ 4. Integrity Metadata Ledger

blockchain.py maintains a local JSON-based ledger in blockchain_data.json.

For each encrypted file, the ledger stores metadata such as:

{
    "hash": "SHA-256 hash",
    "drive_id": "Google Drive file ID",
    "enc_time": 0.01,
    "upload_time": 2.5,
    "owner_email": "owner@example.com"
}

Important: In the current implementation this is a blockchain-style/local integrity ledger, not a decentralized blockchain network or smart contract.

🛡️ 5. Tamper Detection

The audit process checks whether the downloaded cloud copy differs from the stored integrity information.

A file is marked:

Secure ✅ — hash and size match

Tampered ❌ — hash or size differs

Error ❌ — verification could not be completed

The current academic demonstration also contains a random tampering simulation to demonstrate the detection workflow.

📧 6. Email Alerts

When tampering is detected, the system can send an email notification to the file owner.

An administrative audit report can also be generated and emailed after verification.

📊 7. Audit Dashboard

The Flask dashboard displays:

Total files

Secure files

Tampered files

Error rate

Fastest encryption algorithm

Slowest encryption algorithm

Algorithm comparison

Encryption time

Google Drive upload time

Download/verification time

Confusion matrix

Performance graphs

🤖 8. Machine Learning Module

The project contains an optional ML pipeline using a Random Forest Classifier.

The classifier uses:

hash_match

size_diff

time_diff

to classify a file as secure or tampered.

The ML implementation is contained primarily in:

ml_model.py

dataset_builder.py

train_model.py

🧠 9. AI Security Analysis

The system uses a Groq-hosted LLM to generate an analysis of the cloud integrity audit.

The generated report can contain:

Security summary

Risks

Recommendations

Algorithm discussion

Conclusion

An interactive AI chatbot is also available from the audit dashboard.

🏗️ System Architecture

                         ┌─────────────────────┐
                         │      User / Web UI   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Flask App      │
                         │       app.py        │
                         └──────────┬──────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
        ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
        │   Encryption   │  │ SHA-256 Hash   │  │  ML / Dataset  │
        │ AES/DES/BF/RSA │  │  Verification  │  │    Analysis    │
        └───────┬────────┘  └───────┬────────┘  └────────────────┘
                │                   │
                ▼                   ▼
        ┌────────────────┐  ┌────────────────────┐
        │  Google Drive  │  │ Integrity Metadata │
        │ Cloud Storage  │  │ JSON Ledger         │
        └────────────────┘  └────────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Audit / Detection │
                         └──────────┬──────────┘
                                    │
                     ┌──────────────┼──────────────┐
                     ▼              ▼              ▼
              ┌────────────┐ ┌────────────┐ ┌──────────────┐
              │ Dashboard  │ │Email Alert │ │ AI Analysis  │
              └────────────┘ └────────────┘ └──────────────┘

🔄 Application Workflow

Upload and Protection

Select File
    ↓
Enter Owner Email
    ↓
Flask Upload
    ↓
Encrypt File
 ┌──┼────┬────┐
AES DES Blowfish RSA
 └──┼────┴────┘
    ↓
Generate SHA-256 Hash
    ↓
Upload Encrypted Files to Google Drive
    ↓
Store Hash + Drive ID + Timing Metadata
    ↓
Audit Dashboard

Integrity Audit

Retrieve Stored Metadata
        ↓
Download Encrypted File
        ↓
Calculate Current SHA-256
        ↓
Compare Stored Hash
        ↓
Compare File Size
        ↓
 ┌──────┴──────┐
 │             │
Match       Mismatch
 │             │
 ▼             ▼
Secure       Tampered
               │
               ▼
          Email Alert

📁 Project Structure

blockchain-secure-ml-system/
│
├── app.py
├── blockchain.py
├── blockchain_data.json
│
├── encryption.py
├── ml_model.py
├── train_model.py
├── dataset_builder.py
│
├── drive.py
├── email_sender.py
├── llm_helper.py
├── graphs.py
│
├── dataset.csv
├── model.pkl
│
├── templates/
│   ├── index.html
│   └── audit.html
│
├── static/
│   ├── confusion.png
│   ├── enc.png
│   ├── upload.png
│   └── dec.png
│
└── uploads/
    └── application-generated files

🧰 Technologies Used

Backend

Python

Flask

Cryptography

PyCryptodome

AES

DES

Blowfish

RSA

SHA-256

Cloud

Google Drive

PyDrive

Machine Learning

Scikit-learn

Random Forest

Decision Tree

Pandas

Joblib

Visualization

Matplotlib

AI

Groq API

Llama 3.1 8B Instant

Frontend

HTML5

CSS3

JavaScript

Jinja2 templates

⚙️ Installation

1. Clone the repository

git clone https://github.com/aman13155/blockchain-secure-ml-system.git
cd blockchain-secure-ml-system

2. Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

Create a requirements.txt file containing:

Flask
pandas
scikit-learn
joblib
matplotlib
pycryptodome
PyDrive
groq
google-api-python-client
google-auth
google-auth-oauthlib
oauth2client

Then install:

pip install -r requirements.txt

🔑 Configuration

The application requires external credentials for Google Drive, email, and the Groq API.

Google Drive

Configure Google API credentials and provide the required client configuration to PyDrive.

The project currently expects:

client_secrets.json
credentials.json

Groq

Set the API key as an environment variable:

Windows PowerShell:

$env:GROQ_API_KEY="your_api_key"

Linux/macOS:

export GROQ_API_KEY="your_api_key"

Update the application code to read the key from the environment instead of hard-coding it.

Email

Configure Gmail SMTP using an App Password, not a normal Gmail password.

Recommended environment variables:

MAIL_USERNAME
MAIL_APP_PASSWORD

▶️ Running the Application

Start the Flask application:

python app.py

Open:

http://127.0.0.1:5000/

The application opens the browser automatically when app.py is executed directly.

🧪 Using the Application

Step 1 — Upload

From the home page:

Enter the file owner's email.

Select one or more files.

Click Upload & Encrypt.

Step 2 — Encryption

The system generates encrypted versions using:

filename.aes
filename.des
filename.bf
filename.rsa

Step 3 — Cloud Upload

Each encrypted file is uploaded to Google Drive.

Step 4 — Metadata Storage

The application stores the corresponding:

Hash

Drive ID

Encryption time

Upload time

Owner email

Step 5 — Integrity Audit

The audit page downloads the cloud copy and verifies its integrity.

Step 6 — Results

The dashboard displays the integrity status and performance analysis.

📊 Evaluation Metrics

The dashboard currently calculates:

Integrity Accuracy

Accuracy =
Secure Files / Total Files × 100

Error Rate

Error Rate =
Tampered Files / Total Files × 100

Confusion Matrix

The application displays:

                 Predicted
               Secure  Tampered

Actual Secure     TN      FP
Actual Tampered   FN      TP

The current demonstration constructs the displayed confusion matrix from the audit results.

🤖 Machine Learning Pipeline

The optional ML module creates a dataset using three features:

Feature

Description

hash_match

Whether current and original hashes match

size_diff

Difference between original and current file size

time_diff

Simulated/recorded timing feature

The target label is:

0 → Secure
1 → Tampered

A Random Forest classifier is used in ml_model.py.

Example training flow:

Encrypted Files
      ↓
Dataset Builder
      ↓
Feature Extraction
      ↓
Train/Test Split
      ↓
Random Forest
      ↓
Prediction
      ↓
Secure / Tampered

📈 Generated Visualizations

The system generates:

static/confusion.png

static/enc.png

static/upload.png

static/dec.png

These visualize:

Confusion matrix

Encryption time

Cloud upload time

Download/verification time

🧠 AI Analysis

The audit dashboard sends summary information to the LLM layer to generate a natural-language security report.

The report can provide:

Security summary

Identified risks

Recommendations

Algorithm discussion

Conclusion

The dashboard also provides an Ask AI interface for security-related questions.

🔐 Security Considerations

This repository is an academic prototype and should not be considered production-ready security software without further hardening.

Important improvements for production deployment include:

Use authenticated encryption such as AES-GCM instead of AES-ECB.

Never hard-code API keys, email passwords, or cloud credentials.

Use environment variables or a secret manager.

Never commit client_secrets.json or credentials.json.

Do not store private encryption keys in source code.

RSA should be used with proper hybrid encryption for large files.

Add authentication and authorization to the Flask application.

Validate uploaded filenames and file types.

Limit upload size.

Protect against path traversal and malicious uploads.

Disable Flask debug mode in production.

Replace the local JSON ledger with a real tamper-resistant distributed ledger if blockchain functionality is required.

Use proper key management and key rotation.

⚠️ Important Repository Cleanup Before Publishing

Do not upload the current ZIP contents directly to a public GitHub repository.

The supplied project contains credential/API-key material and generated cloud/file metadata. Before pushing to GitHub:

Remove API keys from Python source files.

Revoke/rotate any exposed API keys.

Remove email passwords/app passwords.

Remove client_secrets.json.

Remove credentials.json.

Remove private or personal uploaded documents.

Remove generated encrypted files from uploads/.

Remove Google Drive IDs and personal email addresses from committed data.

Add sensitive files to .gitignore.

Commit only source code and safe sample data.

Example .gitignore:

# Python
__pycache__/
*.py[cod]
venv/
.env

# Secrets
client_secrets.json
credentials.json
*.pem
*.key

# Generated model/data
model.pkl
dataset.csv
blockchain_data.json

# User uploads
uploads/*
!uploads/.gitkeep

# Generated images
static/*.png

# Jupyter
.ipynb_checkpoints/

# IDE
.vscode/
.idea/

🚀 Future Enhancements

Potential future improvements include:

Real blockchain or smart-contract integration

AES-GCM authenticated encryption

Secure hybrid RSA + AES encryption

Automatic key management

Blockchain-based immutable audit logs

User authentication and role-based access control

Cloud storage provider abstraction

Real tamper datasets instead of simulated tampering

More robust ML evaluation

Precision, recall, F1-score and ROC-AUC

Continuous cloud integrity monitoring

Docker deployment

REST API

Production-grade database

Multi-cloud storage support

Security event logging

Admin and user dashboards

🎓 Academic Relevance

This project demonstrates the integration of multiple areas of computer science:

Cloud Computing

Cybersecurity

Cryptography

Machine Learning

Artificial Intelligence

Data Integrity

Web Development

Cloud Storage

Security Monitoring

Data Visualization

It can be used as an academic prototype for studying secure cloud data management and intelligent file integrity monitoring.

📄 License

This project is intended for academic and educational purposes.

If you plan to distribute or deploy it commercially, review and add an appropriate open-source or proprietary license.

👨‍💻 Author

Aman Tarikere

GitHub:
https://github.com/aman13155

Project Repository:
https://github.com/aman13155/blockchain-secure-ml-system

⭐ Acknowledgement

This project combines open-source Python libraries and cloud/AI services for educational experimentation in cloud security, cryptography, machine learning, and intelligent integrity monitoring.
