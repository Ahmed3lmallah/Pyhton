class Parent(object):
    def __init__(self):
        self.name = 'Dada'
        print('Parent Class Instantiated!')

    def identify_me(self):
        print(f'This is the {self.name} class')


class Child(Parent):
    def __init__(self):
        super().__init__()
        super(Child, self).identify_me()
        print('I\'m independent!')
        self.name = 'No Dada!'
        super(Child, self).identify_me()

    def identify_me(self):
        print(f'This is the child class')


class FathersSon(Parent):
    pass


"""
Execution
"""
# Parent Class
parentInstance = Parent()
parentInstance.identify_me()

# Child Class
print()
childInstance = Child()
childInstance.identify_me()

# Second Child Class
print()
secondChildInstance = FathersSon()
secondChildInstance.identify_me()