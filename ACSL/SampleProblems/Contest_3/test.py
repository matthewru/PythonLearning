from clsPalindrome import Palindrome

#testing Palindrome.reverseNum(self, num)
def testReverseNum():
    num = 87
    palindrome = Palindrome(num)
    print("%d reversed is %d" % (num, palindrome.reverseNum(num)))
    num = 70
    palindrome = Palindrome(num)
    print("%d reversed is %d" % (num, palindrome.reverseNum(num)))
    num = 701
    palindrome = Palindrome(num)
    print("%d reversed is %d" % (num, palindrome.reverseNum(num)))

#testing Palindrome.isPalindrome(self, num)
def testIsPalindrome():
    num = 87
    palindrome = Palindrome(num)
    print("%d palindrome %s" % (num, palindrome.isPalindrome(num)))
    num = 88
    palindrome = Palindrome(num)
    print("%d palindrome %s" % (num, palindrome.isPalindrome(num)))

#testing Palindrome.makePalindrome(self, num)
def testMakePalindrome():
    num = 87
    palindrome = Palindrome(num)
    print("%d turns into number %d palindrome %s" % (
    palindrome.num, palindrome.makePalindrome(num), palindrome.isPalindrome(num)))
    num = 196
    palindrome = Palindrome(num)
    print("%d turns into number %d palindrome %s" % (
    palindrome.num, palindrome.makePalindrome(num), palindrome.isPalindrome(num)))

testReverseNum()
testIsPalindrome()
testMakePalindrome()
