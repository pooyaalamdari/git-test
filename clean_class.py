class Animal:
    fur_color = 'Orange'

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print('I am eating yum yum yum!')

    def chase(self):
        pass

class Tiger(Animal):

    fur_color = 'Black'

    def eat(self):
        #if we want to run eat method in Animal class
        #then eat method in Tiger class
        #super().eat()
        #we can use self in super().eat(self)
        #execute Animal class and eat method in Animal class
        super().eat()
        print('I am eating salmon')

#type(tiger) -> Tiger Class
#NOT Animal class
tiger = Tiger()
tiger.eat()
