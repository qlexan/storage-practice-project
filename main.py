
from controller import Controller 
import storage

def main():
    cont = Controller()
    storage.setup()
    cont.show_menu()

if __name__ == "__main__":
    main()