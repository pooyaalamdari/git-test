class Animal:
    fur_color = 'Orange'

    #1-at the first this code line was running :D
    def __init__(self, fur_color):
        self.fur_color = fur_color

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print('I am eating yum yum yum!')

    #by default -> Gazeller
    #2-then this code was run
    def chase(self, animal='Gazelle'):
        print('I am chasing', animal)

    def get_fur_color(self):
        print('Getting fur color: ', self.fur_color)

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

    #chase is (Animal class) method
    # animal is (Animal class) chase method's argument
    #3-at the last this code was run
    def chase(self,animal):
        super().chase(animal)
        print(animal,'was caught')

#type(tiger) -> Tiger Class
#NOT Animal class
tiger = Tiger('Grey')
tiger.get_fur_color()
