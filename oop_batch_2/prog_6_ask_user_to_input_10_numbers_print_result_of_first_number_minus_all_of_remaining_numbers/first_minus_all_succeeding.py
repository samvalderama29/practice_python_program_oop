class OneMinusAll:
    def __init__(self, first_number):
        self.first_number=first_number
        self.suceeding_numbers=[]
    
    def first_minus_succeeding(self):
        difference= self.first_number-total#subtract sum of the 9 numbers to the first number
        print("\ndifference:", difference) #Print their difference
    
    def total_of_succeeding(self):
        global total
        counter= 1
        total=0
        while counter!=10:#Ask user to input other 9 numbers
            print("\ninputted number:", counter)
            other_numbers=int(input("Enter another number:"))
            self.suceeding_numbers.append(other_numbers)
            counter= counter+1 
            total= total+other_numbers
        total=sum(self.suceeding_numbers)