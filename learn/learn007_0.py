# gread = input('请输入成绩')
# greadNum = 0
# while True:
#     if not gread.isdigit():
#         print('输入成绩无效')
#         gread = input('请输入成绩')
#     elif int(gread) <0 or int(gread) >100:
#         print('输入成绩无效')
#         gread = input('请输入成绩')
#     else:
#         greadNum = int(gread)
#         break
# if greadNum >= 90:
#     print('A')
# elif greadNum >= 80:
#     print('B')
# elif greadNum >= 60:
#     print('C')
# else:
#     print('D')


x, y, z = 6, 5, 4
if x < y:
    small = x
    if z < small:
        small = z
elif y < z:
    small = y
else:
    small = z

print('source small = ' + str(small))

x, y, z = 6, 5, 4
small = (z if z <x else x ) if x<y else (y if y<z else  z)
print('sink small = ' + str(small))

x =1;y=2;z=3

x,y,z = y,z,x

print(x,y,z)

i = range(100)
print(i)