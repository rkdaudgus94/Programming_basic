# 6-3 최대 최소 값 반환

x,y,z = input("숫자 세 개를 입력하시오. ").split()
x,y,z = int(x),int(y),int(z)
d = [x,y,z]
def max(d) :
    d.sort()
    d.reverse()
    max = d[0]
    return max
def min(d) :
    d.sort()
    min = d[0]
    return min
 
print("최대값은", max(d))
print("최솟값은", min(d))