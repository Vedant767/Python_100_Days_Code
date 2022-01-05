alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

def caesar(plain_text, shift_amount, follow_direction):
    output_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if follow_direction == "encode":
            new_position = position + shift_amount
        elif follow_direction == "decode":
            new_position = position - shift_amount
            print(new_position)
        output_text += alphabet[new_position]
    print(f"The {follow_direction} text is {output_text}")

caesar(text, shift, direction)