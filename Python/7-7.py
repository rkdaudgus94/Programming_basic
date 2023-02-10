# 7-7 동일한 문자열 삭제
l = []
fluit_list = ['banana','orange','kiwi','apple','melon']
for i in range(5) :
    l.append(len(fluit_list[i]))
max = max(l)
s = []
for j in range(5) :
    if len(fluit_list[j]) != int(max) :
        s.append(fluit_list[j])
    
print(s)





