# 5-8 거꾸로 정수

z = 0
while z >= 0 :
    z = int(input("정수를 입력하시오 : "))
    if ( z < 0) :
        print("프로그램을 종료합니다.")
        break
    z = str(z)
    reverse_z = ''

    for c in z :
        reverse_z = c + reverse_z

    reverse_z = int(reverse_z)
    z = int(z)
    if z == reverse_z :
        print("{}은(는) 거꾸로 정수입니다. ".format(z))
    else              :
        print("{}은(는) 거꾸로 정수가 아닙니다.".format(z))




# # 리스트의 reverse를 이용해서 문자열 뒤집기
# name1 = "ab BlockDMask cd"
# print(f'name1     : {name1}')

# # 문자열을 리스트로
# name_list = list(name1)  
# print(f'name_list : {name_list}')

# # 리스트 역순으로
# name_list.reverse() 
# print(f'name_list : {name_list}')

# # 리스트를 문자열로
# name2 = ''.join(name_list)
# print(f'name2     : {name2}')
