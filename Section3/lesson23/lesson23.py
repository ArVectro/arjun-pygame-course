class German():
    def speak(self):
        print("Speaking...")

class French():
    def speak():
        print("Speaking...") # How do we do this only once? There are many languages

class human():
    def speak(self):
        print("Speaking...")

class Italian(human): # the class Italian inherits the methods of the class human
    pass # Since we can't have nothing in our class, we add a pass

class Indian(human):
    pass

Rohan = Italian()
Rohan.speak()