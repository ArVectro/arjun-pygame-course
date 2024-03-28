class animals:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    def run(self):
        print("Running...")

    def eat(self):
        print("Eating...")

dog = animals()
dog.eat()
dog.breed = "poodle"
dog.age = 5
# instead of all this we can define this in our class
print(dog.age())

dog = animals('poodle', 'white')
print(dog.breed())