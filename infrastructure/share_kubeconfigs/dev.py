import os
import time
from pathlib import Path

from dotenv import load_dotenv
from src.msg import EmailClient, SMTPServer

load_dotenv()
receiver_email: str = "anbae@mmmi.sdu.dk"

attachment = Path(
    "/home/launer/git/phd/teaching/BigDataCourseExercises/infrastructure/share_kubeconfigs/requirements.txt"
)


ec = EmailClient(
    email=os.getenv("EMAIL", "<email>"),
    # email="Anders Launer Bæk-Petersen <anbae@mmmi.sdu.dk>",
    password=os.getenv("PASSWORD", "<password>"),
    smtp_server=SMTPServer.SDU,
)

for _ in range(1):

    for i in range(3):
        msg = ec.create_msg(
            receiver_email=receiver_email,
            subject=f"[{i}] - Kubeconfig for the project in Big Data and Data Science Technology, E24",
            body="Dear student,\n\nHere is the kubeconfig file for the Kubernetes cluster you need for your project in the course Big Data and Data Science Technology, E24.\n\nBest regards,\nAnders Launer Bæk-Petersen\n\n",
            attachment=attachment,
        )
        ec.send_msg(receiver_email, msg)

    time.sleep(60)  # Sleep for 60 seconds before sending the next batch
