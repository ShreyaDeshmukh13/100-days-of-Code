from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=(FONT_NAME, 12, "bold")
        )
        self.score_label.grid(row=0, column=1, sticky="e", pady=(0, 10))

        # Canvas (Question Box)
        self.canvas = Canvas(
            width=350,
            height=250,
            bg="white",
            highlightthickness=0
        )
        self.question_text = self.canvas.create_text(
            175,
            125,
            width=300,
            text="Question text",
            fill=THEME_COLOR,
            font=(FONT_NAME, 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Images (IMPORTANT: keep reference)
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        # Buttons
        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            bd=0,
            cursor="hand2",
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0, padx=20, pady=10)

        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            bd=0,
            cursor="hand2",
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1, padx=20, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(
                self.question_text,
                text="🎉 You've completed the quiz!"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#28a745")  # green
        else:
            self.canvas.config(bg="#dc3545")  # red

        self.window.after(800, self.get_next_question)