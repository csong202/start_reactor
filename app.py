import random
import time
from tkinter import *
from PIL import ImageTk, Image

'''
CURRENT PROBLEMS
- blue does not disappear and reappear when same square is repeated in the sequence
- disabling input frame during wrong_ans looks bad aesthetically

TO DO
Aesthetic
- somehow set frame background to an image
- space out progress lbls properly
- add pale border around solution_frame
- fix the colour between btns to match the frame
- somehow add sound effects??

TO DO: Making code better
- rename some functions (check_ans, get_user_ans)
'''

def reset_game():
    global user_ans, answered
    change_all_prog_lbls(img_grey)
    user_ans = []
    answered = False
    for item in lbl_list:
        item.configure(image=img_black)
        item.update()

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

def play_game():
    reset_game()
    for turn in range(1,6):
        # display solution
        change_prog_lbl(img_green, progL_list[turn-1])
        display_solution(turn)

        # prompt user for an answer
        get_user_ans(turn)

def display_solution(n):
    '''
    n = current iteration, 1 <= n < 6
    '''
    print(f"\nn = {n}")
    change_progR_lbls(img_grey)
    for i in range(n):  # 0 <= i < 5
        global x
        global y

        x = correct_sequence[i][1]
        y = correct_sequence[i][0]
        print(f"i = {i}, x = {x}, y = {y}")

        show_curr_sqr(x,y,img_blue)
        time.sleep(1)
        show_curr_sqr(x,y,img_black)

def show_curr_sqr(x,y,img):
    '''
    (int, int, image) -> None
    '''
    curr_sqr_pos = img_positions.index([y, x])  # 0 <= < 9
    curr_sqr = lbl_list[curr_sqr_pos]
    curr_sqr.configure(image=img)
    curr_sqr.update()

def get_user_ans(n):
    '''
    n = current iteration, 1 <= n < 6
    '''
    global answered

    # user guesses
    for i in range(n):
        prompt_response(i, n)
        if correct_sequence[i] == user_ans:
            print("CORRECT!")
        else:
            print(f"WRONG! Correct position was row = {correct_sequence[i][0]}, col = {correct_sequence[i][1]}")
            print(f"Your answer was row = {user_ans[0]}, col = {user_ans[1]}")
            # change_input_frame_state("normal")
            wrong_ans()
            # change_input_frame_state("disable")
        answered = False
        progR_list[i].configure(image=img_green)
        progR_list[i].update()
        if i == n - 1: time.sleep(0.5)

def prompt_response(i, n):
    while not answered:
        change_prompt_text("Please click a button")
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
    answered = True

def wrong_ans():
    change_progR_lbls(img_red_prog)
    change_all_input_btns(img_red_btn)
    time.sleep(0.5)
    change_progR_lbls(img_lgrey_prog)
    change_all_input_btns(img_lgrey_btn)
    time.sleep(0.5)
    change_progR_lbls(img_red_prog)
    change_all_input_btns(img_red_btn)
    time.sleep(0.5)
    change_progR_lbls(img_grey)
    change_all_input_btns(img_input_btn)
    time.sleep(0.5)
    change_prompt_text("You failed :(")
    play_game()

def change_input_frame_state(new_state):
    global btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9
    for child in btn_list:
        child.configure(state=new_state)

def change_prog_lbl(img, prog_lbl):
    prog_lbl.configure(image=img)
    prog_lbl.update()

def change_progL_lbls(img):
    for prog in progL_list:
        change_prog_lbl(img, prog)

def change_progR_lbls(img):
    for prog in progR_list:
        change_prog_lbl(img, prog)

def change_all_prog_lbls(img):
    change_progL_lbls(img)
    change_progR_lbls(img)

def change_all_input_btns(img):
    for btn in btn_list:
        btn.configure(image=img)
        btn.update()

def change_prompt_text(new_text):
    lbl_prompt.configure(text=new_text)
    lbl_prompt.update()

def quit_game():
    root.destroy()

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
correct_sequence = [[],[],[],[],[]]
x = 0
y = 0
correct_ans = []  # [row, col]
user_ans = []  # [row, col]
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
img_green = Image.open("images/green-btn.jpg")
img_grey = Image.open("images/grey-btn.jpg")
img_red_prog = Image.open("images/red-circle.png")
img_red_btn = Image.open("images/red-btn.png")
img_lgrey_prog = Image.open("images/light-grey-circle.png")
img_lgrey_btn = Image.open("images/light-grey-btn.png")
img_black = img_black.resize((100, 100), Image.ANTIALIAS)
img_blue = img_blue.resize((100, 100), Image.ANTIALIAS)
img_input_btn = img_input_btn.resize((90, 90), Image.ANTIALIAS)
img_green = img_green.resize((20, 20), Image.ANTIALIAS)
img_grey = img_grey.resize((20, 20), Image.ANTIALIAS)
img_red_prog = img_red_prog.resize((20, 20), Image.ANTIALIAS)
img_red_btn = img_red_btn.resize((90, 90), Image.ANTIALIAS)
img_lgrey_prog = img_lgrey_prog.resize((20, 20), Image.ANTIALIAS)
img_lgrey_btn = img_lgrey_btn.resize((90, 90), Image.ANTIALIAS)
img_black = ImageTk.PhotoImage(img_black)
img_blue = ImageTk.PhotoImage(img_blue)
img_input_btn = ImageTk.PhotoImage(img_input_btn)
img_green = ImageTk.PhotoImage(img_green)
img_grey = ImageTk.PhotoImage(img_grey)
img_red_prog = ImageTk.PhotoImage(img_red_prog)
img_red_btn = ImageTk.PhotoImage(img_red_btn)
img_lgrey_prog = ImageTk.PhotoImage(img_lgrey_prog)
img_lgrey_btn = ImageTk.PhotoImage(img_lgrey_btn)
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
prog_1L = Label(left_prog_frame, image=img_grey, borderwidth=0)
prog_2L = Label(left_prog_frame, image=img_grey, borderwidth=0)
prog_3L = Label(left_prog_frame, image=img_grey, borderwidth=0)
prog_4L = Label(left_prog_frame, image=img_grey, borderwidth=0)
prog_5L = Label(left_prog_frame, image=img_grey, borderwidth=0)
lbl_emptyL = Label(left_prog_frame, text="", bg="#ACACAC")
# progress labels right
prog_1R = Label(right_prog_frame, image=img_grey, borderwidth=0)
prog_2R = Label(right_prog_frame, image=img_grey, borderwidth=0)
prog_3R = Label(right_prog_frame, image=img_grey, borderwidth=0)
prog_4R = Label(right_prog_frame, image=img_grey, borderwidth=0)
prog_5R = Label(right_prog_frame, image=img_grey, borderwidth=0)
lbl_emptyR = Label(right_prog_frame, text="", bg="#ACACAC")

# more global variables
lbl_list = [lbl_1, lbl_2, lbl_3, lbl_4, lbl_5, lbl_6, lbl_7, lbl_8, lbl_9]
btn_list = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]
progL_list = [prog_1L, prog_2L, prog_3L, prog_4L, prog_5L]
progR_list = [prog_1R, prog_2R, prog_3R, prog_4R, prog_5R]

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

