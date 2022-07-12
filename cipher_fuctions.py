alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



# This method generates a Vigenère square that will be used by the ciphering and deciphering methods
def generate_vigenere_square():        
    vigenere_square = []
    for letter in alphabet:
        start_index = alphabet.index(letter)
        row_list = []
        for x in alphabet[start_index:]:
            row_list.append(x)

        if len(row_list) < 26:
            for y in alphabet:
                if len(row_list) < 26:
                    row_list.append(y)
                else:
                    break
        vigenere_square.append(row_list)
    return vigenere_square

vigenere_square = generate_vigenere_square()


# This methods ciphers a string using a secret key and a Vigenère square
def cipher(message, key, square):
    cipher = ""
    current_key_index = 0
    joined_message = message.replace(' ', '')

    for letter in joined_message:
        if current_key_index == 0:
            pass
        elif current_key_index >= len(key):
            current_key_index = 0

        cipher += square[alphabet.index(key[current_key_index])][alphabet.index(str.lower(letter))]

        current_key_index += 1

    return cipher


# This methods deciphers a ciphered string using its secret key and a Vigenère square
def decipher(message, key, square):
    cipher = ""
    current_key_index = 0
    joined_message = message.replace(' ', '')

    for letter in joined_message:
        if current_key_index == 0:
            pass
        elif current_key_index >= len(key):
            current_key_index = 0

        row = square[alphabet.index(key[current_key_index])]
        cipher_letter_index = row.index(letter)

        cipher += alphabet[cipher_letter_index]

        current_key_index += 1

    return cipher
