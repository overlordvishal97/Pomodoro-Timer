import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    # Timer title
    timer_label.config(text="Timer", fg=GREEN)
    #timer reset
    canvas.itemconfig(clock, text=f"00:00")
    #correct symbol reset
    correct_label.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    work_break = SHORT_BREAK_MIN * 60
    long_work_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_work_break)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(work_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_time)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(clock,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        timer_start()
        marks = " "
        worksession = math.floor(reps/2)
        for _ in range(worksession):
            marks += "✔"
            correct_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.grid(column=1,row=1)
#Timer
clock = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

#Timer label
timer_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
timer_label.grid(column=1,row=0)

#start button
start = Button(text="Start",highlightthickness=0,command=timer_start)
start.grid(column=0,row=2)
#Reset button
reset_button = Button(text="Reset",highlightthickness=0,command=timer_reset)
reset_button.grid(column=2,row=2)
#correct mark
correct_label=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"))
correct_label.grid(column=1,row=3)


window.mainloop()