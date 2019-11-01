import pickle
from item import Item
import os


class Warehouse:
    INVENTORY_FILE = '../data/inventory_data.dat'

    def __init__(self):
        self.inventory_dic = {}
        self.item_dic = {}
        self.orders_need_ship = {}
        self.load_inventory()
        self.load_item()

    def show_menu(self):
        print("+-----------------------------+")
        print("| ***Warehouse Management**** |")
        print("| 1) Show inventory           |")
        print("| 2) Modify inventory         |")
        print("| 3) Show orders need to ship |")
        print("| 4) Make shipments           |")
        print("| q) Exit to home             |")
        print("+-----------------------------+")

    def show_inventory(self):
        for key in self.inventory_dic:
            print('-->{}({}), stock number: {}'.format(self.item_dic[key].name, key, self.inventory_dic[key]))

    def get_inventory(self, item_id):
        return self.inventory_dic[item_id]

    def create_shipment(self):
        pass

    def show_orders_need_ship(self):
        self.get_orders_need_ship()
        for order_id in self.orders_need_ship:
            self.print_order(order_id)

    def get_orders_need_ship(self):
        result_orders = {}
        file_path_lst = []
        # get order file name list
        for root, dirs, files in os.walk('../data/order/'):
            for name in files:
                file_path_lst.append(os.path.join(root, name))
        # load each order file
        for filename in file_path_lst:
            try:
                with open(filename, 'rb') as fin:
                    result_orders.update(pickle.load(fin))
            except FileNotFoundError:
                return None
        # filter target order
        for key in result_orders:
            if result_orders[key].payment_status == 0 or result_orders[key].shipping_status != 0:
                del result_orders[key]
        self.orders_need_ship = result_orders

    def print_order(self, key):
        print('========================================================================')
        print('Order id: {}\nOrder time: {}'
              .format(key, self.orders_need_ship[key].order_time.strftime('%Y/%m/%d %H:%M:%S')))
        print('Shipping address: {}'.format(self.orders_need_ship[key].shipping_address))
        print('Order item:')
        for key_ in self.orders_need_ship[key].order_item:
            print('--> {}({}) * {}, ${}'
                  .format(self.item_dic[key_].name, key_, self.orders_need_ship[key].order_item[key_],
                          self.item_dic[key_].price * self.orders_need_ship[key].order_item[key_] / 100))
        print('Order amount is: ${}'.format(self.orders_need_ship[key].order_amount / 100))
        print('Payment status: {}'.format(self.orders_need_ship[key].payment_status))
        print('Shipping status: {}'.format(self.orders_need_ship[key].shipping_status))
        print('========================================================================')

    def set_inventory(self):
        self.inventory_dic = {'101': 1000, '102': 1000, '103': 1000, '104': 1000, '105': 1000, '106': 1000, '107': 1000,
                              '108': 1000, '109': 1000, '110': 1000}
        # self.inventory_dic = {'101': 0, '102': 0, '103': 0, '104': 0, '105': 0, '106': 0, '107': 0,
        #                       '108': 0, '109': 0, '110': 0}
        self.save_inventory()

    def modify_inventory(self):
        self.show_inventory()
        key = input('Enter the item id you want to modify: ')
        if key in self.inventory_dic:
            quant = input('Enter the new stock number: ')
            self.inventory_dic[key] = quant
            self.save_inventory()
        else:
            print('Invalid item id')

    def load_inventory(self):
        try:
            with open(self.INVENTORY_FILE, 'rb') as fin:
                self.inventory_dic = pickle.load(fin)
        except FileNotFoundError:
            return None

    def save_inventory(self):
        with open(self.INVENTORY_FILE, 'wb') as fout:
            pickle.dump(self.inventory_dic, fout)

    def load_item(self):
        """load item detail to item_dic"""
        try:
            with open('.' + Item.FILENAME, 'rb') as fin:
                self.item_dic = pickle.load(fin)
        except FileNotFoundError:
            return None


if __name__ == '__main__':
    whouse = Warehouse()
    # whouse.set_inventory()
    # whouse.modify_inventory()
    # whouse.save_inventory()
    # whouse.show_inventory()
    # print(whouse.item_dic)
    whouse.get_orders_need_ship()
    whouse.show_orders_need_ship()

