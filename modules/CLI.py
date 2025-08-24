from . import Item
from .classlib import Slot, Shelf
import os 
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cli_add():
    clear()
    print('\n ---------- \n')
    name = str(input("Enter product name: "))
    stock = int(input("Enter product stock: "))
    supplier = str(input("Enter product supplier: "))
    print('\n ---------- \n')
    return Item(name, supplier)

def cli_slot():
    clear()
    print('\n ---------- \n')
    id = int(input("Enter item id: "))
    stock = int(input("Enter product stock: "))
    name = str(input("Enter shelf: ").strip().capitalize())
    number = str(input("Enter slot number: "))
    print('\n ---------- \n')
    return Slot(stock=stock, shelf=name, number=number, id=id)

def cli_slot_choice():
    clear()
    print('\n ---------- \n')
    return str(input("Would you like to add a slot? (y/n): ").strip().lower())
    

def cli_shelf():
    clear()
    print('\n ---------- \n')
    shelf_name = str(input("Enter shelf name: "))
    return Shelf(shelf_name=shelf_name)

def cli_id():
    clear()
    print('\n ---------- \n')
    id = int(input("Please enter product id: "))
    print('\n ---------- \n')
    return id

def cli_show(item):
    clear()
    print("Product")
    print('\n ---------- \n')
    if not item: 
        print("(empty item)")
    for k, v in item.items():
        print(f"*{k}* : '{v}'")
    time.sleep(2)
    print('\n ---------- \n')
    
    
def cli_login():
    clear()
    print('\n ---------- \n')
    username = str(input("Please enter username: "))
    password = str(input("Please enter password: "))
    return username, password
    
def cli_main():
    clear()
    print('\n ---------- \n')
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Update Item")
    print("4. Show Item")
    print("5. Show all items")
    print("6. Show shelves")
    print("0. Exit")
    print('\n ---------- \n')
    try:
        return int(input("Select an option: "))
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("\n Exiting ...")
        

def cli_error(error):
    clear()
    print('\n ! ---------- ! \n')
    print(f"Error: {error}")
    print('\n ! ---------- ! \n')