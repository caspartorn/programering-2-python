import socket
import threading
import tkinter as tk
from tkinter import messagebox


class TicTacToeClient:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.board = [""] * 9
        self.buttons = []
        self.my_turn = False
        self.symbol = ""

        # UI Setup
        self.create_board()

        # coonectar till server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # OBS KOM IHÅG ATT BYTA TILL DITT NÄTVERK
        self.client.connect(('192.168.1.174', 3333))

        self.symbol = self.client.recv(1024).decode()
        if self.symbol == "X":
            self.my_turn = True  # X börjar alltid

        threading.Thread(target=self.receive_moves, daemon=True).start()

        self.window.mainloop()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.window, text="", font=('Arial', 24), width=5, height=2,
                                command=lambda row=i, col=j: self.make_move(row, col))
                btn.grid(row=i, column=j)
                self.buttons.append(btn)

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == "" and self.my_turn:
            self.board[index] = self.symbol
            self.buttons[index].config(text=self.symbol, state="disabled")
            self.client.send(str(index).encode())
            self.my_turn = False

    def receive_moves(self):
        while True:
            try:
                index = int(self.client.recv(1024).decode())
                opponent_symbol = "O" if self.symbol == "X" else "X"
                self.board[index] = opponent_symbol
                self.buttons[index].config(
                    text=opponent_symbol, state="disabled")
                self.my_turn = True
            except:
                break


if __name__ == "__main__":
    TicTacToeClient()
