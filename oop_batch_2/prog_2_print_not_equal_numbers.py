# Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# Create a class
# Create a function that will ask the user to input two numbers
# Create a function with an if-else method inside to identify if the numbers are equal
# Print "Not Equal" if the numbers are different; otherwise, print "Invalid. Numbers are equal."

class NotEqualNumber:
    def user_num(self):
        try:
            self.num_1 = int(input('Enter a number: '))
            self.num_2 = int(input('Enter another number: '))
        except ValueError:
            print('Invalid. Please enter numbers only')
    def not_equal_num(self):
        if self.num_1 != self.num_2:
            print('Not Equal')
        else:
            print('Invalid. Numbers are equal.')

print_not_equal_num = NotEqualNumber()
print_not_equal_num.user_num()
print_not_equal_num.not_equal_num()