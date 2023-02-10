# 7-8 리스트 슬라이싱

n = input("n를 입력하시오.")
s =[]
n = int(n)
for i in range(1,(n**2+1)) :
    s.append(i)

for j in range(1,n+1) :
    if j % 2 == 0 :
        a = (s[ (j*n)-1 : ((j-1)*n)-1 : -1 ])
        a1 = [str(c) for c in a]
        a2 = ','.join(a1)
        print('{0:2s}'.format(a2))
        #print(','.join('{0:2d}').format(a1))
    else :
        b = (s[ (j-1)*n : j*n ])
        b1 = [str(d) for d in b]
        b2 = ','.join(b1)
        print('{0:2s}'.format(b2))
        # print(','.join('{0:2d}').format(b1)) # 0~n-1 n~2n-1 
