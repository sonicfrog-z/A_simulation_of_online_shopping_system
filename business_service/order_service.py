from business_service.order import Order
from business_service.inventory_service import InventoryService
from business_service.item import Item
from business_service.user_service import UserService
import pickle
import os


class OrderService:
    FILENAME = os.path.join(os.path.dirname(__file__), '../data/order/order_data.dat')
    COUNTER_FILE = os.path.join(os.path.dirname(__file__), '../data/order_id_counter.txt')

    def __init__(self):
        self.order_info = {}  # {orderid : order, orderid : order}
        # self.order_item = {}  # {itemid : quant, itemid : quant}
        self.item_dic = {}
        self.load()
        self.load_item()
        self.user_sv = UserService()

    def load_item(self):
        """load item detail to item_dic"""
        try:
            with open(Item.FILENAME, 'rb') as fin:
                self.item_dic = pickle.load(fin)
        except FileNotFoundError:
            return None

    def load(self):
        try:
            with open(self.FILENAME, 'rb') as fin:
                self.order_info = pickle.load(fin)
        except FileNotFoundError:
            return None

    def save(self):
        with open(self.FILENAME, 'wb') as fout:
            pickle.dump(self.order_info, fout)

    def create_order(self, user_id, order_item, total):
        iv_sv = InventoryService()
        for it_id in order_item:
            stock_number = iv_sv.get_inventory(it_id)
            if order_item[it_id] > stock_number:
                raise Exception('Insufficient inventory for {}({}), {} in stock.'
                                .format(self.item_dic[it_id].name, it_id, stock_number))
        with open(self.COUNTER_FILE, 'r+') as file:
            id_counter = int(file.read().strip()) + 1
            id_counter = str(id_counter)
            file.seek(0)
            file.write(id_counter)
        self.order_info[id_counter] = Order(id_counter, user_id, order_item, total,
                                            self.user_sv.user_info[user_id].address)
        self.save()
        for it_id in order_item:
            iv_sv.reduce_stock(it_id, order_item[it_id])

    def order_filter(self, user_id=None, pay_status=None, shipping_status=None):
        result_order_lst = []
        amount_of_orders = 0
        if self.order_info:
            for key in self.order_info:
                if (self.order_info[key].uid == user_id if user_id is not None else True) \
                        and (self.order_info[key].payment_status == pay_status if pay_status is not None else True) \
                        and (
                        self.order_info[
                            key].shipping_status == shipping_status if shipping_status is not None else True):
                    result_order_lst.append(key)
                    amount_of_orders += self.order_info[key].order_amount
        return result_order_lst, amount_of_orders

    def check_out(self, user_id, unpaid_order_lst=None, amount_need_to_pay=None):
        if not unpaid_order_lst and not amount_need_to_pay:
            unpaid_order_lst, amount_need_to_pay = self.order_filter(user_id, 0)
        if unpaid_order_lst:
            for oid in unpaid_order_lst:
                self.order_info[oid].payment_status = 1
            self.save()

    def ready_to_ship(self, od_id):
        self.order_info[od_id].shipping_status = 1
        self.save()

    def delivered(self, od_id):
        self.order_info[od_id].shipping_status = 2
        self.save()

    def show_order_info(self):
        if self.order_info:
            for key in self.order_info:
                self.print_order(key)
        else:
            print('You don\'t have any order.')

    def print_order(self, oid):
        print('========================================================================')
        print('Order id: {}\nOrder time: {}'
              .format(oid, self.order_info[oid].order_time.strftime('%Y/%m/%d %H:%M:%S')))
        uid = self.order_info[oid].uid
        print('User id: {}\nUser name: {}'.format(uid, self.user_sv.user_info[uid].name))
        print('Shipping address: {}'.format(self.order_info[oid].shipping_address))
        print('Order item:')
        for it_id in self.order_info[oid].order_item:
            print('--> {}({}) * {}, ${}'
                  .format(self.item_dic[it_id].name, it_id, self.order_info[oid].order_item[it_id],
                          self.item_dic[it_id].price * self.order_info[oid].order_item[it_id] / 100))
        print('Order amount is: ${}'.format(self.order_info[oid].order_amount / 100))
        print('Payment status: {}'.format(self.order_info[oid].payment_status))
        print('Shipping status: {}'.format(self.order_info[oid].shipping_status))
        print('========================================================================')


if __name__ == '__main__':
    os = OrderService()
    os.show_order_info()
