import qrcode  
import cStringIO
import base64

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import models
from django.core.urlresolvers import reverse  
from django.core.files.uploadedfile import InMemoryUploadedFile

class QRCode(APIView):

    def get(self, request):
        encoded_string = self.generate_qrcode()
        response = {"image" : encoded_string}
        return Response(response)

    # return qrcode encoded to base64
    def generate_qrcode(self):
        data = {
            "shop_id": 1,
            "product_upcs": ['ABC-1', 'ABC-2', 'ABC-3'],  
        }
        img = qrcode.make(data)
        buffer = cStringIO.StringIO()
        img.save(buffer)
        img_str = base64.b64encode(buffer.getvalue())
        return img_str