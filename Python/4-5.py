# 4-5

import random
count = 0
n = []
for i in range(0,3) :
    n.append(random.randint(0,9))
print(n)0 
x, y, z = map(int, input('당첨번호 세 개를 입력하시오.').split())


for i in range(3) :
    if n[i] == x :
        count += 1
    if n[i] == y :
        count += 1
    if n[i] == z :
        count += 1

if count == 3 :
    print("상금 1억원")
elif count == 2 :
    print("상금 10억원")
elif count == 1 :
    print("상금 100억원")
else :
    print("상금 1조")