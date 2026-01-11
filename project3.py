import random
Rock = 1
Paper = 2
Scissors = 3
def singleplayer():
    PlayerCount = 0
    CompCount = 0
    while PlayerCount < 2 and CompCount < 2:
        print("Rock, Paper, Scissors?")
        ComputerMove = random.randint(1,3)
        PlayerMove = input("")
        if PlayerMove.lower() == "rock" and ComputerMove == Rock:
            print("you both picked Rock, tie")
        elif PlayerMove.lower() == "paper" and ComputerMove == Paper:
            print("you both picked Paper, tie")
        elif PlayerMove.lower() == "scissors" and ComputerMove == Scissors:
            print("you both picked scissors, tie")
        elif PlayerMove.lower() == "rock" and ComputerMove == Paper:
            print("you picked Rock and the computer picked Paper")
            CompCount +=1
        elif PlayerMove.lower() == "rock" and ComputerMove == Scissors:
            print("you picked Rock and the computer picked scissors")
            PlayerCount += 1 
        elif PlayerMove.lower() == "paper" and ComputerMove == Rock:
            print("you picked paper and the computer picked rock")
            PlayerCount +=1
        elif PlayerMove.lower() == "paper" and ComputerMove == Scissors:
            print("you picked paper and the computer picked sciccors")
            CompCount +=1 
        elif PlayerMove.lower() == "scissors" and ComputerMove == Rock:
            print("you picked scissors and the computer picked rock")
            CompCount +=1
        elif PlayerMove.lower() == "scissors" and ComputerMove == Paper:
            print("you picked Scissors and the computer picked paper")
            PlayerCount += 1
        else:
            print("Invalid choice")
    if PlayerCount == 2:
        print("Congratulations you won!!! ")
        print("The scores were you:",PlayerCount,":",CompCount,"Computer")
    elif CompCount == 2:
        print("Unfortunate you lost :( ")
        print("The scores were you:",PlayerCount,":",CompCount,"Computer")
    ask= input("Would you like to play again?: ")
    if ask.lower() == "yes":
        singleplayer()
    elif ask.lower() == "yes":
        print("Thank you for playing")
def Multiplayer():
    Player1Count = 0
    Player2Count = 0
    while Player1Count < 2 or Player2Count < 2:
        print("Rock, Paper, Scissors?")
        Player1Move = input("Player 1:")
        Player2Move = input("Player 2:")
        if Player1Move.lower() == Player2Move.lower():
            print("You both picked the same thing, twins!")
        elif Player1Move.lower() == "rock" and Player2Move.lower() == "paper":
            print("player1 picked Rock and player 2 picked Paper")
            Player2Count +=1
        elif Player1Move.lower() == "rock" and Player2Move.lower() == "scissors":
            print("player1 picked Rock and player2 picked scissors")
            Player1Count += 1 
        elif Player1Move.lower() == "paper" and Player2Move.lower() == "rock":
            print("Player 1 picked paper and Player 2 picked rock")
            Player1Count +=1
        elif Player1Move.lower() == "paper" and Player2Move.lower() == "scissors":
            print("Player 1 picked paper and Player 2 picked sciccors")
            Player2Count +=1 
        elif Player1Move.lower() == "scissors" and Player2Move.lower() == "rock":
            print("you picked scissors and the computer picked rock")
            Player2Count +=1
        if Player1Move.lower() == "scissors" and Player2Move.lower() == "paper":
            print("Player 1 picked Scissors and Player 2 picked paper")
            Player1Count += 1
    if Player1Count == 2:
        print("Congratulations Player 1 won!!! ")
        print("The scores were you:",Player1Count,":",Player2Count,"Computer")
    elif Player2Count == 2:
        print("Congratulations player 2 won!!!")
        print("The scores were you:",Player1Count,":",Player2Count,"Computer")
    ask= input("Would you like to play again?: ")
    if ask.lower() == "yes":
        Multiplayer()
print("Welcome to rock, paper, scissors")
while True:
    query1 = input("Would you like singleplayer or multiplayer?: ")
    if query1.lower() == "singleplayer" or "single":
        singleplayer()
        print("Thank you for playing :) ")
    elif query1.lower() == "mulpiplayer" or "multi":
        Multiplayer()
        print("Thank you for playing :) ")
    else:
        print("Not an option")
        False

for i in range(96):
    random_number = random.randint(1,5)
    print(random_number)
    
print("Tenski save me")
