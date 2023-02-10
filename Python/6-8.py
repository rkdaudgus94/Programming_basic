# 6-8 직선 거리 
import math

def distance(x1,y1,x2,y2) :
    r = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)

    return r

print(distance(4,2,2,1))