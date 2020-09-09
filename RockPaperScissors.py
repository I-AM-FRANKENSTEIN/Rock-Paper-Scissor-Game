import random

def userChoice():               # userChoice()is the function for choosing Rock/Paper/Scissors from the user
    player_choice=input("Enter your choice:- ")
    while not (player_choice=="rock" or player_choice=="paper" or player_choice=="scissors"):
        print("Enter your choice again")
        player_choice=input("Enter your choice:- ")
    return player_choice
def botChoice():                #botChoice() is the function for selecting random choice from Rock/Paper/Scissors
    lst=["rock","paper","scissors"]
    bot_choice=random.choice(lst)
    return bot_choice
def gameLogic(player,bot):      #gameLogic() is the function that contains the winning combinations of RPS game
    if player=="rock" and bot=="rock":
        return "draw"
    elif player=="rock" and bot=="paper":
        return "bot"
    elif player=="rock" and bot=="scissors":
        return "player"
    elif player== "paper" and bot=="scissors":
        return "bot"
    elif player=="paper" and bot=="rock":
        return "player"
    elif player=="paper" and bot=="paper":
        return "draw"
    elif player=="scissors" and bot=="rock":
        return "bot"
    elif player=="scissors" and bot=="paper":
        return "player"
    elif player=="scissors" and bot=="scissors":
        return "draw"
    else:
        return "invalid"
def RPS():                       #RPS() is the function that manages and update the scoreboard of the game
    repeat="y"
    user_score=0
    bot_score=0
    while repeat!="n":
        x=userChoice()
        y=botChoice()
        print("User Choice-->",x)
        print("Bot Choice-->",y)
        winner=gameLogic(x,y)
        if winner=="player":
            user_score+=1
        elif winner=="bot":
            bot_score+=1
        else:
            user_score+=0
            bot_score+=0
        print("\n\n-----SCOREBOARD-----")
        print("USER SCORE -",user_score)
        print("BOT SCORE -",bot_score)
        if winner=="bot":
            print("\nBOT WON!!")
        elif winner=="player":
            print("\nYOU WON!!")
        else:
            print("\nMATCH DRAW!!")
        repeat=input("Do you want to continue:(y/n):- ")

RPS()                            #RPS() function call 