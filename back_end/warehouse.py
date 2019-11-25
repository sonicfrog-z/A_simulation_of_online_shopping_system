import sys
sys.path.append("..")
from business_service.inventory_service import InventoryService
from business_service.order_service import OrderService
from business_service.shipping_service import ShippingService


class Warehouse:
    INVENTORY_FILE = '../data/inventory_data.dat'

    def __init__(self):
        self.orders_need_ship = []
        self.inv_sv = InventoryService()
        self.od_sv = OrderService()
        self.sh_sv = ShippingService()
        self.order_info = self.od_sv.order_info

    def show_menu(self):
        print("+-----------------------------+")
        print("| ***Warehouse Management**** |")
        print("| 1) Show inventory           |")
        print("| 2) Modify inventory         |")
        print("| 3) Show orders need to ship |")
        print("| 4) Show all orders          |")
        print("| 5) Make shipments           |")
        print("| q) Exit to home             |")
        print("+-----------------------------+")

    def show_inventory(self):
        self.inv_sv.show_inventory()

    def modify_inventory(self):
        self.show_inventory()
        it_id = input('Enter the item id you want to modify: ')
        new_stock_number = input('Enter the new stock number: ')
        self.inv_sv.modify_inventory(it_id, new_stock_number)
        print('Inventory successfully changed.')

    def create_shipment(self):
        self.get_orders_need_ship()
        print('Enter order id you want to make shipment:')
        od_id = input('Order id: ')
        if od_id in self.orders_need_ship:
            self.sh_sv.create_shipment(od_id)
            print('Shipment is successfully created for order {}.'.format(od_id))
        else:
            print('In valid order id. Order is not exist, or does not need to ship.')

    def show_orders_need_ship(self):
        self.get_orders_need_ship()
        for order_id in self.orders_need_ship:
            self.print_order(order_id)

    def show_all_orders(self):
        for od_id in self.order_info:
            self.print_order(od_id)

    def get_orders_need_ship(self):
        self.orders_need_ship, _ = self.od_sv.order_filter(pay_status=1, shipping_status=0)

    def print_order(self, od_id):
        self.od_sv.print_order(od_id)


if __name__ == '__main__':
    whouse = Warehouse()
    # whouse.set_inventory()
    # whouse.save_inventory()
    # whouse.show_inventory()
    # whouse.modify_inventory()
    # print(whouse.item_dic)
    # whouse.get_orders_need_ship()
    # whouse.show_orders_need_ship()
    whouse.show_all_orders()
