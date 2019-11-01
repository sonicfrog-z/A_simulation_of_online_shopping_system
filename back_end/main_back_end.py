from warehouse import Warehouse


def show_menu():
    print("+-----------------------------+")
    print("| ***Back END Control Panel** |")
    print("| *********Home Page********* |")
    print("| 1) Manage Warehouse         |")
    print("| 2) Mange Shipments          |")
    print("| q) Exit program             |")
    print("+-----------------------------+")


def run_warehouse():
    warehouse = Warehouse()
    while True:
        warehouse.show_menu()
        key = input('Enter your command: ')
        if key == 'q':
            break
        elif key == '1':
            warehouse.show_inventory()
        elif key == '2':
            warehouse.modify_inventory()
        elif key == '3':
            warehouse.show_orders_need_ship()
        elif key == '4':
            warehouse.create_shipment()


def run_shipments():
    pass


if __name__ == '__main__':
    while True:
        show_menu()
        key = input('Enter your command: ')
        if key == 'q':
            break
        elif key == '1':
            run_warehouse()
        elif key == '2':
            run_shipments()
