from rest_framework import serializers
from homex.models import XXX


class XXXSerializer(serializers.ModelSerializer):
    class Meta:
        model = XXX
        fields = "__all__"
