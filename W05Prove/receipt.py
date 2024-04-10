#Import Libraries
import csv

def read_dictionary(filename,key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    #Initialize compound dictionary
    dictionary = {}

    #Start our reader
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        #Skip the first line
        next(reader)

        #Read from the file
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

def main():
    #Define Indeces
    PROCUDT_ID_INDEX = 0
    QUANTITY_INDEX = 1
    PRICE_INDEX = 1

    #Call read dictionary for products.csv
    products_dict = read_dictionary("products.csv")

    #Opens and reads the request.csv file
    with open("request.csv","rt") as csv_file:
        reader = csv.reader(csv_file)

        #Skip the first line
        next(reader)

        #Loop through each row to find and print the print
        # the product name, quantity, and price
        for row in reader:

            #Get product id
            product_id = row[PROCUDT_ID_INDEX]

            #Get 
            products_dict[product_id]

    return

if __name__ == "__main__":
    main()