import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open(' love_sandwiches')

def get_sales_data():
    """
    Get sales input from the user
    """
    while True:
        print("Please enter sales data from the last market day")
        print("Data should be six numbers, separted by commas")
        print("Example 10,34,26,56,45,87\n")

        data_str = input("Enter your data here:")
        print(f"The data provided is {data_str}")

        sales_data = data_str.split(",")
       
        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data

def validate_data(values):
    """
    inside the try, converts all string values into integers
    Raises ValueError if strings cannot be converted
    or if there arnt exactly 6 values
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values requried, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data {e}, Please try again.\n")
        return False

    return True
"""
def update_sales_worksheet(data):

  #  Update sales worksheet, add new row with the list data provided
    
    print("updating sales worksheet....\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated successfully.\n")
"""
"""
def update_surplus_worksheet(data):

   # Update surplus worksheet, add new row with the list data provided

    print("updating sales worksheet....\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("surplus worksheet updated successfully.\n")
"""

def update_worksheet(data, worksheet):
    """
    Recives a list of integers to be inserted into a worksheet
    Update the relavent worksheet,with the data provided
    """
    print(f"updating {worksheet} worksheet....\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")





def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type

    The surplus is defined as the sales figure subtracted from the stock:
    -Positive surplus indicates waste
    -Negative surplus indicates extra made when stock was sold out.
    """
    print("calculating surplus data......\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
   
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

def get_last_5_entries_sales():
    """
    collects column of data from sales worksheet, 
    collecting the last 5 entries for each sandwich
    and returns the data as a list of lists.
    """
    sales = SHEET.worksheet("sales")
    columns = []
    for int in range(1,7):
        column = sales.col_values(int)
        columns.append(column[-5:])

    return cloumns

def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    





print("Welcome to love sandwiches data automation")
#main()
sales_columns = get_last_5_entries_sales()
