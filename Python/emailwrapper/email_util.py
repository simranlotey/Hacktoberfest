import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


# send outlook mail
def email_user(email: str, sender: str, password: str, subject: str, message: str):
    SENDER_EMAIL = sender
    SENDER_PASSWORD = password
    SMTP_SERVER = "smtp-mail.outlook.com"
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "html"))

    with smtplib.SMTP(SMTP_SERVER, 587) as smtp:
        smtp.starttls()
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)
        smtp.quit()


# send outlook mail with usre name
def email_user_with_name(
    email: str, sender: str, password: str, subject: str, message: str
):
    SENDER_EMAIL = sender
    SENDER_PASSWORD = password
    SMTP_SERVER = "smtp-mail.outlook.com"
    SENDER = "MusicDash"
    msg = EmailMessage()
    msg["From"] = formataddr((SENDER, SENDER_EMAIL))
    msg["To"] = email
    msg["Subject"] = subject
    msg.add_alternative(message, subtype="html")

    with smtplib.SMTP(SMTP_SERVER, 587) as smtp:
        smtp.starttls()
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)
        smtp.quit()


if __name__ == "__main__":
    email_user_with_name(
        "example@gmail.com",
        "example@gmail.com",
        "Test Mail",
        "",
        """
        <html>
        <div>
            <div>
                <h1>Header<h1>
            </div>
            <div>
                <b>This is a test email HTML body.<b>
            </div>
        </html>
        """,
    )
    print("an email sent.")
