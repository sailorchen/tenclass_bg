from rest_framework import serializers
from first import models


class PagerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.shop_user
        fields = "__all__"