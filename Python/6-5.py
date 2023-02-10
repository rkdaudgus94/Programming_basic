# 6-5 섭씨 화씨 반환 함수

def cel2fah(celsius) :
    fahrenheit = (9//5) * celsius + 32
    return fahrenheit


for i in range (0,60,10) :
    print(cel2fah(i))