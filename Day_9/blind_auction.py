from art import logo
import os
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")
check_members_left = True
no_of_auctions = {}

while check_members_left:
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))

    no_of_auctions[name] = bid

    next_bidder = input("Are there any other bidders? Type 'yes' or 'no' " )

    if next_bidder == 'no':
        check_members_left = False
    else:
        os.system('cls')

print(max(zip(no_of_auctions.values(), no_of_auctions.keys()))[0])

