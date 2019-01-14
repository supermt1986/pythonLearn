while True:
    year = input("请输入年份： ")
    yearNum = int(year)

    print(yearNum%400)
    print(yearNum%4)
    print(yearNum%100)
    if yearNum%400 ==0 or (yearNum%4==0 and yearNum%100 !=0):
        print("这是一个润年")
    else:
        print('这不是一个润年')
