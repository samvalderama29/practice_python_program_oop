class QuotientWithDecimal:
    def __init__(self,first_number, second_number):
        self.first_number=first_number
        self.second_number=second_number
    
    def divide(self): #Divide the two numbers
        result= self.first_number/self.second_number
        print("quotient:", result)#Print their quotient(with decimal)
