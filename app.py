import random
import threading
import time
from tkinter import *
from PIL import ImageTk, Image

'''
CURRENT PROBLEMS
- doesn't show blue square for long enough
- doesnt re display blue squares on next turn
- cant quit after while play_game is running

TO DO
- restart game if user is wrong (same sequence??)
- blue squares flash red when player clicks incorrect button
- restart game if user hits start (new sequence)
'''

# function to choose random positions 
def choose_sequence():
    print("\n----NEW GAME----")
    for i in range(0,5):
        row_correct = random.randint(0,2)
        col_correct = random.randint(0,2)
        correct_sequence[i] = [row_correct,col_correct]
        arr_correct[row_correct][col_correct] = 1
    
    for row in range(0,3):
        print(f"{arr_correct[row][0]}\t{arr_correct[row][1]}\t{arr_correct[row][2]}")

    print(f"\n{correct_sequence}")

    play_game()

def display_solution(n):
    '''
    n = current iteration, 1 <= n < 6
    '''
    print(f"\nn = {n}")
    for i in range(n):  # 0 <= i < 5
        global x
        global y
        '''
        if statement to see which button in correct_sequence is being shown
        use timer to set picture to img_blue
        then back to img_black
        '''

        x = correct_sequence[i][1]
        y = correct_sequence[i][0]
        print(f"i = {i}, x = {x}, y = {y}")

        show_curr_sqr(x,y,img_blue)
        # print("made image blue")
        time.sleep(1)
        # show_curr_sqr(x,y,img_black)

def show_curr_sqr(x,y,img):
    '''
    (int, int, image) -> None
    '''
    global lbl_1, lbl_2, lbl_4, lbl_4, lbl_5, lbl_6, lbl_7, lbl_8, lbl_9

    curr_sqr_pos = img_positions.index([y, x])  # 0 <= < 9
    # if img == img_blue: print(f"curr_sqr_pos = {curr_sqr_pos}")

    curr_sqr = lbl_list[curr_sqr_pos]
    curr_sqr.grid_forget()
    curr_sqr = Label(solution_frame, image=img, borderwidth=0)
    curr_sqr.grid(row=img_positions[curr_sqr_pos][0], column=img_positions[curr_sqr_pos][1])

def play_game():
    for turn in range(1,6):
        # display solution
        display_solution(turn)

        # prompt user for an answer
        get_user_ans(turn)

def get_user_ans(n):
    '''
    n = current iteration, 1 <= n < 6
    - undisable input_frame
    - user clicks button
    '''
    global answered

    # user guesses
    for i in range(n):
        prompt_response(i, n)
        if correct_sequence[i] == user_ans:
            print("DING DING DING CORRECT!")
        else:
            print(f"WRONG! Correct position was row = {correct_sequence[i][0]}, col = {correct_sequence[i][1]}")
        answered = False

def prompt_response(i, n):
    while not answered:
        lbl_prompt.configure(text="Please click a button")
        lbl_prompt.update()
        change_input_frame_state("normal")
    change_input_frame_state("disable")
    if i == 4 and n == 5:
        lbl_prompt.configure(text="Finished Game")
    else:
        lbl_prompt.configure(text="Moving on...")
    lbl_prompt.update()

def check_ans(btn_num):
    '''
    btn_num range[1,9]
    btn_pos range[0,8]
    '''
    global user_ans
    global answered
    btn_pos = btn_num - 1
    user_ans = [img_positions[btn_pos][0], img_positions[btn_pos][1]]
    # arr_response[img_positions[btn_pos][0]][img_positions[btn_pos][1]] = 1
    answered = True

def change_input_frame_state(new_state):
    global btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9

    for child in btn_list:
        child.configure(state=new_state)

def quit_game():
    btn_start.configure(state="disable")
    root.quit()

# ------ GLOBAL VARIABLES ---------
img_positions = [  # [row, col]
    [0,0], [0,1], [0,2],
    [1,0], [1,1], [1,2],
    [2,0], [2,1], [2,2]
]
arr_correct = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
arr_response = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
correct_sequence = [[],[],[],[],[]]
x = 0
y = 0
correct_ans = []  # [row, col]
user_ans = []  # [row, col]
# curr_corr_seq = []
# curr_user_seq = []
answered = False

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
btn_exit = Button(root, text="QUIT", padx=12, pady=12, bg="#ACACAC", fg="black", command=quit_game)
lbl_prompt = Label(root, text="Welcome!", padx=12, pady=12)
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
img_black = img_black.resize((100, 100), Image.ANTIALIAS)
img_blue = img_blue.resize((100, 100), Image.ANTIALIAS)
img_input_btn = img_input_btn.resize((90, 90), Image.ANTIALIAS)
img_green_btn = img_green_btn.resize((20, 20), Image.ANTIALIAS)
img_grey_btn = img_grey_btn.resize((20, 20), Image.ANTIALIAS)
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
btn_1 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=lambda: check_ans(1))
btn_2 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=lambda: check_ans(2))
btn_3 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=lambda: check_ans(3))
btn_4 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=lambda: check_ans(4))
btn_5 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=lambda: check_ans(5))
btn_6 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=lambda: check_ans(6))
btn_7 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=lambda: check_ans(7))
btn_8 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=lambda: check_ans(8))
btn_9 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT, command=lambda: check_ans(9))
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

# more global variables
lbl_list = [lbl_1, lbl_2, lbl_3, lbl_4, lbl_5, lbl_6, lbl_7, lbl_8, lbl_9]
btn_list = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]

# -------- DISPLAYING WIDGETS --------
btn_start.grid(row=5, column=0)
btn_exit.grid(row=5, column=1)
lbl_prompt.grid(row=6, column=1)
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

# disable input frame
change_input_frame_state("disable")

# run gui
root.mainloop()

