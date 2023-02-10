# 5-4 스스로 생각해봅시다!!

n = int(input("숫자를 입력하세요 :"))

for i in range(n,0,-1) :
    print(' '*(i-1),'*'*(n-i+1))
