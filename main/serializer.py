from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class About_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProduct
        fields = "__all__"

class About_CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Company
        fields = "__all__"

class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"

class Advice_itemSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Advice_item
        fields = "__all__"


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = "__all__"


class Fact_TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact_Title
        fields = "__all__"

class Fact_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact_item
        fields = "__all__"

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


