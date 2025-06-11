# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point.

# Create a class
# Create a function that will ask the user to input two numbers
# Create a function that will calculate the quotient of the two numbers without the decimal point

class QuotientWithoutDecimal:
    def user_num(self):
        try:
            self.num_1 = int(input("Enter the first number: "))
            self.num_2 = int(input("Enter the second number: "))
            if self.num_2 == 0:
                print("Division by zero is not allowed. Please enter a non-zero second number.")
                self.user_num()
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            self.user_num()
    
    def calculate_quotient(self):
        quotient = self.num_1 // self.num_2
        print(f"The quotient of {self.num_1} and {self.num_2} is {quotient}")