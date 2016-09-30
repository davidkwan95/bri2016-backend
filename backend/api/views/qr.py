import json
import qrcode  
import cStringIO
import base64

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import models
from django.core.urlresolvers import reverse

from backend.apps.shop.models import Product, Order

class QRCode(APIView):

    def get(self, request):
        order = Order.objects.get(id = request.GET.get('id', ''))
        encoded_string = self.generate_qrcode(order)
        response = {"image" : encoded_string}
        return Response(response)

    # return qrcode encoded to base64
    def generate_qrcode(self, order):
        lines = order.lines.all()
        order_lines = []
        for line in lines:
            product = {
                "productName": line.product.name,
                "quantity": line.quantity,
                "unitCost": line.unit_cost,
                "linePrice": line.line_price,
            }
            order_lines.append(product)

        data = {
            "orderId": order.id,
            "shopName": order.shop.name,
            "orderLines": order_lines,  
            "totalPrice": order.total_price
        }
        img = qrcode.make(json.dumps(data))
        buffer = cStringIO.StringIO()
        img.save(buffer)
        img_str = base64.b64encode(buffer.getvalue())
        return img_str