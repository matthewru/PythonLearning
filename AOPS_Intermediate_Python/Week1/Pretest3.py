def Fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        return 1
    elif n > 1:
        for count in range(2, n+1):
            c = a+b
            a=b
            b=c
        return b

print(Fibonacci(9))