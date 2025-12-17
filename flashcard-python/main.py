from tkinter import *
import pandas
import random

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
random_word = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient= "records")

def new_word():
    global random_word,flip_timer
    my_window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text = random_word["French"], fill="black")
    canvas.itemconfig(image, image = card_front_img)
    my_window.after(3000, func=flip_card)


def flip_card():
   canvas.itemconfig(image, image=card_back_img)
   canvas.itemconfig(card_title, text="English", fill="white")
   canvas.itemconfig(card_word, text=random_word["English"], fill="white")
def is_known():
    to_learn.remove(random_word)
    new_word()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)


my_window = Tk()
my_window.title("Flashy")
my_window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = my_window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", fill = "black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

my_image_yes = PhotoImage(file="./images/right.png")
my_image_no = PhotoImage(file="./images/wrong.png")
no_button = Button(image=my_image_no, highlightthickness=0, command=new_word)
no_button.grid(row=1, column=0)
yes_button = Button(image=my_image_yes, highlightthickness=0, command=is_known)
yes_button.grid(row=1, column=1)


new_word()
my_window.mainloop()




