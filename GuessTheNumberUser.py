import random

def guess(x):
    computer_guess = random.randint(1,x)
    print(f"I'm guessing {computer_guess}")
    turn = input("Is my number correct? Enter Yes or Too High or Too Low: ")
    if turn == "Too Low":
        guess
    elif turn == "Too High":
        guess
    else : turn == "Yes"
    print(f"Congratulations you guessed correctly {computer_guess}is the number!")

guess(5)
