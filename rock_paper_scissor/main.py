
from tkinter import *
from PIL import Image , ImageTk                            
from random import randint

root = Tk()
# Tk() is the constructor for the Tkinter class that represents the main window of the application.
root.title("Rock-Paper-Scissor")
root.configure(background = "black")

rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor.png"))

# insert picture
user_label = Label(root , image=scissor_img , bg="black")
comp_label = Label(root , image=scissor_img_comp , bg="black")
comp_label.grid(row=1 , column=0)
user_label.grid(row=1 , column=4)

# scores
player_score = Label(root , text=0 , font=100 , bg="black" , fg="white")
comp_score = Label(root , text=0 , font=100 , bg="black" , fg="white")
comp_score.grid(row=1 , column=1)
player_score.grid(row=1 , column=3)

# indicators
user_indicator = Label(root,font=50,text="USER")
comp_indicator = Label(root,font=50,text="COMPUTER")
user_indicator.grid(row=0 , column=3)
comp_indicator.grid(row=0 , column=1)

# messages
msg = Label(root , font=50 , bg="black" , fg="white")
msg.grid(row=3 , column=2)

# update message
def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore():
    score = int(player_score["text"])
    score += 1
    player_score["text"] = str(score)
# update computer score
def updateCompScore():
    score = int(comp_score["text"])
    score += 1
    comp_score["text"] = str(score)

# check winner
def checkWin(player , computer):
    if player == computer:
        updateMessage("It's a tie!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose!!")
            updateCompScore()
        else:
            updateMessage("You win!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose!!")
            updateCompScore()
        else:
            updateMessage("You win!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose!!")
            updateCompScore()
        else:
            updateMessage("You win!!")
            updateUserScore()
    else:
        pass

# update choices
choices = ["rock" , "paper" , "scissor"]
def updateChoice(x):

    # for computer
    comp_choice  = choices[randint(0,2)]
    if comp_choice == "rock":
        comp_label.configure(image = rock_img_comp)
    elif comp_choice == "paper":
        comp_label.configure(image = paper_img_comp)
    else:
        comp_label.configure(image = scissor_img_comp)


    # for user
    if x == "rock":
        user_label.configure(image = rock_img)
    elif x == "paper":
        user_label.configure(image = paper_img)
    else:
        user_label.configure(image = scissor_img)

    checkWin(x , comp_choice)

rock = Button(root , width=20 , height=2 , text="ROCK" , bg="#DE3163", fg="black" , command=lambda:updateChoice("rock")).grid(row=2 , column=1)
paper = Button(root , width=20 , height=2 , text="PAPER" , bg="#FDDA0D" , fg="black" , command=lambda:updateChoice("paper")).grid(row=2 , column=2)
scissor = Button(root , width=20 , height=2 , text="SCISSOR" , bg="#00bfff" , fg="black" , command=lambda:updateChoice("scissor")).grid(row=2 , column=3)

root.mainloop()