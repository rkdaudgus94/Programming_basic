# 6-6 소수 찾기


n = int(input())
def is_prime(n) :
    for i in range (2,n) :
        if n % i != 0 :
            value = True
        else :
            value = False
            break
    return value

print("소수인가요?", is_prime(n))
        

