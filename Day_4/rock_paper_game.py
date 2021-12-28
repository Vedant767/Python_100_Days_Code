# Rock wins against scissors
# Scissors win against paper
# Paper wins against rock

import random

def fetch_choice(n):
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    if n == 0:
        return rock
    elif n == 1:
        return paper
    else:
        return scissors

ur_chance = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(fetch_choice(ur_chance), "\n", ur_chance)
computer_choice = random.randint(0, 2)
print(fetch_choice(computer_choice), "\n", computer_choice)

if (ur_chance == 0 and computer_choice == 2) or (ur_chance == 2 and computer_choice == 1) or (ur_chance == 1 and computer_choice == 0):
    print("You win")
elif ur_chance == computer_choice:
    print("Draw! Play again")
else:
    print("Computer Wins")

