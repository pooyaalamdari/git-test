
class Animal:
    property_1 = {
        'key_1' : 'value_1'
    }

    this_list = ['kane','patrick','bob']

    def this_is_a_method(self):
        print(self.this_list)

    @property
    def get_bob(self):
        return self.this_list[2]


the_animal = Animal()
#we ignore the self and we don't use in ()
the_animal.this_is_a_method()

#because we use return
#we don't use ()
#the_animal -> is class
#get_bob -> is property
bob = the_animal.get_bob
print('the best person is',bob)
