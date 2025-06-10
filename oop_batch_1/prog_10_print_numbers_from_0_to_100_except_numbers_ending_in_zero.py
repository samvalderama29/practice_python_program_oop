# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# create a class
# create a funtion inside the class that will be responsible for sorting out the numbers that ends with 0
# print the numbers that arent ending in 0

class NoZero:
    def zero_sorter():
        for i in range(1, 101):
            if i % 10 != 0:
                print(i)

no_zero = NoZero
no_zero.zero_sorter()
