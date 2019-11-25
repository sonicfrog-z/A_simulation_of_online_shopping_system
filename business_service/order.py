from datetime import datetime


class Order:
    FILENAME = 'order_info.dat'

    def __init__(self, id, uid, items, total, address='default address'):
        self.id = id
        self.uid = uid
        self.order_time = datetime.now()
        self.order_item = items
        self.order_amount = total
        # payment status: 0 unpaid, 1 paid
        self.payment_status = 0
        # shipping status: 0 not yet create shipment, 1 created shipment but not shipped, 2 shipped
        self.shipping_status = 0
        self.shipping_address = address

    # def __str__(self):
    #     return '*Order id: {oid}\nUser id: {uid}\nOrder time: {time}\nShipping address: {add}\n'.format(oid=self.id,self.name, self.price / 100,
    #                                                                 self.description)
