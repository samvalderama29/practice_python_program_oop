# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# create a class 
# create a function inside the class that will sort out numbers ending in zero or in five
# make sure that only numbers that arent ending in 0 nor 5 gets printed

class NumberPrinter:
    def number_sorter():
        for i in range(0, 101):
            if i % 5 != 0:
                print(i)

number = NumberPrinter
number.number_sorter()