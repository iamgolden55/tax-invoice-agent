import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_invoice_email(receiver_email, subject, body, attachment_path):
    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach PDF
    with open(attachment_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    # Send Email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)

    return f"✅ Invoice sent to {receiver_email}"
