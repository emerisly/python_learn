class Person:
    def __init__(self,name,age): # self -> this
        self.name = name
        self.age = age
    def printName(self):
        print(self.name)
    def printAge(p):
        print(p.age)
    def printObejct(self):
        print(self.name,self.age)

newPerson = Person("Emerald",18)
print(newPerson.name)
newPerson.printName()
newPerson.printAge()
newPerson.age=19
# del newPerson.age
newPerson.printObejct()

print()

class Student(Person):
    def __init__(self,name,age,school):
        # self.name = name
        # self.age = age
        # Person.__init__(self,name,age)
        super().__init__(name,age)
        self.school = school
    def printObejct(self):
        print(self.name,self.age,self.school)

studnet1 = Student("Tommy",13,"Cornell")
studnet1.printObejct()