# 9-3 대문자 소문자 특수기호 구별

n = input("문자열을 입력하시오. : ")
n1 = list(n)
n_len = len(n1)
print(n1)
num_count = 0
alp_count = 0
sig_count = 0

for i in range (n_len) :
    if n1[i].isdecimal() == True :
        num_count += 1
    elif n1[i].isalpha() == True :
        alp_count += 1
    else :
        sig_count += 1

print("문자 갯수 : ",alp_count)
print("숫자 갯수 : ",num_count)
print("기호 갯수 : ",sig_count)
