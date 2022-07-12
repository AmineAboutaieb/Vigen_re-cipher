# Importing the ciphering methods needed
from cipher_fuctions import *


# Message to cipher
message = "The river of sbou is passing and berries are growing on the floor"

# Key used to cipher
key = "whale"


# This loop prints the Vigenere square in the terminal
for x in vigenere_square:
    print(x)


# Ciphering the message
ciphered_message = cipher(message, key, vigenere_square)

print("Message => ", message)
print("Ciphered message => ", ciphered_message)

# Printing the ciphered message
deciphered = decipher(ciphered_message, key, vigenere_square)

print("Deciphered message => ",deciphered)
