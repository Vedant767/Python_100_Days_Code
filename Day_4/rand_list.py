import random
#random,choice() function is used to choose random elements from list.
list_names = input("Enter everybody's name, separated by comma.").split(",")
print(list_names)
print(f"{random.choice(list_names)} is going to pay the bill today.")