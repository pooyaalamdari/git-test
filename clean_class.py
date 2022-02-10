class Animal:
    fur_color = 'Orange'

    def speak(self):
        print("Raaww")

    def eat(self):
        pass

    def chase(self):
        pass

class Tiger(Animal):
    pass

tiger = Tiger()
tiger.speak()
