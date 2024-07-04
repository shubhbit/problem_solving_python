# <!-- Here's an example of a simple string encryption 
# function using a substitution cipher:

# Function: encryptString(text, key)

# Description: Encrypts a given string using a substitution 
# cipher with a provided key.

# Parameters:
# - text: The input string to encrypt.
# - key: An integer key for shifting characters. -->
# Here are some more example usage scenarios for the encryptString function:


def string_encryption(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            asc_code = ord(char)
            new_asc = asc_code + key
            new_char = chr(new_asc)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

# "Hello, World!", 3
# Outputs: "Khoor, Zruog!"

if __name__ == "__main__":
    print(string_encryption("Hello, World!", 3))
    print(string_encryption("abc.", 1))

