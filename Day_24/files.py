# We use with because we don't need to call close function explicitly.

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
from statistics import mode


with open("my_file1.txt", mode='a') as file:
    contents = file.write("\nVedant1")