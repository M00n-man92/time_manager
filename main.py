PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
from tkinter import *
from turtle import xcor
window=Tk()
window.title("get your self together")
window.config(padx=100,pady=50,bg=YELLOW)
phoot=PhotoImage(file='./pamadoror/tomato.png')
canvas=Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(102,110,image=phoot)
canvas.create_text(102,140,text=f"00:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.pack()

window.mainloop()