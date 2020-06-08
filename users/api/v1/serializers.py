from rest_framework import serializers
from users.models import WGWEtgrgtrt


class WGWEtgrgtrtSerializer(serializers.ModelSerializer):
    class Meta:
        model = WGWEtgrgtrt
        fields = "__all__"
