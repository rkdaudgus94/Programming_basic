# 5-9  최댓값 최솟값

z = []
count = 0
while True :
    n = int(input("정수를 입력하시오 :"))
    if n < 0 :
        break
    z.append(n)
    count = count +1

max = z[0]
min = z[0]

for i in range(count) :
    if max <= z[i] :
        max = z[i]
    if min >= z[i] :
        min = z[i]

print("{}개의 유효한 정수중 가장 큰 정수는 {} 이고, 가장 작은 정수는 {} 입니다.".format(count,max,min))
