from re import S


v   = float(input('평균 시속(km/h)을 입력하세요 :'))
h   = float(input('평균 시간(h)를 입력하세요 :'))
h1  = ((h-int(h))*100)*60
m   = round(h1 // 100)
s   = round((h1 % 100) / 100 * 60)
print('평균 시속 :', v)
print('이동 시간 :', int(h),'시간', m,'분', s,'초')    #     (20 / 60) + (31 / 60 /60) = 0.342       =>        0.342 * 60 = (20 + 31/60) 
print('거리 :', v*h, 'km')
