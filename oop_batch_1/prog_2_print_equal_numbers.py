# Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

# Create a class
# Create a function that will ask the user to input two numbers
# Create a function with an if-else method inside to identify if the numbers are equal
# Print "Equal" if the numbers are the same; otherwise, print "Invalid. Numbers are not equal."

class EqualNumber:
    def user_num(self):
        try:
            self.num_1 = int(input('Enter a number: '))
            self.num_2 = int(input('Enter another number: '))
        except ValueError:
            print('Invalid. Please enter numbers only')
    def equal_num(self):
        if self.num_1 == self.num_2:
            print('Equal')
        else:
            print('Invalid. Numbers are not equal.')

print_equal_num = EqualNumber()
print_equal_num.user_num()
print_equal_num.equal_num()