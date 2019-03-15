# Python Class 1889
# Lesson 1 Problem 7
# Author: madmathninja (272729)
import math
import string

def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    rails = []
    for n in range(0, numRails):  #loop from 0 - number of rails incrementing by 1
        rail = ""
        for i in range(n, len(plaintext), numRails):  #picking character in text at position n, n+numRails...
            rail += plaintext[i]  #concatenate the characters into a text
        rails.append(rail)  #add text to a list
    rails.reverse()  #reverse list
    return ''.join(rails)

def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    railLength = math.ceil(len(ciphertext)/numRails)  #number of chars in each rail
    rails = []
    for n in range(len(ciphertext)-1, -1, -railLength):  #loop through length of text going backwards by railLength
        if n > railLength:
            rail = ciphertext[n-railLength+1:n+1]  #get each rail string
        else:
            rail = ciphertext[0:n+1]  #get each rail string
        rails.append(rail)  #store in a list

    text = ""
    for i in range(0, railLength):
        for rail in rails:
            if (i<len(rail)):
                text += rail[i]
    return text



def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    file = open(wordfilename, "r")

    wordList = []
    for line in file:
        wordList.append(line.strip())
    file.close()

    decodedText = ""
    decodedWords = 0

    for count in range(2, 11):  #for loop to loop through the number of rails, 2 - 10
        decipheredText = decipher_fence(ciphertext, count)  #call decipher_fence to get deciphered text
        decipheredText.translate(string.punctuation)  #strip out punctuation
        knownWords = 0
        textList = decipheredText.split(" ")  #split the text by empty space to get a list of words
        for text in textList:
            if text in wordList:  #check each word if it exists in the wordlist.txt
                knownWords += 1  #if so, increment knownWords

        if knownWords > decodedWords:
            decodedWords = knownWords
            decodedText = decipheredText

    return decodedText

# test cases
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!
