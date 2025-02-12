
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
answers = ["Stockholm", "4", "Grön"]

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
