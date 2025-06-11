# Create a program that ask user to input 2 numbers. Print the smaller number.

# Ask the user to input two numbers
# Make a function that will compare the two numbers using if-else and determine which one is smaller
# Print the smaller number

class SmallerNumber:
    def user_num(self):
        self.num_1 = int(input('Enter a number: '))
        self.num_2 = int(input('Enter another number: '))
    def smaller_num(self):
        if self.num_1 > self.num_2:
            print(f'The smaller number is {self.num_2}')
        elif self.num_1 < self.num_2:
            print(f'The smaller number is {self.num_1}')
        else:
            print('Both numbers are equal. It is not possible to determine which one is smaller.')

print_small_num = SmallerNumber()
print_small_num.user_num()
print_small_num.smaller_num()