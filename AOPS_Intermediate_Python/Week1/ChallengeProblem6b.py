greatestWordValue = 0
greatestWords = []
values = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,
          'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,
          'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}

def wordValue(word):
    value = 0
    for letter in word:
        value += values[letter]
    return value

file = open("wordlist.txt", "r")

for line in file:
    word = line.strip().upper()
    if len(word) == 7 and 'Z' not in word:
        val = wordValue(word)
        if val > greatestWordValue:
            greatestWordValue = val
file.close()

file = open("wordlist.txt", "r")
for line in file:
    word = line.strip().upper()
    if len(word) == 7 and 'Z' not in word:
        val = wordValue(word)
        if val == greatestWordValue:
            print(word)
            greatestWords.append(word)

file.close()
print(greatestWords)
print(greatestWordValue)