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
        return Response(response)

    def get(self, request):
        response = {"status" : "ok"}
        return Response(response)

class PayOrder(APIView):

    def post(self, request):
        json_data = json.loads(request.body)
        orderId = json_data["orderId"]
        pin = json_data["pin"]
        # customer = request.user()
        customer_id = 1

        # Validate some fake PIN
        print pin
        if pin != "123456":
            response = {"message": "invalid PIN"}
            return Response(data = response, status=400)

        # Insert whatever BRI API here
        order = Order.objects.get(id = orderId)
        order.status = "Completed"
        order.save()
        response = {
                      "status": "ok",
                   }
        return Response(response)

    def get(self, request):
        response = {"status" : "ok"}
        return Response(response)

class CheckOrderStatus(APIView):

    def get(self, request):
        order = Order.objects.get(id = request.GET.get('id', ''))
        response = {"orderStatus" : order.status}
        return Response(response)

class OrderHistory(APIView):

    def get(self, request):
        orders = Order.objects.filter(status='Completed').order_by('-created_at')
        orderHistory = []
        for order in orders:
            data = {
                "id": order.id,
                "totalPrice": order.total_price,
                "date": order.created_at
            }
            orderHistory.append(data)
        response = {"orderHistory" : orderHistory}
        return Response(response)