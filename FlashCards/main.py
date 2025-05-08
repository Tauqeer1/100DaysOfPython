from tkinter import *
import pandas as pd
from pandas.errors import EmptyDataError
import random

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- FUNCTIONALITY ------------------------------- #

try:
    data_frame = pd.read_csv('data/words_to_learn.csv')
except (FileNotFoundError, EmptyDataError):
    data_frame = pd.read_csv('data/french_words.csv')
    records_dict = data_frame.to_dict(orient='records')
else:
    records_dict = data_frame.to_dict(orient='records')


current_card = {}


def known_word():
    records_dict.remove(current_card)
    remaining_data = pd.DataFrame(records_dict)
    remaining_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(records_dict)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title,fill="black", text=f"French")
    canvas.itemconfig(card_word,fill="black", text=f"{current_card['French']}")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title,fill="white", text=f"English")
    canvas.itemconfig(card_word,fill="white", text=f"{current_card['English']}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")


wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)


right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, borderwidth=0, command=known_word)
right_button.grid(row=1, column=1)



next_card()

window.mainloop()
