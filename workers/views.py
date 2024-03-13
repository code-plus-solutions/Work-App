from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Worker
from .serializer import WorkerSerializerRegister, WorkerSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class Register(APIView):

    def is_exist(self, phone):
        return Worker.objects.filter(phone=phone).exists()

    def post(self, request, format=None):
        try:
            if self.is_exist(request.data['phone']):
                return Response({"error": "user already exist"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = WorkerSerializerRegister(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(WorkerSerializer(Worker.objects.get(phone=serializer.data['phone'])).data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "user is not valued"}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request, format=None):
        try:
            worker = Worker.objects.get(phone=request.data['phone'])
            if worker.password == request.data['password']:
                serializer = WorkerSerializer(worker, many=False)
                return Response(serializer.data)
            else:
                return Response({"error": "password is false"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "user not found"}, status=status.HTTP_404_NOT_FOUND)
