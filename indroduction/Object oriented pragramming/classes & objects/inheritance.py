class Animal:
    def speak(self):
        print("Animals make sounds")

class Dogs(Animal):
    def bark(self):
        print("Dogs bark")


dog = Dogs()
dog.speak()
dog.bark()