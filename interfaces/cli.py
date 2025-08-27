
from modules.inventory.inventory import Item, Slot, Shelf
import os 
import time
import sys

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
    print('\n ---------- \n')
    return stock, id

def cli_slot_choice():
    print('\n ---------- \n')
    return str(input("Would you like to add a slot? (y/n): ").strip().lower())
    

def cli_shelf():
    clear()
    print('\n ---------- \n')
    shelf_name = str(input("Enter shelf name: "))
    return shelf_name

def cli_id():
    clear()
    print('\n ---------- \n')
    id = int(input("Please enter product id: "))
    print('\n ---------- \n')
    return id

def cli_show(item):
    print('\n ---------- \n')
    if not item: 
        print("(empty item)")
    for k, v in item.items():
        print(f"*{k}* : '{v}'")
    time.sleep(2)
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
        state = choices[num]
        return state
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("\n Exiting ...")
        

def cli_error(error):
    clear()
    print('\n ! ---------- ! \n')
    print(f"Error: {error}")
    print('\n ! ---------- ! \n')