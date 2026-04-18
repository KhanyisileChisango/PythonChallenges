import random

while True:
    choice=input("Would you like to roll the dice (y/n): ")
    if choice =="y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll = die1 + die2
        print(f"Congrats you rolled a {roll}")
    elif choice =="n": 
        print("Okay thanks, have a nice day.")
        break
    else:
        print("Error you can only input y for yes or n for no.")
            