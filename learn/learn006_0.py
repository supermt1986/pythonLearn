# import random as r
#
# count = 100
# i = 1
# while count:
#     if i % 2 != 0:
#         print(i)
#     count = count - 1
#     i = i +1

# num = 999999999
# count = 100
# while count:
#     num *= num
#     count -= 1
#
# print('the num is ' + str(num))

count = 1
while True:
    if count %2 ==1 and count %3 ==2 and count % 5 == 4 and count %6 ==5 and count %7 ==0:
        print('the number is ' + str(count))
        break
    count += 1

print(5** -2)

x = 7
i = 1
flag = 0

while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
        flag = 1
    else:
        x = 7 * (i+1) # 根据题意，x一定是7的整数倍，所以每次乘以7
    i += 1

if flag == 1:
    print('阶梯数是：', x)
else:
    print('在程序限定的范围内找不到答案！')
