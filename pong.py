import tkinter as tk


class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong med dig själv")

        # Skärmstorlek
        self.WIDTH = 800
        self.HEIGHT = 400

        self.Ball_speed = [4, 4]
        self.paddle_speed = [20]
        self.paddle_width = [20]
        self.paadle_height = [100]

        self.show_start_menu()

    def show_start_menu(self):
        self.clear_screen()
        self.start_label = tk.Label(
            self.root, text="Pong med dig själv", font=("Arial", 24), fg="white", bg="black"
        )
        self.start_label.pack(pady=20)

        self.start_button = tk.Button(
            self.root, text="Starta Spelet", font=("Arial", 18), command=self.start_game
        )
        self.start_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
