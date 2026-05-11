class car():
    def set_detials(self,brand,color):
        self.brand = brand
        self.color = color
    
    def show_detials(self):
        print(f"This is car is a {self.color} {self.brand}" )

car1 = car()
car1.set_detials("Tesla","Red")

car2 = car()
car2.set_detials("BMW","Black")

car1.show_detials()
car2.show_detials()