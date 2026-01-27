from user import User
from filewriter import FileWriter

class Expenses:

    def __init__(self, person):
        self.person = person
        self.expenses = []

    def print_welcome(self):
        print("=" * 50)
        print("     Welcome to the Expense Tracker".center(50))
        print("=" * 50)
        print(f"Hello {self.person.name},\n\nHere is a list of things you can do:\n\n  1. Add an expense\n  2. View all expenses\n  3. Get total expenses\n  4. Exit\n\n" + "=" * 50)

        while True:
            user_input = int(input("Enter 1-3 to navigate(4 to exit): "))
            if user_input == 4:
                print("You have exited the expense tracker")
                break
            elif user_input == 1:
                self.collect_expense()
                self.menu_list()
            elif user_input == 2:
                self.list_of_expenses()
                self.menu_list()
            elif user_input == 3:
                self.expenses_total()
                self.menu_list()
                
    
    def collect_expense(self):
        
        while True:
            try:
                expense_amount = float(input("Enter the expense amount(enter 0 to exit): "))
                if expense_amount == 0:
                    break
                elif expense_amount < 0:
                    print("Enter a positive number")
                    continue
                
                expense_description = input("Enter description: ")
                expense_type = input("Enter a type(credit/debit): ")
                while expense_type not in ["credit", "debit"]:
                    expense_type = input("Invalid input please enter a type(credit/debit): ")
                expense_frequency = input("Enter a frequecy if applicable: ")

                each_expense = {"amount" : expense_amount,
                          "description" : expense_description,
                          "type" : expense_type,
                          "Frequency" : expense_frequency
                          }
                
                self.expenses.append(each_expense)
                return each_expense
                
                
            except ValueError:
                print("Please enter a number.")

    def list_of_expenses(self):
        method = input("Would you like a json or txt file(json or txt) report off your expenses: ")
        while method not in ["json", "txt", "no"]:
            method = input("Would you like a json or txt file(json or txt) report off your expenses: ")
        
        if method == "no":        
            print("Here is the list of your expenses: ")
            print("Amount|Description|Credit/Debit|Frequency")
            for expense in self.expenses:
                print(f"{expense['amount']}|{expense['description']}|{expense['type']}|{expense['Frequency']}") 
            return
        
        writer = FileWriter()
        if method == "json":
                    writer.write_json(self.expenses)
        elif method == "txt":
                    writer.write_txt(self.expenses)
            

    def expenses_total(self):
        total = 0.0
        for expense in self.expenses:
            total += expense['amount']
        print(f"Expenses total: ${total}")

    def menu_list(self):
        print("***************************\n  1. Add an expense\n  2. View all expenses\n  3. Get total expenses\n  4. Exit\n***************************")