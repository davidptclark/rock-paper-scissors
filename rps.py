import random

# Setting score variable for both computer and player
playerscore = 0
cpuscore = 0

# Store all possible outcomes in a set
outcomes = ["rock","paper","scissors"]

# Define the game
def game():
    global playerscore
    global cpuscore
    random.shuffle(outcomes)
    cpuchoice = random.choice(outcomes)

    playerchoice = input("Choose rock, paper or scissors? ")

    if playerchoice in outcomes:
        print("Player chooses " + playerchoice)
        print("Computer chooses " + cpuchoice)
    else:
        while playerchoice not in outcomes:
            playerchoice = input("Sorry, that isn't a valid option, choose rock, paper or scissors.")


    if playerchoice == cpuchoice:
        print("Draw")
    elif playerchoice =="rock" and cpuchoice =="paper":
        print("You lose")
        cpuscore += 1
    elif playerchoice == "rock" and cpuchoice == "scissors":
        print("You win")
        playerscore += 1
    elif playerchoice == "paper" and cpuchoice == "scissors":
        print("You lose")
        cpuscore += 1
    elif playerchoice == "paper" and cpuchoice == "rock":
        print("You win")
        playerscore += 1
    elif playerchoice == "scissors" and cpuchoice == "rock":
        print("You lose")
        cpuscore += 1
    elif playerchoice == "scissors" and cpuchoice == "paper":
        print("You win")
        playerscore += 1

    print("Computer: ", cpuscore)
    print("Player: ", playerscore)

    playagain = input("Do you want to play again? (y/n)")
    if playagain == "y":
        game()
    else:
        print("Thanks for playing!")

game()


