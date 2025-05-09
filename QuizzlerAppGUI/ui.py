from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.card_text = self.canvas.create_text(150, 125, text="text", font=("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, borderwidth=0)
        self.true_button.grid(row=2, column=0)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, borderwidth=0)
        self.false_button.grid(row=2, column=1)



        self.window.mainloop()



# canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# card_front_image = PhotoImage(file="images/card_front.png")
# card_back_image = PhotoImage(file="images/card_back.png")
# canvas_image = canvas.create_image(400, 263, image=card_front_image)
# canvas.grid(row=0, column=0, columnspan=2)

# card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
# card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")


# wrong_button_image = PhotoImage(file="images/wrong.png")
# wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0, command=next_card)
# wrong_button.grid(row=1, column=0)


# right_button_image = PhotoImage(file="images/right.png")
# right_button = Button(image=right_button_image, highlightthickness=0, borderwidth=0, command=known_word)
# right_button.grid(row=1, column=1)
