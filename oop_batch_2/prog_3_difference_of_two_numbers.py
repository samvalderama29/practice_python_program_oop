# Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

# Create a class
# Create a function that will ask the user to input two numbers
# Create a function that will calculate the difference of the two numbers

class DifferenceOfTwoNumbers:
    def user_num(self):
        try:
            self.num_1 = int(input('Enter the first number: '))
            self.num_2 = int(input('Enter the second number: '))
        except ValueError:
            print('Invalid input. Please enter numbers only.')
            self.user_num()
    
    def calculate_difference(self):
        difference = self.num_1 - self.num_2
        print(f'The difference between {self.num_1} and {self.num_2} is {difference}')
        
difference_numbers = DifferenceOfTwoNumbers()
difference_numbers.user_num()
difference_numbers.calculate_difference()