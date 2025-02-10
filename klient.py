from socket import *


def connect_to_server():
    s = socket()                # Skapa ett socket-objekt
    host = input("Ange serverns IP-adress:")
    port = 12345                # Servern körs på port 12345
    s.connect((host, port))     # Anslut till servern
    return s


s = connect_to_server()

while True:
    message = s.recv(1024).decode()
    if not message:
        break
    print("Meddelande från servern:", message)

s.close()
