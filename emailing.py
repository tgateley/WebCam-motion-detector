import os
import smtplib
import imghdr

from email.message import EmailMessage

PASSWORD = os.getenv("webcam_detect")
SENDER = "tgateley22@gmail.com"
RECEIVER = "tgateley22@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Object Detected!"
    email_message.set_content("New object found in frame.")
    image_type = imghdr.what(image_path)

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image",
                                 subtype=image_type)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/3.png")
