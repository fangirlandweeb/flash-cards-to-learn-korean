from tkinter import *
import pandas
from random import *

LANG_FONT = ("Arial", 20, "italic")
TEXT_FONT = ("Arial", 40, "bold")

def right_answer():
    if random_word in word_meanings:
        word_meanings.remove(random_word)
    else:
        generate_random_word()
    print(len(word_meanings))

    unknown_words = pandas.DataFrame(word_meanings)
    unknown_words.to_csv("unknown_words.csv")

    generate_random_word()


def wrong_answer():
    generate_random_word()

random_word = {}
def generate_random_word():
    global random_word, timer

    window.after_cancel(timer)

    random_word = choice(word_meanings)
    canvas.config(bg="light green", highlightcolor="green")
    canvas.itemconfig(language, text="Korean", fill="white")
    canvas.itemconfig(word, text=random_word["Korean"])

    window.after(5000, func=reveal_answer)

def reveal_answer():
    canvas.config(bg="white", highlightcolor="green")
    canvas.itemconfig(language, fill="light green", font=LANG_FONT, text="English")
    canvas.itemconfig(word, text=random_word["English"])

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg="pink")
canvas = Canvas(width=500, height=300, bg="light green", highlightthickness=10, highlightcolor="blue")
#snopth out edges of rectangle  canvas.create_line()
language = canvas.create_text(245, 75, text="Language", fill="white", font=LANG_FONT)
word = canvas.create_text(245, 185, text="Word", font=TEXT_FONT)
canvas.grid(row=0, column=0, columnspan=2)

tick_mark = Button()
tick_mark.config(width=10, height=3, text="✔", bg="green", fg="white", command=right_answer)
tick_mark.grid(row=1, column=0)

x_mark = Button()
x_mark.config(width=10, height=3, text="❌", bg="red", fg="white", command=wrong_answer)
x_mark.grid(row=1, column=1)

data = pandas.read_csv("korean flashcard.csv")
word_meanings = data.to_dict(orient="records")

timer = window.after(5000, func=reveal_answer)
window.mainloop()
