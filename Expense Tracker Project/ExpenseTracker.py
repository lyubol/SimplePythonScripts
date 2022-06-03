# Expense Tracker - IN PROGRESS...

import datetime

class Manage():
    # Class variables 
    categories = ["Mortgage/rent", "Homeowners or renters insurance", "Property tax", "Auto insurance", "Health insurance", "Out-of-pocket medical costs", "Life insuranceLife insurance", "Electricity and natural gas", "Water", "Sanitation/garbage", "Groceries, toiletries and other essentials", "Car payment", "Gasoline", "Public transportation", "Internet", "Cell phone and/or landline", "Student loan payments", "Other minimum loan payments", "Child support or alimony payments", "Child care"]
    expenses = {}

    def __init__(self):
        print("Manage you expenses - Add/Delete")

    def add(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category 
        self.description = description 

        # Validate date input
        try:
            datetime.datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect date format. Use YYYY-MM-DD.")

        # Validate amount
        try:
            assert isinstance(self.amount, int) or isinstance(self.amount, float)
        except AssertionError:
            raise AssertionError("Incorrect data type (amount). Should be integer or float.")

        # Validate category
        try:
            assert self.category in Manage.categories
        except AssertionError:
            raise AssertionError(f"Category is not in the list of available categories: {Manage.categories}")

        # Add to expenses dictionary
        if len(Manage.expenses) == 0:
            next_expense_id = 1
            Manage.expenses[1] = [self.date, self.amount, self.category, self.description]
        else:
            next_expense_id = len(Manage.expenses) + 1
            Manage.expenses[next_expense_id] = [self.date, self.amount, self.category, self.description]

        print(f"The following expense has been added: {next_expense_id}: {Manage.expenses.get(next_expense_id)}")


    def delete(self, expense_id):
        print(f"The following expense has been removed: {expense_id}: {Manage.expenses.get(expense_id)}")
        Manage.expenses.pop(expense_id)



    def view(self, expense_id=None):
        
        try:
            assert expense_id == None or expense_id in Manage.expenses.keys()
        except AssertionError:
            raise AssertionError(f"Expense with the followiing id does not exist. Id: {expense_id}")

        if expense_id == None:
            print(Manage.expenses)
        else:
            print(f"{expense_id}: {Manage.expenses.get(expense_id)}")



# Execute 
test = Manage()
test.add("2022-06-01", 21.99, "Internet", "Data Saturday Plovdiv - ticket")
test.add("2022-06-03", 15.60 ,"Groceries, toiletries and other essentials" ,"")
test.add("2022-06-04", 2.89 ,"Groceries, toiletries and other essentials" ,"Milk")
test.delete(1)
test.view()