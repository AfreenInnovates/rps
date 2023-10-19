import random 

userWins = 0
computerWins = 0
options = ["rock", "paper", "scissors"]
playAgain = True

while playAgain:
    userChoice = input("Enter Rock/Paper/Scissors to play the game and Q to quit the game: ").lower()
    
    if userChoice == 'q':
        if userWins > 0 or computerWins > 0:
            print("You won", userWins, "times!")
            print("Computer won", computerWins, "times!")
            print("Thanks for playing!")
        print("Enter ctrl+alt+N if you want to play")
        playAgain = False
    elif userChoice not in options:
        print("Please enter your choice as per the game i.e. Rock/Paper/Scissors")
    else:
        # Rock: 0 Paper: 1 Scissors: 2
        randomNumber = random.randint(0, 2)
        computerPick = options[randomNumber]
        print(f"You picked {userChoice}.")
        print(f"Computer picked {computerPick}.") 
        if userChoice == computerPick:
            print("It's a draw!")
        elif (userChoice == 'rock' and computerPick == 'scissors') or \
             (userChoice == 'paper' and computerPick == 'rock') or \
             (userChoice == 'scissors' and computerPick == 'paper'):
            print("You won!")
            userWins += 1
        else:
            print("You lost!")
            computerWins += 1
