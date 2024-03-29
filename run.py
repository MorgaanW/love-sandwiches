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
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    get sales figures from the user
    """
    while True:
        print("please enter sales data from the last mnarket")
        print("data should be six numbers, serperated by commas")
        print("example: 10,20,30,40,50,60\n")

        data_str = input("enter your data here: ")
        
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("data is valid")
            break

def validate_data(values):
    """
    inside the try converts all string vales unto intergers.
    raises valueerror if strings cannot be converted into int,
    or if there arent exaclt 6 values.
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


data = get_sales_data()