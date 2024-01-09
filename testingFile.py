# this file is used for testing git function purpose

def fib(n):
    if n <= 2: 
        return 1 
    else: 
        a = 1
        b = 1 
        for i in range(2, n+1):
            c = a+b
            a = b 
            b = c 
        return c
    
print(fib(100))





