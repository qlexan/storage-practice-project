
from modules.controller import Controller
import modules.storage as storage
def main():
    cont = Controller()
    storage.setup()
    cont.show_menu()

if __name__ == "__main__":
    main()