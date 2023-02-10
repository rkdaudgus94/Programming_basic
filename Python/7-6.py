# 7-5 remove 랑 list 사용법
s = ''
s1 = ''
c = input("문자열을 입력하세요. ")
c = list(c)
for i in range(len(c)) :
    s = s + c[i] 
    print(s)
    if i == len(c) - 1 :
        for j in range(len(c)-1,0,-1) :
            c.remove(c[j])
            
            print(''.join(c))


