import os
from templates import Template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv("../.env"))

EMAIL_ADD = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASS = os.environ.get("PASSWORD")

HOST = "smtp.gmail.com"
PORT = 465


class EmailSender:
    def __init__(
        self,
        subject: str,
        context: dict[str, str],
        to_emails: list[str],
        template_name: str | None = None,
        html_template: str | None = None,
    ) -> None:
        assert template_name == None or html_template == None, "You must set a template"

        assert isinstance(to_emails, list)

        self.to_emails = to_emails
        self.subject = subject
        self.from_email = "Abdullah <abd.almomin@gmail.com>"
        self.has_html = False
        self.html_template = html_template
        self.template_name = template_name
        self.context = context
        if self.html_template is not None:
            self.has_html = True

    def format_email(self):
        msg = MIMEMultipart("alternative")
        msg["From"] = self.from_email
        msg["To"] = ", ".join(self.to_emails)
        msg["Subject"] = self.subject

        if self.template_name is not None:
            temp_text = Template(template_name=self.template_name, context=self.context)
            text_body = MIMEText(temp_text.render_template(), "plain")
            msg.attach(text_body)

        if self.html_template is not None:
            temp_html = Template(template_name=self.html_template, context=self.context)

            html_body = MIMEText(temp_html.render_template(), "html")
            msg.attach(html_body)

        email_msg = msg.as_string()
        return email_msg

    def send(self) -> None:
        email_msg = self.format_email()

        with smtplib.SMTP_SSL(host=HOST, port=PORT) as server:
            server.login(EMAIL_ADD, EMAIL_PASS)
            try:
                server.sendmail(self.from_email, self.to_emails, email_msg)
                sent = True
            except smtplib.SMTPAuthenticationError:
                sent = False
        return sent


if __name__ == "__main__":
    email = EmailSender(
        subject="Test html email",
        # template_name="test.txt",
        html_template='test.html',
        context={"name": "NJM"},
        to_emails=["abd.almomin@gmail.com"],
    )
    print(email.send())
