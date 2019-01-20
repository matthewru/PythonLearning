from clsPalindrome import Palindrome

for count in range(0, 5):
    num = int(input("Number: "))
    palindrome = Palindrome(num)
    hasPalindrome = palindrome.isPalindrome(palindrome.makePalindrome(num))
    if hasPalindrome:
        message = ""
    else: message = "NONE, "
    print("%s%d" % (message, palindrome.makePalindrome(num)))
