# #while '0' :
# #    print('this is loop')
#
# print(bool('C'))
#
# i = 10
# while i:
#     print('chensong shuai' + str(i))
#     # i = i-1
import random as r

# num = int(input('请输入一个整数'))
# i = 1
# while num > 0:
#     print(i)
#     num = num-1
#     i=i+1
#

num = int(input('请输入一个整数'))
str =''
while num:
    i = num
    while i:
        str = str + " "
        i = i-1
    i = num
    while i:
        str = str + "*"
        i = i-1
    print(str)
    num = num -1
    str = ''
