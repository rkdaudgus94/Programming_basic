# 4-4

z = int(input('정수를 입력하시오 :'))
if z % 2 != 0 :
    print(z,"는 2로 나눠지지 않습니다.")
else :
    print(z,"는 2로 나눠집니다.")
if z % 3 == 0 :
    print(z,"는 3으로 나눠집니다.")
else :
    print(z,"는 3으로 나눠지지 않습니다.")

if (z % 2 != 0) & (z % 3 != 0) :
    print(z,"는 2와 3으로 나누어 지지 않습니다.")
elif (z % 2 == 0) & (z % 3 == 0) :
    print(z,"는 2와 3으로 나눠집니다.")