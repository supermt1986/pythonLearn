temp = input('请输入我心中所想数字： ')
print(temp.isdigit())
while (not temp.isdigit()):
    print("输入不合法", end='')
    temp = input('请输入我心中所想数字')
