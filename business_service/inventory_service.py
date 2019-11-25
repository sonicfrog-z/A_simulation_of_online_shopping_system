import pickle
from business_service.item import Item
import os


class InventoryService:
    INVENTORY_FILE = os.path.join(os.path.dirname(__file__), '../data/inventory_data.dat')

    def __init__(self):
        self.inventory_dic = {}
        self.item_dic = {}
        self.load_inventory()
        self.load_item()

    def get_inventory(self, item_id):
        return self.inventory_dic[item_id]['in_stock']

    # codes to init inventory data:
    # def set_inventory(self):
    #     self.inventory_dic = {
    #         '101': {'in_stock': 1000, 'for_ship': 0},
    #         '102': {'in_stock': 998, 'for_ship': 2},
    #         '103': {'in_stock': 1000, 'for_ship': 0},
    #         '104': {'in_stock': 998, 'for_ship': 2},
    #         '105': {'in_stock': 999, 'for_ship': 1},
    #         '106': {'in_stock': 999, 'for_ship': 1},
    #         '107': {'in_stock': 999, 'for_ship': 1},
    #         '108': {'in_stock': 999, 'for_ship': 1},
    #         '109': {'in_stock': 999, 'for_ship': 1},
    #         '110': {'in_stock': 999, 'for_ship': 1},
    #     }
    #     self.save_inventory()

    def modify_inventory(self, it_id, quant):
        try:
            if it_id in self.inventory_dic:
                self.inventory_dic[it_id]['in_stock'] = quant
                self.save_inventory()
            else:
                raise Exception('Invalid item id')
        except Exception as e:
            print(e)

    def reduce_stock(self, it_id, change):
        try:
            if it_id in self.inventory_dic:
                if self.inventory_dic[it_id]['in_stock'] >= change:
                    self.inventory_dic[it_id]['in_stock'] -= change
                    self.inventory_dic[it_id]['for_ship'] += change
                else:
                    raise Exception('Insufficient inventory for {}({}), {} in stock.'
                                    .format(self.item_dic[it_id].name, it_id, self.inventory_dic[it_id]['in_stock']))
                self.save_inventory()
            else:
                raise Exception('Invalid item id')
        except Exception as e:
            print(e)

    def reduce_num_for_ship(self, it_id, change):
        try:
            if it_id in self.inventory_dic:
                if self.inventory_dic[it_id]['for_ship'] >= change:
                    self.inventory_dic[it_id]['for_ship'] -= change
                else:
                    raise Exception('Insufficient for-ship stock number for {}({}), {} in stock.'
                                    .format(self.item_dic[it_id].name, it_id, self.inventory_dic[it_id]['for_ship']))
                self.save_inventory()
            else:
                raise Exception('Invalid item id')
        except Exception as e:
            print(e)

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
            with open(Item.FILENAME, 'rb') as fin:
                self.item_dic = pickle.load(fin)
        except FileNotFoundError:
            return None

    def show_inventory(self):
        for it_id in self.inventory_dic:
            stock_number = self.get_inventory(it_id)
            for_ship_number = self.inventory_dic[it_id]['for_ship']
            print('-->{}({}), stock number: {}, number for ship: {}'
                  .format(self.item_dic[it_id].name, it_id, stock_number, for_ship_number))


if __name__ == '__main__':
    ic = InventoryService()
    # ic.set_inventory()
    # ic.set_inventory()
    # ic.modify_inventory('102', 1)
    ic.show_inventory()
    # print(ic.get_inventory('102'))
