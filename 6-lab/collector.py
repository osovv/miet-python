import imaplib
import email
import os
from email.header import decode_header
from dotenv import load_dotenv
import time
import re

load_dotenv()
EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
IMAP_HOST = os.getenv('IMAP_HOST')
IMAP_PORT = int(os.getenv('IMAP_PORT'))
PERIOD_CHECK = int(os.getenv('PERIOD_CHECK', 60))

def decode_subject(subject):
    try:
        return subject.decode('utf-8')
    except UnicodeDecodeError:
        try:
            return subject.decode('iso-8859-1')
        except UnicodeDecodeError:
            return "Undecodable Subject"

def check_mail():
    with imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT) as mail:
        mail.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        mail.select('inbox')

        _, messages = mail.search(None, 'UNSEEN')
        for num in messages[0].split():
            _, data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(data[0][1])
            subject, encoding = decode_header(msg['Subject'])[0]
            if isinstance(subject, bytes):
                subject = decode_subject(subject)

            subject_pattern = r"\[Ticket #\d+\] Mailer"
            print(f"Collected email: {subject}")
            if re.match(subject_pattern, subject):
                log_file_name = 'success_request.log'
            else:
                log_file_name = 'error_request.log'

            with open(log_file_name, 'a') as file:
                file.write(f"{subject}: {msg.get_payload(decode=True)}\n")

def main():
    while True:
        check_mail()
        time.sleep(PERIOD_CHECK)

if __name__ == '__main__':
    main()
