import tkinter as tk
from tkinter import messagebox


def addera_tal():
    try:
        tal1 = float(entry_tal1.get())
        tal2 = float(entry_tal2.get())
        summa = tal1 + tal2
        result_label.config(text=f"Resultat: {summa}")
    except ValueError:
        messagebox.showerror("Fel", "Vänligen mata in giltiga nummer!")


root = tk.Tk()
root.title("Adderare")
root.geometry("300x200")

label_tal1 = tk.Label(root, text="Skriv in första talet:")
label_tal1.pack(pady=5)
entry_tal1 = tk.Entry(root)
entry_tal1.pack(pady=5)

label_tal2 = tk.Label(root, text="Skriv in andra talet:")
label_tal2.pack(pady=5)
entry_tal2 = tk.Entry(root)
entry_tal2.pack(pady=5)

addera_button = tk.Button(root, text="Addera", command=addera_tal)
addera_button.pack(pady=10)

result_label = tk.Label(root, text="Resultat: ")
result_label.pack(pady=5)

root.mainloop()
