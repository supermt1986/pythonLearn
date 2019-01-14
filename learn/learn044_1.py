import time
class NewTimer():
    def __init__(self):
        self.startTime = 0
        self.endTime = 0
        self.title = "未开始计时"
        # self.timer = []
        # self.unit = ['年','月','日','时','分','秒']
        self.methodName = 'process_time'
        self.timer =0
    def start(self):
        print('计时开始...')
        self.startTime = time.getattr(time, self.methodName)
        self.title = '请先运行stop()'

    def stop(self):
        if not self.startTime:
            print('请先调用start()方法开始计时！')
        else:
            self.endTime = time.getattr(time,self.methodName)
            print('计时结束')
            self._calc()

    def _calc(self):
        # self.timer = []
        # print('startTime = ' + str(self.startTime))
        # print("endTime = " + str(self.endTime))
        print('time type ' + str(type(self.startTime)))
        self.timer = self.endTime - self.startTime
        self.title = '总共运行了%d'% self.timer
        # for i in range(6):
        #     self.timer.append(self.endTime[i] - self.startTime[i])
        #
        #     if self.timer[i] < 0:
        #         print('i = ' + str(self.timer[i]))
        #         self.timer[i-1] = self.timer[i-1]-1
        #         if i ==2:
        #             self.timer[i] = 12 + self.timer[i]
        #         if i ==3:
        #             self.timer[i] = 31 + self.timer[i]
        #         if i ==4:
        #             self.timer[i] = 24 + self.timer[i]
        #         if i ==5 or i == 6:
        #             self.timer[i] = 60 + self.timer[i]
        # for i in range(6):
        #     if self.timer[i]:
        #         self.title += str(self.timer[i]) + self.unit[i]
        self.startTime = 0
        self.endTime = 0
        # print('calc的结果是 ' + self.title)


    def __str__(self):
        return self.title

    def __add__(self, other):
        title = '总共运行了%d'%self.timer + other.timer
        # result =[]
        # for i in range(6):
        #     result.append(self.timer[i] + other.timer[i])
        #     if result[i]:
        #         title += str(result[i]) + self.unit[i]
        # return title



