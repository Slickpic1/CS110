#Import Libraries
import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    #Create empty dictionary
    dictionary = {}
    #Open and parse through dictionary
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

def parse_string(user_input):
    #Parse through user name to remove dashed lines
    split_string = user_input.split("-")
    for split in split_string:
        output_string += split



def main():
    #variables
    filename = "students.csv"
    key_column_index = 0
    NAME_INDEX = 1

    #Create and store dictionary in main
    student_dict = read_dictionary(filename,key_column_index)

    #Ask user for an I-number
    I_number = input("Please input an I-Number: ")

    #Check to see if student is in the directory
    if I_number in student_dict:
        values = student_dict[I_number]
        name = values[NAME_INDEX]

        print(name)

    else:
        print("No such student.")


# Call main to start this program.
if __name__ == "__main__":
    main()