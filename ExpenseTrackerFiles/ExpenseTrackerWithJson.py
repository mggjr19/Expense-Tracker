from user import User
from expenses import Expenses


username = input("Enter your name: ")


user1 = User(username)
tracker = Expenses(user1)
tracker.print_welcome()




    