
class Animal:
    property_1 = {
        'key_1' : 'value_1'
    }

    this_list = ['kane','patrick','bob']

    def add_name(self,name):
        self.this_list.append(name)
        #if we use print instead of return
        print (self.this_list)

    def this_is_a_method(self):
        print(self.this_list)

    @property
    def get_bob(self):
        return self.this_list[2]


the_animal = Animal()

# we can do this 
print(the_animal.add_name('alex'))
