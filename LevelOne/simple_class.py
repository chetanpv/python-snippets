# Question:
# Define a class which has at least two methods:
#     getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class MyClass:
    def get_string(self):
        print "\nEnter something: "
        return raw_input()

    def print_string(self, string_input):
        print string_input.upper()

obj = MyClass()
myinput = obj.get_string()
obj.print_string(myinput)