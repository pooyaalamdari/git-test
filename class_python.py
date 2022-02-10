

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


the_animal = Animal()
print(the_animal.property_1['key_1'])
print(the_animal.this_list)
print(the_animal.this_list[0])
print(the_animal.this_list[:2])
#we can access PUBLIC property directly with class name
print(Animal.this_list)

#how to use private property ?
#use underline sign _this_list
#we cant access directly (with class name)


#(self) in python (this) in js and ($this->) in php
