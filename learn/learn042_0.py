class Nstr(str):
    def __sub__(self, other):
        return self.replace(other,'')

    def __rshift__(self, other):
        return self[int(len(self)) - int(other):] + self[: int(len(self)) - int(other)]
    def __lshift__(self, other):

        return self[int(other):] + self[0:int(other)]

a = Nstr('I dislike FishC!iiiiiiii')
b = Nstr('i')

print(a - b)


a = Nstr('I dislike FishC!')
print(a << 3)
print(a >> 3)


class Nstr2(str):
    def __add__(self, other):
        return self.getAscii(self) + self.getAscii(other)

    def __sub__(self, other):
        return self.getAscii(self) - self.getAscii(other)
    def __mul__(self, other):
        return self.getAscii(self) * self.getAscii(other)
    def __truediv__(self, other):
        return self.getAscii(self) / self.getAscii(other)
    def getAscii(self, s):
        asciiC = 0
        for i in s:
            asciiC += int(ord(i))
        return asciiC

a = Nstr2('FishC')
b = Nstr2('love')

print(a + b)
print(a - b)
print(a * b)
print(a / b)
