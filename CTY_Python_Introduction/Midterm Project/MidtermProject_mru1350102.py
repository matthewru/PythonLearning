#This program encrypts and decrypts messages using the 3-letter-shift used by Julius Caesar.
import string

#This is a list of the alphabet so that we can use their position in the list as a numeric value of the letter.
alphabetic_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#This function finds the character's position according to the specified list above.
def order(char):
    return alphabetic_list.index(char)

#This function finds the character based on it's position in the list above.
def char(position):
    return alphabetic_list[position]

#This function shifts the character's position by a specified amount of positions.
def shiftText(text, shiftSpace):
    encrypted = ""
    for c in text:
        if c in string.punctuation:
            encrypted += c
        elif c == " ":
            encrypted += c
        else:
            pos = order(c.lower()) + shiftSpace
            if pos >= len(alphabetic_list):
                pos = pos - len(alphabetic_list)
            elif pos < 0:
                pos = pos + len(alphabetic_list)
            encodeChar = char(pos)
            if c.isupper():
                encodeChar = encodeChar.upper()
            encrypted += encodeChar
            
    return encrypted

#This function shifts the letters to the left 3 positions
def cipherText(plainText):
    return shiftText(plainText, -3)

#This function shifts the letters to the right 3 positions
def plainText(encodedText):
    return shiftText(encodedText, 3)

#These lines prompt the user to either encrypt or decrypt and also ask for a message to encrypt or decrypt.
action = input("Would you like to encrypt or decrypt? ")

if action == "encrypt":
    plainText = input("What message would you like to encrypt? ")
    print("This is your encrypted text:\n%s" % cipherText(plainText))
elif action == "decrypt":
    encodedText = input("What message would you like to decode? ")
    print("This is your decrypted text:\n%s" % plainText(encodedText))
else:
    print("Please type a valid response")
