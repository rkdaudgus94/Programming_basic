# 9-2 소문자 대문자 구별

a = []
b = []
a_count = 0
b_count = 0

n = input('문자열을 입력하시오. : ')
n_lower = n.lower()
print(n_lower)
#n_upper = n.upper()
n_len = len(n)
list(n_lower)
#list(n_upper)
list(n)
for i in range(n_len) :
    if n[i] == n_lower[i] : 
        a.append(n[i])
        a_count += 1
    else :
        b.append(n[i])
        b_count += 1

for i in range(a_count) :
    print(a[i], end = '')
for i in range(b_count) :
    print(b[i], end = '')
