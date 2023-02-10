# 5-6 연료 탱크 프로그램
tank0 = 500
tank = 500
while tank > tank0 / 10 :
    n = int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: "))
    tank = tank + n
    print("현재 탱크양은","{}입니다.".format(tank))
print("경고 : 연료가 10% 미만이니 충전하세요!")
