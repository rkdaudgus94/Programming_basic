# 5-5 달팽이 문제
m = 7
day = 1
while m <= 30 :
    print("day :","{0:2d}".format(day),"달팽이의 위치 :","{0:2}".format(m),'미터')
    m = m + 2
    day = day + 1

print("축하합니다. 우물을 탈출하였습니다.")
print("우물을 탈출하는 데 걸린 날은","{}일 입니다".format(day))