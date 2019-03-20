# Python Class 1889
# Lesson 2 Problem 4 Part (a)
# Author: madmathninja (272729)

def permute(inputList):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''
    if len(inputList) == 0:
        return []
    if len(inputList) == 1:
        return[inputList]

    perms = []

    for i in range(len(inputList)):
        ele = inputList[i]

        remPerms = inputList[:i] + inputList[i+1:]

        for p in permute(remPerms):
            perms.append([ele] + p)
    return perms

# test cases
print(permute([1,2]))
# should print [[1,2], [2,1]] in some order
print(permute([1,2,3]))
# should print [[1,2,3], [1,3,2], [2,1,3], [3,1,2], [2,3,1], [3,2,1]] in some order