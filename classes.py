class utensil:
    def __init__(self, type, material):
        self.type = type
        self.material = material

    def cut(self):
        if self.type == "knife":
            print("I am a knife, I will cut things. :))")
        elif self.type == "fork":
            print("I am a fork, I can cut soft things.")
        elif self.type == "spork":
            print("I am a spork and no one likes me for good reason. I can't cut.")
        else:
            print("I am not something that cuts well. I am a spoon :(")

    def pickup(self):
        if self.type == "spoon":
            print("I can pick lots of things up because I am a spoon. I scoop.")
        elif self.type == "fork":
            print("I can pick some things up because I am a fork. I stab.")
        elif self.type == "spork":
            print("I am a spork and I cant pick things up, or stab things! worst of both worlds.")
        else:
            print("I can't pick things up because I am not as cool as a fork or a spoon. I cry.")

class person:
    def __init__(self, __name, age, __height, __weight, __sex, __language = "English", nazi = False):
        self.__name = __name
        self.age = age
        self.__height = __height
        self.__weight = __weight
        self.__sex = __sex
        self.__language = __language
        self.nazi = nazi

    def speak(self):
        if self.__language == "English":
            print("Hello, I am " + self.__name + ".")
        elif self.__language == "Portuguese":
            print("Ola meu nome é " + self.__name + ".")

    def __giveAge(self):
        print("I am " + str(self.age) + " years old.")

    def giveWeight(self):
        print("I weigh " + str(self.__weight) + " lbs.")
    
    def setWeight(self, weight):
        self.__weight = weight
        print(self.__name + "'s weight set to " + str(self.__weight) + ".")

    def introduceSelf(self):
        print()
        self.speak()
        self.__giveAge()
        self.giveWeight()

adolf = person("Adolf Hitler", 56, 69, 180, "Male", "English", True)
ronaldo = person("Cristiano Ronaldo", 38, 74, 187, "Male", "Portuguese", False)

fork = utensil("fork", "plastic")
spoon = utensil("spoon", "wood")
knife = utensil("knife", "diamond")
spork = utensil("spork", "uranium")

adolf.introduceSelf()
ronaldo.introduceSelf()

print("\nnazi confirmed") if adolf.age == 5 else print("\nNot nazi")

ronaldo.setWeight(5)