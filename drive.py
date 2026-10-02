from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# -------------------------------
# CONNECT (ONLY ONCE)
# -------------------------------
gauth = GoogleAuth()

# Load client secrets
gauth.LoadClientConfigFile("client_secrets.json")

# Try saved credentials
gauth.LoadCredentialsFile("credentials.json")

if gauth.credentials is None:
    # First time login
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh token
    gauth.Refresh()
else:
    gauth.Authorize()

# Save credentials
gauth.SaveCredentialsFile("credentials.json")

# Create drive object
drive = GoogleDrive(gauth)


# -------------------------------
# UPLOAD FILE
# -------------------------------
def upload_to_drive(file_path):
    file_drive = drive.CreateFile({
        'title': file_path.split("\\")[-1]  # only file name
    })

    file_drive.SetContentFile(file_path)
    file_drive.Upload()

    drive_id = file_drive['id']

    print("Uploaded to Drive ID:", drive_id)

    return drive_id


# -------------------------------
# DOWNLOAD FILE
# -------------------------------
def download_from_drive(file_id, save_path):
    file_drive = drive.CreateFile({'id': file_id})
    file_drive.GetContentFile(save_path)