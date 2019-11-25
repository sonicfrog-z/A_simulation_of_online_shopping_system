from datetime import datetime


class Shipment:
    def __init__(self, shipment_id, od_id, shipping_status):
        self.id = shipment_id
        self.create_time = datetime.now()
        self.od_id = od_id
        self.delivered_time = None
        # shipping status: 0 not created shipment, 1 created shipment, 2 delivered
        self.shipping_status = shipping_status

    def __str__(self):
        result = 'Shipment ID: {}\n' \
                 'Shipment Create Time: {}\n' \
                 'Oder ID: {}\n' \
                 'Delivered Time: {}\n' \
                 'Shipping Status: {}' \
            .format(self.id,
                    self.create_time.strftime('%Y/%m/%d %H:%M:%S'),
                    self.od_id,
                    self.delivered_time.strftime('%Y/%m/%d %H:%M:%S') if self.delivered_time else None,
                    self.shipping_status)
        return result
