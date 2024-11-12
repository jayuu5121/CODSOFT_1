import random
from tkinter import *

# Initialize window
root = Tk()
root.title("ROCK, PAPER, SCISSOR GAME USING PYTHONGEEKS")
width = 700
height = 650
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
x = (window_width / 2) - (width / 2)
y = (window_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#e3f4f1")

# Update image paths
Blank_img = PhotoImage(file="E:/Projects/Source code/resources/blank.png")
Player_Rock = PhotoImage(file="E:/Projects/Source code/resources/rock_player.png")
Player_Rock_ado = Player_Rock.subsample(3, 3)
Player_Paper = PhotoImage(file="E:/Projects/Source code/resources/paper_player.png")
Player_Paper_ado = Player_Paper.subsample(3, 3)
Player_Scissor = PhotoImage(file="E:/Projects/Source code/resources/scissor_player.png")
Player_Scissor_ado = Player_Scissor.subsample(3, 3)
Computer_Rock = PhotoImage(file="E:/Projects/Source code/resources/rock_computer.png")
Computer_Paper = PhotoImage(file="E:/Projects/Source code/resources/paper_computer.png")
Computer_Scissor = PhotoImage(file="E:/Projects/Source code/resources/scissor_computer.png")

# Initialize score
player_score = 0
computer_score = 0

# Function for updating the score display
def update_score():
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}")

# Function for making rock, paper, scissor
def Rock():
    global player_option
    player_option = 1
    Image_Player.configure(image=Player_Rock)
    Matching() 

def Paper():
    global player_option
    player_option = 2
    Image_Player.configure(image=Player_Paper)
    Matching() 

def Scissor():
    global player_option
    player_option = 3
    Image_Player.configure(image=Player_Scissor)
    Matching()

# Function for making rock, paper, scissor for computer
def Comp_Rock():
    global computer_score, player_score
    if player_option == 1:
        Label_Status.config(text="Game Tie")
    elif player_option == 2:
        Label_Status.config(text="Player Win")
        player_score += 1
    elif player_option == 3:
        Label_Status.config(text="Computer Win")
        computer_score += 1
    update_score()

def Comp_Paper():
    global computer_score, player_score
    if player_option == 1:
        Label_Status.config(text="Computer Win")
        computer_score += 1
    elif player_option == 2:
        Label_Status.config(text="Game Tie")
    elif player_option == 3:
        Label_Status.config(text="Player Win")
        player_score += 1
    update_score()

def Comp_Scissor():
    global computer_score, player_score
    if player_option == 1:
        Label_Status.config(text="Player Win")
        player_score += 1
    elif player_option == 2:
        Label_Status.config(text="Computer Win")
        computer_score += 1
    elif player_option == 3:
        Label_Status.config(text="Game Tie")
    update_score()

# Function for matching
def Matching():
    computer_option = random.randint(1, 3)
    if computer_option == 1:
        Image_Computer.configure(image=Computer_Rock)
        Comp_Rock()
    elif computer_option == 2:
        Image_Computer.configure(image=Computer_Paper)
        Comp_Paper()
    elif computer_option == 3:
        Image_Computer.configure(image=Computer_Scissor)
        Comp_Scissor()

# Function to reset the game
def Restart():
    global player_option, player_score, computer_score
    player_option = 0
    player_score = 0
    computer_score = 0
    update_score()
    Label_Status.config(text="")
    Image_Player.configure(image=Blank_img)
    Image_Computer.configure(image=Blank_img)

# Function to reset the game for another round without clearing the status
def TryAgain():
    global player_option
    player_option = 0
    Label_Status.config(text="")
    Image_Player.configure(image=Blank_img)
    Image_Computer.configure(image=Blank_img)

# Function to exit the game
def Exit():
    root.destroy()
    exit()

# UI components
Image_Player = Label(root, image=Blank_img)
Image_Computer = Label(root, image=Blank_img)
Label_Player = Label(root, text="PLAYER")
Label_Player.grid(row=1, column=1)
Label_Player.config(bg="#e8c1c7", fg="black", font=('Times New Roman', 18, 'bold'))
Label_Computer = Label(root, text="COMPUTER")
Label_Computer.grid(row=1, column=3)
Label_Computer.config(bg="#e8c1c7", fg="black", font=('Times New Roman', 18, 'bold'))
Label_Status = Label(root, text="", font=('Times New Roman', 12))
Label_Status.config(fg="black", font=('Times New Roman', 20, 'bold','italic'))
Image_Player.grid(row=2, column=1, padx=30, pady=20)
Image_Computer.grid(row=2, column=3, pady=20)
Label_Status.grid(row=3, column=2)

# Score label
score_label = Label(root, text="Player: 0  |  Computer: 0", font=('Times New Roman', 16, 'bold'))
score_label.grid(row=0, column=1, columnspan=3, pady=10)

# Buttons for rock, paper, scissor
rock = Button(root, image=Player_Rock_ado, command=Rock)
paper = Button(root, image=Player_Paper_ado, command=Paper)
scissor = Button(root, image=Player_Scissor_ado, command=Scissor)
button_quit = Button(root, text="Quit", bg="red", fg="white", font=('Times New Roman', 18, 'bold'), command=Exit)

rock.grid(row=4, column=1, pady=30, padx=10)
paper.grid(row=4, column=2, pady=30, padx=10)
scissor.grid(row=4, column=3, pady=30, padx=10)
button_quit.grid(row=5, column=2, pady=20)

# Buttons for restart, try again, and quit
button_restart = Button(root, text="Restart", bg="green", fg="white", font=('Times New Roman', 18, 'bold'), command=Restart)
button_try_again = Button(root, text="Try Again", bg="yellow", fg="black", font=('Times New Roman', 18, 'bold'), command=TryAgain)
button_restart.grid(row=5, column=1, pady=20, padx=10)
button_try_again.grid(row=5, column=3, pady=20, padx=10)

# Main loop
if __name__ == '__main__':
    root.mainloop()
