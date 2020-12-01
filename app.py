import random
from tkinter import *
from PIL import ImageTk, Image  # python image library, still have to install Pillow

'''
CURRENT PROBLEMS
- solutions do not appear in the order they were generated in
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

def display_solution(n):
    '''
    n = current iteration
    '''
    # for i in range(0,5):
    #     curr_line = lines_correct[correct_sequence[i][0]*3+2]
    #     lines_correct[correct_sequence[i][0]*3+2]=curr_line[:correct_sequence[i][1]*6+2] + "###" + curr_line[correct_sequence[i][1]*6+5:]

    #     # print solution
    #     for line in range(0,14):
    #         print(lines_correct[line])
    for i in range(n):
        '''
        if statement to see which button in correct_sequence is being shown
        use timer to set picture to img_blue for a second
        then back to img_black
        '''
        pass

def display_user_reponse():
    # print grid with 1 filled square   
    pass

def check_user_reponse():
    pass

# global variables

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

######################################
# SET UP TKINTER
######################################
root = Tk()
root.title("Reactor Task - SIMON SAYS")
root.iconbitmap('icons/os_linux_icon.ico')
root.geometry("1100x600")
root.resizable(False, False)

# -------CREATING WIDGETS-----
# frames
left_frame = LabelFrame(root, text="", padx=5, pady=5, bg="#A3A3A3")
solution_frame = LabelFrame(left_frame, text="", padx=5, pady=5, bg="black")
right_frame = LabelFrame(root, text="", padx=5, pady=5, bg="#A3A3A3")
input_frame = LabelFrame(right_frame, text="", padx=5, pady=5, bg="#A3A3A3")
# images
img_black = Image.open("images/black-square.jpg")
img_blue = Image.open("images/blue-square.jpg")
img_input_btn = Image.open("images/input_btn.jpg")
img_black = img_black.resize((100,100), Image.ANTIALIAS)
img_blue = img_blue.resize((100,100), Image.ANTIALIAS)
img_input_btn = img_input_btn.resize((90,90), Image.ANTIALIAS)
img_black = ImageTk.PhotoImage(img_black)
img_blue = ImageTk.PhotoImage(img_blue)
img_input_btn = ImageTk.PhotoImage(img_input_btn)
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
btn_1 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT)
btn_2 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT)
btn_3 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT)
btn_4 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT)
btn_5 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT)
btn_6 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT)
btn_7 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT)
btn_8 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT)
btn_9 = Button(input_frame, image=img_input_btn, borderwidth=3, relief=FLAT)

# DISPLAYING WIDGETS
# frames
left_frame.grid(row=0, column=0)
solution_frame.grid(row=2, column=0)
right_frame.grid(row=0, column=1)
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

# ------MAIN-------
# run gui
root.mainloop()

# generate solution
choose_sequence()

# get user response
# looping through each list in correct_sequence
# for n in range(0,5):
#
#     display_solution(n)
#
#     # ask user to input where it was
#     for j in range(0,n):
#         print(f"n = {n}")
#
#         user_guess_row = int(input("Please enter a row: "))
#         user_guess_col = int(input("Please enter a column: "))
#
#         user_guess = [user_guess_row, user_guess_col]
#         print(f"user_guess = {user_guess}, correct_sequence[j] = {correct_sequence[j]}")
#
#         if user_guess == correct_sequence[j]:
#             print("You are correct!")
#         else:
#             print("incorrect")

