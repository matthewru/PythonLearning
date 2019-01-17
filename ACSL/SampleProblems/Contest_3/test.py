from clsPalindrome import Palindrome

#testing Palindrome.reverseNum(self, num)
def testreverseNum():
    num = 87
    palindrome = Palindrome(num)
    print("%d reversed is %d" % (num, palindrome.reverseNum()))

#testing Palindrome.isPalindrome(self, num)
def testisPalindrome():
    num = 87
    palindrome = Palindrome(num)
    print("%d palindrome %s" % (num, palindrome.isPalindrome()))
    num = 88
    palindrome = Palindrome(num)
    print("%d palindrome %s" % (num, palindrome.isPalindrome()))

#testing Palindrome.makePalindrome(self, num)
def testmakePalindrome():
    num = 87
    palindrome = Palindrome(num)
    print("%d turns into number %d palindrome %s" % (
    palindrome.num, palindrome.makePalindrome(), palindrome.isPalindrome()))
    num = 196
    palindrome = Palindrome(num)
    print("%d turns into number %d palindrome %s" % (
    palindrome.num, palindrome.makePalindrome(), palindrome.isPalindrome()))

testreverseNum()
testisPalindrome()
testmakePalindrome()
