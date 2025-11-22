#number guessing game
import random
print('Welcome to higher or lower')
print("The rules of the game are simple")
print('you have the guess the number and i will tell you if you are higher or lower')
print("you have 20 attempts to guess")
query1 = input('Would you like to begin, yes or no?: ')
if query1.lower() == "yes":
    count = 0
    query2 = int(input('What do you want the highest number to be?: '))
    query3 = int(input('What do you want to lowest number to be?: '))
    number = random.randint(query3,query2)
    print("Let the game begin!!!!!")
    while count <= 20:
        guess = int(input("what is your guess?: "))
        if guess > number:
            print("too high!!!")
            count += 1
            print("you have", 20-count, "guesses remaining")
            print("")
        elif guess < number:
            print("too low!!!!")
            count += 1
            print("you have", 20-count, "guesses remaining")
            print("")
        elif guess == number:
            print("Congratulations!!!!!!!!!")
            print('You did it in', count+1, "attempts")
            break
        else:
            break
if query1.lower() == "no":
    print("Thank you, have a nice day")
        

for 