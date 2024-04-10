#Import Libraries
import csv
from datetime import datetime

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

def test_setup():
    PROCUDT_ID_INDEX = 0
    try: 
        #Check to see if the file that we are looking for exists
        open("products.csv")
        open("request.csv")

        #Check to see if our request has an invadil file
        products_dict = read_dictionary("products.csv",0)
        with open("request.csv","rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                #Get product id
                product_id = row[PROCUDT_ID_INDEX]
                products_dict[product_id]
                
    except FileNotFoundError as file_not_found_err:
        print("Error: missing file")
        print(file_not_found_err)
        return False
    
    except KeyError as key_error:
        print("Error: unknown product ID in the request.csv file")
        print(key_error)
        return False
    
    else:
        return True
    
def CalcSalesTax(subtotal):
    return subtotal*0.06

def calc_discount(subtotal):
    
    return subtotal*.10

def display_receipt(item_list,subtotal,total_quantity):
    store_name = "Inkom Emporium"

    #Find out the day of the week
    dt = datetime.now()
    day = dt.weekday()

    #Print out name of store and two newlines
    print(store_name,"\n")

    for item in item_list:
        print(item)

    print()  #another newline

    #Check to see if a discount can be applied
    if (day == 1 or day == 2):
        discount = calc_discount(subtotal)
        subtotal -= discount
        print(f"Discount amount: {discount:.2f}")

    #Calculate our salestax
    salestax = CalcSalesTax(subtotal)

    #Add up total
    total = subtotal + salestax

    #Print cost section
    print(f"Number of Items: {total_quantity}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {salestax:.2f}")
    print(f"Total: {total:.2f}")

    #Print thank you message
    print(f"Thank you for shopping at the {store_name}.")
    print(f"{dt:%A %I:%M %p}")

    #Print survey
    print("\n Want to win a genuine nuclear warhead?")
    print("Take our online survey for a chance to win at:")
    print("  www.psyop.gov/defnotentrpmnt")

    return

def main():
    #Define Indeces
    PROCUDT_ID_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    QUANTITY_INDEX = 1
    PRICE_INDEX = 2

    #Define variables
    total_quantity = 0
    subtotal = 0
    item_list = []

    #Check for errors
    if (test_setup() == False):
        return

    #Call read dictionary for products.csv
    products_dict = read_dictionary("products.csv",0)

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

            #Get product name, price, and quantity
            product_name = products_dict[product_id][PRODUCT_NAME_INDEX]
            product_price = float(products_dict[product_id][PRICE_INDEX])
            quantity = int(row[QUANTITY_INDEX])

            #Add quanitity to our total_quantity
            total_quantity += quantity

            #Calculate our subtotal and add to total_prive
            subtotal += quantity*product_price

            #Add item to our list
            item_list.append(f'{product_name}: {quantity} @ {product_price}')

    #Print our receipt
    display_receipt(item_list,subtotal,total_quantity)

    return

if __name__ == "__main__":
    main()