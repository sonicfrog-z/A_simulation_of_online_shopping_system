import sys

sys.path.append("..")
from business_service.order_service import OrderService


class OrderPage:
    FILENAME = 'order_data.dat'

    def __init__(self, uid):
        self.user_id = uid
        self.od_sv = OrderService()
        self.od_lst, total_amount = self.od_sv.order_filter(user_id=self.user_id) # user's order list :[odid, odid]

    def show_menu(self):
        print("+-----------------------------+")
        print("| ********Order Page********* |")
        print("| 1) Show order information   |")
        print("| 2) Check out                |")
        print("| q) Exit to home             |")
        print("+-----------------------------+")

    def show_order_info(self):
        if self.od_lst:
            print('Your order is listed as below:')
            for od_id in self.od_lst:
                self.__print_order(od_id)
        else:
            print('You don\'t have any order.')

    def __print_order(self, oid):
        print('========================================================================')
        print('Order id: {}\nOrder time: {}'
              .format(oid, self.od_sv.order_info[oid].order_time.strftime('%Y/%m/%d %H:%M:%S')))
        print('Shipping address: {}'.format(self.od_sv.order_info[oid].shipping_address))
        print('Order item:')
        for it_id in self.od_sv.order_info[oid].order_item:
            print('--> {}({}) * {}, ${}'
                  .format(self.od_sv.item_dic[it_id].name, it_id, self.od_sv.order_info[oid].order_item[it_id],
                          self.od_sv.item_dic[it_id].price * self.od_sv.order_info[oid].order_item[it_id] / 100))
        print('Order amount is: ${}'.format(self.od_sv.order_info[oid].order_amount / 100))
        print('Payment status: {}'.format(self.od_sv.order_info[oid].payment_status))
        print('Shipping status: {}'.format(self.od_sv.order_info[oid].shipping_status))
        print('========================================================================')

    def check_out(self):
        unpaid_order_lst, amount_need_to_pay = self.od_sv.order_filter(self.user_id, 0)
        if unpaid_order_lst:
            print('Your unpaid order(s) is/are listed as below:')
            for oid in unpaid_order_lst:
                self.__print_order(oid)
            print('Total amount need to pay for all orders: ${}'.format(amount_need_to_pay / 100))
            while True:
                k = input('Check out your order above. Enter y to confirm, enter n to cancel: ')
                if k == 'y':
                    self.od_sv.check_out(self.user_id, unpaid_order_lst, amount_need_to_pay)
                    print('Successfully check out.')
                    break
                elif k == 'n':
                    print('Check out canceled.')
                    break


if __name__ == '__main__':
    my_oder_page = OrderPage('1003')
    my_oder_page.show_order_info()
    # my_oder_page.check_out()
