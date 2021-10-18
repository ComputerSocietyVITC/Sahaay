import base64
import binascii
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import PathLike
from types import Mail
from Core.Mail.mail_config import dev_smtp_config


def construct_mail(
    subject: str, plain_text: str, html: str, to_address: Mail
) -> MIMEMultipart:
    # NOTE, have to use `mail_checker` from `Core.Mail.checker` and validate `to_address`.
    # Or have to validate `to_address` before passing it here.
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = dev_smtp_config["test_email"]
    message["To"] = to_address
    message.attach(MIMEText(plain_text, "plain"))
    message.attach(MIMEText(html, "html"))
    return message


def email_html_template():
    """TODO. Add required params, and return a formatted HTML string for the email"""
    example_name = "mainak"
    return f"""
        <html>
            <body>
                <p> Hi {example_name} </p>
            </body>
        </html>
    """
