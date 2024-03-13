from rest_framework import serializers

from .models import Employer


class EmployersSerializerRegister(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = [ "name", "lastName", "phone", "password", "address", "city", "state"]


class EmployersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"
