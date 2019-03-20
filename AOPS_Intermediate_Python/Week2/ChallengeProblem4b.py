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
        anagramsList.append(listtoString(term))

    return anagramsList

# test cases
print(anagrams('stop'))
print(anagrams('wisdom'))