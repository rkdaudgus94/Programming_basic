# 5-7 암스트롱 수
import numpy as np

Arm = []
count = 0
for i in range (1000) :
    x = i // 100
    y = i % 100 // 10
    z = i % 10
    g = x**3 + y**3 + z**3 

    if (i == g) & (i > 100) :
        Arm.append(i)
        count = count + 1
        

print("세 자리의 암스트롱 수 :", end = ' ')
for j in range (count) :
    print(Arm[j], end = ' ')