from socket import *
import threading

Host = "0,0,0,0"
port = 3000
ADDR = (Host, port)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)
server.listen(2)

print("servern är startad på {Host}:{port}")

board = [""] * 9
players = {}
current_turn = "X"


def send_board():
    board_state = ",".join(board)
    for player in players.values():
        player.sendall(board_state.encode())


def check_winner():
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rader
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Kolumner
        (0, 4, 8), (2, 4, 6)  # Diagonaler
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
        return None


def handle_client(conn, symbol):
    global current_turn
    conn.sendall(f"Du är {symbol}".encode())
