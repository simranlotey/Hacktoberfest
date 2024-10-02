import asyncio
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

import aiosmtplib


password = ""
SMTP_SERVER = "smtp-mail.outlook.com"
SENDER = ""


# Send an email to a user
async def async_email_user(email: str, sender: str, subject: str, message: str):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "html"))

    # Create an SMTP connection
    async with aiosmtplib.SMTP(hostname=SMTP_SERVER, port=587, start_tls=True) as smtp:
        # Authenticate with the SMTP server
        await smtp.login(sender, password)

        # Send the email
        await smtp.send_message(msg)


# Send an email to a user with a name
async def async_email_user_with_name(
    email: str, sender: str, name: str, subject: str, message: str
):
    msg = EmailMessage()
    msg["From"] = formataddr((name, sender))
    msg["To"] = email
    msg["Subject"] = subject
    msg.add_alternative(message, subtype="html")

    # Create an SMTP connection
    async with aiosmtplib.SMTP(hostname=SMTP_SERVER, port=587, start_tls=True) as smtp:
        # Authenticate with the SMTP server
        await smtp.login(sender, password)

        # Send the email
        await smtp.send_message(msg)


async def main():
    # Email details
    sender = "example@outlook.com"
    email = "example@gmail.com"
    name = "John Doe"
    subject = "Test Email"
    message = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is a test email.</p>
        </body>
    </html>
    """

    # Send the email asynchronously
    # await async_email_user(email, subject, message)
    await async_email_user_with_name(email, sender, name, subject, message)


if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
