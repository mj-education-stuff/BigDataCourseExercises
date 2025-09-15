import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from src.msg import EmailClient, SMTPServer

if __name__ == "__main__":
    load_dotenv(Path(__file__).resolve().parent / ".env")

    attachment_path = Path(
        os.getenv("KUBECONFIGS_DIR", Path(__file__).resolve().parent.parent / "tmp")
    )
    df = pd.read_csv(attachment_path.parent / "data/project_groups.csv", sep=";")
    attachment_files = list(attachment_path.glob("bd-gr-*.yaml"))
    assert len(attachment_files) == 10, len(attachment_files)

    ec = EmailClient(
        email=os.getenv("EMAIL", "<email>"),
        password=os.getenv("PASSWORD", "<password>"),
        smtp_server=SMTPServer.SDU,
    )

    for idx, (id, students) in df.iterrows():
        students = students.split(", ")
        attachment_file = [
            i
            for i in attachment_files
            if i.name.startswith(f"bd-gr-{str(id).zfill(2)}")
        ][0]

        for user_name in students:
            receiver_email: str = user_name + "@student.sdu.dk"

            print(
                f"Sending to {user_name} at {receiver_email} for group {id} with attachment {attachment_file.name}"
            )

            msg = ec.create_msg(
                receiver_email=receiver_email,
                subject="[Kubeconfig] - Kubeconfig for project work in Big Data and Data Science Technology, E25",
                body=f"Dear {user_name},\n\nHere is the kubeconfig file for the Kubernetes cluster you need for your project in the course Big Data and Data Science Technology, E25.\n\nBest regards,\nAnders Launer Bæk-Petersen\n\n",
                attachment=attachment_file,
            )
            # ec.send_msg(receiver_email, msg)
