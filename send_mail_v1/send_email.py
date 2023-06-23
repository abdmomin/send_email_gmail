import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

EMAIL_ADD = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASS = os.environ.get("PASSWORD")

HOST = "smtp.gmail.com"
PORT = 465


def send_mail(
    from_email: str = "Abdullah <abd.almomin@gmail.com>",
    to_emails: list[str] | None = None,
    text: str = "Email body",
    subject: str = "Hello World",
    html: str | None = None,
) -> None:
    assert isinstance(to_emails, list)

    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject

    text_body = MIMEText(text, "plain")
    msg.attach(text_body)

    if html is not None:
        html_body = MIMEText(html, "html")
        msg.attach(html_body)

    email_msg = msg.as_string()

    with smtplib.SMTP_SSL(host=HOST, port=PORT) as server:
        server.login(EMAIL_ADD, EMAIL_PASS)
        server.sendmail(from_email, to_emails, email_msg)


if __name__ == "__main__":
    send_mail(
        text="Email from script",
        subject="Test email",
        to_emails=["abd.almomin@gmail.com"],
    )
