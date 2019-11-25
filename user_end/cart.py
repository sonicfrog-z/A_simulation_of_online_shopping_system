import pickle
import sys
sys.path.append("..")
from business_service.item import Item
from business_service.order_service import OrderService


class Cart:
    FILENAME = '../local_data/{}_cart_data.dat'

    def __init__(self, uid):
        self.user_id = uid
        self.cart_info = {}  # {itemid : quant, itemid : quant}
        self.item_dic = {}  # {item_id1 : <item1>, item_id2 : <item2>}
        self.load()

    def show_menu(self):
        print("+-----------------------------+")
        print("| *******Shopping Cart******* |")
        print("| 1) Show items in cart       |")
        print("| 2) Place your order         |")
        print("| 3) Clear your shopping cart |")
        print("| q) Exit to home             |")
        print("+-----------------------------+")

    def load_item(self):
        """load item detail to item_dic"""
        try:
            with open(Item.FILENAME, 'rb') as fin:
                self.item_dic = pickle.load(fin)
        except FileNotFoundError:
            return None

    def get_total(self):
        return sum(self.item_dic[key].price * self.cart_info[key] for key in self.cart_info)

    def show_cart(self):
        if self.cart_info:
            self.load_item()
            print('Your cart info is listed as below:')
            for key in self.cart_info:
                print('-->{}({}) * {}, ${}'
                      .format(self.item_dic[key].name, key, self.cart_info[key],
                              self.item_dic[key].price * self.cart_info[key] / 100))
            print('Your total amount is: ${}'.format(self.get_total() / 100))
        else:
            print('Your cart is empty.')

    def add_cart(self, item_id, num):
        if item_id in self.cart_info:
            self.cart_info[item_id] += num
        else:
            self.cart_info[item_id] = num

    def load(self):
        try:
            with open(self.FILENAME.format(self.user_id), 'rb') as fin:
                self.cart_info = pickle.load(fin)
        except FileNotFoundError:
            return None

    def save(self):
        with open(self.FILENAME.format(self.user_id), 'wb') as fout:
            pickle.dump(self.cart_info, fout)

    def place_order(self):
        self.show_cart()
        while True:
            k = input('Place your order above. Enter y to confirm, enter n to cancel: ')
            if k == 'y':
                os = OrderService()
                try:
                    os.create_order(self.user_id, self.cart_info, self.get_total())
                    self.clear_cart()
                    print('Order placed')
                except Exception as e:
                    print(e)
                    print('Place order failed.')
                break
            elif k == 'n':
                print('Order not placed')
                break

    def clear_cart(self):
        self.cart_info = {}
        self.save()


if __name__ == '__main__':
    mycart = Cart('1001')
    # mycart.add_cart('104', 3)
    # mycart.save()
    mycart.show_cart()
    # mycart.place_order()
