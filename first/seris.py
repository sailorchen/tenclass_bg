from rest_framework import serializers
from first.models import shop_user,menu,submenu


class PagerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = shop_user
        fields = "__all__"

class SubMenuSerialiser(serializers.ModelSerializer):
    class Meta:
        model = submenu
        fields = "__all__"

class MenuSerialiser(serializers.ModelSerializer):
    submenu = SubMenuSerialiser(read_only=True,many=True)
    class Meta:
        model = menu
        fields = "__all__"

