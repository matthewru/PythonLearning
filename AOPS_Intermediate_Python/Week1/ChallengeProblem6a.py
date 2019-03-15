tenletterwords = 0

file = open("wordlist.txt", "r")

for line in file:
    word = line.strip()
    if len(word) == 10:
        tenletterwords += 1
file.close()
print(tenletterwords)