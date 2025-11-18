import tkinter as tk
import random

class JokeApp:
    def __init__(self, master):
        self.master = master
        master.title("Alexa, Tell Me a Joke!")
        master.geometry("520x330")
        master.configure(bg="#d9ecff")

        # Joke list
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "What's orange and sounds like a parrot? A carrot.",
            "Why did the bicycle fall over? Because it was two tired!",
            "What do you call a sad strawberry? A blueberry.",
            "How do you catch a squirrel? Climb a tree and act like a nut!"
        ]

        # Title
        self.label_title = tk.Label(
            master, text="Alexa Joke Machine 🤖",
            font=("Arial", 20, "bold"),
            bg="#d9ecff",
            fg="black"
        )
        self.label_title.pack(pady=10)

        # Joke button
        self.button_joke = tk.Button(
            master, text="Tell Me a Joke!", command=self.start_joke_animation,
            font=("Arial", 15), bg="#4CAF50", fg="white",
            activebackground="#45a049", bd=3
        )
        self.button_joke.pack(pady=(5, 10))

        # Hover scaling
        self.button_joke.bind("<Enter>", lambda e: self.button_joke.config(font=("Arial", 16)))
        self.button_joke.bind("<Leave>", lambda e: self.button_joke.config(font=("Arial", 15)))

        # Joke label (start lower so layout is clean)
        self.label_joke = tk.Label(
            master, text="Press the button to hear a joke!",
            font=("Arial", 15), bg="#d9ecff", fg="black", wraplength=480
        )
        self.label_joke.pack(pady=5)

        # Quit button
        self.button_quit = tk.Button(
            master, text="Quit", command=master.quit,
            font=("Arial", 12), bg="#e63946", fg="white",
            activebackground="#c81928", bd=3
        )
        self.button_quit.pack(pady=10)

    # -------------------------------------------------------
    # ANIMATION CONTROLLER
    # -------------------------------------------------------
    def start_joke_animation(self):
        joke = random.choice(self.jokes)

        # Reset joke label color
        self.label_joke.config(fg="#000000")

        self.button_bounce()
        self.fade_in_text(joke, opacity=0)
        self.color_pulse(step=0, forward=True)

    # Fade in text smoothly
    def fade_in_text(self, text, opacity):
        if opacity == 0:
            self.label_joke.config(text=text)

        if opacity <= 1:
            # fade from light gray to black
            gray = int(150 - opacity * 150)
            color = f"#{gray:02x}{gray:02x}{gray:02x}"
            self.label_joke.config(fg=color)
            self.master.after(25, lambda: self.fade_in_text(text, opacity + 0.08))
        else:
            self.label_joke.config(fg="black")

    # Background glow animation
    def color_pulse(self, step, forward):
        blue_value = 240 - step
        color = f"#d9ec{blue_value:02x}"

        self.master.configure(bg=color)
        self.label_title.configure(bg=color)
        self.label_joke.configure(bg=color)
        self.button_joke.configure(bg="#4CAF50")
        self.button_quit.configure(bg="#e63946")

        if forward and step < 20:
            self.master.after(20, lambda: self.color_pulse(step + 2, True))
        elif not forward and step > 0:
            self.master.after(20, lambda: self.color_pulse(step - 2, False))
        elif forward:
            self.master.after(20, lambda: self.color_pulse(step, False))

    # Button bounce animation
    def button_bounce(self, step=0, grow=True):
        size = 15 + step
        self.button_joke.config(font=("Arial", size))

        if grow and step < 3:
            self.master.after(40, lambda: self.button_bounce(step + 1, True))
        elif not grow and step > 0:
            self.master.after(40, lambda: self.button_bounce(step - 1, False))
        elif grow:
            self.master.after(40, lambda: self.button_bounce(step, False))


# MAIN
if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()
