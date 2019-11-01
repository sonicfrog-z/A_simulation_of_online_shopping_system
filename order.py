from datetime import datetime


class Order:
    FILENAME = 'order_info.dat'

    def __init__(self, id, uid, items, total, address='default address'):
        self.id = id
        self.uid = uid
        self.order_time = datetime.now()
        self.order_item = items
        self.order_amount = total
        self.payment_status = 0
        self.shipping_status = 0
        self.shipping_address = address

    # def __str__(self):
    #     return '*Order id: {}\nUser id: {}\nOrder time: {}\n'.format(self.name, self.id, self.price / 100,
    #                                                                 self.description)
