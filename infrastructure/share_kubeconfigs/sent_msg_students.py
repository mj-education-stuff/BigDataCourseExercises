import os
from pathlib import Path

from dotenv import load_dotenv
from src.msg import EmailClient, SMTPServer

if __name__ == "__main__":

    load_dotenv(Path(__file__).resolve().parent / ".env")

    attachment_path = Path(
        os.getenv("KUBECONFIGS_DIR", Path(__file__).resolve().parent.parent / "tmp")
    )
    attachment_files = list(attachment_path.glob("bd-stud-*.yaml"))
    assert len(attachment_files) == 56, len(attachment_files)

    ec = EmailClient(
        email=os.getenv("EMAIL", "<email>"),
        password=os.getenv("PASSWORD", "<password>"),
        smtp_server=SMTPServer.SDU,
    )

    for attachment in attachment_files:

        user_name = attachment.name.split("-")[-2]
        receiver_email: str = user_name + "@student.sdu.dk"

        msg = ec.create_msg(
            receiver_email=receiver_email,
            subject="[Kubeconfig] - Kubeconfig for exercises in Big Data and Data Science Technology, E25",
            body=f"Dear {user_name},\n\nHere is the kubeconfig file for the Kubernetes cluster you need for exercises in the course Big Data and Data Science Technology, E25.\n\nBest regards,\nAnders Launer Bæk-Petersen\n\n",
            attachment=attachment,
        )
        # ec.send_msg(receiver_email, msg)
