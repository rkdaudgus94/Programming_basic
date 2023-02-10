# 9-7 카이사르의 암호 문장

s = input("문자를 입력하시오 : ")
n = int(input("이동시킬 칸 수를 입력하시오 : "))

s1 = list(s)
s_len = len(s1)

for i in range(s_len) :
    if s1[i].isalnum() == True :
        s = ord(s1[i])
        print(chr(s + n), end = '')
    else :
        print(s1[i], end = '')