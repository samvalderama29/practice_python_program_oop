class Remainder:
    def __init__(self, first_number, second_number):
        self.first_number=first_number
        self.second_number=second_number

    def modulo(self):
        remainder= self.first_number%self.second_number#Find their remainder
        print("remainder:", remainder)