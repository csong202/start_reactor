import random
import threading
import time
from tkinter import *
from PIL import ImageTk, Image  # python image library, still have to install Pillow

'''
CURRENT PROBLEMS
- display_solutions() doesnt work
- blue isnt disappearing
'''

# function to choose random positions 
def choose_sequence():
    for i in range(0,5):
        row_correct = random.randint(0,2)
        col_correct = random.randint(0,2)
        correct_sequence[i] = [row_correct,col_correct]
        arr_correct[row_correct][col_correct] = 1
    
    for row in range(0,3):
        print(f"{arr_correct[row][0]}\t{arr_correct[row][1]}\t{arr_correct[row][2]}")

    print(f"\n{correct_sequence}")

    get_user_ans()

def display_solution(n):
    '''
    n = current iteration
    '''
    print(f"\nn = {n}")
    for i in range(n):
        global lbl_1
        global lbl_2
        global lbl_3
        global lbl_4
        global lbl_5
        global lbl_6
        global lbl_7
        global lbl_8
        global lbl_9
        global x
        global y
        '''
        if statement to see which button in correct_sequence is being shown
        use timer to set picture to img_blue
        then back to img_black
        '''
        x = correct_sequence[i][1]
        y = correct_sequence[i][0]
        print(f"x = {x}, y = {y}")

        if x == 0 and y == 0:
            lbl_1 = Label(solution_frame, image=img_blue, borderwidth=0)
        elif x == 1 and y == 0:
            lbl_2 = Label(solution_frame, image=img_blue, borderwidth=0)
        elif x == 2 and y == 0:
            lbl_3 = Label(solution_frame, image=img_blue, borderwidth=0)
        elif x == 0 and y == 1:
            lbl_4 = Label(solution_frame, image=img_blue, borderwidth=0)
        elif x == 1 and y == 1:
            lbl_5 = Label(solution_frame, image=img_blue, borderwidth=0)
        elif x == 2 and y == 1:
            lbl_6 = Label(solution_frame, image=img_blue, borderwidth=0)
        elif x == 0 and y == 2:
            lbl_7 = Label(solution_frame, image=img_blue, borderwidth=0)
        elif x == 1 and y == 2:
            lbl_8 = Label(solution_frame, image=img_blue, borderwidth=0)
        elif x == 2 and y == 2:
            lbl_9 = Label(solution_frame, image=img_blue, borderwidth=0)

        lbl_1.grid(row=0, column=0)
        lbl_2.grid(row=0, column=1)
        lbl_3.grid(row=0, column=2)
        lbl_4.grid(row=1, column=0)
        lbl_5.grid(row=1, column=1)
        lbl_6.grid(row=1, column=2)
        lbl_7.grid(row=2, column=0)
        lbl_8.grid(row=2, column=1)
        lbl_9.grid(row=2, column=2)

        timer = threading.Timer(2.0, hide_sol)
        timer.start()

        # prompt user for an answer
        get_user_response(i)

def hide_sol():
    '''
    if statement to make on of the lbl's images
    turn from blue to black
    '''
    # print("hiding blue")
    global lbl_1
    global lbl_2
    global lbl_3
    global lbl_4
    global lbl_5
    global lbl_6
    global lbl_7
    global lbl_8
    global lbl_9
    global x
    global y

    if x == 0 and y == 0:
        lbl_1 = Label(solution_frame, image=img_black, borderwidth=0)
    elif x == 1 and y == 0:
        lbl_2 = Label(solution_frame, image=img_black, borderwidth=0)
    elif x == 2 and y == 0:
        lbl_3 = Label(solution_frame, image=img_black, borderwidth=0)
    elif x == 0 and y == 1:
        lbl_4 = Label(solution_frame, image=img_black, borderwidth=0)
    elif x == 1 and y == 1:
        lbl_5 = Label(solution_frame, image=img_black, borderwidth=0)
    elif x == 2 and y == 1:
        lbl_6 = Label(solution_frame, image=img_black, borderwidth=0)
    elif x == 0 and y == 2:
        lbl_7 = Label(solution_frame, image=img_black, borderwidth=0)
    elif x == 1 and y == 2:
        lbl_8 = Label(solution_frame, image=img_black, borderwidth=0)
    elif x == 2 and y == 2:
        lbl_9 = Label(solution_frame, image=img_black, borderwidth=0)

    lbl_1.grid(row=0, column=0)
    lbl_2.grid(row=0, column=1)
    lbl_3.grid(row=0, column=2)
    lbl_4.grid(row=1, column=0)
    lbl_5.grid(row=1, column=1)
    lbl_6.grid(row=1, column=2)
    lbl_7.grid(row=2, column=0)
    lbl_8.grid(row=2, column=1)
    lbl_9.grid(row=2, column=2)

def get_user_ans():
    for turn in range(5):
        display_solution(turn+1)
        # get user response

def get_user_response(turn):
    # 1 <= turn <= 5
    '''
    - undisable input_frame
    - user clicks button
    '''
    pass

def check_answer():
    pass

# ------ GLOBAL VARIABLES ---------

arr_correct = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
arr_response = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
correct_sequence = [[],[],[],[],[]]
x = 0
y = 0

######################################
# SET UP TKINTER
######################################
root = Tk()
root.title("Reactor Task - SIMON SAYS")
root.iconbitmap('icons/os_linux_icon.ico')
root.geometry("1100x600")
root.resizable(False, False)

# ------- CREATING WIDGETS -----
btn_start = Button(root, text="START", padx=12, pady=12, bg="#ACACAC", fg="black", command=choose_sequence)
# frames
left_frame = LabelFrame(root, text="", padx=15, pady=15, bg="#ACACAC")
left_prog_frame = LabelFrame(left_frame, text="", padx=5, pady=5, bg="#ACACAC", relief=FLAT)
solution_frame = LabelFrame(left_frame, text="", padx=5, pady=5, bg="black", relief=FLAT)
right_frame = LabelFrame(root, text="", padx=15, pady=15, bg="#ACACAC")
right_prog_frame = LabelFrame(right_frame, text="", padx=5, pady=5, bg="#ACACAC", relief=FLAT)
input_frame = LabelFrame(right_frame, text="", padx=5, pady=5, bg="#ACACAC", relief=FLAT)
# images
img_black = Image.open("images/black-square.jpg")
img_blue = Image.open("images/blue-square.jpg")
img_input_btn = Image.open("images/input_btn.jpg")
img_green_btn = Image.open("images/green-btn.jpg")
img_grey_btn = Image.open("images/grey-btn.jpg")
img_black = img_black.resize((100,100), Image.ANTIALIAS)
img_blue = img_blue.resize((100,100), Image.ANTIALIAS)
img_input_btn = img_input_btn.resize((90,90), Image.ANTIALIAS)
img_green_btn = img_green_btn.resize((20,20), Image.ANTIALIAS)
img_grey_btn = img_grey_btn.resize((20,20), Image.ANTIALIAS)
img_black = ImageTk.PhotoImage(img_black)
img_blue = ImageTk.PhotoImage(img_blue)
img_input_btn = ImageTk.PhotoImage(img_input_btn)
img_green_btn = ImageTk.PhotoImage(img_green_btn)
img_grey_btn = ImageTk.PhotoImage(img_grey_btn)
# labels for displaying pattern
lbl_1 = Label(solution_frame, image=img_black, borderwidth=0)
lbl_2 = Label(solution_frame, image=img_black, borderwidth=0)
lbl_3 = Label(solution_frame, image=img_black, borderwidth=0)
lbl_4 = Label(solution_frame, image=img_black, borderwidth=0)
lbl_5 = Label(solution_frame, image=img_black, borderwidth=0)
lbl_6 = Label(solution_frame, image=img_black, borderwidth=0)
lbl_7 = Label(solution_frame, image=img_black, borderwidth=0)
lbl_8 = Label(solution_frame, image=img_black, borderwidth=0)
lbl_9 = Label(solution_frame, image=img_black, borderwidth=0)
# buttons for entering solution
btn_1 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=check_answer)
btn_2 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=check_answer)
btn_3 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=check_answer)
btn_4 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=check_answer)
btn_5 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=check_answer)
btn_6 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=check_answer)
btn_7 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=check_answer)
btn_8 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=check_answer)
btn_9 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=check_answer)

# progress labels left
prog_1L = Label(left_prog_frame, image=img_grey_btn, borderwidth=0)
prog_2L = Label(left_prog_frame, image=img_grey_btn, borderwidth=0)
prog_3L = Label(left_prog_frame, image=img_grey_btn, borderwidth=0)
prog_4L = Label(left_prog_frame, image=img_grey_btn, borderwidth=0)
prog_5L = Label(left_prog_frame, image=img_grey_btn, borderwidth=0)
lbl_emptyL = Label(left_prog_frame, text="", bg="#ACACAC")
# progress labels right
prog_1R = Label(right_prog_frame, image=img_grey_btn, borderwidth=0)
prog_2R = Label(right_prog_frame, image=img_grey_btn, borderwidth=0)
prog_3R = Label(right_prog_frame, image=img_grey_btn, borderwidth=0)
prog_4R = Label(right_prog_frame, image=img_grey_btn, borderwidth=0)
prog_5R = Label(right_prog_frame, image=img_grey_btn, borderwidth=0)
lbl_emptyR = Label(right_prog_frame, text="", bg="#ACACAC")

# -------- DISPLAYING WIDGETS --------
btn_start.grid(row=5,column=0)
# frames
left_frame.grid(row=0, column=0)
left_prog_frame.grid(row=1, column=0)
solution_frame.grid(row=2, column=0)
right_frame.grid(row=0, column=1)
right_prog_frame.grid(row=1, column=1)
input_frame.grid(row=2, column=1)
# solution frame - labels
lbl_1.grid(row=0, column=0)
lbl_2.grid(row=0, column=1)
lbl_3.grid(row=0, column=2)
lbl_4.grid(row=1, column=0)
lbl_5.grid(row=1, column=1)
lbl_6.grid(row=1, column=2)
lbl_7.grid(row=2, column=0)
lbl_8.grid(row=2, column=1)
lbl_9.grid(row=2, column=2)
# input frame - buttons
btn_1.grid(row=0, column=0)
btn_2.grid(row=0, column=1)
btn_3.grid(row=0, column=2)
btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)

# left frame - progress labels
prog_1L.grid(row=0,column=0)
prog_2L.grid(row=0,column=1)
prog_3L.grid(row=0,column=2)
prog_4L.grid(row=0,column=3)
prog_5L.grid(row=0,column=4)
lbl_emptyL.grid(row=1,column=0)
# right frame - progress labels
prog_1R.grid(row=0,column=0)
prog_2R.grid(row=0,column=1)
prog_3R.grid(row=0,column=2)
prog_4R.grid(row=0,column=3)
prog_5R.grid(row=0,column=4)
lbl_emptyR.grid(row=1,column=0)


# ------MAIN-------
# run gui
root.mainloop()

