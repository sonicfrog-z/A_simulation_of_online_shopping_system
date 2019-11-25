from warehouse import Warehouse
from shipping_center import ShippingCenter


def show_menu():
    print("+-----------------------------+")
    print("| ***Back END Control Panel** |")
    print("| *********Home Page********* |")
    print("| 1) Manage Warehouse         |")
    print("| 2) Manage Shipments         |")
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
            warehouse.show_all_orders()
        elif key == '5':
            warehouse.create_shipment()


def run_shipments():
    shipping_center = ShippingCenter()
    while True:
        shipping_center.show_menu()
        key = input('Enter your command: ')
        if key == 'q':
            break
        elif key == '1':
            shipping_center.show_all_shipments()
        elif key == '2':
            shipping_center.show_pending_shipments()
        elif key == '3':
            shipping_center.set_to_finish()
        elif key == '4':
            shipping_center.set_all_finish()


if __name__ == '__main__':
    while True:
        show_menu()
        key = input('Enter your command: ')
        if key == 'q':
            print('Thanks for using Yabin\'s online shopping management program, bye bye.')
            break
        elif key == '1':
            run_warehouse()
        elif key == '2':
            run_shipments()
