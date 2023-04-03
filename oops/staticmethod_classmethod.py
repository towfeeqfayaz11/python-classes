# staticmethod decorator
# classmethod decorator

class Car:
    # class variable
    wheels = 4
    def __init__(self, color, name):
        self.color = color
        self.name = name
    
    @classmethod
    def get_wheels(cls):
        return cls.wheels
    
    @staticmethod
    def greetFromCar():
        print("Welocome to your car")
    
    def get_color(self):
        print(self.get_wheels())
        return self.color

    def get_name(self):
        return self.name


obj1 = Car("red", "Audi")
obj2 = Car("blue", "Toyota")
obj3 = Car("white", "maruti")


# Car.get_wheels()


# obj1.greetFromCar()
# Car.greetFromCar()
# print(obj1.color, obj1.name, obj1.wheels)
# print(obj2.color, obj2.name, obj2.wheels)

# print(Car.wheels)
# print(Car.get_wheels())
# Car.greetFromCar()