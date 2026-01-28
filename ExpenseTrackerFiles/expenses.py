from user import User
from filewriter import FileWriter

class Expenses:

    def __init__(self, person):
        self.person = person
        self.expenses = []
        self.total = 0.0

    def set_total(self, amount): 
        self.total += amount
        
    def get_total(self):
        print(self.total)
    
    def print_welcome(self):
        print("=" * 50)
        print("     Welcome to the Expense Tracker".center(50))
        print("=" * 50)
        print(f"Hello {self.person.name},\n\nHere is a list of things you can do:\n\n  1. Add an expense\n  2. View all expenses\n  3. Get total expenses\n  4. Exit\n\n" + "=" * 50)

        while True:
            try:
                user_input = int(input("Enter 1-3 to navigate(4 to exit): "))
                if user_input not in range(1,5):
                     raise ValueError("Number must be between 1 and 4.")
                elif user_input == 4:
                    print("You have exited the expense tracker")
                    break
                elif user_input == 1:
                    self.collect_expense()
                    self.menu_list()
                elif user_input == 2:
                    self.list_of_expenses()
                    self.menu_list()
                elif user_input == 3:
                    self.print_total()
                    self.menu_list()
            except ValueError:
                print("Please enter a number 1-4.")
                
    
    def collect_expense(self):
        expense_amount = 1

        while expense_amount != 0:
            try:  
                expense_amount = float(input("Enter the expense amount(enter 0 to exit): "))
                if expense_amount == 0:
                    break
                elif expense_amount < 0:
                    print("Enter a positive number.")
                  
                
                expense_description = input("Enter description: ")
                expense_type = input("Enter a type(credit/debit): ")
                while expense_type not in ["credit", "debit"]:
                    expense_type = input("Invalid input please enter a type(credit/debit): ")
                

                each_expense = {"amount" : expense_amount,
                          "description" : expense_description,
                          "type" : expense_type,
                          }
                self.set_total(expense_amount)
                self.expenses.append(each_expense)
                
            except ValueError:
                print("Please enter a number.")

    def list_of_expenses(self):
        method = input("Would you like to export your report to a json, txt, csv, or view in console(enter json, txt, csv, con): ")
        while method not in ["json", "txt","csv", "con"]:
            method = input("Would you like to export your report to a json, txt, csv, or view in console(enter json, txt, csv, con): ")
        
        if method == "con":        
            print("Here is the list of your expenses: ")
            print("Amount|Description|Credit/Debit")
            for expense in self.expenses:
                print(f"{expense['amount']}|{expense['description']}|{expense['type']}") 
            return
        
        writer = FileWriter()
        if method == "json":
                    writer.write_json(self.expenses,self.total)
        elif method == "txt":
                    writer.write_txt(self.expenses,self.total)
        else:
            writer.write_csv(self.expenses,self.total)
            

    def print_total(self):
        self.total = 0.0
        for expense in self.expenses:
            total += expense['amount']
        print(f"Expenses total: ${self.total}")

    def menu_list(self):
        print("***************************\n  1. Add an expense\n  2. View all expenses\n  3. Get total expenses\n  4. Exit\n***************************")