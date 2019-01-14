# x = range(10,20,2)
#
# for xx in x:
#     print(xx)

# password = input('请输入密码')
# inputCount = 3
#
# while True:
#
#     if password.find('*') >= 0:
#         print('密码中不能含有“*”！您还有%d次机会！'%inputCount,end='')
#         password = input('请输入密码')
#         continue
#     elif password == "supersong":
#         print('密码正确，进入程序')
#         break
#     else:
#         inputCount -= 1
#         if inputCount == 0:
#             print('输入错误超过3次，请明天再试')
#             break
#         print('密码输入错误！您还有%d次机会！'%inputCount, end='')
#         password = input('请输入密码')

# for i in range(100,999):
#     strNum = str(i)
#     sum = 0
#     for k in list(strNum):
#         sum += int(k) *int(k)  * int(k)
#     if i == sum:
#         print(i)
import random
basket = ['red', 'red', 'red', 'yelow', 'yelow','yelow','green','green','green','green','green','green']
basketleng = 11
redcount = 0
yellowcount = 0
greencount = 0
for i in range(8):
    color = basket.pop(random.randint(0, basketleng - i))

    if color == "red":
        redcount += 1
    elif color == "yelow":
        yellowcount += 1
    else:
        greencount += 1
print('篮子里头剩余的球是' + str(basket))
print('取出的红球数是 ' + str(redcount))
print('取出的黄球数是 ' + str(yellowcount))
print('取出的绿球数是 ' + str(greencount))


print('red\tyellow\tgreen')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                # 注意，下边不是字符串拼接，因此不用“+”哦~
                print(red, '\t', yellow, '\t', green)

