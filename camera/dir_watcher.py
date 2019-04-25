import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
from os.path import join, dirname
from dotenv import load_dotenv
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class Watcher:
    DIRECTORY_TO_WATCH = './test_subjects'

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=False)

        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print('Error')

        self.observer.join


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_created(event):
        for path, subdirs, files in os.walk('./test_subjects'):
            for name in files:
                file_name = os.path.join(path, name)
                test_name = os.path.abspath(file_name)
                print(test_name)
        send_email(test_name)
        os.system('rm -rf ' + file_name)


# load sender email and password and recipient password from .env file
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


def send_email(file_name):



    # Define to/from email addresses and subject information
    from_addr = os.environ.get('FROM_ADDR')
    password = os.environ.get('FROM_PASSWORD')
    to_addr = os.environ.get('TO_ADDR')

    subject = 'SnakeEyes Notification'

    # Create multi-part email instance and add pre-defined variables
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    # attach the text of the body of the email
    body = 'Unknown face detected -- see attachment.'
    msg.attach(MIMEText(body, 'plain'))

    # include an attachment to the email
    attachment_name = file_name
    attachment = open(file_name, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    "attachment; filename= " + attachment_name)
    msg.attach(part)

    # open gmail server and login as sender
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(from_addr, password)

    # send the email
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    print('email-sent')

    # close the server
    server.quit()


if __name__ == "__main__":
    w = Watcher()
    w.run()
