class SecondAsExponentOfFirst:
    def __init__(self, first_number, second_number):
        self.first_number=first_number
        self.second_number=second_number
    
    def raise_to_the_second_number(self):
        result = self.first_number**self.second_number
        print("result:", result) #Print result