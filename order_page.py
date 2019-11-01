from order import Order
from item import Item
import pickle


class OrderPage:
    FILENAME = 'order_data.dat'

    def __init__(self, uid):
        self.user_id = uid
        self.order_info = {}  # {orderid : order, orderid : order}
        # self.order_item = {}  # {itemid : quant, itemid : quant}
        self.item_dic = {}
        self.load()
        self.load_item()

    def show_menu(self):
        print("+-----------------------------+")
        print("| ********Order Page********* |")
        print("| 1) Show order information   |")
        print("| 2) Check out                |")
        print("| q) Exit to home             |")
        print("+-----------------------------+")

    def load_item(self):
        """load item detail to item_dic"""
        try:
            with open(Item.FILENAME, 'rb') as fin:
                self.item_dic = pickle.load(fin)
        except FileNotFoundError:
            return None

    def show_order_info(self):
        if self.order_info:
            print('Your order is listed as below:')
            for key in self.order_info:
                self.print_order(key)
        else:
            print('You don\'t have any order.')

    def print_order(self, key):
        print('========================================================================')
        print('Order id: {}\nOrder time: {}'
              .format(key, self.order_info[key].order_time.strftime('%Y/%m/%d %H:%M:%S')))
        print('Shipping address: {}'.format(self.order_info[key].shipping_address))
        print('Order item:')
        for key_ in self.order_info[key].order_item:
            print('--> {}({}) * {}, ${}'
                  .format(self.item_dic[key_].name, key_, self.order_info[key].order_item[key_],
                          self.item_dic[key_].price * self.order_info[key].order_item[key_] / 100))
        print('Order amount is: ${}'.format(self.order_info[key].order_amount / 100))
        print('Payment status: {}'.format(self.order_info[key].payment_status))
        print('Shipping status: {}'.format(self.order_info[key].shipping_status))
        print('========================================================================')

    def load(self):
        try:
            with open('./data/order/' + self.user_id + '_' + self.FILENAME, 'rb') as fin:
                self.order_info = pickle.load(fin)
        except FileNotFoundError:
            return None

    def create_order(self, order_item, total):
        with open('./data/' + 'order_id_counter.txt', 'r+') as file:
            id_counter = int(file.read().strip()) + 1
            id_counter = str(id_counter)
            file.seek(0)
            file.write(id_counter)
        self.order_info[id_counter] = Order(id_counter, self.user_id, order_item, total)

    def save(self):
        with open('./data/order/' + self.user_id + '_' + self.FILENAME, 'wb') as fout:
            pickle.dump(self.order_info, fout)

    def check_out(self):
        unpaid_order_lst = []
        amount_need_to_pay = 0
        if self.order_info:
            print('Your unpaid order(s) is/are listed as below:')
            for key in self.order_info:
                if self.order_info[key].payment_status == 0:
                    self.print_order(key)
                    unpaid_order_lst.append(key)
                    amount_need_to_pay += self.order_info[key].order_amount
            if unpaid_order_lst:
                print('Total amount need to pay for all orders: ${}'.format(amount_need_to_pay / 100))
                while True:
                    k = input('Check out your order above. Enter y to confirm, enter n to cancel: ')
                    if k == 'y':
                        for key in unpaid_order_lst:
                            self.order_info[key].payment_status = 1
                        self.save()
                        print('Successfully check out.')
                        break
                    elif k == 'n':
                        print('Check out canceled.')
                        break
            else:
                print('You don\'t have any order to check out.')
        else:
            print('You don\'t have any order to check out.')


if __name__ == '__main__':
    my_oder_page = OrderPage('1001')
    my_oder_page.show_order_info()
    # my_oder_page.check_out()
