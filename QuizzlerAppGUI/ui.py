from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.card_text = self.canvas.create_text(150, 125, text="text", font=("Ariel", 20, "italic"), width=280, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, borderwidth=0, command=self.choose_true)
        self.true_button.grid(row=2, column=0)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, borderwidth=0, command=self.choose_false)
        self.false_button.grid(row=2, column=1)


        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.card_text, text=q_text)
        else:
            self.canvas.itemconfig(self.card_text, text="Quiz Completed")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def choose_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)


    def choose_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
