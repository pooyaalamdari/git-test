class Animal:
    fur_color = 'Orange'

    def speak(self):
        print("Raaww")

    def eat(self):
        pass

    def chase(self):
        pass

class Tiger(Animal):
    def speak(self):
        print('They are GREEEAAAT')


#type(tiger) -> Tiger Class
#NOT Animal class
tiger = Tiger()
tiger.speak()
print(tiger.fur_color)
