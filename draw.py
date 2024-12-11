# import tkinter as tk

# root = tk.Tk()
# root.title = "ritprogram"

# canvas = tk.Canvas(root, bg="white", width=600, height=400)
# canvas.pack()

# last_x, last_y = None, None


# def start_drawing(event):
#     global last_x, last_y
#     last_x, last_y = event.x, event.y


# def draw(event):
#     global last_x, last_y
#     if last_x and last_y:
#         canvas.create_line(last_x, last_y, event.x,
#                            event.y, fill="black", width=2)
#         last_x, last_y = event.x, event.y


# def reset(event):
#     global last_x, last_y
#     last_x, last_y = None, None


# canvas.bind("<Button-1>", start_drawing)
# canvas.bind("<B1-Motion>", draw)
# canvas.bind("<ButtonRelease-1>", reset)

# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox


# def addera_tal():
#     try:
#         tal1 = float(entry_tal1.get())
#         tal2 = float(entry_tal2.get())
#         summa = tal1 + tal2
#         result_label.config(text=f"Resultat: {summa}")
#     except ValueError:
#         messagebox.showerror("Fel", "Vänligen mata in giltiga nummer!")


# root = tk.Tk()
# root.title("Adderare")
# root.geometry("300x200")

# label_tal1 = tk.Label(root, text="Skriv in första talet:")
# label_tal1.pack(pady=5)
# entry_tal1 = tk.Entry(root)
# entry_tal1.pack(pady=5)

# label_tal2 = tk.Label(root, text="Skriv in andra talet:")
# label_tal2.pack(pady=5)
# entry_tal2 = tk.Entry(root)
# entry_tal2.pack(pady=5)

# addera_button = tk.Button(root, text="Addera", command=addera_tal)
# addera_button.pack(pady=10)

# result_label = tk.Label(root, text="Resultat: ")
# result_label.pack(pady=5)

# root.mainloop()

import tkinter as tk
from tkinter import messagebox


def check_answer():
    user_answer = entry.get().strip().lower()
    correct_answer = answers[current_question.get()].lower()

    if user_answer == correct_answer:
        messagebox.showinfo("Resultat", "Rätt svar! Bra jobbat!")
        current_question.set((current_question.get() + 1) % len(questions))
        update_question()
    else:
        messagebox.showwarning("Resultat", "Fel svar. Försök igen!")


def update_question():
    question_label.config(text=questions[current_question.get()])
    entry.delete(0, tk.END)


questions = ["Vad är huvudstaden i Sverige?", "Vad är 2 + 2?",
             "Vilken färg får man om man blandar blått och gult?"]
answers = ["Stockholm", "4", "Grönt"]

root = tk.Tk()
root.title("Frågespel")
root.geometry("400x200")

current_question = tk.IntVar(value=0)

question_label = tk.Label(
    root, text=questions[current_question.get()], font=("Arial", 14))
question_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

check_button = tk.Button(root, text="Kolla svar",
                         command=check_answer, font=("Arial", 12))
check_button.pack(pady=5)

exit_button = tk.Button(root, text="Avsluta",
                        command=root.quit, font=("Arial", 12))
exit_button.pack(pady=5)

root.mainloop()
