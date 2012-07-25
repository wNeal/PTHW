## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-an Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-an Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-an object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name):
        ## Employee has-a name
        self.name = name
        ## Employee has-a salary
        self.salary = salary

## Fish is-an object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")
## satan is-a Cat
satan = Cat("Satan")
## mary is-a Person
mary = Person("Mary")
## mary has-a satan
mary.pet = satan
## frank is-an Employee
frank = Employee("Frank", 120000)
## frank has-a rover
frank.pet = rover
## flipper is-a fish
flipper = Fish()
## crouse is-a salmon
crouse = Salmon()
## harry is-a halibut
harry = Halibut()
