# TODO: Update to OAUTH authentication
# Server: smtp.office365.com
# Port: 587
# Using: STARTTLS

# current solution:
# needs to be on SDU net.
# Server: smtps.sdu.dk
# Port: 465
# Using: SSL

import enum
import smtplib
import ssl
from dataclasses import dataclass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


class SMTPServer(enum.Enum):
    SDU: dict[str, str | int] = {"host": "smtp.sdu.dk", "port": 25}
    SDUSSL: dict[str, str | int] = {"host": "smtps.sdu.dk", "port": 465}


# batch into N emails
N_EMAILS = 10
SLEEP_TIME: int = 60


@dataclass
class EmailClient:
    email: str
    password: str
    smtp_server: SMTPServer = SMTPServer.SDU
    server: str = None
    port: int = None

    def __post_init__(self):
        self.server = self.smtp_server.value["host"]
        self.port = self.smtp_server.value["port"]

    def create_msg(
        self, receiver_email: str, subject: str, body: str, attachment: Path = None
    ) -> str:

        message = MIMEMultipart()
        message["From"] = self.email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        if attachment:
            with open(attachment, "rb") as fh:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(fh.read())

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {attachment.name}",
            )
            message.attach(part)

        return message.as_string()

    def send_msg(self, receiver_email: str, msg: str) -> None:
        # Log in to server using secure context and send email
        try:

            print(f"Connecting to {self.server}:{self.port} as {self.email}")
            if self.smtp_server == SMTPServer.SDU:
                with smtplib.SMTP(self.server, self.port) as server:
                    print(f"Sending mail to {receiver_email}")
                    server.sendmail(self.email, receiver_email, msg)
            elif self.smtp_server == SMTPServer.SDUSSL:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(
                    self.server, self.port, context=context
                ) as server:
                    server.login(self.email, self.password)
                    server.sendmail(self.email, receiver_email, msg)
            else:
                raise ValueError("Unsupported SMTP server configuration")
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print("Email sent successfully")
