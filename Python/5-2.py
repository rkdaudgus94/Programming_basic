# 5-2

# 1번 문제
from re import S


sum = 0
for i in range(1,101,2) :
    sum = sum + i

print("1에서 100까지의 수 중에서 홀수의 합 :", sum)

# 2번 문제
sum1 = 0
for i in range(2,101,2) :
    sum1 = sum1 + i

print("1에서 100까지의 수 중에서 짝수의 합 :", sum1)

# 3번 문제
z0 = int(input("시작 정수를 입력하세요 : "))
z  = int(input("끝 정수를 입력하세요 : "))
m  = z-z0 
for i in range(z0+1,z+1):
    z0 = z0 + i

print(z0,"에서",z,"까지 정수의 합 :", z0)