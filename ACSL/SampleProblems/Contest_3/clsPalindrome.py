class Palindrome:

    def __init__(self, num):
        self.num = num

    def reverseNum(self):
        return int(str(self.num)[::-1])

    def isPalindrome(self):
        if self.reverseNum() == self.num:
            return True
        else: return False

    def makePalindrome(self):
        if not self.isPalindrome():
            for count in range(0, 10):
                self.num = self.reverseNum() + self.num
                if self.isPalindrome():
                    break
            return self.num
        else:
            return self.num

