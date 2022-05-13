
import gspread
from google.oauth2.service_account import Credentials

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
    print("Please enter sales data from the last market day")
    print("Data should be six numbers, separted by commas")
    print("Example 10,34,26,56,45,87\n")

    data_str = input("Enter your data here:")
    print(f"The data provided is {data_str}")

    sales_data = data_str.split(",")
    validate_data(sales_data)

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

get_sales_data()

