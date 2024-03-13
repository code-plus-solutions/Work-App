from rest_framework import serializers

from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"


class WorkerSerializerRegister(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ["name", "lastName", "phone", "password", "address", "city", "state"]
