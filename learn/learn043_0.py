class C():
    def __init__(self,*args):
        if len(args) == 0:
            print('并没有传入参数')
        else:
            print('传入了%d个参数' % len(args) + ',分别是', end='')
            for i in args:
                print(i, end='')
        print()
c = C()

c = C(1,2,3)

class Nstr(str):
    def __new__(cls, string):
        return str.__new__(cls,str(string).split(' ')[0])
    def __lt__(self, other):
        return int.__lt__(len(self),len(other))
    def __le__(self, other):
        return int.__le__(len(self),len(other))
    def __eq__(self, other):
        return int.__eq__(len(self),len(other))
    def __ne__(self, other):
        return int.__ne__(len(self),len(other))
    def __gt__(self, other):
        return int.__gt__(len(self),len(other))
    def __ge__(self, other):
        return int.__ge__(len(self),len(other))

ns = Nstr('123456789 2547')
print(ns)

ns2 = Nstr('sdfsdfsd')
print(ns2)

ns3 = Nstr('12312312')

print (ns2 >ns)
print (ns2 < ns)
print (ns2 == ns3)
print (ns2 >= ns3)


class Word(str):
#'''存储单词的类，定义比较单词的几种方法'''

    def __new__(cls, word):
        # 注意我们必须要用到 __new__ 方法，因为 str 是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print ("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

word = Word('sdfsdfsdf sdfawdsfas')
print('word is ' + word)