#QUESTION 1
inventory = {
    "apple": {"price": 0.5, "stock": 100},
    "milk": {"price": 1.2, "stock": 50},
    "chicken": {"price": 1.0, "stock":30}}

#QUESTION 2
import math
def add_to_shopping_list():
    grocery_lists = []  
item = input("please add an item:")
quantity = int(input(f"Enter the quantity of {item}: "))
#wasnt sure on how to return the dict
grocery_lists = inventory.items()
print(grocery_lists)

#Question 3
def calculate_bill(inventory, shopping_list):
    bill = []

