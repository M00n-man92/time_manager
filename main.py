PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
w=1
r=0
mark=""
timeing=None
from tkinter import *
import time
import math

def reset_timer():
    global timeing
    global mark
    global w
    global r
    window.after_cancel(timeing)
    canvas.itemconfig(can_text,text="00 : 00")
    label_one.config(text="Timer",font=(FONT_NAME,40,"bold"),bg=YELLOW,fg=GREEN)
    label_two.config(text="")
    w=1
    r=0    
    
def start_timer():
    timerr(WORK_MIN)
    label_one.config(text="Work",font=(FONT_NAME,40,"bold"),bg=YELLOW,fg=GREEN)
def timerr(count):
    global w
    global r
    global mark
    global timeing
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        
        canvas.itemconfig(can_text,text=f"{count_min} : 0{count_sec}")
   
    else:
        canvas.itemconfig(can_text,text=f"{count_min} : {count_sec}")
    if count>0:
        timeing=window.after(1000,timerr,count-1)
    elif count==0:
        if w==r:
            if w ==4 and r==4:
                
                w=0
                r=0 
                print(f"w= {w}") 
                print(f"r= {r}")
                timerr(LONG_BREAK_MIN)
            else:
                timerr(WORK_MIN)
                w+=1
                label_one.config(text="Work",font=(FONT_NAME,40,"bold"),bg=YELLOW,fg=GREEN)
                print(f"w= {w}")
                
                
        elif w>r:
            mark+="✔"
            label_two.config(text=mark,bg=YELLOW,fg=GREEN,font=(CASCADE,15,"bold"))
            timerr(SHORT_BREAK_MIN)
            label_one.config(text="Break",font=(FONT_NAME,40,"bold"),bg=YELLOW,fg=RED)
            r+=1
            print(f"r= {r}")
            
          


window=Tk()
window.title("get your self together")
window.config(padx=100,pady=50,bg=YELLOW)

phoot=PhotoImage(file='./hour.png')
canvas=Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(102,110,image=phoot)
can_text=canvas.create_text(102,110,text=f"",fill=RED,font=(FONT_NAME,24,"bold"))
canvas.grid(column=1,row=1)
label_one=Label(text="Timer",font=(FONT_NAME,40,"bold"),bg=YELLOW,fg=GREEN)
label_one.grid(column=1,row=0)
label_two=Label(text=mark,bg=YELLOW,fg=GREEN,font=(CASCADE,15,"bold"))
label_two.grid(column=1,row=3)
button_one=Button(text="start",height=2,width=5,highlightthickness=0,command=start_timer)
button_one.grid(column=0,row=2)
button_two=Button(text="reset",height=2,width=5,highlightthickness=0,command=reset_timer)
button_two.grid(column=2,row=2)




window.mainloop()