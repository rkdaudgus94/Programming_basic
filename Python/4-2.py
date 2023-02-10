# d=[]
# x,y,z = input('세 정수를 입력하시오.').split()
# x,y,z = int(x),int(y),int(z)
# d.append(x)
# d.append(y)
# d.append(z)
# for i in range(0,3) :
#     for j in range(0,3) :
#         if d[j+1] <= d[j] :  # 8 3 4
#             sum = d[j]
#             d[j] = d[j+1]
#             d[j+1] = sum
                      

# for i in range(0,3) :
#     print(d[i], end= '')



d=[]
x,y,z = input('세 정수를 입력하시오.').split()
x,y,z = int(x),int(y),int(z)

d=[x,y,z]
d.sort()
d.reverse()
print(d)