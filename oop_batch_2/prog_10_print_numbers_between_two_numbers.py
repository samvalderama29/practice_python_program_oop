# Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# create a class
# ask user for two numbers
# add a function that will print out the numbers between those numbers

class PrintBetween:
    def __init__(self):
        self.user_input = None
        self.user_input_2 = None
    def swap_numbers(self):
        self.user_input = input('Enter a number: ')
        self.user_input_2 = input('Enter another number: ')
        if self.user_input >= self.user_input_2:
            self.user_input = self.user_input_2
            self.user_input_2 = self.user_input
    def number_in_between(self):
        for i in range(int(self.user_input) + 1, int(self.user_input_2)):
            print(i)


                
print_between = PrintBetween()
print_between.swap_numbers()
print_between.number_in_between()

