
from modules.inventory.schemas import Item, Shelf, Slot
import os 
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cli_add():
    clear()
    print('\n ---------- \n')
    name = str(input("Enter product name: "))
    supplier = str(input("Enter product supplier: "))
    print('\n ---------- \n')
    return Item(name=name, supplier=supplier)


def cli_slot_choice():
    print('\n ---------- \n')
    return str(input("Would you like to add a slot? (y/n): ").strip().lower())

def cli_stock():
    print('\n ---------- \n')
    stock = int(input("Please enter item stock: "))
    return stock
    

def cli_shelf():
    clear()
    print('\n ---------- \n')
    shelf_name = str(input("Enter shelf name: "))
    return shelf_name

def cli_id(var):
    clear()
    print('\n ---------- \n')
    id = int(input(f"Please enter {var} id: "))
    print('\n ---------- \n')
    return id

def cli_show(item):
    print('\n ---------- \n')
    if not item: 
        print("(empty item)")
    elif isinstance(item, list):
        for i, j in enumerate(item):
            print(f"*{i}* : '{j}'")
        time.sleep(2)
    else:
        print(item)
    print('\n ---------- \n')
    input("Press enter to continue...")
    
def cli_show_shelf():
    print('\n ---------- \n')   
    choice = str(input("Enter which shelf you want to view: ").upper().strip())
    return choice
        
def cli_login():
    clear()
    print('\n ---------- \n')
    username = str(input("Please enter username: "))
    password = str(input("Please enter password: "))
    return username, password
    
def cli_main():
    clear()
    choices = {
        1: "Inventory",
        2: "Shelves",
        3: "Slots",
        4: "Items",
    }
    print('\n ---------- \n')
    for k, v in choices.items():
        print(f"{k}. {v}")
    print("0. Exit")
    print('\n ---------- \n')
    
    try:
        num = int(input("Select an option: "))
        if num == 0:
            sys.exit(0)
        state = choices[num]
        return state
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("\n Exiting ...")

def cli_inventory():
    clear()
    choices = {
        1: "Add item",
        2: "Show item",
        3: "Show all items",
        4: "Update item",
        5: "Delete item",
        6: "Add item to slot",
        7: "Back to dashboard"
    }
    print('\n ---------- \n')
    for k, v in choices.items():
        print(f"{k}. {v}")
    print("0. Exit")
    print('\n ---------- \n')
    
    try:
        num = int(input("Select an option: "))
        print(num)
        if num == 0:
            sys.exit(0)
        if num in choices:
            return num
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("\n Exiting ...")
        

def cli_error(error):
    clear()
    print('\n ! ---------- ! \n')
    print(f"Error: {error}")
    print('\n ! ---------- ! \n')