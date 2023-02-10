import random
import math
s1 = random.randint(1, 100)
s2 = random.randint(1, 100)
ans = s1 + s2
s1_char = str(s1)
s2_char = str(s2)

print(s1,'+',s2,'=', end = '')
sum = int(input())
sum = int(sum)
if ans == sum :
    print('잘했어요!!')
else :
    print('정답은',ans,'입니다.')
