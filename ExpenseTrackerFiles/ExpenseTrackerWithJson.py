from user import User
from expenses import Expenses
from apiretrieve import APIretriever

data = APIretriever()

#getting user information (name and income)
username = input("Enter your name: ")

while True:
    try:
        income = float(input("Enter your annual income: "))
        break
    except ValueError:
        print("Enter your annual income as a number please. ")
 
user1 = User(username, income)
tracker = Expenses(user1)
tracker.print_welcome()




    