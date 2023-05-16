import time
from math import sqrt
class Blobber:
    def __init__(self, __radius = float, __height = float, __color = str, __name = str, __birthvol = float):
        self.__radius = __radius
        self.__height = __height
        self.__color = __color
        self.__name = __name
        self.__birthvol = __birthvol

    def increment(self):
        return self.__radius * 0.002

    def getColor(self):
        return self.__color

    def setColor(self, color = str):
        self.__color = color
    
    def getName(self):
        return self.__name

    def setName(self, name = str):
        self.__name = name

    def feedBlobber(self, amount = float):
        food = sqrt(amount / (3.14 * self.__height))
        print("food", food)
        self.__radius += food

    def timer(self):
        return time.time()

    def blobberSpeak(self, happiness):
        string = ''
        string += "My name is " +  self.__name + ", and I am " + self.__color + "."
        string += "\nMy current happiness level is " + format(happiness, ".2%") + "%"
        return string

    def vitalsOK(self, startTime, incrementer):
        elapsedTime = time.time() - startTime
        self.__radius -= elapsedTime * incrementer
        currentVolume = (self.__radius ** 2) * 3.14 * self.__height
        happiness = float(currentVolume / self.__birthvol)
        if happiness > 0.90 and happiness < 1.10:
            blobberOk = True
        else:
            blobberOk = False
        return happiness, blobberOk