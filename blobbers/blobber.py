from faketimer import FakeTimer

fakeTimer = FakeTimer()

class Blobber:
    def __init__(self, __radius = float, __height = float, __color = str, __name = str):
        self.__radius = __radius
        self.__height = __height
        self.__color = __color
        self.__name = __name

    def getColor(self):
        return self.__color.lower()

    def setColor(self, color):
        self.__color = color
    
    def getName(self):
        return self.__name.capitalize()

    def setName(self, name):
        self.__name = name 

    def feedBlobber(self, amount = float):
        self.__radius += amount


    def blobberSpeak(self):
        string = ''
        string += "My name is " +  self.__name, ", and I am " + self.__color + "."
        string += "\nMy current happiness level is " + str() + "%"

    def vitalsOK(self):
        birthVolume = self.__radius **2 * 3.14 * self.__height
        increment = 0.2 * birthVolume
        time = round(fakeTimer.getElapsedTime())
        currentVolume = (birthVolume - (time * increment))

        happiness = abs(currentVolume / birthVolume)
        if 90 < happiness < 110:
            blobberOk = True
        else:
            blobberOk = False
        return happiness, blobberOk