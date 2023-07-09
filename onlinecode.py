import random

def checking():
    score = 0
    comp = ["r", "p", "s"]
    random.shuffle(comp)
    rounds = int(input("How many rounds do you want to play? "))
    for _ in range(rounds):
        user_input = input("Type 'r' for rock, 'p' for paper, or 's' for scissors: ")
        if user_input == "r" or user_input == "p" or user_input == "s":
            comp_choice = random.choice(comp)
            print("Computer's choice:", comp_choice)
            if user_input == comp_choice:
                score += 1
        else:
            print("Invalid input. You have to enter 'r', 'p', or 's'.")
    return score

user_consent = input("Press 'y' to play or 'n' to not play: ")
if user_consent == "y":
    score = checking()
    print("Final score:", score)
else:
    print("Thank you. Have a nice day.")
