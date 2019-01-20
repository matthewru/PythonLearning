class Palindrome:

    def __init__(self, num):
        self.num = num

    def reverseNum(self, num):
        return int(str(num)[::-1])

    def isPalindrome(self, num):
        if self.reverseNum(num) == num:
            return True
        else: return False

    def makePalindrome(self, num):
        if not self.isPalindrome(num):
            for count in range(0, 10):
                num = self.reverseNum(num) + num
                if self.isPalindrome(num):
                    break
            return num
        else:
            return num




