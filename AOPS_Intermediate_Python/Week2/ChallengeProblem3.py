def factorial(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

def catalanNumber(n):
    return factorial(2 * n) / (factorial(n + 1) * factorial(n))


#test cases
print(catalanNumber(1))
print(catalanNumber(2))
print(catalanNumber(3))
print(catalanNumber(4))


print(catalanNumber(30))