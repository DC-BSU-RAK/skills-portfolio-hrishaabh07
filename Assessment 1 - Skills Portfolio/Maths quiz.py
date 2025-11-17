import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk


class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Colors
        self.bg_color = "#F0F8FF"
        self.button_color = "#4CAF50"
        self.button_fg_color = "white"
        self.label_fg_color = "#333333"
        self.correct_color = "green"
        self.wrong_color = "red"

        self.main_menu()

   
    # Background Creator

    def create_background(self):
        self.canvas = tk.Canvas(self.root, width=500, height=400, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        try:
            img = Image.open("maths quiz background.png")   # <--- for adding background image
            img = img.resize((500, 400), Image.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        except Exception as e:
            print("Error loading background:", e)
            self.canvas.config(bg=self.bg_color)

   # Main Menu
 
    def main_menu(self):
        self.clear_frame()
        self.create_background()

        self.frame = tk.Frame(self.canvas, bg=self.bg_color, bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        title_label = tk.Label(
            self.frame, text="Math Quiz",
            font=("Arial", 30, "bold"),
            fg=self.label_fg_color, bg=self.bg_color
        )
        title_label.pack(pady=20)

        tk.Button(
            self.frame, text="Easy",
            font=("Arial", 14),
            bg=self.button_color, fg=self.button_fg_color,
            command=lambda: self.start_quiz("easy")
        ).pack(pady=5, fill="x")

        tk.Button(
            self.frame, text="Medium",
            font=("Arial", 14),
            bg=self.button_color, fg=self.button_fg_color,
            command=lambda: self.start_quiz("medium")
        ).pack(pady=5, fill="x")

        tk.Button(
            self.frame, text="Hard",
            font=("Arial", 14),
            bg=self.button_color, fg=self.button_fg_color,
            command=lambda: self.start_quiz("hard")
        ).pack(pady=5, fill="x")

        tk.Button(
            self.frame, text="Instructions",
            font=("Arial", 14),
            command=self.show_instructions
        ).pack(pady=5, fill="x")

        tk.Button(
            self.frame, text="Quit",
            font=("Arial", 14),
            bg="red", fg="white",
            command=self.root.quit
        ).pack(pady=20, fill="x")

    # Start Quiz

    def start_quiz(self, difficulty):
        self.clear_frame()
        self.create_background()

        self.difficulty = difficulty
        self.score = 0
        self.question_number = 0

        self.quiz_frame = tk.Frame(self.canvas, bg=self.bg_color, bd=5)
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.question_label = tk.Label(
            self.quiz_frame, text="",
            font=("Arial", 20, "bold"),
            fg=self.label_fg_color, bg=self.bg_color
        )
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.quiz_frame, font=("Arial", 16))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(
            self.quiz_frame, text="Submit",
            font=("Arial", 14),
            bg=self.button_color, fg=self.button_fg_color,
            command=self.check_answer
        )
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(
            self.quiz_frame, text="",
            font=("Arial", 14, "italic"),
            bg=self.bg_color
        )
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(
            self.quiz_frame, text="Score: 0",
            font=("Arial", 14, "bold"),
            fg=self.label_fg_color, bg=self.bg_color
        )
        self.score_label.pack(pady=10)

        self.next_question()

 # Generate Question
   
    def next_question(self):
        self.question_number += 1
        if self.question_number > 10:
            messagebox.showinfo("Quiz Over", f"Your score is {self.score}/10")
            self.main_menu()
            return

        self.answer_entry.delete(0, tk.END)
        self.result_label.config(text="")

        if self.difficulty == "easy":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operator = "+"
            self.correct_answer = num1 + num2

        elif self.difficulty == "medium":
            num1 = random.randint(1, 25)
            num2 = random.randint(1, 25)
            operator = random.choice(["+", "-", "*"])

            if operator == "+":
                self.correct_answer = num1 + num2
            elif operator == "-":
                self.correct_answer = num1 - num2
            else:
                self.correct_answer = num1 * num2

        else:  # Hard
            num1 = random.randint(10, 50)
            num2 = random.randint(1, 10)
            operator = random.choice(["+", "-", "*", "/"])

            if operator == "/":
                num1 = num2 * random.randint(1, 10)
                self.correct_answer = num1 // num2
            elif operator == "+":
                self.correct_answer = num1 + num2
            elif operator == "-":
                self.correct_answer = num1 - num2
            else:
                self.correct_answer = num1 * num2

        self.question_label.config(
            text=f"Question {self.question_number}:  {num1} {operator} {num2} = ?"
        )

   # Check Answer
 
    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_answer:
                self.score += 1
                self.result_label.config(text="Correct!", fg=self.correct_color)
            else:
                self.result_label.config(
                    text=f"Wrong! Answer: {self.correct_answer}",
                    fg=self.wrong_color
                )

            self.score_label.config(text=f"Score: {self.score}")
            self.root.after(1000, self.next_question)

        except ValueError:
            messagebox.showerror("Error", "Enter a valid number!")

# Instructions
    def show_instructions(self):
        self.clear_frame()
        self.create_background()

        instructions_frame = tk.Frame(self.canvas, bg=self.bg_color, bd=5)
        instructions_frame.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(
            instructions_frame, text="Instructions",
            font=("Arial", 24, "bold"),
            fg=self.label_fg_color, bg=self.bg_color
        )
        title.pack(pady=20)

        text = (
            "1. Choose a difficulty.\n"
            "2. Each level has 10 questions.\n"
            "3. Type your answer.\n"
            "4. Press Submit.\n"
            "5. Score updates automatically."
        )

        tk.Label(
            instructions_frame, text=text,
            font=("Arial", 12),
            justify="left",
            fg=self.label_fg_color, bg=self.bg_color
        ).pack(pady=10)

        tk.Button(
            instructions_frame, text="Back",
            font=("Arial", 14),
            bg=self.button_color, fg=self.button_fg_color,
            command=self.main_menu
        ).pack(pady=20)

 # Clear Frame
    def clear_frame(self):
        for w in self.root.winfo_children():
            w.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuiz(root)
    root.mainloop()
