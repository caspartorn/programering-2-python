import socket
import threading

HOST = '192.168.1.174'  # OBS KOM IHÅG ATT BYTA TILL DITT NÄTVERK
PORT = 3333


clients = []
player_symbols = ["X", "O"]
current_turn = 0


def handle_client(client, player_id):
    global current_turn
    client.send(player_symbols[player_id].encode())

    while True:
        try:
            move = client.recv(1024).decode()
            if not move:
                break

            other_player = clients[1 - player_id]
            other_player.send(move.encode())
            current_turn = 1 - current_turn
        except:
            break

    client.close()
    clients.remove(client)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print("Servern väntar för spelare...")

    while len(clients) < 2:
        client, addr = server.accept()
        print(f"Spelare {len(clients) + 1} Annslöt från {addr}")
        clients.append(client)

        player_id = len(clients) - 1
        threading.Thread(target=handle_client,
                         args=(client, player_id)).start()

    print("Spelet börjar...")


start_server()
