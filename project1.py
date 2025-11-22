#diceroller
import random
print("Welcome")
print("This is a dice roller")
count = 0
query1 = input("Would you like to roll dice, yes or no? ")
if query1.lower() =="yes":
    while True:
        query2 = int(input("How many dice would you like to roll? "))
        for num in range(query2):
            dice = random.randint(1,6) 
            print(dice)
            print("")
            count += 1
        query3 = input('would you like to roll again, yes or no? ')
        if query3.lower() == "no":
            print("you rolled the dice" , count , "times")
            print("Thank you for using my dice roller")
            break

else:
    print('Thanks you, Have a nice day')

