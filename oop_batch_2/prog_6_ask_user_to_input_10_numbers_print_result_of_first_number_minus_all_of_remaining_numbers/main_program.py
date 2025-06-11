from first_minus_all_succeeding import OneMinusAll

if __name__ == "__main__":
    numbers=OneMinusAll(float(input("Enter a number:")))
    numbers.total_of_succeeding()
    numbers.first_minus_succeeding()