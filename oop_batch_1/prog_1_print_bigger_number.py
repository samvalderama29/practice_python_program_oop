# Create a program that ask user to input 2 numbers. Print the bigger number.

# Ask the user to input two numbers
# Make a function that will compare the two numbers using if-else and determine which one is bigger
# Print the bigger number

class BiggerNumber:
    def user_num(self):
        self.num_1 = int(input('Enter a number: '))
        self.num_2 = int(input('Enter another number: '))
    def bigger_num(self):
        if self.num_1 > self.num_2:
            print(f'The bigger number is {self.num_1}')
        elif self.num_1 < self.num_2:
            print(f'The bigger number is {self.num_2}')
        else:
            print('Both numbers are equal. It is not possible to determine which one is bigger.')

print_big_num = BiggerNumber()
print_big_num.user_num()
print_big_num.bigger_num()