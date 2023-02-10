# 8-1 철수네 과일가게

apple, pear, watermelon, tangerine, grape = input("과일 가격을 차례로 입력하세요. ").split()

fruits_dic = {'사과':apple, '배':pear, '수박':watermelon, '귤':tangerine, '포도':grape}

print('---------- 오늘 과일의 가격 ----------')
print('사과        :',fruits_dic['사과'])
print('배          :',fruits_dic['배'])
print('수박        :',fruits_dic['수박'])
print('귤          :',fruits_dic['귤'])
print('포도        :',fruits_dic['포도'])