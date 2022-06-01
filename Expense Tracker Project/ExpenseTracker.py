# Expense Tracker - IN PROGRESS...

import datetime
import pyodbc

class Manage():
    # Class variables 
    categories = ["Mortgage/rent", "Homeowners or renters insurance", "Property tax", "Auto insurance", "Health insurance", "Out-of-pocket medical costs", "Life insuranceLife insurance", "Electricity and natural gas", "Water", "Sanitation/garbage", "Groceries, toiletries and other essentials", "Car payment", "Gasoline", "Public transportation", "Internet", "Cell phone and/or landline", "Student loan payments", "Other minimum loan payments", "Child support or alimony payments", "Child care"]

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






# Execute 
test = Manage()
test.add("2022-06-01", 21.99, "Internet", "Data Saturday Plovdiv - ticket")