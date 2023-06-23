import sys
from send_email import send_mail
from email_format import format_msg
from send_email import send_mail
import smtplib


def send(
    name: str, to_email: str = None, website: str = None, verbose: bool = False
) -> bool:
    assert to_email is not None

    if website is not None:
        msg = format_msg(name=name, website=website)
    else:
        msg = format_msg(name=name)

    if verbose:
        print(name, website, to_email)

    try:
        send_mail(text=msg, to_emails=[to_email])
        sent = True
    except smtplib.SMTPAuthenticationError:
        sent = False
    return sent


if __name__ == "__main__":
    name = "Nijhum"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name=name, to_email=email, verbose=True)
    print(response)
