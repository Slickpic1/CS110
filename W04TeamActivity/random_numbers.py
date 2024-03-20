#Import libraries
import random

def append_random_numbers(numbers_list, quantity = 1):
    for i in range(quantity):
        numbers_list.append(round(random.uniform(0,100),1))
    return

def main():
    #Create list of numbers
    numbers = [16.2,75.1,52.3]

    #Append one random number and print
    append_random_numbers(numbers)
    print(f"List after one append: {numbers}")

    #Append three numbers
    append_random_numbers(numbers,3)
    print(f"After three appended numbers: {numbers}")

    return

main()