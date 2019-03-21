# Python Class 1889
# Lesson 2 Problem 4 Part (a)
# Author: madmathninja (272729)

def listtoString(list):
    space = ''
    return space.join(list)


def anagrams(inputString):
    '''permute(charList) -> list
    returns list of all permutations of charList'''
    charList = list(inputString)

    if len(charList) == 0:
        return []
    if len(charList) == 1:
        return listtoString(charList)

    perms = []
    for i in range(len(charList)):
        ele = charList[i]
        remPerms = charList[:i] + charList[i+1:]
        for p in anagrams(remPerms):
            perms.append(ele + p)

    anagramsList = []
    for term in perms:
        word = listtoString(term)
        if word not in anagramsList:
            anagramsList.append(word)

    return anagramsList

def jumble_solve(inputString):
    file = open("wordlist.txt", "r")

    wordList = []
    for line in file:
        wordList.append(line.strip())
    file.close()

    validWords = []

    possibleWords = anagrams(inputString.lower())
    for word in possibleWords:
        if word in wordList:
            validWords.append(word)
    return validWords

# anagrams test cases
print(anagrams('stop'))
print(anagrams('wisdom'))
print(anagrams('armor'))

#jumble_solve test cases
print(jumble_solve('CHWAT'))
print(jumble_solve('RAROM'))
print(jumble_solve('CEPLIN'))
print(jumble_solve('YAFLIM'))