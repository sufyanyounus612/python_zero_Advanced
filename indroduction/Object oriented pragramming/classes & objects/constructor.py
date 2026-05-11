"""
__init__() 

class Car:
    def set_detials(self,brand,color):
        self.brand = brand
        self.color = color

car1 =Car()
car1.set_detials("Tesla","Red")

print(car1.brand)
print(car1.color)


syntax
class Classname:
   def __init__(self,parameters1,parameter2)
          self.property1 = parameter1
          self.porperty2 = parameter2
__init__()constructor
self.property:


"""
class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
car1 = Car("Tesla","Red") #values automatically set
print(car1.brand , car1.color)


