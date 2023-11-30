import socket
import smtplib
import time
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = int(os.getenv('SERVER_PORT', 5006))
EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = int(os.getenv('SMTP_PORT'))

def generate_unique_subject():
    unique_id = int(time.time())
    return f"[Ticket #{unique_id}] Mailer"

def send_email(subject, body, recipient, sender=EMAIL_LOGIN):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        server.sendmail(sender, recipient, msg.as_string())
        print(f"Email sent to {recipient}")

def handle_client_connection(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        email, message = data.split('\n')
        print(f"Received email: {email}")

        subject = generate_unique_subject()
        send_email(subject, message, email)
        send_email(subject, message, EMAIL_LOGIN)

        client_socket.sendall('OK'.encode())
    except Exception as e:
        client_socket.sendall(f"Error: {e}".encode())
    finally:
        client_socket.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen()
        print(f"Server started at: {SERVER_HOST}:{SERVER_PORT}")

        while True:
            client_socket, addr = server_socket.accept()
            handle_client_connection(client_socket)

if __name__ == "__main__":
    main()
