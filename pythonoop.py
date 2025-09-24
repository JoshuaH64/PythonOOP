class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def get_human_years(self):
        return self.age * 7

    def info(self):
        print(f"{self.name} is {self.age} years old ({self.get_human_years()} in human years).")

# Create a Dog object
my_dog = Dog("Buddy", 4)
my_dog.bark()
my_dog.info()