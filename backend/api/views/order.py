import base64
import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import models
from django.core.urlresolvers import reverse

from backend.apps.shop.models import Product, Order, OrderLine

class CreateOrder(APIView):

    def post(self, request):
        json_data = json.loads(request.body)
        lines = json_data["lines"]
        order = Order(shop_id = 1, customer_id = 1, status='Pending', )
        order.save()
        total_price = 0
        for line in lines:
            product = Product.objects.get(code = line['code'])
            quantity = line["quantity"]
            unit_cost = line["unitCost"]
            line_price = unit_cost * quantity

            total_price += line_price
            order_line = OrderLine(order = order, product = product, quantity = quantity,\
                                     unit_cost = unit_cost, line_price = line_price)
            order_line.save()
        order.total_price = total_price
        order.save()

        response = {
                      "status": "ok",
                      "orderId": order.pk
                   }
        print response
        return Response(response)

    def get(self, request):
        response = {"status" : "ok"}
        return Response(response)