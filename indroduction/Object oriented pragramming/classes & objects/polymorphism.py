"""
one name , many forms

run 
persion can run fast 
car run on petrol
computer program run smoothly 

1 word = run 

#polymorphism with classes method overrding 
"""

class Bird():
    def sound(self):
        print("Birds make sounds")

class Crow(Bird):
    def sound(self):
        print('Crow say "Caw Caw" ')

class Parrot(Bird):
    def sound(self):
        print('Parrot sounds , squawk')

bird1 = Crow()
bird2 = Parrot()



bird1.sound()
bird2.sound()