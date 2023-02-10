# 7-9 overlap

a = input("문자열 A를 입력하시오: ")#apple
b = input("문자열 B를 입력하시오: ")#plee     c = appplee
a=list(a)
b=list(b)
a_len = len(a) # 6 justtt  
b_len = len(b) # 5 twice     b count  11
x_len = a_len - b_len
b_index = 0
count = 0
a1 = []
if x_len < 0 :
    x_len = 0

for i in range(x_len,a_len) :
    if a[i] != b[b_index] :
        if a[i] == b[b_index-1] : # a = 3 (t) b = 0 (t)
            b_index = b_index
            count = count
        else :
            b_index = 0
            count = 0
    else :
        b_index += 1
        count += 1
if count >= 1 :
    for j in range(a_len-count) :
        a1.append(a[j]) 

c = a1 + b
c_len = len(c)
for k in range(len(c)) :
    print(c[k], end='')

        
