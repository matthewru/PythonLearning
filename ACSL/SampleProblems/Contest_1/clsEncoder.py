class Encoder:

    ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self):
        pass

    def shiftLetter(self, pos):
        if pos > len(self.ALPHABET):
            return pos % len(self.ALPHABET)
        else:
            return pos

    def encodeAToE(self, char):
        charPos = self.ALPHABET.index(str.lower(char)) + 1
        newPos = charPos * 2
        newLetter = self.ALPHABET[self.shiftLetter(newPos) - 1]
        if newPos == 0:
            newLetter = "#"
        else:
            return newLetter.upper() if char.isupper() else newLetter.lower()

    def encodeFToJ(self, char):
        charPos = self.ALPHABET.index(str.lower(char)) + 1
        newPos = (charPos % 3) * 5
        newLetter = self.ALPHABET[self.shiftLetter(newPos) - 1]
        if newPos == 0:
            newLetter = "#"
        else:
            return newLetter.upper() if char.isupper() else newLetter.lower()

    def encodeKToO(self, char):
        charPos = self.ALPHABET.index(str.lower(char)) + 1
        newPos = int(charPos / 4) * 8
        newLetter = self.ALPHABET[self.shiftLetter(newPos) - 1]
        if newPos == 0:
            newLetter = "#"
        else:
            return newLetter.upper() if char.isupper() else newLetter.lower()

    def encodePToT(self, char):
        charPos = self.ALPHABET.index(str.lower(char)) + 1
        newPos = (sum(int(digit) for digit in str(charPos)) * 10)
        newPos = self.shiftLetter(newPos)
        newLetter = self.ALPHABET[self.shiftLetter(newPos) - 1]
        if newPos == 0:
            newLetter = "#"
        else:
            return newLetter.upper() if char.isupper() else newLetter.lower()

    def encodeUToZ(self, char):
        charPos = self.ALPHABET.index(str.lower(char)) + 1
        for num in range(charPos - 1, 0, -1):
            if charPos % num == 0:
                newPos = num * 12
                newLetter = self.ALPHABET[self.shiftLetter(newPos)- 1]
                if newPos == 0:
                    newLetter = "#"
                else:
                    return newLetter.upper() if char.isupper() else newLetter.lower()
        



