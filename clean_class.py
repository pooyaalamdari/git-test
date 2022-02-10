class Animal:
    fur_color = 'Orange'

    def speak(self):
        raise NotImplementedError

    def eat(self):
        pass

    def chase(self):
        pass

class Tiger(Animal):

    fur_color = 'Black'




#type(tiger) -> Tiger Class
#NOT Animal class
tiger = Tiger()
tiger.speak()
