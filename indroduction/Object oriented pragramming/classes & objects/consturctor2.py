class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

Student1 = Student("subyyal",23,"A+")
Student2 = Student("zeshan",22,"B+")
print(Student1.name,Student1.age,Student1.grade)
print(Student2.name,Student2.age,Student2.grade)


"""
1- default constructor (self)
2- parameterized constructor (self,name,age)
3- constructor with default values (self, name="unknown",age=0)


"""