class Person:
    personCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.personCount +=1

    def displayPersonnumer(self):
        print ("Total person is %d person" % Person.personCount)

    def display(self):
        print ("Name:" + self.name + ",age: "+ str(self.age) )

class Police(Person):
    def __init__(self, name, age, salary):
        super().__init__(name,age)
        self.salary = salary
    def display(self):
        print("Name:" + self.name + ",age: " + str(self.age) + " has salary: " + str(self.salary))

person2 = Person("Le Thuy Duyen", 23)
police1 = Police("Le Duc Cuong",22,990)
police1.display()