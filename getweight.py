class Person:
    __weight = 0

    def setWeight(self, weight):
        if type(weight) == int and weight > 0:
            self.__weight = weight
        else:
            print("Du måste ange ett positivt heltal!")

    def getWeight(self):
        return self.__weight


p = Person()
p.setWeight(-2)
p.setWeight(70)
print(p.getWeight())
