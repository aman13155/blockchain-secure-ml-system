import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

# =========================================
# SEND EMAIL FUNCTION
# =========================================

def send_email(

    subject,

    body,

    receiver_email
):

    # =========================================
    # GMAIL DETAILS
    # =========================================

    sender_email = "mscprojectcc@gmail.com"

    app_password = "omaf yufu koln ljkh"

    # =========================================
    # CREATE MESSAGE
    # =========================================

    msg = MIMEMultipart()

    msg["From"] = sender_email

    msg["To"] = receiver_email

    msg["Subject"] = subject

    msg.attach(

        MIMEText(
            body,
            "plain"
        )
    )

    try:

        # =========================================
        # CONNECT SMTP
        # =========================================

        server = smtplib.SMTP(

            "smtp.gmail.com",

            587
        )

        server.starttls()

        # =========================================
        # LOGIN
        # =========================================

        server.login(

            sender_email,

            app_password
        )

        # =========================================
        # SEND EMAIL
        # =========================================

        server.send_message(msg)

        # =========================================
        # CLOSE SERVER
        # =========================================

        server.quit()

        print(

            "✅ Email Sent Successfully!"
        )

    except Exception as e:

        print(

            "❌ Email Error:",

            e
        )