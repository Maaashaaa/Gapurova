class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print("Села")
    def roll_over(self):
        print("Перекатывается")
my_dog = Dog("willie",6)
print(my_dog.name)
print(my_dog.age)
my_dog = Dog ("lucy",3)
print(my_dog.name,my_dog.age)
