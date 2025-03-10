import socket
import threading

HOST = '192.168.1.174'  # OBS KOM IHÅG ATT BYTA TILL DITT NÄTVERK
PORT = 3333

# 10.32.41.176

clients = []
player_symbols = ["X", "O"]
current_turn = 0
board = [""] * 9


def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rader
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Kolumner
                            (0, 4, 8), (2, 4, 6)              # Diagonaler
                            ]
    for (a, b, c) in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
        if "" not in board:
            return "draw"
    return None


def handle_client(client, player_id):
    global current_turn
    client.send(player_symbols[player_id].encode())

    while True:
        try:
            move = client.recv(1024).decode()
            if not move:
                break

            move = int(move)
            board[move] = player_symbols[player_id]

            winner = check_winner()
            if winner:
                for c in clients:
                    c.send("win".encode())  # Skickar vem som vann
                reset_game()
                continue

            other_player = clients[1 - player_id]
            other_player.send(move.encode())
            current_turn = 1 - current_turn
        except:
            break

    client.close()
    clients.remove(client)


def reset_game():
    global board, current_turn
    board = [""] * 9  # Återställ brädet
    current_turn = 0  # Sätt X som första spelare


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
