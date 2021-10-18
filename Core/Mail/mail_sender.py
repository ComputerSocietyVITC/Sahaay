from email.mime.multipart import MIMEMultipart
import smtplib
from Core.Mail.mail_config import dev_smtp_config


def send_mail(message: MIMEMultipart):
    """Sends an email with the given Multipart message as content.
    Requires the from and to fields to be set.
    """

    smtp_server = dev_smtp_config["smtp_server"]
    port = dev_smtp_config["port"]

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(dev_smtp_config["user"], dev_smtp_config["password"])
        server.sendmail(message["From"], message["To"], message.as_string())
