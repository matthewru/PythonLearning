ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar_shift(text, space):

    shifted = ""
    for c in text:
        if c in ALPHABET:
            pos = ALPHABET.index(c)
            newpos = pos + space
            if newpos % 25 > 0:
                newpos = newpos % 26
            char = ALPHABET[newpos]
        shifted += char

    return shifted

print(caesar_shift("example", 1))
print(caesar_shift("example", -1))
print(caesar_shift("python", 2))
print(caesar_shift("pecan", 4))