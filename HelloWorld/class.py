class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printinfo(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear=year
    def printinfo(self):
        print(self.name,self.age,self.graduationyear)

class Teacher(Person):
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age


person1 = Person("Emerald", 17)
print(person1.name)
person1.age = 16
print(person1.age)
del person1.age
del person1
x = Student("Emerald", "17", 2019)
x.printinfo()
y = Teacher("Emerald", "Liu", "17")
y.printinfo()

class MyNumbers:
    def __iter__(self):
        self.a=1
        print("iter self.a",self.a)
        return self

    def __next__(self):
        x=self.a
        print("x",x)
        self.a+=1
        print("x",x)
        print("self.a",self.a)
        return x

myclass=MyNumbers()
myiter=iter(myclass)
next(myiter)
next(myiter)
next(myiter)


"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""