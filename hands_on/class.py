"""
This is how classes
are defined in Python
"""


class HelloWorld(object):

    # Acts like a Static Variable
    # Investigate more
    messages = ['Hi!']

    # Class constructor
    def __init__(self, name):
        # Member variable
        self.name = name
        print(f'Class Initialized with name: {self.name}!')

    # Class Method
    def greet(self):
        print('greet() function called!')
        print(f'Hello, {self.name}!')

    # Method Overloading
    def what_is_love(self, message=None):
        if message is None:
            print('Program: Baby don\'t hurt me!')
            print('Program: Baby don\'t hurt me!')
            print('Program: No more!')
        else:
            print(f'User: {message}')
            print('Program: Wow, you know it all!')

    # Print method Overriding
    def __str__(self):
        return f'My name is {self.name}'


"""
Execution
"""
myName = 'Ahmed ElMallah'
instance = HelloWorld(myName)
newInstance = HelloWorld('Fawzy')
instance.greet()

"""
Both instances of the HelloWorld Class refer
to the same messages list reference, Unless we explicitly 
reassigned the variable to a new list
"""
print(instance.messages)
instance.messages.append('Bye bye!')
# newInstance.messages = []
print(newInstance.messages)
print(instance.messages)

"""
Testing Overloading
"""
print()
print('Program: What\'s love?')
instance.what_is_love('Love is simply the name of our pursuit of wholeness!')
print()
print('Program: What\'s love?')
instance.what_is_love()

"""
Testing Overriding
"""
print()
print(instance)
