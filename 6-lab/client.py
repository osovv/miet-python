import socket
import os
from dotenv import load_dotenv

load_dotenv()
SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = int(os.getenv('SERVER_PORT', 5006))

def main():
    while True:
        email = input("Enter your email: ")
        message = input("Enter your message: ")

        data = f"{email}\n{message}"

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_HOST, SERVER_PORT))
            sock.sendall(data.encode())

            response = sock.recv(1024).decode()
            if response == 'OK':
                print("Message sent successfully!")
                break
            else:
                print(f"Error: {response}")
                print("Please try again.")

if __name__ == "__main__":
    main()
