
class Animal:
    property_1 = {
        'key_1' : 'value_1'
    }

    this_list = ['kane','patrick','bob']

    def add_name(self,name):
        self.this_list.append(name)
        return self.this_list

    def this_is_a_method(self):
        print(self.this_list)

    @property
    def get_bob(self):
        return self.this_list[2]


the_animal = Animal()

#we ignor self but take name
the_animal.add_name('Rhubarb')
#because retun this_list
print(the_animal.this_list)
