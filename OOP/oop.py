class Human():
    def __init__(self, name:str, gender:str, age:int, blood: str):
        """This function is initializer (constructor). Valuse it require are mandatroy to supply"""
        self.name = name
        self.gender = gender
        self.age = age
        self.blood_group = blood

    def eat(self):
        print("{0} is eating.".format(self.name))

    def sleep(self):
        print(f"{self.name} is sleeping")


human1 = Human("Ali", "Male", 20, "O+")


print(human1.eat)
print(human1.sleep)