# Press Shift+F10 to execute it or replace it with your code.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import basics


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


instance = basics.HelloWorld('Ahmed', 29)
instance.say_hi()
print(instance.name)
print(instance.age)

