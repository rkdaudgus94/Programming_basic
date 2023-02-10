# 7-4 튜플 이해하기
z = []
e = ('A','B','C')
n = ('1','2')

for i in range(3) :
    for j in range(2) :
        z.append(e[i]+(n[j]))

print(z)