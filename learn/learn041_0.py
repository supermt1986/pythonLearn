
class NewFile():
    def __new__(cls, fileName,mode):
        return open(fileName,mode)
    def __del__(self):
        self.close()


newFile = NewFile("learn041_0.txt","w")
newFile.write("12345678910")


class C2F():
    def __new__(cls, fot):
        return fot *1.8+32.0
print(C2F(32))

class Nint(int):
    def __new__(cls, value):
        if isinstance(value,str):
            temp = 0
            for i in value:
                temp += ord(i)
            return temp
        else:
            return int(value)
print(Nint(123))
print(Nint(1.5))
print(Nint('A'))
print(Nint('FishC'))