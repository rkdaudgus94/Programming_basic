# 사용자로부터 세 자리 정수를 입력 받으시오. 

x = int(input('세 자리 정수를 입력하시오 :'))
hun = x // 100
ten = x % 100 // 10
one = x % 10

print(int((one*100)+(ten*10)+hun))
