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
        self.client.connect(('127.0.0.1', 5555))

        self.symbol = self.client.recv(1024).decode()
        if self.symbol == "X":
            self.my_turn = True  # X börjar alltid

        threading.Thread(target=self.receive_moves, daemon=True).start()

        self.window.mainloop()
