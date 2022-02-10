

# class Animal:
#     property_1 = "something"
#
#
# the_animal = Animal()
# print(the_animal.property_1)

#2

class Animal:
    property_1 = {
        'key_1' : 'value_1'
    }

    this_list = ['kane','patrick','bob']

    def this_is_a_method(self):
        print(self.this_list)


the_animal = Animal()
#we ignore the self and we don't use in ()
the_animal.this_is_a_method()
