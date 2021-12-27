name1 = input("What is your name? \n").lower()
name2 = input("What is your name? \n").lower()

add_one = add_two = 0

combined_string = name1 + name2

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

add_one = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

add_two = l + o + v + e

print(add_one + add_two)