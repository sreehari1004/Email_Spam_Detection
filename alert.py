import smtplib
from email.mime.text import MIMEText

def send_alert_email(message):
    try:
        sender = "youremail@example.com"
        receiver = "alert@example.com"
        msg = MIMEText(f"Spam alert: {message}")
        msg['Subject'] = "Spam Detection Alert"
        msg['From'] = sender
        msg['To'] = receiver

        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender, "your_password")
            server.sendmail(sender, receiver, msg.as_string())
            print("Alert email sent!")
    except Exception as e:
        print("Email alert failed:", e)
