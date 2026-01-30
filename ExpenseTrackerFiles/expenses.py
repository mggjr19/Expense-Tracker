from user import User
from filewriter import FileWriter
from apiretrieve import APIretriever

class Expenses:
    
    
    def __init__(self, person):
        self.person = person
        self.expenses = []
        self.total = 0.0

    #method to set the total
    def set_total(self, amount): 
        self.total += amount
    #method to get the total
    def get_total(self):
        print(self.total)
    
    #method that prints the welcome information
    #it also has a if elif statement that calls the other methods to perform the actions the user decides upon
    #it also will then print the menu list again after each action is exited to continue with the program
    def print_welcome(self):
        print("=" * 50)
        print("     Welcome to the Expense Tracker".center(50))
        print("=" * 50)
        print(
    f"Hello {self.person.name} with income of {self.person.annual_income},\n\n"
    "Here is a list of things you can do:\n"
    "  1. Exit.\n"
    "  2. Add an expense.\n"
    "  3. Get total expenses.\n"
    "  4. How much to save.\n"
    "  5. View all expenses.\n"
    "  6. View how much people spend in your income bracket.\n"
    + "=" * 50
)
        #main method for program
        #if elif statement that the user can perform actions and then exit those actions 
        #and perform more action if they choose
        while True:
            try:
                user_input = int(input("Enter 2-6 to navigate(1 to exit): "))
                if user_input not in range(1,7):
                     raise ValueError("Number must be between 1 and 6.")
                elif user_input == 1:
                    print("You have exited the expense tracker")
                    break
                elif user_input == 2:
                    self.add_expense()
                    self.menu_list()
                elif user_input == 3:
                    self.print_total()
                    self.menu_list()
                elif user_input == 4:
                    print(self.savings())
                    self.menu_list()
                elif user_input == 5:
                    self.list_of_expenses()
                    self.menu_list()
                elif user_input == 6:
                    data = APIretriever()
                    data.define_bracket(self.person.annual_income)
            except ValueError:
                print("Please enter a number 1-5.")
                
    #prints the menu for the user
    def menu_list(self):
        print(
    "***************************\n"
    "  1. Exit.\n"
    "  2. Add an expense.\n"
    "  3. Get total expenses.\n"
    "  4. How much to save per month.\n"
    "  5. View all expenses.\n"
    "  6. View how much people spend in your income bracket.\n"
    "***************************"
        )

    #method that asks the user for information about their expense as well
    #as the total of the expense, it then stores this as a dictionary
    #and is then append to the list that holds all the expenses
    def add_expense(self):
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

    #this prints out the list of expenses by the user choise of 
    #json, txt, csv, or console
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
            

    #method to print the total number for all expenses combined
    def print_total(self):
        self.total = 0.0
        for expense in self.expenses:
            self.total += expense['amount']
        print(f"Expenses total: ${self.total}")

    #method that allows the user to find out how much they have to save biweekly/monthly
    #over a year period to hit their defined goal
    def savings(self):
        while True:
            try:
                save = int(input("How much money would you like to save per year: "))

                per = input("Would you like to know how much you need to save every month (m) or every two weeks (tw): ").lower()
                if per not in ["m", "tw"]:
                    raise ValueError("Enter m for month or tw for two weeks.")
                
                if per == "m":
                    return f"Every month you would have to save {save / 12} to achieve your goal of {save}."
                else: 
                    return f"Every two weeks you would have to save {save / 26} to achieve your goal of {save}."
                
                
            except ValueError as e:
                print(f"Invalid input: {e}")

    
        
    