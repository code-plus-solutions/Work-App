from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import SmsServies
from .models import Sms
# Create your views here.


@api_view(['POST'])
def getSms(request):
    try:
        phone = request.data['phone']
        code = SmsServies.sendSms(phone)
        Sms.objects.get(phone=phone).delete()
        print(code)
        print(phone)
        Sms.objects.create(phone=phone, code=code)
        return Response({'code': code})
    except Exception as e:
        return Response({'error': str(e)})


@api_view(['POST'])
def checkSms(request):
    try:
        phone = request.data['phone']
        code = request.data['code']
        sms = Sms.objects.get(phone=phone)
        if sms.code == code:
            return Response({'status': True})
        return Response({'status': False})
    except Exception as e:
        return Response({'error': str(e)})