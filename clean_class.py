class Animal:
    fur_color = 'Orange'

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print('I am eating yum yum yum!')

    #by default -> Gazeller
    def chase(self, animal='Gazelle'):
        print('I am chasing', animal)

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
    def chase(self,animal):
        super().chase(animal)
        print(animal,'was caught')

#type(tiger) -> Tiger Class
#NOT Animal class
tiger = Tiger()
tiger.chase('rabit') 
