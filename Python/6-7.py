# 6-7 factorial 

def factorial(n) :
    fn = 1 
    for i in range (1,n+1) :
        fn = fn * i
    return fn

print(factorial(5))
print(factorial(7))
print(factorial(10))