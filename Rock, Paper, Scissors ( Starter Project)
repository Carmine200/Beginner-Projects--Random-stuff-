from random import randint

Task = ["Rock", "Paper", "scissor"]

computer = Task[randint(0,2)]

player = False 

while player == False:


    player = input("rock, paper, scissor?")

    if player == computer:
        print("tie or something, when is lunch time?")

    elif player == "rock":
        if computer == "paper":
            print ("you lose", computer, "covers up", player)
        else:
            print("you win",player,"smashes",computer)
    elif player == "paper":
        if computer == "scissor":
            print("you lose lol", computer, "cuts through",player)
        else:
            print("you win", player, "covers up", computer)
    elif player == "scissor":
        if computer == "rock":
            print("you lose ha", computer, "smashes", player)
        else: 
            print("you win finally", player, "cut through", computer)
    else:
        print("that is not a valid play try agin later")
    
    player = False

    computer = Task[randint(0,2)]
