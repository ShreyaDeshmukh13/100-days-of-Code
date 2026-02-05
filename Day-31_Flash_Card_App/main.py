from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError :
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text,text="French",fill = "black")
    canvas.itemconfig(word_text,text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card , flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background ,image = card_back)
    canvas.itemconfig(title_text, text="English",fill = "white")
    canvas.itemconfig(word_text, text=current_card["English"])

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index = False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg= BACKGROUND_COLOR)
flip_timer = window.after(3000,func = flip_card)

canvas =  Canvas(width=800,height=526)
card_front =  PhotoImage(file = "images/card_front.png")
card_back =  PhotoImage(file = "images/card_back.png")
canvas.config(bg= BACKGROUND_COLOR, highlightthickness = 0)
card_background = canvas.create_image(410,270,image=card_front)

title_text = canvas.create_text(400,150,text = "" , font = (FONT_NAME,40 ,"italic"))
word_text = canvas.create_text(400, 263, text="", font = (FONT_NAME, 60,"bold"))


canvas.grid(column=0,row=0,columnspan = 2 ,sticky = "w")

right = PhotoImage(file = "images/right.png")
wrong = PhotoImage(file = "images/wrong.png")
right_button = Button(image = right , highlightthickness = 0 , command =next_card)
wrong_button = Button(image = wrong, highlightthickness = 0 ,  command =is_known)
right_button.grid(column=1,row=1)
wrong_button.grid(column=0,row=1)








next_card()



window.mainloop()