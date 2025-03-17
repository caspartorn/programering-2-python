import socket
import threading

HOST = '10.32.41.176'
PORT = 3333

# 10.32.41.176

clients = []
player_symbols = ["X", "O"]
current_turn = 0
board = [""] * 9
lock = threading.Lock()


def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
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
            if move < 0 or move >= 9 or board[move] != "":
                client.send("Ogiltigt drag. Försök igen.".encode())
                continue

            with lock:
                board[move] = player_symbols[player_id]

            winner = check_winner()
            if winner:
                for c in clients:
                    if winner == "draw":
                        c.send("Spelet är oavgjort.".encode())
                    else:
                        c.send(f"{winner} vann!".encode())
                reset_game()
                continue

            other_player = clients[1 - player_id]
            other_player.send(str(move).encode())
            current_turn = 1 - current_turn
        except (socket.error, ConnectionResetError):
            break

    with lock:
        clients.remove(client)
    client.close()


def reset_game():
    global board, current_turn
    board = [""] * 9
    current_turn = 0


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print("Servern väntar för spelare...")

    while len(clients) < 2:
        client, addr = server.accept()
        print(f"Spelare {len(clients) + 1} anslöt från {addr}")
        clients.append(client)

        player_id = len(clients) - 1
        threading.Thread(target=handle_client,
                         args=(client, player_id)).start()

    print("Spelet börjar...")


start_server()
